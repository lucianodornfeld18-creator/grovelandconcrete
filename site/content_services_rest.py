# -*- coding: utf-8 -*-
"""Remaining seven service pages for grovelandconcrete.com.

Matches the structure/rigor established in content_services_driveways.py:
stat-row headline numbers, a sourced spec table, FAQ via <details class="faq-item">
plus matching FAQPage JSON-LD, a "why this is different" section, and a disclaimer
before any cost figure. Section order is varied per page on purpose.
"""
from _data import BUSINESS, SERVICES


def _faq_html(faqs):
    items = "\n".join(
        f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs
    )
    return f'<div class="faq-list">{items}</div>'


def _faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def _service_schema(service_key):
    svc = SERVICES[service_key]
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": svc["name"],
        "areaServed": "South Lake County, FL",
        "provider": {"@type": "Organization", "@id": "https://grovelandconcrete.com/#organization", "name": "Groveland Concrete", "url": "https://grovelandconcrete.com"},
    }


def _disclosure():
    return f'<div class="disclosure-box">{BUSINESS["disclosure_short"]}</div>'


# ---------------------------------------------------------------------------
# 1. RV & Boat Pads
# ---------------------------------------------------------------------------

RV_BOAT_FAQS = [
    ("How much does a concrete RV pad cost?",
     "$1,800–$7,200 is the published national range for a concrete RV pad (concreteslabcost.com), depending on pad size, thickness, and site prep — it isn't a Florida-specific or site-specific figure. Pad size (your motorhome's length and width), base condition, and mixer-truck access all move the real number. Use the RV &amp; Boat Pad Calculator to size a pad to your rig, then request an estimate for a number specific to your lot."),
    ("How thick should a concrete pad be for an RV, and what PSI?",
     "6 inches at 4,000+ PSI is the consensus repeated across RV-focused concrete guides — thicker and stronger than the 4-inch Florida Building Code minimum and 4,000 PSI standard used for an ordinary driveway slab. The extra thickness accounts for a large motorhome's concentrated axle and jack weight sitting in one spot for weeks or months, not rolling through like a car."),
    ("Do I need rebar in an RV concrete pad?",
     "Yes — rebar sized for the load, not wire mesh, is the standard answer, same logic used for any heavy-load slab. Owners researching this on RV forums (Forest River Forums, iRV2) consistently land on rebar over mesh for anything meant to carry a parked motorhome's weight long-term."),
    ("How long do I have to wait before parking my RV or boat trailer on new concrete?",
     "About 28 days. Light vehicle traffic is generally fine around 7 days, once concrete reaches roughly 70% of its design strength, but a stationary heavy load — a parked RV or a boat sitting on a trailer — should wait for full cure. Pulling a loaded rig onto a pad before then risks surface damage the concrete hasn't caught up to yet."),
    ("RV pad vs. driveway — what's the real difference?",
     "A driveway carries a rolling load: weight that crosses the slab and is gone in seconds. An RV pad carries a concentrated load that parks and stays, sometimes for months at a time. That's why RV pads are typically built thicker (6 in vs. 4–5 in) and cured longer before use, even though the concrete mix itself isn't dramatically different."),
    ("How much does a concrete boat pad cost?",
     "Most published cost guides don't treat boat pads as their own category — they fold the pricing into RV pad or general slab numbers ($6–$12 per sq ft installed is the published general slab range). That's a real gap in the available data: a boat-and-trailer load on jack stands and wheels isn't identical to a motorhome's distributed axle weight. Treat RV pad figures as a starting reference, not a boat-specific quote, and request a site-specific number."),
    ("What's actually different between a boat pad and an RV pad?",
     "Both are typically built to a similar thickness and strength spec, but the load pattern differs — a boat trailer often concentrates weight on a few contact points (tongue jack, wheels, blocking) rather than spreading it the way a motorhome's axles do. South Lake County sits in lake country — Lake Louisa, Lake Minneola, Little Lake Harris — where boat-and-trailer storage is a routine ask that generic RV pad content doesn't address directly."),
    ("Do I need drainage or slope on a concrete boat pad?",
     "Yes — the same roughly 1/8-inch-per-foot minimum slope used on driveways applies here, and arguably matters more. A boat pad gets wet routinely from wash-down, rain, and a dripping hull, so water needs somewhere to go instead of sitting against a trailer frame or tires."),
]


