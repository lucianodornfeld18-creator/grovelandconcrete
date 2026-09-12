# -*- coding: utf-8 -*-
from _data import BUSINESS, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, TOOLS
from templates import turnstile_html, web3forms_fields
from _data import WEB3FORMS_ENDPOINT
from _photos import home_strip

HOME_FAQS = [
    ("Do you serve my area?",
     "We're based in Groveland and work across South Lake County: Mascotte, Minneola, Clermont, Montverde, Howey-in-the-Hills and unincorporated Lake County. Call to confirm coverage for a rural address."),
    ("How much does a concrete driveway cost in Groveland?",
     "A standard driveway is priced by area, thickness, reinforcement and truck access; a long rural approach is priced by length. Our driveway calculator gives a planning range, and a free site visit turns it into a written, line-itemized estimate."),
    ("Do I need a permit for a driveway or slab?",
     "Usually yes for a new driveway, RV pad or slab. Groveland, unincorporated Lake County and Sumter County each handle it differently — we tell you which office your job goes through, and our permit directory links to each one."),
    ("How thick should an RV or boat pad be?",
     "5 to 6 inches of 4,000 PSI concrete with rebar, versus the 4-inch code minimum for a driveway, because a parked RV or boat trailer is a concentrated, stationary load rather than a rolling one."),
    ("How soon can you come out?",
     "We typically reply within one business day to set up a free site visit, and you'll have a written estimate shortly after. Light vehicles can use a new driveway after about 7 days; RVs and heavy loads after 28."),
]


def get_pages():
    services_cards = "\n".join(
        f'''<div class="card">
          <h3><a href="{SERVICES[s]["route"]}">{SERVICES[s]["name"]}</a></h3>
          <p>{SERVICES[s]["short"]}</p>
        </div>''' for s in SERVICE_ORDER
    )

    city_chips = "\n".join(
        f'<a class="chip" href="{CITIES[c]["route"]}">{CITIES[c]["name"]}</a>' for c in CITY_ORDER
    )

    body_html = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow">South Lake County, FL — Groveland · Mascotte · Minneola · Howey-in-the-Hills</span>
      <h1>Concrete planning for rural lots, long driveways, and RV &amp; boat pads.</h1>
      <p class="lede">Groveland Concrete is a concrete and paving contractor built for South Lake County's large lots — acreage, long approaches, and outbuildings. We pour and install driveways, RV and boat pads, workshop slabs, patios, pavers, pool decks, walkways and retaining walls, and we answer the questions a standard driveway page never does: can our mixer truck actually reach your house, how thick does a pad need to be for an RV or boat trailer, and what does the base need to look like on Central Florida sand. Fully insured. Free estimates. Written workmanship warranty.</p>
      <div class="cta-row">
        <a class="btn btn-primary btn-lg" href="tel:{BUSINESS['phone_tel_placeholder']}">Call {BUSINESS['phone_placeholder']}</a>
        <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
      </div>
    </div>
    <div class="hero-panel hero-form-panel">
      <h2 class="panel-title" style="margin-bottom:4px">Request a Free Estimate</h2>
      <p class="form-note" style="margin-bottom:16px">Tell us about your project — no obligation.</p>
      <form class="lead-form hero-form" action="{WEB3FORMS_ENDPOINT}" method="POST">
        {web3forms_fields("/", "New estimate request — Groveland Concrete (home page)", prefix="hero-")}

        <div class="field">
          <label for="hero-name">Full name</label>
          <input type="text" id="hero-name" name="name" required maxlength="100" placeholder="Full name">
        </div>
        <div class="field">
          <label for="hero-phone">Phone number</label>
          <input type="tel" id="hero-phone" name="phone" required maxlength="40" placeholder="Phone number">
        </div>
        <div class="field">
          <label for="hero-email">Email</label>
          <input type="email" id="hero-email" name="email" required maxlength="254" placeholder="Email">
        </div>
        <div class="field">
          <label for="hero-service">Service</label>
          <select id="hero-service" name="service">
            <option value="">Service needed…</option>
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
          <label for="hero-city">City / area</label>
          <input type="text" id="hero-city" name="city" maxlength="120" placeholder="City or ZIP">
        </div>
        {turnstile_html()}
        <button class="btn btn-primary btn-lg" type="submit" style="width:100%;justify-content:center">Get My Free Estimate</button>
        <p class="form-note" style="margin:6px 0 0;font-size:.74rem">By submitting, you agree Groveland Concrete may contact you about your project.</p>
        <div class="form-msg" role="status" aria-live="polite"></div>
      </form>
      <p class="form-note" style="margin-top:10px;text-align:center">Or call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a></p>
    </div>
  </div>
