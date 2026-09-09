# -*- coding: utf-8 -*-
from _data import BUSINESS, SERVICES, TOOLS, CITIES, GUIDES

# ---------------------------------------------------------------------------
# 1) RV & Boat Pad Calculator
# ---------------------------------------------------------------------------

RV_CALC_JS = '''
(function () {
  var form = document.getElementById("rvCalc");
  if (!form) return;
  var result = document.getElementById("rvResult");

  var PRESETS = {
    "class-b": [20, 10],
    "travel-trailer": [28, 12],
    "class-c": [30, 12],
    "class-a": [40, 14],
    "boat-trailer": [26, 10]
  };
  var THICKNESS_IN = 6;
  var LOW_PER_SQFT = 8;
  var HIGH_PER_SQFT = 16;
  var FLOOR_LOW = 1800;
  var FLOOR_HIGH = 1980;

  function fmt(n) { return n.toLocaleString("en-US", { maximumFractionDigits: 1 }); }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }

  form.preset.addEventListener("change", function () {
    var p = PRESETS[form.preset.value];
    if (p) {
      form.length.value = p[0];
      form.width.value = p[1];
    }
    calc();
  });
  form.addEventListener("input", calc);
  form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });

  function calc() {
    var length = parseFloat(form.length.value) || 0;
    var width = parseFloat(form.width.value) || 0;
    var waste = parseFloat(form.waste.value) || 10;

    if (length <= 0 || width <= 0) {
      result.hidden = true;
      return;
    }

    var areaSqFt = length * width;
    var volumeCuFt = areaSqFt * (THICKNESS_IN / 12);
    var volumeCuYd = (volumeCuFt / 27) * (1 + waste / 100);

    var lowCost = Math.max(FLOOR_LOW, areaSqFt * LOW_PER_SQFT);
    var highCost = Math.max(FLOOR_HIGH, areaSqFt * HIGH_PER_SQFT);

    document.getElementById("rvArea").textContent = fmt(areaSqFt) + " sq ft";
    document.getElementById("rvVolume").textContent = fmt(volumeCuYd) + " cu yd";
    document.getElementById("rvCost").textContent = money(lowCost) + " \\u2013 " + money(highCost);
    result.hidden = false;
  }
})();
'''

