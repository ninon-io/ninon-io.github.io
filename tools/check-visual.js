/*
 * Repeatable in-browser checks, run against a locally served build.
 * Injected into each page via Chrome headless; prints JSON to stdout.
 *
 * Checks: horizontal overflow, focusable-element visible focus ring,
 * heading order, images missing alt, and computed contrast for the main
 * text/background pairing.
 */
(function () {
  function lum(rgb) {
    var m = rgb.match(/\d+(\.\d+)?/g);
    if (!m) return null;
    var c = m.slice(0, 3).map(function (v) {
      v = v / 255;
      return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function ratio(a, b) {
    var la = lum(a), lb = lum(b);
    if (la === null || lb === null) return null;
    return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
  }

  var out = { url: location.pathname, problems: [] };

  // ---- horizontal overflow -------------------------------------------------
  var de = document.documentElement;
  out.scrollW = de.scrollWidth;
  out.clientW = de.clientWidth;
  if (de.scrollWidth > de.clientWidth + 1) {
    var wide = [];
    document.querySelectorAll("body *").forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.right > de.clientWidth + 1 && r.width > 0) {
        wide.push(el.tagName.toLowerCase() + "." + (el.className || "").toString().split(" ")[0] +
                  " right=" + Math.round(r.right));
      }
    });
    out.problems.push("horizontal overflow: " + de.scrollWidth + " > " + de.clientWidth +
                      " | " + wide.slice(0, 5).join(", "));
  }

  // ---- images without alt --------------------------------------------------
  var noAlt = [];
  document.querySelectorAll("img").forEach(function (i) {
    if (!i.hasAttribute("alt")) noAlt.push(i.getAttribute("src"));
  });
  if (noAlt.length) out.problems.push("img missing alt: " + noAlt.join(", "));

  // ---- heading order -------------------------------------------------------
  var last = 0, bad = [];
  document.querySelectorAll("h1,h2,h3,h4,h5,h6").forEach(function (h) {
    var lvl = +h.tagName[1];
    if (last && lvl > last + 1) bad.push(h.tagName + " after H" + last + ": " + h.textContent.trim().slice(0, 30));
    last = lvl;
  });
  if (bad.length) out.problems.push("heading order: " + bad.join(" | "));

  // ---- focus visibility ----------------------------------------------------
  var focusables = document.querySelectorAll("a[href], button, [tabindex]:not([tabindex='-1'])");
  out.focusables = focusables.length;
  var noRing = 0;
  focusables.forEach(function (el) {
    el.focus();
    var cs = getComputedStyle(el);
    var hasOutline = cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) > 0;
    var hasBorder = parseFloat(cs.borderBottomWidth) > 0;
    if (!hasOutline && !hasBorder) noRing++;
  });
  if (noRing) out.problems.push(noRing + " focusable element(s) with no visible focus indicator");

  // ---- contrast of the main text pairing ----------------------------------
  var body = document.body;
  var bg = getComputedStyle(body).backgroundColor;
  var fg = getComputedStyle(body).color;
  var r = ratio(fg, bg);
  out.bodyContrast = r ? Math.round(r * 100) / 100 : null;
  if (r && r < 4.5) out.problems.push("body contrast " + out.bodyContrast + ":1 below AA");

  return JSON.stringify(out);
})();
