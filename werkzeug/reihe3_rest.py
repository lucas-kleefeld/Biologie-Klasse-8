"""Reihe 3: Aufgaben, Übungen und Modellseiten."""
import json
from zeichnungen3 import NETZ_KNOTEN, NETZ_KANTEN

AUFGABEN = {
"01-oekosystem-see": [
 ("I", "Erkläre die Begriffe Ökosystem, Biotop und Biozönose am Beispiel eines Sees.", 4),
 ("I", "Nenne je vier abiotische und biotische Faktoren, die auf einen Fisch im See einwirken.", 4),
 ("II", "Beschreibe die Zonen eines Sees vom Ufer bis zur Seemitte und nenne für jede Zone eine typische Pflanze oder ein typisches Tier.", 6),
 ("II", "Erkläre, warum in der Bodenzone eines tiefen Sees keine Pflanzen wachsen.", 3),
 ("II", "Stockente, Haubentaucher und Graureiher leben am selben See. Erläutere mithilfe des Begriffs ökologische Nische, warum sie sich kaum Konkurrenz machen.", 5),
 ("III", "Am Ufer eines Badesees soll das Schilf entfernt werden, damit man besser ins Wasser kommt. Beurteile diesen Plan aus biologischer Sicht.", 6),
],
"02-wasserpflanzen-fotosynthese": [
 ("I", "Gib die Wortgleichung der Fotosynthese an und nenne die Bedingungen, unter denen sie abläuft.", 3),
 ("I", "Nenne drei Angepasstheiten der Seerose an das Leben im Wasser.", 3),
 ("II", "Vergleiche Fotosynthese und Zellatmung in einer Tabelle (Ort, Zeitpunkt, Ausgangsstoffe, Produkte, Energie).", 0),
 ("II", "Erkläre, warum die Spaltöffnungen bei der Seerose auf der Blattoberseite liegen, bei der Wasserpest aber ganz fehlen (Struktur und Funktion).", 5),
 ("II", "Plane ein Experiment, mit dem du zeigen kannst, dass die Wasserpest bei mehr Licht mehr Sauerstoff bildet. Gib Vermutung, Material, Durchführung und die Variable an, die du veränderst.", 8),
 ("III", "Ein Aquarium steht im dunklen Keller. Die Fische schnappen nach einigen Tagen an der Oberfläche nach Luft. Erkläre diese Beobachtung und mache einen Vorschlag, wie man das Problem beheben kann.", 5),
],
"03-nahrungsbeziehungen": [
 ("I", "Erkläre die Begriffe Produzent, Konsument und Destruent und nenne je zwei Beispiele aus dem See.", 4),
 ("I", "Stelle zwei Nahrungsketten aus dem See auf, die beide beim Hecht enden.", 3),
 ("II", "Erkläre, warum ein Nahrungsnetz ein Ökosystem stabiler macht als eine einzelne Nahrungskette.", 4),
 ("II", "Erkläre mithilfe der Energiepyramide, warum es in einem See viel weniger Hechte als Rotaugen gibt.", 4),
 ("II", "Beschreibe den Verlauf der Bestände von Hecht und Rotauge über mehrere Jahre und erkläre die Schwankungen.", 5),
 ("III", "In einem Angelsee werden fast alle Hechte herausgefangen. Stelle begründete Vermutungen an, wie sich die Bestände von Rotaugen, Wasserflöhen und Algen in den folgenden Jahren entwickeln.", 7),
],
"04-see-im-jahreslauf": [
 ("I", "Beschreibe die Dichteanomalie des Wassers.", 3),
 ("I", "Nenne die vier Zustände eines Sees im Jahreslauf mit ihren Fachbegriffen.", 3),
 ("II", "Erkläre, warum ein tiefer See im Winter nicht bis zum Grund zufriert, und welche Bedeutung das für die Fische hat.", 5),
 ("II", "Erkläre, warum es am Grund eines nährstoffreichen Sees im Spätsommer kaum noch Sauerstoff gibt.", 5),
 ("II", "Zeichne den Stoffkreislauf im See als Pfeildiagramm und erkläre, warum man bei der Energie von einem Fluss und nicht von einem Kreislauf spricht.", 0),
 ("III", "Ein Schüler sagt: „Im Herbst atmet der See durch.“ Beurteile diese Aussage.", 5),
],
"05-kleinstlebewesen": [
 ("I", "Erkläre, was man unter Plankton versteht, und unterscheide Phyto- und Zooplankton.", 4),
 ("I", "Nenne die Aufgaben von Wimpern, Nahrungsvakuole und pulsierender Vakuole beim Pantoffeltierchen.", 3),
 ("II", "Vergleiche Pantoffeltierchen und Augentierchen in Bezug auf Bewegung und Ernährung.", 5),
 ("II", "Erkläre, warum das Phytoplankton als wichtigster Produzent im See gilt.", 4),
 ("II", "Mikroskopiere einen Tropfen Teichwasser und fertige eine beschriftete Zeichnung eines Lebewesens an. Gib die Vergrößerung an.", 0),
 ("III", "Das Augentierchen wurde früher mal den Pflanzen, mal den Tieren zugeordnet. Begründe, warum beide Zuordnungen nicht richtig passen.", 5),
],
"06-gewaesser-untersuchen-schuetzen": [
 ("I", "Erkläre den Begriff Zeigerorganismus und nenne zwei Beispiele für sauberes und zwei für stark belastetes Wasser.", 4),
 ("II", "Erkläre, warum biologische Untersuchungen mit Zeigerorganismen mehr über ein Gewässer aussagen können als eine einzelne chemische Messung.", 4),
 ("II", "Beschreibe den Ablauf der Eutrophierung als Ursache-Wirkungs-Kette.", 6),
 ("II", "In einer Bachprobe findet ihr viele Wasserasseln und Egel, aber keine Steinfliegenlarven. Werte das Ergebnis aus und stelle Vermutungen über die Ursache an.", 5),
 ("III", "Ein Landwirt düngt seine Felder bis direkt an einen Bach. Entwickle Vorschläge, wie der Bach geschützt werden kann, und bewerte sie.", 6),
 ("III", "Erstellt in Gruppen einen Untersuchungsplan für einen Bach auf der Kursfahrt: Was messt ihr, was sammelt ihr, wie wertet ihr aus, welche Regeln beachtet ihr?", 0),
],
}

