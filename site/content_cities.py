# -*- coding: utf-8 -*-
"""City / service-area pages for grovelandconcrete.com.

Every population figure, zoning note, permit-office name, and competitor
observation below is pulled from research/01-radius-cities-south-lake.md and
research/03-competitor-audit-top3.md. Where that research says a number or
claim isn't confirmed, this file omits it rather than inventing one.
"""
from _data import BUSINESS, SERVICES, TOOLS


def _disclosure():
    return f'<div class="disclosure-box">{BUSINESS["disclosure_short"]}</div>'


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


def _service_schema(area_served):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"Concrete & Hardscape Planning — {area_served}",
        "areaServed": area_served,
        "provider": {"@type": "Organization", "name": BUSINESS["legal_provider_placeholder"]},
    }


def _service_links(*keys):
    cards = "\n".join(
        f'''<div class="card">
      <h3><a href="{SERVICES[k]["route"]}">{SERVICES[k]["name"]}</a></h3>
      <p>{SERVICES[k]["short"]}</p>
    </div>''' for k in keys
    )
    return f'<div class="grid grid-3">{cards}</div>'


def get_pages():
    pages = []

    # ------------------------------------------------------------------
    # GROVELAND (anchor city)
    # ------------------------------------------------------------------
    groveland_faqs = [
        ("Who does concrete driveways in Groveland, FL?",
         "There are very few Groveland-dedicated concrete sites to compare — most search results for \"concrete contractor Groveland FL\" are general directories (BBB, Yellow Pages, Houzz) or single-page listings without pricing, photos, or a visible license number. That's an unusually open field compared to nearby Clermont. Groveland Concrete exists to give Groveland residents a real planning resource — specs, cost ranges, and permit information — before you request an estimate from a provider serving this area."),
        ("Do I need a permit for a concrete driveway in Groveland, FL?",
         "Permitting for work inside Groveland city limits goes through the City of Groveland Building Division, which runs an online eTRAKiT portal for applications and inspections. If your property is just outside the city line, in unincorporated Lake County, the jurisdiction is different — see our Permit Directory to confirm which office covers your address before you assume either way."),
        ("Is there a concrete contractor in Groveland who handles barn or workshop slabs?",
         "At least one Groveland-area concrete site lists \"barn concrete work\" as a service, which tells you there's real local demand for outbuilding and metal-building slabs — Groveland's rural edges (large agricultural parcels, some over 200 acres, being sold without HOA restrictions) are a natural fit for that kind of pour. See our Workshop Slabs page for the thickness and edge-detail questions to ask before you commit to one."),
    ]

    groveland_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Groveland is the anchor city for this site, and it's really two markets in one. Inside the city, Groveland has grown fast — the U.S. Census counted 18,505 residents in 2020, and more recent American Community Survey estimates put the population above 22,000. But 6.4% of that population still lives in a Census-defined rural area, and land listings on Groveland's edges regularly include agricultural parcels from roughly 2 to more than 200 acres, many sold without HOA restrictions and marketed for a homestead or family compound. A driveway, patio, or slab project can mean very different things depending on which side of that line your property sits on.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">18,505</span><span class="lbl">Population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">22,000+</span><span class="lbl">Est. population, ACS 2024</span></div>
    <div class="stat-box"><span class="num">93.6% / 6.4%</span><span class="lbl">Urban / rural population split (Census)</span></div>
    <div class="stat-box"><span class="num">2–200+ ac</span><span class="lbl">Range seen in edge-of-town land listings</span></div>
  </div>
  <p class="calc-disclaimer">Population figures above combine the official 2020 Census count with more recent third-party estimates (Census Reporter, city-data.com); treat the newer numbers as approximate rather than official. They're included to show the pace of growth, not as a precise current count.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Two Groveland Markets</span>
    <h2>Growing subdivisions, and the rural edge that hasn't caught up to them</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Inside city subdivisions</h3>
        <p>Most new Groveland construction is conventional residential — standard lots, standard driveway approaches, sidewalks tied to a city right-of-way. See our <a href="/concrete-driveways/">Concrete Driveways</a> page for the specs a Groveland permit reviewer will actually check.</p>
      </div>
      <div class="card">
        <h3>Large agricultural parcels on the edges</h3>
        <p>Land searches around Groveland turn up plenty of multi-acre, non-HOA parcels — the kind of property where a driveway can run several hundred feet and a mixer truck's access isn't guaranteed. Our <a href="/tools/site-access-checklist/">site-access checklist</a> is built for exactly that situation.</p>
      </div>
      <div class="card">
        <h3>Barn and outbuilding demand</h3>
        <p>At least one Groveland-area concrete listing calls out "barn concrete work" specifically — a sign that outbuilding and metal-building slabs are a real, if under-served, category here. See <a href="/workshop-slabs/">Workshop Slabs</a> for thickness and vapor-barrier decisions.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>Who reviews concrete work inside Groveland city limits</h2>
    <p>Projects within Groveland's city limits are permitted through the <strong>City of Groveland Building Division</strong>, which processes applications and schedules inspections through its online eTRAKiT portal. If your parcel sits just outside the city line, permitting shifts to Lake County Building Services instead — the two jurisdictions aren't interchangeable, and confirming which one covers your address before you pour can save a stop-work order later. Full contact details and portal links are in our <a href="/permits/">South Lake Permit Directory</a>.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">What's Actually Out There</span>
    <h2>Why Groveland is thin on real local concrete content</h2>
    <p>Search for a Groveland concrete contractor today and most of what comes back is generic directory listings rather than dedicated local sites — a noticeably more open field than a market like Clermont, where several competing sites are well established. That's good news if you're trying to compare real options, but it also means less independent information is published about local pricing, permitting, or the specific challenges of building on a large or rural Groveland lot. That gap is what this page and the linked service pages are meant to fill.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Plan Your Project</span>
    <h2>Services relevant to Groveland properties</h2>
    {_service_links("concrete-driveways", "rv-and-boat-pads", "workshop-slabs", "concrete-patios")}
  </div>
