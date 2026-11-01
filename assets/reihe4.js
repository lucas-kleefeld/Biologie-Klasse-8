/* =========================================================
   Modelle der Reihe 4: Teufelskreis, Belohnungssystem, Promille
   ========================================================= */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  function n(tag, a, txt) { var e = document.createElementNS(NS, tag); for (var k in a) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; return e; }
  function leeren(e) { while (e.firstChild) e.removeChild(e.firstChild); }
  function zahl(x, s) { return x.toLocaleString("de-DE", { minimumFractionDigits: s || 0, maximumFractionDigits: s || 0 }); }
  function hand(x, y, t, gr, anker, klasse) { return n("text", { x: x, y: y, "text-anchor": anker || "start", class: klasse || "hk", style: gr ? "font-size:" + gr + "px" : "" }, t); }
  function knoepfe(box, attr, fn, merken) {
    var bs = box.querySelectorAll("button[" + attr + "]");
    Array.prototype.forEach.call(bs, function (b) {
      b.addEventListener("click", function () {
        if (merken !== false) Array.prototype.forEach.call(bs, function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        fn(b.getAttribute(attr));
      });
    });
  }

  /* =======================================================
     1) Teufelskreis
     ======================================================= */
  function teufelskreis() {
    var box = document.getElementById("tk"); if (!box) return;
    var bild = document.getElementById("tk-bild");
    var S = [
      { t: "Problem", u: "Stress, Streit, Kummer", f: "f-blau-weich",
        text: "Am Anfang steht etwas, das belastet: Ärger in der Schule, Streit zu Hause, Liebeskummer, Einsamkeit oder Langeweile.",
        aus: "Ausstieg: Probleme ansprechen, mit Freunden, Familie oder einer Vertrauenslehrkraft reden, Hilfe holen, bevor sich Druck aufstaut." },
      { t: "Griff zum Suchtmittel", u: "um sich besser zu fühlen", f: "f-rosa-weich",
        text: "Statt das Problem anzugehen, greift man zu Alkohol, Zigaretten, anderen Drogen oder flüchtet sich stundenlang in Spiele.",
        aus: "Ausstieg: Nein sagen, andere Wege suchen, mit Stress umzugehen, zum Beispiel Sport, Musik oder ein Gespräch." },
      { t: "kurze Erleichterung", u: "das Problem ist kurz vergessen", f: "f-gruen-weich",
        text: "Das Belohnungssystem schüttet viel Dopamin aus. Für kurze Zeit fühlt man sich besser, lockerer oder entspannter.",
        aus: "Ausstieg: sich bewusst machen, dass das gute Gefühl vom Suchtmittel kommt und das Problem nicht löst." },
      { t: "Problem bleibt", u: "und wird oft größer", f: "f-gelb-weich",
        text: "Die Wirkung lässt nach. Das Problem ist noch da, oft ist es sogar größer geworden, weil man sich nicht darum gekümmert hat.",
        aus: "Ausstieg: ehrlich zu sich selbst sein und sich eingestehen, dass das Suchtmittel nicht hilft." },
      { t: "neue Probleme", u: "Schule, Familie, Geld", f: "f-gelb",
        text: "Es kommen neue Sorgen hinzu: schlechtere Noten, Ärger mit den Eltern, Geldprobleme, Streit mit Freunden, gesundheitliche Beschwerden.",
        aus: "Ausstieg: Spätestens jetzt ist Hilfe von außen wichtig, etwa durch Schulsozialarbeit, Beratungsstellen oder die Nummer gegen Kummer." },
      { t: "mehr Konsum", u: "Gewöhnung: man braucht mehr", f: "f-rosa",
        text: "Wegen der Gewöhnung braucht man für die gleiche Wirkung mehr. Der Kreis beginnt von vorn und dreht sich schneller.",
        aus: "Ausstieg: Eine Suchtberatungsstelle hilft, einen Weg aus der Abhängigkeit zu finden, auch anonym und kostenlos." }
    ];
    var schritt = 0, runde = 1;
    var CX = 300, CY = 236, RX = 230, RY = 170;
    function pos(k) { var w = (-90 + k * 60) * Math.PI / 180; return [CX + Math.cos(w) * RX, CY + Math.sin(w) * RY]; }
    function zeichne() {
      leeren(bild);
      bild.appendChild(n("ellipse", { cx: CX, cy: CY, rx: RX * .92, ry: RY * .92, class: "s2 gestrichelt", fill: "none" }));
      // Pfeile zwischen den Stationen
      for (var k = 0; k < 6; k++) {
        var w1 = (-90 + k * 60 + 21) * Math.PI / 180, w2 = (-90 + (k + 1) * 60 - 21) * Math.PI / 180;
        var x2 = CX + Math.cos(w2) * RX * .92, y2 = CY + Math.sin(w2) * RY * .92;
        var tx = -Math.sin(w2) * RX, ty = Math.cos(w2) * RY, l = Math.sqrt(tx * tx + ty * ty); tx /= l; ty /= l;
        bild.appendChild(n("path", { class: "s tk-pfeil" + (k === (schritt + 5) % 6 ? " aktiv" : ""), fill: "none",
          d: "M" + (CX + Math.cos(w1) * RX * .92).toFixed(1) + " " + (CY + Math.sin(w1) * RY * .92).toFixed(1) + " A " + RX * .92 + " " + RY * .92 + " 0 0 1 " + x2.toFixed(1) + " " + y2.toFixed(1) +
             " M " + (x2 - tx * 12 - ty * 7).toFixed(1) + " " + (y2 - ty * 12 + tx * 7).toFixed(1) + " L " + x2.toFixed(1) + " " + y2.toFixed(1) + " L " + (x2 - tx * 12 + ty * 7).toFixed(1) + " " + (y2 - ty * 12 - tx * 7).toFixed(1) }));
      }
      S.forEach(function (s, k) {
        var p = pos(k), g = n("g", { class: "tk-station" + (k === schritt ? " aktiv" : "") });
        g.appendChild(n("rect", { x: p[0] - 100, y: p[1] - 30, width: 200, height: 60, rx: 14, class: "s " + s.f }));
        g.appendChild(hand(p[0], p[1] - 4, s.t, 21, "middle", "h"));
        g.appendChild(hand(p[0], p[1] + 19, s.u, 17, "middle"));
        bild.appendChild(g);
      });
      // Mitte: Rucksack mit Steinen
      var steine = Math.min(14, (runde - 1) * 3 + (schritt >= 4 ? 2 : 0) + 1);
      bild.appendChild(n("path", { class: "s f-sand", d: "M262 210 q 0 -30 38 -30 q 38 0 38 30 v 70 q 0 10 -10 10 h -56 q -10 0 -10 -10 z" }));
      bild.appendChild(n("path", { class: "s2", fill: "none", d: "M282 182 q 18 -22 36 0" }));
      for (var i = 0; i < steine; i++) bild.appendChild(n("ellipse", { cx: 276 + (i % 4) * 16, cy: 278 - Math.floor(i / 4) * 14, rx: 8, ry: 6, class: "s2 tk-stein" }));
      bild.appendChild(hand(CX, 316, "Probleme", 18, "middle"));
      // Konsum-Balken rechts
      var X = 600, menge = Math.min(1, .15 + (runde - 1) * .22 + (schritt >= 5 ? .1 : 0));
      bild.appendChild(hand(X + 70, 70, "Menge des", 18, "middle")); bild.appendChild(hand(X + 70, 90, "Suchtmittels", 18, "middle"));
      bild.appendChild(n("rect", { x: X + 50, y: 110, width: 40, height: 260, rx: 8, class: "s2 f-weiss" }));
      bild.appendChild(n("rect", { x: X + 54, y: 366 - 252 * menge, width: 32, height: 252 * menge, rx: 5, class: "tk-menge" }));
      bild.appendChild(hand(X + 70, 410, "Runde " + runde, 24, "middle", "h"));
      var s = S[schritt];
      document.getElementById("tk-titel").textContent = "Runde " + runde + ", Station " + (schritt + 1) + ": " + s.t;
      document.getElementById("tk-text").textContent = s.text + (runde > 1 && schritt === 0 ? " Inzwischen sind es mehr Probleme als in der ersten Runde." : "");
      document.getElementById("tk-ausstieg").textContent = s.aus;
    }
    document.getElementById("tk-weiter").addEventListener("click", function () {
      schritt++; if (schritt > 5) { schritt = 0; runde = Math.min(runde + 1, 4); }
      zeichne();
    });
    document.getElementById("tk-reset").addEventListener("click", function () { schritt = 0; runde = 1; zeichne(); });
    zeichne();
  }

  /* =======================================================
     2) Belohnungssystem
     ======================================================= */
  function belohnung() {
    var box = document.getElementById("bs"); if (!box) return;
    var bild = document.getElementById("bs-bild"), regler = document.getElementById("bs-oft"), textE = document.getElementById("bs-text");
    var ausloeser = "nichts";
    var MENGE = { nichts: 3, natur: 8, droge: 22 };
    function rezeptoren(oft) { return Math.max(3, 8 - Math.round(oft * .5)); }
    function zeichne() {
      leeren(bild);
      var oft = +regler.value, rez = rezeptoren(oft), m = MENGE[ausloeser];
      document.getElementById("bs-oft-t").textContent = oft === 0 ? "noch nie" : oft + "-mal" + (oft === 10 ? " und öfter" : "");
      // erste Nervenzelle
      bild.appendChild(n("path", { class: "s f-gelb", d: "M200 0 C 200 50, 90 60, 90 130 C 90 170, 370 170, 370 130 C 370 60, 260 50, 260 0 Z" }));
      [[170, 100], [230, 92], [200, 126], [150, 130], [255, 128]].forEach(function (b) {
        bild.appendChild(n("circle", { cx: b[0], cy: b[1], r: 13, class: "s2 f-weiss" }));
        for (var j = 0; j < 3; j++) bild.appendChild(n("circle", { cx: b[0] - 4 + j * 4, cy: b[1] + (j % 2 ? 3 : -3), r: 2.8, class: "bs-dopa" }));
      });
      // zweite Nervenzelle
      bild.appendChild(n("path", { class: "s f-gelb", d: "M60 270 C 90 236, 370 236, 400 270 L 400 330 H 60 Z" }));
      var rx = [];
      for (var i = 0; i < rez; i++) rx.push(110 + i * 240 / Math.max(1, rez - 1));
      rx.forEach(function (x) { bild.appendChild(n("path", { class: "s f-rosa", d: "M" + (x - 10) + " 246 v -12 h 6 v 6 h 8 v -6 h 6 v 12 z" })); });
      // Dopamin im Spalt, gebundene an Rezeptoren
      var gebunden = Math.min(m, rez);
      for (var k = 0; k < gebunden; k++) bild.appendChild(n("circle", { cx: rx[k], cy: 228, r: 4.5, class: "bs-dopa" }));
      for (k = 0; k < m - gebunden; k++) bild.appendChild(n("circle", { cx: 110 + (k * 47) % 240, cy: 180 + (k * 13) % 36, r: 4.5, class: "bs-dopa" }));
      bild.appendChild(hand(230, 362, "Rezeptoren: " + rez, 20, "middle", "h"));
      bild.appendChild(hand(400, 20, "Nervenzelle 1", 18, "end"));
      bild.appendChild(hand(400, 352, "Nervenzelle 2", 18, "start"));
      // Wohlgefühl
      var gefuehl = m * rez / 8;                       // 3 = normaler Alltag
      var X = 500;
      bild.appendChild(hand(X + 120, 30, "Wohlgefühl", 22, "middle", "h"));
      bild.appendChild(n("rect", { x: X + 90, y: 50, width: 60, height: 300, rx: 10, class: "s2 f-weiss" }));
      var h = Math.min(296, gefuehl / 22 * 296);
      bild.appendChild(n("rect", { x: X + 93, y: 348 - h, width: 54, height: h, rx: 7, class: gefuehl < 2.5 ? "bs-schlecht" : "bs-gut" }));
      var yN = 348 - 3 / 22 * 296;
      bild.appendChild(n("path", { class: "s2 gestrichelt", d: "M" + (X + 80) + " " + yN.toFixed(1) + " H " + (X + 160) }));
      bild.appendChild(hand(X + 166, yN + 5, "normaler", 16)); bild.appendChild(hand(X + 166, yN + 23, "Alltag", 16));
      var yNat = 348 - 8 / 22 * 296;
      bild.appendChild(n("path", { class: "s2 gestrichelt", d: "M" + (X + 80) + " " + yNat.toFixed(1) + " H " + (X + 160) }));
      bild.appendChild(hand(X + 166, yNat + 5, "schönes", 16)); bild.appendChild(hand(X + 166, yNat + 23, "Erlebnis", 16));
      // Text
      var t;
      if (ausloeser === "droge") t = oft < 3 ? "Das Suchtmittel setzt viel mehr Dopamin frei als jede natürliche Belohnung. Das Gehirn merkt sich: „Das war besonders gut!“" :
        "Es sind weniger Rezeptoren übrig. Obwohl das Suchtmittel genauso viel Dopamin freisetzt, ist das Wohlgefühl viel schwächer als am Anfang. Für die alte Wirkung bräuchte man mehr: Toleranz.";
      else if (ausloeser === "natur") t = oft < 3 ? "Ein Lob, ein Tor oder ein gutes Essen: Das Belohnungssystem schüttet Dopamin aus, wir fühlen uns gut." :
        "Weil Rezeptoren abgebaut wurden, wirkt die natürliche Belohnung kaum noch. Dinge, die früher Freude gemacht haben, fühlen sich jetzt nur noch normal an.";
      else t = oft < 3 ? "Im Alltag wird nur wenig Dopamin ausgeschüttet. Das reicht für ein normales Gefühl." :
        "Ohne Suchtmittel bindet kaum Dopamin. Man fühlt sich leer, unruhig und schlecht gelaunt. Das ist ein Teil des Entzugs. Erst nach Wochen bis Monaten ohne Suchtmittel bildet das Gehirn wieder mehr Rezeptoren.";
      textE.textContent = t;
    }
    knoepfe(box, "data-ausloeser", function (v) { ausloeser = v; zeichne(); });
    regler.addEventListener("input", zeichne);
    zeichne();
  }

  /* =======================================================
     3) Promille und Rauschbrille
     ======================================================= */
  function promille() {
    var box = document.getElementById("pm"); if (!box) return;
    var bild = document.getElementById("pm-bild"), sicht = document.getElementById("pm-sicht"), regler = document.getElementById("pm-zeit");
    var GRAMM = { bier: 13.2, wein: 17.6, alkopop: 12.1, schnaps: 6.4 };
    var NAME = { bier: "Bier", wein: "Wein", alkopop: "Mixgetränk", schnaps: "Schnaps" };
    var PERSON = { w: 60 * .6, m: 80 * .7 };
    var person = "w", getraenke = [];             // {t: Minuten ab 20 Uhr, art}
    var X0 = 60, X1 = 740, Y0 = 20, Y1 = 280, DAUER = 720;
    function uhr(min) { var h = (20 + Math.floor(min / 60)) % 24, m = min % 60; return (h < 10 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m; }
    function verlauf() {
      var bak = 0, out = [], div = PERSON[person];
      for (var t = 0; t <= DAUER; t += 5) {
        out.push(bak);
        var zufluss = 0;
        getraenke.forEach(function (g) { if (t >= g.t && t < g.t + 60) zufluss += GRAMM[g.art] / 60 * 5; });
        bak = Math.max(0, bak + zufluss / div - .15 * 5 / 60);
      }
      return out;
    }
    function wirkung(p) {
      if (p < .05) return "Kein Alkohol im Blut.";
      if (p < .2) return "Noch kaum spürbar, aber die Konzentration lässt bereits nach.";
      if (p < .5) return "Enthemmung: Man redet mehr, schätzt Entfernungen und Geschwindigkeiten schlechter ein.";
      if (p < .8) return "Die Reaktionszeit ist deutlich länger, das Blickfeld wird enger, man überschätzt sich.";
      if (p < 1) return "Tunnelblick, Gleichgewichtsstörungen, man wird leichter gereizt.";
      if (p < 2) return "Rausch: Doppeltsehen, Lallen, Torkeln, starke Stimmungsschwankungen.";
      if (p < 3) return "Betäubung: Erbrechen, Verwirrtheit, Gedächtnislücken.";
      return "Lebensgefahr: Bewusstlosigkeit und Atemlähmung möglich. Notruf 112!";
    }
    function zeichne() {
      var v = verlauf(), t = +regler.value * 15, p = v[t / 5];
      var maxV = Math.max.apply(null, v), YMAX = Math.max(1.2, Math.ceil((maxV + .2) * 2) / 2);
      function px(min) { return X0 + min / DAUER * (X1 - X0); }
      function py(w) { return Y1 - w / YMAX * (Y1 - Y0); }
      leeren(bild);
      bild.appendChild(n("rect", { x: X0, y: Y0, width: X1 - X0, height: Y1 - Y0, class: "s2 f-weiss" }));
      for (var w = 0; w <= YMAX + 1e-9; w += .5) {
        bild.appendChild(n("path", { class: "pm-gitter", d: "M" + X0 + " " + py(w) + " H " + X1 }));
        bild.appendChild(hand(X0 - 8, py(w) + 6, zahl(w, 1) + " ‰", 15, "end"));
      }
      for (var h = 0; h <= 12; h += 2) bild.appendChild(hand(px(h * 60), Y1 + 22, uhr(h * 60), 15, "middle"));
      [[.5, "0,5 ‰: Grenze im Straßenverkehr (ab 21 und nach der Probezeit)"], [1.1, "1,1 ‰: absolute Fahruntüchtigkeit"]].forEach(function (g) {
        if (g[0] > YMAX) return;
        bild.appendChild(n("path", { class: "pm-grenze", d: "M" + X0 + " " + py(g[0]) + " H " + X1 }));
        bild.appendChild(hand(X1 - 6, py(g[0]) - 6, g[1], 15, "end"));
      });
      getraenke.forEach(function (g) {
        bild.appendChild(n("path", { class: "s2", d: "M" + px(g.t) + " " + Y1 + " v -12" }));
        bild.appendChild(n("circle", { cx: px(g.t), cy: Y1 - 16, r: 5, class: "pm-glas-" + g.art }));
      });
      var d = "";
      v.forEach(function (w, i) { d += (i ? " L " : "M") + px(i * 5).toFixed(1) + " " + py(w).toFixed(1); });
      bild.appendChild(n("path", { d: d, class: "pm-kurve", fill: "none" }));
      bild.appendChild(n("path", { class: "s2 gestrichelt", d: "M" + px(t) + " " + Y0 + " V " + Y1 }));
      bild.appendChild(n("circle", { cx: px(t), cy: py(p), r: 6, class: "pm-punkt" }));
      document.getElementById("pm-zeit-t").textContent = uhr(t);
      var nuechtern = -1;
      for (var i = v.length - 1; i >= 0; i--) if (v[i] > .001) { nuechtern = i + 1; break; }
      var info = getraenke.length ? getraenke.length + (getraenke.length === 1 ? " Getränk" : " Getränke") + ", höchster Wert " + zahl(maxV, 2) + " ‰" + (nuechtern > 0 && nuechtern * 5 <= DAUER ? ", wieder nüchtern um etwa " + uhr(nuechtern * 5) + " Uhr" : nuechtern > 0 ? ", um 8 Uhr noch nicht nüchtern" : "") : "Noch keine Getränke";
      document.getElementById("pm-wert").textContent = uhr(t) + " Uhr: " + zahl(p, 2) + " ‰. " + info + ".";
      document.getElementById("pm-text").textContent = wirkung(p);
      szene(p);
    }
    function szene(p) {
      leeren(sicht);
      var blur = Math.min(6, p * 2.4), versatz = p < .3 ? 0 : Math.min(26, (p - .3) * 16), tunnel = p < .5 ? 0 : Math.min(1, (p - .5) / 1.5), kipp = Math.min(5, p * 2);
      var defs = n("defs", {});
      var f = n("filter", { id: "pm-blur", x: "-10%", y: "-10%", width: "120%", height: "120%" }); f.appendChild(n("feGaussianBlur", { stdDeviation: blur.toFixed(2) })); defs.appendChild(f);
      var rg = n("radialGradient", { id: "pm-tunnel", cx: "50%", cy: "50%", r: "70%" });
      rg.appendChild(n("stop", { offset: (100 - tunnel * 62) + "%", "stop-opacity": 0, style: "stop-color:var(--tinte)" }));
      rg.appendChild(n("stop", { offset: "100%", "stop-opacity": .92, style: "stop-color:var(--tinte)" }));
      defs.appendChild(rg); sicht.appendChild(defs);
      function inhalt() {
        var g = n("g", {});
        g.appendChild(n("rect", { x: 0, y: 0, width: 760, height: 260, class: "f-blau-weich" }));
        g.appendChild(n("rect", { x: 0, y: 180, width: 760, height: 80, class: "f-sand" }));
        for (var i = 0; i < 6; i++) g.appendChild(n("rect", { x: 300 + i * 34, y: 196, width: 22, height: 54, class: "f-weiss" }));
        g.appendChild(n("rect", { x: 80, y: 40, width: 8, height: 150, class: "s f-sand" }));
        g.appendChild(n("rect", { x: 30, y: 30, width: 200, height: 96, rx: 8, class: "s f-weiss" }));
        g.appendChild(hand(130, 58, "Bus 7", 24, "middle", "h"));
        g.appendChild(hand(130, 84, "20:14  20:44  21:14", 19, "middle"));
        g.appendChild(hand(130, 108, "21:44  22:14  22:44", 19, "middle"));
        g.appendChild(n("rect", { x: 620, y: 40, width: 46, height: 110, rx: 10, class: "s f-weiss" }));
        g.appendChild(n("circle", { cx: 643, cy: 70, r: 14, class: "s f-rosa-tief" }));
        g.appendChild(n("circle", { cx: 643, cy: 118, r: 14, class: "s f-weiss" }));
        g.appendChild(n("rect", { x: 639, y: 150, width: 8, height: 40, class: "s f-sand" }));
        g.appendChild(n("path", { class: "s f-gelb", d: "M470 150 q 30 -8 40 6 l 30 6 v 18 h -100 v -18 z" }));
        g.appendChild(n("circle", { cx: 460, cy: 182, r: 10, class: "s f-weiss" })); g.appendChild(n("circle", { cx: 528, cy: 182, r: 10, class: "s f-weiss" }));
        return g;
      }
      var welt = n("g", { transform: "rotate(" + kipp.toFixed(1) + " 380 130)", filter: blur > .05 ? "url(#pm-blur)" : "" });
      welt.appendChild(inhalt());
      if (versatz > 0) { var geist = inhalt(); geist.setAttribute("transform", "translate(" + versatz.toFixed(1) + " " + (versatz * .3).toFixed(1) + ")"); geist.setAttribute("opacity", ".45"); welt.appendChild(geist); }
      sicht.appendChild(welt);
      if (tunnel > 0) sicht.appendChild(n("rect", { x: 0, y: 0, width: 760, height: 260, fill: "url(#pm-tunnel)" }));
    }
    knoepfe(box.querySelector('[aria-label="Person wählen"]'), "data-person", function (v) { person = v; zeichne(); });
    knoepfe(box.querySelector('[aria-label="Getränk hinzufügen"]'), "data-getraenk", function (v) {
      getraenke.push({ t: +regler.value * 15, art: v });
      zeichne();
    }, false);
    regler.addEventListener("input", zeichne);
    document.getElementById("pm-leeren").addEventListener("click", function () { getraenke = []; regler.value = 0; zeichne(); });
    zeichne();
  }

  teufelskreis(); belohnung(); promille();
})();
