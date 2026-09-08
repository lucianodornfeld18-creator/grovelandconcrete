# -*- coding: utf-8 -*-
from _data import BUSINESS, PUBLIC_NAME
from templates import turnstile_html

def get_pages():
    pages = []

    # ---------------- About ----------------
    pages.append({
        "route": "/about/",
        "title": "About Groveland Concrete",
        "meta_description": "What Groveland Concrete is, how it works, and how your request is handled — no invented team, address, or history.",
        "h1": "About Groveland Concrete",
        "breadcrumbs": [("Home", "/"), ("About", None)],
        "nav_active": "/about/",
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px">
  <p class="lede">{BUSINESS['disclosure_short']}</p>

  <h2>What this site is</h2>
  <p>Groveland Concrete is an independent planning resource focused on one specific, underserved problem: concrete and hardscape projects on the large, rural, and semi-rural lots that make up Groveland and much of South Lake County. Long approaches, RV and boat storage, workshops and metal buildings, and sandy-soil drainage don't get real treatment on typical city-by-city contractor sites — this site exists to cover them properly.</p>

  <h2>What this site is not</h2>
  <p>We are not a general contractor, and we don't have a storefront, showroom, or crew of our own. We publish planning content, permit information, and calculators, and we route qualified requests to a licensed provider who actually serves your area. If a request needs to name that provider for legal or licensing reasons, we'll disclose that clearly before you submit any information — see our <a href="/privacy-policy/">Privacy Policy</a>.</p>

  <h2>Editorial standards</h2>
  <ul class="list-check">
    <li>We do not publish reviews, project counts, years-in-business claims, or licensing details we haven't verified.</li>
    <li>Technical claims (thickness, PSI, permit requirements, curing times) are sourced to the Florida Building Code, ACI/NRMCA industry guidance, or the relevant city/county — sources are linked where we cite a specific number.</li>
    <li>Where research could not confirm something (for example, a specific municipality's permit process for a niche project like a boat pad), we say so instead of guessing.</li>
    <li>We do not use "our crew," "we install," or "licensed contractor" language about ourselves — those claims belong to the provider who actually performs the work.</li>
  </ul>

  <h2>How a request is handled</h2>
  <p>When you call or submit the <a href="/contact/">contact form</a>, your information is forwarded to a provider serving your area so they can follow up about your project. We do not sell your contact information to third parties.</p>
</div>
''',
    })

    # ---------------- Contact ----------------
    pages.append({
        "route": "/contact/",
        "title": "Request a Free Estimate",
        "meta_description": "Tell us about your driveway, RV/boat pad, or slab project. Your request is routed to a provider serving Groveland and South Lake County.",
        "h1": "Request a Free Estimate",
        "breadcrumbs": [("Home", "/"), ("Contact", None)],
        "nav_active": "",
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px;display:grid;grid-template-columns:1.1fr .9fr;gap:48px">
  <div>
    <p class="lede">{BUSINESS['disclosure_form']}</p>
    <form class="lead-form" action="/api/contact" method="POST">
      <label class="hp" for="company">Company (leave blank)</label>
      <input class="hp" type="text" id="company" name="company" tabindex="-1" autocomplete="off">
      <input type="hidden" name="page_url" value="/contact/">
      <input type="hidden" name="utm_source" value="">
      <input type="hidden" name="utm_medium" value="">
      <input type="hidden" name="utm_campaign" value="">

      <div class="field">
        <label for="name">Full name</label>
        <input type="text" id="name" name="name" required maxlength="100">
      </div>
      <div class="field">
        <label for="phone">Phone number</label>
        <input type="tel" id="phone" name="phone" required maxlength="40">
      </div>
      <div class="field">
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required maxlength="254">
      </div>
      <div class="field">
        <label for="service">Service</label>
        <select id="service" name="service">
          <option value="">Not sure yet</option>
          <option>Concrete Driveways</option>
          <option>RV &amp; Boat Pads</option>
          <option>Workshop Slabs</option>
          <option>Concrete Patios</option>
          <option>Concrete Repair &amp; Resurfacing</option>
          <option>Sidewalks &amp; Walkways</option>
          <option>Paver Driveways</option>
          <option>Paver Patios</option>
          <option>Retaining Walls</option>
        </select>
      </div>
      <div class="field">
        <label for="city">City / area</label>
        <select id="city" name="city">
          <option value="">Select one</option>
          <option>Groveland</option>
          <option>Mascotte</option>
          <option>Minneola</option>
          <option>Howey-in-the-Hills</option>
          <option>Rural / unincorporated Lake County</option>
          <option>Other South Lake area</option>
        </select>
      </div>
      <div class="field">
        <label for="message">Tell us about your project</label>
        <textarea id="message" name="message" rows="5" maxlength="3000"></textarea>
      </div>
      <label style="display:flex;gap:10px;align-items:flex-start;font-size:.88rem;color:var(--ink-soft)">
        <input type="checkbox" name="consent" value="yes" required style="margin-top:4px">
        <span>I agree that my request may be forwarded to a licensed provider serving my area so they can contact me about this project.</span>
      </label>
      {turnstile_html()}
      <button class="btn btn-primary btn-lg" type="submit">Send request</button>
      <div class="form-msg" role="status" aria-live="polite"></div>
      <p class="form-note">Prefer to talk? Call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a> or email <a href="mailto:{BUSINESS['email_placeholder']}">{BUSINESS['email_placeholder']}</a>.</p>
    </form>
  </div>
  <aside class="card" style="align-self:start">
    <h3>What happens next</h3>
    <ol style="padding-left:20px;color:var(--ink-soft)">
      <li>Your request is checked and routed to a provider serving your city.</li>
      <li>They'll typically call or email within one business day.</li>
      <li>You'll get a real estimate based on your site — not a phone quote based on square footage alone.</li>
    </ol>
  </aside>
</div>
''',
    })

    # ---------------- Privacy ----------------
    pages.append({
        "route": "/privacy-policy/",
        "title": "Privacy Policy",
        "meta_description": "How Groveland Concrete collects, uses, and forwards the information you submit.",
        "h1": "Privacy Policy",
        "breadcrumbs": [("Home", "/"), ("Privacy Policy", None)],
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px">
  <p class="lede">Last updated: 2026-09-07.</p>
  <h2>What we collect</h2>
  <p>When you submit our contact form, we collect the information you provide (name, phone, email, service, city, and project details), plus basic technical data (page URL, referrer, and UTM parameters) used to route your request correctly. We do not use tracking pixels beyond standard, privacy-respecting analytics.</p>
  <h2>How we use it</h2>
  <p>{BUSINESS['disclosure_form']} We do not sell or rent your information to unrelated third parties.</p>
  <h2>Calls and texts</h2>
  <p>By providing your phone number and submitting the form, you consent to being contacted by phone, text, or email about your request. Calls may be recorded for quality and training purposes by the provider handling your request; if so, that will be disclosed at the start of the call.</p>
  <h2>Data retention</h2>
  <p>Submitted requests are retained only as long as needed to route and follow up on your inquiry, and are not stored in this site's own database — submissions are forwarded by email and are not logged with personal data in site analytics or public logs.</p>
  <h2>Contact</h2>
  <p>Questions about this policy: <a href="mailto:{BUSINESS['email_placeholder']}">{BUSINESS['email_placeholder']}</a>.</p>
</div>
''',
    })

    # ---------------- Terms ----------------
    pages.append({
        "route": "/terms/",
        "title": "Terms of Use",
        "meta_description": "Terms of use for grovelandconcrete.com.",
        "h1": "Terms of Use",
        "breadcrumbs": [("Home", "/"), ("Terms", None)],
        "body_html": '''
<div class="wrap" style="padding:0 0 60px">
  <p class="lede">Last updated: 2026-09-07.</p>
  <h2>Purpose of this site</h2>
  <p>Groveland Concrete publishes planning information, permit links, and calculators for concrete and hardscape projects in Groveland and South Lake County, Florida, and routes visitor requests to a provider serving that area. It is not itself a licensed contractor.</p>
  <h2>Estimates and calculators</h2>
  <p>Costs, thickness recommendations, and other figures shown on this site — including calculator results — are estimates for planning purposes only, based on published industry and local pricing ranges. They are not a quote, bid, or guarantee. A final price depends on a site visit and the provider's own assessment.</p>
  <h2>No professional advice</h2>
  <p>Content on this site is educational and does not replace advice from a licensed contractor, engineer, or your local building department for your specific project and jurisdiction.</p>
  <h2>Limitation of liability</h2>
  <p>This site is provided "as is." We are not liable for decisions made based on its content, or for the work performed by any provider your request is routed to.</p>
</div>
''',
    })

    # ---------------- Accessibility ----------------
    pages.append({
        "route": "/accessibility/",
        "title": "Accessibility Statement",
        "meta_description": "Our accessibility commitment and how to report an issue on grovelandconcrete.com.",
        "h1": "Accessibility Statement",
        "breadcrumbs": [("Home", "/"), ("Accessibility", None)],
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px">
  <p class="lede">We aim for this site to meet WCAG 2.2 Level AA: semantic headings, visible keyboard focus, sufficient color contrast, and labeled form fields.</p>
  <p>If you encounter a barrier using this site, tell us the page and what happened, and we'll fix it: <a href="mailto:{BUSINESS['email_placeholder']}">{BUSINESS['email_placeholder']}</a> or call {BUSINESS['phone_placeholder']}.</p>
</div>
''',
    })

    # ---------------- Thank you ----------------
    pages.append({
        "route": "/thank-you/",
        "title": "Thanks — Request Received",
        "meta_description": "Your request has been received.",
        "h1": "Thanks — we received your request",
        "noindex": True,
        "body_html": f'''
<div class="wrap status-page">
  <p class="lede" style="margin:0 auto">A member of the provider team serving your area will typically reach out within one business day. Need it sooner? Call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a>.</p>
  <p><a class="btn btn-outline" href="/">Back to homepage</a></p>
</div>
''',
    })

    # ---------------- 404 ----------------
    pages.append({
        "route": "/404/",
        "title": "Page Not Found",
        "meta_description": "The page you're looking for doesn't exist.",
        "h1": "That page doesn't exist",
        "noindex": True,
        "body_html": '''
<div class="wrap status-page">
  <p class="lede" style="margin:0 auto">Try the homepage, or jump to <a href="/services/">Services</a>, <a href="/service-area/">Service Area</a>, or <a href="/tools/">Tools</a>.</p>
  <p><a class="btn btn-primary" href="/">Back to homepage</a></p>
</div>
''',
    })

    return pages