def _rv_boat_pad_page():
    t = TOOLS["rv-boat-pad-calculator"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Pick a typical size or enter your RV's, trailer's, or boat-and-trailer's exact footprint to estimate square footage, concrete volume at the 6-inch thickness RV/boat pads are commonly built to, and a planning-level cost range.</p>
</div>

<div class="wrap" style="padding-bottom:50px">
  <div class="calc">
    <form id="rvCalc">
      <div class="calc-grid">
        <div class="field" style="grid-column:1/-1">
          <label for="preset">Size preset</label>
          <select id="preset" name="preset">
            <option value="custom" selected>Custom (enter dimensions below)</option>
            <option value="class-b">Class B camper van / small trailer (~20 &times; 10 ft)</option>
            <option value="travel-trailer">Travel trailer (~28 &times; 12 ft)</option>
            <option value="class-c">Class C motorhome (~30 &times; 12 ft)</option>
            <option value="class-a">Class A motorhome (~40 &times; 14 ft)</option>
            <option value="boat-trailer">Boat + trailer (~26 &times; 10 ft)</option>
          </select>
          <span class="hint">Presets are typical planning dimensions, not exact to any one model &mdash; measure your actual RV or boat-and-trailer length and beam/width for an accurate number.</span>
        </div>
        <div class="field">
          <label for="length">Pad length (ft)</label>
          <input type="number" id="length" name="length" min="1" step="1" placeholder="e.g. 30" required>
          <span class="hint">Add a few feet beyond the vehicle's length for room to walk around it and open doors/hatches.</span>
        </div>
        <div class="field">
          <label for="width">Pad width (ft)</label>
          <input type="number" id="width" name="width" min="1" step="1" placeholder="e.g. 12" required>
          <span class="hint">Vehicle width/beam plus clearance on both sides.</span>
        </div>
        <div class="field" style="grid-column:1/-1">
          <label for="waste">Waste / overage factor</label>
          <select id="waste" name="waste">
            <option value="5">5% &mdash; simple rectangle, easy access</option>
            <option value="10" selected>10% &mdash; typical (recommended default)</option>
            <option value="15">15% &mdash; irregular shape or difficult access</option>
          </select>
        </div>
      </div>
    </form>
    <p class="chip" style="margin-top:16px">Fixed spec for this tool: 6 in thickness &middot; 4,000+ PSI &middot; rebar reinforced</p>
    <div class="calc-result" id="rvResult" hidden>
      <div class="grid grid-3">
        <div><span class="lbl">Surface area</span><div class="num" id="rvArea" style="font-size:1.3rem">-</div></div>
        <div><span class="lbl">Concrete needed</span><div class="num" id="rvVolume">-</div></div>
        <div><span class="lbl">Estimated cost range</span><div class="num" id="rvCost" style="font-size:1.3rem">-</div></div>
      </div>
      <p class="calc-disclaimer">This is a planning estimate, not a quote. It fixes thickness at 6 inches (the consensus spec for a parked, stationary RV or boat load) and scales a published national RV/boat pad cost range against your square footage. It does not include base excavation/compaction, site access work, permit fees, or curing time before you can park on it.</p>
    </div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Methodology</span>
    <h2>Where these numbers come from</h2>
    <p>Thickness and reinforcement are fixed at 6 inches with 4,000+ PSI concrete and rebar &mdash; the consensus spec repeated across RV-pad-focused contractor guides and RV-owner forum discussions of pad requirements. That's thicker than a standard driveway because a parked RV or boat trailer puts a heavy, concentrated, <em>stationary</em> load on one spot rather than the rolling load a driveway sees, so it needs a different spec than the code-minimum 4-inch driveway slab on our <a href="/concrete-driveways/">Concrete Driveways</a> page.</p>
    <p>The cost range is scaled from a published national concrete RV pad cost range of roughly $1,800&ndash;$7,200. We convert that into a per-square-foot band (about $8&ndash;$16/sq ft) and apply it to your exact square footage, with a floor near the low end of the published range so a very small pad estimate doesn't fall unrealistically low. Volume is standard concrete math: length &times; width &times; (thickness in feet), converted to cubic yards, plus your chosen waste/overage percentage.</p>
    <p><strong>Limitations:</strong> the published $1,800&ndash;$7,200 range reflects typically sized pads &mdash; a very large custom pad (say, for a large Class A coach plus a tow vehicle) can reasonably estimate above that ceiling, and a tiny pad can estimate near the floor rather than strictly below it. This tool doesn't know your base soil condition, site access, distance from the road, permit costs, or whether you need site clearing/grading first &mdash; all of which change the real price. It is a planning range based on publicly reported cost data, not a quote from us or any specific provider.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">Before You Pour</span>
    <h2>Curing time and site access still apply</h2>
    <div class="grid grid-2">
      <div class="card">
        <h3>Don't park on it early</h3>
        <p>A stationary, heavy load like a parked RV or boat trailer needs closer to the full 28-day cure, not the 7 days that's enough for a passenger car on a driveway. Park too soon and you risk denting or cracking a slab that hasn't reached full strength.</p>
      </div>
      <div class="card">
        <h3>Confirm the truck can reach the pad site</h3>
        <p>RV and boat pads often sit further back on a rural lot than a driveway does. Run through our <a href="/tools/site-access-checklist/">site-access checklist</a> before assuming a standard mixer truck can get there and turn around.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Ready to plan an RV or boat pad?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="{SERVICES['rv-and-boat-pads']['route']}">See RV &amp; Boat Pad specs</a>
      <a class="btn btn-outline btn-lg" href="/permits/">Check permit requirements</a>
    </div>
  </div>
</section>

<script>{RV_CALC_JS}</script>
'''.strip()

    return {
        "route": t["route"],
        "title": t["name"],
        "meta_description": "Pick a size preset or enter custom dimensions to estimate square footage, concrete volume, and a planning-level cost range for an RV or boat pad in South Lake County, FL.",
        "h1": t["name"],
        "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), (t["name"], None)],
        "nav_active": "/tools/",
        "body_html": body_html,
    }


# ---------------------------------------------------------------------------
# 2) Workshop Slab Thickness Guide
# ---------------------------------------------------------------------------

WORKSHOP_CALC_JS = '''
(function () {
  var form = document.getElementById("workshopCalc");
  if (!form) return;
  var result = document.getElementById("workshopResult");
  var LOW_PER_SQFT = 6;
  var HIGH_PER_SQFT = 12;

  function fmt(n) { return n.toLocaleString("en-US", { maximumFractionDigits: 1 }); }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }

  form.addEventListener("input", calc);
  form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });

  function calc() {
    var length = parseFloat(form.length.value) || 0;
    var width = parseFloat(form.width.value) || 0;
    if (length <= 0 || width <= 0) {
      result.hidden = true;
      return;
    }
    var areaSqFt = length * width;
    var perimeterFt = 2 * (length + width);
    var lowCost = areaSqFt * LOW_PER_SQFT;
    var highCost = areaSqFt * HIGH_PER_SQFT;

    document.getElementById("wsArea").textContent = fmt(areaSqFt) + " sq ft";
    document.getElementById("wsPerimeter").textContent = fmt(perimeterFt) + " ft";
    document.getElementById("wsCost").textContent = money(lowCost) + " \\u2013 " + money(highCost);
    result.hidden = false;
  }
})();
'''

def _workshop_slab_guide_page():
    t = TOOLS["workshop-slab-guide"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">A workshop, metal building, or barn slab isn't priced or built like a driveway. The edges usually need to be thicker, and depending on what's going inside, a vapor barrier can matter a lot more than it does under a driveway or patio. This is a decision guide, not a quote.</p>
</div>

<section class="tight">
  <div class="wrap">
    <span class="eyebrow">Spec Table</span>
    <h2>Thickened-edge slab specs for a metal building or pole barn</h2>
    <p>Most metal-building and pole-barn foundations use a "thickened edge" (or "monolithic slab") design: the perimeter of the slab is poured noticeably deeper than the interior field to carry the wall/column loads without a separate footer.</p>
    <div class="overflow-x">
    <table>
      <thead><tr><th>Element</th><th>Typical spec</th><th>Why</th></tr></thead>
      <tbody>
        <tr><td>Perimeter (thickened edge) width</td><td>12&ndash;16 in</td><td>Carries the point/line loads from wall girts and columns bearing on the edge of the slab.</td></tr>
        <tr><td>Perimeter (thickened edge) depth</td><td>8&ndash;12 in</td><td>Depth (not just width) is what actually resists the building's bearing and any frost/soil movement at the edge.</td></tr>
        <tr><td>Interior field thickness</td><td>4&ndash;6 in</td><td>Similar range to a driveway or patio slab; 6 in is common where a vehicle lift, heavy equipment, or a tractor will sit.</td></tr>
        <tr><td>Vapor barrier</td><td>Often ~10&ndash;25% add to slab cost</td><td>Polyethylene sheeting under the slab to slow moisture migrating up from the soil.</td></tr>
      </tbody>
    </table>
    </div>
    <p class="calc-disclaimer">These are the specs published by metal-building foundation contractor guides for a typical residential/hobby-scale workshop or pole barn, not a Florida Building Code citation specific to accessory-building slabs. Your local building department has the final say on what's required for a permit &mdash; see our <a href="/permits/">Permit Directory</a>.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Decision Guide</span>
    <h2>Do you need a vapor barrier?</h2>
    <p>A vapor barrier is a sheet of polyethylene laid under the slab before the pour to slow ground moisture from wicking up through the concrete. It's not universally required, but it's worth the modest added cost (commonly cited as roughly 10&ndash;25% more for the slab) in a few common workshop scenarios:</p>
    <div class="grid grid-2">
      <div class="card">
        <h3>Where it usually matters</h3>
        <p>You'll finish the floor (epoxy, tile, glued-down flooring), store moisture-sensitive tools/materials, run a woodworking shop where humidity affects wood, or the building sits on a low or poorly drained part of the lot.</p>
      </div>
      <div class="card">
        <h3>Where it matters less</h3>
        <p>A bare, well-ventilated barn or equipment storage building on higher, well-drained ground, with no finished floor covering planned, gets less practical benefit from the added cost.</p>
      </div>
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <span class="eyebrow">Sizing</span>
    <h2>Roughly size your slab, then estimate cost</h2>
    <p>Enter your planned building footprint to see the slab area, approximate thickened-edge perimeter length, and a planning-level cost range at the published national rate of $6&ndash;$12 per square foot for a workshop/metal-building slab.</p>
  </div>
</section>

<div class="wrap" style="padding-bottom:50px">
  <div class="calc">
    <form id="workshopCalc">
      <div class="calc-grid">
        <div class="field">
          <label for="length">Building length (ft)</label>
          <input type="number" id="length" name="length" min="1" step="1" placeholder="e.g. 30" required>
        </div>
        <div class="field">
          <label for="width">Building width (ft)</label>
          <input type="number" id="width" name="width" min="1" step="1" placeholder="e.g. 40" required>
        </div>
      </div>
    </form>
    <div class="calc-result" id="workshopResult" hidden>
      <div class="grid grid-3">
        <div><span class="lbl">Slab area</span><div class="num" id="wsArea" style="font-size:1.3rem">-</div></div>
        <div><span class="lbl">Approx. thickened-edge perimeter</span><div class="num" id="wsPerimeter" style="font-size:1.3rem">-</div></div>
        <div><span class="lbl">Estimated cost range</span><div class="num" id="wsCost" style="font-size:1.3rem">-</div></div>
      </div>
      <p class="calc-disclaimer">This is a planning estimate, not a quote. It multiplies your footprint by a published national workshop/metal-building slab cost range ($6&ndash;$12/sq ft) that already reflects a typical thickened edge; it does not separately price a vapor barrier, site grading, base preparation, permits, or a slab built for unusually heavy equipment. <strong>Limitations:</strong> the per-square-foot range is national, not South Lake County-specific, and does not account for your building's exact edge design, soil, or access &mdash; use it to compare footprint sizes, not as a final number.</p>
    </div>
  </div>
</div>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Planning a workshop, garage, or barn slab?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="{SERVICES['workshop-slabs']['route']}">See Workshop Slab specs</a>
      <a class="btn btn-outline btn-lg" href="/tools/drainage-slope-planner/">Plan drainage first</a>
    </div>
  </div>
</section>

<script>{WORKSHOP_CALC_JS}</script>
'''.strip()

    return {
        "route": t["route"],
        "title": t["name"],
        "meta_description": "Thickened-edge slab specs for a metal building or barn, when a vapor barrier matters, and a footprint-based cost estimator for a workshop slab in South Lake County, FL.",
        "h1": t["name"],
        "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), (t["name"], None)],
        "nav_active": "/tools/",
        "body_html": body_html,
    }


