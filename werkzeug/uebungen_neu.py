"""Neue Übungen: Krankheiten und Training für die Kursarbeit."""

AUFGABEN_KRANKHEITEN = [
 ("I", "Nenne je drei Krankheiten, die durch Bakterien, und drei, die durch Viren ausgelöst werden.", 4),
 ("I", "Erkläre, was der Begriff „meldepflichtig“ bedeutet und warum es eine Meldepflicht gibt.", 3),
 ("II", "Steckbrief erstellen: Wähle eine Krankheit, die nicht im Lerntext steht, zum Beispiel Scharlach, Borreliose, Röteln oder Grippe. Recherchiere und erstelle einen Steckbrief mit den Punkten Erreger, Übertragung, Inkubationszeit, Symptome, Behandlung und Vorbeugung. Gib deine Quellen an.", 0),
 ("II", "Krankheitsdetektiv, Fall 1: Paul (14) hat sich beim Fußball das Knie an einem rostigen Zaun aufgeschürft. Neun Tage später kann er den Mund kaum noch öffnen, und seine Nackenmuskeln verkrampfen. Seinen Impfausweis findet niemand. Bestimme die Krankheit, begründe deine Entscheidung und erkläre, warum Paul sofort ins Krankenhaus muss.", 6),
 ("II", "Krankheitsdetektiv, Fall 2: Lina (5) hat seit drei Tagen Fieber, Schnupfen, Husten und gerötete Augen. Heute zeigen sich hinter den Ohren rotbraune Flecken, die sich über das Gesicht ausbreiten. Zwei Wochen vorher war sie auf einem Kindergeburtstag mit einem kranken Kind. Bestimme die Krankheit, begründe und erkläre, ob ein Antibiotikum helfen würde.", 6),
 ("II", "Krankheitsdetektiv, Fall 3: Nach einem Grillfest mit Hähnchenspießen leiden am nächsten Tag mehrere Gäste unter Durchfall, Bauchschmerzen und Erbrechen. Bestimme die wahrscheinliche Ursache, erkläre, wie es dazu kam, und gib zwei Regeln an, mit denen man das hätte verhindern können.", 6),
 ("III", "Seit 2020 müssen Kinder in Kita und Schule in Deutschland gegen Masern geimpft sein. Erläutere mithilfe der Steckbriefe und des Begriffs Gemeinschaftsschutz, warum der Gesetzgeber das so entschieden hat, und nimm begründet Stellung.", 6),
]

