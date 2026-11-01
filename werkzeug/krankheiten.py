"""Lerntext: Steckbriefe zu Krankheiten durch Bakterien und Viren.
Eigene Formulierungen; Zahlen geprüft an RKI-Ratgebern und WHO (Stand 2025/26)."""
import html
import zeichnungen as Z

FELDER = [("erreger", "Erreger"), ("weg", "Übertragung"), ("inkubation", "Inkubationszeit"),
          ("symptome", "Symptome"), ("behandlung", "Behandlung"), ("schutz", "Vorbeugung")]

BAKTERIELL = [
 {"id": "tetanus", "name": "Tetanus", "auch": "Wundstarrkrampf", "melde": False,
  "erreger": "Tetanus-Bakterium (Clostridium tetani). Seine Sporen kommen fast überall in Erde, Staub und Tierkot vor.",
  "weg": "Schmutz gelangt in eine Wunde, schon ein Holzsplitter oder ein Kratzer bei der Gartenarbeit reicht. Von Mensch zu Mensch ist Tetanus nicht ansteckend.",
  "inkubation": "meist 3 Tage bis 3 Wochen",
  "symptome": "In der Wunde bilden die Bakterien ein Gift, das die Nerven angreift. Es kommt zu sehr schmerzhaften Muskelkrämpfen, oft zuerst im Kiefer, sodass man den Mund nicht mehr öffnen kann. Später verkrampfen Rücken- und Atemmuskeln. Unbehandelt führt Tetanus oft zum Tod.",
  "behandlung": "im Krankenhaus, meist auf der Intensivstation: Antikörper gegen das Gift (Heilimpfung), Antibiotika und Medikamente gegen die Krämpfe",
  "schutz": "Schutzimpfung, die alle 10 Jahre aufgefrischt werden sollte; Wunden gründlich reinigen"},
 {"id": "keuchhusten", "name": "Keuchhusten", "auch": "Pertussis", "melde": True,
  "erreger": "Keuchhusten-Bakterium (Bordetella pertussis)",
  "weg": "Tröpfcheninfektion beim Husten, Niesen und Sprechen; sehr ansteckend",
  "inkubation": "meist 9–10 Tage (6–20 Tage möglich)",
  "symptome": "Zuerst wie eine Erkältung mit Schnupfen und leichtem Husten. Nach ein bis zwei Wochen folgen heftige, krampfartige Hustenanfälle, oft nachts. Danach zieht man die Luft keuchend ein, manchmal muss man erbrechen. Der Husten kann wochenlang anhalten. Für Säuglinge ist Keuchhusten lebensgefährlich, weil sie Atemaussetzer bekommen können.",
  "behandlung": "Antibiotika; sie verkürzen vor allem die Zeit, in der man andere ansteckt",
  "schutz": "Schutzimpfung schon im Säuglingsalter; Auffrischungen auch für Jugendliche, Erwachsene und Schwangere"},
 {"id": "syphilis", "name": "Syphilis", "auch": "Lues", "melde": True,
  "erreger": "Syphilis-Bakterium (Treponema pallidum), ein schraubenförmiges Bakterium",
  "weg": "beim Geschlechtsverkehr über kleinste Verletzungen von Haut und Schleimhaut",
  "inkubation": "meist 2–4 Wochen",
  "symptome": "Zuerst entsteht an der Ansteckungsstelle ein schmerzloser, rötlicher Knoten, der nach einigen Wochen von selbst verschwindet. Wochen bis Monate später folgen Hautausschlag, Fieber, Kopfschmerzen und Müdigkeit. Unbehandelt kann die Krankheit nach Jahren Organe, Blutgefäße, Nerven und das Gehirn schwer schädigen.",
  "behandlung": "Antibiotikum Penicillin; je früher, desto besser",
  "schutz": "Kondome senken das Risiko; bei Verdacht früh zur Ärztin oder zum Arzt gehen"},
 {"id": "salmonellen", "name": "Salmonellen-Infektion", "auch": "Lebensmittelvergiftung durch Salmonellen", "melde": True,
  "erreger": "Salmonellen; es gibt über 2 500 verschiedene Arten",
  "weg": "über Lebensmittel, vor allem rohe oder nicht durchgegarte Eier, Geflügel und Hackfleisch, und über verschmutzte Hände oder Küchengeräte",
  "inkubation": "meist 12–36 Stunden",
  "symptome": "plötzlicher Durchfall, Bauchschmerzen, Übelkeit, Erbrechen, manchmal leichtes Fieber; meist nach wenigen Tagen vorbei. Durch den Flüssigkeitsverlust kann die Krankheit für Kleinkinder, alte und kranke Menschen gefährlich werden.",
  "behandlung": "viel trinken und verlorene Salze ersetzen; Antibiotika nur bei schweren Verläufen",
  "schutz": "Eier, Geflügel und Fleisch vollständig durchgaren, Lebensmittel kühl lagern, Hände und Küchenbretter gründlich reinigen"},
 {"id": "tuberkulose", "name": "Tuberkulose", "auch": "TBC, früher „Schwindsucht“", "melde": True,
  "erreger": "Tuberkulose-Bakterium (Mycobacterium tuberculosis); 1882 von Robert Koch entdeckt",
  "weg": "Tröpfcheninfektion, vor allem bei engem und längerem Kontakt mit Erkrankten, die husten",
  "inkubation": "Wochen bis Monate; viele Infizierte erkranken nie oder erst Jahre später",
  "symptome": "Meist ist die Lunge betroffen: Husten über mehrere Wochen, manchmal mit blutigem Auswurf, Fieber, Nachtschweiß, Müdigkeit und starker Gewichtsverlust. Das Lungengewebe wird zerstört. Die Bakterien können sich auch in andere Organe ausbreiten.",
  "behandlung": "mehrere Antibiotika gleichzeitig über mindestens sechs Monate; wird die Behandlung zu früh abgebrochen, entstehen resistente Bakterien",
  "schutz": "Erkrankte früh erkennen und behandeln, gute Hygiene und Lüften. Tuberkulose kommt vor allem dort vor, wo viele Menschen eng zusammen unter schlechten Bedingungen leben. Weltweit erkrankten 2024 rund 10,7 Millionen Menschen, über 1,2 Millionen starben daran."},
]