# ---------------------------------------------------------------------------
# 3) Concrete Truck Site-Access Checklist
# ---------------------------------------------------------------------------

def _check_item(text):
    return f'<li><label style="display:flex;gap:12px;align-items:flex-start;cursor:pointer;font-weight:normal"><input type="checkbox" style="margin-top:5px;width:16px;height:16px;flex:none"><span>{text}</span></label></li>'

def _site_access_checklist_page():
    t = TOOLS["site-access-checklist"]
    clearance_items = "\n".join(_check_item(x) for x in [
        "At least 10&ndash;12 ft of clear width along the <em>entire</em> path the mixer truck needs to travel, not just at the road.",
        "At least 14 ft of vertical clearance the whole way in &mdash; check under any gate arms, carports, or low structures, not just tree limbs.",
        "Room to turn the truck around at the pour site, or a straight, clear path to back all the way out.",
        "A driver has actually walked or driven the access route recently, not just looked at it from the road.",
    ])
    hazard_items = "\n".join(_check_item(x) for x in [
        "No low-hanging branches or limbs (especially live oaks) across the access path &mdash; a loaded mixer sits taller than most passenger vehicles.",
        "No overhead power or utility lines crossing low over the driveway or access path.",
        "No soft, sandy, or wet ground the truck would have to cross &mdash; a loaded mixer truck weighs several tons and can sink or rut a soft path.",
        "No standing water or a recently rain-soaked section, especially after a Central Florida afternoon storm &mdash; ground that looks firm can turn soft fast.",
    ])
    fallback_items = "\n".join(_check_item(x) for x in [
        "Ask whether a <strong>pump truck</strong> is an option &mdash; the mixer stays on solid ground near the road and pumps concrete through a hose to the pour site.",
        "Ask about a <strong>power buggy</strong> &mdash; a small motorized cart that can carry concrete down a tight or soft path a full-size truck can't use.",
        "Ask about a <strong>smaller mini-mixer truck</strong> (roughly up to 3 cu yd per load, versus about 10 cu yd for a standard truck) that can navigate tighter access, usually with more trips and some added cost.",
    ])

    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Long, rural, or tree-lined driveways don't always let a standard concrete mixer truck reach the pour site. Walk your access route against this checklist before you assume a truck can get in and out &mdash; it's a common surprise on South Lake County's larger lots, and one none of the local competitors we reviewed address directly.</p>
