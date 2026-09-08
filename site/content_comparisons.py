# -*- coding: utf-8 -*-
"""Side-by-side comparison pages — one page per route in _data.COMPARISONS.

Each page carries a real decision-factor table plus prose grounded in the
site's own research (research/02, research/05). Cost or performance claims
sourced from competitor content, rather than a code/standard, are labeled
as such instead of being presented as independently verified data.
"""
from _data import BUSINESS, COMPARISONS


def _disclosure():
    return f'<p class="disclosure-box">{BUSINESS["disclosure_short"]}</p>'


def _cta(heading, links, lede=None):
    btns = "\n".join(
        f'<a class="btn {cls} btn-lg" href="{href}">{label}</a>'
        for href, label, cls in links
    )
    lede_html = f'<p class="lede" style="margin:0 auto 20px">{lede}</p>' if lede else ""
    return f'''
<section>
  <div class="wrap" style="text-align:center">
    <h2>{heading}</h2>
    {lede_html}
    <div class="cta-row" style="justify-content:center">{btns}</div>
    {_disclosure()}
  </div>
</section>'''


def _page(key, meta_description, body_html, schema=None):
    c = COMPARISONS[key]
    page = {
        "route": c["route"],
        "title": c["name"],
        "meta_description": meta_description,
        "h1": c["name"],
        "breadcrumbs": [("Home", "/"), ("Guides", "/guides/"), (c["name"], None)],
        "nav_active": "/guides/",
        "body_html": body_html,
    }
    if schema:
        page["schema"] = schema
    return page