KRANKHEITEN_UEBUNGEN = [
{
"slug": "sortieren-krankheiten",
"titel": "Sortieren: Krankheit durch Bakterien oder Viren?",
"kurz": "15 Krankheiten ihrem Erreger zuordnen",
"typ": "sortieren",
"anleitung": "Wird die Krankheit durch Bakterien oder durch Viren ausgelöst? Ordne zu und klicke dann auf „Prüfen“.",
"daten": {"kategorien": ["Bakterien", "Viren"], "eintraege": [
 {"text": "Tetanus (Wundstarrkrampf)", "kategorie": "Bakterien"},
 {"text": "Keuchhusten", "kategorie": "Bakterien"},
 {"text": "Tuberkulose", "kategorie": "Bakterien"},
 {"text": "Syphilis", "kategorie": "Bakterien"},
 {"text": "Salmonellen-Infektion", "kategorie": "Bakterien"},
 {"text": "Scharlach", "kategorie": "Bakterien", "erklaerung": "Scharlach wird durch Streptokokken ausgelöst."},
 {"text": "Borreliose (durch Zeckenstich)", "kategorie": "Bakterien"},
 {"text": "Masern", "kategorie": "Viren"},
 {"text": "Mumps", "kategorie": "Viren"},
 {"text": "Windpocken", "kategorie": "Viren"},
 {"text": "Hepatitis B", "kategorie": "Viren"},
 {"text": "AIDS", "kategorie": "Viren"},
 {"text": "Lippenherpes", "kategorie": "Viren"},
 {"text": "Warzen", "kategorie": "Viren"},
 {"text": "Grippe", "kategorie": "Viren"}
]}
},
{
"slug": "quiz-wer-bin-ich",
"titel": "Quiz: Welche Krankheit bin ich?",
"kurz": "Krankheiten an ihren Merkmalen erkennen",
"typ": "quiz",
"anleitung": "Lies die Beschreibung und finde heraus, um welche Krankheit es sich handelt.",
"daten": {"fragen": [
 {"frage": "Meine Erreger leben als Sporen in der Erde und gelangen durch Wunden in den Körper. Ihr Gift löst schmerzhafte Muskelkrämpfe aus, oft zuerst im Kiefer.", "optionen": ["Tetanus", "Tuberkulose", "Mumps", "Keuchhusten"], "richtig": 0, "erklaerung": "Tetanus heißt auf Deutsch Wundstarrkrampf. Gegen ihn schützt eine Impfung, die alle zehn Jahre aufgefrischt wird."},
 {"frage": "Ich beginne wie eine Erkältung. Dann kommen heftige Hustenanfälle, nach denen man keuchend einatmet. Für Säuglinge bin ich besonders gefährlich.", "optionen": ["Keuchhusten", "Masern", "Grippe", "Windpocken"], "richtig": 0, "erklaerung": "Keuchhusten wird durch Bakterien ausgelöst und durch Tröpfchen übertragen."},
 {"frage": "Ich wurde früher „Schwindsucht“ genannt. Ich befalle meist die Lunge und muss mindestens sechs Monate mit mehreren Antibiotika behandelt werden.", "optionen": ["Tuberkulose", "Syphilis", "Hepatitis B", "AIDS"], "richtig": 0, "erklaerung": "Tuberkulose ist weltweit eine der tödlichsten Infektionskrankheiten."},
 {"frage": "Man bekommt mich meist durch nicht durchgegarte Eier oder Geflügel. Ich verursache Durchfall, Bauchschmerzen und Erbrechen.", "optionen": ["Salmonellen-Infektion", "Hepatitis B", "Mumps", "Tetanus"], "richtig": 0, "erklaerung": "Gründliches Garen und Küchenhygiene schützen vor Salmonellen."},
 {"frage": "Mein Ausschlag beginnt hinter den Ohren und breitet sich über den ganzen Körper aus. Ich bin extrem ansteckend. In Deutschland müssen Schulkinder gegen mich geimpft sein.", "optionen": ["Masern", "Windpocken", "Mumps", "Warzen"], "richtig": 0, "erklaerung": "Masern werden durch Viren ausgelöst. Seit 2020 gibt es eine Impfpflicht für Kinder in Kita und Schule."},
 {"frage": "Meine Bläschen jucken stark, verkrusten und fallen ab. Wer mich einmal hatte, ist immun, aber ich kann im Alter als Gürtelrose zurückkommen.", "optionen": ["Windpocken", "Lippenherpes", "Masern", "Syphilis"], "richtig": 0, "erklaerung": "Das Windpockenvirus bleibt nach der Krankheit in Nervenzellen."},
 {"frage": "Ich lasse die Ohrspeicheldrüsen anschwellen, sodass man „Hamsterbacken“ bekommt.", "optionen": ["Mumps", "Masern", "Keuchhusten", "Hepatitis B"], "richtig": 0, "erklaerung": "Gegen Mumps schützt die Impfung zusammen mit Masern und Röteln."},
 {"frage": "Ich entzünde die Leber und werde über Blut und Körperflüssigkeiten übertragen. Oft verursache ich Gelbsucht.", "optionen": ["Hepatitis B", "Tuberkulose", "Salmonellen-Infektion", "Warzen"], "richtig": 0, "erklaerung": "Gegen Hepatitis B werden in Deutschland schon Säuglinge geimpft."},
 {"frage": "Ich befalle T-Helferzellen und schwäche so das ganze Immunsystem. Ich bin nicht heilbar, aber gut behandelbar.", "optionen": ["HIV (AIDS)", "Masern", "Syphilis", "Grippe"], "richtig": 0, "erklaerung": "Händeschütteln, Umarmen oder Husten übertragen HIV nicht."},
 {"frage": "Ich bleibe nach der ersten Ansteckung lebenslang in Nervenzellen. Bei Fieber, Sonne oder Stress zeige ich mich als Bläschen an der Lippe.", "optionen": ["Lippenherpes", "Warzen", "Windpocken", "Mumps"], "richtig": 0, "erklaerung": "Lippenherpes wird durch Herpes-simplex-Viren ausgelöst."}
]}
},
]