UEBUNGEN = [
{
"slug": "r3-zonen",
"titel": "Sortieren: Wer lebt in welcher Zone?",
"kurz": "Pflanzen und Tiere den Zonen des Sees zuordnen",
"typ": "sortieren",
"anleitung": "Ordne jedes Lebewesen der Zone des Sees zu, in der es typischerweise vorkommt. Klicke dann auf „Prüfen“.",
"daten": {"kategorien": ["Ufer und Röhricht", "Schwimm- und Tauchblatt", "Freiwasser", "Bodenzone"], "eintraege": [
 {"text": "Schilf", "kategorie": "Ufer und Röhricht"},
 {"text": "Erle", "kategorie": "Ufer und Röhricht"},
 {"text": "Teichrohrsänger", "kategorie": "Ufer und Röhricht"},
 {"text": "Seerose", "kategorie": "Schwimm- und Tauchblatt"},
 {"text": "Wasserpest", "kategorie": "Schwimm- und Tauchblatt"},
 {"text": "Laichkraut", "kategorie": "Schwimm- und Tauchblatt"},
 {"text": "Hecht", "kategorie": "Freiwasser"},
 {"text": "Wasserfloh", "kategorie": "Freiwasser"},
 {"text": "Kieselalgen (Plankton)", "kategorie": "Freiwasser"},
 {"text": "Rote Zuckmückenlarve", "kategorie": "Bodenzone"},
 {"text": "Schlammröhrenwurm", "kategorie": "Bodenzone"},
 {"text": "Fäulnisbakterien", "kategorie": "Bodenzone"}
]}
},
{
"slug": "r3-erzeuger",
"titel": "Sortieren: Produzent, Konsument oder Destruent?",
"kurz": "Lebewesen nach ihrer Rolle im Ökosystem ordnen",
"typ": "sortieren",
"anleitung": "Welche Rolle hat das Lebewesen im Ökosystem See? Ordne zu und klicke auf „Prüfen“.",
"daten": {"kategorien": ["Produzent", "Konsument", "Destruent"], "eintraege": [
 {"text": "Grünalge", "kategorie": "Produzent"},
 {"text": "Seerose", "kategorie": "Produzent"},
 {"text": "Schilf", "kategorie": "Produzent"},
 {"text": "Augentierchen im Licht", "kategorie": "Produzent"},
 {"text": "Wasserfloh", "kategorie": "Konsument"},
 {"text": "Rotauge", "kategorie": "Konsument"},
 {"text": "Graureiher", "kategorie": "Konsument"},
 {"text": "Libellenlarve", "kategorie": "Konsument"},
 {"text": "Fäulnisbakterien", "kategorie": "Destruent"},
 {"text": "Wasserpilze", "kategorie": "Destruent"}
]}
},
{
"slug": "r3-nahrungskette",
"titel": "Reihenfolge: Eine Nahrungskette im See",
"kurz": "Vom Produzenten zum Endkonsumenten",
"typ": "reihenfolge",
"anleitung": "Bringe die Glieder der Nahrungskette in die richtige Reihenfolge: vom Gefressenen zum Fresser.",
"daten": {"schritte": [
 "Grünalge (Produzent)",
 "Wasserfloh (Konsument 1. Ordnung)",
 "Libellenlarve (Konsument 2. Ordnung)",
 "Barsch (Konsument 3. Ordnung)",
 "Hecht (Endkonsument)"
]}
},
{
"slug": "r3-fotosynthese-lueckentext",
"titel": "Lückentext: Fotosynthese und Zellatmung",
"kurz": "Die wichtigsten Fachbegriffe einsetzen",
"typ": "lueckentext",
"anleitung": "Fülle die Lücken mit den Wörtern aus dem Wortspeicher. Groß- und Kleinschreibung ist egal.",
"daten": {"text": "<p>Bei der Fotosynthese stellen Pflanzen aus [[Kohlenstoffdioxid|CO2]] und [[Wasser]] den energiereichen Stoff [[Traubenzucker|Glucose]] her. Als Abfallprodukt entsteht [[Sauerstoff]]. Die nötige Energie liefert das [[Licht|Sonnenlicht]], das vom grünen Farbstoff [[Chlorophyll]] in den [[Chloroplasten]] eingefangen wird. Dabei wird Lichtenergie in [[chemische]] Energie umgewandelt.</p><p>Bei der [[Zellatmung]] wird Traubenzucker mit Sauerstoff abgebaut, und die gespeicherte Energie wird wieder frei. Sie findet in den [[Mitochondrien]] statt, und zwar bei allen Lebewesen, Tag und [[Nacht]].</p>"}
},
{
"slug": "r3-jahreslauf",
"titel": "Sortieren: Stagnation oder Zirkulation?",
"kurz": "Beobachtungen am See den Jahreszeiten zuordnen",
"typ": "sortieren",
"anleitung": "Passt die Beschreibung zur Sommerstagnation, zur Winterstagnation oder zu einer Zirkulation (Frühling oder Herbst)?",
"daten": {"kategorien": ["Sommer", "Winter", "Frühling oder Herbst"], "eintraege": [
 {"text": "Oben über 20 °C, unten 4 bis 6 °C.", "kategorie": "Sommer"},
 {"text": "Zwischen warmer und kalter Schicht liegt eine Sprungschicht.", "kategorie": "Sommer"},
 {"text": "Am Grund wird der Sauerstoff knapp, weil Destruenten viel zersetzen.", "kategorie": "Sommer"},
 {"text": "Die Oberfläche ist zugefroren.", "kategorie": "Winter"},
 {"text": "Direkt unter dem Eis ist das Wasser kälter als am Grund.", "kategorie": "Winter"},
 {"text": "Das Wasser ist überall gleich warm.", "kategorie": "Frühling oder Herbst"},
 {"text": "Der Wind durchmischt den ganzen See.", "kategorie": "Frühling oder Herbst"},
 {"text": "Mineralstoffe vom Grund gelangen nach oben.", "kategorie": "Frühling oder Herbst"}
]}
},
{
"slug": "r3-zeiger",
"titel": "Sortieren: Zeigerorganismen und Gewässergüte",
"kurz": "Tiere aus dem Bach der Wassergüte zuordnen",
"typ": "sortieren",
"anleitung": "Ihr habt im Bach Tiere gefunden. Ordne sie der Gewässergüte zu, auf die sie hinweisen.",
"daten": {"kategorien": ["unbelastet", "mäßig belastet", "stark belastet", "sehr stark belastet"], "eintraege": [
 {"text": "Steinfliegenlarve", "kategorie": "unbelastet"},
 {"text": "Eintagsfliegenlarve", "kategorie": "unbelastet"},
 {"text": "Strudelwurm", "kategorie": "unbelastet"},
 {"text": "Bachflohkrebs", "kategorie": "mäßig belastet"},
 {"text": "Flussnapfschnecke", "kategorie": "mäßig belastet"},
 {"text": "Wasserassel", "kategorie": "stark belastet"},
 {"text": "Egel", "kategorie": "stark belastet"},
 {"text": "Rote Zuckmückenlarve", "kategorie": "sehr stark belastet"},
 {"text": "Schlammröhrenwurm", "kategorie": "sehr stark belastet"},
 {"text": "Rattenschwanzlarve", "kategorie": "sehr stark belastet"}
]}
},
{
"slug": "r3-quiz",
"titel": "Quiz: Grundwissen Leben in Gewässern",
"kurz": "12 Fragen quer durch die ganze Reihe",
"typ": "quiz",
"anleitung": "Klicke jeweils auf die Antwort, die du für richtig hältst. Du bekommst sofort eine Rückmeldung.",
"daten": {"fragen": [
 {"frage": "Was gehört zum Biotop eines Sees?", "optionen": ["Wassertemperatur und Licht", "Hechte und Rotaugen", "Algen und Bakterien", "die Nahrungskette"], "richtig": 0, "erklaerung": "Das Biotop ist der Lebensraum mit seinen unbelebten Bedingungen."},
 {"frage": "Welcher Faktor ist ein biotischer Faktor?", "optionen": ["ein Fressfeind", "der pH-Wert", "der Sauerstoffgehalt", "die Wassertemperatur"], "richtig": 0, "erklaerung": "Biotische Faktoren gehen von Lebewesen aus."},
 {"frage": "In welcher Zone wachsen Seerosen?", "optionen": ["Schwimmblattzone", "Röhrichtzone", "Tauchblattzone", "Bodenzone"], "richtig": 0, "erklaerung": "Seerosen wurzeln am Grund, ihre Blätter schwimmen."},
 {"frage": "Wo liegen die Spaltöffnungen der Seerose?", "optionen": ["auf der Blattoberseite", "auf der Blattunterseite", "an den Wurzeln", "Sie hat keine."], "richtig": 0, "erklaerung": "Die Unterseite liegt im Wasser, Gasaustausch ist nur oben möglich."},
 {"frage": "Was entsteht bei der Fotosynthese als Abfallprodukt?", "optionen": ["Sauerstoff", "Kohlenstoffdioxid", "Wasser", "Stickstoff"], "richtig": 0, "erklaerung": "Den Sauerstoff erkennt man bei der Wasserpest an aufsteigenden Bläschen."},
 {"frage": "Welche Lebewesen betreiben Zellatmung?", "optionen": ["alle Lebewesen", "nur Tiere", "nur Pflanzen", "nur Bakterien"], "richtig": 0, "erklaerung": "Auch Pflanzen brauchen Energie und atmen Tag und Nacht."},
 {"frage": "Wie viel Energie gelangt ungefähr von einer Trophieebene in die nächste?", "optionen": ["etwa 10 %", "etwa 50 %", "etwa 90 %", "100 %"], "richtig": 0, "erklaerung": "Der Rest wird für Bewegung, Wärme und Atmung verbraucht."},
 {"frage": "Welche Aufgabe haben Destruenten?", "optionen": ["Sie zersetzen totes Material zu Mineralstoffen.", "Sie stellen Traubenzucker her.", "Sie fressen nur Fische.", "Sie bilden Sauerstoff."], "richtig": 0, "erklaerung": "Ohne Destruenten gäbe es keinen Stoffkreislauf."},
 {"frage": "Bei welcher Temperatur hat Wasser die größte Dichte?", "optionen": ["4 °C", "0 °C", "10 °C", "20 °C"], "richtig": 0, "erklaerung": "Deshalb ist es am Grund eines tiefen Sees fast immer 4 °C kalt."},
 {"frage": "Was passiert bei der Herbstzirkulation?", "optionen": ["Der See wird ganz durchmischt.", "Der See friert zu.", "Es bildet sich eine Sprungschicht.", "Die Algen sterben alle ab."], "richtig": 0, "erklaerung": "Das Wasser ist überall gleich warm, der Wind kann es umwälzen."},
 {"frage": "Welcher Zeigerorganismus spricht für sehr sauberes Wasser?", "optionen": ["Steinfliegenlarve", "Schlammröhrenwurm", "Rote Zuckmückenlarve", "Wasserassel"], "richtig": 0, "erklaerung": "Sie braucht viel Sauerstoff."},
 {"frage": "Warum entsteht bei der Eutrophierung Sauerstoffmangel?", "optionen": ["Destruenten verbrauchen beim Zersetzen der vielen toten Algen Sauerstoff.", "Algen atmen keinen Sauerstoff aus.", "Dünger ist giftig für Sauerstoff.", "Fische verbrauchen mehr Sauerstoff."], "richtig": 0, "erklaerung": "Je mehr totes Material, desto mehr Zersetzung und Sauerstoffverbrauch."}
]}
},
]

