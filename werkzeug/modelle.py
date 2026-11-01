"""Interaktive Modelle der Reihe 1 (jeweils mit eigenem kleinen Skript)."""

SCHLUESSEL_SCHLOSS = r"""
<p class="lead">Jeder Erreger trägt an seiner Oberfläche ganz bestimmte Merkmale, die <span class="fachwort">Antigene</span>. Nur ein Antikörper mit der passenden Form kann daran binden. Probiere es aus.</p>

<div class="modell" id="ss">
  <svg viewBox="0 0 640 380" role="img" aria-labelledby="ss-t" id="ss-bild">
    <title id="ss-t">Ein Erreger mit Antigenen in der Mitte und die Antikörper, die du ausgewählt hast</title>
    <g id="ss-szene"></g>
  </svg>
  <p class="rueckmeldung" id="ss-meldung" aria-live="polite">Wähle unten einen Antikörper aus.</p>
  <div class="modell-steuerung" role="group" aria-label="Antikörper auswählen">
    <button class="knopf leise" type="button" data-form="dreieck">Antikörper A</button>
    <button class="knopf leise" type="button" data-form="kreis">Antikörper B</button>
    <button class="knopf leise" type="button" data-form="quadrat">Antikörper C</button>
  </div>
  <div class="modell-steuerung">
    <button class="knopf" type="button" id="ss-neu">Neuer Erreger</button>
  </div>
  <p id="ss-gedaechtnis" class="legende" aria-live="polite">Gedächtniszellen: noch keine</p>
</div>

<h2>Was das Modell zeigt</h2>
<ul>
  <li>Die Antigene des Erregers und die Bindungsstelle des Antikörpers passen zueinander wie Schloss und Schlüssel.</li>
  <li>Passt ein Antikörper, heften sich viele davon an den Erreger. So werden Erreger verklumpt und können von Fresszellen beseitigt werden.</li>
  <li>Hat der Körper einen Erreger schon einmal bekämpft, „kennen“ ihn die Gedächtniszellen. Kommt er wieder, werden sofort die passenden Antikörper gebildet.</li>
</ul>
<h3>Grenzen des Modells</h3>
<p>Echte Antigene und Antikörper sind Eiweißmoleküle mit komplizierter räumlicher Form, keine Dreiecke oder Kreise. Außerdem probiert der Körper nicht nacheinander verschiedene Antikörper aus: Unter Millionen verschiedener B-Zellen werden genau die aktiviert, deren Antikörper zufällig passen.</p>

<script>
(function () {
  var ns = "http://www.w3.org/2000/svg";
  var szene = document.getElementById("ss-szene");
  var meldung = document.getElementById("ss-meldung");
  var gedText = document.getElementById("ss-gedaechtnis");
  var knoepfe = document.querySelectorAll("#ss [data-form]");
  var formen = ["dreieck", "kreis", "quadrat"];
  var namen = { dreieck: "Erreger 1", kreis: "Erreger 2", quadrat: "Erreger 3" };
  var gedaechtnis = {};
  var erreger, gebunden;
  var cx = 320, cy = 190, r = 55;

  function neu(tag, attrs) { var e = document.createElementNS(ns, tag); for (var k in attrs) e.setAttribute(k, attrs[k]); return e; }

  // Form einer Bindungsstelle (Antigen = Vorsprung) an Position (x,y), gedreht um winkel
  function antigen(form, x, y, winkel, farbe) {
    var g = neu("g", { transform: "translate(" + x + " " + y + ") rotate(" + winkel + ")" });
    g.appendChild(neu("line", { x1: 0, y1: 0, x2: 0, y2: -14, stroke: "currentColor", "stroke-width": 3 }));
    var s;
    if (form === "dreieck") s = neu("polygon", { points: "-9,-14 9,-14 0,-28" });
    else if (form === "kreis") s = neu("circle", { cx: 0, cy: -22, r: 9 });
    else s = neu("rect", { x: -8, y: -30, width: 16, height: 16 });
    s.setAttribute("fill", farbe); s.setAttribute("stroke", "currentColor"); s.setAttribute("stroke-width", 1.5);
    g.appendChild(s); return g;
  }

  // Y-förmiger Antikörper im Koordinatensystem eines Antigens (außen = negative y-Richtung).
  // Die linke Bindungsstelle sitzt genau über dem Antigen.
  function antikoerper(form, farbe) {
    var g = neu("g", { class: "ak" });
    var linie = { fill: "none", stroke: farbe, "stroke-width": 5, "stroke-linecap": "round", "stroke-linejoin": "round" };
    function stelle(x) {
      var e;
      if (form === "dreieck") e = neu("polyline", { points: (x - 12) + ",-12 " + x + ",-33 " + (x + 12) + ",-12" });
      else if (form === "kreis") e = neu("path", { d: "M" + (x - 13) + " -20 A 13 13 0 0 1 " + (x + 13) + " -20" });
      else e = neu("polyline", { points: (x - 11) + ",-12 " + (x - 11) + ",-33 " + (x + 11) + ",-33 " + (x + 11) + ",-12" });
      for (var k in linie) e.setAttribute(k, linie[k]);
      return e;
    }
    g.appendChild(neu("path", Object.assign({ d: "M0 -33 L20 -58 L40 -33 M20 -58 L20 -88" }, linie)));
    g.appendChild(stelle(0)); g.appendChild(stelle(40));
    return g;
  }

  function zeichne(gewaehlt) {
    while (szene.firstChild) szene.removeChild(szene.firstChild);
    var farbeE = "var(--eosin)", farbeA = "var(--methylenblau)";
    szene.appendChild(neu("circle", { cx: cx, cy: cy, r: r, fill: "color-mix(in srgb, var(--eosin) 14%, transparent)", stroke: farbeE, "stroke-width": 3 }));
    var t = neu("text", { x: cx, y: cy + 5, "text-anchor": "middle", "font-family": "Atkinson Hyperlegible, sans-serif", "font-size": 15, fill: "currentColor" });
    t.textContent = namen[erreger]; szene.appendChild(t);
    var passt = gewaehlt === erreger;
    for (var i = 0; i < 6; i++) {
      var w = i * 60;
      var rad = (w - 90) * Math.PI / 180;
      var x = cx + Math.cos(rad) * r, y = cy + Math.sin(rad) * r;
      szene.appendChild(antigen(erreger, x, y, w, farbeE));
      if (gewaehlt && (passt || i === 0 || i === 3)) {
        var ak = antikoerper(gewaehlt, farbeA);
        ak.setAttribute("transform", "translate(" + x + " " + y + ") rotate(" + w + ")" + (passt ? "" : " translate(0 -26)"));
        szene.appendChild(ak);
      }
    }
  }

  // kleine Abbildung der Antikörper in den Auswahlknöpfen
  knoepfe.forEach(function (b) {
    var s = neu("svg", { viewBox: "-18 -94 76 86", width: 30, height: 34, "aria-hidden": "true" });
    s.appendChild(antikoerper(b.getAttribute("data-form"), "currentColor"));
    b.insertBefore(s, b.firstChild);
  });

  function neuerErreger() {
    erreger = formen[Math.floor(Math.random() * formen.length)];
    gebunden = false;
    zeichne(null);
    if (gedaechtnis[erreger]) {
      meldung.innerHTML = "<strong class='gut'>Dieser Erreger ist bekannt!</strong> Gedächtniszellen erkennen " + namen[erreger] + " sofort. Wähle den passenden Antikörper.";
    } else {
      meldung.textContent = namen[erreger] + " ist in den Körper eingedrungen. Welcher Antikörper passt zu seinen Antigenen?";
    }
  }

  knoepfe.forEach(function (b) {
    b.addEventListener("click", function () {
      var form = b.getAttribute("data-form");
      zeichne(form);
      if (form === erreger) {
        meldung.innerHTML = "<strong class='gut'>Passt!</strong> Die Antikörper binden an die Antigene und verklumpen den Erreger. Fresszellen können ihn jetzt beseitigen.";
        if (!gedaechtnis[erreger]) {
          gedaechtnis[erreger] = true;
          gedText.textContent = "Gedächtniszellen gespeichert für: " + Object.keys(gedaechtnis).map(function (k) { return namen[k]; }).join(", ");
        }
      } else {
        meldung.innerHTML = "<strong class='schlecht'>Passt nicht.</strong> Die Form der Bindungsstelle passt nicht zu den Antigenen. Der Antikörper kann nicht binden.";
      }
    });
  });
  document.getElementById("ss-neu").addEventListener("click", neuerErreger);
  neuerErreger();
})();
</script>
"""

