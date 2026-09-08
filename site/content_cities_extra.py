# -*- coding: utf-8 -*-
"""Clermont and Montverde — added 2026-09-07 after the owner confirmed sibling
hubs may cover the same city as long as content isn't duplicated/textually
similar. Both pages deliberately take the large-lot/acreage/terrain angle
this site owns everywhere else, rather than a general suburban-contractor
angle — verified against windermereconcrete.com's live pages via an n-gram
similarity check (0 shared 8-grams) before publishing. Facts sourced from
research/01-radius-cities-south-lake.md and research/02-keyword-research-web-based.md.
"""
from _data import BUSINESS, SERVICES, CITY_OVERLAP_NOTE


def _disclosure():
    return f'<div class="disclosure-box">{BUSINESS["disclosure_short"]}</div>'


def _overlap_note():
    return f'<p class="calc-disclaimer">{CITY_OVERLAP_NOTE}</p>'


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
    # CLERMONT — rural/lake-edge angle, not the dense suburban core
    # ------------------------------------------------------------------
    clermont_faqs = [
        ("Does Groveland Concrete cover all of Clermont?",
         "No — we intentionally focus on the rural and lake-adjacent edges of Clermont: larger acreage parcels, properties near the Clermont chain of lakes, and long-driveway or boat-storage projects. Clermont's dense suburban core is well covered elsewhere; that's not the project type this site is built around."),
        ("Do you build boat pads near the Clermont chain of lakes?",
         "Yes. Lake Louisa, Lake Minneola, and Little Lake Harris all border or sit near Clermont, and a lakefront or near-lake property here often needs a dedicated concrete pad for boat and trailer storage rather than treating it as an afterthought on the driveway. See our RV & Boat Pads page for sizing and thickness."),
        ("Is Clermont a good fit for a long rural driveway?",
         "The larger, less-subdivided parcels on Clermont's outer edges — toward Groveland and Lake Louisa — are. Clermont's core neighborhoods are conventional suburban lots where a standard driveway page is the better fit; this page is specifically for the acreage side of the city."),
        ("Who handles building permits in Clermont?",
         "City of Clermont Building Services, 685 W Montrose St, Clermont, FL — homeowners submit in person, contractors typically use the eTRAKiT online portal. See our Permit Directory for the link."),
    ]

    clermont_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Clermont is a large, mostly suburban city — but its outer edges, especially toward Groveland and the Clermont chain of lakes, have the same large-lot, long-driveway, boat-and-RV-storage character the rest of this site is built around. That's the specific slice of Clermont this page covers.</p>
  {_overlap_note()}
  <div class="stat-row">
    <div class="stat-box"><span class="num">43,021</span><span class="lbl">Clermont population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">3+ lakes</span><span class="lbl">Lake Louisa, Lake Minneola, Little Lake Harris nearby</span></div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Why This Page Exists</span>
    <h2>The lake-and-acreage edge of Clermont, not the subdivision core</h2>
    <p>Most of Clermont's growth since 2000 has been conventional suburban subdivisions — that's not this site's focus. Where Clermont borders Groveland and the chain of lakes, though, you find larger parcels, lakefront properties, and the same boat-storage and long-driveway questions that define this site's catalog. If your property sits in Clermont's denser core, a standard driveway estimate is probably the right starting point rather than anything acreage-specific here.</p>
    {_service_links("concrete-driveways", "rv-and-boat-pads", "retaining-walls")}
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>City of Clermont Building Services</h2>
    <p>Clermont issues its own building permits — <strong>City of Clermont Building Services</strong>, 685 W Montrose St, Clermont, FL. Homeowners generally submit in person; contractors commonly use the eTRAKiT online portal. Confirm current requirements before you pour — see our <a href="/permits/">South Lake Permit Directory</a> for the direct link.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Clermont questions we actually get</h2>
    {_faq_html(clermont_faqs)}
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>On the acreage or lake side of Clermont?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/tools/driveway-cost-calculator/">Estimate a long driveway</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/clermont/",
        "title": "Concrete for Rural & Lakefront Clermont, FL Properties",
        "meta_description": "Long driveways, boat pads, and retaining walls for the acreage and chain-of-lakes edges of Clermont, FL — not a general suburban driveway page.",
        "h1": "Clermont — Acreage & Lake-Edge Properties",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Clermont", None)],
        "nav_active": "/service-area/",
        "body_html": clermont_body,
        "schema": [_faq_schema(clermont_faqs), _service_schema("Clermont, FL (rural/lake-adjacent properties)")],
    })

    # ------------------------------------------------------------------
    # MONTVERDE — Bella Collina estate-lot terrain angle
    # ------------------------------------------------------------------
    montverde_faqs = [
        ("Does Groveland Concrete work in Bella Collina?",
         "We cover the acreage and terrain side of Montverde properties, including large estate lots like those in Bella Collina (roughly 1.65–2.77 acres each). Our focus is the engineering questions that come with big, often sloped lots — long private driveways, retaining walls, and drainage — not decorative finish selection."),
        ("Why does a large Montverde lot need a retaining wall?",
         "Montverde sits in one of the hillier parts of Lake County, and an estate-sized lot often has real grade change across it. A retaining wall here is a drainage and erosion tool for a sloped site, not a landscaping accessory — see our Retaining Walls page for how we frame that."),
        ("How long are typical driveways in Montverde's estate communities?",
         "We don't have a confirmed average length for this research — lot sizes in Bella Collina alone run 1.65 to 2.77 acres, and driveway length depends heavily on setback and lot shape. Use our Driveway Cost & Volume Calculator with your own approximate length rather than a generic estimate."),
        ("Who handles building permits in Montverde?",
         "Town of Montverde Building/Permitting Department, with online applications through the Citizenserve portal. See our Permit Directory for the link."),
    ]

    montverde_body = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Montverde is a small town built around one very large draw: Bella Collina, a gated estate community with lots running 1.65 to 2.77 acres. That lot size — not a subdivision-scale driveway — is what this page is built around.</p>
  {_overlap_note()}
  <div class="stat-row">
    <div class="stat-box"><span class="num">1,655</span><span class="lbl">Montverde population, 2020 Census</span></div>
    <div class="stat-box"><span class="num">1.65–2.77 acres</span><span class="lbl">Typical Bella Collina estate lot size</span></div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Why This Page Exists</span>
    <h2>Estate-lot terrain, not finish selection</h2>
    <p>A lot this size usually means a long private driveway, real grade change across the property, and drainage that has to be planned rather than assumed. That's a structural and site-planning problem before it's a design one — which is why this page is about driveway length, slope, and retaining walls rather than stone patterns or finish options.</p>
    {_service_links("concrete-driveways", "retaining-walls", "concrete-patios")}
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Terrain</span>
    <h2>Rolling ground changes the plan</h2>
    <p>Montverde sits in a hillier stretch of Lake County than most of South Lake. On an estate-sized lot with real elevation change, a driveway's slope and a retaining wall's job (holding soil against a grade change, not decoration) both need to be sized for the actual terrain — see <a href="/retaining-walls/">Retaining Walls</a> and <a href="/tools/drainage-slope-planner/">Drainage & Slope Planner</a>.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Permits</span>
    <h2>Town of Montverde Building Department</h2>
    <p>Montverde issues its own building permits, with online applications handled through the Citizenserve portal. See our <a href="/permits/">South Lake Permit Directory</a> for the direct link.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">FAQ</span>
    <h2>Montverde &amp; Bella Collina questions</h2>
    {_faq_html(montverde_faqs)}
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Planning a project on a large Montverde lot?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/tools/driveway-cost-calculator/">Estimate your driveway</a>
    </div>
  </div>
</section>
'''.strip()

    pages.append({
        "route": "/montverde/",
        "title": "Concrete for Large Estate Lots in Montverde, FL",
        "meta_description": "Long driveways, retaining walls, and drainage planning for estate-sized lots in Montverde, FL, including Bella Collina — terrain and site planning, not finish selection.",
        "h1": "Montverde — Estate-Lot Terrain & Site Planning",
        "breadcrumbs": [("Home", "/"), ("Service Area", "/service-area/"), ("Montverde", None)],
        "nav_active": "/service-area/",
        "body_html": montverde_body,
        "schema": [_faq_schema(montverde_faqs), _service_schema("Montverde, FL (estate-lot properties)")],
    })

    return pages