TRAINING = [
{
"slug": "r3-fachbegriffe",
"titel": "Fachbegriffe: Ökosystem See",
"kurz": "Die wichtigsten Begriffe der Reihe zuordnen",
"typ": "zuordnen",
"anleitung": "Wähle für jeden Fachbegriff die passende Erklärung. Die Lösung kannst du ansehen, sobald alles zugeordnet ist.",
"daten": {"paare": [
 {"links": "Biotop", "rechts": "Lebensraum mit seinen unbelebten Bedingungen"},
 {"links": "Biozönose", "rechts": "Lebensgemeinschaft aller Lebewesen in einem Lebensraum"},
 {"links": "abiotischer Faktor", "rechts": "Einfluss der unbelebten Umwelt, z. B. Licht"},
 {"links": "ökologische Nische", "rechts": "Art und Weise, wie eine Art ihren Lebensraum nutzt"},
 {"links": "Produzent", "rechts": "stellt durch Fotosynthese selbst Nährstoffe her"},
 {"links": "Destruent", "rechts": "zersetzt totes Material zu Mineralstoffen"},
 {"links": "Trophieebene", "rechts": "Stufe in der Nahrungspyramide"},
 {"links": "Sprungschicht", "rechts": "Schicht, in der die Temperatur schnell abnimmt"},
 {"links": "Plankton", "rechts": "Lebewesen, die im Wasser schweben"},
 {"links": "Eutrophierung", "rechts": "Überdüngung eines Gewässers"},
 {"links": "Neozoon", "rechts": "Tierart, die durch den Menschen in ein neues Gebiet kam"}
]}
},
{
"slug": "r3-eutrophierung",
"titel": "Reihenfolge: Ein See kippt um",
"kurz": "Die Ursache-Wirkungs-Kette der Eutrophierung ordnen",
"typ": "reihenfolge",
"anleitung": "Bringe die Schritte der Eutrophierung in die richtige Reihenfolge und klicke auf „Prüfen“.",
"daten": {"schritte": [
 "Dünger von Feldern und Abwasser gelangen in den See.",
 "Nitrat und Phosphat sind plötzlich reichlich vorhanden.",
 "Algen vermehren sich massenhaft, das Wasser wird grün und trüb.",
 "Wasserpflanzen am Grund bekommen zu wenig Licht und sterben ab.",
 "Abgestorbene Algen und Pflanzen sinken zum Grund.",
 "Destruenten zersetzen das tote Material und verbrauchen viel Sauerstoff.",
 "Am Grund herrscht Sauerstoffmangel, Fische sterben, Faulschlamm entsteht."
]}
},
{
"slug": "r3-schreiben",
"titel": "Schreibtraining: Den See erklären",
"kurz": "Nahrungsbeziehungen und Jahreslauf in eigenen Worten",
"typ": "schreiben",
"anleitung": "Beantworte die Aufgaben in ganzen Sätzen. Erst wenn du genug geschrieben hast, kannst du deinen Text mit einer Musterlösung vergleichen.",
"daten": {"aufgaben": [
 {"frage": "Erkläre die Nahrungsbeziehungen im See. Verwende die Begriffe Produzent, Konsument, Destruent, Nahrungsnetz und Energiepyramide.",
  "hinweis": "Tipp: Beginne bei den Algen und arbeite dich zum Hecht vor. Vergiss die Destruenten nicht.",
  "minWoerter": 60,
  "checkliste": ["Ich habe erklärt, was Produzenten sind, mit Beispiel.", "Ich habe Konsumenten verschiedener Ordnung mit Beispielen genannt.", "Ich habe die Rolle der Destruenten erklärt.", "Ich habe erklärt, warum man von einem Nahrungsnetz spricht.", "Ich habe erklärt, dass von Stufe zu Stufe etwa 90 % der Energie verloren gehen.", "Ich habe Fachbegriffe richtig verwendet."],
  "muster": "Am Anfang aller Nahrungsbeziehungen im See stehen die Produzenten: Algen und Wasserpflanzen stellen durch Fotosynthese mithilfe von Licht Traubenzucker her. Von ihnen ernähren sich Konsumenten 1. Ordnung wie Wasserflöhe und Schnecken. Diese werden von Konsumenten 2. Ordnung gefressen, zum Beispiel vom Rotauge oder vom Barsch. An der Spitze stehen Konsumenten 3. Ordnung wie Hecht und Graureiher. Weil die meisten Tiere verschiedene Nahrung fressen und von verschiedenen Tieren gefressen werden, sind die Nahrungsketten zu einem Nahrungsnetz verknüpft. Das macht das Ökosystem stabiler. Abgestorbene Lebewesen und Ausscheidungen werden von Destruenten wie Bakterien und Pilzen zersetzt. Sie setzen Mineralstoffe frei, die die Produzenten wieder aufnehmen. Von einer Stufe zur nächsten gelangen nur etwa 10 Prozent der Energie, der Rest wird für Bewegung und Wärme verbraucht. Deshalb ist die Energiepyramide unten breit und oben schmal, und es gibt viel mehr Algen als Hechte."},
 {"frage": "Beschreibe, wie sich ein tiefer See im Laufe eines Jahres verändert, und erkläre, welche Rolle die Dichteanomalie des Wassers dabei spielt.",
  "hinweis": "Tipp: Gehe die vier Jahreszeiten durch und nenne jeweils Temperatur, Schichtung und Sauerstoff.",
  "minWoerter": 60,
  "checkliste": ["Ich habe erklärt, dass Wasser bei 4 °C die größte Dichte hat.", "Ich habe die Sommerstagnation mit Sprungschicht beschrieben.", "Ich habe die Herbstzirkulation beschrieben.", "Ich habe die Winterstagnation unter dem Eis beschrieben.", "Ich habe die Frühjahrszirkulation beschrieben.", "Ich habe erklärt, was mit Sauerstoff und Mineralstoffen passiert."],
  "muster": "Wasser hat bei 4 °C seine größte Dichte. Deshalb sammelt sich am Grund eines tiefen Sees das ganze Jahr über etwa 4 °C kaltes Wasser. Im Sommer erwärmt die Sonne die oberen Schichten auf über 20 °C. Darunter liegt die Sprungschicht, in der die Temperatur schnell abnimmt, und ganz unten kaltes Tiefenwasser. Die Schichten mischen sich nicht, man spricht von Sommerstagnation. Am Grund verbrauchen Destruenten Sauerstoff, der nicht ersetzt wird. Im Herbst kühlt die Oberfläche ab, bis der See überall gleich warm ist. Dann kann der Wind ihn ganz durchmischen: Sauerstoff gelangt nach unten, Mineralstoffe nach oben. Das ist die Herbstzirkulation. Im Winter kühlt das Oberflächenwasser unter 4 °C ab und gefriert. Weil kaltes Wasser und Eis leichter sind, bleiben sie oben, und am Grund ist es weiterhin 4 °C warm. Die Fische können dort überwintern. Im Frühling schmilzt das Eis, der See ist wieder überall 4 °C warm und wird bei der Frühjahrszirkulation durchmischt."}
]}
},
]

