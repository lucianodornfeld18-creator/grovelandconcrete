# -*- coding: utf-8 -*-
from _data import BUSINESS

FAQS = [
    ("How thick should a concrete driveway be?",
     "Florida Building Code, Chapter 19, sets a 4-inch minimum for a slab-on-ground driveway. Most residential driveways in South Lake County are poured at 4–5 inches; areas that also carry an RV, boat trailer, or delivery trucks are typically taken to 5–6 inches with reinforcement sized for that load."),
    ("What PSI concrete should I use for a driveway in Florida?",
     "4,000 PSI is the standard call for Florida driveways, usually with about 5% air entrainment for freeze-thaw and durability margin. ACI 332 (the residential concrete standard) allows a range depending on exposure, but 4,000 PSI is the practical floor most installers and inspectors expect here."),
    ("Rebar or wire mesh — which is better for a concrete driveway?",
     "Rebar (commonly #3 or #4 bar on 12–18 inch centers) holds its position during the pour and keeps doing its job after hairline cracking starts. Wire mesh is lighter-duty and easy to push out of position while pouring, so it often ends up doing little once it's not centered in the slab. For anything carrying vehicle loads — including a standard driveway — rebar is the more reliable choice, and some jurisdictions won't accept wire mesh alone for a driveway."),
    ("Does Florida Building Code require a minimum driveway thickness?",
     "Yes. Chapter 19 sets 4 inches as the minimum for a residential slab-on-ground, with fiber reinforcement required in most slab-on-ground applications. A permit reviewer will check this, so it isn't optional design guidance — it's a code minimum."),
    ("What is the correct slope for a concrete driveway to drain properly?",
     "A minimum of about 1/8 inch of fall per foot (roughly 1%) is the standard reference for drainage, per long-standing concrete industry guidance (cement.org). Less than that and water tends to pool instead of running off, which is a common complaint on flat South Lake County lots."),
    ("How long before I can drive on a new concrete driveway?",
     "About 7 days for regular passenger vehicles, once the slab has reached roughly 70% of its design strength. Full-strength cure for heavier, stationary loads — like parking an RV — takes closer to 28 days. See our RV & Boat Pads page for why that distinction matters if you're planning to park something heavy."),
    ("Do I need a permit to pour a concrete driveway in Florida?",
     "In most cases, yes. A separate driveway/encroachment permit is often required specifically when you're cutting a new curb or connecting to a public road, in addition to any building permit for the slab itself. Skipping it can mean a stop-work order or a fine in the $500–$2,500 range in many Florida jurisdictions. Check our Permit Directory for the office that covers your address."),
]

def _faq_html():
    items = "\n".join(
        f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQS
    )
    return f'<div class="faq-list">{items}</div>'

def _faq_schema():
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in FAQS
        ],
    }

def get_pages():
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Concrete driveways are the core of what we cover — from a standard two-car approach to the long rural driveways that are common on South Lake County's larger lots. A long driveway isn't just a bigger version of a short one: it changes how the concrete is priced, how it's poured, and whether a mixer truck can even get to your house.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$4,500–$7,500</span><span class="lbl">Typical Florida driveway (published range)</span></div>
    <div class="stat-box"><span class="num">$6–$10</span><span class="lbl">Per sq ft, broom finish</span></div>
    <div class="stat-box"><span class="num">4"</span><span class="lbl">Florida Building Code minimum thickness</span></div>
    <div class="stat-box"><span class="num">4,000 PSI</span><span class="lbl">Standard Florida driveway mix</span></div>
  </div>
  <p class="calc-disclaimer">Ranges above reflect published Florida cost data as of this writing, not a quote for your project. For a driveway longer than a standard 60–80 ft approach, use the <a href="/tools/driveway-cost-calculator/">Driveway Cost &amp; Volume Calculator</a> instead — length changes the math more than most cost guides account for.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">The Long-Driveway Difference</span>
    <h2>What changes when your driveway isn't 60 feet long</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Pricing shifts from "per project" to "per foot"</h3>
        <p>Most cost guides quote a flat range for a standard two-car driveway. Once you're past roughly 100–150 feet, cost tracks much more closely with length and volume than with a generic square-footage average — see our <a href="/blog/long-driveway-cost-florida/">long driveway cost guide</a>.</p>
      </div>
      <div class="card">
        <h3>Truck access becomes a real question</h3>
        <p>A loaded mixer truck needs roughly 10–12 ft of clear width and 14 ft of vertical clearance to maneuver. On a long, narrow, or tree-lined rural approach, that's not guaranteed. Run through our <a href="/tools/site-access-checklist/">site-access checklist</a> before you assume a standard truck can reach the pour site.</p>
      </div>
      <div class="card">
        <h3>Base preparation matters more, not less</h3>
        <p>Central Florida's sandy soil compacts differently than clay-based soil, and a longer run of driveway means more opportunity for an inconsistent base to show up later as settling or cracking. See <a href="/blog/best-base-sandy-soil-florida/">base preparation on sandy Florida soil</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Specs That Matter</span>
    <h2>Thickness, strength, and reinforcement</h2>
    <p class="lede">These aren't marketing numbers — they're the specs a permit reviewer or inspector will actually check.</p>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Spec</th><th>Standard driveway</th><th>Heavier loads (RV/trailer parking)</th><th>Source</th></tr></thead>
      <tbody>
        <tr><td>Thickness</td><td>4–5 in (4 in code minimum)</td><td>5–6 in</td><td>Florida Building Code, Ch. 19</td></tr>
        <tr><td>Strength</td><td>4,000 PSI</td><td>4,000+ PSI</td><td>ACI 332 range; 4,000 PSI is the common Florida call</td></tr>
        <tr><td>Reinforcement</td><td>Rebar preferred over wire mesh</td><td>Rebar sized for load</td><td>Industry consensus; some jurisdictions restrict wire mesh</td></tr>
        <tr><td>Slope</td><td>~1/8 in per foot minimum</td><td>Same, verified toward drainage path</td><td>cement.org (American Cement Association) mix design guidance</td></tr>
        <tr><td>Cure before load</td><td>7 days (light vehicles)</td><td>28 days (heavy/stationary loads)</td><td>Standard concrete curing practice</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Common driveway questions</h2>
    {_faq_html()}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning a driveway project?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/driveway-cost-calculator/">Estimate cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()

    return [{
        "route": "/concrete-driveways/",
        "title": "Concrete Driveways in Groveland & South Lake County",
        "meta_description": "Standard and long concrete driveways for South Lake County — thickness, PSI, rebar, base prep, cost ranges, and real truck-access planning.",
        "h1": "Concrete Driveways",
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), ("Concrete Driveways", None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(), {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": "Concrete Driveways",
            "areaServed": "South Lake County, FL",
            "provider": {"@type": "Organization", "@id": "https://grovelandconcrete.com/#organization", "name": "Groveland Concrete", "url": "https://grovelandconcrete.com"},
        }],
    }]
