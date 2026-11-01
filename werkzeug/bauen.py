"""Erzeugt alle Seiten der Website. Aufruf: python3 bauen.py (im Ordner werkzeug)."""
import html
from basis import seite, uebung, REIHEN
import zeichnungen as Z

AFB_TEXT = {"I": "AFB I", "II": "AFB II", "III": "AFB III"}
FERTIG = {1, 2, 3, 4}

# ======================================================================
# Daten der Reihen
# ======================================================================
# Reihe 1
from lerntexte import LERNTEXTE as LT1
from aufgaben import AUFGABEN as AUF1
from uebungsdaten import UEBUNGEN as UEB1
from modelle import MODELLE as MOD1
from mikroskop_seite import MIKROSKOP
from krankheiten import LERNTEXT as LT_KRANK
from uebungen_neu import AUFGABEN_KRANKHEITEN, KRANKHEITEN_UEBUNGEN, TRAINING
LT1.insert(2, LT_KRANK)
AUF1[LT_KRANK["slug"]] = AUFGABEN_KRANKHEITEN
MOD1 = [MIKROSKOP] + MOD1

# Reihe 2
import zeichnungen2 as Z2
from reihe2_texte import LERNTEXTE as LT2
from reihe2_rest import AUFGABEN as AUF2, UEBUNGEN as UEB2, MODELLE as MOD2, TRAINING as TRAIN2

FIGUREN = {
    "virusvermehrung": (Z.virusvermehrung, "So vermehrt sich ein Virus in einer Wirtszelle (vereinfacht)."),
    "uebertragungswege": (Z.uebertragungswege, "So gelangen Krankheitserreger in den Körper."),
    "krankheitsverlauf": (Z.krankheitsverlauf, "Typischer Verlauf einer Infektionskrankheit (vereinfacht)."),
    "zweiteilung": (Z.zweiteilung, "Aus einem Bakterium werden alle 20 Minuten doppelt so viele."),
    "abwehr_koerper": (Z.abwehr_koerper, "Die äußeren Schranken halten die meisten Erreger ab."),
    "zeitstrahl_impfen": (Z.zeitstrahl_impfen, "Meilensteine in der Geschichte des Impfens."),
    "gemeinschaftsschutz": (Z.gemeinschaftsschutz, "Wenn viele geimpft sind, kann sich eine Krankheit kaum ausbreiten."),
    "resistenz_bilder": (Z.resistenz_bilder, "Das Antibiotikum wählt die zufällig resistenten Bakterien aus."),
    "allergie_ablauf": (Z.allergie_ablauf, "Ablauf einer allergischen Reaktion (vereinfacht)."),
}
FIGUREN.update(Z2.FIGUREN)

# Reihe 3
import zeichnungen3 as Z3
from reihe3_texte import LERNTEXTE as LT3
from reihe3_rest import AUFGABEN as AUF3, UEBUNGEN as UEB3, MODELLE as MOD3, TRAINING as TRAIN3
FIGUREN.update(Z3.FIGUREN)

# Reihe 4
import zeichnungen4 as Z4
from reihe4_texte import LERNTEXTE as LT4
from reihe4_rest import AUFGABEN as AUF4, UEBUNGEN as UEB4, MODELLE as MOD4, TRAINING as TRAIN4
FIGUREN.update(Z4.FIGUREN)


def figuren_einsetzen(text):
    for name, (fn, unterschrift) in FIGUREN.items():
        text = text.replace(f"<!--FIG:{name}-->", f'<figure class="breit"><div class="bild">{fn()}</div><figcaption>{unterschrift}</figcaption></figure>')
    return text


def reihenkopf(nr, name, text, bild):
    return f"""
<section class="reihe-kopf">
  <div class="huelle">
    <div>
      <span class="reihe-nr">Reihe {nr}</span>
      <h1>{html.escape(name)}</h1>
      <p>{text}</p>
    </div>
    {bild}
  </div>
</section>"""


def liste(eintraege, ordner, mit_nr=True):
    zeilen = []
    for i, e in enumerate(eintraege):
        nr = f'<span class="nr">{i + 1}</span>' if mit_nr else ""
        zeilen.append(f'<li><a href="{ordner}/{e["slug"]}.html"><span class="kachel">{Z.symbol(e["slug"])}{nr}</span>'
                      f'<span class="titel">{html.escape(e["titel"])}</span><span class="info">{html.escape(e["kurz"])}</span></a></li>')
    return '<ul class="liste zweispaltig">' + "".join(zeilen) + "</ul>"


def kurztitel(t):
    return t.split(": ", 1)[1] if ": " in t else t


