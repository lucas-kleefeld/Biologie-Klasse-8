/* =========================================================
   Virtuelles Lichtmikroskop
   Alle Präparate sind maßstabsgetreu in Mikrometern (µm) angelegt.
   Das Sehfeld ergibt sich aus der Sehfeldzahl des Okulars (18 mm)
   geteilt durch die Objektivvergrößerung.
   ========================================================= */
(function () {
  "use strict";
  var app = document.getElementById("mk");
  if (!app) return;

  var OKULAR = 10, FELDZAHL = 18;
  var OBJEKTIVE = [4, 10, 40, 100];
  var VERGLEICH_MASSE = [1, 40, 100, 400, 1000];

  /* ---------- Zufall mit festem Startwert: jedes Präparat sieht immer gleich aus ---------- */
  function rng(seed) {
    return function () {
      seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function hash(n) {
    n = Math.imul(n ^ 0x9e3779b9, 0x85ebca6b); n ^= n >>> 13;
    n = Math.imul(n, 0xc2b2ae35); n ^= n >>> 16;
    return (n >>> 0) / 4294967296;
  }
  function imKreis(r, R) { var a = r() * Math.PI * 2, d = R * Math.sqrt(r()); return [Math.cos(a) * d, Math.sin(a) * d]; }
  function gauss(r) { return (r() + r() + r() + r() - 2) * 1.2; }

  /* ---------- Farben (Färbungen) ---------- */
  var F = {
    blau: { f: "rgba(52,86,182,0.80)", r: "rgba(22,38,110,0.95)" },
    blauHell: { f: "rgba(118,148,226,0.20)", r: "rgba(66,96,182,0.70)", k: "rgba(40,62,160,0.80)", g: "rgba(70,96,180,0.35)" },
    violett: { f: "rgba(112,58,170,0.82)", r: "rgba(60,24,108,0.95)" },
    rosa: { f: "rgba(208,74,120,0.78)", r: "rgba(126,26,62,0.95)" },
    grau: { f: "rgba(118,118,118,0.70)", r: "rgba(60,60,60,0.90)" },
    fett: { f: "rgba(255,255,255,0.55)", r: "rgba(120,118,110,0.65)" },
    riese: { f: "rgba(236,232,212,0.60)", r: "rgba(128,112,72,0.90)" }
  };

  /* ---------- Bausteine zum Erzeugen ---------- */
  function stab(o, typ, x, y, l, b, w, c) { o.push({ k: "s", typ: typ, x: x, y: y, l: Math.max(l, b), b: b, w: w, c: c }); }
  function kugel(o, typ, x, y, r, c) { o.push({ k: "k", typ: typ, x: x, y: y, r: r, c: c }); }
  function kette(o, r, typ, x, y, n, d, c) {
    var w = r() * Math.PI * 2;
    for (var i = 0; i < n; i++) {
      kugel(o, typ, x, y, d / 2, c);
      w += (r() - 0.5) * 0.5; x += Math.cos(w) * d * 0.96; y += Math.sin(w) * d * 0.96;
    }
  }
  function stabkette(o, r, typ, x, y, n, l, b, c) {
    var w = r() * Math.PI * 2;
    for (var i = 0; i < n; i++) {
      var li = l * (0.75 + r() * 0.5);
      x += Math.cos(w) * li / 2; y += Math.sin(w) * li / 2;
      stab(o, typ, x, y, li, b, w, c);
      x += Math.cos(w) * (li / 2 + b * 0.25); y += Math.sin(w) * (li / 2 + b * 0.25);
      w += (r() - 0.5) * 0.35;
    }
  }
  function zelle(o, r, typ, x, y, rad, c) {
    var pts = []; for (var i = 0; i < 11; i++) pts.push(0.82 + r() * 0.3);
    var kw = r() * Math.PI * 2, kd = rad * (0.05 + r() * 0.2);
    o.push({ k: "z", typ: typ, x: x, y: y, r: rad, w: r() * Math.PI * 2, pts: pts, c: c,
      kx: Math.cos(kw) * kd, ky: Math.sin(kw) * kd, kr: 3.5 + r() * 1.3, id: o.length });
  }

  /* ---------- Präparate ---------- */
  var VIRUS = { name: "Grippevirus (zum Vergleich)", text: "ca. 0,1 µm", um: 0.1, virus: true };

  var PRAEPARATE = {
    mund: {
      name: "Mundschleimhaut", tropfen: "#7f9be3", umfang: 2300, start: "mundbakt",
      text: "Abstrich von der Innenseite der Wange, gefärbt mit Methylenblau. Neben den großen, flachen Zellen der Mundschleimhaut liegen Bakterien der Mundflora.",
      typen: {
        zelle: { name: "Mundschleimhautzelle", text: "ca. 60 µm", um: 60 },
        kern: { name: "Zellkern", text: "ca. 8 µm", um: 8, kern: true },
        mundbakt: { name: "Mundbakterien (Streptokokken)", text: "ca. 1 µm", um: 1, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [], zellen = [];
        zelle(o, r, "zelle", 0, 0, 31, F.blauHell); zellen.push(o[0]);
        for (var g = 0; g < 520; g++) {
          var m = g === 0 ? [40, 30] : imKreis(r, 2350), n = 2 + Math.floor(r() * 7);
          for (var i = 0; i < n; i++) {
            zelle(o, r, "zelle", m[0] + gauss(r) * 45, m[1] + gauss(r) * 45, 24 + r() * 12, F.blauHell);
            zellen.push(o[o.length - 1]);
          }
        }
        for (var b = 0; b < 16000; b++) {
          var p;
          if (r() < 0.7) { var z = zellen[Math.floor(r() * zellen.length)]; p = [z.x + gauss(r) * z.r * 0.7, z.y + gauss(r) * z.r * 0.7]; }
          else p = imKreis(r, 2400);
          if (r() < 0.8) kette(o, r, "mundbakt", p[0], p[1], 2 + Math.floor(r() * 5), 0.95, F.blau);
          else stab(o, "mundbakt", p[0], p[1], 1.6, 0.6, r() * 6.3, F.blau);
        }
        return o;
      }
    },
    joghurt: {
      name: "Joghurt", tropfen: "#9c8fe0", umfang: 2300, start: "lacto",
      text: "Ein Tropfen Joghurt mit Wasser verdünnt und mit Methylenblau gefärbt. Milchsäurebakterien machen aus Milch Joghurt. Die runden Fetttröpfchen stammen aus der Milch.",
      typen: {
        lacto: { name: "Milchsäurebakterium Lactobacillus (Stäbchen)", text: "ca. 5 µm lang", um: 5, bakterium: true },
        strepto: { name: "Streptococcus thermophilus (Kugeln in Ketten)", text: "ca. 1 µm", um: 1, bakterium: true },
        fett: { name: "Fetttröpfchen", text: "ca. 1–5 µm", um: 3 }
      },
      erzeugen: function (r) {
        var o = [];
        stabkette(o, r, "lacto", -4, 0, 3, 5.5, 0.75, F.blau);
        for (var f = 0; f < 15000; f++) { var p = imKreis(r, 2400); kugel(o, "fett", p[0], p[1], 0.5 + r() * r() * 2.6, F.fett); }
        for (var i = 0; i < 15000; i++) { var q = imKreis(r, 2400); stabkette(o, r, "lacto", q[0], q[1], 1 + Math.floor(r() * r() * 4), 5, 0.75, F.blau); }
        for (var k = 0; k < 7500; k++) { var s = imKreis(r, 2400); kette(o, r, "strepto", s[0], s[1], 3 + Math.floor(r() * 10), 0.95, F.blau); }
        return o;
      }
    },
    ecoli: {
      name: "Darmbakterien (E. coli)", tropfen: "#e38aa8", umfang: 2300, start: "ecoli",
      text: "Escherichia coli ist ein typisches Darmbakterium mit Stäbchenform. Die Bakterien sind angefärbt. Manche sind gerade dabei, sich zu teilen.",
      typen: {
        ecoli: { name: "Escherichia coli (Stäbchen)", text: "ca. 2 µm lang, 0,6 µm dick", um: 2, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [];
        stab(o, "ecoli", 0, 0, 2.1, 0.6, 0.6, F.rosa);
        for (var i = 0; i < 30000; i++) {
          var p = imKreis(r, 2400), w = r() * 6.3, l = 1.5 + r() * 1;
          if (r() < 0.15) {
            stab(o, "ecoli", p[0], p[1], l, 0.6, w, F.rosa);
            stab(o, "ecoli", p[0] + Math.cos(w) * (l + 0.15), p[1] + Math.sin(w) * (l + 0.15), l, 0.6, w, F.rosa);
          } else stab(o, "ecoli", p[0], p[1], l, 0.6, w, F.rosa);
        }
        return o;
      }
    },
    staph: {
      name: "Staphylokokken", tropfen: "#a07ad8", umfang: 2300, start: "staph",
      text: "Staphylokokken sind kugelförmige Bakterien, die in Haufen wie Weintrauben zusammenliegen. Manche Arten lösen Hautentzündungen aus.",
      typen: {
        staph: { name: "Staphylococcus (Kugeln in Trauben)", text: "ca. 1 µm", um: 1, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [];
        for (var c = 0; c < 9000; c++) {
          var m = c === 0 ? [0, 0] : imKreis(r, 2400), n = 3 + Math.floor(r() * 12);
          for (var i = 0; i < n; i++) kugel(o, "staph", m[0] + gauss(r) * 0.85, m[1] + gauss(r) * 0.85, 0.45 + r() * 0.08, F.violett);
        }
        return o;
      }
    },
    bacillus: {
      name: "Bacillus megaterium", tropfen: "#a07ad8", umfang: 2300, start: "bacillus",
      text: "Bacillus megaterium gehört zu den größten gewöhnlichen Bakterien. Die dicken Stäbchen hängen oft in Ketten aneinander. Der Name bedeutet „großes Tier“.",
      typen: {
        bacillus: { name: "Bacillus megaterium (dicke Stäbchen)", text: "ca. 5 µm lang, 1,5 µm dick", um: 5, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [];
        stabkette(o, r, "bacillus", -6, 0, 3, 4.8, 1.45, F.violett);
        for (var i = 0; i < 9000; i++) { var p = imKreis(r, 2400); stabkette(o, r, "bacillus", p[0], p[1], 1 + Math.floor(r() * 5), 4.8, 1.45, F.violett); }
        return o;
      }
    },
    thio: {
      name: "Riesenbakterium Thiomargarita", tropfen: "#d9cfa6", umfang: 2200, start: "thio",
      text: "Thiomargarita namibiensis lebt im Meeresboden vor Namibia. Die kugelförmigen Zellen hängen wie Perlen an einer Kette. Die hellen Körnchen sind Schwefel. Zum Vergleich liegen gewöhnliche Bakterien dazwischen.",
      typen: {
        thio: { name: "Thiomargarita namibiensis (Kugel)", text: "ca. 100–300 µm", um: 180, bakterium: true },
        klein: { name: "gewöhnliches Bakterium (zum Vergleich)", text: "ca. 2 µm", um: 2, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [], ketten = [];
        for (var c = 0; c < 26; c++) {
          var p = c === 0 ? [-60, 0] : imKreis(r, 2100), n = 3 + Math.floor(r() * 10), w = r() * 6.3, glied = [];
          var x = p[0], y = p[1];
          for (var i = 0; i < n; i++) {
            var rad = 55 + r() * 70, kr = [];
            for (var g = 0; g < 70; g++) { var q = imKreis(r, rad * 0.88); kr.push(q[0], q[1], 2 + r() * 2.5); }
            glied.push({ x: x, y: y, r: rad });
            o.push({ k: "r", typ: "thio", x: x, y: y, r: rad, c: F.riese, koerner: kr });
            w += (r() - 0.5) * 0.7; x += Math.cos(w) * rad * 2.05; y += Math.sin(w) * rad * 2.05;
          }
          ketten.push({ k: "h", typ: "-", x: glied[0].x, y: glied[0].y, r: 2000, glieder: glied });
        }
        for (var b = 0; b < 25000; b++) { var s = imKreis(r, 2400); stab(o, "klein", s[0], s[1], 1.6 + r() * 0.8, 0.6, r() * 6.3, F.grau); }
        return ketten.concat(o);
      }
    },
    elodea: {
      name: "Wasserpest-Blatt", tropfen: "#7cc77a", umfang: 1400, start: "chloro", eigen: true,
      text: "Ein Blättchen der Wasserpflanze Wasserpest, ungefärbt. Die Pflanzenzellen sind von einer Zellwand umgeben. Die grünen Körnchen sind Chloroplasten. Zum Vergleich mit den Bakterien: Auch Chloroplasten sind ungefähr so groß wie ein großes Bakterium.",
      typen: {
        blattzelle: { name: "Blattzelle der Wasserpest", text: "ca. 70 µm lang", um: 70 },
        chloro: { name: "Chloroplast", text: "ca. 5 µm", um: 5 }
      },
      erzeugen: function () { return []; }
    }
  };

  /* ---------- Zustand ---------- */
  var z = { p: "mund", obj: 2, vx: 0, vy: 0, fokus: 0, ziel: 0, beschriften: true, massstab: true, auswahl: null };
  var objekte = {};
  var feld = document.getElementById("mk-feld"), canvas = document.getElementById("mk-canvas"), ctx = canvas.getContext("2d");
  var dpr = 1, W = 0, R = 0, cx = 0, cy = 0, s = 1;
  var winzig = [];

  function sehfeldUm() { return FELDZAHL / OBJEKTIVE[z.obj] * 1000; }
  function gesamt() { return OKULAR * OBJEKTIVE[z.obj]; }
  function zahl(n, stellen) { return n.toLocaleString("de-DE", { maximumSignificantDigits: stellen || 2 }); }
  function laenge(mm) {
    if (mm >= 1000) return zahl(mm / 1000) + " m";
    if (mm >= 10) return zahl(mm / 10) + " cm";
    return zahl(mm) + " mm";
  }

  /* ---------- Zeichnen ---------- */
  var geplant = false;
  function neuZeichnen() { if (!geplant) { geplant = true; requestAnimationFrame(function () { geplant = false; zeichne(); }); } }

  function groesse() {
    var css = feld.clientWidth;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(css * dpr); canvas.height = Math.round(css * dpr);
    W = canvas.width; cx = cy = W / 2; R = W / 2 * 0.97;
    anzeigen(); neuZeichnen();
  }

  function sichtbar(X, Y, rad) { return Math.abs(X - cx) < R + rad && Math.abs(Y - cy) < R + rad; }

  function zeichneObjekt(o) {
    var X = cx + (o.x - z.vx) * s, Y = cy + (o.y - z.vy) * s, gr;
    if (o.k === "h") return zeichneHuelle(o);
    gr = (o.k === "s" ? o.l / 2 : o.k === "z" ? o.r * 1.2 : o.r) * s;
    if (!sichtbar(X, Y, gr + 2)) return;
    if (gr < 0.6 * dpr) { winzig.push(X, Y, o.c.r); return; }
    if (o.k === "s") {
      var L = o.l * s, B = Math.max(o.b * s, 1.1 * dpr), dx = Math.cos(o.w) * (L - B) / 2, dy = Math.sin(o.w) * (L - B) / 2;
      ctx.beginPath(); ctx.moveTo(X - dx, Y - dy); ctx.lineTo(X + dx, Y + dy);
      ctx.strokeStyle = o.c.r; ctx.lineWidth = B; ctx.stroke();
      if (B > 3.5 * dpr) { ctx.strokeStyle = o.c.f; ctx.lineWidth = B - Math.max(1.4 * dpr, B * 0.24); ctx.stroke(); }
    } else if (o.k === "k") {
      var rr = Math.max(o.r * s, 0.6 * dpr);
      ctx.beginPath(); ctx.arc(X, Y, rr, 0, 6.2832); ctx.fillStyle = o.c.r; ctx.fill();
      if (rr > 1.8 * dpr) { ctx.beginPath(); ctx.arc(X, Y, rr - Math.max(0.8 * dpr, rr * 0.25), 0, 6.2832); ctx.fillStyle = o.c.f; ctx.fill(); }
      if (o.typ === "fett" && rr > 4 * dpr) { ctx.beginPath(); ctx.arc(X - rr * 0.3, Y - rr * 0.3, rr * 0.25, 0, 6.2832); ctx.fillStyle = "rgba(255,255,255,0.9)"; ctx.fill(); }
    } else if (o.k === "z") {
      var n = o.pts.length;
      ctx.beginPath();
      for (var i = 0; i <= n; i++) {
        var a = o.w + i / n * 6.2832, a2 = o.w + (i + 0.5) / n * 6.2832;
        var r1 = o.r * o.pts[i % n] * s, r2 = o.r * (o.pts[i % n] + o.pts[(i + 1) % n]) / 2 * s;
        var px = X + Math.cos(a) * r1, py = Y + Math.sin(a) * r1, mx = X + Math.cos(a2) * r2, my = Y + Math.sin(a2) * r2;
        if (i === 0) ctx.moveTo(mx, my); else ctx.quadraticCurveTo(px, py, mx, my);
      }
      ctx.closePath(); ctx.fillStyle = o.c.f; ctx.fill();
      ctx.strokeStyle = o.c.r; ctx.lineWidth = Math.max(0.8 * dpr, Math.min(2.2 * dpr, 0.5 * s)); ctx.stroke();
      if (o.r * s > 40 * dpr) {
        ctx.fillStyle = o.c.g;
        for (var g = 0; g < 40; g++) {
          var ga = hash(o.id * 97 + g) * 6.2832, gd = Math.sqrt(hash(o.id * 131 + g)) * o.r * 0.75 * s;
          ctx.beginPath(); ctx.arc(X + Math.cos(ga) * gd, Y + Math.sin(ga) * gd, Math.max(0.6 * dpr, 0.5 * s), 0, 6.2832); ctx.fill();
        }
      }
      ctx.beginPath(); ctx.arc(X + o.kx * s, Y + o.ky * s, Math.max(0.6 * dpr, o.kr * s), 0, 6.2832); ctx.fillStyle = o.c.k; ctx.fill();
    } else if (o.k === "r") {
      var rr2 = o.r * s;
      ctx.beginPath(); ctx.arc(X, Y, rr2, 0, 6.2832); ctx.fillStyle = o.c.f; ctx.fill();
      ctx.strokeStyle = o.c.r; ctx.lineWidth = Math.max(0.8 * dpr, Math.min(3 * dpr, 1.5 * s)); ctx.stroke();
      if (rr2 > 10 * dpr) {
        for (var k = 0; k < o.koerner.length; k += 3) {
          var kxx = X + o.koerner[k] * s, kyy = Y + o.koerner[k + 1] * s, krr = Math.max(0.7 * dpr, o.koerner[k + 2] * s);
          ctx.beginPath(); ctx.arc(kxx, kyy, krr, 0, 6.2832); ctx.fillStyle = "rgba(255,255,250,0.95)"; ctx.fill();
          if (krr > 2 * dpr) { ctx.strokeStyle = "rgba(110,100,70,0.75)"; ctx.lineWidth = Math.max(0.7 * dpr, krr * 0.2); ctx.stroke(); }
        }
      }
    }
  }

  function zeichneHuelle(o) {
    var g = o.glieder;
    ctx.beginPath();
    for (var i = 0; i < g.length; i++) { var X = cx + (g[i].x - z.vx) * s, Y = cy + (g[i].y - z.vy) * s; if (i) ctx.lineTo(X, Y); else ctx.moveTo(X, Y); }
    if (g.length === 1) ctx.lineTo(cx + (g[0].x - z.vx) * s + 0.1, cy + (g[0].y - z.vy) * s);
    ctx.strokeStyle = "rgba(206,196,150,0.22)"; ctx.lineCap = "round"; ctx.lineJoin = "round";
    ctx.lineWidth = 2 * 150 * s; ctx.stroke();
  }

  /* Wasserpest: Blattzellen werden direkt aus ihrer Lage berechnet */
  var CW = 72, CH = 22;
  function blattrand(x) { return 620 + 40 * Math.sin(x / 380) + 18 * Math.sin(x / 97); }
  function zeichneElodea() {
    var x0 = z.vx - R / s, x1 = z.vx + R / s, y0 = z.vy - R / s, y1 = z.vy + R / s;
    // Blattfläche
    ctx.beginPath();
    var schritt = Math.max(4, 12 / s);
    for (var x = x0 - schritt; x <= x1 + schritt; x += schritt) { var X = cx + (x - z.vx) * s, Y = cy + (-blattrand(x) - z.vy) * s; if (x === x0 - schritt) ctx.moveTo(X, Y); else ctx.lineTo(X, Y); }
    for (x = x1 + schritt; x >= x0 - schritt; x -= schritt) ctx.lineTo(cx + (x - z.vx) * s, cy + (blattrand(x) - z.vy) * s);
    ctx.closePath(); ctx.fillStyle = "rgba(150,200,120,0.32)"; ctx.fill();
    ctx.strokeStyle = "rgba(70,120,50,0.75)"; ctx.lineWidth = Math.max(1 * dpr, 2 * s); ctx.stroke();

    if (CH * s < 1.6 * dpr) return;
    var j0 = Math.floor(Math.max(y0, -700) / CH), j1 = Math.ceil(Math.min(y1, 700) / CH);
    ctx.lineWidth = Math.max(0.6 * dpr, Math.min(2 * dpr, 1.2 * s));
    ctx.strokeStyle = "rgba(70,120,50," + (CH * s < 5 * dpr ? 0.35 : 0.7) + ")";
    var chloro = 5 * s >= 1.4 * dpr;
    for (var j = j0; j <= j1; j++) {
      var versatz = (j % 2 ? CW / 2 : 0) + (j % 3) * 7;
      var i0 = Math.floor((x0 - versatz) / CW) - 1, i1 = Math.ceil((x1 - versatz) / CW);
      for (var i = i0; i <= i1; i++) {
        var lx = i * CW + versatz, ly = j * CH, mx = lx + CW / 2;
        var rand = blattrand(mx);
        if (ly < -rand || ly + CH > rand) continue;
        var X0 = cx + (lx - z.vx) * s, Y0 = cy + (ly - z.vy) * s;
        ctx.strokeRect(X0, Y0, CW * s, CH * s);
        if (chloro) {
          var id = (i * 7919 + j * 104729) | 0, n = 14 + Math.floor(hash(id) * 10);
          ctx.fillStyle = "rgba(48,140,52,0.88)";
          for (var c = 0; c < n; c++) {
            var t = hash(id + c * 31), seite = hash(id + c * 57), px, py;
            var innen = 3 + hash(id + c * 13) * 4;
            if (seite < 0.42) { px = lx + 4 + t * (CW - 8); py = ly + innen; }
            else if (seite < 0.84) { px = lx + 4 + t * (CW - 8); py = ly + CH - innen; }
            else { px = (seite < 0.92 ? lx + innen : lx + CW - innen); py = ly + 4 + t * (CH - 8); }
            ctx.beginPath(); ctx.ellipse(cx + (px - z.vx) * s, cy + (py - z.vy) * s, 2.7 * s, 1.9 * s, t * 3, 0, 6.2832); ctx.fill();
            if (5 * s > 6 * dpr) { ctx.strokeStyle = "rgba(20,80,24,0.8)"; ctx.lineWidth = Math.max(0.6 * dpr, 0.3 * s); ctx.stroke(); ctx.strokeStyle = "rgba(70,120,50,0.7)"; ctx.lineWidth = Math.max(0.6 * dpr, Math.min(2 * dpr, 1.2 * s)); }
          }
        }
      }
    }
  }

  function beschriftungenElodea() {
    var j = Math.floor(z.vy / CH), versatz = (j % 2 ? CW / 2 : 0) + (j % 3) * 7, i = Math.floor((z.vx - versatz) / CW);
    var lx = i * CW + versatz, ly = j * CH, liste = [];
    if (Math.abs(ly) > 600) return liste;
    liste.push({ typ: "blattzelle", x: lx + CW / 2, y: ly + CH / 2, r: CH / 2 });
    var id = (i * 7919 + j * 104729) | 0, t = hash(id), innen = 3 + hash(id + 13) * 4;
    liste.push({ typ: "chloro", x: lx + 4 + hash(id + 31) * (CW - 8), y: hash(id + 57) < 0.42 ? ly + innen : ly + CH - innen, r: 2.5 });
    return liste;
  }

  function beschriftungsziele() {
    var p = PRAEPARATE[z.p];
    if (p.eigen) return beschriftungenElodea();
    var beste = {}, liste = objekte[z.p];
    for (var i = 0; i < liste.length; i++) {
      var o = liste[i];
      if (!p.typen[o.typ]) continue;
      var d = (o.x - z.vx) * (o.x - z.vx) + (o.y - z.vy) * (o.y - z.vy);
      if (!beste[o.typ] || d < beste[o.typ].d) beste[o.typ] = { d: d, o: o };
      if (o.k === "z" && p.typen.kern) {
        var kx = o.x + o.kx, ky = o.y + o.ky, dk = (kx - z.vx) * (kx - z.vx) + (ky - z.vy) * (ky - z.vy);
        if (!beste.kern || dk < beste.kern.d) beste.kern = { d: dk, o: { x: kx, y: ky, r: o.kr, k: "kern" } };
      }
    }
    var ziele = [];
    Object.keys(beste).forEach(function (t) {
      var o = beste[t].o, rad = o.k === "s" ? o.l / 2 : o.r;
      ziele.push({ typ: t, x: o.x, y: o.y, r: rad });
    });
    return ziele;
  }

  function kurzname(t) { return PRAEPARATE[z.p].typen[t].name.replace(/\s*\(.*\)/, ""); }

  function zeichneBeschriftungen() {
    var ziele = beschriftungsziele(), belegt = [], css = dpr;
    ctx.font = "700 " + Math.round(21 * css) + "px Caveat, cursive";
    ctx.lineJoin = "round";
    ziele.forEach(function (zl, idx) {
      var X = cx + (zl.x - z.vx) * s, Y = cy + (zl.y - z.vy) * s, rad = zl.r * s;
      if (rad * 2 < 4 * css) return;
      if (Math.hypot(X - cx, Y - cy) > R * 0.8) return;
      var basis = Math.atan2(Y - cy, X - cx);
      if (Math.hypot(X - cx, Y - cy) < 20 * css) basis = -0.8 + idx * 2.1;
      var text = kurzname(zl.typ), tw = ctx.measureText(text).width, gesetzt = null;
      for (var v = 0; v < 8 && !gesetzt; v++) {
        var w = basis + [0, 0.7, -0.7, 1.4, -1.4, 2.2, -2.2, 3.1][v];
        var abst = rad + 38 * css, lx = X + Math.cos(w) * abst, ly = Y + Math.sin(w) * abst;
        if (Math.hypot(lx - cx, ly - cy) > R * 0.88) continue;
        var links = Math.cos(w) < 0, bx = links ? lx - tw - 6 * css : lx + 6 * css, box = [bx, ly - 14 * css, tw, 22 * css];
        if (bx < cx - R * 0.95 || bx + tw > cx + R * 0.95) continue;
        var frei = belegt.every(function (b) { return box[0] > b[0] + b[2] + 6 || box[0] + box[2] + 6 < b[0] || box[1] > b[1] + b[3] || box[1] + box[3] < b[1]; });
        if (frei) gesetzt = { w: w, lx: lx, ly: ly, bx: bx, box: box };
      }
      if (!gesetzt) return;
      belegt.push(gesetzt.box);
      var sx = X + Math.cos(gesetzt.w) * (rad + 2 * css), sy = Y + Math.sin(gesetzt.w) * (rad + 2 * css);
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(gesetzt.lx, gesetzt.ly);
      ctx.strokeStyle = "rgba(255,255,255,0.9)"; ctx.lineWidth = 4.5 * css; ctx.stroke();
      ctx.strokeStyle = "#1f2a36"; ctx.lineWidth = 1.8 * css; ctx.stroke();
      ctx.beginPath(); ctx.arc(sx, sy, 2.4 * css, 0, 6.2832); ctx.fillStyle = "#1f2a36"; ctx.fill();
      ctx.textBaseline = "middle"; ctx.textAlign = "left";
      ctx.strokeStyle = "rgba(255,255,255,0.95)"; ctx.lineWidth = 5 * css; ctx.strokeText(text, gesetzt.bx, gesetzt.ly);
      ctx.fillStyle = "#1f2a36"; ctx.fillText(text, gesetzt.bx, gesetzt.ly);
    });
  }

  function zeichneMassstab() {
    var ziel = 0.3 * 2 * R / s, werte = [0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000], l = werte[0];
    werte.forEach(function (w) { if (w <= ziel) l = w; });
    var px = l * s, x0 = cx - px / 2, y0 = cy + R * 0.76, css = dpr;
    ctx.lineCap = "butt";
    ctx.fillStyle = "rgba(255,255,255,0.88)"; ctx.fillRect(x0 - 8 * css, y0 - 30 * css, px + 16 * css, 42 * css);
    ctx.fillStyle = "#1f2a36"; ctx.fillRect(x0, y0, px, 5 * css);
    ctx.fillRect(x0, y0 - 5 * css, 2 * css, 15 * css); ctx.fillRect(x0 + px - 2 * css, y0 - 5 * css, 2 * css, 15 * css);
    ctx.font = "700 " + Math.round(20 * css) + "px Caveat, cursive"; ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    ctx.fillText(l >= 1000 ? zahl(l / 1000) + " mm" : zahl(l) + " µm", cx, y0 - 9 * css);
  }

  function zeichne() {
    if (!W) return;
    var p = PRAEPARATE[z.p];
    s = 2 * R / sehfeldUm();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    var hg = ctx.createRadialGradient(cx, cy, 0, cx, cy, R);
    hg.addColorStop(0, "#fffef8"); hg.addColorStop(1, "#f3efe0");
    ctx.fillStyle = hg; ctx.fillRect(0, 0, W, W);
    ctx.save(); ctx.beginPath(); ctx.arc(cx, cy, R, 0, 6.2832); ctx.clip();
    ctx.lineCap = "round";
    if (p.eigen) zeichneElodea();
    else {
      var liste = objekte[z.p]; winzig = [];
      for (var i = 0; i < liste.length; i++) zeichneObjekt(liste[i]);
      // sehr kleine Objekte gesammelt als einzelne Bildpunkte zeichnen (schneller)
      ctx.globalAlpha = 0.35; var farbe = null;
      for (var w = 0; w < winzig.length; w += 3) { if (winzig[w + 2] !== farbe) { farbe = winzig[w + 2]; ctx.fillStyle = farbe; } ctx.fillRect(winzig[w], winzig[w + 1], dpr, dpr); }
      ctx.globalAlpha = 1; winzig = [];
    }
    if (z.beschriften) zeichneBeschriftungen();
    if (z.massstab) zeichneMassstab();
    ctx.restore();
    var unschaerfe = Math.abs(z.fokus - z.ziel) * (0.7 + z.obj * 0.25);
    canvas.style.filter = unschaerfe > 0 ? "blur(" + unschaerfe.toFixed(1) + "px)" : "none";
  }

  /* ---------- Anzeige der Werte ---------- */
  var el = {
    gesamt: document.getElementById("mk-gesamt"), rechnung: document.getElementById("mk-rechnung"),
    sehfeld: document.getElementById("mk-sehfeld"), hinweis: document.getElementById("mk-hinweis"),
    erkennbar: document.getElementById("mk-erkennbar"), text: document.getElementById("mk-text"),
    liste: document.getElementById("mk-liste"), leiter: document.getElementById("mk-leiter"), leitertext: document.getElementById("mk-leitertext"),
    fein: document.getElementById("mk-feintrieb")
  };

  function vergleich(mm) {
    if (mm < 0.1) return "zu klein, um es mit dem Auge zu erkennen";
    if (mm < 0.4) return "etwa wie ein Staubkorn";
    if (mm < 1.5) return "etwa wie ein Sandkorn";
    if (mm < 3.5) return "etwa wie ein Stecknadelkopf";
    if (mm < 9) return "etwa wie ein Reiskorn";
    if (mm < 18) return "etwa wie ein Fingernagel";
    if (mm < 40) return "etwa wie eine Münze";
    if (mm < 110) return "etwa wie eine Streichholzschachtel";
    if (mm < 300) return "etwa wie ein Handy";
    return "größer als ein Schulheft";
  }

  function erkennbarText() {
    var p = PRAEPARATE[z.p], ja = [], nein = [], css = feld.clientWidth * 0.97 / sehfeldUm();
    Object.keys(p.typen).forEach(function (t) {
      var px = p.typen[t].um * css;
      (px >= 3 ? ja : nein).push(kurzname(t));
    });
    var txt = "";
    if (ja.length) txt += "Erkennbar: " + ja.join(", ") + ". ";
    if (nein.length) txt += "Noch zu klein: " + nein.join(", ") + ".";
    return txt;
  }

  function anzeigen() {
    var p = PRAEPARATE[z.p], m = gesamt();
    el.gesamt.textContent = zahl(m, 4) + "×";
    el.rechnung.textContent = OKULAR + " (Okular) × " + OBJEKTIVE[z.obj] + " (Objektiv) = " + zahl(m, 4) + "-fach";
    el.sehfeld.textContent = zahl(sehfeldUm() / 1000) + " mm";
    var h = [];
    if (OBJEKTIVE[z.obj] === 100) h.push("Für das 100er-Objektiv gibt man einen Tropfen Immersionsöl auf das Deckglas.");
    if (z.fokus !== z.ziel) h.push("Das Bild ist unscharf. Stelle es mit dem Feintrieb scharf.");
    el.hinweis.textContent = h.join(" ");
    el.hinweis.hidden = !h.length;
    el.erkennbar.textContent = erkennbarText();
    el.text.textContent = p.text;
    canvas.setAttribute("aria-label", "Blick durch das Mikroskop: " + p.name + " bei " + zahl(m, 4) + "-facher Vergrößerung. " + erkennbarText());
    document.querySelectorAll("#mk [data-praeparat]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-praeparat") === z.p ? "true" : "false"); });
    document.querySelectorAll("#mk [data-objektiv]").forEach(function (b) { b.setAttribute("aria-pressed", +b.getAttribute("data-objektiv") === z.obj ? "true" : "false"); });
    var rev = document.getElementById("mk-revolver");
    if (rev) rev.style.transform = "rotate(" + (-z.obj * 32) + "deg)";
    var tr = document.getElementById("mk-tropfen"); if (tr) tr.setAttribute("fill", p.tropfen);
    var fm = document.getElementById("mk-feinmarke"); if (fm) fm.style.transform = "rotate(" + (z.fokus * 18) + "deg)";
    var ti = document.getElementById("mk-tisch"); if (ti) ti.style.transform = "translateY(" + (z.fokus * -0.5) + "px)";
    document.querySelectorAll("#mk-revolver [data-obj]").forEach(function (g) { g.classList.toggle("aktiv", +g.getAttribute("data-obj") === z.obj); });
    listeAnzeigen(); leiterAnzeigen();
  }

  function alleTypen() {
    var p = PRAEPARATE[z.p], t = Object.keys(p.typen).map(function (k) { return { key: k, d: p.typen[k] }; });
    t.push({ key: "virus", d: VIRUS });
    return t;
  }

  function listeAnzeigen() {
    var m = gesamt(), html = "";
    alleTypen().forEach(function (t) {
      var mm = t.d.um / 1000 * m;
      html += '<li><button type="button" data-typ="' + t.key + '" aria-pressed="' + (z.auswahl === t.key) + '">' +
        '<span class="mk-name">' + t.d.name + '</span>' +
        '<span class="mk-wirklich">wirklich ' + t.d.text + '</span>' +
        '<span class="mk-schein">erscheint ' + laenge(mm) + ' groß, ' + (t.d.virus ? "bleibt aber unsichtbar" : vergleich(mm)) + '</span></button></li>';
    });
    el.liste.innerHTML = html;
  }

  function leiterAnzeigen() {
    var t = alleTypen().filter(function (x) { return x.key === z.auswahl; })[0] || alleTypen()[0];
    var mmEcht = t.d.um / 1000, L = 24, Rr = 676, MIN = -3, MAX = 3, achse = 120;
    function X(mm) { return L + (Math.log10(mm) - MIN) / (MAX - MIN) * (Rr - L); }
    var svg = '<svg class="ill" viewBox="0 0 700 210" role="img" aria-labelledby="mk-leiter-t"><title id="mk-leiter-t">Größenleiter: So groß erscheint ' + t.d.name + ' ohne Mikroskop und bei 40-, 100-, 400- und 1000-facher Vergrößerung</title>';
    svg += '<rect class="f-rosa-weich" x="' + L + '" y="34" width="' + (X(0.1) - L) + '" height="' + (achse - 34) + '" rx="10"/>';
    svg += '<text class="hk" x="' + (L + 12) + '" y="80">für das Auge</text><text class="hk" x="' + (L + 12) + '" y="100">zu klein</text>';
    var refs = [[0.07, "Haar (Dicke)", 1], [1, "Sandkorn", 0], [6, "Reiskorn", 1], [23, "1-Euro-Münze", 0], [150, "Handy", 1]];
    refs.forEach(function (r) {
      var x = X(r[0]), y = r[2] ? 52 : 92;
      svg += '<line class="s2" x1="' + x + '" y1="' + (y + 8) + '" x2="' + x + '" y2="' + achse + '" stroke-dasharray="2 5"/><text class="hk" x="' + x + '" y="' + y + '" text-anchor="middle">' + r[1] + '</text>';
    });
    svg += '<line class="s" x1="' + L + '" y1="' + achse + '" x2="' + Rr + '" y2="' + achse + '"/>';
    [[0.001, "0,001 mm"], [0.01, "0,01 mm"], [0.1, "0,1 mm"], [1, "1 mm"], [10, "1 cm"], [100, "10 cm"], [1000, "1 m"]].forEach(function (d) {
      var x = X(d[0]);
      svg += '<line class="s2" x1="' + x + '" y1="' + (achse - 5) + '" x2="' + x + '" y2="' + (achse + 5) + '"/><text class="hk" x="' + x + '" y="' + (achse + 24) + '" text-anchor="middle" style="font-size:15px">' + d[1] + '</text>';
    });
    VERGLEICH_MASSE.forEach(function (m, i) {
      var mm = mmEcht * m, x = X(mm), aktiv = m === gesamt(), raus = mm < 0.001;
      if (raus) x = L;
      var y = achse + 52;
      svg += '<line class="s2" x1="' + x + '" y1="' + (achse + 30) + '" x2="' + x + '" y2="' + (y - 9) + '"/>';
      svg += '<circle class="s ' + (aktiv ? "f-blau-tief" : "f-weiss") + '" cx="' + x + '" cy="' + y + '" r="' + (aktiv ? 9 : 6) + '"/>';
      var lab = m === 1 ? "ohne Mikroskop" : m + "×";
      svg += '<text class="' + (aktiv ? "h" : "hk") + '" x="' + x + '" y="' + (y + (i % 2 ? 26 : 30)) + '" text-anchor="' + (x < 70 ? "start" : x > 640 ? "end" : "middle") + '">' + (raus ? "◂ " : "") + lab + '</text>';
    });
    svg += "</svg>";
    el.leiter.innerHTML = svg;
    var jetzt = mmEcht * gesamt();
    var echt = t.d.text.replace("ca. ", "etwa ");
    if (!/lang|dick/.test(echt)) echt += " groß";
    var satz = t.d.name.replace(/\s*\(.*\)/, "") + ": in Wirklichkeit " + echt + " (" + zahl(mmEcht, 2) + " mm). " +
      "Bei " + zahl(gesamt(), 4) + "-facher Vergrößerung wirkt das " + laenge(jetzt) + " groß";
    if (t.d.virus) satz += ". Trotzdem sieht man Viren im Lichtmikroskop nicht: Alles, was kleiner als etwa 0,2 µm ist, kann ein Lichtmikroskop nicht mehr auflösen. Dafür braucht man ein Elektronenmikroskop.";
    else satz += ", " + vergleich(jetzt) + ".";
    el.leitertext.textContent = satz;
  }

  /* ---------- Bedienung ---------- */
  function praeparatWaehlen(key) {
    z.p = key; z.vx = 0; z.vy = 0;
    if (!objekte[key]) objekte[key] = PRAEPARATE[key].erzeugen(rng(key.length * 7919 + key.charCodeAt(0)));
    z.auswahl = PRAEPARATE[key].start;
    anzeigen(); neuZeichnen();
  }
  function objektivWaehlen(i) {
    if (i === z.obj) return;
    z.obj = i;
    var neu; do { neu = Math.round((Math.random() - 0.5) * 6); } while (neu === z.fokus && Math.random() < 0.6);
    z.ziel = Math.abs(neu) > 3 ? 3 * Math.sign(neu) : neu;
    if (z.ziel === z.fokus) z.ziel = z.fokus + (z.fokus < 3 ? 2 : -2);
    anzeigen(); neuZeichnen();
  }

  app.addEventListener("click", function (e) {
    var b = e.target.closest("[data-praeparat], [data-objektiv], [data-typ], [data-obj]");
    if (!b) return;
    if (b.hasAttribute("data-praeparat")) praeparatWaehlen(b.getAttribute("data-praeparat"));
    else if (b.hasAttribute("data-objektiv")) objektivWaehlen(+b.getAttribute("data-objektiv"));
    else if (b.hasAttribute("data-obj")) objektivWaehlen(+b.getAttribute("data-obj"));
    else { z.auswahl = b.getAttribute("data-typ"); listeAnzeigen(); leiterAnzeigen(); var n = el.liste.querySelector('[data-typ="' + z.auswahl + '"]'); if (n) n.focus(); }
  });
  el.fein.addEventListener("input", function () { z.fokus = +el.fein.value; anzeigen(); neuZeichnen(); });
  document.getElementById("mk-beschriften").addEventListener("change", function (e) { z.beschriften = e.target.checked; neuZeichnen(); });
  document.getElementById("mk-massstab").addEventListener("change", function (e) { z.massstab = e.target.checked; neuZeichnen(); });

  function verschieben(dxUm, dyUm) {
    var u = PRAEPARATE[z.p].umfang;
    z.vx = Math.max(-u, Math.min(u, z.vx + dxUm)); z.vy = Math.max(-u, Math.min(u, z.vy + dyUm));
    neuZeichnen();
  }
  var ziehen = null;
  feld.addEventListener("pointerdown", function (e) { ziehen = { x: e.clientX, y: e.clientY }; feld.setPointerCapture(e.pointerId); feld.classList.add("zieht"); });
  feld.addEventListener("pointermove", function (e) {
    if (!ziehen) return;
    var dx = e.clientX - ziehen.x, dy = e.clientY - ziehen.y; ziehen = { x: e.clientX, y: e.clientY };
    verschieben(-dx * dpr / s, -dy * dpr / s);
  });
  function loslassen() { ziehen = null; feld.classList.remove("zieht"); }
  feld.addEventListener("pointerup", loslassen); feld.addEventListener("pointercancel", loslassen);
  feld.addEventListener("keydown", function (e) {
    var d = sehfeldUm() * 0.1, k = { ArrowLeft: [-d, 0], ArrowRight: [d, 0], ArrowUp: [0, -d], ArrowDown: [0, d] }[e.key];
    if (k) { e.preventDefault(); verschieben(k[0], k[1]); }
  });

  if (window.ResizeObserver) new ResizeObserver(groesse).observe(feld); else window.addEventListener("resize", groesse);
  praeparatWaehlen(z.p);
  groesse();
  if (document.fonts && document.fonts.load) document.fonts.load("700 20px Caveat").then(neuZeichnen, function () {});
})();