# ---------------------------------------------------------------- Modellseiten
SEE = """
<p class="lead">Wähle eine Jahreszeit und sieh dir an, wie warm das Wasser in welcher Tiefe ist und wie viel Sauerstoff es enthält. Tippe auf eine Zone des Sees, um mehr über sie zu erfahren.</p>
<div class="modell" id="se">
  <div class="wahl" role="group" aria-label="Jahreszeit wählen">
    <button type="button" data-zeit="fruehling" aria-pressed="false">Frühling</button>
    <button type="button" data-zeit="sommer" aria-pressed="true">Sommer</button>
    <button type="button" data-zeit="herbst" aria-pressed="false">Herbst</button>
    <button type="button" data-zeit="winter" aria-pressed="false">Winter</button>
  </div>
  <svg id="se-bild" class="ill" viewBox="0 0 760 420" role="img" aria-label="See im Querschnitt mit Temperatur- und Sauerstoffkurve"></svg>
  <div class="wahl" role="group" aria-label="Zone wählen" id="se-zonen">
    <button type="button" data-zone="erle">Erlenbruch</button>
    <button type="button" data-zone="roehricht">Röhricht</button>
    <button type="button" data-zone="schwimm">Schwimmblatt</button>
    <button type="button" data-zone="tauch">Tauchblatt</button>
    <button type="button" data-zone="frei">Freiwasser</button>
    <button type="button" data-zone="boden">Bodenzone</button>
  </div>
  <div class="schritt-text" aria-live="polite"><h3 id="se-titel"></h3><p id="se-text"></p></div>
</div>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Vergleiche die Temperaturkurven im Sommer und im Winter. Erkläre, warum es am Grund in beiden Jahreszeiten etwa 4 °C kalt ist.</li>
  <li>Beschreibe die Sauerstoffkurve im Sommer. Erkläre, warum oben viel und unten wenig Sauerstoff vorhanden ist.</li>
  <li>Erkläre, warum der See im Frühling und Herbst durchmischt werden kann, im Sommer und Winter aber nicht.</li>
  <li>Klicke dich durch die Zonen. Lege eine Tabelle an: Zone, Lichtverhältnisse, typische Pflanzen, typische Tiere.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Die Kurven zeigen einen typischen, tiefen und nährstoffreichen See in Mitteleuropa. Flache Teiche bilden im Sommer meist keine Sprungschicht, weil der Wind sie bis zum Grund durchmischt. Die Werte sind gerundet, und die Zonen gehen in der Natur fließend ineinander über.</p>
"""

