/*
 * Rail Signal — prototype, homepage only.
 *
 * Turns the Selected rail into a readout: which entry you are level with, what
 * type it is, and a calibration mark showing the position. Nothing else moves.
 *
 * Activation rule
 *   A zero-height line sits at 42% of the viewport. A row becomes current when
 *   its top edge crosses that line, and stays current until the next row
 *   crosses. Because the rule is a single threshold per row rather than a
 *   nearest-neighbour search, it cannot oscillate when two rows are close
 *   together, and it needs no hysteresis.
 *
 * Cost while stationary
 *   Zero. An IntersectionObserver reports only on change, and the scroll-end
 *   resync runs once when motion stops. There is no per-frame scroll handler and
 *   no requestAnimationFrame loop, so a page left open does no work at all.
 *
 * Removing it
 *   Delete this file, the `has_signal` flag on _pages/home.md, the rail__signal
 *   block in _layouts/index.html and the styles in _sass/_components.scss.
 */
(function () {
  "use strict";

  var rail = document.querySelector("[data-signal]");
  var list = document.querySelector("[data-signal-index]");
  if (!rail || !list) return;

  var rows = Array.prototype.slice.call(list.querySelectorAll(".index__row"));
  if (rows.length < 2) return;

  var valEl = rail.querySelector("[data-signal-val]");
  var kindEl = rail.querySelector("[data-signal-kind]");
  var mark = rail.querySelector("[data-signal-mark]");

  var current = 0;   // index set by reading position
  var preview = -1;  // index set by hover or focus; -1 when none

  var HAIR = " "; // hair space, so "02 / 05" reads as one value not three

  function pad(n) { return n < 10 ? "0" + n : String(n); }

  function kindOf(row) {
    // Reuse the type already printed in the row rather than a second taxonomy.
    var tag = row.querySelector(".index__row__tag");
    return tag ? tag.textContent.trim() : "";
  }

  function render() {
    var i = preview > -1 ? preview : current;
    valEl.textContent = pad(i + 1) + HAIR + "/" + HAIR + pad(rows.length);
    kindEl.textContent = kindOf(rows[i]);
    // A ready-made percentage: CSS cannot divide by a variable.
    mark.style.setProperty("--signal-x", (i / rows.length) * 100 + "%");
    rail.setAttribute("data-preview", preview > -1 ? "true" : "false");
  }

  // ---- reading position ---------------------------------------------------
  // rootMargin collapses the viewport to a thin band at 42% of its height. At
  // most one row intersects it; in the gaps between rows nothing does, and the
  // last value simply persists, which is the behaviour we want.
  //
  // The band is a sliver, not a zero-height line: an intersection of exactly
  // zero area is not reported as intersecting, so a symmetric -42%/-58% pair
  // would observe nothing at all.
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var i = rows.indexOf(entry.target);
      if (i > -1 && i !== current) {
        current = i;
        if (preview === -1) render();
      }
    });
  }, { rootMargin: "-42% 0px -57.5% 0px", threshold: 0 });

  rows.forEach(function (r) { io.observe(r); });

  // The band is only a few pixels tall, so a fast momentum flick can carry a row
  // across it entirely between two frames — no state change, nothing reported,
  // and the readout is left showing a row you have already scrolled past. One
  // geometry read once the scroll stops resolves it: the current entry is the
  // last one whose top has crossed the line. This also covers the foot of the
  // page, where the line sits below every row and nothing intersects.
  function resync() {
    var y = window.innerHeight * 0.42;
    var best = 0;
    for (var i = 0; i < rows.length; i++) {
      if (rows[i].getBoundingClientRect().top <= y) best = i;
      else break;
    }
    if (best !== current) {
      current = best;
      if (preview === -1) render();
    }
  }

  // scrollend fires once, when motion stops. The debounced fallback costs a
  // clearTimeout per scroll event and nothing at all while the page is still.
  if ("onscrollend" in window) {
    window.addEventListener("scrollend", resync, { passive: true });
  } else {
    var idle;
    window.addEventListener("scroll", function () {
      clearTimeout(idle);
      idle = setTimeout(resync, 120);
    }, { passive: true });
  }
  window.addEventListener("resize", resync, { passive: true });

  // ---- hover and focus preview -------------------------------------------
  // Keyboard focus behaves exactly as hover does. The rail itself never becomes
  // interactive or focusable.
  function setPreview(i) {
    if (preview === i) return;
    preview = i;
    render();
  }

  rows.forEach(function (row, i) {
    row.addEventListener("mouseenter", function () { setPreview(i); });
    row.addEventListener("focus", function () { setPreview(i); });
  });

  list.addEventListener("mouseleave", function () { setPreview(-1); });
  list.addEventListener("focusout", function (e) {
    if (!list.contains(e.relatedTarget)) setPreview(-1);
  });

  // Touch: a tap is a navigation, not a preview. Clearing on touchstart stops a
  // stale preview sticking after the tap-emulated mouseenter.
  list.addEventListener("touchstart", function () { setPreview(-1); }, { passive: true });

  rail.setAttribute("data-signal-on", "");
  render();
})();
