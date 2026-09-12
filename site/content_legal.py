# -*- coding: utf-8 -*-
from _data import BUSINESS, PUBLIC_NAME
from templates import turnstile_html, web3forms_fields
from _data import WEB3FORMS_ENDPOINT

def get_pages():
    pages = []

    # ---------------- About ----------------
    pages.append({
        "route": "/about/",
        "title": "About Groveland Concrete",
        "meta_description": "Groveland Concrete is a concrete and paving contractor serving Groveland and South Lake County — what we install, how we work, and what to expect when you call.",
        "h1": "About Groveland Concrete",
        "breadcrumbs": [("Home", "/"), ("About", None)],
        "nav_active": "/about/",
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px">
  <p class="lede">{BUSINESS['disclosure_short']}</p>
  <div class="trust-strip" style="margin:0 0 28px">{"".join(f'<span class="chip trust-chip">{t}</span>' for t in BUSINESS['trust_points'])}</div>

  <h2>Who we are</h2>
  <p>Groveland Concrete is a concrete and paving contractor built around one specific, underserved kind of property: the large, rural, and semi-rural lots that make up Groveland and much of South Lake County. Long approaches, RV and boat storage, workshops and metal buildings, and sandy-soil drainage don't get real treatment from typical city-by-city contractors — that is the work we set the company up to do well. Groveland is home base; from there our crews cover Mascotte, Minneola, Clermont, Montverde, Howey-in-the-Hills, and unincorporated Lake County as a service-area business.</p>

  <h2>What we install</h2>
  <ul class="list-check">
    <li>Concrete driveways — standard two-car approaches and long rural driveways, 4–6 inches, 4,000 PSI, rebar-reinforced.</li>
    <li>RV and boat pads and workshop slabs, sized and reinforced for the load that will actually sit on them.</li>
    <li>Concrete patios, sidewalks and walkways, repair and resurfacing.</li>
    <li>Paver driveways, paver patios, pool decks in marble, travertine and concrete pavers, entry steps and retaining walls.</li>
  </ul>

  <h2>How we work</h2>
  <ol style="padding-left:20px">
    <li><strong>Site walk first.</strong> We test the soil with a probe rather than judging it from the surface, measure the approach, and confirm a loaded mixer truck can reach and turn around on your lot.</li>
    <li><strong>Everything in writing.</strong> A line-itemized estimate with thickness, PSI, base spec, reinforcement, and joint plan on paper — not a phone quote by the square foot.</li>
    <li><strong>Permits handled up front.</strong> We tell you which office your job goes through (Groveland, Lake County, or Sumter County) before anything is scheduled.</li>
    <li><strong>Drainage you can see.</strong> Slope is built to the 1/8-inch-per-foot standard and hose-tested at handover.</li>
    <li><strong>Warranty and care guide.</strong> Every job closes with our workmanship warranty in writing plus a cure calendar, so you know exactly when it's safe to drive, park, or load.</li>
  </ol>

  <h2>Our standards</h2>
  <ul class="list-check">
    <li>Technical claims on this site (thickness, PSI, permit requirements, curing times) are sourced to the Florida Building Code, ACI/NRMCA industry guidance, or the relevant city/county — sources are linked where we cite a specific number.</li>
    <li>We do not publish reviews, project counts, or years-in-business figures we can't back up.</li>
    <li>Where something could not be confirmed (for example, a municipality's permit process for a niche project like a boat pad), we say so instead of guessing.</li>
  </ul>

  <h2>What happens when you call</h2>
  <p>Call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a> or send the <a href="/contact/">contact form</a>; we typically reply within one business day to set up a free site visit, and you'll have a written estimate shortly after. We do not sell your contact information to third parties.</p>
</div>
''',
    })

    # ---------------- Contact ----------------
    pages.append({
        "route": "/contact/",
        "title": "Request a Free Estimate",
        "meta_description": "Tell us about your driveway, RV/boat pad, slab, or paver project. Free written estimates from Groveland Concrete across Groveland and South Lake County.",
        "h1": "Request a Free Estimate",
        "breadcrumbs": [("Home", "/"), ("Contact", None)],
        "nav_active": "",
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px;display:grid;grid-template-columns:1.1fr .9fr;gap:48px">
  <div>
    <p class="lede">{BUSINESS['disclosure_form']}</p>
    <form class="lead-form" action="{WEB3FORMS_ENDPOINT}" method="POST">
      {web3forms_fields("/contact/", "New estimate request — Groveland Concrete (contact page)")}

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
      {turnstile_html()}
      <button class="btn btn-primary btn-lg" type="submit">Send request</button>
      <div class="form-msg" role="status" aria-live="polite"></div>
      <p class="form-note">Prefer to talk? Call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a> or email <a href="mailto:{BUSINESS['email_placeholder']}">{BUSINESS['email_placeholder']}</a>.</p>
    </form>
  </div>
  <aside class="card" style="align-self:start">
    <h2 class="card-title">What happens next</h2>
    <ol style="padding-left:20px;color:var(--ink-soft)">
      <li>We call or email back, typically within one business day, to set up a free site visit.</li>
      <li>On site we probe the ground, measure the approach, and check mixer-truck access.</li>
      <li>You get a written, line-itemized estimate — thickness, PSI, base, reinforcement — not a phone quote by the square foot.</li>
    </ol>
  </aside>
</div>
''',
    })

    # ---------------- Privacy ----------------
    pages.append({
        "route": "/privacy-policy/",
        "title": "Privacy Policy",
        "meta_description": "How Groveland Concrete collects and uses the information you submit.",
        "h1": "Privacy Policy",
        "breadcrumbs": [("Home", "/"), ("Privacy Policy", None)],
        "body_html": f'''
<div class="wrap" style="padding:0 0 60px">
  <p class="lede">Last updated: 2026-09-07.</p>
  <h2>What we collect</h2>
  <p>When you send us the contact form, we collect the information you provide (name, phone, email, service, city, and project details), plus basic technical data (page URL, referrer, and UTM parameters) used to follow up on your request correctly. We do not use tracking pixels beyond standard, privacy-respecting analytics.</p>
  <h2>How we use it</h2>
  <p>{BUSINESS['disclosure_form']} We do not sell or rent your information to unrelated third parties.</p>
  <h2>Calls and texts</h2>
  <p>By providing your phone number and submitting the form, you consent to being contacted by phone, text, or email about your request. Calls may be recorded for quality and training purposes; if so, that will be disclosed at the start of the call.</p>
  <h2>Data retention</h2>
  <p>Submitted requests are retained only as long as needed to follow up on your inquiry and to service the resulting job, and are not stored in this site's own database — submissions are delivered to our office by email and are not logged with personal data in site analytics or public logs.</p>
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
  <p>Groveland Concrete is a concrete and paving contractor serving Groveland and South Lake County, Florida. This site describes our services and publishes planning information, permit links, and calculators for concrete and hardscape projects in that area.</p>
  <h2>Estimates and calculators</h2>
  <p>Costs, thickness recommendations, and other figures shown on this site — including calculator results — are estimates for planning purposes only, based on published industry and local pricing ranges. They are not a quote, bid, or guarantee. A final price depends on a site visit and the written estimate we prepare for your project.</p>
  <h2>No professional advice</h2>
  <p>Planning content on this site is educational and does not replace a site visit, an engineer's review where one is required, or your local building department's requirements for your specific project and jurisdiction.</p>
  <h2>Limitation of liability</h2>
  <p>This site is provided "as is," and we are not liable for decisions made solely on the basis of its planning content or calculators. Work we perform is governed by the written estimate and workmanship warranty issued for that job.</p>
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
  <p class="lede" style="margin:0 auto">We'll typically reach out within one business day to set up your free site visit. Need it sooner? Call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a>.</p>
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