FOTO = """
<p class="lead">Ein Stängel Wasserpest steht in einem Reagenzglas mit Wasser. Eine Lampe beleuchtet ihn. Zähle die aufsteigenden Sauerstoffbläschen und finde heraus, was die Fotosynthese beeinflusst.</p>
<div class="modell" id="fo">
  <svg id="fo-bild" class="ill" viewBox="0 0 760 360" role="img" aria-label="Versuchsaufbau mit Lampe, Reagenzglas und Wasserpest"></svg>
  <div class="modell-steuerung">
    <label for="fo-abstand">Abstand der Lampe: <strong id="fo-abstand-t">20 cm</strong></label>
    <input type="range" id="fo-abstand" min="10" max="60" step="5" value="20" class="breit-regler">
  </div>
  <div class="modell-steuerung">
    <label for="fo-temp">Wassertemperatur: <strong id="fo-temp-t">20 °C</strong></label>
    <input type="range" id="fo-temp" min="5" max="45" step="5" value="20" class="breit-regler">
  </div>
  <div class="modell-steuerung">
    <span>Wasser:</span>
    <div class="wahl" role="group" aria-label="Kohlenstoffdioxid im Wasser">
      <button type="button" data-co2="0.15" aria-pressed="false">abgekocht (fast kein CO₂)</button>
      <button type="button" data-co2="1" aria-pressed="true">Leitungswasser</button>
      <button type="button" data-co2="1.6" aria-pressed="false">mit CO₂ angereichert</button>
    </div>
  </div>
  <div class="modell-steuerung">
    <label class="schalter"><input type="checkbox" id="fo-dunkel"> Raum abdunkeln, Lampe aus</label>
  </div>
  <p class="vh-zahl" id="fo-rate" aria-live="polite"></p>
  <div class="knopfreihe"><button class="knopf" type="button" id="fo-notieren">Messwert notieren</button><button class="knopf leise" type="button" id="fo-leeren">Tabelle leeren</button></div>
  <div class="tabelle-scroll"><table id="fo-tabelle"><thead><tr><th>Nr.</th><th>Abstand</th><th>Temperatur</th><th>Wasser</th><th>Bläschen pro Minute</th></tr></thead><tbody></tbody></table></div>
</div>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Stelle eine Vermutung auf, wie die Bläschenzahl vom Abstand der Lampe abhängt. Überprüfe sie: Verändere nur den Abstand und notiere mindestens fünf Messwerte. Zeichne ein Diagramm.</li>
  <li>Untersuche ebenso den Einfluss der Temperatur. Beschreibe, was oberhalb von 35 °C passiert, und stelle eine Vermutung auf, woran das liegt.</li>
  <li>Vergleiche die drei Wassersorten bei gleichem Licht und gleicher Temperatur. Erkläre das Ergebnis mit der Wortgleichung der Fotosynthese.</li>
  <li>Erkläre, warum man immer nur einen Faktor verändern darf, wenn man ein Ergebnis auswerten will.</li>
  <li>Dunkle den Raum ab. Erkläre, warum keine Bläschen mehr aufsteigen, obwohl die Pflanze weiterlebt.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Im echten Versuch schwankt die Bläschenzahl, die Bläschen sind unterschiedlich groß und enthalten nicht nur Sauerstoff. Die Lampe erwärmt außerdem das Wasser, wenn sie nah ist. Die Werte im Modell sind berechnet und sollen nur den typischen Zusammenhang zeigen.</p>
"""

