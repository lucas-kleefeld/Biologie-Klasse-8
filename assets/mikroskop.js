/* =========================================================
   Virtuelles Licht- und Elektronenmikroskop
   Alle Präparate sind maßstabsgetreu in Mikrometern (µm) angelegt.
   Die Breite des Bildausschnitts ergibt sich wie beim Schulmikroskop
   aus der Sehfeldzahl (18 mm) geteilt durch die Objektivvergrößerung,
   also 180 000 µm geteilt durch die Gesamtvergrößerung.
   ========================================================= */
(function () {
  "use strict";
  var app = document.getElementById("mk");
  if (!app) return;

  var GERAETE = {
    licht: {
      name: "Lichtmikroskop", stufen: [40, 100, 400, 1000], knopf: ["4×", "10×", "40×", "100× Öl"],
      ringe: ["#d23b3b", "#e8b923", "#5aa7e0", "#f6f6f6"], vergleich: [1, 40, 100, 400, 1000], min: -3,
      legende: "Objektiv", notiz: "Das Okular vergrößert immer 10-fach.", start: "mund", startStufe: 2
    },
    elektronen: {
      name: "Elektronenmikroskop", stufen: [1000, 10000, 100000, 500000], knopf: ["1 000×", "10 000×", "100 000×", "500 000×"],
      vergleich: [1, 1000, 10000, 100000, 500000], min: -5,
      legende: "Vergrößerung", notiz: "Statt Licht nutzt das Gerät einen Elektronenstrahl. Die Vergrößerung wird mit Magnetlinsen eingestellt, das Bild erscheint auf einem Bildschirm.",
      start: "grippe", startStufe: 2
    }
  };

  /* ---------- Zufall mit festem Startwert ---------- */
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
  var TAU = 6.2832;

  /* ---------- Farben ---------- */
  var F = {
    blau: { f: "rgba(52,86,182,0.80)", r: "rgba(22,38,110,0.95)" },
    blauHell: { f: "rgba(118,148,226,0.20)", r: "rgba(66,96,182,0.70)", k: "rgba(40,62,160,0.80)", g: "rgba(70,96,180,0.35)" },
    violett: { f: "rgba(112,58,170,0.82)", r: "rgba(60,24,108,0.95)" },
    rosa: { f: "rgba(208,74,120,0.78)", r: "rgba(126,26,62,0.95)" },
    grau: { f: "rgba(118,118,118,0.70)", r: "rgba(60,60,60,0.90)" },
    fett: { f: "rgba(255,255,255,0.55)", r: "rgba(120,118,110,0.65)" },
    riese: { f: "rgba(236,232,212,0.60)", r: "rgba(128,112,72,0.90)" },
    em: { r: "#c9ced2" }
  };

  /* ---------- Bausteine ---------- */
  function stab(o, typ, x, y, l, b, w, c) { o.push({ k: "s", typ: typ, x: x, y: y, l: Math.max(l, b), b: b, w: w, c: c }); }
  function kugel(o, typ, x, y, r, c) { o.push({ k: "k", typ: typ, x: x, y: y, r: r, c: c }); }
  function kette(o, r, typ, x, y, n, d, c) {
    var w = r() * TAU;
    for (var i = 0; i < n; i++) { kugel(o, typ, x, y, d / 2, c); w += (r() - 0.5) * 0.5; x += Math.cos(w) * d * 0.96; y += Math.sin(w) * d * 0.96; }
  }
  function stabkette(o, r, typ, x, y, n, l, b, c) {
    var w = r() * TAU;
    for (var i = 0; i < n; i++) {
      var li = l * (0.75 + r() * 0.5);
      x += Math.cos(w) * li / 2; y += Math.sin(w) * li / 2;
      stab(o, typ, x, y, li, b, w, c);
      x += Math.cos(w) * (li / 2 + b * 0.25); y += Math.sin(w) * (li / 2 + b * 0.25);
      w += (r() - 0.5) * 0.35;
    }
  }
  function zelle(o, r, typ, x, y, rad, c, k) {
    var pts = []; for (var i = 0; i < 11; i++) pts.push(0.82 + r() * 0.3);
    var kw = r() * TAU, kd = rad * (0.05 + r() * 0.2);
    o.push({ k: k || "z", typ: typ, x: x, y: y, r: rad, w: r() * TAU, pts: pts, c: c,
      kx: Math.cos(kw) * kd, ky: Math.sin(kw) * kd, kr: 3.5 + r() * 1.3, id: o.length });
  }

  var VIRUS = { name: "Grippevirus (zum Vergleich)", text: "ca. 0,1 µm", um: 0.1, virus: true };

  /* =========================================================
     Präparate für das Lichtmikroskop
     ========================================================= */
  var PRAEPARATE = {
    mund: {
      geraet: "licht", name: "Mundschleimhaut", tropfen: "#7f9be3", umfang: 2300, start: "mundbakt",
      text: "Abstrich von der Innenseite der Wange, gefärbt mit Methylenblau. Neben den großen, flachen Zellen der Mundschleimhaut liegen Bakterien der Mundflora.",
      typen: {
        zelle: { name: "Mundschleimhautzelle", text: "ca. 60 µm", um: 60 },
        kern: { name: "Zellkern", text: "ca. 8 µm", um: 8 },
        mundbakt: { name: "Mundbakterien (Streptokokken)", text: "ca. 1 µm", um: 1, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [], zellen = [];
        zelle(o, r, "zelle", 0, 0, 31, F.blauHell); zellen.push(o[0]);
        for (var g = 0; g < 520; g++) {
          var m = g === 0 ? [40, 30] : imKreis(r, 2350), n = 2 + Math.floor(r() * 7);
          for (var i = 0; i < n; i++) { zelle(o, r, "zelle", m[0] + gauss(r) * 45, m[1] + gauss(r) * 45, 24 + r() * 12, F.blauHell); zellen.push(o[o.length - 1]); }
        }
        for (var b = 0; b < 16000; b++) {
          var p;
          if (r() < 0.7) { var zl = zellen[Math.floor(r() * zellen.length)]; p = [zl.x + gauss(r) * zl.r * 0.7, zl.y + gauss(r) * zl.r * 0.7]; }
          else p = imKreis(r, 2400);
          if (r() < 0.8) kette(o, r, "mundbakt", p[0], p[1], 2 + Math.floor(r() * 5), 0.95, F.blau);
          else stab(o, "mundbakt", p[0], p[1], 1.6, 0.6, r() * TAU, F.blau);
        }
        return o;
      }
    },
    zwiebel: {
      geraet: "licht", name: "Zwiebelhaut", tropfen: "#d9a441", umfang: 2500, start: "zwiebelzelle",
      text: "Das dünne Häutchen von der Innenseite einer Zwiebelschuppe, angefärbt mit Iod-Kaliumiodid-Lösung. Die Pflanzenzellen liegen wie Mauersteine nebeneinander. In jeder Zelle erkennt man einen Zellkern.",
      typen: {
        zwiebelzelle: { name: "Zwiebelhautzelle", text: "ca. 250 µm lang", um: 250 },
        kern: { name: "Zellkern", text: "ca. 20 µm", um: 20 }
      },
      erzeugen: function () { return {}; },
      zeichnen: zeichneZwiebel, ziele: zieleZwiebel
    },
    elodea: {
      geraet: "licht", name: "Wasserpest-Blatt", tropfen: "#7cc77a", umfang: 1400, start: "chloro",
      text: "Ein Blättchen der Wasserpflanze Wasserpest, ungefärbt. Die Pflanzenzellen sind von einer Zellwand umgeben. Die grünen Körnchen sind Chloroplasten, ungefähr so groß wie ein großes Bakterium.",
      typen: {
        blattzelle: { name: "Blattzelle der Wasserpest", text: "ca. 70 µm lang", um: 70 },
        chloro: { name: "Chloroplast", text: "ca. 5 µm", um: 5 }
      },
      erzeugen: function () { return {}; },
      zeichnen: zeichneElodea, ziele: zieleElodea
    },
    haar: {
      geraet: "licht", name: "Menschliches Haar", tropfen: "#8a5a2b", umfang: 2500, start: "haar",
      text: "Drei Kopfhaare, ungefärbt: zwei dunkle und ein blondes. Die Oberfläche ist mit flachen Schuppen bedeckt, die wie Dachziegel übereinanderliegen. Die dunklen Körnchen sind Farbstoff (Pigment).",
      typen: {
        haar: { name: "Menschliches Haar (Dicke)", text: "ca. 70 µm dick", um: 70 },
        schuppe: { name: "Haarschuppe", text: "ca. 7 µm breit", um: 7 }
      },
      erzeugen: function (r) {
        var h = [
          { mx: 0, my: 0, a: 0.35, w: 72, dunkel: true },
          { mx: 700, my: 250, a: -0.95, w: 56, dunkel: false },
          { mx: -1600, my: -900, a: 1.35, w: 86, dunkel: true }
        ];
        h.forEach(function (x, i) { x.ux = Math.cos(x.a); x.uy = Math.sin(x.a); x.L = 7000; x.id = i * 1000 + 17; });
        return h;
      },
      zeichnen: zeichneHaare, ziele: zieleHaare
    },
    fluegel: {
      geraet: "licht", name: "Fliegenflügel", tropfen: "#c9d9ea", umfang: 3600, start: "haerchen",
      text: "Der Flügel einer Stubenfliege, ungefärbt. Die dünne, durchsichtige Flügelhaut wird von Adern gestützt. Bei starker Vergrößerung sieht man, dass sie mit winzigen Härchen besetzt ist. Am Rand sitzen längere Borsten.",
      typen: {
        fluegel: { name: "Fliegenflügel", text: "ca. 6,5 mm lang", um: 6500 },
        ader: { name: "Flügelader", text: "ca. 30 µm dick", um: 30 },
        haerchen: { name: "Flügelhärchen", text: "ca. 7 µm lang", um: 7 }
      },
      erzeugen: erzeugeFluegel,
      zeichnen: zeichneFluegel, ziele: zieleFluegel
    },
    biene: {
      geraet: "licht", name: "Bienenbein", tropfen: "#e0a52a", umfang: 4300, start: "pollen",
      text: "Das Hinterbein einer Honigbiene. Am Unterschenkel (Schiene) liegt das Pollenkörbchen: eine Mulde, eingerahmt von langen Haaren. Darin trägt die Biene ein Klümpchen Pollen nach Hause. Am Glied darunter sitzt die Pollenbürste.",
      typen: {
        bein: { name: "Bienenbein (Schiene)", text: "ca. 3 mm lang", um: 3000 },
        borste: { name: "Borste (Haar)", text: "ca. 0,5 mm lang", um: 500 },
        pollen: { name: "Pollenkorn", text: "ca. 35 µm", um: 35 }
      },
      erzeugen: erzeugeBiene,
      zeichnen: zeichneBiene, ziele: zieleBiene
    },
    joghurt: {
      geraet: "licht", name: "Joghurt", tropfen: "#9c8fe0", umfang: 2300, start: "lacto",
      text: "Ein Tropfen Joghurt, mit Wasser verdünnt und mit Methylenblau gefärbt. Milchsäurebakterien machen aus Milch Joghurt. Die runden Fetttröpfchen stammen aus der Milch.",
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
      geraet: "licht", name: "Darmbakterien (E. coli)", tropfen: "#e38aa8", umfang: 2300, start: "ecoli",
      text: "Escherichia coli ist ein typisches Darmbakterium mit Stäbchenform. Die Bakterien sind angefärbt. Manche sind gerade dabei, sich zu teilen.",
      typen: { ecoli: { name: "Escherichia coli (Stäbchen)", text: "ca. 2 µm lang, 0,6 µm dick", um: 2, bakterium: true } },
      erzeugen: function (r) {
        var o = [];
        stab(o, "ecoli", 0, 0, 2.1, 0.6, 0.6, F.rosa);
        for (var i = 0; i < 30000; i++) {
          var p = imKreis(r, 2400), w = r() * TAU, l = 1.5 + r();
          stab(o, "ecoli", p[0], p[1], l, 0.6, w, F.rosa);
          if (r() < 0.15) stab(o, "ecoli", p[0] + Math.cos(w) * (l + 0.15), p[1] + Math.sin(w) * (l + 0.15), l, 0.6, w, F.rosa);
        }
        return o;
      }
    },
    staph: {
      geraet: "licht", name: "Staphylokokken", tropfen: "#a07ad8", umfang: 2300, start: "staph",
      text: "Staphylokokken sind kugelförmige Bakterien, die in Haufen wie Weintrauben zusammenliegen. Manche Arten lösen Hautentzündungen aus.",
      typen: { staph: { name: "Staphylococcus (Kugeln in Trauben)", text: "ca. 1 µm", um: 1, bakterium: true } },
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
      geraet: "licht", name: "Bacillus megaterium", tropfen: "#a07ad8", umfang: 2300, start: "bacillus",
      text: "Bacillus megaterium gehört zu den größten gewöhnlichen Bakterien. Die dicken Stäbchen hängen oft in Ketten aneinander. Der Name bedeutet „großes Tier“.",
      typen: { bacillus: { name: "Bacillus megaterium (dicke Stäbchen)", text: "ca. 5 µm lang, 1,5 µm dick", um: 5, bakterium: true } },
      erzeugen: function (r) {
        var o = [];
        stabkette(o, r, "bacillus", -6, 0, 3, 4.8, 1.45, F.violett);
        for (var i = 0; i < 9000; i++) { var p = imKreis(r, 2400); stabkette(o, r, "bacillus", p[0], p[1], 1 + Math.floor(r() * 5), 4.8, 1.45, F.violett); }
        return o;
      }
    },
    thio: {
      geraet: "licht", name: "Riesenbakterium Thiomargarita", tropfen: "#d9cfa6", umfang: 2200, start: "thio",
      text: "Thiomargarita namibiensis lebt im Meeresboden vor Namibia. Die kugelförmigen Zellen hängen wie Perlen an einer Kette. Die hellen Körnchen sind Schwefel. Zum Vergleich liegen gewöhnliche Bakterien dazwischen.",
      typen: {
        thio: { name: "Thiomargarita namibiensis (Kugel)", text: "ca. 100–300 µm", um: 180, bakterium: true },
        klein: { name: "gewöhnliches Bakterium (zum Vergleich)", text: "ca. 2 µm", um: 2, bakterium: true }
      },
      erzeugen: function (r) {
        var o = [], ketten = [];
        for (var c = 0; c < 26; c++) {
          var p = c === 0 ? [-60, 0] : imKreis(r, 2100), n = 3 + Math.floor(r() * 10), w = r() * TAU, glied = [], x = p[0], y = p[1];
          for (var i = 0; i < n; i++) {
            var rad = 55 + r() * 70, kr = [];
            for (var g = 0; g < 70; g++) { var q = imKreis(r, rad * 0.88); kr.push(q[0], q[1], 2 + r() * 2.5); }
            glied.push({ x: x, y: y, r: rad });
            o.push({ k: "r", typ: "thio", x: x, y: y, r: rad, c: F.riese, koerner: kr });
            w += (r() - 0.5) * 0.7; x += Math.cos(w) * rad * 2.05; y += Math.sin(w) * rad * 2.05;
          }
          ketten.push({ k: "h", typ: "-", x: glied[0].x, y: glied[0].y, glieder: glied });
        }
        for (var b = 0; b < 25000; b++) { var s = imKreis(r, 2400); stab(o, "klein", s[0], s[1], 1.6 + r() * 0.8, 0.6, r() * TAU, F.grau); }
        return ketten.concat(o);
      }
    },

    /* =========================================================
       Präparate für das Elektronenmikroskop (Rasterelektronenmikroskop)
       ========================================================= */
    grippe: {
      geraet: "elektronen", name: "Grippeviren an einer Zelle", tropfen: "#9aa3aa", umfang: 40, start: "virus",
      text: "Zellen aus den Atemwegen, die mit Grippeviren infiziert sind. Neue Viren schnüren sich an der Zelloberfläche ab und werden freigesetzt. Die Hülle der Viren ist mit Oberflächenproteinen gespickt.",
      typen: {
        zelle: { name: "Zelle der Atemwege", text: "ca. 15 µm", um: 15 },
        virus: { name: "Grippevirus", text: "ca. 100 nm (0,1 µm)", um: 0.1 },
        spike: { name: "Oberflächenprotein (Spike)", text: "ca. 13 nm lang", um: 0.013 }
      },
      erzeugen: function (r) { return erzeugeVirenZellen(r, { n: 36, sl: 0.013, sb: 0.005, keule: false, frei: 1600, knospen: 260 }); }
    },
    corona: {
      geraet: "elektronen", name: "Coronaviren an einer Zelle", tropfen: "#9aa3aa", umfang: 40, start: "virus",
      text: "Coronaviren an der Oberfläche einer Zelle. Ihre keulenförmigen Spike-Proteine stehen ab wie die Zacken einer Krone (lateinisch: corona). Mit ihnen docken die Viren an Wirtszellen an.",
      typen: {
        zelle: { name: "Zelle der Atemwege", text: "ca. 15 µm", um: 15 },
        virus: { name: "Coronavirus", text: "ca. 100 nm (0,1 µm)", um: 0.1 },
        spike: { name: "Spike-Protein", text: "ca. 20 nm lang", um: 0.02 }
      },
      erzeugen: function (r) { return erzeugeVirenZellen(r, { n: 20, sl: 0.021, sb: 0.004, keule: true, frei: 1200, knospen: 200 }); }
    },
    phagen: {
      geraet: "elektronen", name: "Bakteriophagen an E. coli", tropfen: "#9aa3aa", umfang: 30, start: "phage",
      text: "Bakteriophagen sind Viren, die Bakterien befallen. Sie setzen sich mit ihren Schwanzfasern auf die Oberfläche eines Bakteriums und spritzen ihr Erbgut hinein. Die langen Fäden der Bakterien sind Geißeln.",
      typen: {
        bakterium: { name: "Bakterium E. coli", text: "ca. 2 µm lang", um: 2, bakterium: true },
        phage: { name: "Bakteriophage T4 (Virus)", text: "ca. 200 nm (0,2 µm)", um: 0.2 },
        geissel: { name: "Geißel", text: "ca. 20 nm dick", um: 0.02 }
      },
      erzeugen: erzeugePhagen
    },
    tmv: {
      geraet: "elektronen", name: "Tabakmosaikviren", tropfen: "#9aa3aa", umfang: 25, start: "tmv",
      text: "Das Tabakmosaikvirus befällt Pflanzen und war 1892 das erste Virus, das entdeckt wurde. Es ist ein winziges Stäbchen aus Erbgut und Eiweiß.",
      typen: { tmv: { name: "Tabakmosaikvirus", text: "ca. 300 nm lang, 18 nm dick", um: 0.3 } },
      erzeugen: function (r) {
        var o = [];
        o.push({ k: "t", typ: "tmv", x: 0, y: 0, l: 0.3, b: 0.018, w: 0.4 });
        for (var i = 0; i < 3500; i++) {
          var p = r() < 0.02 ? imKreis(r, 1.5) : imKreis(r, 25), w = r() * TAU, n = r() < 0.2 ? 2 + Math.floor(r() * 4) : 1;
          for (var k = 0; k < n; k++) o.push({ k: "t", typ: "tmv", x: p[0] + Math.cos(w + 1.57) * k * 0.02, y: p[1] + Math.sin(w + 1.57) * k * 0.02, l: r() < 0.75 ? 0.3 : 0.08 + r() * 0.2, b: 0.018, w: w + (r() - 0.5) * 0.05 });
        }
        return o;
      }
    }
  };

  /* ---------- Erzeugen: Elektronenmikroskop ---------- */
  function erzeugeVirenZellen(r, v) {
    var o = [], zellen = [];
    var mitten = [[0, 8.6], [17, 6], [-15, 10], [4, -16], [-20, -12], [24, -14], [-4, 26], [28, 22]];
    mitten.forEach(function (m, i) {
      zelle(o, r, "zelle", m[0], m[1], i === 0 ? 8 : 6.5 + r() * 2.5, F.em, "ez");
      var zl = o[o.length - 1]; zl.pts = zl.pts.map(function (p) { return 0.92 + (p - 0.82) * 0.4; }); zellen.push(zl);
    });
    function virus(x, y) { o.push({ k: "v", typ: "virus", x: x, y: y, r: 0.045 + r() * 0.015, n: v.n, sl: v.sl, sb: v.sb, keule: v.keule, w: r() * TAU, id: o.length }); }
    virus(0.02, -0.02);
    for (var i = 0; i < v.knospen; i++) {
      var zl = zellen[i % 4 === 0 ? 0 : Math.floor(r() * zellen.length)], a = i % 4 === 0 ? -Math.PI / 2 + gauss(r) * 0.5 : r() * TAU;
      var rr = zl.r * randFaktor(zl, a) + 0.03;
      virus(zl.x + Math.cos(a) * rr, zl.y + Math.sin(a) * rr);
    }
    for (var k = 0; k < v.frei; k++) { var p = r() < 0.035 ? imKreis(r, 1.3) : imKreis(r, 40); if (Math.hypot(p[0], p[1] - 8.6) < 8.3) continue; virus(p[0], p[1]); }
    return o;
  }
  function randFaktor(zl, a) {
    var n = zl.pts.length, t = ((((a - zl.w) / TAU) % 1) + 1) % 1 * n, i = Math.floor(t), f = t - i;
    return zl.pts[i % n] * (1 - f) + zl.pts[(i + 1) % n] * f;
  }

  function erzeugePhagen(r) {
    var o = [], bakt = [];
    var start = [[0.15, 0.42, 0.05], [2.6, -1.4, -0.9], [-3, -2.2, 0.5], [3.5, 3.6, 1.2], [-1.5, 4.8, -0.2]];
    for (var i = 0; i < 70; i++) {
      var p = i < start.length ? start[i] : imKreis(r, 28), w = i < start.length ? start[i][2] : r() * TAU;
      var b = { k: "eb", typ: "bakterium", x: p[0], y: p[1], l: 1.9 + r() * 0.6, b: 0.62, w: w, geisseln: [] };
      var ng = 4 + Math.floor(r() * 4);
      for (var g = 0; g < ng; g++) b.geisseln.push({ pos: (r() - 0.5) * 0.9, seite: r() < 0.5 ? -1 : 1, w: (r() - 0.5) * 1.2, l: 4 + r() * 4, ph: r() * TAU });
      bakt.push(b);
    }
    o = o.concat(bakt);
    o.push({ k: "p", typ: "phage", x: -0.02, y: 0.42 - 0.31 + 0.005, w: -Math.PI / 2 - 0.08 });
    bakt.slice(0, 14).forEach(function (b, bi) {
      var n = bi === 0 ? 14 : 5 + Math.floor(r() * 12);
      for (var k = 0; k < n; k++) {
        // Andockstelle auf der Oberfläche (Stäbchen = Rechteck mit runden Enden)
        var t = (r() - 0.5) * (b.l - b.b), seite = r() < 0.5 ? -1 : 1, ax = Math.cos(b.w), ay = Math.sin(b.w);
        var nx = -ay * seite, ny = ax * seite, x = b.x + ax * t + nx * b.b / 2, y = b.y + ay * t + ny * b.b / 2;
        o.push({ k: "p", typ: "phage", x: x, y: y, w: Math.atan2(ny, nx) + (r() - 0.5) * 0.5 });
      }
    });
    for (var f = 0; f < 700; f++) { var q = r() < 0.08 ? imKreis(r, 2.5) : imKreis(r, 28); o.push({ k: "p", typ: "phage", x: q[0], y: q[1], w: r() * TAU, frei: true }); }
    return o;
  }

  /* ---------- Erzeugen: Fliegenflügel ---------- */
  var FL = 3200;
  function flOben(x) { var u = x / FL; return Math.abs(u) >= 1 ? 0 : -1150 * Math.sqrt(1 - u * u) * (0.6 + 0.4 * (u + 1) / 2); }
  function flUnten(x) { var u = x / FL; return Math.abs(u) >= 1 ? 0 : 1350 * Math.sqrt(1 - u * u) * (0.5 + 0.5 * (u + 1) / 2); }
  function imFluegel(x, y) { return y > flOben(x) && y < flUnten(x); }
  function erzeugeFluegel() {
    var adern = [], defs = [[-0.97, 0.98, 40], [-0.62, 0.55, 32], [-0.25, 0.9, 30], [0.12, 0.97, 28], [0.48, 0.7, 26], [0.8, 0.25, 22]];
    defs.forEach(function (d) {
      var pts = [];
      for (var k = 0; k <= 40; k++) {
        var u = -0.96 + k / 40 * (d[1] + 0.96), f = Math.pow((u + 1) / (1 + d[1]), 4);
        var v = d[0] + (Math.sign(d[0]) - d[0]) * f * 0.97, x = u * FL;
        pts.push([x, v < 0 ? -v * flOben(x) : v * flUnten(x)]);
      }
      adern.push({ pts: pts, b: d[2] });
    });
    function punkt(a, u) { var x = u * FL, best = adern[a].pts[0]; adern[a].pts.forEach(function (p) { if (Math.abs(p[0] - x) < Math.abs(best[0] - x)) best = p; }); return best; }
    adern.push({ pts: [punkt(2, 0.05), punkt(3, 0.08)], b: 20 });
    adern.push({ pts: [punkt(3, 0.38), punkt(4, 0.33)], b: 20 });
    return { adern: adern };
  }

  /* ---------- Erzeugen: Bienenbein ---------- */
  function biegung(x) { return 60 * Math.sin(x / 2000); }
  var BEIN = [
    { x0: -4300, x1: -1530, h: function (x) { var t = (x + 2900) / 1400; return 330 * (1 - 0.18 * t * t); } },
    { x0: -1500, x1: 1350, h: function (x) { return 230 + (x + 1500) / 2850 * 300; } },
    { x0: 1400, x1: 3000, h: function () { return 380; } },
    { x0: 3050, x1: 3340, h: function () { return 150; } },
    { x0: 3380, x1: 3620, h: function () { return 130; } },
    { x0: 3660, x1: 3860, h: function () { return 115; } },
    { x0: 3900, x1: 4260, h: function () { return 105; } }
  ];
  var KORB = { x: -50, y: 20, rx: 960, ry: 330 };
  function erzeugeBiene(r) {
    var haare = [], pollen = [];
    function haar(bx, by, w, l, krumm, dicke, farbe, verzweigt) {
      var tx = bx + Math.cos(w) * l, ty = by + Math.sin(w) * l, mx = (bx + tx) / 2 - Math.sin(w) * l * krumm, my = (by + ty) / 2 + Math.cos(w) * l * krumm;
      haare.push({ bx: bx, by: by, mx: mx, my: my, tx: tx, ty: ty, l: l, d: dicke, f: farbe, v: verzweigt, id: haare.length });
    }
    var hell = "rgba(176,124,52,0.92)", dunkel = "rgba(66,42,16,0.95)";
    BEIN.forEach(function (sg, si) {
      for (var x = sg.x0 + 30; x < sg.x1 - 30; x += si === 1 ? 42 : si === 0 ? 70 : 85) {
        for (var s = -1; s <= 1; s += 2) {
          var by = biegung(x) + s * sg.h(x) * 0.97;
          if (si === 1) haar(x, by, s * (Math.PI / 2 - 0.5) + (r() - 0.5) * 0.3, 450 + r() * 350, -s * (0.12 + r() * 0.08), 9, hell, false);
          else if (si === 0) haar(x, by, s * (Math.PI / 2 - 0.7) + (r() - 0.5) * 0.5, 260 + r() * 160, -s * 0.08, 8, hell, true);
          else haar(x, by, s * (Math.PI / 2 - 0.6) + (r() - 0.5) * 0.4, 120 + r() * 140, -s * 0.06, 7, hell, false);
        }
      }
      if (si === 0) for (var k = 0; k < 45; k++) { var fx = sg.x0 + 150 + r() * (sg.x1 - sg.x0 - 300), fy = biegung(fx) + (r() - 0.5) * sg.h(fx) * 1.4; haar(fx, fy, (r() - 0.5) * 0.8 - 0.3, 220 + r() * 120, 0.06, 7, hell, true); }
    });
    var bt = BEIN[2];
    for (var x2 = bt.x0 + 60; x2 < bt.x1 - 80; x2 += 48) for (var y2 = -bt.h() * 0.78; y2 < bt.h() * 0.8; y2 += 46) {
      var j = hash(Math.round(x2 * 7 + y2 * 13));
      haar(x2 + (j - 0.5) * 20, biegung(x2) + y2, 0.75 + (j - 0.5) * 0.3, 110 + j * 40, 0.05, 7, dunkel, false);
    }
    for (var py = -KORB.ry; py <= KORB.ry; py += 29) for (var px = -KORB.rx; px <= KORB.rx; px += 34) {
      var ox = px + ((Math.round(py / 29) & 1) ? 17 : 0);
      if ((ox * ox) / (KORB.rx * KORB.rx) + (py * py) / (KORB.ry * KORB.ry) > 1) continue;
      pollen.push({ x: KORB.x + ox + (r() - 0.5) * 6, y: KORB.y + py + (r() - 0.5) * 6, r: 16 + r() * 3, id: pollen.length });
    }
    for (var lp = 0; lp < 160; lp++) { var lx = -4200 + r() * 8400; pollen.push({ x: lx, y: biegung(lx) + (r() - 0.5) * 1800, r: 16 + r() * 3, id: pollen.length, lose: true }); }
    return { haare: haare, pollen: pollen };
  }

  /* =========================================================
     Zustand und Zeichenfläche
     ========================================================= */
  var z = { geraet: "licht", p: "mund", obj: 2, vx: 0, vy: 0, fokus: 0, ziel: 0, beschriften: true, massstab: true, auswahl: null };
  var objekte = {};
  var feld = document.getElementById("mk-feld"), canvas = document.getElementById("mk-canvas"), ctx = canvas.getContext("2d");
  var dpr = 1, W = 0, R = 0, RC = 0, cx = 0, cy = 0, s = 1, winzig = [], rauschen = null;

  function G() { return GERAETE[z.geraet]; }
  function P() { return PRAEPARATE[z.p]; }
  function gesamt() { return G().stufen[z.obj]; }
  function sehfeldUm() { return 180000 / gesamt(); }
  function zahl(n, stellen) { return n.toLocaleString("de-DE", { maximumSignificantDigits: stellen || 2 }); }
  function laenge(mm) {
    if (mm >= 1000) return zahl(mm / 1000) + " m";
    if (mm >= 10) return zahl(mm / 10) + " cm";
    if (mm >= 0.1) return zahl(mm) + " mm";
    if (mm >= 0.001) return zahl(mm * 1000) + " µm";
    return zahl(mm * 1e6) + " nm";
  }
  function X(x) { return cx + (x - z.vx) * s; }
  function Y(y) { return cy + (y - z.vy) * s; }

  var geplant = false;
  function neuZeichnen() { if (!geplant) { geplant = true; requestAnimationFrame(function () { geplant = false; zeichne(); }); } }

  function groesse() {
    var css = feld.clientWidth;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(css * dpr); canvas.height = Math.round(css * dpr);
    W = canvas.width; cx = cy = W / 2; R = W / 2 * 0.97;
    anzeigen(); neuZeichnen();
  }
  function sichtbar(x, y, rad) { return Math.abs(x - cx) < RC + rad && Math.abs(y - cy) < RC + rad; }

  /* ---------- Objekte zeichnen ---------- */
  function zeichneObjekt(o) {
    if (o.k === "h") return zeichneHuelle(o);
    if (o.k === "v") return zeichneVirus(o);
    if (o.k === "p") return zeichnePhage(o);
    if (o.k === "eb") return zeichneEmBakterium(o);
    if (o.k === "t") return zeichneTmv(o);
    if (o.k === "ez") return zeichneEmZelle(o);
    var x = X(o.x), y = Y(o.y), gr = (o.k === "s" ? o.l / 2 : o.k === "z" ? o.r * 1.2 : o.r) * s;
    if (!sichtbar(x, y, gr + 2)) return;
    if (gr < 0.6 * dpr) { winzig.push(x, y, o.c.r); return; }
    if (o.k === "s") {
      var L = o.l * s, B = Math.max(o.b * s, 1.1 * dpr), dx = Math.cos(o.w) * (L - B) / 2, dy = Math.sin(o.w) * (L - B) / 2;
      ctx.beginPath(); ctx.moveTo(x - dx, y - dy); ctx.lineTo(x + dx, y + dy);
      ctx.strokeStyle = o.c.r; ctx.lineWidth = B; ctx.stroke();
      if (B > 3.5 * dpr) { ctx.strokeStyle = o.c.f; ctx.lineWidth = B - Math.max(1.4 * dpr, B * 0.24); ctx.stroke(); }
    } else if (o.k === "k") {
      var rr = Math.max(o.r * s, 0.6 * dpr);
      ctx.beginPath(); ctx.arc(x, y, rr, 0, TAU); ctx.fillStyle = o.c.r; ctx.fill();
      if (rr > 1.8 * dpr) { ctx.beginPath(); ctx.arc(x, y, rr - Math.max(0.8 * dpr, rr * 0.25), 0, TAU); ctx.fillStyle = o.c.f; ctx.fill(); }
      if (o.typ === "fett" && rr > 4 * dpr) { ctx.beginPath(); ctx.arc(x - rr * 0.3, y - rr * 0.3, rr * 0.25, 0, TAU); ctx.fillStyle = "rgba(255,255,255,0.9)"; ctx.fill(); }
    } else if (o.k === "z") {
      zellPfad(o, x, y);
      ctx.fillStyle = o.c.f; ctx.fill();
      ctx.strokeStyle = o.c.r; ctx.lineWidth = Math.max(0.8 * dpr, Math.min(2.2 * dpr, 0.5 * s)); ctx.stroke();
      if (o.r * s > 40 * dpr) {
        ctx.fillStyle = o.c.g;
        for (var g = 0; g < 40; g++) {
          var ga = hash(o.id * 97 + g) * TAU, gd = Math.sqrt(hash(o.id * 131 + g)) * o.r * 0.75 * s;
          ctx.beginPath(); ctx.arc(x + Math.cos(ga) * gd, y + Math.sin(ga) * gd, Math.max(0.6 * dpr, 0.5 * s), 0, TAU); ctx.fill();
        }
      }
      ctx.beginPath(); ctx.arc(x + o.kx * s, y + o.ky * s, Math.max(0.6 * dpr, o.kr * s), 0, TAU); ctx.fillStyle = o.c.k; ctx.fill();
    } else if (o.k === "r") {
      var rr2 = o.r * s;
      ctx.beginPath(); ctx.arc(x, y, rr2, 0, TAU); ctx.fillStyle = o.c.f; ctx.fill();
      ctx.strokeStyle = o.c.r; ctx.lineWidth = Math.max(0.8 * dpr, Math.min(3 * dpr, 1.5 * s)); ctx.stroke();
      if (rr2 > 10 * dpr) {
        for (var k = 0; k < o.koerner.length; k += 3) {
          var kxx = x + o.koerner[k] * s, kyy = y + o.koerner[k + 1] * s, krr = Math.max(0.7 * dpr, o.koerner[k + 2] * s);
          ctx.beginPath(); ctx.arc(kxx, kyy, krr, 0, TAU); ctx.fillStyle = "rgba(255,255,250,0.95)"; ctx.fill();
          if (krr > 2 * dpr) { ctx.strokeStyle = "rgba(110,100,70,0.75)"; ctx.lineWidth = Math.max(0.7 * dpr, krr * 0.2); ctx.stroke(); }
        }
      }
    }
  }

  function zellPfad(o, x, y) {
    var n = o.pts.length;
    ctx.beginPath();
    for (var i = 0; i <= n; i++) {
      var a = o.w + i / n * TAU, a2 = o.w + (i + 0.5) / n * TAU;
      var r1 = o.r * o.pts[i % n] * s, r2 = o.r * (o.pts[i % n] + o.pts[(i + 1) % n]) / 2 * s;
      var px = x + Math.cos(a) * r1, py = y + Math.sin(a) * r1, mx = x + Math.cos(a2) * r2, my = y + Math.sin(a2) * r2;
      if (i === 0) ctx.moveTo(mx, my); else ctx.quadraticCurveTo(px, py, mx, my);
    }
    ctx.closePath();
  }

  function zeichneHuelle(o) {
    var g = o.glieder;
    ctx.beginPath();
    for (var i = 0; i < g.length; i++) { if (i) ctx.lineTo(X(g[i].x), Y(g[i].y)); else ctx.moveTo(X(g[i].x), Y(g[i].y)); }
    if (g.length === 1) ctx.lineTo(X(g[0].x) + 0.1, Y(g[0].y));
    ctx.strokeStyle = "rgba(206,196,150,0.22)"; ctx.lineCap = "round"; ctx.lineJoin = "round";
    ctx.lineWidth = 300 * s; ctx.stroke();
  }

  /* ---------- Elektronenmikroskop: graue, plastische Darstellung ---------- */
  function kugelGrau(x, y, rr, hell) {
    var g = ctx.createRadialGradient(x - rr * 0.35, y - rr * 0.4, rr * 0.08, x, y, rr);
    g.addColorStop(0, hell ? "#f4f6f7" : "#e3e7ea"); g.addColorStop(0.65, hell ? "#aab1b6" : "#979fa5"); g.addColorStop(1, "#5d656b");
    ctx.beginPath(); ctx.arc(x, y, rr, 0, TAU); ctx.fillStyle = g; ctx.fill();
    ctx.strokeStyle = "rgba(235,240,243,0.45)"; ctx.lineWidth = Math.max(0.6 * dpr, rr * 0.06); ctx.stroke();
  }
  function zeichneVirus(o) {
    var x = X(o.x), y = Y(o.y), rr = o.r * s, aussen = (o.r + o.sl * 1.4) * s;
    if (!sichtbar(x, y, aussen + 2)) return;
    if (rr < 0.8 * dpr) { winzig.push(x, y, F.em.r); return; }
    var sl = o.sl * s;
    if (sl >= 1.2 * dpr) {
      ctx.strokeStyle = "#b7bec3"; ctx.lineWidth = Math.max(0.6 * dpr, o.sb * s); ctx.lineCap = "round";
      ctx.beginPath();
      for (var k = 0; k < o.n; k++) {
        var a = o.w + (k + hash(o.id * 7 + k) * 0.5) / o.n * TAU, c = Math.cos(a), si = Math.sin(a), l = sl * (0.85 + hash(o.id * 11 + k) * 0.3);
        ctx.moveTo(x + c * rr * 0.9, y + si * rr * 0.9); ctx.lineTo(x + c * (rr + l), y + si * (rr + l));
      }
      ctx.stroke();
      if (o.keule && sl > 3 * dpr) {
        ctx.fillStyle = "#d2d8dc";
        for (var k2 = 0; k2 < o.n; k2++) {
          var a2 = o.w + (k2 + hash(o.id * 7 + k2) * 0.5) / o.n * TAU, l2 = sl * (0.85 + hash(o.id * 11 + k2) * 0.3);
          ctx.beginPath(); ctx.arc(x + Math.cos(a2) * (rr + l2), y + Math.sin(a2) * (rr + l2), Math.max(0.8 * dpr, sl * 0.32), 0, TAU); ctx.fill();
        }
      }
    } else if (sl > 0.25 * dpr) {
      ctx.beginPath(); ctx.arc(x, y, rr + sl, 0, TAU); ctx.fillStyle = "rgba(190,197,202,0.45)"; ctx.fill();
    }
    kugelGrau(x, y, rr, false);
    if (rr > 14 * dpr) {
      ctx.fillStyle = "rgba(255,255,255,0.28)";
      for (var t = 0; t < 26; t++) {
        var ta = hash(o.id * 13 + t) * TAU, td = Math.sqrt(hash(o.id * 17 + t)) * rr * 0.82;
        ctx.beginPath(); ctx.arc(x + Math.cos(ta) * td, y + Math.sin(ta) * td, Math.max(0.8 * dpr, o.sb * s * 0.9), 0, TAU); ctx.fill();
      }
    }
  }
  function zeichnePhage(o) {
    var x = X(o.x), y = Y(o.y), L = 0.2 * s;
    if (!sichtbar(x, y, L + 0.15 * s)) return;
    if (L < 1.5 * dpr) { winzig.push(x, y, F.em.r); return; }
    var ux = Math.cos(o.w), uy = Math.sin(o.w), nx = -uy, ny = ux;
    // Schwanzfasern
    if (0.15 * s > 3 * dpr) {
      ctx.strokeStyle = "#a9b0b5"; ctx.lineWidth = Math.max(0.6 * dpr, 0.004 * s); ctx.beginPath();
      for (var f = 0; f < 6; f++) {
        var seite = f < 3 ? -1 : 1, spreiz = 0.35 + (f % 3) * 0.3;
        var kx = x + (nx * seite * Math.cos(spreiz) * 0.075 + ux * 0.04) * s, ky = y + (ny * seite * Math.cos(spreiz) * 0.075 + uy * 0.04) * s;
        var ex = kx + (nx * seite * 0.02 - ux * 0.07) * s, ey = ky + (ny * seite * 0.02 - uy * 0.07) * s;
        ctx.moveTo(x, y); ctx.lineTo(kx, ky); ctx.lineTo(ex, ey);
      }
      ctx.stroke();
    }
    // Schwanz
    var sx = x + ux * 0.1 * s, sy = y + uy * 0.1 * s;
    ctx.strokeStyle = "#8d959b"; ctx.lineCap = "butt"; ctx.lineWidth = Math.max(0.8 * dpr, 0.022 * s);
    ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(sx, sy); ctx.stroke();
    if (0.022 * s > 3 * dpr) {
      ctx.strokeStyle = "rgba(60,66,70,0.6)"; ctx.lineWidth = Math.max(0.5 * dpr, 0.003 * s); ctx.beginPath();
      for (var q = 1; q < 10; q++) { var qx = x + ux * q * 0.01 * s, qy = y + uy * q * 0.01 * s; ctx.moveTo(qx - nx * 0.011 * s, qy - ny * 0.011 * s); ctx.lineTo(qx + nx * 0.011 * s, qy + ny * 0.011 * s); }
      ctx.stroke();
    }
    ctx.lineCap = "round";
    // Kopf (gestrecktes Sechseck)
    var kx0 = x + ux * 0.155 * s, ky0 = y + uy * 0.155 * s, hl = 0.056 * s, hb = 0.043 * s;
    ctx.beginPath();
    [[-1, 0], [-0.55, 1], [0.55, 1], [1, 0], [0.55, -1], [-0.55, -1]].forEach(function (p, i) {
      var px = kx0 + ux * p[0] * hl + nx * p[1] * hb, py = ky0 + uy * p[0] * hl + ny * p[1] * hb;
      if (i) ctx.lineTo(px, py); else ctx.moveTo(px, py);
    });
    ctx.closePath();
    var g = ctx.createLinearGradient(kx0 - nx * hb, ky0 - ny * hb, kx0 + nx * hb, ky0 + ny * hb);
    g.addColorStop(0, "#e9edef"); g.addColorStop(0.5, "#b3babf"); g.addColorStop(1, "#6b7378");
    ctx.fillStyle = g; ctx.fill(); ctx.strokeStyle = "rgba(240,244,246,0.5)"; ctx.lineWidth = Math.max(0.6 * dpr, 0.004 * s); ctx.stroke();
  }
  function zeichneEmBakterium(o) {
    var x = X(o.x), y = Y(o.y), L = o.l * s, B = o.b * s, ux = Math.cos(o.w), uy = Math.sin(o.w);
    var reichweite = (o.l / 2 + 8) * s;
    if (!sichtbar(x, y, reichweite)) return;
    if (L < 1.2 * dpr) { winzig.push(x, y, F.em.r); return; }
    // Geißeln
    if (0.4 * s > 1.5 * dpr) {
      ctx.strokeStyle = "rgba(196,203,208,0.85)"; ctx.lineWidth = Math.max(0.6 * dpr, 0.02 * s); ctx.lineCap = "round";
      o.geisseln.forEach(function (g) {
        var bx = o.x + ux * g.pos * o.l / 2 - uy * g.seite * o.b / 2, by = o.y + uy * g.pos * o.l / 2 + ux * g.seite * o.b / 2;
        var dw = Math.atan2(ux * g.seite, -uy * g.seite) + g.w, dx = Math.cos(dw), dy = Math.sin(dw);
        ctx.beginPath(); ctx.moveTo(X(bx), Y(by));
        for (var t = 0.1; t <= g.l; t += 0.1) {
          var welle = Math.sin(t / 2.4 * TAU + g.ph) * 0.25 * Math.min(1, t / 0.6);
          ctx.lineTo(X(bx + dx * t - dy * welle), Y(by + dy * t + dx * welle));
        }
        ctx.stroke();
      });
    }
    var dx = ux * (L - B) / 2, dy = uy * (L - B) / 2;
    if (B < 3 * dpr) { ctx.strokeStyle = "#b9c0c5"; ctx.lineWidth = Math.max(B, dpr); ctx.beginPath(); ctx.moveTo(x - dx, y - dy); ctx.lineTo(x + dx, y + dy); ctx.stroke(); return; }
    var g2 = ctx.createLinearGradient(x + uy * B / 2, y - ux * B / 2, x - uy * B / 2, y + ux * B / 2);
    g2.addColorStop(0, "#eef1f3"); g2.addColorStop(0.45, "#aeb5ba"); g2.addColorStop(1, "#5c646a");
    ctx.lineCap = "round";
    ctx.strokeStyle = "rgba(235,240,243,0.55)"; ctx.lineWidth = B + Math.max(1 * dpr, 0.02 * s); ctx.beginPath(); ctx.moveTo(x - dx, y - dy); ctx.lineTo(x + dx, y + dy); ctx.stroke();
    ctx.strokeStyle = g2; ctx.lineWidth = B; ctx.stroke();
  }
  function zeichneTmv(o) {
    var x = X(o.x), y = Y(o.y), L = o.l * s;
    if (!sichtbar(x, y, L)) return;
    if (L < 1.5 * dpr) { winzig.push(x, y, F.em.r); return; }
    var B = Math.max(0.7 * dpr, o.b * s), dx = Math.cos(o.w) * L / 2, dy = Math.sin(o.w) * L / 2;
    ctx.lineCap = "butt"; ctx.strokeStyle = "#c3c9cd"; ctx.lineWidth = B;
    ctx.beginPath(); ctx.moveTo(x - dx, y - dy); ctx.lineTo(x + dx, y + dy); ctx.stroke();
    if (B > 4 * dpr) {
      ctx.strokeStyle = "rgba(80,86,92,0.55)"; ctx.lineWidth = Math.max(0.6 * dpr, B * 0.2); ctx.stroke();
      ctx.strokeStyle = "rgba(240,244,246,0.5)"; ctx.lineWidth = Math.max(0.5 * dpr, B * 0.12);
      var nx = -Math.sin(o.w) * B * 0.32, ny = Math.cos(o.w) * B * 0.32;
      ctx.beginPath(); ctx.moveTo(x - dx - nx, y - dy - ny); ctx.lineTo(x + dx - nx, y + dy - ny); ctx.stroke();
    }
    ctx.lineCap = "round";
  }
  function zeichneEmZelle(o) {
    var x = X(o.x), y = Y(o.y), gr = o.r * 1.15 * s;
    if (!sichtbar(x, y, gr + 0.5 * s)) return;
    zellPfad(o, x, y);
    var g = ctx.createRadialGradient(x - gr * 0.3, y - gr * 0.35, gr * 0.1, x, y, gr);
    g.addColorStop(0, "#9aa1a6"); g.addColorStop(1, "#5f676d");
    ctx.fillStyle = g; ctx.fill();
    ctx.strokeStyle = "rgba(220,226,230,0.55)"; ctx.lineWidth = Math.max(1 * dpr, 0.06 * s); ctx.stroke();
    if (0.06 * s >= 1.4 * dpr) {
      var n = Math.round(TAU * o.r / 0.16);
      ctx.lineCap = "round"; ctx.strokeStyle = "#a9b0b5"; ctx.lineWidth = 0.08 * s;
      ctx.beginPath();
      for (var i = 0; i < n; i++) {
        var a = i / n * TAU + hash(i + o.id * 1000) * 0.02, rf = o.r * randFaktor(o, a), l = 0.15 + hash(i * 3 + o.id) * 0.25;
        var bx = X(o.x + Math.cos(a) * rf), by = Y(o.y + Math.sin(a) * rf);
        if (!sichtbar(bx, by, l * s)) continue;
        var dw = a + (hash(i * 5 + o.id) - 0.5) * 0.6;
        ctx.moveTo(bx - Math.cos(dw) * 0.05 * s, by - Math.sin(dw) * 0.05 * s); ctx.lineTo(bx + Math.cos(dw) * l * s, by + Math.sin(dw) * l * s);
      }
      ctx.stroke();
    }
  }

  /* ---------- Wasserpest ---------- */
  var CW = 72, CH = 22;
  function blattrand(x) { return 620 + 40 * Math.sin(x / 380) + 18 * Math.sin(x / 97); }
  function zeichneElodea() {
    var x0 = z.vx - RC / s, x1 = z.vx + RC / s, y0 = z.vy - RC / s, y1 = z.vy + RC / s;
    var schritt = Math.max(4, 12 / s), x;
    ctx.beginPath();
    for (x = x0 - schritt; x <= x1 + schritt; x += schritt) { if (x === x0 - schritt) ctx.moveTo(X(x), Y(-blattrand(x))); else ctx.lineTo(X(x), Y(-blattrand(x))); }
    for (x = x1 + schritt; x >= x0 - schritt; x -= schritt) ctx.lineTo(X(x), Y(blattrand(x)));
    ctx.closePath(); ctx.fillStyle = "rgba(150,200,120,0.32)"; ctx.fill();
    ctx.strokeStyle = "rgba(70,120,50,0.75)"; ctx.lineWidth = Math.max(1 * dpr, 2 * s); ctx.stroke();
    if (CH * s < 1.6 * dpr) return;
    var j0 = Math.floor(Math.max(y0, -700) / CH), j1 = Math.ceil(Math.min(y1, 700) / CH);
    var wand = "rgba(70,120,50," + (CH * s < 5 * dpr ? 0.35 : 0.7) + ")", wb = Math.max(0.6 * dpr, Math.min(2 * dpr, 1.2 * s));
    var chloro = 5 * s >= 1.4 * dpr;
    for (var j = j0; j <= j1; j++) {
      var versatz = (j % 2 ? CW / 2 : 0) + (j % 3) * 7;
      var i0 = Math.floor((x0 - versatz) / CW) - 1, i1 = Math.ceil((x1 - versatz) / CW);
      for (var i = i0; i <= i1; i++) {
        var lx = i * CW + versatz, ly = j * CH, rand = blattrand(lx + CW / 2);
        if (ly < -rand || ly + CH > rand) continue;
        ctx.strokeStyle = wand; ctx.lineWidth = wb;
        ctx.strokeRect(X(lx), Y(ly), CW * s, CH * s);
        if (!chloro) continue;
        var id = (i * 7919 + j * 104729) | 0, n = 14 + Math.floor(hash(id) * 10);
        ctx.fillStyle = "rgba(48,140,52,0.88)";
        for (var c = 0; c < n; c++) {
          var t = hash(id + c * 31), seite = hash(id + c * 57), innen = 3 + hash(id + c * 13) * 4, px, py;
          if (seite < 0.42) { px = lx + 4 + t * (CW - 8); py = ly + innen; }
          else if (seite < 0.84) { px = lx + 4 + t * (CW - 8); py = ly + CH - innen; }
          else { px = seite < 0.92 ? lx + innen : lx + CW - innen; py = ly + 4 + t * (CH - 8); }
          ctx.beginPath(); ctx.ellipse(X(px), Y(py), 2.7 * s, 1.9 * s, t * 3, 0, TAU); ctx.fill();
          if (5 * s > 6 * dpr) { ctx.strokeStyle = "rgba(20,80,24,0.8)"; ctx.lineWidth = Math.max(0.6 * dpr, 0.3 * s); ctx.stroke(); }
        }
      }
    }
  }
  function zieleElodea() {
    var j = Math.floor(z.vy / CH), versatz = (j % 2 ? CW / 2 : 0) + (j % 3) * 7, i = Math.floor((z.vx - versatz) / CW);
    var lx = i * CW + versatz, ly = j * CH, liste = [];
    if (Math.abs(ly) > 600) return liste;
    liste.push({ typ: "blattzelle", x: lx + CW / 2, y: ly + CH / 2, r: CH / 2 });
    var id = (i * 7919 + j * 104729) | 0, innen = 3 + hash(id + 13) * 4;
    liste.push({ typ: "chloro", x: lx + 4 + hash(id + 31) * (CW - 8), y: hash(id + 57) < 0.42 ? ly + innen : ly + CH - innen, r: 2.5 });
    return liste;
  }

  /* ---------- Zwiebelhaut ---------- */
  var ZW = 250, ZH = 62;
  function zwGrenze(i, j) { return i * ZW + (j & 1 ? ZW / 2 : 0) + (hash(i * 7349 + j * 9157) - 0.5) * ZW * 0.35; }
  function zwKern(i, j) {
    var a = zwGrenze(i, j), b = zwGrenze(i + 1, j), id = i * 131 + j * 977;
    return { x: a + (b - a) * (0.2 + 0.6 * hash(id + 1)), y: j * ZH + ZH * (0.32 + 0.36 * hash(id + 2)), w: (hash(id + 3) - 0.5) * 0.6, id: id };
  }
  function zeichneZwiebel() {
    var x0 = z.vx - RC / s, x1 = z.vx + RC / s, y0 = z.vy - RC / s, y1 = z.vy + RC / s;
    ctx.fillStyle = "rgba(232,196,110,0.30)"; ctx.fillRect(0, 0, W, W);
    var j0 = Math.floor(y0 / ZH) - 1, j1 = Math.ceil(y1 / ZH);
    var wb = Math.max(0.8 * dpr, Math.min(3.5 * dpr, 2.5 * s));
    ctx.strokeStyle = "rgba(132,84,22," + (ZH * s < 4 * dpr ? 0.4 : 0.8) + ")"; ctx.lineWidth = wb;
    ctx.beginPath();
    for (var j = j0; j <= j1; j++) {
      ctx.moveTo(0, Y(j * ZH)); ctx.lineTo(W, Y(j * ZH));
      var i0 = Math.floor(x0 / ZW) - 2, i1 = Math.ceil(x1 / ZW) + 1;
      for (var i = i0; i <= i1; i++) { var gx = X(zwGrenze(i, j)); ctx.moveTo(gx, Y(j * ZH)); ctx.lineTo(gx + (hash(i + j * 31) - 0.5) * 6 * s, Y((j + 1) * ZH)); }
    }
    ctx.stroke();
    if (ZH * s < 3 * dpr) return;
    for (var j2 = j0; j2 <= j1; j2++) {
      for (var i2 = Math.floor(x0 / ZW) - 2; i2 <= Math.ceil(x1 / ZW) + 1; i2++) {
        var k = zwKern(i2, j2), kx = X(k.x), ky = Y(k.y), rx = 11 * s, ry = 8 * s;
        if (!sichtbar(kx, ky, rx + 2)) continue;
        ctx.beginPath(); ctx.ellipse(kx, ky, Math.max(0.8 * dpr, rx), Math.max(0.6 * dpr, ry), k.w, 0, TAU);
        ctx.fillStyle = "rgba(150,92,24,0.78)"; ctx.fill();
        if (rx > 6 * dpr) {
          ctx.strokeStyle = "rgba(96,56,12,0.9)"; ctx.lineWidth = Math.max(0.8 * dpr, 0.8 * s); ctx.stroke();
          ctx.fillStyle = "rgba(80,44,8,0.9)";
          ctx.beginPath(); ctx.arc(kx - 3 * s, ky - 1.5 * s, 1.8 * s, 0, TAU); ctx.fill();
          ctx.beginPath(); ctx.arc(kx + 3.5 * s, ky + 2 * s, 1.4 * s, 0, TAU); ctx.fill();
        }
        if (s * 1 >= 1.2 * dpr) {
          ctx.fillStyle = "rgba(170,120,40,0.35)";
          for (var g = 0; g < 30; g++) {
            var a = zwGrenze(i2, j2), b = zwGrenze(i2 + 1, j2), gx2 = a + 4 + hash(k.id * 7 + g) * (b - a - 8), gy2 = j2 * ZH + (hash(k.id * 11 + g) < 0.5 ? 4 + hash(g + k.id) * 5 : ZH - 4 - hash(g + k.id) * 5);
            ctx.beginPath(); ctx.arc(X(gx2), Y(gy2), 0.9 * s, 0, TAU); ctx.fill();
          }
        }
      }
    }
  }
  function zieleZwiebel() {
    var j = Math.floor(z.vy / ZH), i = Math.floor(z.vx / ZW) - 1;
    while (zwGrenze(i + 1, j) < z.vx) i++;
    var a = zwGrenze(i, j), b = zwGrenze(i + 1, j), k = zwKern(i, j);
    return [{ typ: "zwiebelzelle", x: (a + b) / 2 + (k.x > (a + b) / 2 ? -(b - a) * 0.22 : (b - a) * 0.22), y: j * ZH + ZH * 0.5, r: ZH / 2 }, { typ: "kern", x: k.x, y: k.y, r: 10 }];
  }

  /* ---------- Haare ---------- */
  function zeichneHaare(daten) {
    daten.forEach(function (h) {
      var ox = h.mx - h.ux * h.L, oy = h.my - h.uy * h.L, nx = -h.uy, ny = h.ux;
      var abst = (z.vx - ox) * nx + (z.vy - oy) * ny;
      if (Math.abs(abst) > RC / s + h.w) return;
      var tc = (z.vx - ox) * h.ux + (z.vy - oy) * h.uy, hr = RC / s * 1.5 + h.w;
      var t0 = Math.max(0, tc - hr), t1 = Math.min(2 * h.L, tc + hr), hw = h.w / 2;
      function P(t, q) { return [X(ox + h.ux * t + nx * q), Y(oy + h.uy * t + ny * q)]; }
      var a = P(t0, -hw), b = P(t1, -hw), c = P(t1, hw), d = P(t0, hw);
      var m1 = P((t0 + t1) / 2, -hw), m2 = P((t0 + t1) / 2, hw);
      var g = ctx.createLinearGradient(m1[0], m1[1], m2[0], m2[1]);
      if (h.dunkel) { g.addColorStop(0, "rgba(64,36,16,0.92)"); g.addColorStop(0.5, "rgba(150,98,52,0.78)"); g.addColorStop(1, "rgba(64,36,16,0.92)"); }
      else { g.addColorStop(0, "rgba(168,126,58,0.75)"); g.addColorStop(0.5, "rgba(236,208,140,0.55)"); g.addColorStop(1, "rgba(168,126,58,0.75)"); }
      ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.lineTo(c[0], c[1]); ctx.lineTo(d[0], d[1]); ctx.closePath();
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = h.dunkel ? "rgba(46,24,10,0.95)" : "rgba(130,92,36,0.85)"; ctx.lineWidth = Math.max(0.8 * dpr, Math.min(2.5 * dpr, 1.2 * s));
      ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.moveTo(c[0], c[1]); ctx.lineTo(d[0], d[1]); ctx.stroke();
      // Mark (Markkanal) in dunklen, dicken Haaren
      if (h.dunkel && h.w > 80 && h.w * 0.16 * s > 1.5 * dpr) {
        ctx.strokeStyle = "rgba(40,20,8,0.55)"; ctx.lineWidth = h.w * 0.16 * s; ctx.lineCap = "round"; ctx.beginPath();
        for (var m = Math.floor(t0 / 120); m * 120 < t1; m++) { if (hash(m + h.id) < 0.35) continue; var mm = P(m * 120 + 10, 0), me = P(m * 120 + 40 + hash(m * 3 + h.id) * 70, 0); ctx.moveTo(mm[0], mm[1]); ctx.lineTo(me[0], me[1]); }
        ctx.stroke();
      }
      // Pigmentkörnchen
      if (s >= 0.9 * dpr) {
        ctx.fillStyle = h.dunkel ? "rgba(40,20,6,0.75)" : "rgba(140,96,40,0.5)";
        for (var k = Math.floor(t0 / 3); k * 3 < t1; k++) {
          var anz = h.dunkel ? 2 : 1;
          for (var q = 0; q < anz; q++) {
            var hh = hash(k * 7 + q * 131 + h.id), p = P(k * 3 + hh * 3, (hash(k * 13 + q + h.id) - 0.5) * h.w * 0.75);
            ctx.beginPath(); ctx.ellipse(p[0], p[1], 0.9 * s, 0.4 * s, h.a, 0, TAU); ctx.fill();
          }
        }
      }
      // Schuppenränder
      if (7 * s >= 2.5 * dpr) {
        ctx.strokeStyle = h.dunkel ? "rgba(30,14,4,0.55)" : "rgba(110,76,26,0.6)"; ctx.lineWidth = Math.max(0.6 * dpr, 0.5 * s); ctx.beginPath();
        for (var n = Math.floor(t0 / 7); n * 7 < t1; n++) {
          var tb = n * 7 + hash(n + h.id) * 2;
          for (var sg = 0; sg <= 6; sg++) {
            var qv = -hw + sg / 6 * h.w, dt = (hash(n * 17 + sg + h.id) - 0.5) * 3 + Math.sin(sg / 6 * Math.PI) * 2.2;
            var pp = P(tb + dt, qv); if (sg) ctx.lineTo(pp[0], pp[1]); else ctx.moveTo(pp[0], pp[1]);
          }
        }
        ctx.stroke();
      }
    });
  }
  function zieleHaare(daten) {
    var h = daten[0], ox = h.mx - h.ux * h.L, oy = h.my - h.uy * h.L, nx = -h.uy, ny = h.ux, beste = null;
    daten.forEach(function (hh) {
      var o2x = hh.mx - hh.ux * hh.L, o2y = hh.my - hh.uy * hh.L, d = Math.abs((z.vx - o2x) * -hh.uy + (z.vy - o2y) * hh.ux);
      if (!beste || d < beste.d) beste = { d: d, h: hh };
    });
    h = beste.h; ox = h.mx - h.ux * h.L; oy = h.my - h.uy * h.L; nx = -h.uy; ny = h.ux;
    var tc = (z.vx - ox) * h.ux + (z.vy - oy) * h.uy;
    return [
      { typ: "haar", x: ox + h.ux * tc, y: oy + h.uy * tc, r: h.w / 2 },
      { typ: "schuppe", x: ox + h.ux * (tc + 12) + nx * h.w * 0.32, y: oy + h.uy * (tc + 12) + ny * h.w * 0.32, r: 3.5 }
    ];
  }

  /* ---------- Fliegenflügel ---------- */
  function zeichneFluegel(daten) {
    var x0 = z.vx - RC / s, x1 = z.vx + RC / s, y0 = z.vy - RC / s, y1 = z.vy + RC / s;
    var schritt = Math.max(6, 6 / s), x;
    // Flügelhaut
    ctx.beginPath();
    for (x = -FL; x <= FL; x += schritt) { if (x === -FL) ctx.moveTo(X(x), Y(flOben(x))); else ctx.lineTo(X(x), Y(flOben(x))); }
    for (x = FL; x >= -FL; x -= schritt) ctx.lineTo(X(x), Y(flUnten(x)));
    ctx.closePath();
    var g = ctx.createLinearGradient(X(-FL), Y(-800), X(FL), Y(800));
    g.addColorStop(0, "rgba(190,206,232,0.30)"); g.addColorStop(0.5, "rgba(214,196,234,0.30)"); g.addColorStop(1, "rgba(192,228,208,0.30)");
    ctx.fillStyle = g; ctx.fill();
    // Härchen der Flügelhaut
    if (7 * s >= 2.4 * dpr) {
      ctx.strokeStyle = "rgba(92,72,40,0.55)"; ctx.lineWidth = Math.max(0.6 * dpr, 0.8 * s); ctx.beginPath();
      var A = 13;
      for (var gy = Math.floor(y0 / A); gy * A < y1; gy++) for (var gx = Math.floor(x0 / A); gx * A < x1; gx++) {
        var id = gx * 7919 + gy * 104729, hx = gx * A + hash(id) * A, hy = gy * A + hash(id + 1) * A;
        if (!imFluegel(hx, hy)) continue;
        var w = 0.35 + hash(id + 2) * 0.5, l = 6 + hash(id + 3) * 2.5;
        ctx.moveTo(X(hx), Y(hy)); ctx.lineTo(X(hx + Math.cos(w) * l), Y(hy + Math.sin(w) * l));
      }
      ctx.stroke();
    }
    // Adern
    ctx.lineCap = "round"; ctx.lineJoin = "round";
    daten.adern.forEach(function (a) {
      ctx.beginPath(); a.pts.forEach(function (p, i) { if (i) ctx.lineTo(X(p[0]), Y(p[1])); else ctx.moveTo(X(p[0]), Y(p[1])); });
      ctx.strokeStyle = "rgba(104,72,34,0.88)"; ctx.lineWidth = Math.max(1 * dpr, a.b * s); ctx.stroke();
      if (a.b * s > 6 * dpr) { ctx.strokeStyle = "rgba(176,140,84,0.75)"; ctx.lineWidth = a.b * s * 0.45; ctx.stroke(); }
    });
    // Rand mit Borsten
    ctx.beginPath();
    for (x = -FL; x <= FL; x += schritt) { if (x === -FL) ctx.moveTo(X(x), Y(flUnten(x))); else ctx.lineTo(X(x), Y(flUnten(x))); }
    ctx.strokeStyle = "rgba(104,72,34,0.75)"; ctx.lineWidth = Math.max(1 * dpr, 8 * s); ctx.stroke();
    if (50 * s >= 4 * dpr) {
      ctx.strokeStyle = "rgba(92,66,32,0.8)"; ctx.lineWidth = Math.max(0.6 * dpr, 2 * s); ctx.beginPath();
      for (var bx = Math.max(-FL + 30, x0 - 100); bx < Math.min(FL - 10, x1 + 100); bx += 22) {
        [flOben, flUnten].forEach(function (f, fi) {
          var by = f(bx), dy = (f(bx + 3) - f(bx - 3)) / 6, n = Math.hypot(1, dy), nxx = -dy / n * (fi ? 1 : -1), nyy = 1 / n * (fi ? 1 : -1);
          var l = (fi ? 60 : 35) + hash(Math.round(bx) * 3 + fi) * 40, w = 0.45;
          var ex = bx + (nxx * Math.cos(w) + 1 * Math.sin(w) / n) * l, ey = by + nyy * l * 0.9;
          if (!sichtbar(X(bx), Y(by), l * s)) return;
          ctx.moveTo(X(bx), Y(by)); ctx.lineTo(X(ex), Y(ey));
        });
      }
      ctx.stroke();
    }
  }
  function zieleFluegel(daten) {
    var liste = [], beste = null;
    if (imFluegel(z.vx, z.vy)) liste.push({ typ: "fluegel", x: z.vx + 4, y: z.vy + 4, r: 60 });
    daten.adern.forEach(function (a) { a.pts.forEach(function (p) { var d = Math.hypot(p[0] - z.vx, p[1] - z.vy); if (!beste || d < beste.d) beste = { d: d, p: p, b: a.b }; }); });
    if (beste) liste.push({ typ: "ader", x: beste.p[0], y: beste.p[1], r: beste.b / 2 });
    var A = 13, bh = null;
    for (var gy = Math.floor(z.vy / A) - 2; gy <= Math.floor(z.vy / A) + 2; gy++) for (var gx = Math.floor(z.vx / A) - 2; gx <= Math.floor(z.vx / A) + 2; gx++) {
      var id = gx * 7919 + gy * 104729, hx = gx * A + hash(id) * A, hy = gy * A + hash(id + 1) * A;
      if (!imFluegel(hx, hy)) continue;
      var d = Math.hypot(hx - z.vx - 25, hy - z.vy + 25);
      if (!bh || d < bh.d) bh = { d: d, x: hx + Math.cos(0.6) * 3.5, y: hy + Math.sin(0.6) * 3.5 };
    }
    if (bh) liste.push({ typ: "haerchen", x: bh.x, y: bh.y, r: 3.5 });
    return liste;
  }

  /* ---------- Bienenbein ---------- */
  function zeichneBiene(daten) {
    var x0 = z.vx - RC / s, x1 = z.vx + RC / s;
    // Glieder
    BEIN.forEach(function (sg) {
      if (sg.x1 < x0 - 200 || sg.x0 > x1 + 200) return;
      var schritt = Math.max(8, (sg.x1 - sg.x0) / 60), x, ende = 0.35;
      ctx.beginPath();
      for (x = sg.x0; x <= sg.x1; x += schritt) {
        var e = Math.min(1, Math.min(x - sg.x0, sg.x1 - x) / (sg.h(x) * ende)), k = Math.sqrt(Math.max(0, 1 - (1 - e) * (1 - e)));
        if (x === sg.x0) ctx.moveTo(X(x), Y(biegung(x) - sg.h(x) * k)); else ctx.lineTo(X(x), Y(biegung(x) - sg.h(x) * k));
      }
      for (x = sg.x1; x >= sg.x0; x -= schritt) {
        var e2 = Math.min(1, Math.min(x - sg.x0, sg.x1 - x) / (sg.h(x) * ende)), k2 = Math.sqrt(Math.max(0, 1 - (1 - e2) * (1 - e2)));
        ctx.lineTo(X(x), Y(biegung(x) + sg.h(x) * k2));
      }
      ctx.closePath();
      var mx = (sg.x0 + sg.x1) / 2, g = ctx.createLinearGradient(X(mx), Y(biegung(mx) - sg.h(mx)), X(mx), Y(biegung(mx) + sg.h(mx)));
      g.addColorStop(0, "rgba(54,34,12,0.96)"); g.addColorStop(0.5, "rgba(140,94,38,0.92)"); g.addColorStop(1, "rgba(54,34,12,0.96)");
      ctx.fillStyle = g; ctx.fill();
      ctx.strokeStyle = "rgba(34,20,6,0.95)"; ctx.lineWidth = Math.max(1 * dpr, Math.min(3 * dpr, 4 * s)); ctx.stroke();
    });
    // Krallen
    var kx = 4260, ky = biegung(kx);
    ctx.strokeStyle = "rgba(34,20,6,0.95)"; ctx.lineWidth = Math.max(1.2 * dpr, 30 * s); ctx.lineCap = "round";
    ctx.beginPath(); ctx.moveTo(X(kx - 20), Y(ky - 40)); ctx.quadraticCurveTo(X(kx + 200), Y(ky - 150), X(kx + 220), Y(ky - 20));
    ctx.moveTo(X(kx - 20), Y(ky + 40)); ctx.quadraticCurveTo(X(kx + 200), Y(ky + 150), X(kx + 220), Y(ky + 20)); ctx.stroke();
    // Pollenhöschen
    var pr = 17 * s;
    if (pr < 1.5 * dpr) {
      ctx.beginPath(); ctx.ellipse(X(KORB.x), Y(KORB.y), KORB.rx * s, KORB.ry * s, 0, 0, TAU); ctx.fillStyle = "rgba(232,164,32,0.95)"; ctx.fill();
    }
    daten.pollen.forEach(function (p) {
      if (pr < 1.5 * dpr && !p.lose) return;
      var x = X(p.x), y = Y(p.y), rr = Math.max(0.7 * dpr, p.r * s);
      if (!sichtbar(x, y, rr + 2)) return;
      ctx.beginPath(); ctx.arc(x, y, rr, 0, TAU); ctx.fillStyle = "rgba(240,180,40,0.97)"; ctx.fill();
      if (rr > 2.5 * dpr) { ctx.strokeStyle = "rgba(150,92,8,0.95)"; ctx.lineWidth = Math.max(0.7 * dpr, 1.6 * s); ctx.stroke(); }
      if (rr > 7 * dpr) {
        ctx.fillStyle = "rgba(150,92,8,0.9)";
        for (var k = 0; k < 14; k++) { var a = k / 14 * TAU + hash(p.id) ; ctx.beginPath(); ctx.arc(x + Math.cos(a) * rr * 1.04, y + Math.sin(a) * rr * 1.04, Math.max(0.6 * dpr, 1.3 * s), 0, TAU); ctx.fill(); }
        ctx.fillStyle = "rgba(255,240,180,0.7)"; ctx.beginPath(); ctx.arc(x - rr * 0.3, y - rr * 0.3, rr * 0.28, 0, TAU); ctx.fill();
      }
    });
    // Haare
    ctx.lineCap = "round";
    daten.haare.forEach(function (h) {
      var bx = X(h.bx), by = Y(h.by), tx = X(h.tx), ty = Y(h.ty);
      if (h.l * s < 2 * dpr) return;
      if (!sichtbar((bx + tx) / 2, (by + ty) / 2, h.l * s * 0.6)) return;
      ctx.strokeStyle = h.f; ctx.lineWidth = Math.max(0.6 * dpr, h.d * s);
      ctx.beginPath(); ctx.moveTo(bx, by); ctx.quadraticCurveTo(X(h.mx), Y(h.my), tx, ty); ctx.stroke();
      if (h.v && 25 * s >= 3 * dpr) {
        ctx.lineWidth = Math.max(0.5 * dpr, h.d * 0.45 * s); ctx.beginPath();
        for (var t = 0.15; t < 0.95; t += 30 / h.l) {
          var ax = (1 - t) * (1 - t) * h.bx + 2 * (1 - t) * t * h.mx + t * t * h.tx, ay = (1 - t) * (1 - t) * h.by + 2 * (1 - t) * t * h.my + t * t * h.ty;
          var dx = 2 * (1 - t) * (h.mx - h.bx) + 2 * t * (h.tx - h.mx), dy = 2 * (1 - t) * (h.my - h.by) + 2 * t * (h.ty - h.my), w = Math.atan2(dy, dx);
          var seite = Math.round(t * h.l / 30) % 2 ? 0.8 : -0.8;
          ctx.moveTo(X(ax), Y(ay)); ctx.lineTo(X(ax + Math.cos(w + seite) * 26), Y(ay + Math.sin(w + seite) * 26));
        }
        ctx.stroke();
      }
    });
  }
  function zieleBiene(daten) {
    var liste = [], bp = null, bh = null;
    liste.push({ typ: "bein", x: Math.max(-1350, Math.min(1250, z.vx)), y: biegung(z.vx) - 160, r: 90 });
    daten.pollen.forEach(function (p) { var d = Math.hypot(p.x - z.vx - 30, p.y - z.vy - 30); if (!bp || d < bp.d) bp = { d: d, p: p }; });
    if (bp) liste.push({ typ: "pollen", x: bp.p.x, y: bp.p.y, r: bp.p.r });
    daten.haare.forEach(function (h) { var d = Math.hypot(h.mx - z.vx, h.my - z.vy); if (!bh || d < bh.d) bh = { d: d, h: h }; });
    if (bh) liste.push({ typ: "borste", x: bh.h.mx, y: bh.h.my, r: bh.h.d });
    return liste;
  }

  /* ---------- Beschriftungen ---------- */
  function beschriftungsziele() {
    var p = P();
    if (p.ziele) return p.ziele(objekte[z.p]);
    var beste = {}, liste = objekte[z.p];
    function pruefe(typ, x, y, r) {
      if (!p.typen[typ]) return;
      var d = (x - z.vx) * (x - z.vx) + (y - z.vy) * (y - z.vy);
      if (!beste[typ] || d < beste[typ].d) beste[typ] = { d: d, x: x, y: y, r: r };
    }
    for (var i = 0; i < liste.length; i++) {
      var o = liste[i];
      if (o.k === "s") pruefe(o.typ, o.x, o.y, o.l / 2);
      else if (o.k === "z" || o.k === "ez") { pruefe(o.typ, o.x + Math.cos(o.w + 0.3) * o.r * 0.55, o.y + Math.sin(o.w + 0.3) * o.r * 0.55, o.r * 0.4); pruefe("kern", o.x + o.kx, o.y + o.ky, o.kr); }
      else if (o.k === "v") { pruefe("virus", o.x, o.y, o.r); }
      else if (o.k === "p") pruefe("phage", o.x + Math.cos(o.w) * 0.155, o.y + Math.sin(o.w) * 0.155, 0.05);
      else if (o.k === "eb") pruefe("bakterium", o.x, o.y, o.b / 2);
      else if (o.k === "t") pruefe("tmv", o.x, o.y, o.l / 2);
      else if (o.k !== "h") pruefe(o.typ, o.x, o.y, o.r);
    }
    if (beste.virus && p.typen.spike) {
      var v = liste.filter(function (o) { return o.k === "v"; }).reduce(function (a, b) { return Math.hypot(b.x - z.vx, b.y - z.vy) < Math.hypot(a.x - z.vx, a.y - z.vy) ? b : a; });
      beste.spike = { x: v.x + Math.cos(-2.3) * (v.r + v.sl * 0.6), y: v.y + Math.sin(-2.3) * (v.r + v.sl * 0.6), r: v.sl / 2 };
    }
    if (beste.bakterium && p.typen.geissel) {
      var b = liste.filter(function (o) { return o.k === "eb"; }).reduce(function (a, c) { return Math.hypot(c.x - z.vx, c.y - z.vy) < Math.hypot(a.x - z.vx, a.y - z.vy) ? c : a; });
      var gg = b.geisseln[0], ux = Math.cos(b.w), uy = Math.sin(b.w);
      var gbx = b.x + ux * gg.pos * b.l / 2 - uy * gg.seite * b.b / 2, gby = b.y + uy * gg.pos * b.l / 2 + ux * gg.seite * b.b / 2;
      var dw = Math.atan2(ux * gg.seite, -uy * gg.seite) + gg.w, t = 1.2, welle = Math.sin(t / 2.4 * TAU + gg.ph) * 0.25;
      beste.geissel = { x: gbx + Math.cos(dw) * t - Math.sin(dw) * welle, y: gby + Math.sin(dw) * t + Math.cos(dw) * welle, r: 0.01 };
    }
    return Object.keys(beste).map(function (t) { var e = beste[t]; return { typ: t, x: e.x, y: e.y, r: e.r }; });
  }
  function kurzname(t) { return P().typen[t].name.replace(/\s*\(.*\)/, ""); }

  function zeichneBeschriftungen() {
    var ziele = beschriftungsziele(), belegt = [], css = dpr, grenze = z.geraet === "licht" ? R * 0.88 : W * 0.46;
    ctx.font = "700 " + Math.round(21 * css) + "px Caveat, cursive"; ctx.lineJoin = "round";
    ziele.forEach(function (zl, idx) {
      var x = X(zl.x), y = Y(zl.y), rad = zl.r * s;
      var mindest = zl.typ === "spike" || zl.typ === "geissel" || zl.typ === "schuppe" || zl.typ === "haerchen" ? 3 : 4;
      if (Math.max(rad * 2, zl.typ === "geissel" ? 0.4 * s : 0) < mindest * css) return;
      if (Math.hypot(x - cx, y - cy) > grenze * 0.92) return;
      var basis = Math.atan2(y - cy, x - cx);
      if (Math.hypot(x - cx, y - cy) < 20 * css) basis = -0.8 + idx * 2.1;
      var text = kurzname(zl.typ), tw = ctx.measureText(text).width, gesetzt = null;
      for (var v = 0; v < 10 && !gesetzt; v++) {
        var w = basis + [0, 0.7, -0.7, 1.4, -1.4, 2.2, -2.2, 3.1, 2.7, -2.7][v];
        var abst = Math.min(rad, 60 * css) + 38 * css, lx = x + Math.cos(w) * abst, ly = y + Math.sin(w) * abst;
        if (z.geraet === "licht" && Math.hypot(lx - cx, ly - cy) > grenze) continue;
        var links = Math.cos(w) < 0, bx = links ? lx - tw - 6 * css : lx + 6 * css, box = [bx, ly - 14 * css, tw, 22 * css];
        if (bx < cx - grenze * 1.05 || bx + tw > cx + grenze * 1.05 || ly < 16 * css || ly > W - 50 * css) continue;
        var frei = belegt.every(function (b) { return box[0] > b[0] + b[2] + 6 || box[0] + box[2] + 6 < b[0] || box[1] > b[1] + b[3] || box[1] + box[3] < b[1]; });
        if (frei) gesetzt = { w: w, lx: lx, ly: ly, bx: bx, box: box };
      }
      if (!gesetzt) return;
      belegt.push(gesetzt.box);
      var ra = Math.min(rad, 60 * css), sx = x + Math.cos(gesetzt.w) * (rad > 60 * css ? 0 : ra + 2 * css), sy = y + Math.sin(gesetzt.w) * (rad > 60 * css ? 0 : ra + 2 * css);
      ctx.beginPath(); ctx.moveTo(sx, sy); ctx.lineTo(gesetzt.lx, gesetzt.ly);
      ctx.strokeStyle = "rgba(255,255,255,0.9)"; ctx.lineWidth = 4.5 * css; ctx.stroke();
      ctx.strokeStyle = "#1f2a36"; ctx.lineWidth = 1.8 * css; ctx.stroke();
      ctx.beginPath(); ctx.arc(sx, sy, 2.4 * css, 0, TAU); ctx.fillStyle = "#1f2a36"; ctx.fill();
      ctx.textBaseline = "middle"; ctx.textAlign = "left";
      ctx.strokeStyle = "rgba(255,255,255,0.95)"; ctx.lineWidth = 5 * css; ctx.strokeText(text, gesetzt.bx, gesetzt.ly);
      ctx.fillStyle = "#1f2a36"; ctx.fillText(text, gesetzt.bx, gesetzt.ly);
    });
  }

  function massstabWert() {
    var ziel = 0.3 * 0.97 * W / s, werte = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000], l = werte[0];
    werte.forEach(function (w) { if (w <= ziel) l = w; });
    return { l: l, text: l >= 1000 ? zahl(l / 1000) + " mm" : l < 1 ? zahl(l * 1000) + " nm" : zahl(l) + " µm" };
  }
  function zeichneMassstab() {
    var m = massstabWert(), px = m.l * s, x0 = cx - px / 2, y0 = cy + R * 0.76, css = dpr;
    ctx.lineCap = "butt";
    ctx.fillStyle = "rgba(255,255,255,0.88)"; ctx.fillRect(x0 - 8 * css, y0 - 30 * css, px + 16 * css, 42 * css);
    ctx.fillStyle = "#1f2a36"; ctx.fillRect(x0, y0, px, 5 * css);
    ctx.fillRect(x0, y0 - 5 * css, 2 * css, 15 * css); ctx.fillRect(x0 + px - 2 * css, y0 - 5 * css, 2 * css, 15 * css);
    ctx.font = "700 " + Math.round(20 * css) + "px Caveat, cursive"; ctx.textAlign = "center"; ctx.textBaseline = "alphabetic";
    ctx.fillText(m.text, cx, y0 - 9 * css);
  }
  function zeichneDatenleiste() {
    var css = dpr, h = 34 * css, y0 = W - h;
    ctx.fillStyle = "rgba(8,10,12,0.88)"; ctx.fillRect(0, y0, W, h);
    ctx.fillStyle = "#e8edf0"; ctx.font = "700 " + Math.round(13 * css) + "px 'Atkinson Hyperlegible', sans-serif"; ctx.textBaseline = "middle"; ctx.textAlign = "left";
    ctx.fillText("REM   10 kV   " + zahl(gesamt(), 6) + "×", 12 * css, y0 + h / 2);
    if (!z.massstab) return;
    var m = massstabWert(), px = m.l * s, xe = W - 14 * css;
    ctx.fillRect(xe - px, y0 + h / 2 + 4 * css, px, 3 * css);
    ctx.textAlign = "right"; ctx.fillText(m.text, xe - px - 8 * css, y0 + h / 2 + 2 * css);
  }

  function zeichne() {
    if (!W) return;
    var p = P(), em = z.geraet === "elektronen";
    s = 0.97 * W / sehfeldUm(); RC = em ? W * 0.72 : R;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    var hg = ctx.createRadialGradient(cx, cy, 0, cx, cy, em ? W * 0.75 : R);
    if (em) { hg.addColorStop(0, "#3a4045"); hg.addColorStop(1, "#1a1e21"); }
    else { hg.addColorStop(0, "#fffef8"); hg.addColorStop(1, "#f3efe0"); }
    ctx.fillStyle = hg; ctx.fillRect(0, 0, W, W);
    ctx.save();
    if (!em) { ctx.beginPath(); ctx.arc(cx, cy, R, 0, TAU); ctx.clip(); }
    ctx.lineCap = "round";
    winzig = [];
    if (p.zeichnen) p.zeichnen(objekte[z.p]);
    else { var liste = objekte[z.p]; for (var i = 0; i < liste.length; i++) zeichneObjekt(liste[i]); }
    ctx.globalAlpha = em ? 0.55 : 0.35; var farbe = null;
    for (var w = 0; w < winzig.length; w += 3) { if (winzig[w + 2] !== farbe) { farbe = winzig[w + 2]; ctx.fillStyle = farbe; } ctx.fillRect(winzig[w], winzig[w + 1], dpr, dpr); }
    ctx.globalAlpha = 1; winzig = [];
    if (em) {
      if (!rauschen) { var rc = document.createElement("canvas"); rc.width = rc.height = 128; var rx = rc.getContext("2d"), d = rx.createImageData(128, 128); for (var k = 0; k < d.data.length; k += 4) { var v = Math.random() * 255; d.data[k] = d.data[k + 1] = d.data[k + 2] = v; d.data[k + 3] = 255; } rx.putImageData(d, 0, 0); rauschen = ctx.createPattern(rc, "repeat"); }
      ctx.globalAlpha = 0.07; ctx.fillStyle = rauschen; ctx.fillRect(0, 0, W, W); ctx.globalAlpha = 1;
    }
    if (z.beschriften) zeichneBeschriftungen();
    if (em) zeichneDatenleiste(); else if (z.massstab) zeichneMassstab();
    ctx.restore();
    var unschaerfe = Math.abs(z.fokus - z.ziel) * (0.7 + z.obj * 0.25);
    canvas.style.filter = unschaerfe > 0 ? "blur(" + unschaerfe.toFixed(1) + "px)" : "none";
  }

  /* =========================================================
     Anzeige
     ========================================================= */
  var el = {
    gesamt: document.getElementById("mk-gesamt"), rechnung: document.getElementById("mk-rechnung"),
    sehfeld: document.getElementById("mk-sehfeld"), sehfeldName: document.getElementById("mk-sehfeld-name"),
    hinweis: document.getElementById("mk-hinweis"), erkennbar: document.getElementById("mk-erkennbar"), text: document.getElementById("mk-text"),
    liste: document.getElementById("mk-liste"), leiter: document.getElementById("mk-leiter"), leitertext: document.getElementById("mk-leitertext"),
    fein: document.getElementById("mk-feintrieb"), praep: document.getElementById("mk-praeparate"), stufen: document.getElementById("mk-stufen"),
    stufenLegende: document.getElementById("mk-stufen-legende"), stufenNotiz: document.getElementById("mk-stufen-notiz")
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
    if (mm < 1500) return "etwa wie ein Tisch";
    if (mm < 5000) return "etwa wie ein Klassenraum hoch ist";
    return "größer als ein Haus";
  }
  function erkennbarText() {
    var p = P(), ja = [], nein = [], css = feld.clientWidth * 0.97 / sehfeldUm();
    Object.keys(p.typen).forEach(function (t) { (p.typen[t].um * css >= 3 ? ja : nein).push(kurzname(t)); });
    var txt = "";
    if (ja.length) txt += "Erkennbar: " + ja.join(", ") + ". ";
    if (nein.length) txt += "Noch zu klein: " + nein.join(", ") + ".";
    return txt;
  }

  function knoepfeBauen() {
    var g = G(), html = "";
    Object.keys(PRAEPARATE).forEach(function (k) { if (PRAEPARATE[k].geraet === z.geraet) html += '<button type="button" data-praeparat="' + k + '" aria-pressed="false">' + PRAEPARATE[k].name + "</button>"; });
    el.praep.innerHTML = html;
    html = "";
    g.knopf.forEach(function (t, i) { html += '<button type="button" data-objektiv="' + i + '" aria-pressed="false">' + (g.ringe ? '<span class="mk-ring" style="--ring:' + g.ringe[i] + '" aria-hidden="true"></span>' : "") + t + "</button>"; });
    el.stufen.innerHTML = html;
    el.stufenLegende.textContent = g.legende;
    el.stufenNotiz.textContent = g.notiz;
    var em = z.geraet === "elektronen";
    feld.classList.toggle("em", em);
    document.getElementById("mk-svg-licht").style.display = em ? "none" : "";
    document.getElementById("mk-svg-em").style.display = em ? "" : "none";
    document.querySelectorAll("#mk [data-geraet]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-geraet") === z.geraet ? "true" : "false"); });
  }

  function anzeigen() {
    var p = P(), m = gesamt(), em = z.geraet === "elektronen";
    el.gesamt.textContent = zahl(m, 6) + "×";
    el.rechnung.textContent = em ? "eingestellt mit den Magnetlinsen" : "10 (Okular) × " + (m / 10) + " (Objektiv) = " + zahl(m, 4) + "-fach";
    el.sehfeldName.textContent = em ? "Breite des Bildausschnitts" : "Durchmesser des Sehfelds";
    el.sehfeld.textContent = laenge(sehfeldUm() / 1000);
    var h = [];
    if (!em && m === 1000) h.push("Für das 100er-Objektiv gibt man einen Tropfen Immersionsöl auf das Deckglas.");
    if (z.fokus !== z.ziel) h.push("Das Bild ist unscharf. Stelle es mit dem Feintrieb scharf.");
    el.hinweis.textContent = h.join(" "); el.hinweis.hidden = !h.length;
    el.erkennbar.textContent = erkennbarText();
    el.text.textContent = p.text;
    canvas.setAttribute("aria-label", "Blick durch das " + G().name + ": " + p.name + " bei " + zahl(m, 6) + "-facher Vergrößerung. " + erkennbarText());
    document.querySelectorAll("#mk [data-praeparat]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-praeparat") === z.p ? "true" : "false"); });
    document.querySelectorAll("#mk [data-objektiv]").forEach(function (b) { b.setAttribute("aria-pressed", +b.getAttribute("data-objektiv") === z.obj ? "true" : "false"); });
    var rev = document.getElementById("mk-revolver"); if (rev && !em) rev.style.transform = "rotate(" + (-z.obj * 32) + "deg)";
    var tr = document.getElementById("mk-tropfen"); if (tr) tr.setAttribute("fill", p.tropfen);
    var fm = document.getElementById("mk-feinmarke"); if (fm) fm.style.transform = "rotate(" + (z.fokus * 18) + "deg)";
    var ti = document.getElementById("mk-tisch"); if (ti) ti.style.transform = "translateY(" + (z.fokus * -0.5) + "px)";
    document.querySelectorAll("#mk-revolver [data-obj]").forEach(function (g) { g.classList.toggle("aktiv", +g.getAttribute("data-obj") === z.obj); });
    listeAnzeigen(); leiterAnzeigen();
  }

  function alleTypen() {
    var p = P(), t = Object.keys(p.typen).map(function (k) { return { key: k, d: p.typen[k] }; });
    if (z.geraet === "licht") t.push({ key: "virus", d: VIRUS });
    return t;
  }
  function listeAnzeigen() {
    var m = gesamt(), html = "";
    alleTypen().forEach(function (t) {
      var mm = t.d.um / 1000 * m;
      html += '<li><button type="button" data-typ="' + t.key + '" aria-pressed="' + (z.auswahl === t.key) + '">' +
        '<span class="mk-name">' + t.d.name + '</span><span class="mk-wirklich">wirklich ' + t.d.text + '</span>' +
        '<span class="mk-schein">erscheint ' + laenge(mm) + " groß, " + (t.d.virus ? "bleibt im Lichtmikroskop aber unsichtbar" : vergleich(mm)) + "</span></button></li>";
    });
    el.liste.innerHTML = html;
  }
  function leiterAnzeigen() {
    var t = alleTypen().filter(function (x) { return x.key === z.auswahl; })[0] || alleTypen()[0];
    var mmEcht = t.d.um / 1000, L = 24, Rr = 676, MIN = G().min, MAX = 3, achse = 120;
    function XL(mm) { return L + (Math.log10(mm) - MIN) / (MAX - MIN) * (Rr - L); }
    var svg = '<svg class="ill" viewBox="0 0 700 210" role="img" aria-labelledby="mk-leiter-t"><title id="mk-leiter-t">Größenleiter: So groß erscheint ' + t.d.name + " ohne Mikroskop und bei verschiedenen Vergrößerungen</title>";
    svg += '<rect class="f-rosa-weich" x="' + L + '" y="34" width="' + (XL(0.1) - L) + '" height="' + (achse - 34) + '" rx="10"/>';
    svg += '<text class="hk" x="' + (L + 12) + '" y="80">für das Auge</text><text class="hk" x="' + (L + 12) + '" y="100">zu klein</text>';
    [[0.07, "Haar (Dicke)", 1], [1, "Sandkorn", 0], [6, "Reiskorn", 1], [23, "1-Euro-Münze", 0], [150, "Handy", 1]].forEach(function (r) {
      var x = XL(r[0]), y = r[2] ? 52 : 92;
      svg += '<line class="s2" x1="' + x + '" y1="' + (y + 8) + '" x2="' + x + '" y2="' + achse + '" stroke-dasharray="2 5"/><text class="hk" x="' + x + '" y="' + y + '" text-anchor="middle">' + r[1] + "</text>";
    });
    svg += '<line class="s" x1="' + L + '" y1="' + achse + '" x2="' + Rr + '" y2="' + achse + '"/>';
    for (var e = MIN; e <= MAX; e++) {
      var mm = Math.pow(10, e), x = XL(mm);
      svg += '<line class="s2" x1="' + x + '" y1="' + (achse - 5) + '" x2="' + x + '" y2="' + (achse + 5) + '"/><text class="hk" x="' + x + '" y="' + (achse + 24) + '" text-anchor="middle" style="font-size:15px">' + laenge(mm) + "</text>";
    }
    G().vergleich.forEach(function (m, i) {
      var mm2 = mmEcht * m, x2 = XL(mm2), aktiv = m === gesamt(), raus = mm2 < Math.pow(10, MIN), y = achse + 52;
      if (raus) x2 = L;
      svg += '<line class="s2" x1="' + x2 + '" y1="' + (achse + 30) + '" x2="' + x2 + '" y2="' + (y - 9) + '"/>';
      svg += '<circle class="s ' + (aktiv ? "f-blau-tief" : "f-weiss") + '" cx="' + x2 + '" cy="' + y + '" r="' + (aktiv ? 9 : 6) + '"/>';
      var lab = m === 1 ? "ohne Mikroskop" : zahl(m, 6) + "×";
      svg += '<text class="' + (aktiv ? "h" : "hk") + '" x="' + x2 + '" y="' + (y + (i % 2 ? 26 : 30)) + '" text-anchor="' + (x2 < 70 ? "start" : x2 > 640 ? "end" : "middle") + '">' + (raus ? "◂ " : "") + lab + "</text>";
    });
    svg += "</svg>";
    el.leiter.innerHTML = svg;
    var jetzt = mmEcht * gesamt(), echt = t.d.text.replace("ca. ", "etwa ");
    if (!/lang|dick|breit/.test(echt)) echt += " groß";
    var satz = t.d.name.replace(/\s*\(.*\)/, "") + ": in Wirklichkeit " + echt + " (" + zahl(mmEcht, 2) + " mm). Bei " + zahl(gesamt(), 6) + "-facher Vergrößerung wirkt das " + laenge(jetzt) + " groß";
    if (t.d.virus) satz += ". Trotzdem sieht man Viren im Lichtmikroskop nicht: Alles, was kleiner als etwa 0,2 µm ist, kann ein Lichtmikroskop nicht mehr auflösen. Wechsle zum Elektronenmikroskop, um Viren zu sehen.";
    else satz += ", " + vergleich(jetzt) + ".";
    el.leitertext.textContent = satz;
  }

  /* =========================================================
     Bedienung
     ========================================================= */
  function praeparatWaehlen(key) {
    z.p = key; z.vx = 0; z.vy = 0;
    if (!objekte[key]) objekte[key] = PRAEPARATE[key].erzeugen(rng(key.length * 7919 + key.charCodeAt(0)));
    z.auswahl = PRAEPARATE[key].start;
    anzeigen(); neuZeichnen();
  }
  function geraetWaehlen(g) {
    if (g === z.geraet) return;
    z.geraet = g; z.obj = GERAETE[g].startStufe; z.fokus = 0; z.ziel = 0; el.fein.value = 0;
    knoepfeBauen(); praeparatWaehlen(GERAETE[g].start);
  }
  function objektivWaehlen(i) {
    if (i === z.obj) return;
    z.obj = i;
    var neu = Math.round((Math.random() - 0.5) * 6);
    z.ziel = neu === z.fokus ? z.fokus + (z.fokus < 3 ? 2 : -2) : neu;
    anzeigen(); neuZeichnen();
  }

  app.addEventListener("click", function (e) {
    var b = e.target.closest("[data-geraet], [data-praeparat], [data-objektiv], [data-typ], [data-obj]");
    if (!b) return;
    if (b.hasAttribute("data-geraet")) geraetWaehlen(b.getAttribute("data-geraet"));
    else if (b.hasAttribute("data-praeparat")) praeparatWaehlen(b.getAttribute("data-praeparat"));
    else if (b.hasAttribute("data-objektiv")) objektivWaehlen(+b.getAttribute("data-objektiv"));
    else if (b.hasAttribute("data-obj")) objektivWaehlen(+b.getAttribute("data-obj"));
    else { z.auswahl = b.getAttribute("data-typ"); listeAnzeigen(); leiterAnzeigen(); var n = el.liste.querySelector('[data-typ="' + z.auswahl + '"]'); if (n) n.focus(); }
  });
  el.fein.addEventListener("input", function () { z.fokus = +el.fein.value; anzeigen(); neuZeichnen(); });
  document.getElementById("mk-beschriften").addEventListener("change", function (e) { z.beschriften = e.target.checked; neuZeichnen(); });
  document.getElementById("mk-massstab").addEventListener("change", function (e) { z.massstab = e.target.checked; neuZeichnen(); });

  function verschieben(dx, dy) {
    var u = P().umfang;
    z.vx = Math.max(-u, Math.min(u, z.vx + dx)); z.vy = Math.max(-u, Math.min(u, z.vy + dy));
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

  knoepfeBauen();
  if (window.ResizeObserver) new ResizeObserver(groesse).observe(feld); else window.addEventListener("resize", groesse);
  praeparatWaehlen(z.p);
  groesse();
  if (document.fonts && document.fonts.load) document.fonts.load("700 20px Caveat").then(neuZeichnen, function () {});
})();