VIRAL = [
 {"id": "hiv", "name": "HIV-Infektion und AIDS", "auch": "erworbenes Immunschwächesyndrom", "melde": True,
  "erreger": "HI-Virus (Humanes Immundefizienz-Virus). Es befällt T-Helferzellen des Immunsystems.",
  "weg": "beim ungeschützten Geschlechtsverkehr, über Blut (zum Beispiel gemeinsam benutzte Spritzen) und von der Mutter auf das Kind. Nicht durch Händeschütteln, Umarmen, Husten, gemeinsames Geschirr oder Insektenstiche.",
  "inkubation": "nach 2–4 Wochen oft grippeähnliche Beschwerden; danach meist viele Jahre ohne Beschwerden. Ohne Behandlung bricht AIDS im Durchschnitt nach etwa 10 Jahren aus.",
  "symptome": "Das Virus zerstört nach und nach die T-Helferzellen. Das Immunsystem wird immer schwächer. Bei AIDS kommt es zu häufigen, schweren Infektionen und bestimmten Krebsarten.",
  "behandlung": "nicht heilbar. Moderne Medikamente unterdrücken aber die Vermehrung des Virus so gut, dass Betroffene fast normal lange leben können und bei erfolgreicher Behandlung andere nicht mehr anstecken.",
  "schutz": "Kondome, keine Spritzen gemeinsam benutzen; es gibt keine Impfung"},
 {"id": "warzen", "name": "Warzen", "auch": "", "melde": False,
  "erreger": "Humane Papillomviren (HPV)",
  "weg": "durch direkten Hautkontakt oder über Gegenstände, zum Beispiel barfuß im Schwimmbad oder in der Umkleide; kleine Risse in der Haut erleichtern die Ansteckung",
  "inkubation": "Wochen bis viele Monate",
  "symptome": "Die Viren bringen Hautzellen dazu, übermäßig zu wachsen. Es entstehen harmlose, raue Knötchen, oft an Händen und Füßen.",
  "behandlung": "Oft heilen Warzen nach einiger Zeit von selbst. Sonst helfen Mittel aus der Apotheke oder Vereisen beim Arzt.",
  "schutz": "Badeschuhe im Schwimmbad, Handtücher nicht teilen, Warzen nicht aufkratzen"},
 {"id": "herpes", "name": "Lippenherpes", "auch": "", "melde": False,
  "erreger": "Herpes-simplex-Virus",
  "weg": "über Speichel und Bläschenflüssigkeit, zum Beispiel beim Küssen oder durch gemeinsames Benutzen von Gläsern",
  "inkubation": "einige Tage nach der ersten Ansteckung. Danach bleibt das Virus lebenslang in Nervenzellen und kann immer wieder aktiv werden, ausgelöst etwa durch Fieber, Sonne (UV-Licht) oder Stress.",
  "symptome": "Zuerst Kribbeln und Spannen an der Lippe, dann kleine, mit klarer Flüssigkeit gefüllte Bläschen. Sie trocknen ein und heilen nach etwa zehn Tagen ohne Narben ab.",
  "behandlung": "Cremes mit virenhemmenden Wirkstoffen lindern und verkürzen die Beschwerden",
  "schutz": "Bläschen nicht berühren, danach Hände waschen, Gläser und Handtücher nicht teilen; Sonnenschutz für die Lippen"},
 {"id": "windpocken", "name": "Windpocken", "auch": "", "melde": True,
  "erreger": "Varizella-Zoster-Virus",
  "weg": "Tröpfcheninfektion, sehr leicht übertragbar, auch über einige Meter Entfernung (daher der Name); außerdem über die Flüssigkeit der Bläschen",
  "inkubation": "meist etwa 2 Wochen (8–28 Tage möglich). Ansteckend ist man schon 1–2 Tage bevor der Ausschlag beginnt, bis alle Bläschen verkrustet sind.",
  "symptome": "leichtes Fieber und stark juckender Ausschlag: Erst bilden sich rote Flecken, daraus Bläschen, die verkrusten und abfallen. Der Ausschlag beginnt meist am Kopf und Rumpf und breitet sich aus. Wer stark kratzt, kann Narben behalten. Nach überstandener Krankheit ist man immun. Das Virus bleibt aber im Körper und kann im Alter eine Gürtelrose auslösen.",
  "behandlung": "Mittel gegen den Juckreiz und gegen Fieber; bei schweren Verläufen virenhemmende Medikamente",
  "schutz": "Schutzimpfung im Kleinkindalter"},
 {"id": "hepatitisb", "name": "Hepatitis B", "auch": "", "melde": True,
  "erreger": "Hepatitis-B-Virus; es befällt die Leber",
  "weg": "über Blut und andere Körperflüssigkeiten, zum Beispiel beim ungeschützten Geschlechtsverkehr, über gemeinsam benutzte Spritzen oder von der Mutter auf das Kind bei der Geburt; schon winzige Mengen Blut reichen",
  "inkubation": "sehr lang: etwa 1,5 bis 6 Monate",
  "symptome": "Entzündung der Leber mit Müdigkeit, Übelkeit, Appetitlosigkeit und oft Gelbsucht (gelbe Haut und Augen). Viele Erwachsene werden nach einigen Monaten wieder gesund. Bei manchen bleibt die Entzündung dauerhaft (chronisch) und kann Jahre später die Leber schwer schädigen.",
  "behandlung": "Schonung; bei chronischem Verlauf Medikamente, die die Vermehrung des Virus bremsen",
  "schutz": "Schutzimpfung, in Deutschland für alle Säuglinge empfohlen; Kondome"},
 {"id": "masern", "name": "Masern", "auch": "", "melde": True,
  "erreger": "Masernvirus",
  "weg": "Tröpfcheninfektion; Masern gehören zu den ansteckendsten Krankheiten überhaupt. Fast jeder Ungeimpfte, der Kontakt hat, steckt sich an.",
  "inkubation": "etwa 8–10 Tage bis zu den ersten Beschwerden, etwa 2 Wochen bis zum Ausschlag. Ansteckend ist man 4 Tage vor bis 4 Tage nach Beginn des Ausschlags.",
  "symptome": "Zuerst Fieber, Schnupfen, Husten und entzündete, lichtempfindliche Augen. Nach einigen Tagen erscheint hinter den Ohren und im Gesicht ein rotbrauner, fleckiger Ausschlag, der sich über den ganzen Körper ausbreitet. Danach ist das Immunsystem für Wochen geschwächt. Gefährliche Folgen können Lungen- und Gehirnentzündungen sein.",
  "behandlung": "Gegen das Virus selbst gibt es kein Mittel; man behandelt nur die Beschwerden, etwa das Fieber",
  "schutz": "Schutzimpfung (zusammen mit Mumps und Röteln). In Deutschland müssen Kinder, die in die Kita oder Schule gehen, seit 2020 gegen Masern geimpft sein."},
 {"id": "mumps", "name": "Mumps", "auch": "Ziegenpeter", "melde": True,
  "erreger": "Mumpsvirus",
  "weg": "Tröpfcheninfektion und Speichel, zum Beispiel über gemeinsam benutzte Flaschen",
  "inkubation": "meist 16–18 Tage (12–25 Tage möglich). Ansteckend ist man schon einige Tage vor der Schwellung.",
  "symptome": "Fieber, Kopf- und Gliederschmerzen und eine schmerzhafte Schwellung der Ohrspeicheldrüsen vor und unter den Ohren („Hamsterbacken“). Nach etwa einer Woche geht die Schwellung zurück. Mögliche Folgen sind Hirnhautentzündung und bei Jungen und Männern eine Hodenentzündung.",
  "behandlung": "nur die Beschwerden: Ruhe, Mittel gegen Fieber und Schmerzen",
  "schutz": "Schutzimpfung (zusammen mit Masern und Röteln)"},
]


