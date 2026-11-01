"""Seite: Virtuelles Lichtmikroskop."""

OBJ = [  # Vergrößerung, Länge, Farbring (Farbcode der Objektive)
    (4, 40, "#d23b3b"), (10, 50, "#e8b923"), (40, 60, "#5aa7e0"), (100, 68, "#f6f6f6"),
]


def objektive_svg():
    g = ""
    for i, (v, l, farbe) in enumerate(OBJ):
        b = 22 if v < 40 else 20
        g += (f'<g class="mk-obj" data-obj="{i}" transform="rotate({i * 32} 230 178)">'
              f'<rect class="s f-weiss" x="{230 - b / 2}" y="190" width="{b}" height="{l - 12}" rx="3"/>'
              f'<rect class="s2" x="{230 - b / 2}" y="{190 + l - 30}" width="{b}" height="7" fill="{farbe}"/>'
              f'<rect class="s f-sand" x="{230 - b / 2 + 4}" y="{190 + l - 12}" width="{b - 8}" height="12" rx="2"/>'
              f'<text class="hk" x="230" y="{190 + (l - 30) / 2 + 6}" text-anchor="middle" style="font-size:14px">{v}</text></g>')
    return g


MIKROSKOP_SVG = f'''<svg id="mk-svg-licht" class="ill" viewBox="0 0 480 480" role="img" aria-labelledby="mk-geraet-t mk-geraet-d">
<title id="mk-geraet-t">Aufbau eines Lichtmikroskops</title>
<desc id="mk-geraet-d">Beschriftete Zeichnung eines Lichtmikroskops mit Okular, Tubus, Revolver, Objektiven, Objekttisch mit Objektträger, Blende, Lichtquelle, Stativ, Grob- und Feintrieb sowie Fuß. Das ausgewählte Objektiv zeigt nach unten auf das Präparat.</desc>
<path class="mk-licht" d="M218 398 L 242 398 L 238 262 L 222 262 Z"/>
<path class="s f-blau" d="M128 456 Q 126 424 152 422 H 382 Q 406 424 404 456 Z"/>
<rect class="s f-weiss" x="206" y="396" width="48" height="26" rx="6"/>
<circle class="s f-gelb" cx="230" cy="404" r="8"/>
<path class="s f-weiss" d="M350 422 C 360 380, 372 330, 372 270 C 372 200, 346 150, 270 124 L 252 156 C 312 176, 336 214, 336 270 C 336 330, 322 380, 312 422 Z"/>
<rect class="s f-sand" x="202" y="292" width="56" height="14" rx="4"/>
<path class="s2" d="M258 299 h 20" fill="none"/>
<g id="mk-tisch" class="mk-tisch">
  <rect class="s f-blau" x="138" y="270" width="214" height="14" rx="4"/>
  <rect class="s f-weiss" x="168" y="262" width="124" height="8" rx="1.5"/>
  <rect class="s2 f-blau-weich" x="212" y="259" width="36" height="3"/>
  <ellipse id="mk-tropfen" cx="230" cy="265" rx="11" ry="2.6" fill="#7f9be3"/>
  <path class="s2" fill="none" d="M160 262 l 22 -5 M 300 262 l -22 -5"/>
</g>
<circle class="s f-sand" cx="372" cy="318" r="22"/>
<g id="mk-feinmarke" class="mk-feinmarke"><circle class="s f-weiss" cx="372" cy="318" r="11"/><line class="s" x1="372" y1="318" x2="372" y2="309"/></g>
<rect class="s f-weiss" x="210" y="58" width="40" height="112" rx="5"/>
<rect class="s f-blau" x="216" y="18" width="28" height="44" rx="5"/>
<rect class="s f-sand" x="212" y="12" width="36" height="10" rx="4"/>
<g id="mk-revolver" class="mk-revolver">{objektive_svg()}</g>
<circle class="s f-sand" cx="230" cy="178" r="20"/>
<circle class="d" cx="230" cy="178" r="3"/>
<g class="mk-beschr">
  <path class="s2" fill="none" d="M164 36 H 214 M 164 112 H 208 M 164 176 H 208 M 164 226 H 220 M 128 252 L 176 264 M 120 300 L 146 282 M 164 326 L 206 306 M 164 410 H 206 M 364 196 L 346 210 M 398 316 H 396 M 398 344 L 380 326 M 410 446 H 404"/>
  <text class="h" x="160" y="42" text-anchor="end">Okular</text>
  <text class="h" x="160" y="118" text-anchor="end">Tubus</text>
  <text class="h" x="160" y="182" text-anchor="end">Revolver</text>
  <text class="h" x="160" y="232" text-anchor="end">Objektiv</text>
  <text class="h" x="124" y="256" text-anchor="end">Objektträger</text>
  <text class="h" x="116" y="306" text-anchor="end">Objekttisch</text>
  <text class="h" x="160" y="332" text-anchor="end">Blende</text>
  <text class="h" x="160" y="416" text-anchor="end">Lichtquelle</text>
  <text class="h" x="368" y="192">Stativ</text>
  <text class="h" x="400" y="322">Grobtrieb</text>
  <text class="h" x="400" y="350">Feintrieb</text>
  <text class="h" x="412" y="452">Fuß</text>
</g>
</svg>'''


