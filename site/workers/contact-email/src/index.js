const MAX_BODY_BYTES = 24_000;
const SENDER = "hello@grovelandconcrete.com"; // must match a verified Cloudflare Email Routing address

function clean(value, maxLength) {
  return typeof value === "string" ? value.trim().slice(0, maxLength) : "";
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function json(data, status = 200) {
  return Response.json(data, { status, headers: { "cache-control": "no-store" } });
}

function normalize(input) {
  return {
    hub_id: clean(input?.hub_id, 40) || "groveland",
    name: clean(input?.name, 100),
    phone: clean(input?.phone, 40),
    email: clean(input?.email, 254),
    service: clean(input?.service, 120),
    city: clean(input?.city, 120),
    message: clean(input?.message, 3_000),
    consent: !!input?.consent,
    page_url: clean(input?.page_url, 300),
    referrer: clean(input?.referrer, 300),
    utm_source: clean(input?.utm_source, 120),
    utm_medium: clean(input?.utm_medium, 120),
    utm_campaign: clean(input?.utm_campaign, 120),
    submittedAt: clean(input?.submittedAt, 40),
  };
}

function isValid(payload) {
  return (
    payload.name.length > 0 &&
    payload.phone.length > 0 &&
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(payload.email)
  );
}

function buildText(payload) {
  return [
    "New request from grovelandconcrete.com",
    "",
    `Hub: ${payload.hub_id}`,
    `Name: ${payload.name}`,
    `Phone: ${payload.phone}`,
    `Email: ${payload.email}`,
    `Service: ${payload.service || "Not specified"}`,
    `City: ${payload.city || "Not specified"}`,
    `Consent to be contacted: ${payload.consent ? "Yes" : "No"}`,
    `Page: ${payload.page_url || "Not recorded"}`,
    `Referrer: ${payload.referrer || "Direct/none"}`,
    `UTM: ${payload.utm_source || "-"} / ${payload.utm_medium || "-"} / ${payload.utm_campaign || "-"}`,
    `Submitted: ${payload.submittedAt || "Not recorded"}`,
    "",
    "Project details:",
    payload.message || "Not provided",
  ].join("\n");
}

function buildHtml(payload) {
  const rows = [
    ["Hub", payload.hub_id],
    ["Name", payload.name],
    ["Phone", payload.phone],
    ["Email", payload.email],
    ["Service", payload.service || "Not specified"],
    ["City", payload.city || "Not specified"],
    ["Consent", payload.consent ? "Yes" : "No"],
    ["Page", payload.page_url || "Not recorded"],
    ["Referrer", payload.referrer || "Direct/none"],
    ["UTM", `${payload.utm_source || "-"} / ${payload.utm_medium || "-"} / ${payload.utm_campaign || "-"}`],
    ["Submitted", payload.submittedAt || "Not recorded"],
  ]
    .map(
      ([label, value]) =>
        `<tr><th align="left" style="padding:6px 12px 6px 0">${escapeHtml(label)}</th><td style="padding:6px 0">${escapeHtml(value)}</td></tr>`,
    )
    .join("");

  return `<h1 style="font-size:20px">New request — Groveland Concrete</h1><table>${rows}</table><h2 style="font-size:16px">Project details</h2><p style="white-space:pre-wrap">${escapeHtml(payload.message || "Not provided")}</p>`;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (request.method !== "POST" || url.pathname !== "/send") {
      return json({ error: "Not found" }, 404);
    }

    const contentLength = Number(request.headers.get("content-length") || "0");
    if (contentLength > MAX_BODY_BYTES) return json({ error: "Request too large" }, 413);

    if (!env.CONTACT_DESTINATION) {
      console.error("CONTACT_DESTINATION secret is missing");
      return json({ error: "Email service is not configured" }, 503);
    }

    let input;
    try {
      input = await request.json();
    } catch {
      return json({ error: "Invalid JSON" }, 400);
    }

    const payload = normalize(input);
    if (!isValid(payload)) return json({ error: "Invalid contact data" }, 400);

    try {
      const result = await env.EMAIL.send({
        to: env.CONTACT_DESTINATION,
        from: { name: "Groveland Concrete", email: SENDER },
        replyTo: { name: payload.name, email: payload.email },
        subject: `New request${payload.city ? ` — ${payload.city}` : ""}`,
        text: buildText(payload),
        html: buildHtml(payload),
      });
      return json({ ok: true, messageId: result.messageId });
    } catch (error) {
      console.error("Cloudflare email send failed", { name: error instanceof Error ? error.name : "UnknownError" });
      return json({ error: "Email delivery failed" }, 502);
    }
  },
};
