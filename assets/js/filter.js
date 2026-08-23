/* Work index filter. Progressive enhancement: the control is hidden until this
   runs, so with JavaScript off every row simply stays visible. */
(function () {
  "use strict";
  var bar = document.querySelector("[data-filter]");
  var index = document.querySelector("[data-index]");
  var empty = document.querySelector("[data-empty]");
  if (!bar || !index) return;

  bar.hidden = false;
  var rows = Array.prototype.slice.call(index.querySelectorAll(".index__row"));

  bar.addEventListener("click", function (e) {
    var btn = e.target.closest(".filter__btn");
    if (!btn) return;
    var kind = btn.getAttribute("data-kind");

    bar.querySelectorAll(".filter__btn").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b === btn));
    });

    var shown = 0;
    rows.forEach(function (r) {
      var match = kind === "all" || r.getAttribute("data-kind") === kind;
      r.hidden = !match;
      if (match) shown++;
    });
    if (empty) empty.hidden = shown > 0;
  });
})();
