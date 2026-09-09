// Cloudflare Pages Function — POST /api/contact
// Mirrors the proven pattern already running on windermereconcrete.com, plus
// Turnstile verification, hub_id attribution, and a best-effort KV rate limit.

const MAX_FORM_BYTES = 24_000;
const HUB_ID = "groveland";

const LIMITS = {
  name: 100,
  phone: 40,
  email: 254,
  service: 120,
  city: 120,
  message: 3_000,
  page_url: 300,
  utm_source: 120,
  utm_medium: 120,
  utm_campaign: 120,
};

function isAllowedOrigin(origin) {
  if (!origin) return true;
  try {
    const { hostname, protocol } = new URL(origin);
    if (protocol !== "https:" && hostname !== "localhost" && hostname !== "127.0.0.1") {
      return false;
    }
    return (
      hostname === "grovelandconcrete.com" ||
      hostname === "www.grovelandconcrete.com" ||
      hostname === "grovelandconcrete.pages.dev" ||
      hostname.endsWith(".grovelandconcrete.pages.dev") ||
      hostname === "localhost" ||
      hostname === "127.0.0.1"
    );
  } catch {
    return false;
  }
}

function field(form, name) {
  const value = form.get(name);
  return typeof value === "string" ? value.trim() : "";
}

function validate(payload) {
  if (!payload.name || payload.name.length > LIMITS.name) return "Please enter a valid name.";
  if (!payload.phone || payload.phone.length > LIMITS.phone) return "Please enter a valid phone number.";
  if (
    !payload.email ||
    payload.email.length > LIMITS.email ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(payload.email)
  ) {
    return "Please enter a valid email address.";
  }
  if (payload.service.length > LIMITS.service) return "Please select a valid service.";
  if (payload.city.length > LIMITS.city) return "Please select a valid city.";
  if (payload.message.length > LIMITS.message) return "The project description is too long.";
  return null;
}

function textResponse(message, status) {
  return new Response(message, {
    status,
    headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" },
  });
}

async function verifyTurnstile(token, secret, remoteip) {
  if (!secret) return { ok: true, skipped: true }; // not yet configured — see OWNER-INPUTS.md
  if (!token) return { ok: false };
  const body = new URLSearchParams({ secret, response: token });
  if (remoteip) body.set("remoteip", remoteip);
  try {
    const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      headers: { "content-type": "application/x-www-form-urlencoded" },
      body,
    });
    const data = await res.json();
    return { ok: !!data.success };
  } catch {
    return { ok: false };
  }
}

async function checkRateLimit(env, ip) {
  if (!env.RATE_LIMIT_KV || !ip) return true; // best-effort only — see OWNER-INPUTS.md
  const key = `rl:${ip}`;
  const count = Number((await env.RATE_LIMIT_KV.get(key)) || "0");
  if (count >= 5) return false; // 5 submissions / rolling 10 minutes per IP
  await env.RATE_LIMIT_KV.put(key, String(count + 1), { expirationTtl: 600 });
  return true;
}

export async function onRequestPost(context) {
  const { request, env } = context;
  const contentLength = Number(request.headers.get("content-length") || "0");

  if (contentLength > MAX_FORM_BYTES) return textResponse("This request is too large.", 413);
  if (!isAllowedOrigin(request.headers.get("origin"))) {
    return textResponse("This form submission is not allowed.", 403);
  }

  const contentType = request.headers.get("content-type") || "";
  if (
    !contentType.startsWith("application/x-www-form-urlencoded") &&
    !contentType.startsWith("multipart/form-data")
  ) {
    return textResponse("Unsupported form format.", 415);
  }

  let form;
  try {
    form = await request.formData();
  } catch {
    return textResponse("The form could not be read.", 400);
  }

  // Honeypot — real users never fill this in.
  if (field(form, "company")) {
    return Response.redirect(new URL("/thank-you/", request.url), 303);
  }

  const ip = request.headers.get("cf-connecting-ip") || "";
  const withinLimit = await checkRateLimit(env, ip);
  if (!withinLimit) {
    return textResponse("Too many requests. Please call us directly instead.", 429);
  }

  const turnstileToken = field(form, "cf-turnstile-response");
  const turnstile = await verifyTurnstile(turnstileToken, env.TURNSTILE_SECRET_KEY, ip);
  if (!turnstile.ok) {
    return textResponse("We could not verify this submission was made by a person. Please try again.", 403);
  }

  const payload = {
    hub_id: HUB_ID,
    name: field(form, "name"),
    phone: field(form, "phone"),
    email: field(form, "email"),
    service: field(form, "service"),
    city: field(form, "city"),
    message: field(form, "message"),
    // Consent is stated in the disclosure text next to every form ("By submitting,
    // you agree your request may be forwarded…"); submitting the form is the consent.
    consent: true,
    page_url: field(form, "page_url").slice(0, LIMITS.page_url),
    referrer: (request.headers.get("referer") || "").slice(0, LIMITS.page_url),
    utm_source: field(form, "utm_source").slice(0, LIMITS.utm_source),
    utm_medium: field(form, "utm_medium").slice(0, LIMITS.utm_medium),
    utm_campaign: field(form, "utm_campaign").slice(0, LIMITS.utm_campaign),
    submittedAt: new Date().toISOString(),
  };

  const error = validate(payload);
  if (error) return textResponse(error, 400);

  try {
    const result = await env.CONTACT_EMAIL.fetch("https://contact-email.internal/send", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
    });
    if (!result.ok) {
      console.error("Contact email service rejected the submission", { status: result.status });
      return textResponse("We could not send your request. Please call (352) 604-5480.", 502);
    }
  } catch (err) {
    console.error("Contact email service was unavailable", { name: err instanceof Error ? err.name : "UnknownError" });
    return textResponse("We could not send your request. Please call (352) 604-5480.", 502);
  }

  return Response.redirect(new URL("/thank-you/", request.url), 303);
}
