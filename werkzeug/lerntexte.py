"""Lerntexte der Reihe 1: Abwehr von Krankheiten."""

SVG_BAKTERIUM_VIRUS = """<svg viewBox="0 0 640 300" role="img" aria-labelledby="bv-t bv-d" xmlns="http://www.w3.org/2000/svg">
  <title id="bv-t">Bau eines Bakteriums und eines Virus im Vergleich</title>
  <desc id="bv-d">Links ein stäbchenförmiges Bakterium mit Zellwand, Zellmembran, Zellplasma, ringförmigem Erbgut, Plasmiden, Ribosomen und Geißel. Rechts, stark vergrößert, ein Virus aus Erbgut in einer Eiweißhülle mit Andockstellen.</desc>
  <g font-family="Caveat, cursive" font-weight="700" font-size="18" fill="currentColor">
    <text x="20" y="24" font-size="22">Bakterium (ca. 2 µm)</text>
    <path d="M300 150 C 330 140, 345 175, 375 160 S 410 140, 425 155" fill="none" stroke="currentColor" stroke-width="2"/>
    <rect x="40" y="95" width="265" height="110" rx="55" fill="none" stroke="var(--methylenblau, #2e5aa6)" stroke-width="7"/>
    <rect x="48" y="103" width="249" height="94" rx="47" fill="color-mix(in srgb, var(--methylenblau, #2e5aa6) 12%, transparent)" stroke="currentColor" stroke-width="1.5"/>
    <path d="M110 150 c 15 -30, 50 -30, 60 -5 s 40 25, 55 -5 s -25 35, -55 30 s -70 5, -60 -20z" fill="none" stroke="#b3305f" stroke-width="2.5"/>
    <circle cx="245" cy="125" r="9" fill="none" stroke="#b3305f" stroke-width="2"/>
    <circle cx="90" cy="178" r="7" fill="none" stroke="#b3305f" stroke-width="2"/>
    <g fill="currentColor"><circle cx="210" cy="175" r="2.6"/><circle cx="225" cy="170" r="2.6"/><circle cx="95" cy="130" r="2.6"/><circle cx="125" cy="182" r="2.6"/><circle cx="260" cy="165" r="2.6"/><circle cx="180" cy="120" r="2.6"/></g>
    <line x1="60" y1="90" x2="40" y2="60" stroke="currentColor"/><text x="20" y="54">Zellwand</text>
    <line x1="150" y1="104" x2="150" y2="62" stroke="currentColor"/><text x="110" y="54">Zellmembran</text>
    <line x1="160" y1="135" x2="210" y2="70" stroke="currentColor"/><text x="200" y="64">Erbgut (ringförmig, frei)</text>
    <line x1="245" y1="134" x2="280" y2="240" stroke="currentColor"/><text x="230" y="256">Plasmid</text>
    <line x1="125" y1="185" x2="110" y2="240" stroke="currentColor"/><text x="60" y="256">Ribosomen</text>
    <line x1="200" y1="190" x2="180" y2="240" stroke="currentColor"/><text x="150" y="276">Zellplasma</text>
    <text x="380" y="190">Geißel</text>
    <line x1="470" y1="20" x2="470" y2="290" stroke="currentColor" stroke-dasharray="4 5" opacity=".4"/>
    <text x="490" y="24" font-size="22">Virus (ca. 0,1 µm)</text>
    <polygon points="560,95 600,118 600,164 560,187 520,164 520,118" fill="color-mix(in srgb, var(--methylenblau, #2e5aa6) 12%, transparent)" stroke="var(--methylenblau, #2e5aa6)" stroke-width="5"/>
    <path d="M545 130 c 10 -12, 25 10, 30 0 s -25 25, -20 30 s 25 -5, 20 10" fill="none" stroke="#b3305f" stroke-width="2.5"/>
    <g stroke="currentColor" stroke-width="2"><line x1="560" y1="95" x2="560" y2="78"/><line x1="600" y1="118" x2="614" y2="108"/><line x1="600" y1="164" x2="614" y2="174"/><line x1="560" y1="187" x2="560" y2="204"/><line x1="520" y1="164" x2="506" y2="174"/><line x1="520" y1="118" x2="506" y2="108"/></g>
    <g fill="currentColor"><circle cx="560" cy="76" r="4"/><circle cx="616" cy="106" r="4"/><circle cx="616" cy="176" r="4"/><circle cx="560" cy="206" r="4"/><circle cx="504" cy="176" r="4"/><circle cx="504" cy="106" r="4"/></g>
    <text x="490" y="236">Eiweißhülle</text>
    <text x="490" y="256">Erbgut</text>
    <text x="490" y="276">Andockstellen</text>
  </g>
</svg>"""

