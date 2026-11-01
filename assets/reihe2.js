/* =========================================================
   Modelle der Reihe 2: Zyklus, Schwangerschaft, Verhütung
   ========================================================= */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  function n(tag, a, txt) { var e = document.createElementNS(NS, tag); for (var k in a) e.setAttribute(k, a[k]); if (txt != null) e.textContent = txt; return e; }
  function leeren(e) { while (e.firstChild) e.removeChild(e.firstChild); }
  function zahl(x, s) { return x.toLocaleString("de-DE", { maximumFractionDigits: s == null ? 1 : s }); }
  var bewegungArm = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* =======================================================
     1) Menstruationszyklus
     ======================================================= */
  function zyklus() {
    var box = document.getElementById("zy"); if (!box) return;
    var H = {
      fsh: [.45, .5, .55, .55, .52, .48, .42, .38, .35, .33, .33, .38, .6, .55, .3, .25, .22, .2, .2, .2, .2, .2, .22, .25, .3, .35, .4, .42],
      lh: [.18, .18, .18, .18, .18, .18, .18, .2, .2, .22, .25, .35, .85, 1, .35, .2, .18, .16, .15, .15, .15, .15, .15, .15, .16, .17, .18, .18],
      oes: [.15, .15, .17, .2, .25, .3, .38, .48, .6, .75, .9, 1, .9, .55, .35, .35, .42, .5, .56, .6, .6, .58, .52, .45, .36, .28, .2, .16],
      pro: [.03, .03, .03, .03, .03, .03, .03, .03, .03, .03, .04, .05, .07, .1, .25, .45, .65, .82, .93, 1, 1, .95, .85, .7, .5, .3, .14, .06]
    };
    var NAMEN = { fsh: "FSH", lh: "LH", oes: "Östrogen", pro: "Progesteron" };
    var FARBE = { fsh: "var(--bernstein)", lh: "var(--malachit)", oes: "var(--eosin)", pro: "var(--methylenblau)" };
    var tag = 1, schwanger = false, timer = null;
    var bild = document.getElementById("zy-bild"), regler = document.getElementById("zy-tag"), tagText = document.getElementById("zy-tagtext");
    var titel = document.getElementById("zy-titel"), text = document.getElementById("zy-text"), play = document.getElementById("zy-play"), sw = document.getElementById("zy-schwanger");

    function wert(h, t) {
      var v = H[h][t - 1];
      if (schwanger && t >= 21) v = { fsh: .15, lh: .12, oes: .65, pro: 1 }[h];
      return v;
    }
    function schleimhaut(t) {
      if (schwanger && t >= 21) return 1;
      if (t <= 5) return .9 - (t - 1) * .17;
      if (t <= 14) return .22 + (t - 5) * .045;
      if (t <= 21) return .62 + (t - 14) * .054;
      if (t <= 26) return 1;
      return 1 - (t - 26) * .06;
    }
    function phase(t) {
      if (schwanger && t >= 21) return ["Schwangerschaft: keine Menstruation", "Die befruchtete Eizelle hat sich um Tag 20–21 in der Gebärmutterschleimhaut eingenistet. Ihre Zellen bilden das Hormon hCG. Es sorgt dafür, dass der Gelbkörper erhalten bleibt und weiter Progesteron bildet. Die Schleimhaut bleibt bestehen, eine Menstruation setzt nicht ein. Das viele Progesteron hemmt FSH und LH: Es reift kein neuer Follikel heran."];
      if (t <= 5) return ["Menstruation", "Die obere Schicht der Gebärmutterschleimhaut löst sich ab und fließt mit etwas Blut ab, weil Östrogen und Progesteron am Ende des letzten Zyklus stark gesunken sind. Gleichzeitig steigt FSH an: Im Eierstock beginnen neue Follikel zu wachsen."];
      if (t <= 12) return ["Follikelreifung", "FSH aus der Hirnanhangdrüse lässt einen Follikel im Eierstock heranreifen. Der wachsende Follikel bildet immer mehr Östrogen. Östrogen baut die Gebärmutterschleimhaut wieder auf."];
      if (t <= 14) return ["Eisprung", "Sehr viel Östrogen bewirkt, dass die Hirnanhangdrüse kurz und stark LH ausschüttet (positive Rückkopplung). Der LH-Gipfel löst den Eisprung aus: Der reife Follikel platzt und gibt die Eizelle frei. Sie ist jetzt etwa einen Tag lang befruchtungsfähig."];
      if (t <= 24) return ["Gelbkörperphase", "Aus dem leeren Follikel wird der Gelbkörper. Er bildet Progesteron und etwas Östrogen. Progesteron lässt die Schleimhaut weiter wachsen und gut durchbluten, damit sich eine befruchtete Eizelle einnisten könnte. Gleichzeitig hemmt es FSH und LH (negative Rückkopplung): Es reift kein neuer Follikel."];
      return ["Ende des Zyklus", "Die Eizelle wurde nicht befruchtet. Der Gelbkörper geht zugrunde, Progesteron und Östrogen sinken. Dadurch fällt die Hemmung weg: FSH steigt wieder an. Ohne Progesteron kann die Schleimhaut nicht bestehen bleiben, in wenigen Tagen beginnt die nächste Menstruation."];
    }

    function zeichne() {
      leeren(bild);
      var g = n("g", { "font-family": "Caveat, cursive", "font-weight": "700", fill: "currentColor" });
      bild.appendChild(g);
      // ---- Eierstock
      g.appendChild(n("text", { x: 20, y: 30, "font-size": 22 }, "Eierstock"));
      g.appendChild(n("ellipse", { cx: 190, cy: 100, rx: 150, ry: 62, class: "s f-gelb" }));
      [[90, 80, 7], [110, 130, 6], [250, 70, 6], [280, 120, 7], [140, 64, 5]].forEach(function (f) { g.appendChild(n("circle", { cx: f[0], cy: f[1], r: f[2], class: "s2 f-weiss" })); });
      var fx = 190, fy = 100;
      if (tag <= 13) {
        var r = 8 + tag * 2.6;
        g.appendChild(n("circle", { cx: fx, cy: fy, r: r, class: "s f-weiss" }));
        g.appendChild(n("circle", { cx: fx + r * .35, cy: fy - r * .2, r: Math.max(4, r * .28), class: "s2 f-rosa" }));
        g.appendChild(n("text", { x: fx, y: fy + r + 22, "text-anchor": "middle", "font-size": 18 }, "Follikel mit Eizelle"));
      } else if (tag === 14) {
        g.appendChild(n("path", { d: "M160 70 Q 190 50 220 70 L 240 60 L 214 92 Q 190 112 166 92 L 140 60 Z", class: "s f-weiss" }));
        g.appendChild(n("circle", { cx: 300, cy: 44, r: 11, class: "s f-rosa" }));
        g.appendChild(n("path", { d: "M222 72 Q 260 46 286 44", class: "s2", fill: "none" }));
        g.appendChild(n("text", { x: 310, y: 30, "font-size": 18 }, "Eisprung!"));
      } else {
        var gelb = schwanger && tag >= 21 ? 1 : (tag <= 23 ? 1 : 1 - (tag - 23) * .16);
        var rg = 22 + 18 * gelb;
        g.appendChild(n("circle", { cx: fx, cy: fy, r: rg, fill: gelb > .5 ? "#f2c94c" : "#efe6c4", class: "s" }));
        g.appendChild(n("text", { x: fx, y: fy + rg + 22, "text-anchor": "middle", "font-size": 18 }, gelb > .5 ? "Gelbkörper" : "Gelbkörper bildet sich zurück"));
      }
      // ---- Gebärmutterschleimhaut
      var oy = 262, d = schleimhaut(tag), sb = 180;
      g.appendChild(n("text", { x: 410, y: 30, "font-size": 22 }, "Gebärmutterschleimhaut"));
      g.appendChild(n("rect", { x: 380, y: sb, width: 360, height: 34, rx: 6, class: "s f-sand" }));
      g.appendChild(n("text", { x: 560, y: sb + 54, "text-anchor": "middle", "font-size": 16 }, "Muskelschicht der Gebärmutter"));
      var hoehe = 14 + d * 86, top = sb - hoehe;
      var welle = "M380 " + sb + " V " + top;
      for (var x = 380; x < 740; x += 20) welle += " Q " + (x + 10) + " " + (top - 6) + " " + (x + 20) + " " + top;
      welle += " V " + sb + " Z";
      g.appendChild(n("path", { d: welle, class: "s f-rosa" }));
      if (d > .5) for (var k = 0; k < 9; k++) g.appendChild(n("path", { d: "M" + (400 + k * 38) + " " + (sb - 4) + " q 6 " + (-hoehe * .4) + " 0 " + (-hoehe * .75), class: "s2 k-rosa", fill: "none" }));
      if (tag <= 5 && !(schwanger && tag >= 21)) for (var t2 = 0; t2 < 6; t2++) g.appendChild(n("path", { d: "M" + (420 + t2 * 52) + " " + (top - 26) + " c 5 7 8 11 8 15 a 8 8 0 0 1 -16 0 c 0 -4 3 -8 8 -15 z", fill: "#c9455f" }));
      if (schwanger && tag >= 21) g.appendChild(n("circle", { cx: 560, cy: top + 16, r: 13, class: "s f-gelb" }));
      // ---- Hormonkurven
      var L = 70, R = 740, O = oy + 30, U = oy + 230;
      g.appendChild(n("text", { x: 20, y: oy + 18, "font-size": 22 }, "Hormone im Blut"));
      g.appendChild(n("line", { x1: L, y1: U, x2: R, y2: U, class: "s2" }));
      g.appendChild(n("line", { x1: L, y1: O, x2: L, y2: U, class: "s2" }));
      function px(t) { return L + (t - 1) / 27 * (R - L); }
      [1, 7, 14, 21, 28].forEach(function (t) { g.appendChild(n("text", { x: px(t), y: U + 22, "text-anchor": "middle", "font-size": 16 }, "Tag " + t)); });
      g.appendChild(n("rect", { x: px(1), y: O, width: px(5) - px(1), height: U - O, fill: "rgba(201,69,95,.12)" }));
      ["fsh", "lh", "oes", "pro"].forEach(function (h) {
        var dd = "";
        for (var t = 1; t <= 28; t++) dd += (t === 1 ? "M" : " L") + px(t).toFixed(1) + " " + (U - wert(h, t) * (U - O - 10)).toFixed(1);
        g.appendChild(n("path", { d: dd, fill: "none", stroke: FARBE[h], "stroke-width": 3.5, "stroke-linejoin": "round" }));
      });
      g.appendChild(n("line", { x1: px(tag), y1: O - 6, x2: px(tag), y2: U, stroke: "currentColor", "stroke-width": 2, "stroke-dasharray": "5 5" }));
      ["fsh", "lh", "oes", "pro"].forEach(function (h) {
        g.appendChild(n("circle", { cx: px(tag), cy: U - wert(h, tag) * (U - O - 10), r: 6, fill: FARBE[h], stroke: "var(--flaeche)", "stroke-width": 2 }));
      });
      // Legende
      ["oes", "pro", "fsh", "lh"].forEach(function (h, i) {
        var lx = L + i * 170;
        g.appendChild(n("rect", { x: lx, y: U + 38, width: 22, height: 6, rx: 3, fill: FARBE[h] }));
        g.appendChild(n("text", { x: lx + 30, y: U + 46, "font-size": 18 }, NAMEN[h]));
      });
      var ph = phase(tag);
      titel.textContent = "Tag " + tag + ": " + ph[0];
      text.textContent = ph[1];
      tagText.textContent = "Tag " + tag;
      bild.setAttribute("aria-label", "Zyklus an Tag " + tag + ": " + ph[0] + ". " + ph[1]);
    }
    function setze(t) { tag = Math.max(1, Math.min(28, t)); regler.value = tag; zeichne(); }
    regler.addEventListener("input", function () { setze(+regler.value); });
    sw.addEventListener("change", function () { schwanger = sw.checked; zeichne(); });
    play.addEventListener("click", function () {
      if (timer) { clearInterval(timer); timer = null; play.textContent = "Abspielen"; return; }
      play.textContent = "Anhalten";
      timer = setInterval(function () { setze(tag >= 28 ? 1 : tag + 1); }, bewegungArm ? 1400 : 700);
    });
    zeichne();
  }

  /* =======================================================
     2) Schwangerschaft Woche für Woche
     ======================================================= */
  function schwangerschaft() {
    var box = document.getElementById("sw"); if (!box) return;
    // SSW, Länge cm, Gewicht g, Messart, Vergleich, Farbe, Form, Text
    var D = [
      [4, 0.1, 0, "ssl", "Mohnsamen", "#6b5b52", "k", "Die Zellkugel hat sich in der Gebärmutterschleimhaut eingenistet. Die Plazenta beginnt sich zu bilden. Viele Frauen wissen noch nicht, dass sie schwanger sind."],
      [5, 0.2, 0, "ssl", "Sesamkorn", "#e9d6a4", "e", "Das Neuralrohr entsteht, aus dem später Gehirn und Rückenmark werden."],
      [6, 0.5, 0, "ssl", "Linse", "#c98a4a", "k", "Das Herz beginnt zu schlagen. Im Ultraschall sieht man ein kleines Flackern."],
      [8, 1.6, 1, "ssl", "Himbeere", "#d94a63", "k", "Arme und Beine wachsen, Finger bilden sich. Alle wichtigen Organe werden angelegt. Gerade jetzt ist der Embryo sehr empfindlich gegenüber Alkohol, Nikotin und Medikamenten."],
      [10, 3, 4, "ssl", "Erdbeere", "#e0473f", "k", "Alle Organe sind angelegt. Ab jetzt spricht man vom Fetus. Er sieht schon wie ein kleiner Mensch aus."],
      [12, 6, 15, "ssl", "Limette", "#8cc152", "k", "Der Fetus bewegt sich, streckt sich und kann am Daumen nuckeln. Die Mutter spürt davon noch nichts."],
      [16, 12, 100, "ssl", "Avocado", "#5f8a3a", "e", "Die Muskeln werden kräftiger. Im Ultraschall kann man oft das Geschlecht erkennen."],
      [20, 25, 300, "ges", "Banane", "#f2d34f", "b", "Die Mutter spürt erste Bewegungen. Der Fetus kann Geräusche wahrnehmen, zum Beispiel den Herzschlag und die Stimme der Mutter. Ab jetzt wird die Gesamtlänge angegeben."],
      [24, 30, 600, "ges", "Maiskolben", "#f0c040", "e", "Ab jetzt kann ein zu früh geborenes Kind mit intensiver medizinischer Hilfe überleben. Die Lunge ist aber noch lange nicht reif."],
      [28, 37, 1000, "ges", "Aubergine", "#6a3f7a", "e", "Die Augen öffnen sich. Der Fetus schläft und wacht in einem eigenen Rhythmus."],
      [32, 42, 1700, "ges", "Ananas", "#d9a641", "e", "Der Fetus legt Fettpolster an und nimmt jetzt schnell zu. Es wird enger in der Gebärmutter."],
      [36, 47, 2600, "ges", "Honigmelone", "#e8d77a", "k", "Die Lunge ist fast ausgereift. Meist dreht sich der Fetus mit dem Kopf nach unten."],
      [40, 50, 3400, "ges", "Wassermelone", "#4f8a3a", "k", "Das Kind ist bereit für die Geburt. Um die 40. Woche kommen viele Kinder zur Welt, normal ist der Zeitraum von der 37. bis zur 42. Woche."]
    ];
    var regler = document.getElementById("sw-woche"), bild = document.getElementById("sw-bild");
    var el = { woche: document.getElementById("sw-wochetext"), titel: document.getElementById("sw-titel"), text: document.getElementById("sw-text"), werte: document.getElementById("sw-werte") };

    function daten(w) {
      var a = D[0], b = D[D.length - 1];
      for (var i = 0; i < D.length; i++) { if (D[i][0] <= w) a = D[i]; if (D[i][0] >= w) { b = D[i]; break; } }
      var f = b[0] === a[0] ? 0 : (w - a[0]) / (b[0] - a[0]);
      return { a: a, b: b, laenge: a[1] + (b[1] - a[1]) * f, gewicht: a[2] + (b[2] - a[2]) * f, nah: f < .5 ? a : b };
    }
    function fetus(g, x, y, s, frueh) {
      // stilisierter Embryo/Fetus, Größe s = Gesamthöhe in px
      var k = s / 100;
      var t = n("g", { transform: "translate(" + x + " " + y + ") scale(" + k + ")" });
      if (frueh) {
        t.appendChild(n("path", { d: "M-6 -40 C 30 -50, 44 -10, 30 22 C 18 46, -14 50, -18 30 C -22 18, -10 14, -4 20 C 8 10, 6 -12, -10 -16 C -30 -20, -34 -36, -6 -40 Z", class: "s f-sand" }));
        t.appendChild(n("circle", { cx: 6, cy: -28, r: 3.5, class: "d" }));
      } else {
        // gekrümmter Rücken, angezogene Beine, großer Kopf
        t.appendChild(n("path", { d: "M-22 -18 C -44 0, -42 38, -14 50 C 8 58, 34 50, 38 32 C 42 16, 30 4, 18 6 C 22 -6, 12 -16, 0 -14 Z", class: "s f-sand" }));
        t.appendChild(n("path", { d: "M36 30 C 30 22, 18 22, 12 30 C 8 36, 14 44, 22 42", class: "s2", fill: "none" }));
        t.appendChild(n("path", { d: "M2 8 C 10 14, 14 20, 10 28", class: "s2", fill: "none" }));
        t.appendChild(n("circle", { cx: 2, cy: -34, r: 26, class: "s f-sand" }));
        t.appendChild(n("path", { d: "M16 -40 q 5 3 1 9", class: "s2", fill: "none" }));
        t.appendChild(n("circle", { cx: 12, cy: -40, r: 2.5, class: "d" }));
        t.appendChild(n("path", { d: "M-6 42 C -30 60, -60 40, -90 50", class: "s2", fill: "none", "stroke-width": 4 }));
      }
      g.appendChild(t);
    }
    function zeichne() {
      var w = +regler.value, d = daten(w);
      leeren(bild);
      var g = n("g", { "font-family": "Caveat, cursive", "font-weight": "700", fill: "currentColor" });
      bild.appendChild(g);
      // Fruchtblase
      g.appendChild(n("circle", { cx: 190, cy: 190, r: 160, class: "s f-rosa-weich" }));
      g.appendChild(n("circle", { cx: 190, cy: 190, r: 150, class: "s2 f-blau-weich", opacity: ".7" }));
      // Maßstab: 50 cm = 270 px in der großen Ansicht
      var px = d.laenge / 50 * 270, lupe = d.laenge < 5;
      // zusammengerollt ist der Fetus etwa halb so hoch wie seine gestreckte Länge
      if (!lupe) fetus(g, 196, 196, px * 0.55, false);
      else {
        g.appendChild(n("circle", { cx: 190, cy: 196, r: Math.max(1.5, px / 2), class: "s2 f-sand" }));
        // Lupe
        g.appendChild(n("circle", { cx: 300, cy: 300, r: 70, class: "s f-weiss" }));
        var faktoren = [5, 10, 20, 50, 100, 200, 500], fak = faktoren[0];
        faktoren.forEach(function (f) { if (px * f <= 110) fak = f; });
        fetus(g, 300, 304, px * fak * (w < 10 ? 1 : 0.55), w < 10);
        g.appendChild(n("path", { d: "M196 200 L 248 252", class: "s2", "stroke-dasharray": "4 4", fill: "none" }));
        g.appendChild(n("text", { x: 300, y: 392, "text-anchor": "middle", "font-size": 18 }, fak + "-fach vergrößert"));
      }
      // Lineal
      var ly = 400, l0 = 20, l1 = 20 + 270 * 55 / 50;
      g.appendChild(n("rect", { x: l0 - 8, y: ly - 4, width: l1 - l0 + 16, height: 34, rx: 4, class: "s f-sand" }));
      for (var c = 0; c <= 55; c++) {
        var xx = l0 + c / 50 * 270;
        g.appendChild(n("line", { x1: xx, y1: ly - 4, x2: xx, y2: ly - 4 + (c % 10 === 0 ? 14 : c % 5 === 0 ? 10 : 5), class: "s2" }));
        if (c % 10 === 0) g.appendChild(n("text", { x: xx, y: ly + 26, "text-anchor": "middle", "font-size": 14 }, c + (c === 50 ? " cm" : "")));
      }
      g.appendChild(n("rect", { x: l0, y: ly - 16, width: Math.max(2, px), height: 8, rx: 3, fill: "var(--eosin)" }));
      g.appendChild(n("text", { x: 18, y: 448, "font-size": 16 }, "Der rote Balken zeigt, wie lang das Kind gestreckt wäre."));
      // Vergleichsobjekt
      var v = d.nah, vx = 560, vy = 170, vr = Math.max(2, Math.min(150, d.laenge / 50 * 270 / 2 * 1.6));
      g.appendChild(n("text", { x: vx, y: 40, "text-anchor": "middle", "font-size": 22 }, "so groß wie eine " + v[4]));
      var form = v[6], vk;
      if (form === "k") vk = n("circle", { cx: vx, cy: vy, r: vr / 1.6, fill: v[5], class: "s" });
      else if (form === "b") vk = n("path", { d: "M" + (vx - vr) + " " + (vy + 10) + " Q " + vx + " " + (vy + vr * .9) + " " + (vx + vr) + " " + (vy - vr * .4) + " Q " + vx + " " + (vy + vr * .5) + " " + (vx - vr) + " " + (vy + 10) + " Z", fill: v[5], class: "s" });
      else vk = n("ellipse", { cx: vx, cy: vy, rx: vr / 1.4, ry: vr / 2.2, fill: v[5], class: "s" });
      g.appendChild(vk);
      // Zeitleiste
      var tl = 470, t0 = 400, t1 = 720;
      g.appendChild(n("line", { x1: t0, y1: tl, x2: t1, y2: tl, class: "s" }));
      [[4, "4"], [12, "12"], [20, "20"], [28, "28"], [40, "40. SSW"]].forEach(function (p) { var xx = t0 + (p[0] - 4) / 36 * (t1 - t0); g.appendChild(n("line", { x1: xx, y1: tl - 6, x2: xx, y2: tl + 6, class: "s2" })); g.appendChild(n("text", { x: xx, y: tl + 24, "text-anchor": "middle", "font-size": 15 }, p[1])); });
      [[4, 13, "1. Drittel"], [14, 27, "2. Drittel"], [28, 40, "3. Drittel"]].forEach(function (p) {
        var a = t0 + (p[0] - 4) / 36 * (t1 - t0), b = t0 + (p[1] - 4) / 36 * (t1 - t0);
        g.appendChild(n("text", { x: (a + b) / 2, y: tl - 14, "text-anchor": "middle", "font-size": 15 }, p[2]));
      });
      g.appendChild(n("circle", { cx: t0 + (w - 4) / 36 * (t1 - t0), cy: tl, r: 9, fill: "var(--eosin)", stroke: "var(--flaeche)", "stroke-width": 2 }));

      var nahText = D.filter(function (x) { return x[0] <= w; }).pop();
      el.woche.textContent = w + ". SSW";
      el.titel.textContent = w + ". Schwangerschaftswoche" + (w <= 10 ? " (Embryo)" : " (Fetus)");
      el.text.textContent = nahText[7];
      var mass = d.laenge < 1 ? zahl(d.laenge * 10) + " mm" : zahl(d.laenge, d.laenge < 10 ? 1 : 0) + " cm";
      var art = (d.laenge < 20 && w < 20) ? "Scheitel-Steiß-Länge" : "Gesamtlänge";
      var gew = d.gewicht < 1 ? "unter 1 g" : d.gewicht < 1000 ? zahl(d.gewicht, 0) + " g" : zahl(d.gewicht / 1000, 1) + " kg";
      el.werte.textContent = "Länge: etwa " + mass + " (" + art + ") · Gewicht: " + (d.gewicht < 1 ? "unter 1 g" : "etwa " + gew);
      bild.setAttribute("aria-label", w + ". Schwangerschaftswoche: " + el.werte.textContent + ", etwa so groß wie eine " + v[4] + ". " + nahText[7]);
    }
    regler.addEventListener("input", zeichne);
    zeichne();
  }

  /* =======================================================
     3) Verhütung im Vergleich
     ======================================================= */
  function verhuetung() {
    var box = document.getElementById("vh"); if (!box) return;
    var M = {
      keine: { name: "keine Verhütung", min: 85, max: 85, hormone: "–", rezept: "–", sti: false, text: "Ohne Verhütung werden innerhalb eines Jahres etwa 85 von 100 Frauen schwanger, die regelmäßig Geschlechtsverkehr haben.", plus: "", minus: "" },
      kondom: { name: "Kondom", min: 2, max: 12, hormone: "nein", rezept: "nein", sti: true, text: "Eine dünne Hülle aus Latex oder einem anderen Material wird vor dem Geschlechtsverkehr über den steifen Penis gerollt und fängt das Sperma auf.", plus: "einzige Methode, die auch vor sexuell übertragbaren Infektionen schützt; ohne Hormone; überall erhältlich", minus: "kann reißen oder abrutschen, wenn es falsch angewendet wird oder nicht passt; Verfallsdatum beachten" },
      pille: { name: "Pille", min: 0.1, max: 0.9, hormone: "ja", rezept: "ja", sti: false, text: "Eine Tablette mit Hormonen, die täglich zur gleichen Zeit eingenommen wird. Sie verhindert den Eisprung, ähnlich wie das Progesteron in der Gelbkörperphase.", plus: "sehr sicher bei richtiger Anwendung", minus: "Einnahme darf nicht vergessen werden; Erbrechen, Durchfall und manche Medikamente können die Wirkung aufheben; mögliche Nebenwirkungen" },
      ring: { name: "Vaginalring", min: 0.4, max: 0.65, hormone: "ja", rezept: "ja", sti: false, text: "Ein weicher Ring gibt Hormone ab. Er wird selbst in die Scheide eingesetzt, bleibt drei Wochen dort und wird dann für eine Woche entfernt.", plus: "man muss nicht täglich daran denken", minus: "mögliche Nebenwirkungen wie bei der Pille" },
      implantat: { name: "Hormonimplantat", min: 0, max: 0.08, hormone: "ja", rezept: "ja", sti: false, text: "Ein streichholzgroßes Stäbchen wird unter die Haut des Oberarms gesetzt und gibt bis zu drei Jahre lang Hormone ab.", plus: "eine der sichersten Methoden; kein Anwendungsfehler möglich", minus: "muss ärztlich eingesetzt und entfernt werden; häufig unregelmäßige Blutungen" },
      hspirale: { name: "Hormonspirale", min: 0.16, max: 0.16, hormone: "ja", rezept: "ja", sti: false, text: "Ein kleiner T-förmiger Körper wird von der Frauenärztin in die Gebärmutter eingesetzt und gibt dort mehrere Jahre lang wenig Hormon ab.", plus: "sehr sicher über mehrere Jahre", minus: "Einsetzen kann unangenehm sein; muss ärztlich eingesetzt werden" },
      kspirale: { name: "Kupferspirale", min: 0.3, max: 0.8, hormone: "nein", rezept: "ja", sti: false, text: "Ein kleiner Körper mit Kupferdraht in der Gebärmutter. Das Kupfer hemmt die Spermienzellen und verhindert die Einnistung.", plus: "sehr sicher, ohne Hormone, hält mehrere Jahre", minus: "Menstruation kann stärker und schmerzhafter werden" },
      diaphragma: { name: "Diaphragma", min: 1, max: 20, hormone: "nein", rezept: "nein", sti: false, text: "Eine weiche Kappe wird vor dem Geschlechtsverkehr zusammen mit einem spermienhemmenden Gel vor den Muttermund gesetzt.", plus: "ohne Hormone, wiederverwendbar", minus: "Anwendung muss geübt werden; deutlich weniger sicher bei Fehlern" },
      nfp: { name: "Natürliche Familienplanung", min: 0.4, max: 1.8, hormone: "nein", rezept: "nein", sti: false, text: "Die fruchtbaren Tage werden täglich bestimmt, zum Beispiel über die Körpertemperatur nach dem Aufwachen und den Schleim am Muttermund. An diesen Tagen wird auf Geschlechtsverkehr verzichtet oder zusätzlich verhütet.", plus: "ohne Hormone; man lernt den eigenen Körper kennen", minus: "nur bei sehr genauer Anwendung und regelmäßigem Zyklus sicher; für Jugendliche wegen schwankender Zyklen ungeeignet. Bei Fehlern liegt die Zahl deutlich höher, als hier gezeigt." },
      aufpassen: { name: "„Aufpassen“", min: 4, max: 18, hormone: "nein", rezept: "nein", sti: false, text: "Der Penis wird vor dem Samenerguss aus der Scheide gezogen. Das ist keine sichere Methode, denn schon vorher können Spermienzellen austreten.", plus: "–", minus: "sehr unsicher; nicht zur Verhütung geeignet" }
    };
    var wahl = "kondom";
    var raster = document.getElementById("vh-raster"), info = document.getElementById("vh-info"), zahlEl = document.getElementById("vh-zahl");
    function zeichne() {
      var m = M[wahl];
      leeren(raster);
      var spalten = 40, zeilen = 25, a = 17;
      var nMin = Math.round(m.min * 10), nMax = Math.round(m.max * 10);
      var g = n("g", {});
      for (var i = 0; i < 1000; i++) {
        var x = 10 + (i % spalten) * a, y = 10 + Math.floor(i / spalten) * a;
        var cls = i < nMin ? "vh-p voll" : i < nMax ? "vh-p teil" : "vh-p";
        g.appendChild(n("circle", { cx: x, cy: y, r: 6, class: cls }));
      }
      raster.appendChild(g);
      function wort(z) { return zahl(z / 10, 1).replace(/,0$/, ""); }
      var txt = m.min === m.max ? "Etwa " + zahl(nMin, 0) + " von 1000 Frauen (" + wort(nMin) + " von 100) werden innerhalb eines Jahres schwanger."
        : "Zwischen " + zahl(nMin, 0) + " und " + zahl(nMax, 0) + " von 1000 Frauen (" + wort(nMin) + " bis " + wort(nMax) + " von 100) werden innerhalb eines Jahres schwanger.";
      if (nMax <= 1) txt = "Höchstens etwa 1 von 1000 Frauen wird innerhalb eines Jahres schwanger.";
      zahlEl.textContent = txt;
      info.innerHTML = "";
      function zeile(t, w) { var dt = document.createElement("dt"); dt.textContent = t; var dd = document.createElement("dd"); dd.textContent = w; info.appendChild(dt); info.appendChild(dd); }
      zeile("So funktioniert es", m.text);
      zeile("Pearl-Index", m.min === m.max ? zahl(m.min, 2) : zahl(m.min, 2) + " bis " + zahl(m.max, 2));
      zeile("Mit Hormonen", m.hormone);
      zeile("Ärztliches Rezept nötig", m.rezept);
      zeile("Schützt vor Infektionen", m.sti ? "ja" : "nein");
      if (m.plus) zeile("Vorteile", m.plus);
      if (m.minus) zeile("Nachteile", m.minus);
      raster.setAttribute("aria-label", m.name + ": " + txt);
      box.querySelectorAll("[data-methode]").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-methode") === wahl ? "true" : "false"); });
    }
    box.addEventListener("click", function (e) { var b = e.target.closest("[data-methode]"); if (b) { wahl = b.getAttribute("data-methode"); zeichne(); } });
    zeichne();
  }

  function start() { zyklus(); schwangerschaft(); verhuetung(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