def _page_rv_boat_pads():
    svc = SERVICES["rv-and-boat-pads"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">RVs and boats are both common on South Lake County's larger lots, and the concrete they sit on shares a lot of the same technical spec — but they aren't the same job. An RV parks and stays for a season; a boat-and-trailer combination concentrates its weight differently, and often needs to be near a lake access route rather than tucked beside a house. This page covers both, together, because the underlying slab spec overlaps, and separately, because the loads and use patterns don't.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$1,800–$7,200</span><span class="lbl">Published national RV pad cost range</span></div>
    <div class="stat-box"><span class="num">6"</span><span class="lbl">Typical RV/boat pad thickness</span></div>
    <div class="stat-box"><span class="num">4,000+ PSI</span><span class="lbl">Standard mix strength</span></div>
    <div class="stat-box"><span class="num">28 days</span><span class="lbl">Cure time before parking a loaded RV or boat</span></div>
  </div>
  <p class="calc-disclaimer">Figures above are published planning ranges, not a quote for your project. Size a pad to your specific rig with the <a href="/tools/rv-boat-pad-calculator/">RV &amp; Boat Pad Calculator</a>, then request a site-specific estimate.</p>
</div>

<section>
  <div class="wrap">
    <span class="eyebrow">RV Pads</span>
    <h2>Built for a load that parks and stays</h2>
    <p>A driveway is engineered around a rolling load — a car's weight crosses it and is gone. An RV pad has to hold a much heavier, stationary load in the same spot for weeks or months: jacks down, slide-outs out, axles bearing the full weight of a motorhome that isn't going anywhere. That's the reasoning behind building RV pads thicker (6 in is the number that shows up consistently across RV-focused concrete guides) and to a higher cure standard before anything heavy sits on them. See our <a href="/blog/rv-pad-vs-driveway/">RV Pad vs. Driveway</a> guide for the full comparison, and the <a href="/concrete-driveways/">Concrete Driveways</a> page if you're weighing whether to widen an existing driveway instead of pouring a separate pad.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Boat Pads</span>
    <h2>A different load, and a lake-country lot</h2>
    <p>South Lake County sits inside a chain of lakes — Lake Louisa, Lake Minneola, Little Lake Harris among them — so boat and trailer storage is a routine request here, not a niche one. Most published cost and spec guides treat a boat pad as a copy of an RV pad, and the base numbers are close. But a boat sitting on a trailer concentrates weight on a few points — the tongue jack, the wheels, blocking under the hull — differently than a motorhome's distributed axle weight, and the pad gets wet far more often from wash-down and rain runoff off the hull. See <a href="/blog/boat-pad-vs-rv-pad/">Boat Pad vs. RV Pad</a> for where the specs actually diverge.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Shared Specs</span>
    <h2>Thickness, strength, and reinforcement</h2>
    <p class="lede">Both pad types start from the same technical baseline before diverging on load pattern and drainage detail.</p>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Spec</th><th>RV pad</th><th>Boat pad</th><th>Source</th></tr></thead>
      <tbody>
        <tr><td>Thickness</td><td>6 in (vs. 4 in driveway minimum)</td><td>6 in typical</td><td>Consensus across RV/concrete contractor guides; Florida Building Code Ch. 19 sets the 4 in slab-on-ground floor</td></tr>
        <tr><td>Strength</td><td>4,000+ PSI</td><td>4,000+ PSI</td><td>ACI 332 residential concrete guidance</td></tr>
        <tr><td>Reinforcement</td><td>Rebar sized for stationary axle load</td><td>Rebar sized for trailer point loads</td><td>Industry consensus; wire mesh is not preferred for load-bearing slabs</td></tr>
        <tr><td>Slope</td><td>~1/8 in per foot toward drainage path</td><td>Same, plus wash-down runoff planning</td><td>cement.org mix-design and drainage guidance</td></tr>
        <tr><td>Cure before load</td><td>28 days (stationary heavy load)</td><td>28 days (trailer + boat weight)</td><td>Standard concrete curing practice</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>RV and boat pad questions</h2>
    {_faq_html(RV_BOAT_FAQS)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning an RV or boat pad?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/rv-boat-pad-calculator/">Size your pad</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Concrete RV and boat pads for South Lake County — thickness, PSI, rebar, cure time before parking, and the real difference between an RV pad and a boat pad.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(RV_BOAT_FAQS), _service_schema("rv-and-boat-pads")],
    }


# ---------------------------------------------------------------------------
# 2. Workshop Slabs
# ---------------------------------------------------------------------------

WORKSHOP_FAQS = [
    ("What is a thickened edge slab for a metal building?",
     "It's a slab where the perimeter is poured deeper than the field of the slab — commonly 12–16 inches wide and 8–12 inches deep around the edge — to carry the point loads of a metal building's or barn's support posts. A flat, uniform slab isn't built to carry those concentrated loads along the perimeter — the reason workshop and metal-building slabs are specified differently from a driveway or patio slab."),
    ("Do I need a vapor barrier under my workshop slab?",
     "It depends on what's going in the building. If you're storing tools, running equipment with electronics, finishing wood, or putting down flooring that moisture can damage, a vapor barrier under the slab is worth the added cost — it keeps ground moisture from wicking up through the concrete. For an open-air equipment pad with no climate-sensitive contents, it's a smaller priority. This is a conversation to have before the pour, since it can't be added after."),
    ("How thick should a workshop slab be to support heavy equipment or a lift?",
     "A general workshop floor often follows standard slab guidance (4–5 in, 4,000 PSI), but a slab that needs to support a vehicle lift, heavy stationary machinery, or concentrated point loads needs to be engineered for that specific load — thickness, reinforcement, and sometimes a thickened pad under the lift's mounting points go well beyond a standard floor spec. Tell your provider what's going in the building before the pour, not after."),
    ("What does a concrete slab for a workshop or metal building cost?",
     "$6–$12 per square foot installed is the published general range for a concrete slab, though the exact number moves with thickness, edge detail, reinforcement, and site access. A thickened-edge metal building slab sits toward the higher end of that range because of the extra concrete and rebar at the perimeter. Use this as a planning range, not a quote — request a site-specific estimate once you know the building's footprint."),
    ("Do I need a permit to pour a concrete slab for a workshop in Lake County?",
     "In most cases, yes — a slab for a workshop, barn, or metal building typically falls under a building permit in Lake County and the surrounding cities, separate from any driveway or encroachment permit. Requirements vary by jurisdiction and by whether the building itself also needs a permit. Check the South Lake Permit Directory for the office that covers your address before you schedule a pour."),
    ("What size concrete slab do I need for a workshop or garage?",
     "Size follows the building footprint plus any apron or approach you want poured at the same time — most metal building manufacturers specify the exact slab dimensions and anchor bolt layout the foundation needs to match. Get those dimensions from the building plans first; pouring to a guess instead of the manufacturer's spec is a common and expensive mistake on rural workshop projects."),
]


def _page_workshop_slabs():
    svc = SERVICES["workshop-slabs"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">A workshop, barn, or metal building slab looks like a bigger version of a driveway pour, but it isn't specified like one. The walls of a metal building sit directly on the slab's perimeter, which means that edge has to carry a real structural load — and whatever's going inside (a lift, a welder, moisture-sensitive storage) can change the spec further. This is one of the more common projects on South Lake County's rural, ag-zoned lots.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$6–$12</span><span class="lbl">Per sq ft, published general slab cost range</span></div>
    <div class="stat-box"><span class="num">12–16"</span><span class="lbl">Thickened edge width at the perimeter</span></div>
    <div class="stat-box"><span class="num">8–12"</span><span class="lbl">Thickened edge depth at the perimeter</span></div>
    <div class="stat-box"><span class="num">4,000 PSI</span><span class="lbl">Standard mix strength floor</span></div>
  </div>
  <p class="calc-disclaimer">Ranges above reflect published cost data, not a quote for your project — a metal building slab's real cost tracks its footprint, edge detail, and reinforcement. Walk through the <a href="/tools/workshop-slab-guide/">Workshop Slab Thickness Guide</a> before you pour, then request a site-specific estimate.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Not Just a Bigger Driveway</span>
    <h2>What actually changes for a metal building or barn slab</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>The perimeter carries the structure</h3>
        <p>A metal building's wall posts bear directly on the slab's edge, which is why that edge is typically thickened — 12–16 inches wide, 8–12 inches deep — rather than poured at a uniform depth like a driveway or patio.</p>
      </div>
      <div class="card">
        <h3>What's inside changes the floor spec</h3>
        <p>A vapor barrier, a thicker slab under a lift's mounting points, or reinforcement sized for heavy stationary equipment are all decisions that have to be made before the pour, not retrofitted after.</p>
      </div>
      <div class="card">
        <h3>Dimensions come from the building, not a guess</h3>
        <p>Most metal building kits specify exact slab dimensions and anchor bolt layout. Pouring before that spec is finalized is among the most frequent — and expensive — mistakes on rural workshop projects.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Specs That Matter</span>
    <h2>Standard floor vs. metal building slab</h2>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Spec</th><th>General workshop floor</th><th>Metal building / barn slab</th><th>Source</th></tr></thead>
      <tbody>
        <tr><td>Thickness</td><td>4–5 in</td><td>4–5 in field, thickened perimeter</td><td>General slab-on-ground practice; Florida Building Code Ch. 19 sets the 4 in floor</td></tr>
        <tr><td>Perimeter edge</td><td>Not applicable</td><td>12–16 in wide, 8–12 in deep</td><td>Metal building foundation contractor consensus</td></tr>
        <tr><td>Strength</td><td>4,000 PSI</td><td>4,000+ PSI</td><td>ACI 332 residential concrete range</td></tr>
        <tr><td>Vapor barrier</td><td>Optional</td><td>Recommended for climate-sensitive contents</td><td>Common add-on across slab-cost guides</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Common workshop slab questions</h2>
    {_faq_html(WORKSHOP_FAQS)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning a workshop or metal building slab?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/workshop-slab-guide/">Use the slab thickness guide</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Concrete slabs for workshops, metal buildings, and barns in South Lake County — thickened edges, vapor barriers, thickness, PSI, and permit basics.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(WORKSHOP_FAQS), _service_schema("workshop-slabs")],
    }


# ---------------------------------------------------------------------------
# 3. Concrete Patios
# ---------------------------------------------------------------------------

PATIO_FAQS = [
    ("How much does a concrete patio cost in Florida?",
     "There isn't a reliable patio-specific published range we can point to — most cost data available covers driveways and general slabs, not patios specifically. The published general slab cost of $6–$12 per sq ft installed is a reasonable starting reference point since the underlying concrete work is similar, but treat it as a rough planning anchor, not a patio quote. Size and finish move the number more for a patio than for a driveway, since patios vary widely from a simple rectangle to a multi-level entertaining space."),
    ("What is the best concrete finish for a patio in Florida's heat and humidity?",
     "A lighter-colored finish reflects heat instead of absorbing it — dark stained or dyed patios can get uncomfortably hot underfoot in direct Central Florida sun. A broom finish or a light exposed-aggregate texture also holds up better against the slickness that humidity and afternoon rain create on a smooth-troweled surface."),
    ("Does a concrete patio need the same base preparation as a driveway?",
     "Yes — the same principles apply: a properly compacted base (typically 4–8 inches) matters as much for a patio as for a driveway, especially on South Lake County's sandy soil, which compacts differently than clay-based soil. A patio isn't a lighter-duty project just because it doesn't carry vehicles; poor base prep shows up the same way, as settling and cracking."),
    ("How do I keep a concrete patio from flooding during Florida's rainy season?",
     "The same roughly 1/8-inch-per-foot minimum slope used on driveways applies to a patio, directed away from the house toward a drainage path. A patio poured flat, or sloped back toward the foundation, is a common and avoidable cause of standing water and even interior flooding during Central Florida's summer storm pattern."),
    ("Should I choose stamped concrete or a plain patio?",
     "Stamped concrete costs more upfront and gives you a decorative pattern and texture; a plain broom-finished patio is the lower-cost, lower-maintenance option. Neither is objectively better — it depends on budget and how much you value the look versus long-term simplicity. See our full <a href=\"/compare/stamped-vs-plain-patio/\">Stamped Concrete vs. Plain Patio</a> comparison for the trade-offs."),
    ("Does the same building code that covers driveways apply to patios?",
     "Largely yes — ACI 332, the residential concrete standard referenced by Florida's building code framework, explicitly covers slab-on-ground driveways, patios, sidewalks, and garages under the same general guidance. A patio doesn't get a separate, looser standard just because it isn't load-bearing for vehicles."),
]


def _page_concrete_patios():
    svc = SERVICES["concrete-patios"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">A patio is often the first outdoor space people plan and the last one they think through technically — but Central Florida's combination of intense sun, high humidity, and heavy summer rain makes finish, slope, and base prep just as important here as on a driveway. On South Lake County's larger lots, patios also tend to be bigger and more custom-shaped than a standard subdivision slab, which changes how they should be planned.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$6–$12</span><span class="lbl">Per sq ft, general slab cost (not patio-specific — see note)</span></div>
    <div class="stat-box"><span class="num">4"</span><span class="lbl">Typical slab-on-ground thickness reference</span></div>
    <div class="stat-box"><span class="num">1/8" per ft</span><span class="lbl">Minimum slope to move water off the patio</span></div>
  </div>
  <p class="calc-disclaimer">No reliable published cost range exists specifically for patios as of this writing — the figure above is the general concrete slab cost range, offered as a rough planning anchor, not a patio quote. Request a site-specific estimate once you have a shape and size in mind.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Built for Florida's Climate</span>
    <h2>What a patio needs that a driveway doesn't have to worry about</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Finish affects comfort, not just looks</h3>
        <p>Bare feet make finish choice a real functional decision on a patio in a way it isn't on a driveway — dark, smooth-troweled surfaces get hot and slick fast under Florida sun and rain.</p>
      </div>
      <div class="card">
        <h3>Shape drives cost more than size</h3>
        <p>Patios are rarely a simple rectangle. Curves, multiple levels, and cutouts around existing landscaping all add cost beyond what a per-square-foot number captures.</p>
      </div>
      <div class="card">
        <h3>Drainage still has to point somewhere</h3>
        <p>A patio poured flat against a house is a common cause of water finding its way toward the foundation during Central Florida's rainy season — slope planning matters as much here as on a driveway.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Common patio questions</h2>
    {_faq_html(PATIO_FAQS)}
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Planning a patio project?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/paver-patios/">See paver patio options</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Concrete patios for South Lake County — finish choices for Florida heat and humidity, base prep, drainage, and honest cost guidance without invented numbers.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(PATIO_FAQS), _service_schema("concrete-patios")],
    }


# ---------------------------------------------------------------------------
# 4. Concrete Repair & Resurfacing
# ---------------------------------------------------------------------------

REPAIR_FAQS = [
    ("How do I know if my driveway needs repair or full replacement?",
     "Hairline surface cracks, minor pitting, and cosmetic discoloration are usually repair or resurfacing candidates. Wide cracks that keep growing, sections that have visibly sunk or tilted, or a slab that's crumbling below the surface generally point to a base failure that resurfacing won't fix — that's a replacement conversation. See our <a href=\"/blog/repair-vs-replace-driveway/\">Repair or Replace</a> guide for the full breakdown."),
    ("What causes concrete driveways to sink or settle over time?",
     "Most sinking traces back to the base underneath, not the concrete itself — inadequate compaction during the original pour, erosion or washout under the slab from poor drainage, or Central Florida's sandy soil shifting over time. A slab can't be any more stable than the ground under it, so base preparation matters as much to long-term durability as the pour itself."),
    ("Can a cracked concrete slab be resurfaced instead of replaced?",
     "Often, yes — if the cracking is cosmetic and the base underneath is still sound, a resurfacing overlay (commonly around 1 inch) can restore the surface without a full tear-out. If the cracks indicate the base has failed, resurfacing over that problem just delays it, and typically costs more in the long run than fixing the base and repouring."),
    ("How much does concrete resurfacing cost compared to a new pour?",
     "A full replacement, including demolition of the old slab, runs a published $8–$12 per sq ft in Florida cost data — resurfacing is generally cheaper per square foot since there's no demolition and less material, but a confirmed side-by-side range isn't available as of this writing. Treat any number here as a planning estimate; see <a href=\"/blog/resurfacing-vs-new-pour-cost/\">Resurfacing vs. a New Pour</a> for how to think through the trade-off, then request a site-specific estimate."),
    ("Is a permit required for a thin concrete resurfacing overlay in Florida?",
     "Often not — a thin overlay (around 1 inch) applied to an existing slab commonly falls outside the permit requirement that applies to pouring a new driveway slab, since it isn't new construction. This varies by jurisdiction, so confirm with the office listed in the South Lake Permit Directory before assuming either way."),
    ("Is it worth resurfacing a driveway before selling a rural property?",
     "There's no confirmed data on how resurfacing specifically affects a sale price or appraisal for a rural South Lake County property — this is a real question buyers and sellers ask, but it isn't one we have a sourced answer for. What is true: a visibly cracked, sunken, or patched driveway is a first impression, and resurfacing is generally the lower-cost way to address that impression compared to a full replacement. See <a href=\"/blog/is-resurfacing-worth-it-before-selling/\">Is Resurfacing Worth It Before Selling</a> for the fuller discussion."),
]


def _page_repair_resurfacing():
    svc = SERVICES["concrete-repair-resurfacing"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Not every cracked or sunken slab needs to be torn out and repoured. Central Florida's heat cycles, heavy summer rain, and sandy soil all put real stress on aging concrete, and the honest answer to "repair, resurface, or replace" depends on what's actually wrong underneath the surface — not just what it looks like on top.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$8–$12</span><span class="lbl">Per sq ft, full replacement incl. demolition (published FL range)</span></div>
    <div class="stat-box"><span class="num">~1"</span><span class="lbl">Typical thin resurfacing overlay thickness</span></div>
    <div class="stat-box"><span class="num">Often no permit</span><span class="lbl">For thin overlays — verify with your local office</span></div>
  </div>
  <p class="calc-disclaimer">Figures above are published planning ranges, not a quote for your project — repair and resurfacing costs depend heavily on the extent and cause of the damage. Request a site-specific estimate before assuming a number.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Diagnosing the Real Problem</span>
    <h2>What's actually wrong before you decide what to do about it</h2>
    <div class="grid grid-2">
      <div class="card">
        <h3>Surface problem: repair or resurface</h3>
        <p>Hairline cracks, surface pitting, and cosmetic wear on a slab that's still structurally flat and stable are typically resurfacing candidates — a new overlay restores the look without a full tear-out.</p>
      </div>
      <div class="card">
        <h3>Base problem: replace</h3>
        <p>Wide, spreading cracks, sunken sections, or a slab that rocks or tilts point to a failed base underneath — compaction failure, erosion, or soil movement. Resurfacing over that just hides the problem temporarily.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Repair, resurfacing, and replacement questions</h2>
    {_faq_html(REPAIR_FAQS)}
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Not sure if you need repair or replacement?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free assessment</a>
      <a class="btn btn-outline btn-lg" href="/concrete-driveways/">See new driveway specs</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Concrete repair and resurfacing guidance for South Lake County — how to tell repair from replacement, resurfacing cost basics, and permit notes.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(REPAIR_FAQS), _service_schema("concrete-repair-resurfacing")],
    }


# ---------------------------------------------------------------------------
# 5. Sidewalks & Walkways
# ---------------------------------------------------------------------------

SIDEWALK_FAQS = [
    ("How much does a concrete sidewalk or walkway cost?",
     "There's no reliable published range specific to residential sidewalks and walkways as of this writing — this is a smaller, lower-volume project type than driveways or slabs, and most cost guides don't break it out separately. Cost depends heavily on length, width, and finish; request a site-specific estimate rather than relying on a generic number."),
    ("Does Lake County require a permit for a new sidewalk or walkway?",
     "This depends on the jurisdiction and whether the walkway connects to a public right-of-way — that's a different situation than a private path across your own yard. Check the South Lake Permit Directory for the building office covering your address rather than assuming either way."),
    ("What is the minimum width for a concrete walkway?",
     "Accessibility guidance commonly references 36 inches as a functional minimum for a clear path, though that standard is aimed at public and commercial accessibility requirements rather than a private residential walkway. For a private path on your own property, width is more a comfort and function decision than a fixed code number — verify with your local building office if the walkway will be part of an approved site plan."),
    ("How thick should a concrete walkway or path be?",
     "A residential walkway is typically lighter-duty than a driveway — commonly 3–4 inches, versus the 4-inch Florida Building Code minimum for a slab that carries vehicle loads. A path that will regularly see heavier foot traffic, equipment, or golf-cart use should be discussed with your provider before the pour, since that can push the spec closer to driveway-grade."),
    ("Does a walkway need the same base prep and slope as a driveway?",
     "The same underlying principles apply even though the loads are lighter — a compacted base is still what keeps a walkway from settling or cracking unevenly over time, and a slight slope (roughly the same 1/8-inch-per-foot reference used for driveways) still matters for keeping water from pooling along the path. Skipping base prep because a walkway is 'just foot traffic' is a common way these smaller projects end up cracking early."),
    ("Does a walkway need rebar, or is fiber-reinforced concrete enough?",
     "For a standard foot-traffic path, fiber reinforcement mixed into the concrete is generally adequate — the loads are far lighter than a driveway, so the rebar some jurisdictions require for vehicle-bearing slabs usually isn't necessary here. If a walkway will occasionally see a golf cart, mower, or other light equipment, mention that before the pour so the reinforcement can be sized accordingly."),
]


def _page_sidewalks_walkways():
    svc = SERVICES["sidewalks-walkways"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Sidewalks and walkways are a smaller project than a driveway or a slab, but they're not an afterthought — a path from a long driveway to the front door, or from a house to a workshop or RV pad, gets used constantly and needs to hold up to the same Florida sun and rain everything else on the property does.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">3–4"</span><span class="lbl">Typical residential walkway thickness</span></div>
    <div class="stat-box"><span class="num">1/8" per ft</span><span class="lbl">Minimum slope reference for drainage</span></div>
    <div class="stat-box"><span class="num">Ranges vary</span><span class="lbl">Cost depends on length, width &amp; finish — request a site estimate</span></div>
  </div>
  <p class="calc-disclaimer">No confirmed published cost range exists specifically for residential sidewalks and walkways as of this writing — request a site-specific estimate rather than assuming a number.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Where This Fits on a Larger Lot</span>
    <h2>A connector between the projects you're already planning</h2>
    <p>On a standard subdivision lot, a sidewalk is often just the strip between the driveway and the front door. On South Lake County's larger, rural lots, walkways more often connect separate structures — house to workshop, driveway to an RV pad, house to a detached garage — which means length and routing matter more than they would on a short suburban path. If you're already planning a <a href="/concrete-driveways/">driveway</a>, a <a href="/workshop-slabs/">workshop slab</a>, or an <a href="/rv-and-boat-pads/">RV or boat pad</a>, a connecting walkway is worth pricing in the same visit rather than as a separate project later.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Lighter Duty, Same Fundamentals</span>
    <h2>Why a small project still needs a real spec</h2>
    <div class="grid grid-2">
      <div class="card">
        <h3>Lighter load, not no load</h3>
        <p>A walkway doesn't carry a vehicle, so it's built thinner (3–4 in) with lighter reinforcement than a driveway — but it still needs a compacted base and correct slope, or it settles and cracks the same way a driveway does.</p>
      </div>
      <div class="card">
        <h3>Routing matters on a big lot</h3>
        <p>A short suburban path and a few-hundred-foot walkway connecting a house to a workshop or RV pad are different projects in practice, even if the per-foot spec is similar — plan the route with the rest of your site work, not as an afterthought.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Common sidewalk and walkway questions</h2>
    {_faq_html(SIDEWALK_FAQS)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning a walkway alongside another project?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/permits/">Check permit requirements</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Concrete sidewalks and walkways for South Lake County — thickness, width, permit basics, and honest guidance on a project type with no reliable published cost data.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(SIDEWALK_FAQS), _service_schema("sidewalks-walkways")],
    }


# ---------------------------------------------------------------------------
# 6a. Paver Driveways
# ---------------------------------------------------------------------------

PAVER_DRIVEWAY_FAQS = [
    ("How much does a paver driveway cost in Florida?",
     "Pavers run a published $10–$30 per sq ft installed, versus $4–$15 per sq ft for poured concrete — pavers cost more upfront in almost every case. That published range isn't broken out separately for driveways vs. patios, but a driveway typically lands toward the higher end because of the deeper base a vehicle load requires. Treat this as a planning estimate and request a site-specific quote."),
    ("Does a paver driveway need a different base than a paver patio?",
     "Yes. A driveway carrying vehicle weight needs a deeper compacted aggregate base — commonly 6–8+ inches of crushed stone, versus roughly 4–6 inches under a pedestrian-only paver patio — plus a properly compacted bedding layer under the pavers themselves. Skimping on base depth is the most common reason a paver driveway starts to rut or shift where tires track."),
    ("Do paver driveways need edge restraints?",
     "Yes, and it matters more here than on a patio. Vehicles turning and braking push pavers sideways, and without a solid edge restraint (plastic, aluminum, or a concrete curb) anchored into the base, the outer rows gradually spread and the whole field loosens over time. This is among the most frequent failure points on paver driveways installed without it."),
    ("What paver pattern holds up best under vehicle traffic?",
     "Herringbone (pavers laid at a 45- or 90-degree interlocking angle) is the pattern most commonly recommended for vehicular use because it interlocks against the shifting forces of turning and braking better than a simple running-bond or stack pattern, which are more common on patios where only foot traffic applies."),
    ("Can a long paver driveway work the same way a long concrete driveway does?",
     "Structurally, yes — the same base and edge-restraint principles just apply over more distance. Cost scales with area more noticeably than with concrete, though, since the per-square-foot price is already higher; for a long rural approach, run the numbers on both materials before deciding. See our <a href=\"/tools/driveway-cost-calculator/\">Driveway Cost &amp; Volume Calculator</a> for the concrete comparison."),
    ("Is a paver driveway or a concrete driveway the better choice?",
     "It depends on budget and maintenance preference more than on which one is objectively better — see our full <a href=\"/compare/paver-vs-concrete-driveway/\">Paver vs. Concrete Driveway</a> comparison for the cost, drainage, and repair trade-offs side by side."),
]


def _page_paver_driveways():
    svc = SERVICES["paver-driveways"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">A paver driveway isn't a patio that happens to be wider — it carries vehicle weight, which changes the base depth, the edge detail, and even which paver pattern actually holds up. This page covers the driveway-specific side of paver installation; if you're deciding between pavers and poured concrete in the first place, see our <a href="/compare/paver-vs-concrete-driveway/">full comparison</a> instead.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$10–$30</span><span class="lbl">Per sq ft installed (published range)</span></div>
    <div class="stat-box"><span class="num">6–8"+</span><span class="lbl">Compacted base depth for vehicle loads</span></div>
    <div class="stat-box"><span class="num">Herringbone</span><span class="lbl">Recommended interlocking pattern for traffic</span></div>
  </div>
  <p class="calc-disclaimer">The cost range above is a general published figure, not split separately for driveways vs. patios — a driveway typically runs toward the higher end because of the deeper base required. Request a site-specific estimate for your project.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">What a Vehicle Load Changes</span>
    <h2>Base, edges, and pattern all work harder under a car</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Deeper base than a patio</h3>
        <p>A driveway needs 6–8+ inches of compacted aggregate base under the bedding layer — more than the 4–6 inches typical under a pedestrian paver patio — to keep vehicle weight from working the pavers loose over time.</p>
      </div>
      <div class="card">
        <h3>Edge restraint isn't optional</h3>
        <p>Turning and braking push pavers sideways at the edges. A solid restraint anchored into the base keeps the outer rows from spreading — the single most common failure point on driveways installed without one.</p>
      </div>
      <div class="card">
        <h3>Pattern affects durability, not just looks</h3>
        <p>Herringbone interlocks against shifting forces better than the running-bond patterns common on patios, which only need to handle foot traffic.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Paver driveway questions</h2>
    {_faq_html(PAVER_DRIVEWAY_FAQS)}
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Considering pavers for your driveway?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/compare/paver-vs-concrete-driveway/">Compare pavers vs. concrete</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Paver driveway installation for South Lake County — base depth, edge restraints, and pattern choices built for vehicle loads, not just looks.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(PAVER_DRIVEWAY_FAQS), _service_schema("paver-driveways")],
    }


# ---------------------------------------------------------------------------
# 6b. Paver Patios
# ---------------------------------------------------------------------------

PAVER_PATIO_FAQS = [
    ("How much does a paver patio cost?",
     "Pavers run a published $10–$30 per sq ft installed — that range isn't broken out separately for patios vs. driveways, but a patio's simpler base requirements often land it toward the lower-to-middle end compared to a driveway carrying vehicle loads. Shape and pattern complexity move the number more than base depth does for a patio."),
    ("Do paver patios need as deep a base as a paver driveway?",
     "No. A pedestrian-only patio typically needs roughly 4–6 inches of compacted aggregate base, compared to the 6–8+ inches a vehicle-bearing paver driveway needs — see our <a href=\"/paver-driveways/\">Paver Driveways</a> page for that comparison. Base prep still matters on South Lake County's sandy soil either way; it's just a lighter-duty version of the same principle."),
    ("Are paver patios more comfortable underfoot than concrete?",
     "Lighter-colored and textured paver units tend to stay cooler underfoot than a dark, smooth-troweled concrete surface in direct Central Florida sun — the same heat-reflectance logic that applies to concrete finish choice applies to paver color choice. Neither material is immune to summer heat, but color and texture make a real difference for bare feet."),
    ("Paver patio or stamped concrete — which should I choose?",
     "Our <a href=\"/compare/stamped-vs-plain-patio/\">Stamped Concrete vs. Plain Patio</a> comparison covers two concrete finishes specifically; pavers are a third path with their own trade-off — more pattern and color flexibility than either concrete option, individual units that can be replaced without disturbing the rest of the surface, but a higher upfront cost and periodic joint-sand maintenance neither concrete finish requires."),
    ("Can a paver patio be installed around curves or existing landscaping?",
     "Yes — this is one of paver's practical advantages over a poured slab. Individual units can follow a curve or work around an existing tree or planting bed more easily than form-and-pour concrete work, without the cost premium a custom-shaped concrete pour usually carries."),
]


def _page_paver_patios():
    svc = SERVICES["paver-patios"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">A patio doesn't carry vehicle weight, so the questions that matter most are comfort, pattern, and how well the surface works with an irregular shape — not base depth for traffic loads. This page covers paver patios specifically; for the driveway application, see our <a href="/paver-driveways/">Paver Driveways</a> page.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$10–$30</span><span class="lbl">Per sq ft installed (published range)</span></div>
    <div class="stat-box"><span class="num">4–6"</span><span class="lbl">Compacted base depth, pedestrian-only</span></div>
    <div class="stat-box"><span class="num">Curve-friendly</span><span class="lbl">Individual units follow irregular shapes easily</span></div>
  </div>
  <p class="calc-disclaimer">The cost range above is a general published figure, not split separately for patios vs. driveways. Shape, pattern, and material choice move the number more than base depth for a patio — request a site-specific estimate.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Where Pavers Fit a Patio Best</span>
    <h2>Comfort and shape flexibility, not load-bearing</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Lighter base, same soil to manage</h3>
        <p>No vehicle load means a lighter base than a driveway — but South Lake County's sandy soil still needs proper compaction underneath, or you'll see the same settling problems at a smaller scale.</p>
      </div>
      <div class="card">
        <h3>Color and texture affect comfort</h3>
        <p>Lighter, textured units stay cooler underfoot than dark, smooth surfaces — a real consideration for bare feet on a patio in a way it rarely is on a driveway.</p>
      </div>
      <div class="card">
        <h3>Built for irregular shapes</h3>
        <p>Curves, cutouts around existing trees, and multi-level layouts are more practical with individual units than with a custom concrete pour.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Paver patio questions</h2>
    {_faq_html(PAVER_PATIO_FAQS)}
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Planning a paver patio?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/compare/stamped-vs-plain-patio/">See concrete patio finishes</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Paver patio installation for South Lake County — comfort, pattern, and shape flexibility for outdoor living, with honest base-prep and cost guidance.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(PAVER_PATIO_FAQS), _service_schema("paver-patios")],
    }


# ---------------------------------------------------------------------------
# 7. Retaining Walls
# ---------------------------------------------------------------------------

RETAINING_WALL_FAQS = [
    ("Do I need a retaining wall if my property has a slope or drainage problem?",
     "A retaining wall is one tool for one specific problem: soil that's eroding or sliding because of a grade change. If your issue is water pooling on a flat area, a retaining wall usually isn't the fix — a French drain, catch basin, or corrected slope handles standing water better. If the issue is soil moving or eroding at a grade change, a retaining wall (often paired with drainage behind it) is the right category of solution. The two problems look similar but call for different fixes."),
    ("How much does a retaining wall cost for a sloped property in Florida?",
     "$3,190–$9,203 is a published national cost range for a retaining wall, not a Florida-specific figure — wall height, length, material, and how steep the site is all move the number substantially. Sloped sites also commonly add 50% or more to labor cost compared to a flat site, since access and excavation are harder. Treat this as a planning range and request a site-specific estimate."),
    ("Can a retaining wall prevent erosion on a rural or hilly Lake County property?",
     "Yes, that's the core engineering purpose of a retaining wall — holding soil in place against a grade change so it doesn't erode or slide, particularly during Central Florida's heavy summer rain. Areas with real elevation change, like the rolling terrain around Howey-in-the-Hills or the sloped sections of larger Groveland-area lots, are exactly the kind of site where a wall solves a real physical problem rather than serving a decorative purpose."),
    ("What drainage solutions exist for water that won't stop pooling on my property?",
     "Channel drains, catch basins, and French drains are the standard tools for moving standing water off a flat or poorly graded area — often a better fix than a retaining wall if the core problem is water sitting still rather than soil moving. Sometimes a project needs both: a wall to hold a grade change, and a drain behind or below it so water doesn't just build up against the new wall instead."),
    ("Does a sloped driveway need different concrete thickness or reinforcement?",
     "A driveway on a real grade change should be evaluated on its own, not assumed to follow the same 4–5 inch standard-lot spec — water flow, soil movement at the base, and how the slab ties into surrounding grade all matter more on a sloped site. See our <a href=\"/concrete-driveways/\">Concrete Driveways</a> page for the baseline spec, and treat a sloped or eroding lot as a case for a site-specific plan rather than a standard pour."),
]


def _page_retaining_walls():
    svc = SERVICES["retaining-walls"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">This isn't a landscaping page. A retaining wall's job is to hold soil in place against a grade change — stopping erosion, managing runoff, and keeping a sloped section of a rural lot from sliding or washing out during Central Florida's heavy summer rain. On lots with real elevation change, like the rolling terrain around Howey-in-the-Hills or sloped sections of larger Groveland-area properties, that's a structural and drainage problem worth solving correctly, not a decorative upgrade.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">$3,190–$9,203</span><span class="lbl">Published national retaining wall cost range</span></div>
    <div class="stat-box"><span class="num">50%+</span><span class="lbl">Typical added labor cost on a sloped site</span></div>
    <div class="stat-box"><span class="num">1/8" per ft</span><span class="lbl">Minimum slope reference for surface drainage nearby</span></div>
  </div>
  <p class="calc-disclaimer">Figures above are published national planning ranges, not Florida-specific or site-specific quotes — wall height, length, material, and site slope all move the real number. Request a site-specific estimate.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Matching the Fix to the Problem</span>
    <h2>Erosion, runoff, and standing water aren't the same problem</h2>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Symptom</th><th>Likely cause</th><th>Typical fix</th></tr></thead>
      <tbody>
        <tr><td>Soil eroding or sliding at a grade change</td><td>Unsupported slope, heavy rain runoff</td><td>Retaining wall, often with drainage behind it</td></tr>
        <tr><td>Water pooling on a flat or gently graded area</td><td>Inadequate slope or no outlet for runoff</td><td>Corrected grading, French drain, or catch basin — not a wall</td></tr>
        <tr><td>Driveway or slab settling near a slope</td><td>Base movement, water undermining the slab edge</td><td>Site-specific reinforcement plan, evaluated with the slope in mind</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Common slope and retaining wall questions</h2>
    {_faq_html(RETAINING_WALL_FAQS)}
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Dealing with a slope, erosion, or drainage problem?</h2>
    {_disclosure()}
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/drainage-slope-planner/">Plan your drainage &amp; slope</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()
    return {
        "route": svc["route"],
        "title": f'{svc["name"]} in Groveland & South Lake County',
        "meta_description": "Retaining walls for South Lake County rural lots — framed as an erosion, runoff, and slope-drainage solution, not a decorative landscaping feature.",
        "h1": svc["name"],
        "breadcrumbs": [("Home", "/"), ("Services", "/services/"), (svc["name"], None)],
        "nav_active": "/services/",
        "body_html": body_html,
        "schema": [_faq_schema(RETAINING_WALL_FAQS), _service_schema("retaining-walls")],
    }


def get_pages():
    return [
        _page_rv_boat_pads(),
        _page_workshop_slabs(),
        _page_concrete_patios(),
        _page_repair_resurfacing(),
        _page_sidewalks_walkways(),
        _page_paver_driveways(),
        _page_paver_patios(),
        _page_retaining_walls(),
    ]