def steckbrief(k, art):
    symbol = Z.deko("0 0 64 64", Z.stab(32, 32, 40, 16, -25, "f-blau", False) if art == "b" else Z.virus(32, 32, 1.0), "ill")
    auch = f'<span class="sb-auch">{html.escape(k["auch"])}</span>' if k["auch"] else ""
    melde = '<span class="sb-melde">meldepflichtig</span>' if k["melde"] else ""
    zeilen = "".join(f'<dt>{t}</dt><dd>{html.escape(k[f])}</dd>' for f, t in FELDER)
    return (f'<article class="steckbrief sb-{art}" id="{k["id"]}">'
            f'<header><span class="sb-symbol">{symbol}</span><div><h3>{html.escape(k["name"])}</h3>{auch}</div>{melde}</header>'
            f'<dl>{zeilen}</dl></article>')


def uebersicht():
    def zeile(k):
        return f'<li><a href="#{k["id"]}">{html.escape(k["name"])}</a></li>'
    return (f'<div class="sb-uebersicht">'
            f'<div><h3>Bakterien</h3><ul>{"".join(zeile(k) for k in BAKTERIELL)}</ul></div>'
            f'<div><h3>Viren</h3><ul>{"".join(zeile(k) for k in VIRAL)}</ul></div></div>')


