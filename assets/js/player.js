/*
 * Custom audio player.
 *
 * Waveforms are drawn from peak data precomputed at build time by
 * tools/generate-peaks.sh — no large file is ever decoded in the browser.
 * Only one source plays at a time. Fully keyboard operable.
 */
(function () {
  "use strict";

  var players = [];

  function fmt(sec) {
    if (!isFinite(sec) || sec < 0) sec = 0;
    var m = Math.floor(sec / 60);
    var s = Math.floor(sec % 60);
    return m + ":" + (s < 10 ? "0" : "") + s;
  }

  function cssVar(el, name) {
    return getComputedStyle(el).getPropertyValue(name).trim();
  }

  function Player(root) {
    this.root = root;
    this.audio = root.querySelector("audio");
    this.wave = root.querySelector(".player__wave");
    this.canvas = root.querySelector("canvas");
    this.toggle = root.querySelector(".player__toggle");
    this.time = root.querySelector(".player__time");
    this.peaks = null;

    if (!this.audio || !this.canvas || !this.toggle) return;

    this.ctx = this.canvas.getContext("2d");
    root.setAttribute("data-enhanced", "");
    this.bind();
    this.loadPeaks();
    this.paint();
  }

  Player.prototype.loadPeaks = function () {
    var src = this.root.getAttribute("data-peaks");
    var self = this;
    if (!src) return;
    fetch(src)
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (d && d.peaks) { self.peaks = d.peaks; self.paint(); }
      })
      .catch(function () { /* waveform is decoration; silence is fine */ });
  };

  Player.prototype.paint = function () {
    var c = this.canvas, ctx = this.ctx;
    var dpr = window.devicePixelRatio || 1;
    var w = c.clientWidth, h = c.clientHeight;
    if (!w || !h) return;

    c.width = Math.round(w * dpr);
    c.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);

    var idle = cssVar(this.root, "--faint") || "#726C62";
    var done = cssVar(this.root, "--gold") || "#C9A227";
    var mid = h / 2;
    var progress = this.audio.duration ? this.audio.currentTime / this.audio.duration : 0;

    if (!this.peaks) {
      // No peaks yet: a single hairline keeps the control legible and clickable.
      ctx.fillStyle = idle;
      ctx.fillRect(0, mid - 0.5, w, 1);
      ctx.fillStyle = done;
      ctx.fillRect(0, mid - 0.5, w * progress, 1);
      return;
    }

    var n = this.peaks.length;
    var barW = 2, gap = 1, step = barW + gap;
    var bars = Math.max(1, Math.floor(w / step));

    for (var i = 0; i < bars; i++) {
      var v = this.peaks[Math.floor((i / bars) * n)] || 0;
      var bh = Math.max(1, v * (h - 2));
      var x = i * step;
      ctx.fillStyle = x / w < progress ? done : idle;
      ctx.fillRect(x, mid - bh / 2, barW, bh);
    }
  };

  Player.prototype.seekFromEvent = function (e) {
    var rect = this.wave.getBoundingClientRect();
    var x = (e.clientX !== undefined ? e.clientX : 0) - rect.left;
    var pct = Math.min(1, Math.max(0, x / rect.width));
    if (this.audio.duration) this.audio.currentTime = pct * this.audio.duration;
  };

  Player.prototype.bind = function () {
    var self = this;

    this.toggle.addEventListener("click", function () {
      if (self.audio.paused) self.play(); else self.audio.pause();
    });

    this.wave.addEventListener("click", function (e) { self.seekFromEvent(e); });

    // Keyboard: arrows scrub, space/enter toggles, home/end jump.
    this.wave.addEventListener("keydown", function (e) {
      var d = self.audio.duration || 0;
      var k = e.key;
      if (k === "ArrowRight") { self.audio.currentTime = Math.min(d, self.audio.currentTime + 5); }
      else if (k === "ArrowLeft") { self.audio.currentTime = Math.max(0, self.audio.currentTime - 5); }
      else if (k === "Home") { self.audio.currentTime = 0; }
      else if (k === "End") { self.audio.currentTime = d; }
      else if (k === " " || k === "Enter") { if (self.audio.paused) self.play(); else self.audio.pause(); }
      else return;
      e.preventDefault();
      self.update();
    });

    this.audio.addEventListener("play", function () {
      // One at a time.
      players.forEach(function (p) { if (p !== self && !p.audio.paused) p.audio.pause(); });
      self.root.setAttribute("data-state", "playing");
      self.toggle.setAttribute("aria-label", "Pause");
    });

    this.audio.addEventListener("pause", function () {
      self.root.setAttribute("data-state", "paused");
      self.toggle.setAttribute("aria-label", "Play");
    });

    this.audio.addEventListener("timeupdate", function () { self.update(); });
    this.audio.addEventListener("loadedmetadata", function () { self.update(); });
    this.audio.addEventListener("ended", function () {
      self.root.setAttribute("data-state", "paused");
      self.audio.currentTime = 0;
      self.update();
    });

    var ro = window.ResizeObserver ? new ResizeObserver(function () { self.paint(); }) : null;
    if (ro) ro.observe(this.canvas); else window.addEventListener("resize", function () { self.paint(); });
  };

  Player.prototype.play = function () {
    var p = this.audio.play();
    if (p && p.catch) p.catch(function () { /* autoplay policy; user will retry */ });
  };

  Player.prototype.update = function () {
    var d = this.audio.duration;
    this.time.textContent = fmt(this.audio.currentTime) + " / " + (isFinite(d) ? fmt(d) : "--:--");
    this.wave.setAttribute("aria-valuenow", Math.round(this.audio.currentTime));
    if (isFinite(d)) this.wave.setAttribute("aria-valuemax", Math.round(d));
    this.wave.setAttribute("aria-valuetext", fmt(this.audio.currentTime) + " of " + (isFinite(d) ? fmt(d) : "unknown"));
    this.paint();
  };

  function init() {
    document.querySelectorAll(".player").forEach(function (el) {
      players.push(new Player(el));
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