EM_SVG = '''<svg id="mk-svg-em" class="ill" viewBox="0 0 480 480" role="img" aria-labelledby="mk-em-t mk-em-d" style="display:none">
<title id="mk-em-t">Aufbau eines Rasterelektronenmikroskops</title>
<desc id="mk-em-d">Beschriftete Zeichnung: Oben in einer hohen Säule sitzt die Elektronenquelle. Der Elektronenstrahl wird von Magnetlinsen gebündelt und trifft unten in der Probenkammer auf die Probe. Ein Detektor fängt die zurückkommenden Elektronen auf, ein Computer setzt daraus das Bild auf dem Bildschirm zusammen. Eine Vakuumpumpe saugt die Luft aus der Säule.</desc>
<rect class="s f-sand" x="40" y="408" width="320" height="36" rx="6"/>
<rect class="s f-weiss" x="196" y="40" width="76" height="250" rx="10"/>
<rect class="s f-sand" x="208" y="14" width="52" height="32" rx="6"/>
<path class="s2 k-bernstein" fill="none" d="M226 30 l 4 -6 l 4 6 l 4 -6"/>
<path class="mk-strahl" d="M234 46 L 234 330"/>
<path class="mk-strahlkegel" d="M222 50 L 246 50 L 238 110 L 230 110 Z M 226 132 L 242 132 L 236 190 L 232 190 Z M 229 212 L 239 212 L 235 330 L 233 330 Z"/>
<g class="mk-spulen">
  <rect class="s f-blau" x="188" y="104" width="92" height="30" rx="6"/>
  <rect class="s f-blau" x="188" y="184" width="92" height="30" rx="6"/>
  <path class="s2" fill="none" d="M196 110 v18 M204 110 v18 M212 110 v18 M256 110 v18 M264 110 v18 M272 110 v18 M196 190 v18 M204 190 v18 M212 190 v18 M256 190 v18 M264 190 v18 M272 190 v18"/>
</g>
<rect class="s f-weiss" x="160" y="290" width="148" height="88" rx="10"/>
<rect class="s f-sand" x="210" y="346" width="48" height="10" rx="2"/>
<ellipse id="mk-tropfen-em" cx="234" cy="343" rx="12" ry="3.5" fill="#9aa3aa"/>
<rect class="s f-blau" x="264" y="306" width="30" height="20" rx="4"/>
<path class="s2" fill="none" d="M264 318 L 244 334"/>
<path class="s" fill="none" d="M294 316 C 330 316, 360 300, 372 252"/>
<rect class="s f-blau-weich" x="64" y="320" width="54" height="86" rx="10"/>
<path class="s" fill="none" d="M118 352 H 160"/>
<path class="s2" fill="none" d="M76 336 h30 M76 348 h30 M76 360 h30"/>
<rect class="s f-weiss" x="314" y="120" width="150" height="110" rx="10"/>
<rect x="326" y="132" width="126" height="80" rx="4" fill="#2b3135"/>
<circle cx="360" cy="166" r="14" fill="#c9ced2"/><circle cx="398" cy="180" r="10" fill="#b1b8bd"/><circle cx="420" cy="152" r="12" fill="#d8dde0"/>
<g stroke="#c9ced2" stroke-width="2"><line x1="360" y1="150" x2="360" y2="146"/><line x1="374" y1="166" x2="378" y2="166"/><line x1="346" y1="166" x2="342" y2="166"/><line x1="360" y1="180" x2="360" y2="184"/></g>
<path class="s f-sand" d="M378 230 L 372 252 H 406 L 400 230 Z"/>
<g class="mk-beschr">
  <path class="s2" fill="none" d="M176 30 H 206 M 176 120 H 186 M 176 160 L 232 160 M 150 264 L 164 294 M 200 360 L 214 352 M 300 296 L 284 304"/>
  <text class="h" x="172" y="36" text-anchor="end">Elektronenquelle</text>
  <text class="h" x="172" y="126" text-anchor="end">Magnetlinse</text>
  <text class="h" x="172" y="166" text-anchor="end">Elektronenstrahl</text>
  <text class="h" x="146" y="268" text-anchor="end">Probenkammer</text>
  <text class="hk" x="172" y="372">Probe</text>
  <text class="h" x="91" y="310" text-anchor="middle">Vakuumpumpe</text>
  <text class="h" x="304" y="290">Detektor</text>
  <text class="h" x="390" y="110" text-anchor="middle">Bildschirm</text>
</g>
</svg>'''