</section>

<div class="wrap">{_disclosure()}</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Groveland concrete questions</h2>
    {_faq_html(groveland_faqs)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning concrete or hardscape work in Groveland?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/driveway-cost-calculator/">Estimate cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/groveland/",
        "title": "Concrete & Hardscape Planning in Groveland, FL",
        "meta_description": "Driveways, RV/boat pads, and workshop slabs for Groveland, FL — city subdivisions and rural edge lots, permit jurisdiction, and real local cost ranges.",
        "h1": "Groveland, FL",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Groveland", None)],
        "nav_active": "/service-area/",
        "body_html": groveland_body,
        "schema": [_faq_schema(groveland_faqs), _service_schema("Groveland, FL")],
    })

    # ------------------------------------------------------------------
    # MASCOTTE
    # ------------------------------------------------------------------
    mascotte_faqs = [
        ("Is there a concrete contractor that actually serves Mascotte, FL?",
         "Mascotte shows the same pattern as Groveland — most of what turns up in a search is a competitor based in a neighboring city rather than a business built around Mascotte itself. That's a gap for residents trying to find someone who understands the town's specific mix of older in-town lots and larger parcels on its western edge."),
        ("What kind of properties are common in Mascotte?",
         "Mascotte calls itself the \"Gateway to South Lake County,\" and its housing reflects a town in transition — craftsman-style bungalows on conventional in-town lots close to the center, and ranch-style homes on larger, more isolated parcels to the west. Agricultural land in the 8- to 80-plus-acre range, including some former citrus and tree-nursery operations, is still available on the town's edges, per current land listings."),
        ("Do I need a permit for a driveway or slab in Mascotte, FL?",
         "Work inside Mascotte's city limits is permitted through the City of Mascotte Building Department, which uses an online iworq portal for applications. Confirm the exact requirements for your project with that office, or check our Permit Directory for the current contact and portal link — that page also covers unincorporated Lake County if your parcel is outside city limits."),
    ]

    mascotte_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Mascotte is smaller than Groveland but growing quickly — the 2020 Census counted 6,609 residents, up nearly 30% from 5,101 in 2010, and more recent estimates put the population closer to 7,400–9,150 depending on the source. The town markets itself as the "Gateway to South Lake County," and its housing stock tells that story: about 80% of the population is in a Census-defined urban area, with the remaining 20% on larger, more rural parcels — many still tied to Mascotte's agricultural past.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">6,609</span><span class="lbl">Population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">+29.6%</span><span class="lbl">Growth, 2010–2020 Census</span></div>
    <div class="stat-box"><span class="num">79.9% / 20.1%</span><span class="lbl">Urban / rural population split (Census)</span></div>
    <div class="stat-box"><span class="num">8–80+ ac</span><span class="lbl">Agricultural lot sizes seen on the edges</span></div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">A Town Between Two Eras</span>
    <h2>Citrus roots, suburban growth</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>In-town lots</h3>
        <p>Craftsman-style bungalows on conventional lots close to Mascotte's center are a common project type — driveways, sidewalks, and patios sized like a typical residential job. See <a href="/concrete-driveways/">Concrete Driveways</a>.</p>
      </div>
      <div class="card">
        <h3>Western edge acreage</h3>
        <p>Ranch-style homes on larger, more isolated lots to the west of town are common, alongside agricultural parcels still being sold in the 8- to 80-plus-acre range, including former tree-nursery land. Longer approaches and rural-lot access questions come up more here than in-town.</p>
      </div>
      <div class="card">
        <h3>Room for RV and workshop needs</h3>
        <p>The same acreage properties that support agricultural use are often a good fit for an RV pad, a boat pad, or a workshop slab. See <a href="/rv-and-boat-pads/">RV &amp; Boat Pads</a> and <a href="/workshop-slabs/">Workshop Slabs</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>Where Mascotte permits are handled</h2>
    <p>Projects inside Mascotte city limits go through the <strong>City of Mascotte Building Department</strong>, which runs applications through an online iworq portal. If your property sits outside city limits, Lake County Building Services is the jurisdiction instead. Confirm which one applies to your address, and get current contact details, in our <a href="/permits/">South Lake Permit Directory</a>.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Local Market Note</span>
    <h2>Mascotte has less direct competition than you'd expect</h2>
    <p>Like Groveland, Mascotte doesn't have much dedicated concrete-contractor content of its own — most search results are competitors headquartered in neighboring cities, reaching into Mascotte rather than being built around it. That's a real opening for anyone comparing options locally: there simply isn't much independent, Mascotte-specific pricing or planning information published yet.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Plan Your Project</span>
    <h2>Services relevant to Mascotte properties</h2>
    {_service_links("concrete-driveways", "workshop-slabs", "rv-and-boat-pads", "sidewalks-walkways")}
  </div>