INHALT = """
<p class="lead">Steckbriefe zu wichtigen Krankheiten, die durch Bakterien oder Viren ausgelöst werden. Du kannst sie der Reihe nach lesen oder gezielt nachschlagen.</p>

<div class="wusstest"><strong>Wichtig</strong>
<p>Bei Verdacht auf eine dieser Krankheiten sollte man immer zur Ärztin oder zum Arzt gehen. Manche Krankheiten sind <span class="fachwort">meldepflichtig</span>: Die Ärztin oder der Arzt muss sie dem Gesundheitsamt melden. So können Ausbrüche früh erkannt und weitere Ansteckungen verhindert werden.</p></div>

<h2>Auf einen Blick</h2>
""" + uebersicht() + """

<div class="merke"><strong>Merke: Bakteriell oder viral?</strong>
<p>Gegen Krankheiten durch Bakterien helfen <strong>Antibiotika</strong>. Gegen Viren wirken sie nicht. Bei Viren behandelt man meist nur die Beschwerden, bei einigen gibt es virenhemmende Medikamente. Gegen viele Krankheiten beider Gruppen schützen <strong>Impfungen</strong>.</p></div>

<h2>Krankheiten durch Bakterien</h2>
<div class="steckbriefe">""" + "".join(steckbrief(k, "b") for k in BAKTERIELL) + """</div>

<h2>Krankheiten durch Viren</h2>
<div class="steckbriefe">""" + "".join(steckbrief(k, "v") for k in VIRAL) + """</div>

<h2>So beschreibst du eine Krankheit</h2>
<p>Wenn du eine Krankheit beschreiben sollst, zum Beispiel in einer Kursarbeit, geh diese Punkte der Reihe nach durch:</p>
<ol>
  <li><strong>Name und Erreger:</strong> Wie heißt die Krankheit? Wird sie von Bakterien oder von Viren ausgelöst?</li>
  <li><strong>Übertragung:</strong> Wie steckt man sich an?</li>
  <li><strong>Inkubationszeit:</strong> Wie lange dauert es bis zu den ersten Beschwerden?</li>
  <li><strong>Symptome:</strong> Welche Beschwerden treten auf, und in welcher Reihenfolge? Was kann gefährlich werden?</li>
  <li><strong>Behandlung und Vorbeugung:</strong> Was hilft, wie kann man sich schützen?</li>
</ol>
<p class="legende">Quellen für Zahlen und Fakten: Ratgeber des Robert Koch-Instituts und Weltgesundheitsorganisation (WHO), Global Tuberculosis Report 2025.</p>
"""

LERNTEXT = {"slug": "07-krankheiten-steckbriefe", "titel": "Krankheiten durch Bakterien und Viren",
            "kurz": "Steckbriefe zu Tetanus, Keuchhusten, Tuberkulose, Masern, Windpocken, HIV und weiteren Krankheiten.",
            "inhalt": INHALT}