NN_DATEN = json.dumps({
    "knoten": {k: {"x": v[0], "y": v[1], "name": v[2], "f": v[3]} for k, v in NETZ_KNOTEN.items()},
    "kanten": NETZ_KANTEN,
}, ensure_ascii=False)
NETZ = """
<p class="lead">Tippe auf eine Art, um sie aus dem See zu entfernen, zum Beispiel weil sie durch eine Krankheit ausstirbt oder überfischt wird. Das Modell zeigt, welche Arten betroffen sind.</p>
<div class="modell" id="nn">
  <svg id="nn-bild" class="ill" viewBox="0 0 820 340" role="img" aria-label="Nahrungsnetz zum Antippen"></svg>
  <p class="legende"><span class="nn-leg weg"></span> entfernt &nbsp; <span class="nn-leg weniger"></span> verliert Nahrung, wird seltener &nbsp; <span class="nn-leg mehr"></span> weniger Fressfeinde, wird häufiger &nbsp; <span class="nn-leg tot"></span> findet keine Nahrung mehr</p>
  <div class="knopfreihe"><button class="knopf leise" type="button" id="nn-reset">Alle Arten zurück</button></div>
  <div class="schritt-text" aria-live="polite"><h3 id="nn-titel">Wähle eine Art aus</h3><p id="nn-text">Die Pfeile zeigen vom Gefressenen zum Fresser.</p></div>
</div>
<script type="application/json" id="nn-daten">""" + NN_DATEN + """</script>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Entferne den Hecht. Beschreibe, welche Arten häufiger werden, und erkläre, welche Folgen das wiederum für die Wasserflöhe und Algen haben kann.</li>
  <li>Entferne den Wasserfloh. Erkläre, warum keine Art völlig verschwindet, obwohl der Wasserfloh für viele Tiere Nahrung ist.</li>
  <li>Entferne nacheinander Algen und Wasserpflanzen. Erkläre, warum die Produzenten für das ganze Ökosystem unverzichtbar sind.</li>
  <li>Erkläre mithilfe des Modells, warum ein Nahrungsnetz stabiler ist als eine einzelne Nahrungskette.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Ein echtes Nahrungsnetz im See umfasst hunderte Arten. Das Modell zeigt nur die direkten Folgen: Es sagt nicht, wie stark sich die Bestände ändern, und berücksichtigt nicht, dass Tiere auf ganz andere Nahrung ausweichen oder neue Arten einwandern können.</p>
"""

