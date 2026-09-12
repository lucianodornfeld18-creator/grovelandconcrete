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

      // Must stay a multipart FormData POST: it is a CORS "simple request", so
      // no preflight is sent. Web3Forms answers OPTIONS with 403 and no CORS
      // headers, so anything that triggers a preflight — a JSON body, a custom
      // header — fails in the browser with "Failed to fetch" even though the
      // same call works from curl. The multipart POST does come back with
      // access-control-allow-origin: *, so the response is readable.
      var data = new FormData();
      new FormData(form).forEach(function (value, key) {
        // `redirect` is only for the no-JS path. Sending it here would make
        // Web3Forms answer with a 302 that fetch has to follow back across
        // origins; we navigate ourselves instead.
        if (key !== "redirect") data.append(key, value);
      });

      // Carry campaign tags only when the visitor actually arrived with them,
      // so the emailed lead has no row of empty utm_* fields.
      try {
        var params = new URLSearchParams(window.location.search);
        CAMPAIGN_KEYS.forEach(function (k) {
          var v = params.get(k);
          if (v) data.append(k, v);
        });
      } catch (e) {}

      fetch(form.action, {
        method: "POST",
        body: data,
        headers: { Accept: "application/json" },
      })
        .then(function (res) {
          // A multipart submit is answered with Web3Forms' own HTML success
          // page, not JSON, so the status is what decides; parse a body only to
          // surface their message when there is one.
          return res.text().then(function (text) {
            var json = null;
            try {
              json = JSON.parse(text);
            } catch (e) {}
            if (res.ok && (!json || json.success !== false)) {
              window.location.href = "/thank-you/";
              return;
            }
            throw new Error((json && json.message) || "We could not send your request.");
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
