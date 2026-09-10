# -*- coding: utf-8 -*-
"""Per-route <title> and meta-description overrides.

Titles: full string <= 60 chars (the " | Groveland Concrete" suffix is added by
render_page unless the override is marked full). Descriptions: 120-160 chars.
Anything not listed keeps the page's own title/description."""

SUFFIX = " | Groveland Concrete"

# route -> page-part title (suffix appended) or ("FULL", "exact title")
TITLES = {
    "/": ("FULL", "Groveland Concrete | Concrete & Paving Contractor, FL"),
    "/clermont/": "Concrete & Pavers in Clermont, FL",
    "/compare/paver-vs-concrete-driveway/": "Paver vs. Concrete Driveway in FL",
    "/compare/rebar-vs-wire-mesh/": "Rebar vs. Wire Mesh for Driveways",
    "/concrete-driveways/": "Concrete Driveways in Groveland, FL",
    "/concrete-patios/": "Concrete Patios in Groveland, FL",
    "/concrete-repair-resurfacing/": "Concrete Repair & Resurfacing in FL",
    "/gallery/": "Photo Gallery: Driveways & Pool Decks",
    "/groveland/": "Concrete Contractor in Groveland, FL",
    "/blog/": "Blog: Concrete & Paver Guides",
    "/blog/best-base-sandy-soil-florida/": "Best Concrete Base for Sandy FL Soil",
    "/blog/boat-pad-vs-rv-pad/": "Boat Pad vs. RV Pad: Same Concrete?",
    "/blog/concrete-truck-access-rural-driveway/": "Can a Concrete Truck Reach Your Lot?",
    "/blog/concrete-vs-gravel-driveway-florida/": "Concrete vs. Gravel Driveways in FL",
    "/blog/fixing-flooding-sloped-driveway/": "Fixing a Sloped Driveway That Floods",
    "/blog/is-resurfacing-worth-it-before-selling/": "Resurface a Driveway Before Selling?",
    "/blog/long-driveway-cost-florida/": "Long Driveway Cost in Florida",
    "/blog/maintain-concrete-driveway-florida-climate/": "Concrete Driveway Care in Florida",
    "/blog/repair-vs-replace-driveway/": "Repair or Replace an Aging Driveway?",
    "/blog/resurfacing-vs-new-pour-cost/": "Resurfacing vs. New Pour: Real Cost",
    "/blog/rv-pad-vs-driveway/": "RV Pad vs. Driveway: The Difference",
    "/blog/why-concrete-driveway-cracking/": "Why Is My New Driveway Cracking?",
    "/howey-in-the-hills/": "Concrete & Pavers, Howey-in-the-Hills",
    "/mascotte/": "Concrete Contractor in Mascotte, FL",
    "/minneola/": "Concrete Contractor in Minneola, FL",
    "/montverde/": "Concrete & Pavers in Montverde, FL",
    "/paver-driveways/": "Paver Driveways in Groveland, FL",
    "/paver-patios/": "Paver Patios in Groveland, FL",
    "/retaining-walls/": "Retaining Walls in Groveland, FL",
    "/rural-lake-county/": "Concrete for Rural Lake County Lots",
    "/rv-and-boat-pads/": "RV & Boat Pads in Groveland, FL",
    "/sidewalks-walkways/": "Sidewalks & Walkways in Groveland, FL",
    "/workshop-slabs/": "Workshop Slabs in Groveland, FL",
}

