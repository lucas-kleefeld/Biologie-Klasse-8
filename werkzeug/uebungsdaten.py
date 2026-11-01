"""Inhalte der interaktiven Übungen der Reihe 1."""

UEBUNGEN = [
{
"slug": "quiz-grundwissen",
"titel": "Quiz: Grundwissen Abwehr von Krankheiten",
"kurz": "12 Fragen quer durch die ganze Reihe",
"typ": "quiz",
"anleitung": "Klicke jeweils auf die Antwort, die du für richtig hältst. Du bekommst sofort eine Rückmeldung.",
"daten": {"fragen": [
 {"frage": "Wie nennt man die Zeit zwischen der Ansteckung und dem Auftreten der ersten Beschwerden?", "optionen": ["Inkubationszeit", "Genesungszeit", "Sensibilisierung", "Immunität"], "richtig": 0, "erklaerung": "In der Inkubationszeit vermehren sich die Erreger, man merkt aber noch nichts."},
 {"frage": "Welche Aussage über Viren ist richtig?", "optionen": ["Viren vermehren sich nur in Wirtszellen.", "Viren teilen sich durch Zweiteilung.", "Viren haben einen Zellkern.", "Viren lassen sich mit Antibiotika bekämpfen."], "richtig": 0, "erklaerung": "Viren haben keinen eigenen Stoffwechsel und brauchen eine Wirtszelle, die neue Viren für sie herstellt."},
 {"frage": "Wodurch unterscheiden sich Bakterien von Pflanzen- und Tierzellen?", "optionen": ["Sie haben keinen Zellkern.", "Sie haben keine Zellmembran.", "Sie haben kein Erbgut.", "Sie haben keinen Stoffwechsel."], "richtig": 0, "erklaerung": "Das Erbgut der Bakterien liegt frei im Zellplasma, nicht in einem Zellkern."},
 {"frage": "Welche Zellen stellen Antikörper her?", "optionen": ["Plasmazellen", "Fresszellen", "Killerzellen", "rote Blutzellen"], "richtig": 0, "erklaerung": "Aktivierte B-Zellen werden zu Plasmazellen und bilden große Mengen Antikörper."},
 {"frage": "Was beschreibt das Schlüssel-Schloss-Prinzip?", "optionen": ["Ein Antikörper passt nur zu einem bestimmten Antigen.", "Die Haut verschließt den Körper gegen alle Erreger.", "Fresszellen schließen Erreger in sich ein.", "Impfstoffe schließen Viren in Kapseln ein."], "richtig": 0, "erklaerung": "Antikörper und Antigen passen genau zueinander, deshalb ist die Abwehr spezifisch."},
 {"frage": "Warum wird man bei vielen Krankheiten nur einmal krank?", "optionen": ["Gedächtniszellen erkennen den Erreger beim zweiten Kontakt sofort.", "Der Erreger stirbt nach der ersten Krankheit aus.", "Die Antikörper bleiben für immer in großer Menge im Blut.", "Fieber zerstört den Erreger für immer."], "richtig": 0, "erklaerung": "Gedächtniszellen sorgen dafür, dass beim zweiten Kontakt schnell und stark Antikörper gebildet werden."},
 {"frage": "Was bekommt man bei einer Schutzimpfung (aktive Immunisierung)?", "optionen": ["abgeschwächte oder abgetötete Erreger bzw. Teile davon", "fertige Antikörper", "Antibiotika", "Histamin"], "richtig": 0, "erklaerung": "Der Körper bildet daraufhin selbst Antikörper und Gedächtniszellen."},
 {"frage": "Welche Eigenschaft hat die Heilimpfung (passive Immunisierung)?", "optionen": ["Sie wirkt sofort, schützt aber nur kurz.", "Sie wirkt erst nach Wochen, schützt aber lebenslang.", "Sie bildet Gedächtniszellen.", "Sie wirkt nur gegen Bakterien."], "richtig": 0, "erklaerung": "Die fertigen Antikörper wirken sofort, werden aber nach einigen Wochen abgebaut."},
 {"frage": "Wer übertrug 1796 Kuhpocken-Material auf einen Jungen, um ihn vor Pocken zu schützen?", "optionen": ["Edward Jenner", "Alexander Fleming", "Robert Koch", "Ignaz Semmelweis"], "richtig": 0, "erklaerung": "Edward Jenner gilt als Begründer der Impfung."},
 {"frage": "Wie entsteht eine Antibiotikaresistenz in einer Bakterienpopulation?", "optionen": ["Zufällig resistente Bakterien überleben das Antibiotikum und vermehren sich.", "Das Antibiotikum verwandelt Bakterien gezielt in resistente Bakterien.", "Der Mensch wird gegen das Antibiotikum resistent.", "Viren machen Bakterien resistent."], "richtig": 0, "erklaerung": "Das Antibiotikum selektiert die zufällig resistenten Bakterien, es erzeugt die Resistenz nicht."},
 {"frage": "Welcher Botenstoff löst die Beschwerden bei einer allergischen Reaktion aus?", "optionen": ["Histamin", "Laktase", "Penicillin", "Insulin"], "richtig": 0, "erklaerung": "Mastzellen schütten Histamin aus, das zu Juckreiz, Schwellungen oder Niesen führt."},
 {"frage": "Bei welcher Störung hilft laktosefreie Milch?", "optionen": ["Laktoseintoleranz", "Milchallergie", "Pollenallergie", "beiden: Milchallergie und Laktoseintoleranz"], "richtig": 0, "erklaerung": "Bei Laktoseintoleranz fehlt das Enzym Laktase. Bei einer Milchallergie stören die Milcheiweiße, die auch in laktosefreier Milch stecken."}
]}
},
{
"slug": "zuordnen-abwehrzellen",
"titel": "Zuordnen: Wer macht was im Immunsystem?",
"kurz": "Zellen und Begriffe der Abwehr ihren Aufgaben zuordnen",
"typ": "zuordnen",
"anleitung": "Wähle für jeden Begriff die passende Beschreibung aus. Klicke dann auf „Prüfen“.",
"daten": {"paare": [
 {"links": "Fresszelle", "rechts": "umfließt Erreger, verdaut sie und präsentiert ihre Antigene"},
 {"links": "T-Helferzelle", "rechts": "erkennt präsentierte Antigene und aktiviert B-Zellen und Killerzellen"},
 {"links": "Plasmazelle", "rechts": "stellt große Mengen Antikörper her"},
 {"links": "Killerzelle", "rechts": "zerstört Körperzellen, die von Viren befallen sind"},
 {"links": "Gedächtniszelle", "rechts": "erkennt einen Erreger beim zweiten Kontakt sofort wieder"},
 {"links": "Antikörper", "rechts": "bindet nach dem Schlüssel-Schloss-Prinzip an Antigene und verklumpt Erreger"},
 {"links": "Antigen", "rechts": "Merkmal an der Oberfläche eines Erregers"},
 {"links": "Mastzelle", "rechts": "schüttet bei einer Allergie Histamin aus"}
]}
},
{
"slug": "sortieren-bakterien-viren",
"titel": "Sortieren: Bakterien oder Viren?",
"kurz": "Aussagen Bakterien, Viren oder beiden zuordnen",
"typ": "sortieren",
"anleitung": "Entscheide bei jeder Aussage, ob sie auf Bakterien, auf Viren oder auf beide zutrifft. Klicke dann auf „Prüfen“.",
"daten": {"kategorien": ["Bakterien", "Viren", "beide"], "eintraege": [
 {"text": "vermehren sich durch Zweiteilung", "kategorie": "Bakterien"},
 {"text": "haben einen eigenen Stoffwechsel", "kategorie": "Bakterien"},
 {"text": "besitzen eine Zellwand", "kategorie": "Bakterien"},
 {"text": "können mit Antibiotika bekämpft werden", "kategorie": "Bakterien"},
 {"text": "werden zum Joghurtmachen genutzt", "kategorie": "Bakterien"},
 {"text": "sind im Lichtmikroskop zu erkennen", "kategorie": "Bakterien"},
 {"text": "vermehren sich nur in Wirtszellen", "kategorie": "Viren"},
 {"text": "bestehen aus Erbgut in einer Eiweißhülle", "kategorie": "Viren"},
 {"text": "zählen nicht zu den Lebewesen", "kategorie": "Viren"},
 {"text": "lösen Grippe und Masern aus", "kategorie": "Viren"},
 {"text": "enthalten Erbgut", "kategorie": "beide"},
 {"text": "können Krankheiten auslösen", "kategorie": "beide"},
 {"text": "besitzen keinen Zellkern", "kategorie": "beide", "erklaerung": "Bakterien haben keinen Zellkern, Viren sind gar keine Zellen."}
]}
},
{
"slug": "lueckentext-impfen",
"titel": "Lückentext: Impfen",
"kurz": "Schutzimpfung, Heilimpfung und die Geschichte des Impfens",
"typ": "lueckentext",
"anleitung": "Fülle die Lücken mit den Wörtern aus dem Wortspeicher. Groß- und Kleinschreibung ist egal.",
"daten": {"text": "<p>Bei einer [[Schutzimpfung]] werden abgeschwächte oder abgetötete Erreger gespritzt. Der Körper bildet daraufhin selbst [[Antikörper]] und [[Gedächtniszellen]]. Man spricht von einer [[aktiven]] Immunisierung. Der Schutz setzt erst nach einigen Tagen bis Wochen ein, hält aber lange an. Damit er bestehen bleibt, sind manchmal [[Auffrischimpfungen]] nötig.</p><p>Bei einer [[Heilimpfung]] bekommt man dagegen fertige Antikörper. Diese [[passive]] Immunisierung wirkt [[sofort]], schützt aber nur wenige Wochen.</p><p>Der Arzt [[Edward Jenner|Jenner]] übertrug 1796 Material aus [[Kuhpocken]]-Blasen auf einen Jungen und schützte ihn so vor den Pocken. Alle Impfungen werden im [[Impfausweis]] eingetragen. In Deutschland gibt die [[STIKO]] Empfehlungen zum Impfen.</p>"}
},
{
"slug": "sortieren-allergie-unvertraeglichkeit",
"titel": "Sortieren: Milchallergie oder Laktoseintoleranz?",
"kurz": "Merkmale der richtigen Störung zuordnen",
"typ": "sortieren",
"anleitung": "Ordne jedes Merkmal der Milchallergie, der Laktoseintoleranz oder beiden zu.",
"daten": {"kategorien": ["Milchallergie", "Laktoseintoleranz", "beide"], "eintraege": [
 {"text": "Das Immunsystem bildet Antikörper gegen Milcheiweiß.", "kategorie": "Milchallergie"},
 {"text": "Das Enzym Laktase wird nicht in ausreichender Menge gebildet.", "kategorie": "Laktoseintoleranz"},
 {"text": "Schon kleinste Mengen Milch lösen Beschwerden aus.", "kategorie": "Milchallergie"},
 {"text": "Kleine Mengen Milch werden oft vertragen.", "kategorie": "Laktoseintoleranz"},
 {"text": "Laktosefreie Milch kann problemlos getrunken werden.", "kategorie": "Laktoseintoleranz"},
 {"text": "Im Extremfall kann ein allergischer Schock auftreten.", "kategorie": "Milchallergie"},
 {"text": "Bakterien im Dickdarm vergären den Milchzucker.", "kategorie": "Laktoseintoleranz"},
 {"text": "Mastzellen schütten Histamin aus.", "kategorie": "Milchallergie"},
 {"text": "Nach dem Trinken von Milch können Bauchschmerzen auftreten.", "kategorie": "beide"},
 {"text": "Betroffene sollten Zutatenlisten genau lesen.", "kategorie": "beide"}
]}
},
]