def get_pages():
    pages = []

    # 1 — Rebar vs. Wire Mesh --------------------------------------------
    body1 = f'''
<div class="wrap" style="padding-bottom:10px">
  <p class="lede">This is one of the more technical decisions in a driveway build, and it's also one of the clearest — the industry consensus is strong enough that some jurisdictions won't accept wire mesh alone for a driveway carrying vehicle loads.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Side by Side</span>
    <h2>Rebar vs. wire mesh, factor by factor</h2>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Factor</th><th>Rebar</th><th>Wire mesh</th></tr></thead>
      <tbody>
        <tr><td>Typical spec</td><td>#3 or #4 bar, 12–18 in centers</td><td>6x6 or similar welded wire grid</td></tr>
        <tr><td>Cost</td><td>Higher material and labor cost (chairs, tying)</td><td>Lower material cost, faster to lay out</td></tr>
        <tr><td>Behavior during the pour</td><td>Set on chairs, holds its position as concrete is placed</td><td>Light and flexible — easily pushed to the bottom of the slab if not carefully held up during the pour</td></tr>
        <tr><td>Performance after a crack starts</td><td>Continues holding the two sides of a crack together, since it stays positioned mid-slab</td><td>Does little once out of position — often ends up near the bottom of the slab where it can't do its job</td></tr>
        <tr><td>Code / jurisdiction acceptance</td><td>Broadly accepted for vehicle-bearing slabs</td><td>Some jurisdictions won't accept wire mesh alone for a driveway</td></tr>
        <tr><td>Best fit</td><td>Any slab carrying vehicle loads — driveways, RV/boat pads, workshop slabs</td><td>Lighter-duty applications with minimal load, if used at all</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Why Rebar Wins for Driveways</span>
    <h2>It's not about strength on day one — it's about what happens after</h2>
    <p>Both materials are meant to do the same basic job: hold concrete together across the crack that's going to happen eventually (see our <a href="/guides/why-concrete-driveway-cracking/">cracking guide</a> for why cracking is normal, not a failure). The difference is what happens in practice. Rebar is rigid enough to be set on chairs and tied into a grid that keeps its position through the pour, placing it at the correct depth within the slab where it can actually resist the two sides of a future crack pulling apart. Wire mesh is thin and springy — it's genuinely difficult to keep it from getting stepped on, walked over, or simply sinking as concrete is poured and worked around it, unless a crew is deliberately pulling it up into position as they go. Once it's settled near the bottom of the slab instead of mid-depth, it's not doing the job it was installed for.</p>
    <p>That practical reality — not a lab test — is the main reason rebar is the more reliable choice for anything carrying vehicle loads, and it's part of why some municipalities have moved to require it (or at minimum, won't sign off on wire mesh alone) for driveways specifically.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Where Mesh Still Shows Up</span>
    <h2>It isn't automatically wrong — just rarely the right call under a driveway</h2>
    <p>Wire mesh isn't a discontinued product; it still gets specified for some lighter-duty flatwork where cost matters more than long-term crack control and the load is minimal. But for a residential driveway, RV or boat pad, or workshop slab — the categories this site covers — rebar sized to the expected load is the standard recommendation, and it's what a permit reviewer is more likely to expect to see called out on a driveway plan.</p>
  </div>
</section>
'''.strip() + _cta(
        "Specifying reinforcement for your pour?",
        [
            ("/concrete-driveways/", "See full driveway specs", "btn-primary"),
            ("/tools/driveway-cost-calculator/", "Estimate cost &amp; volume", "btn-outline"),
        ],
    )
    pages.append(_page(
        "rebar-vs-wire-mesh",
        "Rebar vs. wire mesh for a concrete driveway, compared factor by factor — cost, pour behavior, crack performance, and why some jurisdictions won't accept mesh alone.",
        body1,
    ))

    # 2 — Paver vs. Concrete Driveway --------------------------------------
    body2 = f'''
<div class="wrap" style="padding-bottom:10px">
  <p class="lede">Regional Florida competitors already make this comparison, usually to sell pavers — arguing that jointed paver units resist Florida's heat and rain better than a solid concrete slab. That's worth engaging with honestly rather than dismissing, but it's also worth being clear about which parts of that argument are competitor marketing and which parts are simply how the two materials behave.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Side by Side</span>
    <h2>Concrete vs. pavers, factor by factor</h2>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Factor</th><th>Poured concrete</th><th>Pavers</th></tr></thead>
      <tbody>
        <tr><td>Upfront cost</td><td>Lower — roughly $6–$10/sq ft for a broom finish (published Florida range)</td><td>Higher — regional Florida paver installers commonly cite roughly $10–$30/sq ft, depending on material and pattern</td></tr>
        <tr><td>Visible cracking</td><td>A solid slab shows cracks as a continuous line across the surface</td><td>Individual units can shift or settle without a visible "crack" the way a slab shows one</td></tr>
        <tr><td>Repair approach</td><td>Patch, resurface, or replace the affected section — repairs can be visible against the original pour</td><td>Lift and reset or swap individual units — often blends in better than a concrete patch</td></tr>
        <tr><td>Drainage</td><td>Relies entirely on slope, since the surface is solid</td><td>Joints between units allow some water infiltration in addition to surface slope</td></tr>
        <tr><td>Base preparation</td><td>Compacted base required either way</td><td>Compacted base required either way — sandy Central Florida soil matters for both (see our <a href="/guides/best-base-sandy-soil-florida/">base prep guide</a>)</td></tr>
        <tr><td>Ongoing maintenance</td><td>Occasional sealing, joint cleaning</td><td>Periodic joint-sand refresh and weed/ant control between units</td></tr>
        <tr><td>Long-term cost picture</td><td>Lower upfront, repairs less "invisible"</td><td>Higher upfront, competitor claim is lower maintenance cost over roughly 20 years — not independently verified here</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">The Competitor Claim, Examined</span>
    <h2>Do pavers really handle Florida's heat and rain better?</h2>
    <p class="disclosure-box">Regional paver installers (serving the greater Orlando/Central Florida market) argue that pavers resist thermal cracking better than a solid concrete slab and drain more effectively through their joints. Both claims have a real mechanism behind them — jointed units do have more room to move with thermal expansion than a continuous slab, and open joints do let some water pass through rather than requiring it all to run off the surface. What we haven't verified independently is how much that translates into a measurable durability or maintenance advantage specifically in South Lake County's climate and soil. Treat these as directionally reasonable points made by installers who sell pavers, not as neutral third-party findings.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">What Actually Drives the Decision</span>
    <h2>Budget now vs. a different maintenance profile later</h2>
    <p>For most South Lake County projects, this comes down to upfront budget against a willingness to do different (not necessarily less) ongoing maintenance. Concrete costs less to install and its cracking, when it happens, is normal and manageable (see our <a href="/guides/why-concrete-driveway-cracking/">cracking guide</a>) — but a crack is visible as a crack. Pavers cost more upfront and trade that for a repair process that can look cleaner section-by-section, plus periodic joint maintenance concrete doesn't need. Neither is objectively "better" — they're different trade-offs.</p>
  </div>
</section>
'''.strip() + _cta(
        "Deciding between concrete and pavers?",
        [
            ("/concrete-driveways/", "See concrete driveway specs", "btn-primary"),
            ("/paver-driveways/", "See paver driveway installation details", "btn-outline"),
        ],
    )
    pages.append(_page(
        "paver-vs-concrete-driveway",
        "Concrete vs. paver driveways in Florida, compared honestly — cost, cracking, drainage, and repair — including what's a documented tradeoff vs. a competitor's marketing claim.",
        body2,
    ))

    # 3 — Stamped vs. Plain Patio -------------------------------------------
    body3 = f'''
<div class="wrap" style="padding-bottom:10px">
  <p class="lede">This decision comes up constantly once someone starts pricing out a patio, and it's less about which one is "better" and more about how much you value a decorative pattern against a lower-maintenance, lower-cost surface.</p>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Side by Side</span>
    <h2>Stamped vs. plain, factor by factor</h2>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Factor</th><th>Stamped concrete</th><th>Plain (broom/trowel) finish</th></tr></thead>
      <tbody>
        <tr><td>Upfront cost</td><td>Higher — color hardener, release agent, stamping labor, and sealer all add cost on top of the base slab</td><td>Lower — a standard broom or trowel finish without the extra material and labor steps</td></tr>
        <tr><td>Appearance</td><td>Textured pattern that can mimic stone, brick, or tile</td><td>Uniform, simple surface</td></tr>
        <tr><td>Maintenance</td><td>Needs periodic resealing to maintain color, sheen, and surface protection</td><td>Lower maintenance — no decorative coating relying on a reseal cycle</td></tr>
        <tr><td>Slip resistance</td><td>Pattern grooves can add texture, but a smooth sealer topcoat can offset that if over-applied</td><td>A broom finish is specifically textured for slip resistance and is the standard choice for that reason</td></tr>
        <tr><td>Heat underfoot</td><td>Darker color options can absorb more heat in direct Florida sun (general color-and-heat principle, not a study of this product specifically)</td><td>Lighter, more traditional finishes are less prone to this</td></tr>
        <tr><td>Crack repair visibility</td><td>A crack running through a pattern can be harder to patch invisibly</td><td>A patch on a plain surface can sometimes blend in more easily, though color and texture matching is never perfect</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Why the Cost Gap Exists</span>
    <h2>You're paying for extra steps, not just a look</h2>
    <p>Stamped concrete isn't just concrete with a pattern pressed into it as an afterthought — it involves color hardener worked into the surface, a release agent to keep the stamping tools from sticking, careful timing during the pour so the concrete is workable enough to stamp but firm enough to hold the impression, and a sealer to lock in the color and pattern afterward. Each of those is additional material and skilled labor on top of the base slab cost, which is why stamped patios reliably cost more than a plain finish — we're not going to put a specific percentage on that gap here, since it varies with pattern complexity, color count, and installer, and we don't have a Florida-specific figure we're confident citing.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Climate Considerations</span>
    <h2>What actually matters for a Central Florida backyard</h2>
    <p>Two climate-related points are worth thinking through before choosing a finish. First, slip resistance: a patio gets wet often here, between rain and general outdoor living, so whichever finish you choose should have real texture underfoot — a heavily sealed, glossy stamped surface can end up slicker than a standard broom finish if it's over-sealed. Second, heat: darker stamped color choices sit in direct Florida sun and can get noticeably hot underfoot in summer, the same general principle that makes dark pavement hotter than light pavement — this is basic color-and-heat behavior, not a finding specific to any stamped concrete product, so weigh it against how the patio will actually be used (bare feet by a pool vs. a covered lanai floor, for example).</p>
  </div>
</section>
'''.strip() + _cta(
        "Choosing a finish for your patio?",
        [
            ("/concrete-patios/", "See patio finish options", "btn-primary"),
            ("/contact/", "Ask about a specific pattern or color", "btn-outline"),
        ],
    )
    pages.append(_page(
        "stamped-vs-plain-patio",
        "Stamped concrete vs. a plain broom-finish patio, compared on cost, maintenance, slip resistance, and heat underfoot in Central Florida's climate.",
        body3,
    ))

    return pages