</section>

<div class="wrap">{_disclosure()}</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Mascotte concrete questions</h2>
    {_faq_html(mascotte_faqs)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning concrete or hardscape work in Mascotte?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/driveway-cost-calculator/">Estimate cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/mascotte/",
        "title": "Concrete & Hardscape Planning in Mascotte, FL",
        "meta_description": "Driveways, workshop slabs, and RV pads for Mascotte, FL — in-town lots and western acreage, permit jurisdiction, and real cost ranges.",
        "h1": "Mascotte, FL",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Mascotte", None)],
        "nav_active": "/service-area/",
        "body_html": mascotte_body,
        "schema": [_faq_schema(mascotte_faqs), _service_schema("Mascotte, FL")],
    })

    # ------------------------------------------------------------------
    # MINNEOLA
    # ------------------------------------------------------------------
    minneola_faqs = [
        ("Is Minneola a good fit for new-construction concrete work?",
         "Yes — Minneola is in the middle of one of South Lake County's largest planned developments. \"Hills of Minneola\" is a multi-builder master-planned community (builders reported include Del Webb, Dream Finders, Meritage, Lennar, Ashton Woods, and Starlight Homes) bringing thousands of single-family homes, townhomes, and apartments, plus a town center anchored by a Walmart and Sam's Club. That kind of growth means a steady pipeline of new driveways, sidewalks, and patios."),
        ("Do concrete contractors in Minneola mention RV, boat, or workshop pads?",
         "Not in what we found. Existing Minneola-area concrete listings mention handling \"heavy vehicles\" in general terms but don't call out RV pads, boat pads, or workshop slabs as their own category, and none mention serving builders or larger adjacent rural lots specifically — even though Minneola sits right next to that kind of property."),
        ("Do I need a permit for concrete work in Minneola, FL?",
         "Minneola's Building Department is operated through a third-party provider (SafeBuilt) rather than staffed entirely in-house, and applications route through City Hall. Confirm current requirements and contact information in our Permit Directory before you schedule a pour."),
    ]

    minneola_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Minneola is the fastest-growing city in this service area, and almost all of that growth is planned, high-density residential construction rather than rural or agricultural land. The 2020 Census put the population at 13,843; more recent estimates run from about 16,600 (ACS 2024) up to nearly 19,700 depending on the source. The driver behind those numbers is "Hills of Minneola," a multi-builder master-planned community bringing thousands of new homes, townhomes, and apartments, along with a town center anchored by big-box retail.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">13,843</span><span class="lbl">Population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">16,600+</span><span class="lbl">Est. population, ACS 2024</span></div>
    <div class="stat-box"><span class="num">Thousands</span><span class="lbl">Planned units, Hills of Minneola</span></div>
    <div class="stat-box"><span class="num">6+</span><span class="lbl">Builders reported in the development</span></div>
  </div>
  <p class="calc-disclaimer">Population estimates above vary by source (Census Reporter's ACS figure vs. city-data.com); treat anything past the 2020 Census count as an approximation of a fast-moving number, not a fixed total.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Growth Profile</span>
    <h2>A subdivision boom, not a rural market</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>New-construction driveways &amp; walkways</h3>
        <p>New subdivisions mean a steady volume of standard driveway pours and sidewalk connections tied to new streets. See <a href="/concrete-driveways/">Concrete Driveways</a> and <a href="/sidewalks-walkways/">Sidewalks &amp; Walkways</a>.</p>
      </div>
      <div class="card">
        <h3>Paver interest in newer builds</h3>
        <p>Master-planned communities often skew toward decorative finishes for driveways and patios. See <a href="/paver-driveways/">Paver Driveways</a> and <a href="/paver-patios/">Paver Patios</a>, or our <a href="/compare/paver-vs-concrete-driveway/">paver vs. concrete comparison</a> before deciding.</p>
      </div>
      <div class="card">
        <h3>Patios in new backyards</h3>
        <p>New homes generally arrive without an outdoor living space finished — <a href="/concrete-patios/">Concrete Patios</a> covers the finish options that hold up to Central Florida heat and rain.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>Minneola's permitting process</h2>
    <p>Minneola's Building Department operates with third-party plan review and inspection support rather than an entirely in-house team, and applications are handled through City Hall. If your project is outside city limits, Lake County Building Services is the relevant office instead. Current contact details for both are in our <a href="/permits/">South Lake Permit Directory</a>.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Local Market Note</span>
    <h2>A gap between the growth and the content about it</h2>
    <p>Despite the scale of the Hills of Minneola development, the concrete-contractor sites we found serving Minneola don't speak to that boom directly — no mention of working with builders, no acknowledgment of the larger, more rural parcels sitting just outside the new subdivisions, and only vague language about handling "heavy vehicles" rather than naming RV, boat, or workshop slabs as their own service. That's the gap Groveland Concrete's service pages are built to close.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Plan Your Project</span>
    <h2>Services relevant to Minneola properties</h2>
    {_service_links("concrete-driveways", "paver-driveways", "sidewalks-walkways", "concrete-patios")}
  </div>
</section>

<div class="wrap">{_disclosure()}</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Minneola concrete questions</h2>
    {_faq_html(minneola_faqs)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning concrete or hardscape work in Minneola?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/driveway-cost-calculator/">Estimate cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/minneola/",
        "title": "Concrete & Hardscape Planning in Minneola, FL",
        "meta_description": "Driveways, sidewalks, and patios for Minneola, FL new construction — Hills of Minneola growth context, permit jurisdiction, and cost ranges.",
        "h1": "Minneola, FL",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Minneola", None)],
        "nav_active": "/service-area/",
        "body_html": minneola_body,
        "schema": [_faq_schema(minneola_faqs), _service_schema("Minneola, FL")],
    })

    # ------------------------------------------------------------------
    # HOWEY-IN-THE-HILLS
    # ------------------------------------------------------------------
    howey_faqs = [
        ("How big is Howey-in-the-Hills, really?",
         "Small. The 2020 Census counted 1,643 residents, and even the higher third-party estimates only put it around 1,700–2,150. It's a village, not a suburb — which is exactly why there's very little dedicated concrete-contractor content specific to it. We're not aware of any confirmed, dedicated competitor content for Howey-in-the-Hills at the time of writing, so treat this page as a starting point, not a competitive landscape."),
        ("Is there new construction coming to Howey-in-the-Hills?",
         "Yes — a 220-acre site was acquired in 2025 for a planned 560-home active-adult (55+) community, a significant project relative to the town's current size. That's a real, if forward-looking, source of demand for new driveways, walkways, and patios in the next few years."),
        ("Who handles building permits in Howey-in-the-Hills?",
         "The Town of Howey-in-the-Hills' Building Services function is handled by an outside engineering firm rather than fully in-house staff, with applications going through a Citizen Portal. Confirm current details in our Permit Directory before starting a project."),
    ]

    howey_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Howey-in-the-Hills is the smallest place in this service area, and we want to be upfront about that: with 1,643 residents at the 2020 Census, there isn't the volume of population or public data that a page like our Groveland or Minneola one can draw on. What research does confirm is a distinct character — a lakefront village on Little Lake Harris, founded as an agricultural settlement, still carrying Spanish Revival architecture from the 1920s alongside golf-course homes and newer acreage parcels.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">1,643</span><span class="lbl">Population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">92% / 8%</span><span class="lbl">Urban / rural population split (Census)</span></div>
    <div class="stat-box"><span class="num">220 ac</span><span class="lbl">Site for a planned 55+ community (2025)</span></div>
    <div class="stat-box"><span class="num">560</span><span class="lbl">Homes planned in that community</span></div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">A Village, Not a Suburb</span>
    <h2>What's actually there</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Historic lakefront core</h3>
        <p>Little Lake Harris frontage means boat storage and boat pad questions come up naturally here — see <a href="/rv-and-boat-pads/">RV &amp; Boat Pads</a> for the difference between a rolling-load RV pad and a boat/trailer pad.</p>
      </div>
      <div class="card">
        <h3>Golf-course and acreage homes</h3>
        <p>Mixed lot types — from historic in-town parcels to larger acreage near the golf course — mean project scope varies a lot house to house. <a href="/concrete-driveways/">Concrete Driveways</a> covers both a short in-town approach and a longer rural one.</p>
      </div>
      <div class="card">
        <h3>Rolling terrain</h3>
        <p>"Hills" isn't just the name — sloped lots are common enough here that drainage and retaining are worth planning for early. See <a href="/retaining-walls/">Retaining Walls</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>Building Services in Howey-in-the-Hills</h2>
    <p>The Town of Howey-in-the-Hills' Building Services are handled through an outside engineering firm rather than a fully in-house department, with applications submitted through a Citizen Portal. Confirm current contact information and requirements in our <a href="/permits/">South Lake Permit Directory</a> before scheduling a pour.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Honest Note</span>
    <h2>Why this page is shorter than our other city pages</h2>
    <p>Howey-in-the-Hills simply doesn't have the population, development pipeline, or published local market data that Groveland, Mascotte, or Minneola do — and we'd rather say that plainly than pad this page with generic filler. The one concrete signal worth tracking is the planned 560-home active-adult community announced in 2025, which points to real future demand even if it isn't reflected in the town's current size.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Plan Your Project</span>
    <h2>Services relevant to Howey-in-the-Hills properties</h2>
    {_service_links("concrete-driveways", "rv-and-boat-pads", "concrete-patios", "retaining-walls")}
  </div>