SVG_ANTIKOERPER_KURVE = """<svg viewBox="0 0 640 280" role="img" aria-labelledby="ak-t ak-d" xmlns="http://www.w3.org/2000/svg">
  <title id="ak-t">Antikörpermenge im Blut beim ersten und zweiten Kontakt mit demselben Erreger</title>
  <desc id="ak-d">Nach dem ersten Kontakt steigt die Antikörpermenge erst nach etwa einer Woche langsam und nur mäßig an. Beim zweiten Kontakt steigt sie schon nach wenigen Tagen steil und viel höher an.</desc>
  <g font-family="Caveat, cursive" font-weight="700" font-size="18" fill="currentColor">
    <line x1="60" y1="230" x2="620" y2="230" stroke="currentColor" stroke-width="1.5"/>
    <line x1="60" y1="230" x2="60" y2="20" stroke="currentColor" stroke-width="1.5"/>
    <text x="16" y="130" transform="rotate(-90 16 130)" text-anchor="middle">Antikörper im Blut</text>
    <text x="340" y="268" text-anchor="middle">Zeit in Wochen</text>
    <g text-anchor="middle"><text x="60" y="248">0</text><text x="140" y="248">1</text><text x="220" y="248">2</text><text x="300" y="248">3</text><text x="380" y="248">4</text><text x="460" y="248">5</text><text x="540" y="248">6</text></g>
    <path d="M60 228 C 120 228, 140 220, 170 190 S 220 165, 250 180 S 320 215, 360 218" fill="none" stroke="var(--methylenblau, #2e5aa6)" stroke-width="3.5"/>
    <path d="M360 218 C 390 216, 395 120, 420 60 S 470 50, 500 80 S 560 130, 610 140" fill="none" stroke="#b3305f" stroke-width="3.5"/>
    <line x1="60" y1="20" x2="60" y2="230" stroke="currentColor"/>
    <polygon points="60,212 52,200 68,200" fill="currentColor"/><text x="72" y="206">1. Kontakt</text>
    <polygon points="360,212 352,200 368,200" fill="currentColor"/><text x="372" y="206">2. Kontakt</text>
    <text x="150" y="160" fill="var(--methylenblau, #2e5aa6)" font-weight="700">langsam, schwach</text>
    <text x="520" y="66" fill="#b3305f">schnell, stark</text>
  </g>
</svg>"""

