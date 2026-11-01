/* =========================================================
   Modelle der Reihe 3: See, Fotosynthese, Nahrungsnetz, Räuber-Beute
   ========================================================= */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  function n(tag, a, txt) { var e = document.createElementNS(NS, tag); for (var k in a) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; return e; }
  function leeren(e) { while (e.firstChild) e.removeChild(e.firstChild); }
  function zahl(x, s) { return x.toLocaleString("de-DE", { maximumFractionDigits: s == null ? 1 : s }); }
  function knoepfe(box, attr, fn) {
    var bs = box.querySelectorAll("button[" + attr + "]");
    Array.prototype.forEach.call(bs, function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call(bs, function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        fn(b.getAttribute(attr));
      });
    });
  }
  function hand(x, y, t, gr, anker, klasse) {
    return n("text", { x: x, y: y, "text-anchor": anker || "start", class: klasse || "hk", style: gr ? "font-size:" + gr + "px" : "" }, t);
  }
  var bewegungArm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* =======================================================
     1) See im Jahreslauf
     ======================================================= */
  function see() {
    var box = document.getElementById("se"); if (!box) return;
    var bild = document.getElementById("se-bild"), titel = document.getElementById("se-titel"), text = document.getElementById("se-text");
    var TIEFE = [0, 2, 4, 6, 8, 10, 12, 15, 20];
    var JZ = {
      fruehling: { name: "Frühling: Frühjahrszirkulation", t: [4, 4, 4, 4, 4, 4, 4, 4, 4], o: [12, 12, 12, 12, 12, 12, 12, 11.5, 11.5], zirk: true,
        text: "Das Eis ist geschmolzen, das Wasser ist überall etwa 4 °C kalt und hat damit überall die gleiche Dichte. Schon ein leichter Wind kann den ganzen See umwälzen. Sauerstoff gelangt bis zum Grund, Mineralstoffe vom Grund nach oben. Mit mehr Licht und Mineralstoffen beginnen die Algen stark zu wachsen." },
      sommer: { name: "Sommer: Sommerstagnation", t: [22, 21.5, 20, 15, 9, 6.5, 5.5, 5, 4.5], o: [9, 9.5, 10, 8, 5, 3, 2, 1, .5],
        text: "Die Sonne erwärmt das Oberflächenwasser. Warmes Wasser ist leichter und bleibt oben. In der Sprungschicht nimmt die Temperatur schnell ab. Darunter ist das Wasser kalt und schwer. Die Schichten mischen sich nicht. Oben bilden Algen und Pflanzen viel Sauerstoff. Unten ist es zu dunkel für Fotosynthese, und Destruenten verbrauchen beim Zersetzen Sauerstoff, der nicht ersetzt wird." },
      herbst: { name: "Herbst: Herbstzirkulation", t: [8, 8, 8, 8, 8, 8, 8, 8, 8], o: [9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5], zirk: true,
        text: "Das Oberflächenwasser kühlt ab und sinkt, bis der ganze See gleich warm ist. Die Sprungschicht verschwindet. Herbststürme durchmischen den See bis zum Grund. Das sauerstoffarme Tiefenwasser bekommt wieder Sauerstoff, und die Mineralstoffe vom Grund verteilen sich im ganzen See." },
      winter: { name: "Winter: Winterstagnation", t: [0, 1.5, 2.5, 3.2, 3.6, 3.8, 4, 4, 4], o: [12.5, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5], eis: true,
        text: "Das Oberflächenwasser kühlt unter 4 °C ab. Weil Wasser unter 4 °C wieder leichter wird, bleibt es oben und gefriert schließlich. Das Eis schwimmt und schützt den See vor weiterer Abkühlung. Am Grund bleibt es 4 °C warm, dort überwintern Fische und andere Tiere. Unter dem Eis gibt es kaum Durchmischung." }
    };
    var ZONEN = {
      erle: { x: 0, w: 66, name: "Erlenbruchzone", text: "Der feuchte Uferstreifen ist oft überschwemmt. Hier wachsen Schwarzerlen und Weiden, deren Wurzeln nasse, sauerstoffarme Böden vertragen. Frösche, Kröten und Ringelnattern finden Verstecke." },
      roehricht: { x: 66, w: 62, name: "Röhrichtzone", text: "Im flachen Wasser wachsen Schilf, Rohrkolben und Binsen. Ihre hohlen Stängel leiten Luft zu den Wurzeln im Schlamm. Teichrohrsänger und Blässhühner brüten hier, Fische laichen zwischen den Halmen." },
      schwimm: { x: 128, w: 64, name: "Schwimmblattzone", text: "Seerosen und Teichrosen wurzeln im Grund. Ihre Blätter schwimmen auf der Oberfläche und haben die Spaltöffnungen auf der Oberseite. Unter den Blättern leben Schnecken und Insektenlarven." },
      tauch: { x: 192, w: 80, name: "Tauchblattzone", text: "Laichkraut, Wasserpest und Tausendblatt leben ganz unter Wasser. Ihre Blätter sind dünn und oft fein zerteilt. Sie wachsen so tief, wie noch genug Licht für die Fotosynthese ankommt." },
      frei: { x: 272, w: 208, name: "Freiwasserzone", text: "Oben, wo Licht hinkommt, schweben Algen (Phytoplankton) und kleine Tiere wie Wasserflöhe (Zooplankton). Fische wie Rotauge, Barsch und Hecht jagen hier. Haubentaucher tauchen nach Fischen." },
      boden: { x: 0, w: 480, name: "Bodenzone", text: "Am dunklen Grund wachsen keine Pflanzen. Abgestorbene Lebewesen sinken herab und werden von Bakterien, Pilzen, Schlammröhrenwürmern und Zuckmückenlarven zersetzt. Dabei wird Sauerstoff verbraucht und Mineralstoffe werden frei." }
    };
    var zeit = "sommer", zone = null;
    var Y0 = 90, Y1 = 340;                       // Oberfläche, 20 m Tiefe
    function ty(m) { return Y0 + m / 20 * (Y1 - Y0); }
    function boden(x) { if (x < 66) return Y0 - 8; if (x < 272) return Y0 + (x - 66) / (272 - 66) * 210; return Y0 + 210 + (x - 272) / 208 * 40; }
    function farbe(t, winter) { if (t >= 15) return "f-rosa"; if (t >= 7) return "f-rosa-weich"; if (t > 4.4 || (winter && t < 3.5)) return "f-blau-weich"; return "f-blau"; }
    function lin(arr, m) { for (var i = 0; i < TIEFE.length - 1; i++) if (m <= TIEFE[i + 1]) { var q = (m - TIEFE[i]) / (TIEFE[i + 1] - TIEFE[i]); return arr[i] + q * (arr[i + 1] - arr[i]); } return arr[arr.length - 1]; }

    function zeichne() {
      leeren(bild);
      var d = JZ[zeit];
      // Himmel
      if (zeit === "winter") bild.appendChild(n("circle", { cx: 420, cy: 34, r: 14, class: "s f-gelb-weich" }));
      else bild.appendChild(n("circle", { cx: 420, cy: 34, r: zeit === "sommer" ? 22 : 16, class: "s f-gelb" }));
      if (d.zirk) { var w = n("g", {}); w.appendChild(n("path", { class: "s2", fill: "none", d: "M300 30 q 20 -8 40 0 t 40 0 M310 46 q 20 -8 40 0 t 30 0" })); bild.appendChild(w); bild.appendChild(hand(300, 70, "Wind", 18)); }
      // Wasser in Schichten
      for (var m = 0; m < 20; m += 1) {
        var t = lin(d.t, m + .5);
        bild.appendChild(n("rect", { x: 0, y: ty(m), width: 480, height: ty(m + 1) - ty(m) + .6, class: farbe(t, !!d.eis) }));
      }
      if (zeit === "sommer") {
        bild.appendChild(n("path", { class: "s2 gestrichelt", d: "M150 " + ty(5) + " H 480 M 210 " + ty(9) + " H 480" }));
        bild.appendChild(hand(474, ty(7) + 6, "Sprungschicht", 18, "end"));
      }
      // Ufer und Grund
      var p = "M0 " + (Y0 - 8);
      for (var x = 0; x <= 480; x += 8) p += " L " + x + " " + boden(x).toFixed(1);
      p += " L 480 360 L 0 360 Z";
      bild.appendChild(n("path", { d: p, class: "s f-sand" }));
      bild.appendChild(n("path", { class: "s2", fill: "none", d: "M66 " + Y0 + " H 480" }));
      if (d.eis) bild.appendChild(n("rect", { x: 70, y: Y0 - 6, width: 410, height: 12, rx: 3, class: "s f-weiss" }));
      // Pflanzen
      var g = n("g", {});
      [20, 46].forEach(function (x, i) {
        g.appendChild(n("path", { class: "s k-bernstein", "stroke-width": 4, fill: "none", d: "M" + x + " " + (Y0 - 8) + " V " + (Y0 - 46 + i * 6) }));
        g.appendChild(n("circle", { cx: x, cy: Y0 - 58 + i * 6, r: zeit === "winter" ? 10 : 18, class: zeit === "winter" ? "s2 f-weiss" : "s f-gruen" }));
      });
      [80, 96, 112].forEach(function (x) {
        var hh = zeit === "winter" ? 40 : 66;
        g.appendChild(n("path", { class: "s k-gruen", "stroke-width": 3, fill: "none", d: "M" + x + " " + boden(x) + " C " + (x - 2) + " " + (Y0 - 20) + ", " + (x + 4) + " " + (Y0 - hh + 10) + ", " + (x + 3) + " " + (Y0 - hh) }));
        if (zeit !== "winter") g.appendChild(n("rect", { x: x, y: Y0 - hh - 18, width: 7, height: 18, rx: 3.5, class: "s2 f-sand" }));
      });
      if (zeit !== "winter") [146, 176].forEach(function (x) {
        g.appendChild(n("path", { class: "s2 k-gruen", fill: "none", d: "M" + x + " " + boden(x) + " Q " + (x + 6) + " " + ((boden(x) + Y0) / 2) + " " + x + " " + Y0 }));
        g.appendChild(n("ellipse", { cx: x, cy: Y0 - 2, rx: 15, ry: 5, class: "s2 f-gruen" }));
      });
      if (zeit === "sommer") g.appendChild(n("circle", { cx: 152, cy: Y0 - 8, r: 5, class: "s2 f-weiss" }));
      [212, 236, 258].forEach(function (x) {
        var y = boden(x), h = (y - Y0) * .7;
        if (zeit === "winter") h *= .4;
        var dd = "M" + x + " " + y + " C " + (x - 6) + " " + (y - h * .4) + ", " + (x + 6) + " " + (y - h * .7) + ", " + x + " " + (y - h);
        g.appendChild(n("path", { class: "s k-gruen", "stroke-width": 2.5, fill: "none", d: dd }));
        for (var k = 1; k < 6; k++) g.appendChild(n("path", { class: "s2 k-gruen", fill: "none", d: "M" + x + " " + (y - h * k / 6) + " l -8 -6 M " + x + " " + (y - h * k / 6) + " l 8 -6" }));
      });
      // Fische und Plankton
      function fisch(x, y, s, f) { return n("path", { class: "s " + f, transform: "translate(" + x + " " + y + ") scale(" + s + ")", d: "M-26 0 C -14 -14, 14 -14, 24 0 C 14 14, -14 14, -26 0 Z M24 0 L 38 -11 L 35 0 L 38 11 Z" }); }
      if (zeit === "winter") { g.appendChild(fisch(380, 300, .8, "f-gelb")); g.appendChild(fisch(430, 316, .7, "f-gelb")); }
      else if (zeit === "sommer") { g.appendChild(fisch(340, 130, .9, "f-gelb")); g.appendChild(fisch(330, 190, .8, "f-gruen")); }
      else { g.appendChild(fisch(330, 200, .9, "f-gelb")); g.appendChild(fisch(420, 260, .8, "f-gruen")); }
      var nAlgen = zeit === "sommer" ? 14 : zeit === "fruehling" ? 10 : zeit === "herbst" ? 6 : 2;
      for (var a = 0; a < nAlgen; a++) g.appendChild(n("circle", { cx: 290 + (a * 47) % 180, cy: Y0 + 14 + (a * 19) % 50, r: 3.5, class: "s2 f-gruen" }));
      bild.appendChild(g);
      // Zirkulationspfeile
      if (d.zirk) {
        var pf = n("g", { class: "k-blau" });
        pf.appendChild(n("path", { class: "s k-blau", fill: "none", d: "M300 110 C 270 200, 320 290, 380 290 C 440 290, 470 200, 440 110" }));
        pf.appendChild(n("path", { class: "s k-blau", fill: "none", d: "M432 120 l 8 -12 l 4 14" }));
        pf.appendChild(n("path", { class: "s k-blau", fill: "none", d: "M296 124 l 4 -14 l 8 12" }));
        bild.appendChild(pf);
        bild.appendChild(hand(380, 230, "Durchmischung", 18, "middle"));
      }
      // Zone hervorheben
      if (zone) {
        var z = ZONEN[zone];
        if (zone === "boden") {
          var bp = "M66 " + (Y0 + 2);
          for (var bx = 66; bx <= 480; bx += 8) bp += " L " + bx + " " + (boden(bx) - 14).toFixed(1);
          for (bx = 480; bx >= 66; bx -= 8) bp += " L " + bx + " " + (boden(bx) + 6).toFixed(1);
          bild.appendChild(n("path", { d: bp + " Z", class: "se-zone" }));
        } else bild.appendChild(n("rect", { x: z.x + 2, y: zone === "erle" ? 20 : Y0 - 74, width: z.w - 4, height: zone === "erle" ? 80 : (zone === "frei" ? 270 : Math.min(260, boden(z.x + z.w) - Y0 + 74)), rx: 10, class: "se-zone" }));
      }
      // Diagramm rechts
      var X0 = 540, X1 = 740;
      var gr = n("g", {});
      gr.appendChild(n("rect", { x: X0, y: Y0, width: X1 - X0, height: Y1 - Y0, class: "s2 f-weiss" }));
      [0, 5, 10, 15, 20].forEach(function (mm) {
        gr.appendChild(n("path", { class: "s2", d: "M" + (X0 - 5) + " " + ty(mm) + " H " + X0 }));
        gr.appendChild(hand(X0 - 9, ty(mm) + 6, mm + " m", 16, "end"));
      });
      [0, 5, 10, 15, 20, 25].forEach(function (tt) {
        var xx = X0 + tt / 25 * (X1 - X0);
        gr.appendChild(n("path", { class: "s2", d: "M" + xx + " " + Y1 + " v 5" }));
        gr.appendChild(hand(xx, Y1 + 20, String(tt), 15, "middle"));
      });
      gr.appendChild(hand(X0 - 50, Y0 - 10, "Tiefe", 17));
      gr.appendChild(hand((X0 + X1) / 2, Y1 + 40, "°C bzw. mg O₂ pro Liter", 16, "middle"));
      function kurve(arr, klasse) {
        var s = "";
        TIEFE.forEach(function (mm, i) { s += (i ? " L " : "M") + (X0 + arr[i] / 25 * (X1 - X0)).toFixed(1) + " " + ty(mm).toFixed(1); });
        gr.appendChild(n("path", { d: s, fill: "none", class: klasse, "stroke-width": 3.5 }));
      }
      kurve(d.t, "s k-rosa");
      kurve(d.o, "s k-blau");
      gr.appendChild(n("rect", { x: X0 + 6, y: Y0 - 50, width: 14, height: 4, class: "se-leg-t" }));
      gr.appendChild(hand(X0 + 26, Y0 - 42, "Temperatur", 17));
      gr.appendChild(n("rect", { x: X0 + 6, y: Y0 - 28, width: 14, height: 4, class: "se-leg-o" }));
      gr.appendChild(hand(X0 + 26, Y0 - 20, "Sauerstoff", 17));
      bild.appendChild(gr);
      bild.appendChild(hand(240, 386, JZ[zeit].name, 24, "middle", "h"));

      if (zone) { titel.textContent = ZONEN[zone].name; text.textContent = ZONEN[zone].text; }
      else { titel.textContent = d.name; text.textContent = d.text; }
    }
    knoepfe(box.querySelector('[aria-label="Jahreszeit wählen"]'), "data-zeit", function (v) {
      zeit = v; zone = null;
      Array.prototype.forEach.call(document.querySelectorAll("#se-zonen button"), function (b) { b.setAttribute("aria-pressed", "false"); });
      zeichne();
    });
    Array.prototype.forEach.call(document.querySelectorAll("#se-zonen button"), function (b) { b.setAttribute("aria-pressed", "false"); });
    knoepfe(document.getElementById("se-zonen"), "data-zone", function (v) { zone = v; zeichne(); });
    zeichne();
  }

  /* =======================================================
     2) Fotosynthese messen
     ======================================================= */
  function foto() {
    var box = document.getElementById("fo"); if (!box) return;
    var bild = document.getElementById("fo-bild"), rAbst = document.getElementById("fo-abstand"), rTemp = document.getElementById("fo-temp");
    var dunkel = document.getElementById("fo-dunkel"), ausgabe = document.getElementById("fo-rate"), tbody = document.querySelector("#fo-tabelle tbody");
    var co2 = 1, CO2NAME = { "0.15": "abgekocht", "1": "Leitungswasser", "1.6": "mit CO₂" };
    var blasen = [], letzte = 0, rate = 0, nr = 0;
    var GX = 600, STIEL = 214;                    // Glas und Stängelende
    function berechne() {
      var d = +rAbst.value, T = +rTemp.value;
      if (dunkel.checked) return 0;
      var I = 100 * Math.pow(10 / d, 2), L = I / (I + 20);
      var C = co2 / (co2 + .5);
      var Tf = T <= 30 ? .15 + .85 * (T - 5) / 25 : Math.max(0, 1 - Math.pow((T - 30) / 15, .8));
      return Math.round(60 * Math.min(L, C) * Tf);
    }
    var statisch = n("g", {}), blasenG = n("g", {});
    function aufbau() {
      leeren(bild); leeren(statisch);
      var d = +rAbst.value, lx = GX - 120 - (d - 10) * 8.4, an = !dunkel.checked;
      // Tisch
      statisch.appendChild(n("rect", { x: 10, y: 320, width: 740, height: 12, rx: 4, class: "s f-sand" }));
      // Lineal
      statisch.appendChild(n("path", { class: "s2", d: "M" + (lx + 50) + " 300 H " + GX }));
      statisch.appendChild(n("path", { class: "s2", d: "M" + (lx + 50) + " 294 v 12 M " + GX + " 294 v 12" }));
      statisch.appendChild(n("rect", { x: (lx + 50 + GX) / 2 - 30, y: 274, width: 60, height: 24, rx: 6, class: "f-weiss" }));
      statisch.appendChild(hand((lx + 50 + GX) / 2, 292, d + " cm", 20, "middle"));
      // Lampe
      if (an) statisch.appendChild(n("path", { d: "M" + (lx + 50) + " 120 L " + (GX - 40) + " 70 L " + (GX - 40) + " 270 L " + (lx + 50) + " 200 Z", class: "fo-licht", opacity: Math.max(.15, Math.min(.9, 9 / d)) }));
      statisch.appendChild(n("path", { class: "s f-weiss", d: "M" + (lx - 10) + " 320 h 60 l -10 -14 h -40 z" }));
      statisch.appendChild(n("path", { class: "s k-bernstein", "stroke-width": 4, fill: "none", d: "M" + (lx + 20) + " 306 V 170" }));
      statisch.appendChild(n("path", { class: "s " + (an ? "f-gelb" : "f-weiss"), d: "M" + (lx - 10) + " 140 L " + (lx + 50) + " 110 L " + (lx + 50) + " 210 L " + (lx - 10) + " 180 Z" }));
      statisch.appendChild(n("circle", { cx: lx + 50, cy: 160, r: 16, class: "s2 " + (an ? "f-gelb-weich" : "f-weiss") }));
      // Becherglas mit Reagenzglas
      statisch.appendChild(n("path", { class: "f-blau-weich", d: "M" + (GX - 46) + " 150 V 314 H " + (GX + 46) + " V 150 Z" }));
      statisch.appendChild(n("path", { class: "s", fill: "none", d: "M" + (GX - 50) + " 110 V 318 H " + (GX + 50) + " V 110" }));
      statisch.appendChild(n("path", { class: "s2 f-weiss", d: "M" + (GX - 16) + " 60 V 286 a 16 16 0 0 0 32 0 V 60 Z", opacity: .5 }));
      statisch.appendChild(n("path", { class: "f-blau-weich", d: "M" + (GX - 13) + " 80 V 286 a 13 13 0 0 0 26 0 V 80 Z" }));
      statisch.appendChild(n("path", { class: "s2", fill: "none", d: "M" + (GX - 16) + " 60 V 286 a 16 16 0 0 0 32 0 V 60" }));
      // Wasserpest
      var p = "M" + GX + " 296 C " + (GX - 4) + " 260, " + (GX + 4) + " 240, " + GX + " " + STIEL;
      statisch.appendChild(n("path", { class: "s k-gruen", "stroke-width": 3, fill: "none", d: p }));
      for (var k = 0; k < 7; k++) {
        var y = 290 - k * 11;
        statisch.appendChild(n("path", { class: "s2 f-gruen", d: "M" + GX + " " + y + " q -10 -2 -11 -9 q 8 1 11 7 z M " + GX + " " + y + " q 10 -2 11 -9 q -8 1 -11 7 z" }));
      }
      statisch.appendChild(hand(GX + 60, 230, "Wasserpest", 20));
      statisch.appendChild(n("path", { class: "s2", fill: "none", d: "M" + (GX + 58) + " 226 L " + (GX + 10) + " 250" }));
      statisch.appendChild(hand(GX + 60, 150, "Sauerstoff-", 20));
      statisch.appendChild(hand(GX + 60, 172, "bläschen", 20));
      statisch.appendChild(n("path", { class: "s2", fill: "none", d: "M" + (GX + 58) + " 152 L " + (GX + 8) + " 140" }));
      // Thermometer
      var T = +rTemp.value;
      statisch.appendChild(n("rect", { x: GX - 40, y: 130, width: 8, height: 150, rx: 4, class: "s2 f-weiss" }));
      statisch.appendChild(n("rect", { x: GX - 38, y: 278 - T * 3, width: 4, height: T * 3, class: "fo-thermo" }));
      statisch.appendChild(n("circle", { cx: GX - 36, cy: 284, r: 7, class: "s2 fo-thermo-k" }));
      bild.appendChild(statisch); bild.appendChild(blasenG);
    }
    function aktualisieren() {
      rate = berechne();
      document.getElementById("fo-abstand-t").textContent = rAbst.value + " cm";
      document.getElementById("fo-temp-t").textContent = rTemp.value + " °C";
      ausgabe.textContent = rate === 0 ? "Es steigen keine Bläschen auf." : "Etwa " + rate + " Bläschen pro Minute";
      aufbau();
      if (bewegungArm) {
        leeren(blasenG);
        for (var i = 0; i < Math.min(10, Math.round(rate / 6)); i++) blasenG.appendChild(n("circle", { cx: GX + (i % 2 ? 3 : -3), cy: STIEL - 10 - i * 13, r: 3, class: "s2 f-weiss" }));
      }
    }
    function schritt(zeitpunkt) {
      if (!letzte) letzte = zeitpunkt;
      var dt = Math.min(.1, (zeitpunkt - letzte) / 1000); letzte = zeitpunkt;
      if (rate > 0 && Math.random() < dt * rate / 60 * 3) blasen.push({ y: STIEL - 4, x: GX + (Math.random() - .5) * 4, r: 2.5 + Math.random() * 1.5 });
      leeren(blasenG);
      blasen = blasen.filter(function (b) { b.y -= dt * 60; b.x += Math.sin(b.y / 8) * .15; return b.y > 84; });
      blasen.forEach(function (b) { blasenG.appendChild(n("circle", { cx: b.x.toFixed(1), cy: b.y.toFixed(1), r: b.r.toFixed(1), class: "s2 f-weiss" })); });
      requestAnimationFrame(schritt);
    }
    [rAbst, rTemp].forEach(function (r) { r.addEventListener("input", aktualisieren); });
    dunkel.addEventListener("change", aktualisieren);
    knoepfe(box, "data-co2", function (v) { co2 = +v; aktualisieren(); });
    document.getElementById("fo-notieren").addEventListener("click", function () {
      if (tbody.children.length >= 15) tbody.removeChild(tbody.firstChild);
      nr++;
      var tr = document.createElement("tr");
      [nr, dunkel.checked ? "Lampe aus" : rAbst.value + " cm", rTemp.value + " °C", CO2NAME[String(co2)], rate].forEach(function (w) { var td = document.createElement("td"); td.textContent = w; tr.appendChild(td); });
      tbody.appendChild(tr);
    });
    document.getElementById("fo-leeren").addEventListener("click", function () { leeren(tbody); nr = 0; });
    aktualisieren();
    if (!bewegungArm) requestAnimationFrame(schritt);
    // Hinweis zur Zeitraffung
    ausgabe.setAttribute("title", "Die Bläschen in der Zeichnung steigen im Zeitraffer auf.");
  }

  /* =======================================================
     3) Nahrungsnetz
     ======================================================= */
  function netz() {
    var box = document.getElementById("nn"); if (!box) return;
    var D = JSON.parse(document.getElementById("nn-daten").textContent);
    var bild = document.getElementById("nn-bild"), titel = document.getElementById("nn-titel"), text = document.getElementById("nn-text");
    var weg = {}, PROD = { algen: 1, pflanzen: 1 };
    function beute(k) { return D.kanten.filter(function (e) { return e[1] === k; }).map(function (e) { return e[0]; }); }
    function feinde(k) { return D.kanten.filter(function (e) { return e[0] === k; }).map(function (e) { return e[1]; }); }
    function status() {
      var st = {}, k;
      for (k in D.knoten) st[k] = weg[k] ? "weg" : "normal";
      var geaendert = true;
      while (geaendert) {
        geaendert = false;
        for (k in D.knoten) {
          if (st[k] !== "normal" || PROD[k] || k === "destruenten") continue;
          var b = beute(k);
          if (b.length && b.every(function (x) { return st[x] === "weg" || st[x] === "tot"; })) { st[k] = "tot"; geaendert = true; }
        }
      }
      for (k in D.knoten) {
        if (st[k] !== "normal") continue;
        var verlorenB = beute(k).some(function (x) { return st[x] === "weg" || st[x] === "tot"; });
        var verlorenF = feinde(k).some(function (x) { return st[x] === "weg" || st[x] === "tot"; });
        if (PROD[k] && weg.destruenten) verlorenB = true;
        if (verlorenB) st[k] = "weniger"; else if (verlorenF) st[k] = "mehr";
      }
      return st;
    }
    var PLURAL = { algen: 1, pflanzen: 1, destruenten: 1 };
    function mz(liste) { return liste.length > 1 || PLURAL[liste[0]]; }
    function namen(liste) {
      var t = liste.map(function (k) { return D.knoten[k].name; });
      return t.length > 1 ? t.slice(0, -1).join(", ") + " und " + t[t.length - 1] : t[0];
    }
    function zeichne() {
      leeren(bild);
      var st = status();
      D.kanten.forEach(function (e) {
        var a = D.knoten[e[0]], b = D.knoten[e[1]];
        var dx = b.x - a.x, dy = b.y - a.y, l = Math.sqrt(dx * dx + dy * dy), ux = dx / l, uy = dy / l;
        var x1 = a.x + ux * 26, y1 = a.y + uy * 20, x2 = b.x - ux * 30, y2 = b.y - uy * 22;
        var aus = st[e[0]] === "weg" || st[e[0]] === "tot" || st[e[1]] === "weg" || st[e[1]] === "tot";
        var g = n("g", { class: aus ? "nn-kante aus" : "nn-kante" });
        g.appendChild(n("path", { class: "s2", fill: "none", d: "M" + x1.toFixed(1) + " " + y1.toFixed(1) + " L " + x2.toFixed(1) + " " + y2.toFixed(1) }));
        var w = Math.atan2(uy, ux);
        g.appendChild(n("path", { class: "s2", fill: "none", d: "M" + (x2 - 10 * Math.cos(w - .45)).toFixed(1) + " " + (y2 - 10 * Math.sin(w - .45)).toFixed(1) + " L " + x2.toFixed(1) + " " + y2.toFixed(1) + " L " + (x2 - 10 * Math.cos(w + .45)).toFixed(1) + " " + (y2 - 10 * Math.sin(w + .45)).toFixed(1) }));
        bild.appendChild(g);
      });
      [[40, "Konsumenten 3. Ordnung"], [125, "Konsumenten 2. Ordnung"], [215, "Konsumenten 1. Ordnung"], [300, "Produzenten"]].forEach(function (r) { bild.appendChild(hand(816, r[0], r[1], 16, "end")); });
      Object.keys(D.knoten).forEach(function (k) {
        var kn = D.knoten[k], w = Math.max(84, kn.name.length * 10);
        var g = n("g", { class: "nn-knoten " + st[k], tabindex: 0, role: "button", "aria-pressed": weg[k] ? "true" : "false", "aria-label": kn.name + (weg[k] ? " (entfernt)" : "") });
        g.appendChild(n("rect", { x: kn.x - w / 2, y: kn.y - 17, width: w, height: 34, rx: 17, class: "s " + kn.f }));
        g.appendChild(n("text", { x: kn.x, y: kn.y + 6, "text-anchor": "middle", class: "hk" }, kn.name));
        var zeichen = { weg: "✕", tot: "†", weniger: "↓", mehr: "↑" }[st[k]];
        if (zeichen) {
          g.appendChild(n("circle", { cx: kn.x + w / 2 - 2, cy: kn.y - 15, r: 11, class: "nn-marke" }));
          g.appendChild(n("text", { x: kn.x + w / 2 - 2, y: kn.y - 10, "text-anchor": "middle", class: "nn-marke-t" }, zeichen));
        }
        function umschalten() { weg[k] = !weg[k]; zeichne(); erklaeren(k); }
        g.addEventListener("click", umschalten);
        g.addEventListener("keydown", function (ev) { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); umschalten(); } });
        bild.appendChild(g);
      });
    }
    function erklaeren(k) {
      var st = status(), gruppe = function (s) { return Object.keys(st).filter(function (x) { return st[x] === s; }); };
      var w = gruppe("weg");
      if (!w.length) { titel.textContent = "Alle Arten sind da"; text.textContent = "Tippe auf eine Art, um sie zu entfernen."; return; }
      titel.textContent = "Entfernt: " + namen(w);
      var s = [], tot = gruppe("tot"), weniger = gruppe("weniger"), mehr = gruppe("mehr");
      if (tot.length) s.push(namen(tot) + " " + (mz(tot) ? "finden" : "findet") + " keine Nahrung mehr und " + (mz(tot) ? "verschwinden" : "verschwindet") + " ebenfalls.");
      if (weniger.length) s.push(namen(weniger) + " " + (mz(weniger) ? "verlieren" : "verliert") + " einen Teil der Nahrung und " + (mz(weniger) ? "werden" : "wird") + " wahrscheinlich seltener.");
      if (mehr.length) s.push(namen(mehr) + " " + (mz(mehr) ? "haben" : "hat") + " weniger Fressfeinde und " + (mz(mehr) ? "können" : "kann") + " sich stärker vermehren.");
      if (weg.destruenten) s.push("Ohne Destruenten wird totes Material nicht mehr zersetzt. Es fehlen Mineralstoffe, sodass die Produzenten schlechter wachsen. Am Grund sammelt sich Schlamm an.");
      if (!s.length) s.push("Die übrigen Arten können auf andere Nahrung ausweichen.");
      text.textContent = s.join(" ");
    }
    document.getElementById("nn-reset").addEventListener("click", function () { weg = {}; zeichne(); erklaeren(); });
    zeichne();
  }

  /* =======================================================
     4) Räuber und Beute
     ======================================================= */
  function rb() {
    var box = document.getElementById("rb"); if (!box) return;
    var bild = document.getElementById("rb-bild"), rV = document.getElementById("rb-vermehrung"), rJ = document.getElementById("rb-jagd");
    var start = document.getElementById("rb-start"), textE = document.getElementById("rb-text");
    var STUFE = ["gering", "eher gering", "mittel", "eher hoch", "hoch"];
    var A = [.35, .48, .6, .75, .9], B = [.012, .016, .02, .025, .03];
    var JAHRE = 40, X0 = 70, X1 = 740, Y0 = 36, Y1 = 300, YMAX = 1000;
    var ereignisse = [], gezeigt = JAHRE, timer = null, daten = [];
    function simuliere() {
      var a = A[rV.value - 1], b = B[rJ.value - 1], c = .1, d = .5;
      var x = 400, y = 20, h = .02, t = 0, out = [{ t: 0, b: x, r: y }], ev = ereignisse.slice().sort(function (p, q) { return p - q; }), ei = 0;
      function f(x, y) { return [a * x - b * x * y, c * b * x * y - d * y]; }
      while (t < JAHRE - 1e-9) {
        if (ei < ev.length && t >= ev[ei] - 1e-9) { y *= .5; ei++; }
        var k1 = f(x, y), k2 = f(x + h / 2 * k1[0], y + h / 2 * k1[1]), k3 = f(x + h / 2 * k2[0], y + h / 2 * k2[1]), k4 = f(x + h * k3[0], y + h * k3[1]);
        x += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); y += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]);
        t += h;
        if (Math.abs(t * 10 - Math.round(t * 10)) < 1e-6) out.push({ t: Math.round(t * 10) / 10, b: x, r: y });
      }
      daten = out;
    }
    function px(t) { return X0 + t / JAHRE * (X1 - X0); }
    function py(v) { return Y1 - Math.min(v, YMAX * 1.08) / YMAX * (Y1 - Y0); }
    function zeichne() {
      leeren(bild);
      bild.appendChild(n("rect", { x: X0, y: Y0, width: X1 - X0, height: Y1 - Y0, class: "s2 f-weiss" }));
      for (var v = 0; v <= YMAX; v += 250) {
        bild.appendChild(n("path", { class: "rb-gitter", d: "M" + X0 + " " + py(v) + " H " + X1 }));
        bild.appendChild(hand(X0 - 8, py(v) + 6, String(v), 15, "end"));
      }
      for (var j = 0; j <= JAHRE; j += 5) bild.appendChild(hand(px(j), Y1 + 22, String(j), 15, "middle"));
      bild.appendChild(hand((X0 + X1) / 2, Y1 + 46, "Jahre", 17, "middle"));
      bild.appendChild(hand(X0, Y0 - 10, "Anzahl", 16));
      ereignisse.forEach(function (e) {
        if (e > gezeigt) return;
        bild.appendChild(n("path", { class: "s2 gestrichelt", d: "M" + px(e) + " " + Y0 + " V " + Y1 }));
        bild.appendChild(hand(px(e) + 4, Y0 + 18, "Angler", 15));
      });
      var sb = "", sr = "", last = null;
      daten.forEach(function (p, i) {
        if (p.t > gezeigt + 1e-9) return;
        sb += (i ? " L " : "M") + px(p.t).toFixed(1) + " " + py(p.b).toFixed(1);
        sr += (i ? " L " : "M") + px(p.t).toFixed(1) + " " + py(p.r * 10).toFixed(1);
        last = p;
      });
      bild.appendChild(n("path", { d: sb, fill: "none", class: "rb-beute" }));
      bild.appendChild(n("path", { d: sr, fill: "none", class: "rb-raeuber" }));
      if (last) {
        bild.appendChild(n("circle", { cx: px(last.t), cy: py(last.b), r: 5, class: "rb-punkt-b" }));
        bild.appendChild(n("circle", { cx: px(last.t), cy: py(last.r * 10), r: 5, class: "rb-punkt-r" }));
        textE.textContent = "Jahr " + zahl(Math.floor(last.t), 0) + ": etwa " + zahl(Math.round(last.b / 10) * 10, 0) + " Rotaugen und " + zahl(Math.round(last.r), 0) + " Hechte.";
      }
      document.getElementById("rb-vermehrung-t").textContent = STUFE[rV.value - 1];
      document.getElementById("rb-jagd-t").textContent = STUFE[rJ.value - 1];
    }
    function stopp() { if (timer) { clearInterval(timer); timer = null; } start.textContent = "Abspielen"; }
    function abspielen() {
      if (timer) { stopp(); return; }
      if (gezeigt >= JAHRE) gezeigt = 0;
      start.textContent = "Anhalten";
      if (bewegungArm) { gezeigt = JAHRE; zeichne(); stopp(); return; }
      timer = setInterval(function () { gezeigt = Math.min(JAHRE, gezeigt + .2); zeichne(); if (gezeigt >= JAHRE) stopp(); }, 40);
    }
    start.addEventListener("click", abspielen);
    [rV, rJ].forEach(function (r) { r.addEventListener("input", function () { simuliere(); zeichne(); }); });
    document.getElementById("rb-angeln").addEventListener("click", function () {
      var t = (gezeigt > 0 && gezeigt < JAHRE) ? Math.round(gezeigt * 10) / 10 : 15;
      if (ereignisse.indexOf(t) < 0) ereignisse.push(t);
      simuliere(); zeichne();
    });
    document.getElementById("rb-reset").addEventListener("click", function () { stopp(); ereignisse = []; rV.value = 3; rJ.value = 3; gezeigt = JAHRE; simuliere(); zeichne(); });
    simuliere(); zeichne();
  }

  see(); foto(); netz(); rb();
})();
