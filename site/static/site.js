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

  // Lead form: progressive enhancement over a plain HTML form POST.
  // If fetch fails or is unsupported, the form still submits normally to /api/contact.
  var form = document.querySelector("form.lead-form");
  if (form && window.fetch) {
    form.addEventListener("submit", function (evt) {
      evt.preventDefault();
      var msgBox = form.querySelector(".form-msg");
      var submitBtn = form.querySelector('button[type="submit"]');
      if (msgBox) {
        msgBox.textContent = "";
        msgBox.className = "form-msg";
      }
      if (submitBtn) submitBtn.disabled = true;

      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      })
        .then(function (res) {
          if (res.redirected || res.ok) {
            window.location.href = "/thank-you/";
            return;
          }
          return res.text().then(function (text) {
            throw new Error(text || "We could not send your request.");
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
  }
})();