DESCRIPTIONS = {
    "/": "Concrete & paving contractor in Groveland, FL: driveways, RV and boat pads, slabs, pavers, pool decks and walkways across South Lake County. Free estimates.",
    "/404/": "That page doesn't exist on grovelandconcrete.com. Head back to the homepage or jump to our services, service area, planning tools, or photo gallery.",
    "/accessibility/": "Groveland Concrete aims for WCAG 2.2 AA on grovelandconcrete.com. Here is what we do for accessibility and how to report a barrier so we can fix it fast.",
    "/compare/paver-vs-concrete-driveway/": "Paver vs. concrete driveway in Florida, compared on cost, cracking, drainage and repair — what is a documented tradeoff and what is just marketing copy.",
    "/compare/rebar-vs-wire-mesh/": "Rebar vs. wire mesh for a concrete driveway, compared on cost, pour behavior and crack control — and why some Florida jurisdictions won't accept mesh alone.",
    "/gallery/": "Groveland Concrete job photos: paver driveways, marble and travertine pool decks, raised terraces, entry steps and walkways across South Lake County, FL.",
    "/blog/": "Guides and side-by-side comparisons on concrete driveways, RV pads, slabs, pavers and drainage for South Lake County, FL — written from the specs, not ad copy.",
    "/blog/best-base-sandy-soil-florida/": "Why sandy Central Florida soil needs careful base compaction before a concrete pour, the 4–8 inch base standard, and what is still unconfirmed for this soil.",
    "/blog/boat-pad-vs-rv-pad/": "Boat pad vs. RV pad: why South Lake County's lakes make boat-trailer storage its own need, and what is confirmed vs. assumed about the concrete specs for each.",
    "/blog/concrete-truck-access-rural-driveway/": "Can a loaded mixer truck reach and turn around on a long or narrow rural driveway? The clearances that matter and the fallbacks: pump truck, buggy, mini-mixer.",
    "/blog/concrete-vs-gravel-driveway-florida/": "Concrete vs. gravel for a long rural Florida driveway: upfront cost, maintenance, and where Central Florida rain and sandy soil change the answer.",
    "/blog/fixing-flooding-sloped-driveway/": "Why a concrete driveway floods in Florida rainstorms, the 1/8-inch-per-foot slope standard, and real fixes — drains to retaining walls — once the slab is down.",
    "/blog/is-resurfacing-worth-it-before-selling/": "Is resurfacing a cracked driveway worth it before selling a rural South Lake County property? Curb appeal, disclosure risk, and what the numbers don't confirm.",
    "/blog/maintain-concrete-driveway-florida-climate/": "Practical care for a concrete driveway in Central Florida heat, humidity and heavy rain — cleaning, sealing and joint upkeep without overstated heat claims.",
    "/blog/repair-vs-replace-driveway/": "How to tell whether an aging or cracked concrete driveway needs repair or full replacement, including the permit difference between an overlay and a new pour.",
    "/blog/resurfacing-vs-new-pour-cost/": "Resurfacing vs. a full driveway replacement: what the costs actually are, and why resurfacing over a failed base can end up costing more, not less.",
    "/blog/rv-pad-vs-driveway/": "The engineering difference between a driveway and an RV pad — rolling load vs. concentrated stationary load — and what it means for thickness, PSI and rebar.",
    "/blog/why-concrete-driveway-cracking/": "The three real causes behind a newly cracked concrete driveway — shrinkage, base movement and wire mesh — plus an honest look at the Florida-heat theory.",
    "/montverde/": "Long driveways, retaining walls and drainage for estate-sized lots in Montverde, FL, including Bella Collina — built for sloped terrain and lake-edge sites.",
    "/permits/": "Direct links to the building and permit office for Groveland, Mascotte, Minneola, Howey-in-the-Hills, unincorporated Lake County and the Center Hill area.",
    "/privacy-policy/": "How Groveland Concrete collects, uses and keeps the information you submit through the contact form, including calls, texts and data retention.",
    "/sidewalks-walkways/": "Concrete sidewalks and walkways in Groveland and South Lake County — thickness, width, permit basics, and straight answers on a job with scarce public pricing.",
    "/terms/": "Terms of use for grovelandconcrete.com: how estimates and calculators should be read, what the planning content covers, and the limits of our liability.",
    "/thank-you/": "Your request reached Groveland Concrete. We typically reply within one business day to set up a free site visit and put a written estimate together.",
    "/tools/driveway-cost-calculator/": "Estimate cubic yards and a planning-level cost range for a standard or long concrete driveway in South Lake County, FL, using local ready-mix pricing.",
    "/tools/rv-boat-pad-calculator/": "Pick a size preset or enter custom dimensions to estimate square footage, concrete volume and a planning-level cost range for an RV or boat pad in FL.",
    "/tools/site-access-checklist/": "Check clearance width, height, turnaround room and ground conditions before assuming a concrete mixer truck can reach your rural South Lake County lot.",
    "/tools/workshop-slab-guide/": "Thickened-edge slab specs for a metal building or barn, when a vapor barrier matters, and a footprint-based cost estimator for a workshop slab in FL.",
}


def title_for(route, default, is_home):
    t = TITLES.get(route)
    if t is None:
        return default if is_home else default + SUFFIX
    if isinstance(t, tuple):
        return t[1]
    return t + SUFFIX


def description_for(route, default):
    return DESCRIPTIONS.get(route, default)