def baue_reihe(nr, lerntexte, aufgaben, uebungen, modelle, kopftext, kopfbild, training=None, training_text="", vorwort="", training_titel="Training für die Kursarbeit"):
    ordner, name = REIHEN[nr]
    alle_uebungen = uebungen + (training or [])

    for i, lt in enumerate(lerntexte):
        vor = lerntexte[i - 1] if i > 0 else None
        nach = lerntexte[i + 1] if i < len(lerntexte) - 1 else None
        links = [f'<a href="{vor["slug"]}.html">Zurück: {html.escape(vor["titel"])}</a>' if vor else '<span></span>',
                 f'<a href="{nach["slug"]}.html">Weiter: {html.escape(nach["titel"])}</a>' if nach else '<a href="../index.html">Zur Übersicht der Reihe</a>']
        inhalt = f"""
<article class="spalte lerntext">
  <div class="lt-bild">{Z.lt_kopf(lt["slug"])}</div>
  <h1>{html.escape(lt["titel"])}</h1>
{figuren_einsetzen(lt["inhalt"])}
  <div class="knopfreihe">
    <a class="knopf" href="../aufgaben/{lt["slug"]}.html">Aufgaben zu diesem Text</a>
  </div>
  <nav class="weiter" aria-label="Weitere Lerntexte">{links[0]}{links[1]}</nav>
</article>"""
        seite(f"{ordner}/lerntexte/{lt['slug']}.html", lt["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Lerntext " + str(i + 1), None)], beschreibung=lt["kurz"])

    for i, lt in enumerate(lerntexte):
        items = []
        for afb, text, zeilen in aufgaben[lt["slug"]]:
            z = f'<div class="schreibzeilen" style="--zeilen:{zeilen}"></div>' if zeilen else ""
            items.append(f'<li><p>{html.escape(text)} <span class="afb" title="Anforderungsbereich {afb}">{AFB_TEXT[afb]}</span></p>{z}</li>')
        inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(lt["slug"])}<h1>Aufgaben: {html.escape(lt["titel"])}</h1></div>
  <p class="legende">Grundlage ist der Lerntext <a href="../lerntexte/{lt["slug"]}.html">{html.escape(lt["titel"])}</a>.
  AFB I = wiedergeben, AFB II = anwenden und erklären, AFB III = beurteilen und Stellung nehmen.</p>
  <div class="knopfreihe nicht-drucken">
    <button class="knopf leise" type="button" onclick="window.print()">Als Arbeitsblatt drucken</button>
  </div>
  <p class="nicht-drucken legende">Beim Drucken werden automatisch Schreiblinien eingefügt.</p>
  <p class="nur-druck">Name: ______________________________ &nbsp; Datum: ______________</p>
  <ol class="aufgaben">
    {''.join(items)}
  </ol>
  <nav class="weiter" aria-label="Navigation">
    <a href="../lerntexte/{lt["slug"]}.html">Zurück zum Lerntext</a>
    <a href="../index.html">Zur Übersicht der Reihe</a>
  </nav>
</article>"""
        seite(f"{ordner}/aufgaben/{lt['slug']}.html", "Aufgaben: " + lt["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Aufgaben " + str(i + 1), None)], beschreibung="Aufgaben zu " + lt["titel"])

    for u in alle_uebungen:
        inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(u["slug"])}<h1>{html.escape(u["titel"])}</h1></div>
  <p class="lead">{html.escape(u["anleitung"])}</p>
  {uebung(u["typ"], u["daten"])}
  <noscript><p>Für diese Übung muss JavaScript im Browser aktiviert sein.</p></noscript>
  <nav class="weiter" aria-label="Navigation"><a href="../index.html">Zur Übersicht der Reihe</a></nav>
</article>"""
        seite(f"{ordner}/uebungen/{u['slug']}.html", u["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Übung", None)], beschreibung=u["kurz"], skripte=["assets/uebungen.js"])

    for m in modelle:
        inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(m["slug"])}<h1>{html.escape(m["titel"])}</h1></div>
  {m["inhalt"]}
  <nav class="weiter" aria-label="Navigation"><a href="../index.html">Zur Übersicht der Reihe</a></nav>
</article>"""
        seite(f"{ordner}/modelle/{m['slug']}.html", m["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Modell", None)], beschreibung=m["kurz"], skripte=m.get("skripte", []))

    aufg = [{"slug": lt["slug"], "titel": lt["titel"], "kurz": f'{len(aufgaben[lt["slug"]])} Aufgaben, druckbar als Arbeitsblatt'} for lt in lerntexte]
    modelle_k = [dict(m, titel=kurztitel(m["titel"])) for m in modelle]
    training_html = ""
    if training:
        training_html = f"""
    <h3 class="unterteil">{training_titel}</h3>
    <p class="hinweis">{training_text}</p>
    {liste(training, "uebungen", mit_nr=False)}"""
    seite(f"{ordner}/index.html", name, reihenkopf(nr, name, kopftext, kopfbild) + f"""