IMMUNREAKTION = r"""
<p class="lead">Ein Virus dringt über eine kleine Wunde in den Körper ein. Gehe Schritt für Schritt durch, wie das Immunsystem reagiert.</p>

<div class="modell" id="ir">
  <svg viewBox="0 0 640 320" role="img" aria-labelledby="ir-t" id="ir-bild">
    <title id="ir-t">Schematische Darstellung der Immunreaktion, passend zum aktuellen Schritt</title>
    <defs>
      <g id="virus"><polygon points="0,-11 10,-5 10,5 0,11 -10,5 -10,-5" fill="var(--eosin)" stroke="currentColor" stroke-width="1"/><g stroke="currentColor" stroke-width="1.5"><line x1="0" y1="-11" x2="0" y2="-16"/><line x1="10" y1="5" x2="14" y2="8"/><line x1="-10" y1="5" x2="-14" y2="8"/></g></g>
      <g id="ak"><path d="M0 12 L0 2 M0 2 L-6 -6 M0 2 L6 -6" fill="none" stroke="var(--methylenblau)" stroke-width="3" stroke-linecap="round"/></g>
    </defs>
    <g font-family="Atkinson Hyperlegible, sans-serif" font-size="13" fill="currentColor">
      <!-- Haut -->
      <rect x="0" y="0" width="640" height="34" fill="color-mix(in srgb, var(--bernstein) 22%, transparent)"/>
      <path d="M300 0 L320 34 L340 0" fill="var(--flaeche)" stroke="none"/>
      <text x="12" y="22">Haut</text>
      <text x="350" y="22" data-ab="0" data-bis="1">Wunde</text>

      <!-- Schritt 0/1: Viren dringen ein -->
      <g data-ab="0" data-bis="2"><use href="#virus" x="320" y="54"/><use href="#virus" x="300" y="78"/><use href="#virus" x="345" y="84"/><use href="#virus" x="322" y="108"/></g>
      <!-- befallene Körperzelle -->
      <g data-ab="1">
        <ellipse cx="520" cy="120" rx="58" ry="42" fill="color-mix(in srgb, var(--malachit) 14%, transparent)" stroke="var(--malachit)" stroke-width="2.5"/>
        <circle cx="520" cy="120" r="13" fill="none" stroke="var(--malachit)" stroke-width="2"/>
        <text x="520" y="182" text-anchor="middle">Körperzelle</text>
      </g>
      <g data-ab="1" data-bis="6"><use href="#virus" x="490" y="104"/><use href="#virus" x="548" y="110"/><use href="#virus" x="530" y="140"/><use href="#virus" x="498" y="138"/></g>
      <text x="520" y="200" text-anchor="middle" data-ab="1" data-bis="6" fill="var(--eosin)" font-weight="700">von Viren befallen</text>

      <!-- Fresszelle -->
      <g data-ab="2">
        <path d="M120 120 c 30 -40, 80 -30, 90 0 s 10 50, -30 60 s -80 10, -70 -30 z" fill="color-mix(in srgb, var(--bernstein) 16%, transparent)" stroke="var(--bernstein)" stroke-width="2.5"/>
        <use href="#virus" x="160" y="140"/>
        <text x="160" y="205" text-anchor="middle">Fresszelle</text>
      </g>
      <g data-ab="3"><polygon points="198,96 210,92 206,104" fill="var(--eosin)"/><text x="222" y="92">präsentiert Antigen</text></g>

      <!-- T-Helferzelle -->
      <g data-ab="3">
        <circle cx="300" cy="170" r="28" fill="color-mix(in srgb, var(--methylenblau) 14%, transparent)" stroke="var(--methylenblau)" stroke-width="2.5"/>
        <text x="300" y="175" text-anchor="middle" font-weight="700">T</text>
        <text x="300" y="215" text-anchor="middle">T-Helferzelle</text>
        <line x1="208" y1="128" x2="274" y2="160" stroke="currentColor" stroke-dasharray="4 4"/>
      </g>
      <!-- B-Zelle / Plasmazelle -->
      <g data-ab="4">
        <line x1="300" y1="198" x2="250" y2="250" stroke="currentColor" stroke-dasharray="4 4"/>
        <circle cx="230" cy="270" r="26" fill="color-mix(in srgb, var(--methylenblau) 22%, transparent)" stroke="var(--methylenblau)" stroke-width="2.5"/>
        <text x="230" y="275" text-anchor="middle" font-weight="700">B</text>
        <text x="230" y="312" text-anchor="middle" data-bis="4">B-Zelle</text>
      </g>
      <g data-ab="5">
        <text x="230" y="312" text-anchor="middle">Plasmazelle</text>
        <use href="#ak" x="275" y="262"/><use href="#ak" x="290" y="280"/><use href="#ak" x="268" y="290"/>
      </g>
      <!-- Antikörper verklumpen freie Viren -->
      <g data-ab="5">
        <use href="#virus" x="390" y="270"/><use href="#virus" x="420" y="262"/><use href="#virus" x="405" y="292"/>
        <use href="#ak" x="404" y="262" transform="rotate(180 404 268)"/><use href="#ak" x="380" y="292"/><use href="#ak" x="425" y="290"/>
        <text x="408" y="250" text-anchor="middle">verklumpte Viren</text>
      </g>
      <!-- Killerzelle -->
      <g data-ab="6">
        <circle cx="420" cy="170" r="24" fill="color-mix(in srgb, var(--falsch) 14%, transparent)" stroke="var(--falsch)" stroke-width="2.5"/>
        <text x="420" y="175" text-anchor="middle" font-weight="700">K</text>
        <text x="420" y="212" text-anchor="middle">Killerzelle</text>
        <line x1="440" y1="158" x2="466" y2="140" stroke="var(--falsch)" stroke-width="3"/>
        <text x="520" y="200" text-anchor="middle" fill="var(--falsch)" font-weight="700">wird zerstört</text>
      </g>
      <!-- Gedächtniszellen -->
      <g data-ab="7">
        <circle cx="560" cy="270" r="20" fill="none" stroke="var(--methylenblau)" stroke-width="2.5" stroke-dasharray="5 3"/>
        <circle cx="605" cy="282" r="16" fill="none" stroke="var(--methylenblau)" stroke-width="2.5" stroke-dasharray="5 3"/>
        <text x="560" y="275" text-anchor="middle" font-weight="700">G</text>
        <text x="580" y="314" text-anchor="middle">Gedächtniszellen</text>
      </g>
    </g>
  </svg>

  <div class="schritt-text" aria-live="polite">
    <h3 id="ir-titel"></h3>
    <p id="ir-text"></p>
  </div>
  <div class="fortschritt" id="ir-fortschritt" aria-hidden="true"></div>
  <div class="modell-steuerung">
    <button class="knopf leise" type="button" id="ir-zurueck">Zurück</button>
    <button class="knopf" type="button" id="ir-weiter">Weiter</button>
    <span class="legende" id="ir-zaehler"></span>
  </div>
</div>

<h3>Grenzen des Modells</h3>
<p>Im Modell laufen die Schritte nacheinander ab. In Wirklichkeit passiert vieles gleichzeitig und an verschiedenen Orten im Körper, etwa in den Lymphknoten. Außerdem sind die Zellen hier stark vereinfacht und nicht maßstabsgetreu gezeichnet.</p>

<script>
(function () {
  var schritte = [
    ["Infektion", "Über eine kleine Wunde in der Haut gelangen Viren in den Körper. Die äußere Schranke ist durchbrochen."],
    ["Viren befallen Körperzellen", "Die Viren dringen in Körperzellen ein und lassen sie neue Viren herstellen. Die Zahl der Viren steigt schnell an. Man merkt noch nichts: Das ist die Inkubationszeit."],
    ["Unspezifische Abwehr: Fresszellen", "Fresszellen umfließen Viren und verdauen sie. Sie greifen alle Eindringlinge gleich an, sind aber gegen die schnelle Vermehrung allein zu langsam."],
    ["Antigen präsentieren und Alarm geben", "Die Fresszelle zeigt Bruchstücke des Virus, die Antigene, an ihrer Oberfläche. Eine T-Helferzelle mit passendem Rezeptor erkennt sie und gibt Alarm. Jetzt startet die spezifische Abwehr."],
    ["B-Zellen werden aktiviert", "Die T-Helferzelle aktiviert B-Zellen, die genau zu diesem Antigen passen. Sie teilen sich viele Male."],
    ["Antikörper werden gebildet", "Aus den B-Zellen werden Plasmazellen. Sie stellen große Mengen Antikörper her. Die Antikörper binden nach dem Schlüssel-Schloss-Prinzip an die Viren und verklumpen sie. Fresszellen räumen die Klumpen weg."],
    ["Killerzellen zerstören befallene Zellen", "Viren in Körperzellen erreichen die Antikörper nicht. Deshalb erkennen Killerzellen befallene Körperzellen und zerstören sie, bevor weitere Viren freigesetzt werden."],
    ["Genesung und Gedächtnis", "Die Viren sind besiegt, man wird wieder gesund. Einige B- und T-Zellen bleiben als Gedächtniszellen erhalten. Beim nächsten Kontakt mit demselben Virus reagieren sie sofort: Man ist immun."]
  ];
  var nr = 0;
  var bild = document.getElementById("ir-bild");
  var fort = document.getElementById("ir-fortschritt");
  schritte.forEach(function () { fort.appendChild(document.createElement("span")); });

  function zeigen() {
    bild.querySelectorAll("[data-ab]").forEach(function (e) {
      var ab = +e.getAttribute("data-ab");
      var bis = e.hasAttribute("data-bis") ? +e.getAttribute("data-bis") : 99;
      e.style.display = (nr >= ab && nr <= bis) ? "" : "none";
    });
    bild.querySelectorAll("[data-bis]:not([data-ab])").forEach(function (e) {
      e.style.display = nr <= +e.getAttribute("data-bis") ? "" : "none";
    });
    document.getElementById("ir-titel").textContent = schritte[nr][0];
    document.getElementById("ir-text").textContent = schritte[nr][1];
    document.getElementById("ir-zaehler").textContent = "Schritt " + (nr + 1) + " von " + schritte.length;
    Array.prototype.forEach.call(fort.children, function (s, i) { s.classList.toggle("an", i <= nr); });
    document.getElementById("ir-zurueck").disabled = nr === 0;
    var w = document.getElementById("ir-weiter");
    w.textContent = nr === schritte.length - 1 ? "Von vorn" : "Weiter";
  }
  document.getElementById("ir-weiter").addEventListener("click", function () { nr = nr === schritte.length - 1 ? 0 : nr + 1; zeigen(); });
  document.getElementById("ir-zurueck").addEventListener("click", function () { if (nr > 0) { nr--; zeigen(); } });
  document.addEventListener("keydown", function (e) {
    if (e.target.closest && e.target.closest("input, textarea, select")) return;
    if (e.key === "ArrowRight") { nr = Math.min(nr + 1, schritte.length - 1); zeigen(); }
    if (e.key === "ArrowLeft") { nr = Math.max(nr - 1, 0); zeigen(); }
  });
  zeigen();
})();
</script>
"""