PRAEP = [("mund", "Mundschleimhaut"), ("joghurt", "Joghurt"), ("ecoli", "Darmbakterien (E. coli)"),
         ("staph", "Staphylokokken"), ("bacillus", "Bacillus megaterium"), ("thio", "Riesenbakterium Thiomargarita"),
         ("elodea", "Wasserpest-Blatt")]

knoepfe_p = "".join(f'<button type="button" data-praeparat="{k}" aria-pressed="false">{n}</button>' for k, n in PRAEP)
knoepfe_o = "".join(f'<button type="button" data-objektiv="{i}" aria-pressed="false"><span class="mk-ring" style="--ring:{f}" aria-hidden="true"></span>{v}×</button>'
                    for i, (v, _, f) in enumerate(OBJ))

INHALT = f'''
<p class="lead">Lege ein Präparat ein, wähle ein Objektiv und stelle scharf. Alle Präparate sind maßstabsgetreu: Du siehst Zellen, Bakterien und Viren so groß, wie sie bei der gewählten Vergrößerung wirklich erscheinen. Für Viren brauchst du das Elektronenmikroskop.</p>

<div class="ausbrechen">
<div class="mk" id="mk">
  <div class="mk-blick">
    <div class="mk-feld" id="mk-feld" tabindex="0" aria-describedby="mk-bedienung">
      <canvas id="mk-canvas" role="img" aria-label="Blick durch das Mikroskop"></canvas>
      <div class="mk-okularrand" aria-hidden="true"></div>
    </div>
    <p class="legende mk-bedienung" id="mk-bedienung">Objekttisch verschieben: im Bild ziehen oder mit den Pfeiltasten.</p>
    <div class="mk-werte">
      <div class="mk-wert gross"><span class="legende">Gesamtvergrößerung</span><strong id="mk-gesamt">400×</strong><span class="legende" id="mk-rechnung"></span></div>
      <div class="mk-wert"><span class="legende" id="mk-sehfeld-name">Durchmesser des Sehfelds</span><strong id="mk-sehfeld">0,45 mm</strong></div>
    </div>
    <p class="mk-erkennbar" id="mk-erkennbar" aria-live="polite"></p>
    <p class="mk-hinweis" id="mk-hinweis" aria-live="polite" hidden></p>
  </div>

  <div class="mk-steuerung">
    <fieldset>
      <legend>Gerät</legend>
      <div class="wahl mk-geraetwahl"><button type="button" data-geraet="licht" aria-pressed="true">Lichtmikroskop</button><button type="button" data-geraet="elektronen" aria-pressed="false">Elektronenmikroskop</button></div>
    </fieldset>
    <fieldset>
      <legend>Präparat</legend>
      <div class="wahl" id="mk-praeparate"></div>
      <p class="legende mk-praeptext" id="mk-text"></p>
    </fieldset>
    <fieldset>
      <legend id="mk-stufen-legende">Objektiv</legend>
      <div class="wahl" id="mk-stufen"></div>
      <p class="legende" id="mk-stufen-notiz"></p>
    </fieldset>
    <fieldset>
      <legend><label for="mk-feintrieb">Feintrieb (Scharfstellen)</label></legend>
      <input type="range" id="mk-feintrieb" min="-6" max="6" step="1" value="0">
    </fieldset>
    <fieldset class="mk-schalter">
      <legend>Anzeige</legend>
      <label><input type="checkbox" id="mk-beschriften" checked> Beschriftungen</label>
      <label><input type="checkbox" id="mk-massstab" checked> Maßstab</label>
    </fieldset>
  </div>

  <div class="mk-geraet">{MIKROSKOP_SVG}{EM_SVG}</div>
</div>

<section class="mk-groesse" aria-labelledby="mk-groesse-t">
  <h2 id="mk-groesse-t">Wie groß erscheint was?</h2>
  <p class="hinweis">Wähle ein Objekt aus der Liste. Die Größenleiter zeigt, wie groß es ohne Mikroskop und bei jeder Vergrößerung erscheint. Gemeint ist: so groß, wie es wirken würde, wenn es in normaler Leseentfernung (25 cm) vor dir läge.</p>
  <div class="mk-groesse-raster">
    <ul class="mk-liste" id="mk-liste"></ul>
    <div>
      <div class="mk-leiter" id="mk-leiter"></div>
      <p class="mk-leitertext" id="mk-leitertext" aria-live="polite"></p>
    </div>
  </div>
</section>
</div>

<h2>So rechnest du</h2>
<p>Ein Lichtmikroskop vergrößert zweimal hintereinander: erst das <span class="fachwort">Objektiv</span>, dann das <span class="fachwort">Okular</span>. Die Gesamtvergrößerung erhältst du, indem du beide Werte multiplizierst.</p>
<div class="merke"><strong>Merke</strong>
<p>Gesamtvergrößerung = Vergrößerung des Okulars × Vergrößerung des Objektivs. Beispiel: 10 × 40 = 400-fach. Ein Bakterium von 2 µm Länge erscheint dann 2 µm × 400 = 800 µm = 0,8 mm groß.</p></div>
<div class="tabelle-scroll"><table>
  <thead><tr><th>Objektiv</th><th>Gesamtvergrößerung</th><th>Durchmesser des Sehfelds</th><th>Bakterium (2 µm) erscheint</th></tr></thead>
  <tbody>
    <tr><td>4×</td><td>40-fach</td><td>4,5 mm</td><td>0,08 mm: unsichtbar</td></tr>
    <tr><td>10×</td><td>100-fach</td><td>1,8 mm</td><td>0,2 mm: winziger Punkt</td></tr>
    <tr><td>40×</td><td>400-fach</td><td>0,45 mm</td><td>0,8 mm: wie ein Sandkorn</td></tr>
    <tr><td>100× mit Öl</td><td>1000-fach</td><td>0,18 mm</td><td>2 mm: wie ein Stecknadelkopf</td></tr>
  </tbody>
</table></div>
<p>Je stärker die Vergrößerung, desto kleiner wird der Ausschnitt, den du siehst. Deshalb sucht man eine Stelle immer zuerst mit dem schwächsten Objektiv und wechselt dann zu stärkeren.</p>

<h2>Licht- oder Elektronenmikroskop?</h2>
<p>Ein Lichtmikroskop kann Dinge, die kleiner als etwa 0,2 µm sind, nicht mehr getrennt darstellen, egal wie stark man vergrößert. Diese Grenze heißt <span class="fachwort">Auflösungsgrenze</span>. Viren sind meist kleiner und bleiben deshalb unsichtbar. Ein <span class="fachwort">Elektronenmikroskop</span> nutzt statt Licht einen Strahl aus Elektronen. Damit lassen sich noch Strukturen von wenigen Nanometern erkennen, und man kann bis zu mehrere hunderttausendfach vergrößern.</p>
<div class="tabelle-scroll"><table>
  <thead><tr><th></th><th>Lichtmikroskop</th><th>Elektronenmikroskop</th></tr></thead>
  <tbody>
    <tr><th scope="row">Strahlung</th><td>Licht</td><td>Elektronen</td></tr>
    <tr><th scope="row">Linsen</th><td>Glaslinsen</td><td>Magnetlinsen</td></tr>
    <tr><th scope="row">Vergrößerung</th><td>bis etwa 1000-fach</td><td>bis mehrere 100 000-fach</td></tr>
    <tr><th scope="row">Auflösung</th><td>etwa 0,2 µm</td><td>wenige Nanometer und feiner</td></tr>
    <tr><th scope="row">Proben</th><td>auch lebende Zellen</td><td>nur tote, getrocknete Proben im Vakuum</td></tr>
    <tr><th scope="row">Bild</th><td>farbig</td><td>schwarz-weiß</td></tr>
    <tr><th scope="row">Kosten</th><td>ab etwa 100 Euro</td><td>mehrere hunderttausend Euro</td></tr>
  </tbody>
</table></div>
<p>1 µm (Mikrometer) ist ein Tausendstel Millimeter. 1 nm (Nanometer) ist ein Tausendstel Mikrometer, also ein Millionstel Millimeter.</p>

<h2>Arbeitsaufträge</h2>
<ol>
  <li>Lege das Präparat „Joghurt“ ein und beginne mit dem 4er-Objektiv. Wechsle schrittweise zu stärkeren Objektiven. Notiere, ab welcher Gesamtvergrößerung du die Milchsäurebakterien erkennen kannst.</li>
  <li>Vergleiche bei 400-facher Vergrößerung die Mundschleimhautzellen mit den Mundbakterien. Nenne mindestens zwei Unterschiede, an denen man Bakterienzellen von menschlichen Zellen unterscheiden kann.</li>
  <li>Ein Escherichia-coli-Bakterium ist 2 µm lang. Berechne, wie groß es bei 100-, 400- und 1000-facher Vergrößerung erscheint. Kontrolliere deine Ergebnisse mit der Größenleiter.</li>
  <li>Miss mithilfe des Maßstabs den Durchmesser einer Kugel des Riesenbakteriums Thiomargarita. Beurteile mit der Größenleiter, ob man sie mit bloßem Auge sehen könnte.</li>
  <li>Vergleiche ein Bakterium von Bacillus megaterium mit einem Chloroplasten der Wasserpest. Was fällt dir auf?</li>
  <li>Erkläre, warum man Viren auch bei 1000-facher Vergrößerung im Lichtmikroskop nicht sehen kann.</li>
  <li>Miss mit dem Maßstab die Dicke eines menschlichen Haares. Vergleiche sie mit der Länge eines Bakteriums: Wie viele E.-coli-Bakterien passen nebeneinander auf die Breite eines Haares?</li>
  <li>Vergleiche eine Zwiebelhautzelle mit einer Mundschleimhautzelle. Nenne Gemeinsamkeiten und Unterschiede zwischen Pflanzen- und Tierzellen.</li>
  <li>Untersuche das Bienenbein. Beschreibe, wie das Pollenkörbchen aufgebaut ist und wozu die Biene es braucht.</li>
  <li>Wechsle zum Elektronenmikroskop und betrachte die Bakteriophagen an E. coli. Vergleiche die Größe eines Phagen mit der des Bakteriums.</li>
  <li>Stelle das Grippevirus und das Coronavirus jeweils bei 500 000-facher Vergrößerung ein. Beschreibe die Unterschiede ihrer Oberfläche.</li>
</ol>

<div class="wusstest"><strong>Schon gewusst?</strong>
<p>2022 wurde in einem Mangrovensumpf in der Karibik das bisher größte bekannte Bakterium beschrieben: <em>Thiomargarita magnifica</em>. Seine fadenförmigen Zellen werden etwa 1 cm, manche sogar bis zu 2 cm lang. Man kann sie mit bloßem Auge sehen.</p></div>

<h2>Grenzen des Modells</h2>
<ul>
  <li>Im echten Mikroskop steht das Bild auf dem Kopf und ist seitenverkehrt. Schiebst du das Präparat nach links, wandert das Bild nach rechts. Im Modell ist das nicht so, damit das Verschieben leichter fällt.</li>
  <li>Bakterien sind fast durchsichtig. Damit man sie gut sieht, muss man sie anfärben. Die Farben im Modell sind vereinfacht.</li>
  <li>Echte Präparate sind räumlich: Es ist immer nur eine Ebene scharf. Im Modell gibt es nur eine Ebene.</li>
  <li>Die Größen sind maßstabsgetreu, Anzahl und Anordnung der Objekte sind aber ausgedacht.</li>
  <li>Echte Bilder aus dem Elektronenmikroskop sind schwarz-weiß. Farbige Bilder, wie man sie oft in Büchern sieht, wurden nachträglich eingefärbt. Das Modell zeigt Bilder eines Rasterelektronenmikroskops, das die Oberfläche abtastet.</li>
  <li>Lebende Viren und Zellen kann man im Elektronenmikroskop nicht beobachten: Die Proben müssen getrocknet und oft mit einer dünnen Metallschicht überzogen werden.</li>
</ul>
<p class="legende">Sicherheitshinweis: Im Unterricht werden nur ungefährliche Bakterien mikroskopiert, zum Beispiel aus Joghurt. Mögliche Krankheitserreger wie Staphylokokken oder E. coli untersucht man nur in Speziallaboren.</p>
'''

MIKROSKOP = {"slug": "lichtmikroskop", "titel": "Modell: Licht- und Elektronenmikroskop", "kurz": "Zellen, Bakterien und Viren von 40- bis 500 000-facher Vergrößerung",
             "inhalt": INHALT, "skripte": ["assets/mikroskop.js"]}