</section>

<div class="wrap">{_disclosure()}</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Howey-in-the-Hills concrete questions</h2>
    {_faq_html(howey_faqs)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning concrete or hardscape work in Howey-in-the-Hills?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/driveway-cost-calculator/">Estimate cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/howey-in-the-hills/",
        "title": "Concrete & Hardscape Planning in Howey-in-the-Hills, FL",
        "meta_description": "Driveways, boat pads, and patios for Howey-in-the-Hills, FL — lakefront village character, planned 55+ growth, and permit jurisdiction.",
        "h1": "Howey-in-the-Hills, FL",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Howey-in-the-Hills", None)],
        "nav_active": "/service-area/",
        "body_html": howey_body,
        "schema": [_faq_schema(howey_faqs), _service_schema("Howey-in-the-Hills, FL")],
    })

    # ------------------------------------------------------------------
    # RURAL & UNINCORPORATED LAKE COUNTY
    # ------------------------------------------------------------------
    rural_faqs = [
        ("What zoning applies to rural properties in unincorporated Lake County?",
         "Large unincorporated tracts are commonly zoned Agriculture (A) under Lake County's Comprehensive Plan, with land-use categories like \"Green Swamp Rural\" and \"Rural Transition\" governing what's allowed. Equestrian uses — stables, riding academies — are permitted with a Conditional Use Permit, and mobile or manufactured homes generally require a minimum 5-acre lot in agricultural or rural-residential zones. This is county-level policy, not a Groveland Concrete determination — confirm specifics for your parcel with Lake County Planning & Zoning."),
        ("Do I need a driveway permit in unincorporated Lake County?",
         "Permitting for unincorporated parcels goes through Lake County Building Services rather than any city building department — a different office and process than Groveland, Mascotte, Minneola, or Howey-in-the-Hills use. See our Permit Directory for current contact information and the online portal."),
        ("Is unincorporated Lake County a good fit for a long driveway or RV pad?",
         "It's close to the ideal fit for this site's core services. The 5-acre minimum lot size common in agricultural and rural-residential zoning, combined with permitted equestrian and agricultural uses, points strongly toward large lots, long driveway runs, and properties set up for RVs, trailers, and outbuildings — exactly the projects covered on our Long Driveways, RV &amp; Boat Pads, and Workshop Slabs pages."),
        ("Does a concrete truck need special access on a rural Lake County property?",
         "Often, yes. A long, narrow, gated, or tree-lined approach on a large agricultural parcel isn't guaranteed to give a loaded mixer truck the roughly 10–12 ft of clear width and 14 ft of vertical clearance it needs to maneuver. Run through our site-access checklist before assuming standard truck access will work."),
    ]

    rural_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">This isn't a city — it's the large, unincorporated stretch of Lake County that sits between and around Groveland, Mascotte, Minneola, and Howey-in-the-Hills. Lake County as a whole counted 383,956 residents at the 2020 Census, but there's no single published figure for just the unincorporated South Lake area; what's well documented instead is the zoning, and it points squarely at the kind of property this site is built around.</p>
  <div class="stat-row">
    <div class="stat-box"><span class="num">383,956</span><span class="lbl">Lake County population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">5 acres</span><span class="lbl">Min. lot for manufactured homes, ag/rural-residential zones</span></div>
    <div class="stat-box"><span class="num">Agriculture (A)</span><span class="lbl">Common zoning designation</span></div>
    <div class="stat-box"><span class="num">CUP</span><span class="lbl">Required for stables/riding academies</span></div>
  </div>
  <p class="calc-disclaimer">There's no confirmed population figure specific to just the unincorporated South Lake area in the research behind this page — the county-wide number above is included for scale, not as a local count.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">What The Zoning Tells Us</span>
    <h2>Agricultural and equestrian, by design</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Large-lot agricultural zoning</h3>
        <p>Lake County's Comprehensive Plan uses land-use categories like "Green Swamp Rural" and "Rural Transition" across much of the unincorporated county, with a 5-acre minimum lot size for manufactured homes in agricultural and rural-residential zones — a strong signal that big parcels, not subdivision lots, are the norm.</p>
      </div>
      <div class="card">
        <h3>Equestrian uses are built in</h3>
        <p>Stables and riding academies are permitted uses here, subject to a Conditional Use Permit — which lines up with the horse properties and equestrian-oriented lots common across this part of the county.</p>
      </div>
      <div class="card">
        <h3>The exact right property type for this site's services</h3>
        <p>Long driveways, RV pads, boat pads, and workshop slabs are all built for large-lot, rural properties like these — see <a href="/concrete-driveways/">Concrete Driveways</a>, <a href="/rv-and-boat-pads/">RV &amp; Boat Pads</a>, and <a href="/workshop-slabs/">Workshop Slabs</a>.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>Lake County Building Services handles this area</h2>
    <p>Unincorporated parcels are permitted through <strong>Lake County Building Services</strong> and Lake County Planning &amp; Zoning — not through any city building department. That's a meaningfully different process than the four incorporated cities in this service area use, with its own portal, timelines, and appointment-based service windows. Confirm current contact details and the online application portal in our <a href="/permits/">South Lake Permit Directory</a> before scheduling any work, including a Conditional Use Permit application for equestrian facilities.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Long-Driveway Reality</span>
    <h2>Why acreage properties change the math</h2>
    <p>On a 5-plus-acre parcel, the driveway itself often stops being a small line item and becomes one of the bigger decisions in the project. Length changes pricing more than a flat per-project cost range accounts for, base preparation on Central Florida's sandy soil matters more over a longer run, and getting a loaded mixer truck down a long, gated, or tree-lined approach isn't something to assume — it's something to check. Use our <a href="/tools/driveway-cost-calculator/">Driveway Cost &amp; Volume Calculator</a> and <a href="/tools/site-access-checklist/">site-access checklist</a> before you get a quote, not after.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Plan Your Project</span>
    <h2>Services built for rural Lake County properties</h2>
    {_service_links("concrete-driveways", "rv-and-boat-pads", "workshop-slabs", "retaining-walls")}
  </div>
</section>

<div class="wrap">{_disclosure()}</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Rural & unincorporated Lake County questions</h2>
    {_faq_html(rural_faqs)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning concrete work on a rural Lake County property?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/tools/driveway-cost-calculator/">Estimate cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="/contact/">Request a free estimate</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/rural-lake-county/",
        "title": "Concrete Planning for Rural & Unincorporated Lake County, FL",
        "meta_description": "Long driveways, RV/boat pads, and workshop slabs for agricultural and equestrian-zoned unincorporated Lake County, FL — zoning, permits, and truck access.",
        "h1": "Rural & Unincorporated Lake County",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Rural & Unincorporated Lake County", None)],
        "nav_active": "/service-area/",
        "body_html": rural_body,
        "schema": [_faq_schema(rural_faqs), _service_schema("Unincorporated Lake County, FL")],
    })

    return pages
