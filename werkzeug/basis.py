"""Gemeinsame Bausteine zum Erzeugen der statischen HTML-Seiten."""
import json, os, html
from zeichnungen import deko, zelle
LOGO = deko("0 0 40 40", zelle(20, 20, 16, 13, "f-gruen"))

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REIHEN = {
    1: ("reihe-1-abwehr-von-krankheiten", "Abwehr von Krankheiten"),
    2: ("reihe-2-freundschaft-liebe-sexualitaet", "Freundschaft, Liebe, Sexualität"),
    3: ("reihe-3-leben-in-gewaessern", "Leben in Gewässern"),
    4: ("reihe-4-drogen-und-sucht", "Drogen und Sucht"),
}


def seite(pfad, titel, inhalt, reihe=None, krumen=None, beschreibung="", skripte=(), hauptklasse=""):
    """pfad: relativ zum Repo, z. B. 'reihe-1-.../lerntexte/01.html'"""
    tiefe = pfad.count("/")
    wurzel = "../" * tiefe if tiefe else "./"
    krumen = krumen or []
    pfad_html = ""
    if krumen:
        teile = []
        for text, link in krumen:
            if link:
                teile.append(f'<li><a href="{link}">{html.escape(text)}</a></li>')
            else:
                teile.append(f'<li aria-current="page">{html.escape(text)}</li>')
        pfad_html = f'<nav aria-label="Brotkrümel"><ol class="pfad">{"".join(teile)}</ol></nav>'
    body_klasse = f' class="reihe-{reihe}"' if reihe else ""
    skript_html = "".join(f'\n  <script src="{wurzel}{s}" defer></script>' for s in skripte)
    seite_html = f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(titel)} – Biologie Klasse 8</title>
  <meta name="description" content="{html.escape(beschreibung)}">
  <link rel="stylesheet" href="{wurzel}assets/style.css">{skript_html}
</head>
<body{body_klasse}>
  <header class="kopf">
    <div class="huelle">
      <a class="marke" href="{wurzel}index.html">{LOGO}Biologie Klasse 8</a>
      {pfad_html}
    </div>
  </header>
  <main id="inhalt"{(' class="' + hauptklasse + '"') if hauptklasse else ''}>
{inhalt}
  </main>
  <footer class="fuss">
    <div class="huelle">
      <p>Wahlpflichtkurs Biologie, Klasse 8. Die Übungen speichern keine Daten und funktionieren ohne Anmeldung.</p>
    </div>
  </footer>
</body>
</html>
"""
    ziel = os.path.join(REPO, pfad)
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, "w", encoding="utf-8") as f:
        f.write(seite_html)
    return ziel


def uebung(typ, daten):
    js = json.dumps(daten, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<div class="uebung" data-typ="{typ}">\n<script type="application/json">\n{js}\n</script>\n</div>'


def krumen_reihe(nr, tiefe_in_reihe, extra=None):
    """Brotkrümel für Seiten innerhalb einer Reihe. tiefe_in_reihe: 0 = Reihenübersicht, 1 = Unterordner."""
    ordner, name = REIHEN[nr]
    hoch = "../" * (tiefe_in_reihe + 1)
    k = []
    if extra:
        k.append((name, "../" * tiefe_in_reihe + "index.html"))
        k.append((extra, None))
    else:
        k.append((name, None))
    return k


def schreibe(pfad, text):
    ziel = os.path.join(REPO, pfad)
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, "w", encoding="utf-8") as f:
        f.write(text)