</div>

<section class="tight">
  <div class="wrap">
    <span class="eyebrow">Step 1</span>
    <h2>Clearance &amp; maneuvering room</h2>
    <ul class="list-check" style="list-style:none;padding:0;display:flex;flex-direction:column;gap:14px">
      {clearance_items}
    </ul>
  </div>
</section>

<section class="alt tight">
  <div class="wrap">
    <span class="eyebrow">Step 2</span>
    <h2>Overhead &amp; ground hazards</h2>
    <ul class="list-check" style="list-style:none;padding:0;display:flex;flex-direction:column;gap:14px">
      {hazard_items}
    </ul>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <span class="eyebrow">Step 3</span>
    <h2>If access fails &mdash; solutions to ask about</h2>
    <p>Checking a box above isn't a pass/fail grade on your property &mdash; a difficult access route just means the job needs a different method, usually at some added cost.</p>
    <ul class="list-check" style="list-style:none;padding:0;display:flex;flex-direction:column;gap:14px">
      {fallback_items}
    </ul>
  </div>
</section>

<div class="wrap">
  <div class="disclosure-box">
    This checklist reflects general clearance guidance discussed in concrete-industry and DIY forums about mixer-truck access on rural driveways &mdash; it is not a site inspection and not a guarantee that any specific truck fits your property. Measure your own access route at the actual width and height needed before assuming a standard mixer truck can reach your pour location. {BUSINESS["disclosure_short"]}
  </div>