</section>

<section class="tight trust-wrap">
  <div class="wrap trust-strip">
    {"".join(f'<span class="chip trust-chip">{t}</span>' for t in BUSINESS['trust_points'])}
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Services</span>
    <h2>Concrete &amp; hardscape services for South Lake properties</h2>
    <p class="lede">Every service below is installed by our own crews — from a 4-inch reinforced driveway to a marble pool deck. Nothing on this list is subcontracted out or advertised without the equipment and people to do it.</p>
    <div class="grid grid-4" style="margin-top:26px">
      {services_cards}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Why Groveland Concrete</span>
    <h2>Built for large lots and long driveways, not subdivisions</h2>
    <div class="grid grid-3" style="margin-top:26px">
      <div class="card">
        <h3>We start with access</h3>
        <p>A loaded mixer truck weighs over 60,000 lb and needs room to turn around. Most contractors don't bring it up until pour day — we check it on the first site walk, because on 5+ acre rural lots it's often the first real question.</p>
      </div>
      <div class="card">
        <h3>RV and boat pads get their own specs</h3>
        <p>A pad built for a parked RV or boat trailer carries a different, more concentrated load than a driveway. We size and reinforce for that load instead of treating it as a smaller driveway.</p>
      </div>
      <div class="card">
        <h3>Honest permit guidance</h3>
        <p>Groveland, unincorporated Lake County, and neighboring Sumter County each handle driveway and slab permits differently. We tell you up front which office your job goes through, and our <a href="/permits/">permit directory</a> links to the real building department for each — no guessing.</p>
      </div>
    </div>
  </div>
</section>

{home_strip(6)}

<section>
  <div class="wrap">
    <span class="eyebrow">Featured Tool</span>
    <h2>Plan a long driveway before you call anyone</h2>
    <p class="lede">Our <a href="/tools/driveway-cost-calculator/">Driveway Cost &amp; Volume Calculator</a> estimates cubic yards and a cost range for a standard driveway or a long rural approach — using published Central Florida ready-mix pricing ranges, not a nationwide average.</p>
    <a class="btn btn-primary" href="/tools/driveway-cost-calculator/">Open the calculator</a>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Service Area</span>
    <h2>Groveland &amp; South Lake County</h2>
    <p class="lede">We're based in Groveland and work the rural and large-lot communities around it. Other South Lake cities may be reachable — call to confirm coverage for your address.</p>
    <div class="cta-row" style="margin-top:16px">{city_chips}</div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Questions</span>
    <h2>Straight answers before you call</h2>
    <div class="faq-list" style="margin-top:10px">
      {"".join(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in HOME_FAQS)}
    </div>
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Ready to plan your project?</h2>
    <p class="lede" style="margin:0 auto 20px">Tell us about your driveway, pad, slab, or paver project. We'll come out, probe the ground, check truck access, and put a line-itemized estimate in writing.</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="tel:{BUSINESS['phone_tel_placeholder']}">Call {BUSINESS['phone_placeholder']}</a>
    </div>
  </div>
</section>
'''.strip()

    return [{
        "route": "/",
        "is_home": True,
        "title": "Groveland Concrete | South Lake County Driveway, RV Pad & Slab Planning",
        "meta_description": "Groveland Concrete helps South Lake County property owners plan long driveways, RV/boat pads, and workshop slabs — with honest permit guidance and a real cost calculator.",
        "nav_active": "/",
        "body_html": body_html,
        "schema": [{
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQS],
        }, {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Groveland Concrete",
            "url": "https://grovelandconcrete.com",
            "publisher": {"@id": "https://grovelandconcrete.com/#organization"},
        }, {
            # Service-area business: no storefront address is published, so Organization (not LocalBusiness).
            "@context": "https://schema.org",
            "@type": "Organization",
            "@id": "https://grovelandconcrete.com/#organization",
            "name": "Groveland Concrete",
            "url": "https://grovelandconcrete.com",
            "logo": "https://grovelandconcrete.com/static/brand/png/logo-full-h400.png",
            "image": "https://grovelandconcrete.com/static/brand/png/og-default.jpg",
            "telephone": BUSINESS["phone_tel_placeholder"],
            "email": BUSINESS["email_placeholder"],
            "areaServed": [{"@type": "City", "name": CITIES[c]["name"]} for c in CITY_ORDER if CITIES[c]["kind"] != "area"] + [{"@type": "AdministrativeArea", "name": "Lake County, Florida"}],
            "description": BUSINESS["disclosure_short"],
        }],
    }]