TRAINING = [
{
"slug": "ka-fachbegriffe",
"titel": "Fachbegriffe der Abwehr zuordnen",
"kurz": "14 wichtige Begriffe rund um Krankheit und Immunsystem",
"typ": "zuordnen",
"anleitung": "Wähle für jeden Fachbegriff die passende Erklärung. Die Lösung kannst du ansehen, sobald alles zugeordnet ist.",
"daten": {"paare": [
 {"links": "Infektion", "rechts": "Krankheitserreger dringen in den Körper ein und vermehren sich dort."},
 {"links": "Fieber", "rechts": "Die Körpertemperatur steigt, um die Vermehrung von Erregern zu bremsen."},
 {"links": "Resistenz", "rechts": "Widerstandskraft gegen schädliche Einflüsse wie Erreger, Gifte oder Medikamente."},
 {"links": "Symptome", "rechts": "Anzeichen einer Krankheit, zum Beispiel Husten, Schmerzen oder Müdigkeit."},
 {"links": "Inkubationszeit", "rechts": "Zeit zwischen der Ansteckung und den ersten Krankheitszeichen."},
 {"links": "Medikamente", "rechts": "Wirkstoffe, die Beschwerden lindern oder Erreger bekämpfen."},
 {"links": "Rekonvaleszenz", "rechts": "Erholungsphase nach einer Krankheit, in der man wieder zu Kräften kommt."},
 {"links": "Übertragung", "rechts": "Weg, auf dem Erreger von einem Lebewesen zum nächsten gelangen."},
 {"links": "Antikörper", "rechts": "Eiweiße des Immunsystems, die Erreger erkennen, binden und unschädlich machen."},
 {"links": "Weiße Blutkörperchen", "rechts": "Abwehrzellen, die wie eine Polizei Erreger aufspüren und vernichten."},
 {"links": "Antigene", "rechts": "Merkmale auf der Oberfläche von Erregern, die das Immunsystem als fremd erkennt."},
 {"links": "Impfstoffe", "rechts": "Mittel, die das Immunsystem auf einen Erreger vorbereiten, bevor man ihm begegnet."},
 {"links": "Entzündung", "rechts": "Eine Stelle wird stärker durchblutet, rötet sich, schwillt an, wird warm und schmerzt."},
 {"links": "Knochenmark", "rechts": "Hier werden Blutzellen gebildet, auch die Abwehrzellen."}
]}
},
{
"slug": "ka-wissenscheck",
"titel": "Wissenscheck: Bakterien und Viren",
"kurz": "14 Fragen zu Bau, Vermehrung und Bedeutung",
"typ": "quiz",
"anleitung": "Teste dein Wissen über Bakterien und Viren. Du bekommst nach jeder Frage sofort eine Rückmeldung.",
"daten": {"fragen": [
 {"frage": "Aus wie vielen Zellen besteht ein Bakterium?", "optionen": ["aus einer einzigen Zelle", "aus zwei Zellen", "aus vielen tausend Zellen", "aus gar keiner Zelle"], "richtig": 0, "erklaerung": "Bakterien sind Einzeller."},
 {"frage": "Wie nennt man Lebewesen, deren Zellen keinen Zellkern haben?", "optionen": ["Prokaryoten", "Eukaryoten", "Zygoten", "Antigene"], "richtig": 0, "erklaerung": "Bakterien sind Prokaryoten. Menschen, Tiere und Pflanzen sind Eukaryoten, ihre Zellen haben einen Zellkern."},
 {"frage": "Wie vermehren sich Bakterien?", "optionen": ["durch Zweiteilung", "nur in Wirtszellen", "durch Sporen", "durch Knospung an der Zelle"], "richtig": 0, "erklaerung": "Ein Bakterium verdoppelt sein Erbgut und teilt sich in zwei Tochterzellen."},
 {"frage": "Bei welchen Temperaturen vermehren sich die meisten krankmachenden Bakterien am besten?", "optionen": ["zwischen 20 und 40 °C", "zwischen 0 und 20 °C", "zwischen 40 und 60 °C", "über 70 °C"], "richtig": 0, "erklaerung": "Auch unsere Körpertemperatur von 37 °C liegt in diesem Bereich."},
 {"frage": "Wie heißt der widerstandsfähige Ruhezustand, in dem manche Bakterien schlechte Bedingungen überstehen?", "optionen": ["Spore", "Plasmid", "Kolonie", "Wirtszelle"], "richtig": 0, "erklaerung": "Sporen haben eine dicke Hülle und überstehen Hitze, Kälte und Trockenheit."},
 {"frage": "Wie lange können Bakteriensporen überleben?", "optionen": ["Jahrzehnte, vermutlich sogar Tausende Jahre", "wenige Stunden", "ein bis zwei Wochen", "genau ein Jahr"], "richtig": 0, "erklaerung": "Sporen sind extrem langlebig."},
 {"frage": "Welche wichtige Aufgabe haben Bakterien in der Natur?", "optionen": ["Sie zersetzen tote Pflanzen und Tiere.", "Sie betreiben Fotosynthese für alle Pflanzen.", "Sie bestäuben Blüten.", "Sie bilden den Sauerstoff in unserem Blut."], "richtig": 0, "erklaerung": "Als Zersetzer machen Bakterien Mineralstoffe für Pflanzen wieder verfügbar."},
 {"frage": "Welche Medikamente töten Bakterien ab?", "optionen": ["Antibiotika, zum Beispiel Penicillin", "Impfstoffe", "Antikörper aus Heilserum", "Schmerzmittel"], "richtig": 0, "erklaerung": "Penicillin war das erste Antibiotikum. Es wurde 1928 von Alexander Fleming entdeckt."},
 {"frage": "Wofür werden Bakterien genutzt?", "optionen": ["zur Herstellung von Joghurt, Käse und Insulin", "zur Herstellung von Stahl", "zum Antrieb von Elektroautos", "zur Herstellung von Antikörpern im Blut"], "richtig": 0, "erklaerung": "Milchsäurebakterien machen Milchprodukte, gentechnisch veränderte Bakterien stellen Insulin her."},
 {"frage": "Woraus besteht ein Virus hauptsächlich?", "optionen": ["aus Erbgut und einer Eiweißhülle", "aus Zellwand und Zellkern", "aus Zellplasma und Ribosomen", "aus Muskeln und Nerven"], "richtig": 0, "erklaerung": "Viren sind keine Zellen, sondern Erbgut in einer Hülle."},
 {"frage": "Wie groß sind Viren ungefähr?", "optionen": ["0,02 bis 0,3 µm", "0,5 bis 1 µm", "2 bis 3 µm", "50 bis 100 µm"], "richtig": 0, "erklaerung": "Viren sind so klein, dass man sie nur im Elektronenmikroskop sieht."},
 {"frage": "Wofür steht die Einheit µm?", "optionen": ["Mikrometer, ein Tausendstel Millimeter", "Millimeter", "Nanometer, ein Millionstel Millimeter", "Mikrogramm"], "richtig": 0, "erklaerung": "1 µm = 0,001 mm. Bakterien sind etwa 1 bis 5 µm groß."},
 {"frage": "Wie nennt man eine Zelle, die von einem Virus befallen ist?", "optionen": ["Wirtszelle", "Plasmazelle", "Gedächtniszelle", "Spore"], "richtig": 0, "erklaerung": "Die Wirtszelle stellt nach dem Bauplan des Virus neue Viren her."},
 {"frage": "Warum zählen Viren nicht zu den Lebewesen?", "optionen": ["Sie haben keinen eigenen Stoffwechsel und können sich nicht selbst vermehren.", "Sie sind zu klein.", "Sie haben kein Erbgut.", "Sie kommen nur in Menschen vor."], "richtig": 0, "erklaerung": "Außerdem wachsen und bewegen sich Viren nicht selbst."}
]}
},
{
"slug": "ka-lueckentext-bakterien",
"titel": "Lückentext: Bakterien und Viren",
"kurz": "Die wichtigsten Fachbegriffe im Zusammenhang",
"typ": "lueckentext",
"anleitung": "Fülle die Lücken mit den Wörtern aus dem Wortspeicher. Groß- und Kleinschreibung ist egal.",
"daten": {"text": "<p>Bakterien sind [[einzellige]] Lebewesen. Weil ihre Zelle keinen Zellkern hat, nennt man sie auch [[Prokaryoten]]. Sie vermehren sich durch [[Zweiteilung]], am schnellsten bei Temperaturen zwischen 20 und 40 °C. Bei schlechten Bedingungen bilden manche Bakterien widerstandsfähige [[Sporen]]. In der Natur bauen Bakterien als [[Zersetzer]] tote Lebewesen ab. Gegen krankmachende Bakterien helfen [[Antibiotika]], zum Beispiel [[Penicillin]].</p><p>Viren bestehen aus [[Erbgut]] und einer [[Eiweißhülle|Eiweisshülle|Hülle]]. Sie sind nur 0,02 bis 0,3 [[Mikrometer|µm]] groß. Weil sie keinen eigenen [[Stoffwechsel]] haben, können sie sich nur in einer [[Wirtszelle]] vermehren.</p>"}
},
{
"slug": "ka-virusvermehrung",
"titel": "Reihenfolge: Wie sich ein Virus vermehrt",
"kurz": "Die sechs Schritte der Virusvermehrung ordnen",
"typ": "reihenfolge",
"anleitung": "Bringe die Schritte mit den Pfeiltasten in die richtige Reihenfolge und klicke auf „Prüfen“.",
"daten": {"schritte": [
 "Das Virus dockt mit seinen Andockstellen an eine Wirtszelle an.",
 "Das Virus oder sein Erbgut dringt in die Wirtszelle ein.",
 "Die Hülle löst sich auf, das Virus-Erbgut liegt frei in der Zelle.",
 "Die Zelle wird umprogrammiert: Sie vervielfältigt das Virus-Erbgut und stellt Hüllbausteine her.",
 "Aus Erbgut und Hüllbausteinen werden viele neue Viren zusammengebaut.",
 "Die neuen Viren verlassen die Zelle und befallen weitere Zellen."
]}
},
{
"slug": "ka-krankheitsverlauf",
"titel": "Reihenfolge: Verlauf einer Infektionskrankheit",
"kurz": "Von der Ansteckung bis zur Immunität",
"typ": "reihenfolge",
"anleitung": "Bringe die Abschnitte einer Infektionskrankheit in die richtige Reihenfolge.",
"daten": {"schritte": [
 "Infektion: Erreger dringen in den Körper ein.",
 "Inkubationszeit: Die Erreger vermehren sich, man merkt noch nichts.",
 "Krankheitsausbruch: Symptome wie Fieber oder Husten treten auf.",
 "Überwindung: Das Immunsystem bekämpft die Erreger mit Antikörpern und Abwehrzellen.",
 "Rekonvaleszenz: Der Körper erholt sich und kommt wieder zu Kräften.",
 "Immunität: Gedächtniszellen schützen vor einer erneuten Erkrankung."
]}
},
{
"slug": "ka-krankheit-beschreiben",
"titel": "Schreibtraining: Eine Krankheit beschreiben",
"kurz": "Eine bakterielle und eine virale Erkrankung im Detail beschreiben",
"typ": "schreiben",
"anleitung": "Beschreibe jeweils eine gefährliche Erkrankung so ausführlich wie in einer Kursarbeit. Erst wenn du genug geschrieben hast, kannst du deinen Text mit einer Musterlösung vergleichen.",
"daten": {"aufgaben": [
 {"frage": "Beschreibe eine gefährliche bakterielle Erkrankung im Detail. Erkläre, wie sie übertragen wird und welche Symptome auftreten.",
  "hinweis": "Tipp: Geeignet sind zum Beispiel Tetanus, Keuchhusten oder Tuberkulose. Nachschlagen kannst du im Lerntext „Krankheiten durch Bakterien und Viren“.",
  "minWoerter": 45,
  "checkliste": ["Ich habe die Krankheit genannt.", "Ich habe geschrieben, dass sie durch Bakterien ausgelöst wird (wenn möglich mit Namen des Erregers).", "Ich habe den Übertragungsweg erklärt.", "Ich habe die Inkubationszeit angegeben.", "Ich habe mehrere Symptome beschrieben, möglichst in der richtigen Reihenfolge.", "Ich habe erklärt, was gefährlich ist.", "Ich habe Behandlung (Antibiotika) oder Vorbeugung genannt.", "Ich habe Fachbegriffe verwendet und in ganzen Sätzen geschrieben."],
  "muster": "Tetanus, auch Wundstarrkrampf genannt, ist eine gefährliche Krankheit, die durch Bakterien ausgelöst wird. Die Sporen des Tetanus-Bakteriums kommen in Erde, Staub und Tierkot vor. Gelangt Schmutz in eine Wunde, zum Beispiel durch einen Holzsplitter oder einen rostigen Nagel, können die Bakterien in den Körper eindringen. Von Mensch zu Mensch ist Tetanus nicht ansteckend. Nach einer Inkubationszeit von meist drei Tagen bis drei Wochen bilden die Bakterien in der Wunde ein Gift, das die Nerven angreift. Es kommt zu sehr schmerzhaften Muskelkrämpfen. Oft verkrampft zuerst die Kiefermuskulatur, sodass man den Mund nicht mehr öffnen kann. Später sind Rücken- und Atemmuskeln betroffen. Unbehandelt führt die Krankheit oft zum Tod, weil die Atmung versagt. Behandelt wird im Krankenhaus mit Antikörpern gegen das Gift und mit Antibiotika. Schützen kann man sich durch eine Impfung, die alle zehn Jahre aufgefrischt werden sollte."},
 {"frage": "Beschreibe eine gefährliche virale Erkrankung im Detail. Erkläre, wie sie übertragen wird und welche Symptome auftreten.",
  "hinweis": "Tipp: Geeignet sind zum Beispiel Masern, Hepatitis B oder HIV/AIDS.",
  "minWoerter": 45,
  "checkliste": ["Ich habe die Krankheit genannt.", "Ich habe geschrieben, dass sie durch Viren ausgelöst wird.", "Ich habe den Übertragungsweg erklärt.", "Ich habe die Inkubationszeit angegeben.", "Ich habe mehrere Symptome beschrieben, möglichst in der richtigen Reihenfolge.", "Ich habe erklärt, was gefährlich ist.", "Ich habe Behandlung oder Vorbeugung genannt (und dass Antibiotika nicht helfen).", "Ich habe Fachbegriffe verwendet und in ganzen Sätzen geschrieben."],
  "muster": "Masern sind eine gefährliche Krankheit, die durch das Masernvirus ausgelöst wird. Das Virus wird durch Tröpfcheninfektion übertragen, also beim Husten, Niesen oder Sprechen. Masern sind extrem ansteckend: Fast jeder Ungeimpfte, der Kontakt mit einem Erkrankten hat, steckt sich an. Nach einer Inkubationszeit von etwa 8 bis 10 Tagen treten die ersten Symptome auf: Fieber, Schnupfen, Husten und entzündete, lichtempfindliche Augen. Einige Tage später erscheint hinter den Ohren und im Gesicht ein rotbrauner, fleckiger Hautausschlag, der sich über den ganzen Körper ausbreitet. Danach ist das Immunsystem für mehrere Wochen geschwächt. Gefährlich sind Folgeerkrankungen wie Lungen- oder Gehirnentzündungen. Antibiotika helfen nicht, weil Masern durch Viren ausgelöst werden; man kann nur die Beschwerden behandeln. Den besten Schutz bietet die Impfung. In Deutschland müssen Kinder in Kita und Schule seit 2020 gegen Masern geimpft sein."}
]}
},
]