</div>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Not sure if your access will work?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Describe your site &amp; ask</a>
      <a class="btn btn-outline btn-lg" href="/tools/driveway-cost-calculator/">Estimate driveway cost &amp; volume</a>
      <a class="btn btn-outline btn-lg" href="{GUIDES['concrete-truck-access-rural-driveway']['route']}">Read the full access guide</a>
    </div>
  </div>
</section>
'''.strip()

    return {
        "route": t["route"],
        "title": t["name"],
        "meta_description": "Check clearance width, vertical height, turnaround room, and ground conditions before assuming a concrete mixer truck can reach your rural South Lake County lot.",
        "h1": t["name"],
        "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), (t["name"], None)],
        "nav_active": "/tools/",
        "body_html": body_html,
    }


# ---------------------------------------------------------------------------
# 4) Drainage & Slope Planner
# ---------------------------------------------------------------------------

SLOPE_CALC_JS = '''
(function () {
  var form = document.getElementById("slopeCalc");
  if (!form) return;
  var result = document.getElementById("slopeResult");
  var MIN_IN_PER_FT = 0.125;

  form.addEventListener("input", calc);
  form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });

  function calc() {
    var rise = parseFloat(form.rise.value);
    var run = parseFloat(form.run.value);
    if (!(run > 0) || isNaN(rise)) {
      result.hidden = true;
      return;
    }
    var inPerFt = rise / run;
    var percent = (rise / (run * 12)) * 100;
    var meets = inPerFt >= MIN_IN_PER_FT;

    document.getElementById("slopeInPerFt").textContent = inPerFt.toFixed(3) + " in/ft";
    document.getElementById("slopePercent").textContent = percent.toFixed(2) + "%";
    var statusEl = document.getElementById("slopeStatus");
    if (meets) {
      statusEl.textContent = "Meets the 1/8 in/ft minimum \\u2014 should drain toward the intended path.";
      statusEl.style.color = "var(--ok)";
    } else {
      statusEl.textContent = "Below the 1/8 in/ft minimum \\u2014 water is likely to pool instead of draining.";
      statusEl.style.color = "var(--warn)";
    }
    result.hidden = false;
  }
})();
'''

def _drainage_slope_planner_page():
    t = TOOLS["drainage-slope-planner"]
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Standing water on a slab almost always traces back to slope. Enter the rise and run over a section of driveway, patio, or pad to check it against the long-standing 1/8-inch-per-foot minimum drainage slope &mdash; the same reference we cite on our <a href="/concrete-driveways/">Concrete Driveways</a> page.</p>
</div>

<div class="wrap" style="padding-bottom:50px">
  <div class="calc">
    <form id="slopeCalc">
      <div class="calc-grid">
        <div class="field">
          <label for="rise">Rise / drop (inches)</label>
          <input type="number" id="rise" name="rise" step="0.1" placeholder="e.g. 1.5" required>
          <span class="hint">Height difference between the high end and low end of the section you're checking.</span>
        </div>
        <div class="field">
          <label for="run">Run / distance (feet)</label>
          <input type="number" id="run" name="run" min="0.1" step="0.5" placeholder="e.g. 12" required>
          <span class="hint">Horizontal distance over which that rise happens.</span>
        </div>
      </div>
    </form>
    <div class="calc-result" id="slopeResult" hidden>
      <div class="grid grid-3">
        <div><span class="lbl">Slope</span><div class="num" id="slopeInPerFt" style="font-size:1.3rem">-</div></div>
        <div><span class="lbl">As a percent grade</span><div class="num" id="slopePercent" style="font-size:1.3rem">-</div></div>
        <div><span class="lbl">Status</span><div class="num" id="slopeStatus" style="font-size:1.1rem">-</div></div>
      </div>
      <p class="calc-disclaimer">This checks your entered rise/run against the published 1/8 in per foot (about 1%) minimum drainage slope for concrete flatwork. <strong>Limitations:</strong> it does not know where the water is supposed to go, whether the surrounding grade actually carries it away, or whether a much steeper slope (beyond what's needed to drain) creates its own erosion or runoff problem on your lot &mdash; use it as a first check, not a final grading plan.</p>
    </div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Methodology</span>
    <h2>Where the 1/8 in/ft number comes from</h2>
    <p>A minimum slope of about 1/8 inch of fall per foot (roughly 1%) is the long-standing reference from concrete industry mix-design and construction guidance (cement.org). Below that, water tends to sit on the slab instead of running off &mdash; a common complaint on the flatter lots found throughout South Lake County.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <span class="eyebrow">If Slope Alone Isn't Enough</span>
    <h2>Common drainage fixes</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Channel drains</h3>
        <p>A narrow trench drain with a metal or plastic grate, set into the low point of a slab or at a garage/entry threshold, to catch and carry away sheet flow before it pools.</p>
      </div>
      <div class="card">
        <h3>Catch basins</h3>
        <p>A boxed drain set at a specific low point, connected to buried pipe that carries water away from the slab and house to a safe discharge point on the lot.</p>
      </div>
      <div class="card">
        <h3>French drains</h3>
        <p>A gravel-filled trench with a perforated pipe that collects and redirects groundwater or runoff moving through the soil next to a slab, rather than water sitting on top of it.</p>
      </div>
    </div>
    <p class="calc-disclaimer">These are the drainage solutions most commonly discussed for flooding or pooling driveways and slabs. If the underlying problem is the overall grade of the lot rather than the slab itself, a <a href="{SERVICES['retaining-walls']['route']}">retaining wall</a> sized to manage slope and runoff may solve more than a drain alone.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap" style="text-align:center">
    <h2>Dealing with a slab that already floods?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/tools/site-access-checklist/">Check truck access first</a>
    </div>
  </div>
</section>

<script>{SLOPE_CALC_JS}</script>
'''.strip()

    return {
        "route": t["route"],
        "title": t["name"],
        "meta_description": "Check rise-over-run slope against the 1/8-inch-per-foot minimum drainage standard, plus common fixes for a driveway, patio, or pad that pools water.",
        "h1": t["name"],
        "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), (t["name"], None)],
        "nav_active": "/tools/",
        "body_html": body_html,
    }


