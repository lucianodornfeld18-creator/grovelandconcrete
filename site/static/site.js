(function () {
  "use strict";

  // Mobile nav toggle
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("primaryNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Lead forms: progressive enhancement over a plain HTML POST to Web3Forms.
  // Without fetch the form submits normally and Web3Forms follows the hidden
  // `redirect` field to /thank-you/, so the no-JS path lands in the same place.
  var CAMPAIGN_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid"];

  document.querySelectorAll("form.lead-form").forEach(function (form) {
    if (!window.fetch) return;
    form.addEventListener("submit", function (evt) {
      evt.preventDefault();
      var msgBox = form.querySelector(".form-msg");
      var submitBtn = form.querySelector('button[type="submit"]');
      if (msgBox) {
        msgBox.textContent = "";
        msgBox.className = "form-msg";
      }
      if (submitBtn) submitBtn.disabled = true;

      var data = new FormData(form);
      // Carry campaign tags only when the visitor actually arrived with them,
      // so the emailed lead has no row of empty utm_* fields.
      try {
        var params = new URLSearchParams(window.location.search);
        CAMPAIGN_KEYS.forEach(function (k) {
          var v = params.get(k);
          if (v) data.append(k, v);
        });
      } catch (e) {}

      // Web3Forms answers a multipart POST with an HTML success page and a JSON
      // POST with {success, message}. Send JSON so a failure can be reported to
      // the visitor instead of guessed at. `redirect` only matters to the no-JS
      // path, so it is dropped here rather than emailed as a stray field.
      var payload = {};
      data.forEach(function (value, key) {
        if (key !== "redirect") payload[key] = value;
      });

      fetch(form.action, {
        method: "POST",
        body: JSON.stringify(payload),
        headers: { "Content-Type": "application/json", Accept: "application/json" },
      })
        .then(function (res) {
          return res
            .json()
            .catch(function () {
              return {};
            })
            .then(function (json) {
              if (res.ok && json.success !== false) {
                window.location.href = "/thank-you/";
                return;
              }
              throw new Error(json.message || "We could not send your request.");
            });
        })
        .catch(function (err) {
          if (msgBox) {
            msgBox.textContent = err.message || "We could not send your request. Please call instead.";
            msgBox.className = "form-msg error";
          }
        })
        .finally(function () {
          if (submitBtn) submitBtn.disabled = false;
        });
    });
  });
})();