RESISTENZ = r"""
<p class="lead">In einer Bakterienpopulation gibt es fast immer ein paar wenige Bakterien, denen ein bestimmtes Antibiotikum zufällig nichts anhaben kann. Was passiert mit ihnen, wenn das Antibiotikum eingesetzt wird?</p>

<div class="modell" id="rs">
  <svg viewBox="0 0 600 300" role="img" aria-labelledby="rs-t" id="rs-feld">
    <title id="rs-t">Bakterienpopulation: empfindliche und resistente Bakterien als Punkte</title>
  </svg>
  <p class="legende">
    <svg width="14" height="14" aria-hidden="true"><circle cx="7" cy="7" r="6" fill="var(--methylenblau)"/></svg> empfindlich: <strong id="rs-e">0</strong>
    &nbsp;&nbsp;
    <svg width="14" height="14" aria-hidden="true"><circle cx="7" cy="7" r="6" fill="var(--eosin)"/></svg> resistent: <strong id="rs-r">0</strong>
    &nbsp;&nbsp; Tag <strong id="rs-tag">0</strong>
  </p>
  <div class="modell-steuerung">
    <button class="knopf leise" type="button" id="rs-ohne">Ein Tag ohne Antibiotikum</button>
    <button class="knopf" type="button" id="rs-mit">Ein Tag mit Antibiotikum</button>
    <button class="knopf leise" type="button" id="rs-reset">Zurücksetzen</button>
  </div>
  <p class="rueckmeldung" id="rs-meldung" aria-live="polite"></p>
  <h3>Verlauf</h3>
  <svg viewBox="0 0 600 180" role="img" aria-labelledby="rs-vt" id="rs-verlauf">
    <title id="rs-vt">Diagramm: Anzahl empfindlicher und resistenter Bakterien über die Tage</title>
  </svg>
</div>

<h2>Arbeitsauftrag</h2>
<ol>
  <li>Lass die Bakterien zunächst drei Tage ohne Antibiotikum wachsen. Beschreibe, was du beobachtest.</li>
  <li>Gib nun mehrere Tage hintereinander das Antibiotikum. Beschreibe, wie sich der Anteil der resistenten Bakterien verändert.</li>
  <li>Setze das Antibiotikum danach ab und lass die Bakterien wieder wachsen. Erkläre, warum dasselbe Antibiotikum jetzt kaum noch helfen würde.</li>
  <li>Erkläre mit dem Begriff <span class="fachwort">Selektion</span>, warum das Antibiotikum die Bakterien nicht resistent <em>macht</em>, aber trotzdem dafür sorgt, dass Resistenzen zunehmen.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Das Modell ist stark vereinfacht: Das Immunsystem des Menschen ist nicht dargestellt, obwohl es in Wirklichkeit viele Bakterien selbst bekämpft. Die Zahlen sind ausgedacht und sollen nur das Prinzip zeigen. Außerdem können Bakterien Resistenzen in Wirklichkeit auch über Plasmide aneinander weitergeben.</p>

<script>
(function () {
  var ns = "http://www.w3.org/2000/svg";
  var MAX = 480, START_E = 40, START_R = 1;
  var feld = document.getElementById("rs-feld");
  var verlauf = document.getElementById("rs-verlauf");
  var meldung = document.getElementById("rs-meldung");
  var e, r, tag, daten, plaetze;

  function neu(tag, attrs) { var x = document.createElementNS(ns, tag); for (var k in attrs) x.setAttribute(k, attrs[k]); return x; }

  // feste, gemischte Plätze im Feld
  plaetze = [];
  for (var y = 0; y < 16; y++) for (var x = 0; x < 30; x++) plaetze.push([12 + x * 19.5 + (y % 2) * 6, 12 + y * 18.3]);
  var saat = 20261029; function zufall() { saat = (saat + 0x6D2B79F5) | 0; var q = Math.imul(saat ^ (saat >>> 15), 1 | saat); q = (q + Math.imul(q ^ (q >>> 7), 61 | q)) ^ q; return ((q ^ (q >>> 14)) >>> 0) / 4294967296; }
  for (var i = plaetze.length - 1; i > 0; i--) { var j = Math.floor(zufall() * (i + 1)); var t = plaetze[i]; plaetze[i] = plaetze[j]; plaetze[j] = t; }

  function zufallRunden(x) { var g = Math.floor(x); return g + (Math.random() < x - g ? 1 : 0); }

  function wachsen() {
    // Wachstum mit Platzgrenze (Nährstoffe begrenzt)
    var gesamt = e + r;
    var frei = Math.max(0, MAX - gesamt);
    var zuwachsE = Math.min(e, zufallRunden(e * frei / MAX));
    var zuwachsR = Math.min(r, zufallRunden(r * frei / MAX));
    e += zuwachsE; r += zuwachsR;
  }

  function antibiotikum() {
    // tötet etwa 80 % der empfindlichen Bakterien, resistente überleben
    var tot = 0;
    for (var k = 0; k < e; k++) if (Math.random() < 0.8) tot++;
    e -= tot;
  }

  function zeichneFeld() {
    while (feld.firstChild) feld.removeChild(feld.firstChild);
    feld.appendChild(neu("rect", { x: 0, y: 0, width: 600, height: 300, rx: 10, fill: "var(--papier)" }));
    var n = 0;
    for (var a = 0; a < r && n < MAX; a++, n++) feld.appendChild(neu("circle", { cx: plaetze[n][0], cy: plaetze[n][1], r: 6.5, fill: "var(--eosin)" }));
    for (var b = 0; b < e && n < MAX; b++, n++) feld.appendChild(neu("circle", { cx: plaetze[n][0], cy: plaetze[n][1], r: 6.5, fill: "var(--methylenblau)" }));
    document.getElementById("rs-e").textContent = e;
    document.getElementById("rs-r").textContent = r;
    document.getElementById("rs-tag").textContent = tag;
  }

  function zeichneVerlauf() {
    while (verlauf.firstChild) verlauf.removeChild(verlauf.firstChild);
    var L = 46, R = 590, O = 12, U = 150;
    var g = neu("g", { "font-family": "Atkinson Hyperlegible, sans-serif", "font-size": 12, fill: "currentColor" });
    verlauf.appendChild(g);
    g.appendChild(neu("line", { x1: L, y1: U, x2: R, y2: U, stroke: "currentColor" }));
    g.appendChild(neu("line", { x1: L, y1: O, x2: L, y2: U, stroke: "currentColor" }));
    [0, 240, 480].forEach(function (v) {
      var yy = U - v / MAX * (U - O);
      var t = neu("text", { x: L - 6, y: yy + 4, "text-anchor": "end" }); t.textContent = v; g.appendChild(t);
    });
    var tx = neu("text", { x: (L + R) / 2, y: 174, "text-anchor": "middle" }); tx.textContent = "Tage"; g.appendChild(tx);
    var tage = Math.max(10, daten.length - 1);
    function px(i) { return L + i / tage * (R - L); }
    function py(v) { return U - v / MAX * (U - O); }
    // Antibiotika-Tage hinterlegen
    daten.forEach(function (d, i) {
      if (i > 0 && d.ab) g.appendChild(neu("rect", { x: px(i - 1), y: O, width: px(i) - px(i - 1), height: U - O, fill: "color-mix(in srgb, var(--bernstein) 16%, transparent)" }));
    });
    ["e", "r"].forEach(function (k) {
      var d = daten.map(function (p, i) { return (i ? "L" : "M") + px(i).toFixed(1) + " " + py(p[k]).toFixed(1); }).join(" ");
      g.appendChild(neu("path", { d: d, fill: "none", stroke: k === "e" ? "var(--methylenblau)" : "var(--eosin)", "stroke-width": 3, "stroke-linejoin": "round" }));
    });
    var hinweis = neu("text", { x: R, y: O + 4, "text-anchor": "end", fill: "var(--tinte-weich)" }); hinweis.textContent = "hinterlegt = Tage mit Antibiotikum"; g.appendChild(hinweis);
  }

  function bewerte(mitAB) {
    var anteil = (e + r) ? r / (e + r) : 0;
    if (e + r === 0) meldung.textContent = "Alle Bakterien sind abgestorben.";
    else if (mitAB && anteil > 0.5) meldung.textContent = "Die meisten übrig gebliebenen Bakterien sind resistent. Das Antibiotikum wirkt kaum noch.";
    else if (mitAB) meldung.textContent = "Das Antibiotikum tötet viele empfindliche Bakterien. Die resistenten überleben alle.";
    else if (anteil > 0.5) meldung.textContent = "Die resistenten Bakterien haben jetzt viel Platz und vermehren sich ungestört.";
    else meldung.textContent = "Die Bakterien vermehren sich, bis Platz und Nährstoffe knapp werden.";
  }

  function tagVorbei(mitAB) {
    tag++;
    if (mitAB) antibiotikum();
    wachsen();
    daten.push({ e: e, r: r, ab: mitAB });
    zeichneFeld(); zeichneVerlauf(); bewerte(mitAB);
  }

  function reset() {
    e = START_E; r = START_R; tag = 0; daten = [{ e: e, r: r, ab: false }];
    meldung.textContent = "Am Anfang ist nur ein einziges Bakterium resistent.";
    zeichneFeld(); zeichneVerlauf();
  }

  document.getElementById("rs-ohne").addEventListener("click", function () { tagVorbei(false); });
  document.getElementById("rs-mit").addEventListener("click", function () { tagVorbei(true); });
  document.getElementById("rs-reset").addEventListener("click", reset);
  reset();
})();
</script>
"""

MODELLE = [
 {"slug": "schluessel-schloss", "titel": "Modell: Das Schlüssel-Schloss-Prinzip", "kurz": "Finde den Antikörper, der zum Erreger passt", "inhalt": SCHLUESSEL_SCHLOSS},
 {"slug": "immunreaktion", "titel": "Modell: Die Immunreaktion Schritt für Schritt", "kurz": "Von der Infektion bis zu den Gedächtniszellen", "inhalt": IMMUNREAKTION},
 {"slug": "antibiotika-resistenz", "titel": "Modell: Wie Resistenzen entstehen", "kurz": "Simulation einer Bakterienpopulation unter Antibiotika", "inhalt": RESISTENZ},
]