# ---------------------------------------------------------------------------
# 5) /permits/ — South Lake Permit Directory
# ---------------------------------------------------------------------------

def _jurisdiction_card(name, county, links_html, address, note=None):
    note_html = f'<p class="calc-disclaimer" style="margin-top:10px">{note}</p>' if note else ""
    return f'''
    <div class="card">
      <h3>{name}</h3>
      <p class="chip" style="margin-bottom:10px">{county}</p>
      <p>{links_html}</p>
      {f"<p style='margin-top:8px'>{address}</p>" if address else ""}
      {note_html}
    </div>'''

def _permits_page():
    t = TOOLS["permits"]

    groveland = _jurisdiction_card(
        f"{CITIES['groveland']['name']}",
        "Lake County",
        'City of Groveland Building Division: <a href="https://groveland-fl.gov/130/Building-Division">groveland-fl.gov/130/Building-Division</a> &middot; online portal (eTRAKiT): <a href="https://gvld-trk.aspgov.com/etrakit/">gvld-trk.aspgov.com/etrakit</a>',
        "6825 SR 50, Groveland, FL 34736",
    )
    mascotte = _jurisdiction_card(
        f"{CITIES['mascotte']['name']}",
        "Lake County",
        'City of Mascotte Building Department: <a href="https://www.cityofmascotte.com/169/Building-Dept---Permits-Inspections">cityofmascotte.com/169/Building-Dept-Permits-Inspections</a> &middot; online portal: <a href="https://mascottefl.portal.iworq.net">mascottefl.portal.iworq.net</a> &middot; <a href="mailto:Building@CityOfMascotte.com">Building@CityOfMascotte.com</a> &middot; 352-557-8888',
        None,
    )
    minneola = _jurisdiction_card(
        f"{CITIES['minneola']['name']}",
        "Lake County",
        'City of Minneola Building Department (administered by SafeBuilt): <a href="https://www.minneola.us/building-department">minneola.us/building-department</a> &middot; <a href="mailto:buildingservices@minneola.us">buildingservices@minneola.us</a> &middot; (352) 394-3598',
        "800 N. US Highway 27, Minneola, FL 34715",
    )
    howey = _jurisdiction_card(
        f"{CITIES['howey-in-the-hills']['name']}",
        "Lake County",
        'Town of Howey-in-the-Hills Building Services (administered by Alpha/Willdan Engineering): <a href="https://www.howey.org/236/Building-Services">howey.org/236/Building-Services</a> &middot; online Citizen Portal linked from that page &middot; 407-745-3633',
        "101 N. Palm Avenue, Howey-in-the-Hills, FL 34737",
    )
    lake_county = _jurisdiction_card(
        f"{CITIES['rural-lake-county']['name']}",
        "Lake County (unincorporated)",
        'Lake County Building Services: <a href="https://www.lakecountyfl.gov/building-services">lakecountyfl.gov/building-services</a> &middot; Planning &amp; Zoning: <a href="https://www.lakecountyfl.gov/Planning-and-Zoning">lakecountyfl.gov/Planning-and-Zoning</a>',
        "P.O. Box 7800, Tavares, FL 32778",
        note="<strong>Not confirmed in our research:</strong> we found Lake County's general Building Services department, but not a page describing the exact driveway/slab permit process (fees, when a separate encroachment permit applies, etc.) the way Sumter County publishes below. Call Lake County Building Services directly to verify the process before you pour on unincorporated land.",
    )
    sumter = _jurisdiction_card(
        "Center Hill area",
        "Sumter County",
        'Sumter County Building Services: <a href="https://www.sumtercountyfl.gov/77/Building-Services">sumtercountyfl.gov/77/Building-Services</a> &middot; dedicated driveway-permitting page: <a href="https://www.sumtercountyfl.gov/926/Driveway-Permitting">sumtercountyfl.gov/926/Driveway-Permitting</a> &middot; online permitting: <a href="https://sumtercountyfl.gov/139/Online-Permitting">sumtercountyfl.gov/139/Online-Permitting</a>',
        "7375 Powell Rd, Wildwood, FL",
        note="Center Hill is a small city inside Sumter County (not Lake County). Center Hill City Hall is at 94 Virginia Avenue, Center Hill, FL 33514 (352-793-4431) and may issue certain local land-use items, but <strong>our research did not confirm</strong> whether full building/driveway permits for Center Hill addresses are issued by the city or route through Sumter County above &mdash; call either office to confirm which applies to your address before you pour.",
    )

    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Real links to the building/permit department for each jurisdiction in our South Lake County service area, so you know which office your project goes through before we pour.</p>
  <div class="disclosure-box">
    We link directly to each city or county's own building/permitting page below. We did not find a page for every jurisdiction that spells out the exact driveway-permit process (fees, inspections, what triggers a separate encroachment permit) &mdash; where that's the case, it's noted plainly rather than guessed at. Always confirm current requirements and fees directly with the department before you pour.
  </div>