<div class="huelle">{vorwort}
  <section class="bereich" aria-labelledby="b-lt">
    <h2 id="b-lt">Lerntexte</h2>
    <p class="hinweis">In dieser Reihenfolge lesen. Jeder Text baut auf dem vorherigen auf.</p>
    {liste(lerntexte, "lerntexte")}
  </section>
  <section class="bereich" aria-labelledby="b-mo">
    <h2 id="b-mo">Modelle</h2>
    <p class="hinweis">Zum Ausprobieren und Verstehen.</p>
    {liste(modelle_k, "modelle", mit_nr=False)}
  </section>
  <section class="bereich" aria-labelledby="b-ue">
    <h2 id="b-ue">Übungen</h2>
    <p class="hinweis">Zum Üben und Wiederholen, mit sofortiger Rückmeldung.</p>
    {liste(uebungen, "uebungen", mit_nr=False)}{training_html}
  </section>
  <section class="bereich" aria-labelledby="b-au">
    <h2 id="b-au">Aufgaben</h2>
    <p class="hinweis">Passend zu den Lerntexten, für den Unterricht oder zu Hause.</p>
    {liste(aufg, "aufgaben")}
  </section>
</div>
""", reihe=nr, krumen=[(name, None)], beschreibung=f"Unterrichtsreihe {name}, Biologie Klasse 8")


# ======================================================================
# Startseite
# ======================================================================
beschr = {
    1: "Bakterien und Viren, das Immunsystem, Impfen, Antibiotika und Allergien.",
    2: "Pubertät, Zyklus, Schwangerschaft, Verhütung und Vielfalt in Beziehungen.",
    3: "Der See als Ökosystem: Lebewesen, Nahrungsnetze und Gewässergüte.",
    4: "Wie Suchtmittel auf Körper und Gehirn wirken und wie Abhängigkeit entsteht.",
}
karten = []
for nr, (ordner, name) in REIHEN.items():
    fertig = nr in FERTIG
    klasse = "reihe-karte" + ("" if fertig else " in-arbeit")
    stand = "Materialien ansehen" if fertig else "In Vorbereitung"
    karten.append(
        f'<li class="reihe-{nr}"><a class="{klasse}" href="{ordner}/index.html">'
        f'<div class="bildflaeche">{Z.karte_bild(nr)}</div>'
        f'<div class="karte-text"><span class="reihe-nr">Reihe {nr}</span><h2>{html.escape(name)}</h2><p>{beschr[nr]}</p><span class="stand">{stand}</span></div>'
        f'</a></li>')

seite("index.html", "Übersicht", f"""
<section class="buehne">
  <div class="huelle">
    <div>
      <p class="unterzeile">Wahlpflichtkurs</p>
      <h1>Biologie<br>Klasse&nbsp;8</h1>
      <p class="einleitung">Lerntexte, Aufgaben, Übungen und Modelle zum Ausprobieren. Die vier Unterrichtsreihen folgen der Reihenfolge im Schuljahr.</p>
    </div>
    {Z.hero_bild()}
  </div>
</section>
<div class="huelle">
  <ol class="reihen" aria-label="Unterrichtsreihen in der Reihenfolge des Schuljahres">
    {''.join(karten)}
  </ol>
</div>
""", beschreibung="Materialien für den Wahlpflichtkurs Biologie, Klasse 8")

# ======================================================================
# Reihen bauen
# ======================================================================
baue_reihe(1, LT1, AUF1, UEB1 + KRANKHEITEN_UEBUNGEN, MOD1,
           "Wie Krankheitserreger in den Körper gelangen, wie sich das Immunsystem wehrt und was Impfungen, Antibiotika und Allergien damit zu tun haben.",
           Z.reihe1_kopf(), training=TRAINING,
           training_text="Damit kannst du alle Themen der Kursarbeit üben: Fachbegriffe, Bakterien, Viren und das Beschreiben von Krankheiten.")

baue_reihe(2, LT2, AUF2, UEB2, MOD2,
           "Wie sich der Körper in der Pubertät verändert, wie ein neues Leben entsteht, wie man verhütet und sich schützt und was gute Beziehungen ausmacht.",
           Z2.reihe2_kopf(), training=TRAIN2,
           training_text="Wiederhole die wichtigsten Inhalte der Reihe: Fachbegriffe, Zyklus, Verhütung und Infektionsschutz.",
           vorwort=Z2.VORWORT, training_titel="Wiederholen und vertiefen")

baue_reihe(3, LT3, AUF3, UEB3, MOD3,
           "Wie Pflanzen und Tiere im See zusammenleben, wie Energie und Stoffe weitergegeben werden, wie sich der See im Jahreslauf verändert und wie man Gewässer untersucht und schützt.",
           Z3.reihe3_kopf(), training=TRAIN3,
           training_text="Wiederhole die wichtigsten Inhalte der Reihe: Fachbegriffe, Eutrophierung und das Erklären in ganzen Sätzen.",
           training_titel="Wiederholen und vertiefen")

baue_reihe(4, LT4, AUF4, UEB4, MOD4,
           "Was Suchtmittel im Körper und im Gehirn bewirken, wie aus Genuss Abhängigkeit werden kann, welche Gesetze gelten und wo es Hilfe gibt.",
           Z4.reihe4_kopf(), training=TRAIN4,
           training_text="Wiederhole die wichtigsten Inhalte der Reihe: Fachbegriffe, Herkunft der Drogen und das Erklären in ganzen Sätzen.",
           vorwort=Z4.VORWORT, training_titel="Wiederholen und vertiefen")
print("fertig")