RB = """
<p class="lead">Hechte fressen Rotaugen. Wie entwickeln sich die beiden Bestände über viele Jahre? Starte die Simulation und verändere die Einstellungen.</p>
<div class="modell" id="rb">
  <svg id="rb-bild" class="ill" viewBox="0 0 760 360" role="img" aria-label="Diagramm der Bestände von Rotauge und Hecht"></svg>
  <p class="legende"><span class="rb-leg beute"></span> Rotaugen (Beute) &nbsp; <span class="rb-leg raeuber"></span> Hechte (Räuber, 10-fach überhöht dargestellt)</p>
  <div class="modell-steuerung">
    <label for="rb-vermehrung">Vermehrung der Rotaugen: <strong id="rb-vermehrung-t"></strong></label>
    <input type="range" id="rb-vermehrung" min="1" max="5" value="3" class="breit-regler">
  </div>
  <div class="modell-steuerung">
    <label for="rb-jagd">Jagderfolg der Hechte: <strong id="rb-jagd-t"></strong></label>
    <input type="range" id="rb-jagd" min="1" max="5" value="3" class="breit-regler">
  </div>
  <div class="knopfreihe">
    <button class="knopf" type="button" id="rb-start">Abspielen</button>
    <button class="knopf leise" type="button" id="rb-angeln">Angler fangen die Hälfte der Hechte</button>
    <button class="knopf leise" type="button" id="rb-reset">Neu starten</button>
  </div>
  <div class="schritt-text" aria-live="polite"><p id="rb-text"></p></div>
</div>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Spiele die Simulation ab. Beschreibe den Verlauf der beiden Kurven und erkläre, warum die Kurve der Hechte der Kurve der Rotaugen zeitlich hinterherläuft.</li>
  <li>Erhöhe die Vermehrung der Rotaugen. Beschreibe, wie sich beide Kurven verändern.</li>
  <li>Lass Angler die Hälfte der Hechte fangen. Beschreibe die Folgen in den nächsten Jahren.</li>
  <li>Erkläre, warum es selbst bei vielen Hechten fast nie passiert, dass alle Rotaugen gefressen werden.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Das Modell kennt nur zwei Arten. In einem echten See fressen Hechte auch andere Fische, und Rotaugen haben weitere Feinde. Wetter, Nahrungsangebot, Krankheiten und Angler beeinflussen die Bestände zusätzlich. Echte Messdaten schwanken deshalb viel unregelmäßiger. Das Modell eignet sich, um das Prinzip zu verstehen, nicht für Vorhersagen.</p>
"""

MODELLE = [
 {"slug": "see", "titel": "Modell: Der See im Jahreslauf", "kurz": "Temperatur, Sauerstoff und Zonen eines Sees erkunden", "inhalt": SEE, "skripte": ["assets/reihe3.js"]},
 {"slug": "fotosynthese", "titel": "Modell: Fotosynthese messen", "kurz": "Licht, Temperatur und CO₂ verändern und Bläschen zählen", "inhalt": FOTO, "skripte": ["assets/reihe3.js"]},
 {"slug": "nahrungsnetz", "titel": "Modell: Nahrungsnetz im See", "kurz": "Eine Art entfernen und die Folgen beobachten", "inhalt": NETZ, "skripte": ["assets/reihe3.js"]},
 {"slug": "raeuber-beute", "titel": "Modell: Hecht und Rotauge", "kurz": "Räuber-Beute-Beziehung über viele Jahre simulieren", "inhalt": RB, "skripte": ["assets/reihe3.js"]},
]