LERNTEXTE = [
{
"slug": "01-gesund-oder-krank",
"titel": "Gesund oder krank?",
"kurz": "Was Gesundheit bedeutet, wie Krankheitserreger übertragen werden und wie eine Infektionskrankheit verläuft.",
"inhalt": """
<p class="lead">Fast jeder kennt das: Erst kratzt der Hals, am nächsten Tag kommt Fieber. Doch was genau passiert da eigentlich – und was heißt es überhaupt, gesund zu sein?</p>

<h2>Was ist Gesundheit?</h2>
<p>Die <span class="fachwort">Weltgesundheitsorganisation (WHO)</span> hat 1946 festgelegt, was sie unter Gesundheit versteht: Gesund ist, wer sich <strong>körperlich, seelisch und sozial</strong> rundum wohlfühlt. Gesundheit bedeutet also mehr, als einfach nur nicht krank zu sein. Auch Schlaf, Bewegung, Ernährung, Freundschaften und Stress spielen eine Rolle.</p>

<h2>Wie Krankheitserreger in den Körper gelangen</h2>
<p>Viele Krankheiten werden durch winzige Lebewesen oder Partikel ausgelöst, die man <span class="fachwort">Krankheitserreger</span> nennt. Dazu gehören vor allem <strong>Bakterien</strong> und <strong>Viren</strong>, aber auch Pilze und Parasiten wie Würmer. Dringen Erreger in den Körper ein und vermehren sich dort, spricht man von einer <span class="fachwort">Infektion</span>.</p>
<!--FIG:uebertragungswege-->
<div class="tabelle-scroll"><table>
  <thead><tr><th>Übertragungsweg</th><th>So funktioniert er</th><th>Beispiel</th></tr></thead>
  <tbody>
    <tr><td>Tröpfcheninfektion</td><td>Beim Husten, Niesen oder Sprechen gelangen winzige Tröpfchen mit Erregern in die Luft und werden eingeatmet.</td><td>Grippe, Erkältung</td></tr>
    <tr><td>Kontakt- oder Schmierinfektion</td><td>Erreger gelangen über Hände, Türklinken oder Handys an Mund, Nase oder Augen.</td><td>Magen-Darm-Infekte</td></tr>
    <tr><td>Nahrung und Wasser</td><td>Erreger stecken in verdorbenen Lebensmitteln oder verschmutztem Wasser.</td><td>Salmonellen, Cholera</td></tr>
    <tr><td>Tiere</td><td>Erreger werden durch Stiche oder Bisse übertragen.</td><td>Borreliose (Zecke), Tollwut</td></tr>
  </tbody>
</table></div>

<h2>Wie eine Infektionskrankheit verläuft</h2>
<p>Zwischen der Ansteckung und den ersten Beschwerden vergeht meist etwas Zeit. Eine Infektionskrankheit läuft typischerweise in diesen Abschnitten ab:</p>
<ol>
  <li><strong>Infektion:</strong> Erreger gelangen in den Körper.</li>
  <li><strong>Inkubationszeit:</strong> Die Erreger vermehren sich, man merkt aber noch nichts. Je nach Krankheit dauert das Stunden bis Wochen. Oft kann man andere schon anstecken.</li>
  <li><strong>Krankheitsausbruch:</strong> Es treten <span class="fachwort">Symptome</span> auf, zum Beispiel Fieber, Husten oder Durchfall.</li>
  <li><strong>Überwindung:</strong> Das Immunsystem bekämpft die Erreger. Oft hat man dabei <span class="fachwort">Fieber</span>: Die erhöhte Körpertemperatur ist eine Abwehrreaktion, die die Vermehrung vieler Erreger bremst.</li>
  <li><strong>Genesung (Rekonvaleszenz):</strong> Die Erreger sind besiegt. In der <span class="fachwort">Rekonvaleszenz</span> erholt sich der Körper und gewinnt langsam seine Kräfte zurück.</li>
  <li><strong>Immunität:</strong> Bei vielen Krankheiten ist man danach für längere Zeit vor demselben Erreger geschützt.</li>
</ol>
<!--FIG:krankheitsverlauf-->

<div class="merke"><strong>Merke</strong>
<p>Eine Infektion liegt vor, wenn Krankheitserreger in den Körper eindringen und sich dort vermehren. Die Zeit zwischen Ansteckung und Krankheitsausbruch heißt Inkubationszeit. Die Erholungsphase nach der Krankheit heißt Rekonvaleszenz.</p></div>

<h2>Hygiene schützt</h2>
<p>Viele Ansteckungen lassen sich mit einfachen Mitteln verhindern: Hände gründlich mit Seife waschen (etwa 20 bis 30 Sekunden), in die Armbeuge niesen, Lebensmittel richtig lagern und gut durchgaren. In Krankenhäusern und Pflegeheimen sind Hygieneregeln besonders streng, weil dort viele geschwächte Menschen auf engem Raum leben.</p>

<div class="wusstest"><strong>Schon gewusst?</strong>
<p>Der Arzt Ignaz Semmelweis bemerkte 1847 in Wien, dass in einer Geburtsklinik viele Mütter am sogenannten Kindbettfieber starben, wenn Ärzte direkt aus dem Sektionssaal kamen. Er führte das Händedesinfizieren mit Chlorkalk ein, und die Zahl der Todesfälle sank stark. Viele Ärzte glaubten ihm damals trotzdem nicht.</p></div>
"""
},
{
"slug": "02-bakterien-und-viren",
"titel": "Bakterien und Viren",
"kurz": "Wie Bakterien und Viren gebaut sind und wie sie sich vermehren – ein Vergleich.",
"inhalt": """
<p class="lead">Bakterien und Viren werden oft in einen Topf geworfen. Dabei unterscheiden sie sich grundlegend: Bakterien sind Lebewesen, Viren dagegen nicht einmal Zellen.</p>

<h2>Bakterien: winzige Einzeller</h2>
<p>Bakterien bestehen aus nur <strong>einer einzigen Zelle</strong>. Sie sind etwa 1 bis 5 Tausendstel Millimeter (Mikrometer, µm) groß und gerade noch im Lichtmikroskop zu erkennen. Anders als Pflanzen- und Tierzellen haben Bakterien <strong>keinen Zellkern</strong>: Ihr Erbgut liegt als ringförmiger Faden frei im Zellplasma. Zusätzlich besitzen viele Bakterien kleine Erbgutringe, die <span class="fachwort">Plasmide</span>. Bakterien haben einen eigenen Stoffwechsel, nehmen also Nährstoffe auf und gewinnen daraus Energie.</p>
<p>Lebewesen, deren Zellen keinen Zellkern haben, nennt man <span class="fachwort">Prokaryoten</span> (griechisch: „vor dem Kern“). Pflanzen, Tiere, Pilze und Menschen bestehen dagegen aus Zellen mit Zellkern. Sie heißen <span class="fachwort">Eukaryoten</span>.</p>

<figure><div class="bild">""" + SVG_BAKTERIUM_VIRUS + """</div>
<figcaption>Bau eines Bakteriums und eines Virus (schematisch, nicht im gleichen Maßstab: Das Virus ist in Wirklichkeit etwa zwanzigmal kleiner).</figcaption></figure>

<h3>Vermehrung durch Zweiteilung</h3>
<p>Bakterien vermehren sich, indem sie sich in zwei Tochterzellen teilen. Vorher verdoppeln sie ihr Erbgut. Unter guten Bedingungen (Wärme, Feuchtigkeit, Nährstoffe) teilen sich manche Bakterien etwa <strong>alle 20 Minuten</strong>. Aus einem einzigen Bakterium können so nach wenigen Stunden Millionen werden.</p>
<!--FIG:zweiteilung-->

<p><a class="knopf leise" href="../modelle/lichtmikroskop.html">Bakterien im virtuellen Mikroskop ansehen</a></p>

<h3>Wann Bakterien gut wachsen – und wie sie schlechte Zeiten überstehen</h3>
<p>Die meisten Bakterien, die uns krank machen können, vermehren sich am besten bei Temperaturen zwischen <strong>20 und 40 °C</strong>, also auch bei unserer Körpertemperatur von 37 °C. Im Kühlschrank wachsen sie nur langsam, beim Kochen über 70 °C sterben die meisten ab.</p>
<p>Werden die Bedingungen schlecht, etwa weil es zu trocken, zu heiß oder zu kalt ist, bilden manche Bakterien <span class="fachwort">Sporen</span>. Das ist ein Ruhezustand mit einer dicken, widerstandsfähigen Hülle. Sporen können Hitze, Kälte und Trockenheit überstehen und so Jahrzehnte, vermutlich sogar Tausende Jahre überleben. Verbessern sich die Bedingungen, wachsen aus den Sporen wieder aktive Bakterien. Auch der Tetanus-Erreger überdauert als Spore in der Erde.</p>

<h3>Bakterien sind meistens nützlich</h3>
<p>Nur wenige Bakterienarten machen krank. Die meisten sind harmlos oder sogar unverzichtbar:</p>
<ul>
  <li><strong>Zersetzer in der Natur:</strong> Bakterien bauen gemeinsam mit Pilzen tote Pflanzen und Tiere ab. Dabei entstehen Mineralstoffe, die Pflanzen wieder aufnehmen können. Ohne diese <span class="fachwort">Zersetzer</span> würden sich Laub und Tierleichen immer höher auftürmen.</li>
  <li><strong>Lebensmittel:</strong> Milchsäurebakterien machen aus Milch Joghurt, Quark und Käse, aus Weißkohl Sauerkraut.</li>
  <li><strong>Medikamente:</strong> Gentechnisch veränderte Bakterien stellen Insulin für Menschen mit Diabetes her.</li>
  <li><strong>Verdauung:</strong> Darmbakterien helfen beim Verdauen und schützen vor Krankheitserregern.</li>
</ul>
<p>Gegen krankmachende Bakterien helfen <span class="fachwort">Antibiotika</span>, zum Beispiel der Wirkstoff <strong>Penicillin</strong>. Krankheiten durch Bakterien sind etwa Tetanus, Keuchhusten, Tuberkulose oder Salmonellen-Vergiftungen. Mehr dazu findest du im Lerntext <a href="07-krankheiten-steckbriefe.html">Krankheiten durch Bakterien und Viren</a>.</p>

<h2>Viren: Erbgut in einer Hülle</h2>
<p>Viren sind noch viel kleiner, meist nur 20 bis 300 Millionstel Millimeter (Nanometer), also 0,02 bis 0,3 µm. Die Abkürzung µm steht für <strong>Mikrometer</strong>, ein Tausendstel Millimeter. Man kann sie nur im Elektronenmikroskop sehen. Ein Virus besteht im Wesentlichen aus <strong>Erbgut in einer Eiweißhülle</strong>. Viren haben keinen eigenen Stoffwechsel und können sich <strong>nicht selbst vermehren</strong>. Deshalb zählen sie nicht zu den Lebewesen.</p>

<h3>Vermehrung nur in Wirtszellen</h3>
<ol>
  <li><strong>Andocken:</strong> Das Virus heftet sich mit passenden Andockstellen an eine Körperzelle, die <span class="fachwort">Wirtszelle</span>.</li>
  <li><strong>Eindringen:</strong> Das Virus oder sein Erbgut gelangt in die Wirtszelle.</li>
  <li><strong>Erbgut freisetzen:</strong> Die Eiweißhülle löst sich auf, das Erbgut des Virus liegt frei in der Zelle.</li>
  <li><strong>Umprogrammieren und Vermehren:</strong> Die Wirtszelle wird umprogrammiert. Sie vervielfältigt das Virus-Erbgut und stellt nach seinem Bauplan neue Hüllbausteine her.</li>
  <li><strong>Zusammenbau:</strong> Aus Erbgut und Hüllbausteinen entstehen viele neue Viren.</li>
  <li><strong>Freisetzung:</strong> Die neuen Viren verlassen die Zelle, die dabei oft zugrunde geht, und befallen weitere Zellen.</li>
</ol>
<!--FIG:virusvermehrung-->
<p>Viren lösen zum Beispiel Erkältungen, Grippe, Masern, Windpocken oder COVID-19 aus.</p>

<div class="tabelle-scroll"><table>
  <thead><tr><th></th><th>Bakterien</th><th>Viren</th></tr></thead>
  <tbody>
    <tr><th scope="row">Größe</th><td>ca. 1–5 µm, im Lichtmikroskop sichtbar</td><td>ca. 0,02–0,3 µm, nur im Elektronenmikroskop sichtbar</td></tr>
    <tr><th scope="row">Bau</th><td>Zelle ohne Zellkern: Zellwand, Zellmembran, Zellplasma, Erbgut, Ribosomen</td><td>keine Zelle: Erbgut in einer Eiweißhülle</td></tr>
    <tr><th scope="row">Stoffwechsel</th><td>ja</td><td>nein</td></tr>
    <tr><th scope="row">Vermehrung</th><td>selbstständig durch Zweiteilung</td><td>nur in Wirtszellen</td></tr>
    <tr><th scope="row">Lebewesen?</th><td>ja</td><td>nein</td></tr>
    <tr><th scope="row">Antibiotika wirken?</th><td>ja</td><td>nein</td></tr>
  </tbody>
</table></div>

<div class="merke"><strong>Merke</strong>
<p>Bakterien sind Einzeller ohne Zellkern, die sich durch Zweiteilung selbst vermehren. Viren sind keine Zellen: Sie bestehen aus Erbgut in einer Eiweißhülle und können sich nur in Wirtszellen vermehren.</p></div>
"""
},
{
"slug": "03-das-immunsystem",
"titel": "Das Immunsystem",
"kurz": "Wie unser Körper sich mit unspezifischer und spezifischer Abwehr gegen Erreger wehrt.",
"inhalt": """
<p class="lead">Jeden Tag kommen wir mit unzähligen Krankheitserregern in Kontakt – und werden trotzdem nur selten krank. Das verdanken wir unserem Immunsystem.</p>

<h2>Wo das Immunsystem sitzt</h2>
<p>Das Immunsystem ist kein einzelnes Organ. Es besteht vor allem aus den <span class="fachwort">weißen Blutzellen</span>, die im Blut und in der Lymphe durch den ganzen Körper wandern. Gebildet werden sie im <strong>Knochenmark</strong>. Wichtige Stationen sind außerdem die Lymphknoten, die Milz, die Mandeln und der Thymus.</p>

<h2>Die unspezifische Abwehr</h2>
<p>Die unspezifische Abwehr richtet sich gegen <strong>alle</strong> Eindringlinge gleich. Sie ist sofort zur Stelle.</p>
<!--FIG:abwehr_koerper-->
<ul>
  <li><strong>Äußere Schranken:</strong> Die Haut hält Erreger ab. Schleimhäute in Nase und Atemwegen fangen sie ein, Flimmerhärchen befördern sie nach draußen. Tränenflüssigkeit und Speichel enthalten Stoffe, die Bakterien schädigen, und die Magensäure tötet viele Erreger in der Nahrung ab.</li>
  <li><strong>Fresszellen:</strong> Gelangen Erreger trotzdem in den Körper, etwa durch eine Wunde, umfließen und verdauen <span class="fachwort">Fresszellen</span> sie.</li>
  <li><strong>Entzündung und Fieber:</strong> Die betroffene Stelle wird stärker durchblutet, rot, warm und schwillt an. So gelangen mehr Abwehrzellen dorthin. Fieber verlangsamt die Vermehrung vieler Erreger.</li>
</ul>

<h2>Die spezifische Abwehr</h2>
<p>Reicht das nicht aus, startet die spezifische Abwehr. Sie richtet sich <strong>gezielt gegen einen bestimmten Erreger</strong>. Dazu erkennt sie Merkmale an seiner Oberfläche, die <span class="fachwort">Antigene</span>.</p>
<ol>
  <li><strong>Erkennen:</strong> Fresszellen nehmen Erreger auf und präsentieren deren Antigene an ihrer Oberfläche.</li>
  <li><strong>Alarm:</strong> <span class="fachwort">T-Helferzellen</span> erkennen die präsentierten Antigene und geben Alarm. Sie aktivieren B-Zellen und Killerzellen, die genau zu diesem Antigen passen.</li>
  <li><strong>Antikörper bilden:</strong> Aktivierte B-Zellen vermehren sich und werden zu <span class="fachwort">Plasmazellen</span>. Diese stellen große Mengen <span class="fachwort">Antikörper</span> her. Antikörper passen zu den Antigenen wie ein Schlüssel zum Schloss. Sie heften sich an die Erreger, verklumpen sie und machen sie unschädlich. Fresszellen räumen die Klumpen anschließend weg.</li>
  <li><strong>Infizierte Zellen beseitigen:</strong> <span class="fachwort">Killerzellen</span> erkennen Körperzellen, die schon von Viren befallen sind, und zerstören sie, damit sich die Viren nicht weiter vermehren.</li>
  <li><strong>Erinnern:</strong> Am Ende bleiben langlebige <span class="fachwort">Gedächtniszellen</span> zurück. Sie „merken“ sich den Erreger.</li>
</ol>

<div class="merke"><strong>Merke: Schlüssel-Schloss-Prinzip</strong>
<p>Jeder Antikörper passt nur zu einem ganz bestimmten Antigen, so wie ein Schlüssel nur in ein bestimmtes Schloss passt. Deshalb heißt diese Abwehr spezifisch.</p></div>

<h2>Warum man manche Krankheiten nur einmal bekommt</h2>
<p>Beim ersten Kontakt mit einem Erreger dauert es etwa eine Woche, bis genug passende Antikörper gebildet sind. In dieser Zeit wird man krank. Trifft man später erneut auf denselben Erreger, erkennen die Gedächtniszellen ihn sofort. Die Abwehr läuft dann viel schneller und stärker ab, oft bemerkt man gar nichts. Man ist <span class="fachwort">immun</span>.</p>

<figure><div class="bild">""" + SVG_ANTIKOERPER_KURVE + """</div>
<figcaption>Antikörpermenge im Blut beim ersten und zweiten Kontakt mit demselben Erreger (vereinfachte Darstellung).</figcaption></figure>

<div class="wusstest"><strong>Schon gewusst?</strong>
<p>Grippeviren verändern ihre Antigene ständig ein wenig. Die Gedächtniszellen erkennen die neue Variante dann nicht mehr sicher. Deshalb kann man jedes Jahr wieder Grippe bekommen, und deshalb wird der Grippeimpfstoff jedes Jahr angepasst.</p></div>
"""
},
{
"slug": "04-impfen",
"titel": "Impfen",
"kurz": "Schutzimpfung und Heilimpfung, die Geschichte des Impfens und der Impfausweis.",
"inhalt": """
<p class="lead">Krank werden, um immun zu sein – das muss nicht sein. Mit einer Impfung lernt das Immunsystem einen Erreger kennen, ohne dass man die Krankheit durchmachen muss.</p>

<h2>Wie alles begann: Edward Jenner</h2>
<p>Pocken waren über Jahrhunderte eine der gefährlichsten Krankheiten. Der englische Landarzt <strong>Edward Jenner</strong> beobachtete, dass Melkerinnen, die sich bei Kühen mit den harmlosen <em>Kuhpocken</em> angesteckt hatten, später nicht an Pocken erkrankten. 1796 übertrug er Material aus einer Kuhpocken-Blase auf den achtjährigen James Phipps. Einige Wochen später brachte er bei dem Jungen Material aus echten Pockenblasen in die Haut ein. James erkrankte nicht. Aus dem lateinischen Wort <em>vacca</em> für Kuh entstand später der Begriff <span class="fachwort">Vakzination</span> (Impfung).</p>
<p>Heute wäre ein solcher Versuch an einem Kind verboten. Medizinische Forschung muss strengen ethischen Regeln folgen. Jenners Entdeckung führte aber dazu, dass die Pocken weltweit bekämpft wurden: 1980 erklärte die WHO sie für ausgerottet.</p>

<h2>Weitere Meilensteine</h2>
<ul>
  <li><strong>Louis Pasteur</strong> (Frankreich) entwickelte Impfstoffe aus <em>abgeschwächten</em> Erregern. 1885 impfte er erfolgreich einen Jungen, der von einem tollwütigen Hund gebissen worden war.</li>
  <li><strong>Robert Koch</strong> (Deutschland) wies nach, dass bestimmte Bakterien bestimmte Krankheiten auslösen, etwa Milzbrand und Tuberkulose.</li>
  <li><strong>Emil von Behring</strong> (Deutschland) gewann um 1890 aus dem Blut von Tieren ein <em>Heilserum</em> mit fertigen Antikörpern gegen Diphtherie. Damit konnten erkrankte Kinder gerettet werden. Er erhielt dafür 1901 den ersten Nobelpreis für Medizin.</li>
</ul>
<!--FIG:zeitstrahl_impfen-->

<h2>Schutzimpfung und Heilimpfung</h2>
<div class="tabelle-scroll"><table>
  <thead><tr><th></th><th>Schutzimpfung (aktive Immunisierung)</th><th>Heilimpfung (passive Immunisierung)</th></tr></thead>
  <tbody>
    <tr><th scope="row">Was wird gegeben?</th><td>abgeschwächte oder abgetötete Erreger, Teile davon oder ein Bauplan für ein Erreger-Eiweiß</td><td>fertige Antikörper (Heilserum)</td></tr>
    <tr><th scope="row">Was macht der Körper?</th><td>bildet selbst Antikörper und Gedächtniszellen</td><td>nutzt die fremden Antikörper, bildet selbst keine</td></tr>
    <tr><th scope="row">Wann wirkt sie?</th><td>nach einigen Tagen bis Wochen</td><td>sofort</td></tr>
    <tr><th scope="row">Wie lange schützt sie?</th><td>lange, oft viele Jahre (Auffrischung nötig)</td><td>nur wenige Wochen, da Antikörper abgebaut werden</td></tr>
    <tr><th scope="row">Wofür?</th><td>Vorbeugung, bevor man Kontakt mit dem Erreger hat</td><td>Behandlung, wenn eine Ansteckung schon passiert sein könnte</td></tr>
    <tr><th scope="row">Beispiel</th><td>Masern-, Tetanus- oder Grippeimpfung</td><td>Tetanus-Antikörper nach einer verschmutzten Wunde ohne Impfschutz</td></tr>
  </tbody>
</table></div>

<div class="merke"><strong>Merke</strong>
<p>Bei der Schutzimpfung bildet der Körper selbst Antikörper und Gedächtniszellen. Sie wirkt langsam, aber lange. Bei der Heilimpfung bekommt man fertige Antikörper. Sie wirkt sofort, aber nur kurz.</p></div>

<h2>Der Impfausweis</h2>
<p>Jede Impfung wird im <span class="fachwort">Impfausweis</span> eingetragen: das Datum, gegen welche Krankheit geimpft wurde, der Name des Impfstoffs mit Chargennummer und Stempel und Unterschrift der Ärztin oder des Arztes. So lässt sich jederzeit nachprüfen, wogegen man geschützt ist und wann eine <strong>Auffrischimpfung</strong> fällig ist. In Deutschland gibt die <strong>Ständige Impfkommission (STIKO)</strong> am Robert Koch-Institut Empfehlungen, wer wann gegen was geimpft werden sollte.</p>

<h2>Gemeinschaftsschutz</h2>
<p>Wenn viele Menschen geimpft sind, kann sich ein Erreger kaum noch ausbreiten. Davon profitieren auch Menschen, die selbst nicht geimpft werden können, etwa Neugeborene oder Menschen mit einem geschwächten Immunsystem. Das nennt man <span class="fachwort">Gemeinschaftsschutz</span> oder Herdenimmunität.</p>
<!--FIG:gemeinschaftsschutz-->
"""
},
{
"slug": "05-antibiotika-und-resistenz",
"titel": "Antibiotika und Resistenz",
"kurz": "Wie Antibiotika wirken, warum sie bei Viren nicht helfen und wie Resistenzen entstehen.",
"inhalt": """
<p class="lead">Ein Schimmelpilz, der zufällig auf eine Bakterienkultur fiel, veränderte die Medizin. Doch die Wunderwaffe wird stumpf, wenn wir sie falsch einsetzen.</p>

<h2>Die Entdeckung des Penicillins</h2>
<p>1928 kam der schottische Forscher <strong>Alexander Fleming</strong> aus dem Urlaub zurück und fand in seinem Labor eine Bakterienkultur, auf der ein Schimmelpilz gewachsen war. Rund um den Pilz waren die Bakterien abgestorben. Fleming schloss daraus, dass der Pilz einen Stoff abgibt, der Bakterien tötet. Er nannte ihn nach dem Pilz <em>Penicillium</em> <span class="fachwort">Penicillin</span>. Erst rund zehn Jahre später gelang es anderen Forschern, Penicillin in größeren Mengen herzustellen. Seit den 1940er-Jahren rettet es Millionen Menschenleben.</p>

<h2>Wie Antibiotika wirken</h2>
<p><span class="fachwort">Antibiotika</span> sind Stoffe, die Bakterien abtöten oder ihre Vermehrung hemmen. Manche stören zum Beispiel den Aufbau der Zellwand, andere den Stoffwechsel der Bakterien. Weil Viren weder eine Zellwand noch einen eigenen Stoffwechsel haben, sind <strong>Antibiotika gegen Viren wirkungslos</strong>. Bei einer gewöhnlichen Erkältung oder Grippe helfen sie also nicht.</p>

<h2>Wie Resistenzen entstehen</h2>
<p>Bakterien vermehren sich sehr schnell. Dabei verändert sich ihr Erbgut manchmal zufällig. Ganz selten entsteht so ein Bakterium, dem ein bestimmtes Antibiotikum nichts anhaben kann. Es ist <span class="fachwort">resistent</span>.</p>
<ol>
  <li>In einer Bakterienpopulation gibt es zufällig einige wenige resistente Bakterien.</li>
  <li>Das Antibiotikum tötet die empfindlichen Bakterien. Die resistenten überleben.</li>
  <li>Die resistenten Bakterien vermehren sich ungestört weiter und haben nun den Platz für sich.</li>
  <li>Bakterien können ihre Resistenz sogar über <strong>Plasmide</strong> an andere Bakterien weitergeben.</li>
</ol>
<!--FIG:resistenz_bilder-->
<p>Das Antibiotikum macht die Bakterien also nicht resistent. Es sorgt aber dafür, dass sich die zufällig resistenten durchsetzen. Diesen Vorgang nennt man <span class="fachwort">Selektion</span>.</p>

<div class="merke"><strong>Merke</strong>
<p>Antibiotika wirken nur gegen Bakterien, nicht gegen Viren. Je häufiger Antibiotika eingesetzt werden, desto mehr setzen sich resistente Bakterien durch.</p></div>

<h2>Was jeder tun kann</h2>
<ul>
  <li>Antibiotika nur nehmen, wenn eine Ärztin oder ein Arzt sie verschrieben hat.</li>
  <li>Sie genau so einnehmen wie verordnet: in der richtigen Menge, zur richtigen Zeit und so lange wie besprochen. Nicht eigenmächtig abbrechen.</li>
  <li>Reste nicht aufheben, nicht an andere weitergeben und nicht in den Ausguss oder die Toilette schütten.</li>
  <li>Nicht nach Antibiotika verlangen, wenn man „nur“ eine Erkältung hat.</li>
</ul>

<div class="wusstest"><strong>Schon gewusst?</strong>
<p>Besonders gefürchtet sind <strong>multiresistente Erreger</strong>, gegen die mehrere Antibiotika nicht mehr wirken. Sie kommen vor allem in Krankenhäusern vor. Deshalb ist dort gründliche Händedesinfektion so wichtig. Auch der Einsatz von Antibiotika in der Tierhaltung trägt zur Entstehung von Resistenzen bei.</p></div>
"""
},
{
"slug": "06-allergien-und-unvertraeglichkeiten",
"titel": "Allergien und Unverträglichkeiten",
"kurz": "Wenn das Immunsystem überreagiert – und warum Laktoseintoleranz keine Allergie ist.",
"inhalt": """
<p class="lead">Niesen im Frühling, juckende Augen bei Katzen, Bauchweh nach dem Kakao: Nicht immer steckt ein Krankheitserreger dahinter.</p>

<h2>Allergie: Fehlalarm im Immunsystem</h2>
<p>Bei einer <span class="fachwort">Allergie</span> reagiert das Immunsystem auf eigentlich harmlose Stoffe, als wären sie gefährliche Erreger. Diese Stoffe heißen <span class="fachwort">Allergene</span>. Häufige Allergene sind Blütenpollen, Ausscheidungen von Hausstaubmilben, Tierhaare und -schuppen, Insektengift und bestimmte Lebensmittel wie Erdnüsse, Milch oder Ei.</p>

<h3>So entsteht eine Allergie</h3>
<ol>
  <li><strong>Sensibilisierung beim ersten Kontakt:</strong> Das Immunsystem hält das Allergen fälschlich für gefährlich und bildet passende Antikörper. Diese setzen sich auf bestimmte Abwehrzellen im Gewebe, die <span class="fachwort">Mastzellen</span>. Man merkt davon noch nichts.</li>
  <li><strong>Allergische Reaktion bei jedem weiteren Kontakt:</strong> Das Allergen bindet an die Antikörper auf den Mastzellen. Diese schütten daraufhin den Botenstoff <span class="fachwort">Histamin</span> aus.</li>
  <li><strong>Beschwerden:</strong> Histamin löst die typischen Symptome aus: laufende Nase, Niesen, juckende Augen, Hautausschlag, Schwellungen oder Atemnot.</li>
</ol>
<!--FIG:allergie_ablauf-->
<p>Die allergische Reaktion nutzt also dieselben Werkzeuge wie die spezifische Abwehr, nur richtet sie sich gegen das Falsche.</p>

<div class="wusstest"><strong>Notfall: allergischer Schock</strong>
<p>Sehr selten reagiert der ganze Körper heftig, zum Beispiel nach einem Wespenstich oder nach Erdnüssen. Der Blutdruck fällt, das Atmen wird schwer. Das ist lebensgefährlich: sofort den Notruf <strong>112</strong> wählen. Betroffene haben oft ein Notfallset mit einem Adrenalin-Pen dabei.</p></div>

<h2>Nahrungsmittelunverträglichkeit: kein Fall fürs Immunsystem</h2>
<p>Bei einer <span class="fachwort">Nahrungsmittelunverträglichkeit</span> ist das Immunsystem nicht beteiligt. Das bekannteste Beispiel ist die <strong>Laktoseintoleranz</strong>. Laktose ist Milchzucker. Damit der Darm ihn aufnehmen kann, muss das Enzym <span class="fachwort">Laktase</span> ihn im Dünndarm in kleinere Zuckerbausteine spalten. Bildet der Körper zu wenig Laktase, gelangt der Milchzucker ungespalten in den Dickdarm. Dort vergären ihn Bakterien. Dabei entstehen Gase, und es kommt zu Blähungen, Bauchschmerzen oder Durchfall.</p>

<div class="tabelle-scroll"><table>
  <thead><tr><th></th><th>Milchallergie</th><th>Laktoseintoleranz</th></tr></thead>
  <tbody>
    <tr><th scope="row">Auslöser</th><td>Eiweiße in der Milch</td><td>Milchzucker (Laktose)</td></tr>
    <tr><th scope="row">Ursache</th><td>Fehlreaktion des Immunsystems</td><td>zu wenig Enzym Laktase</td></tr>
    <tr><th scope="row">Menge</th><td>schon kleinste Mengen lösen Beschwerden aus</td><td>kleine Mengen werden oft vertragen</td></tr>
    <tr><th scope="row">Beschwerden</th><td>Haut, Atemwege, Verdauung, im Extremfall allergischer Schock</td><td>vor allem Verdauung: Blähungen, Bauchweh, Durchfall</td></tr>
    <tr><th scope="row">Laktosefreie Milch?</th><td>hilft nicht, die Eiweiße sind noch enthalten</td><td>hilft, der Milchzucker ist schon gespalten</td></tr>
  </tbody>
</table></div>

<div class="merke"><strong>Merke</strong>
<p>Bei einer Allergie reagiert das Immunsystem fälschlich auf harmlose Stoffe. Bei einer Unverträglichkeit wie der Laktoseintoleranz fehlt dagegen ein Enzym; das Immunsystem ist nicht beteiligt.</p></div>

<h2>Lebensmittel richtig lesen</h2>
<p>In der EU müssen die <strong>14 häufigsten Allergene</strong> auf verpackten Lebensmitteln in der Zutatenliste hervorgehoben werden, zum Beispiel fett gedruckt. Dazu gehören unter anderem Milch, Eier, Erdnüsse, Schalenfrüchte (Nüsse), Gluten, Soja, Fisch und Sellerie. Auch Restaurants und Bäckereien müssen darüber informieren.</p>
"""
},
]
