# -*- coding: utf-8 -*-

CALC_JS = '''
(function () {
  var form = document.getElementById("drivewayCalc");
  if (!form) return;
  var result = document.getElementById("calcResult");

  function fmt(n) { return n.toLocaleString("en-US", { maximumFractionDigits: 1 }); }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }

  form.addEventListener("input", calc);
  form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });

  function calc() {
    var length = parseFloat(form.length.value) || 0;
    var width = parseFloat(form.width.value) || 0;
    var thickness = parseFloat(form.thickness.value) || 4;
    var waste = parseFloat(form.waste.value) || 10;

    if (length <= 0 || width <= 0) {
      result.hidden = true;
      return;
    }

    var areaSqFt = length * width;
    var volumeCuFt = areaSqFt * (thickness / 12);
    var volumeCuYd = (volumeCuFt / 27) * (1 + waste / 100);

    // Published Florida cost range is $6-10/sq ft at a 4" standard thickness (broom finish).
    // We scale that range proportionally with thickness since more inches means more material and labor.
    var thicknessFactor = thickness / 4;
    var lowPerSqFt = 6 * thicknessFactor;
    var highPerSqFt = 10 * thicknessFactor;
    var lowCost = areaSqFt * lowPerSqFt;
    var highCost = areaSqFt * highPerSqFt;

    document.getElementById("resArea").textContent = fmt(areaSqFt) + " sq ft";
    document.getElementById("resVolume").textContent = fmt(volumeCuYd) + " cu yd";
    document.getElementById("resCost").textContent = money(lowCost) + " – " + money(highCost);
    result.hidden = false;
  }
})();
'''

def get_pages():
    body_html = f'''
<div class="wrap" style="padding-bottom:20px">
  <p class="lede">Estimate the concrete volume and a planning-level cost range for a driveway of any length — including long rural approaches that generic nationwide calculators aren't built for.</p>
</div>

<div class="wrap" style="padding-bottom:50px">
  <div class="calc">
    <form id="drivewayCalc">
      <div class="calc-grid">
        <div class="field">
          <label for="length">Driveway length (ft)</label>
          <input type="number" id="length" name="length" min="1" step="1" placeholder="e.g. 300" required>
          <span class="hint">Measure from the road/edge of pavement to where the driveway ends.</span>
        </div>
        <div class="field">
          <label for="width">Driveway width (ft)</label>
          <input type="number" id="width" name="width" min="1" step="0.5" value="12" required>
          <span class="hint">12 ft fits one vehicle comfortably; 16–18 ft is standard for two cars side by side.</span>
        </div>
        <div class="field">
          <label for="thickness">Slab thickness</label>
          <select id="thickness" name="thickness">
            <option value="4">4 in — code minimum, passenger vehicles</option>
            <option value="5">5 in — added durability</option>
            <option value="6">6 in — RV, trailer, or heavier loads</option>
          </select>
        </div>
        <div class="field">
          <label for="waste">Waste / overage factor</label>
          <select id="waste" name="waste">
            <option value="5">5% — simple rectangle, easy access</option>
            <option value="10" selected>10% — typical (recommended default)</option>
            <option value="15">15% — irregular shape or difficult access</option>
          </select>
        </div>
      </div>
    </form>
    <div class="calc-result" id="calcResult" hidden>
      <div class="grid grid-3">
        <div><span class="lbl">Surface area</span><div class="num" id="resArea" style="font-size:1.3rem">-</div></div>
        <div><span class="lbl">Concrete needed</span><div class="num" id="resVolume">-</div></div>
        <div><span class="lbl">Estimated cost range</span><div class="num" id="resCost" style="font-size:1.3rem">-</div></div>
      </div>
      <p class="calc-disclaimer">This is a planning estimate, not a quote. It scales the published Florida broom-finish range of $6–$10 per sq ft (at 4 in thickness) by your chosen thickness and adds your waste factor for concrete volume. It does not include demolition of an existing slab, site grading, extended truck access (pump truck, power buggy), curb cuts, permit fees, or decorative finishes.</p>
    </div>
  </div>
</div>

<section class="alt">
  <div class="wrap">
    <span class="eyebrow">Methodology</span>
    <h2>Where these numbers come from</h2>
    <p>The cost range is based on a published Florida driveway cost range of $6–$10 per square foot for a standard broom-finish pour at 4-inch thickness (see our <a href="/concrete-driveways/">Concrete Driveways</a> page for sourcing). We scale that per-square-foot range in proportion to slab thickness, since a 6-inch pour uses roughly 50% more material and labor than a 4-inch pour. Volume is a standard concrete math calculation: length × width × (thickness in feet), converted to cubic yards, plus a waste/overage percentage to account for spillage, subgrade irregularity, and minor over-excavation.</p>
    <p><strong>Limitations:</strong> this tool does not know your specific site conditions — slope, existing pavement to remove, distance the truck has to travel from the road, permit costs, or finish upgrades (stamped, colored, exposed aggregate) all change the real price. It also does not represent a specific provider's pricing; it is a planning range based on publicly reported Florida cost data, not a quote from us or anyone we work with.</p>
  </div>
</section>

<section>
  <div class="wrap" style="text-align:center">
    <h2>Want an estimate based on your actual site?</h2>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-primary btn-lg" href="/contact/">Request a free estimate</a>
      <a class="btn btn-outline btn-lg" href="/tools/site-access-checklist/">Check truck access first</a>
    </div>
  </div>
</section>

<script>{CALC_JS}</script>
'''.strip()

    return [{
        "route": "/tools/driveway-cost-calculator/",
        "title": "Driveway Cost & Volume Calculator",
        "meta_description": "Estimate cubic yards and a planning-level cost range for a standard or long concrete driveway in South Lake County, FL.",
        "h1": "Driveway Cost & Volume Calculator",
        "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), ("Driveway Cost & Volume Calculator", None)],
        "nav_active": "/tools/",
        "body_html": body_html,
    }]