</div>

<section class="tight">
  <div class="wrap">
    <span class="eyebrow">General Rule Of Thumb</span>
    <h2>Do you need a permit at all?</h2>
    <p>In most Florida jurisdictions, yes &mdash; pouring a new driveway or slab typically requires a building permit. A separate <strong>driveway/encroachment permit</strong> is commonly required specifically when you're cutting a new curb or connecting a driveway to a public road, in addition to (or instead of) a building permit for the slab itself. A thin resurfacing overlay (roughly 1 inch) over an existing driveway is often exempt where a full new pour is not. Skipping a required permit can mean a stop-work order or a fine commonly cited in the $500&ndash;$2,500 range in Florida jurisdictions. None of this replaces confirming the exact rule for your specific address and project with the department below.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Directory</span>
    <h2>Jurisdictions in our South Lake County service area</h2>
    <div class="grid grid-2">
      {groveland}
      {mascotte}
      {minneola}
      {howey}
      {lake_county}
      {sumter}
    </div>
  </div>
</section>

<section class="tight">
  <div class="wrap">
    <span class="eyebrow">Plan Before You Call</span>
    <h2>Related planning tools</h2>
    <div class="grid grid-3">
      <div class="card">
        <h3>Driveway Cost &amp; Volume Calculator</h3>
        <p>Estimate cubic yards and cost range before you talk permit fees.</p>
        <a class="card-link" href="{TOOLS['driveway-cost-calculator']['route']}">Open calculator &rarr;</a>
      </div>
      <div class="card">
        <h3>RV &amp; Boat Pad Calculator</h3>
        <p>Size a pad and see the 6-inch spec permit reviewers expect.</p>
        <a class="card-link" href="{TOOLS['rv-boat-pad-calculator']['route']}">Open calculator &rarr;</a>
      </div>
      <div class="card">
        <h3>Site-Access Checklist</h3>
        <p>Confirm a mixer truck can reach the pour site before you schedule anything.</p>
        <a class="card-link" href="{TOOLS['site-access-checklist']['route']}">Open checklist &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Not sure which permit applies to your project?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Ask us before you pour</a>
      <a class="btn btn-outline btn-lg" href="/services/">Browse services</a>
    </div>
  </div>
</section>
'''.strip()

    return {
        "route": t["route"],
        "title": t["name"],
        "meta_description": "Real links to the building and permit department for Groveland, Mascotte, Minneola, Howey-in-the-Hills, unincorporated Lake County, and the Center Hill/Sumter County area.",
        "h1": t["name"],
        "breadcrumbs": [("Home", "/"), ("Permits", None)],
        "nav_active": "/permits/",
        "body_html": body_html,
    }


def get_pages():
    return [
        _rv_boat_pad_page(),
        _workshop_slab_guide_page(),
        _site_access_checklist_page(),
        _drainage_slope_planner_page(),
        _permits_page(),
    ]
