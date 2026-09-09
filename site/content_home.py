# -*- coding: utf-8 -*-
from _data import BUSINESS, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, TOOLS
from templates import turnstile_html
from _photos import home_strip

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
      <p class="lede">Groveland Concrete is a planning and request-routing resource for South Lake County property owners with acreage, long approaches, and outbuildings — not a generic city-by-city contractor directory. We focus on the questions a standard driveway page never answers: can a mixer truck actually reach your house, how thick does a pad need to be for an RV or boat trailer, and what does the base need to look like on Central Florida sand.</p>
      <div class="cta-row">
        <a class="btn btn-primary btn-lg" href="tel:{BUSINESS['phone_tel_placeholder']}">Call {BUSINESS['phone_placeholder']}</a>
        <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
      </div>
    </div>
    <div class="hero-panel hero-form-panel">
      <h3 style="margin-bottom:4px">Request a Free Estimate</h3>
      <p class="form-note" style="margin-bottom:16px">Tell us about your project — no obligation.</p>
      <form class="lead-form hero-form" action="/api/contact" method="POST">
        <label class="hp" for="hero-company">Company (leave blank)</label>
        <input class="hp" type="text" id="hero-company" name="company" tabindex="-1" autocomplete="off">
        <input type="hidden" name="page_url" value="/">
        <input type="hidden" name="utm_source" value="">
        <input type="hidden" name="utm_medium" value="">
        <input type="hidden" name="utm_campaign" value="">

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
        <label class="hero-consent" for="hero-consent">
          <input type="checkbox" id="hero-consent" name="consent" value="yes" required>
          <span>I agree my request may be forwarded to a provider serving my area.</span>
        </label>
        {turnstile_html()}
        <button class="btn btn-primary btn-lg" type="submit" style="width:100%;justify-content:center">Get My Free Estimate</button>
        <div class="form-msg" role="status" aria-live="polite"></div>
      </form>
      <p class="form-note" style="margin-top:10px;text-align:center">Or call <a href="tel:{BUSINESS['phone_tel_placeholder']}">{BUSINESS['phone_placeholder']}</a></p>
    </div>
  </div>
</section>

<section class="disclosure-wrap">
  <div class="wrap">
    <div class="disclosure-box">{BUSINESS['disclosure_short']}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Services</span>
    <h2>Concrete &amp; hardscape services for South Lake properties</h2>
    <p class="lede">Every service below is confirmed with a real provider serving this area — nothing here is advertised without a matching, staffed capability.</p>
    <div class="grid grid-4" style="margin-top:26px">
      {services_cards}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Why This Site Exists</span>
    <h2>Built for large lots and long driveways, not subdivisions</h2>
    <div class="grid grid-3" style="margin-top:26px">
      <div class="card">
        <h3>We start with access</h3>
        <p>A concrete mixer truck weighs over 60,000 lb loaded and needs room to turn around. Most driveway pages skip this entirely — we don't, because on 5+ acre rural lots it's often the first real question.</p>
      </div>
      <div class="card">
        <h3>RV and boat pads get their own specs</h3>
        <p>A pad built for a parked RV or boat trailer carries a different, more concentrated load than a driveway. We size and reinforce for that load instead of treating it as a smaller driveway.</p>
      </div>
      <div class="card">
        <h3>Honest permit guidance</h3>
        <p>Groveland, unincorporated Lake County, and neighboring Sumter County each handle driveway and slab permits differently. Our <a href="/permits/">permit directory</a> links to the real building department for each — no guessing.</p>
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
    <p class="lede">We focus on Groveland and the rural/large-lot communities around it. Other South Lake cities may be reachable — call to confirm before assuming coverage.</p>
    <div class="cta-row" style="margin-top:16px">{city_chips}</div>
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Ready to plan your project?</h2>
    <p class="lede" style="margin:0 auto 20px">Tell us about your driveway, pad, or slab project and we'll route your request to a provider who covers your area.</p>
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
            "@type": "WebSite",
            "name": "Groveland Concrete",
            "url": "https://grovelandconcrete.com",
        }],
    }]
