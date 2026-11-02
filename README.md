# Biologie Klasse 8 – Wahlpflichtkurs

Materialien für den Wahlpflichtkurs Biologie (Realschule NRW, Klasse 8): Lerntexte, Aufgaben, interaktive Übungen und Modelle.
Die Inhalte orientieren sich am Kernlehrplan für das Wahlpflichtfach Biologie an Realschulen in NRW (2015) und am schulinternen Lehrplan.

## Unterrichtsreihen

| Nr. | Reihe | Inhaltsfeld (KLP WP Biologie) | Stand |
|---|---|---|---|
| 1 | [Abwehr von Krankheiten](reihe-1-abwehr-von-krankheiten/) | IF 2 Biologische Forschung und Medizin | fertig, freischaltbar |
| 2 | [Freundschaft, Liebe, Sexualität](reihe-2-freundschaft-liebe-sexualitaet/) | IF 7 Sexualerziehung | fertig, freischaltbar |
| 3 | [Leben in Gewässern](reihe-3-leben-in-gewaessern/) | IF 1 Ökosysteme (Kontext Ökosystem See) | fertig, freischaltbar |
| 4 | [Drogen und Sucht](reihe-4-drogen-und-sucht/) | schulinterner Kontext, Bezug zu IF 5 Information und Regulation | fertig, freischaltbar |

## Reihen freischalten (für Lehrkräfte)

Welche Reihen Schülerinnen und Schüler sehen, steht in der Datei [`freigabe.json`](freigabe.json):

1. Auf GitHub die Datei `freigabe.json` öffnen und auf den Stift („Edit this file“) klicken.
2. Bei der gewünschten Reihe `false` durch `true` ersetzen (zum Sperren umgekehrt).
3. Unten auf „Commit changes“ klicken.

Danach erzeugt GitHub die Seiten automatisch neu (Reiter „Actions“). Nach etwa zwei Minuten ist die Reihe auf der Website freigeschaltet. Gesperrte Reihen werden gar nicht als Seiten veröffentlicht; Schülerinnen und Schüler sehen nur den Hinweis „Noch nicht freigeschaltet“.

Hinweis: Weil das Repository öffentlich ist, sind die Quelltexte im Ordner `werkzeug/` auf GitHub weiterhin einsehbar. Wer gezielt im Repository sucht, kann die Texte dort also lesen. Auf der Website selbst sind gesperrte Reihen nicht erreichbar.

## Aufbau einer Reihe

```
reihe-x-name/
├── index.html     Übersichtsseite für Schülerinnen und Schüler
├── README.md      Hinweise für Lehrkräfte: Lehrplanbezug, Stundenfolge, Material
├── lerntexte/     Lerntexte zum Lesen im Browser
├── aufgaben/      Aufgaben zu den Lerntexten, druckbar als Arbeitsblatt
├── uebungen/      interaktive Übungen mit sofortiger Rückmeldung
└── modelle/       interaktive Modelle mit Hinweisen zu Modellgrenzen
```

Gemeinsames Design und die Übungsbausteine liegen in `assets/`.

## Seiten neu erzeugen

Alle HTML-Seiten werden aus den Python-Dateien im Ordner `werkzeug/` erzeugt. Nach Änderungen dort: `cd werkzeug && python3 bauen.py`. Texte, Aufgaben und Übungen stehen jeweils in eigenen Dateien (z. B. `reihe2_texte.py`, `reihe2_rest.py`).

## Datenschutz und Urheberrecht

- Die Seiten laden keine externen Inhalte: Schriften und Skripte liegen im Repository selbst. Es werden keine Daten gespeichert oder übertragen, eine Anmeldung ist nicht nötig.
- Texte, Aufgaben, Grafiken und Modelle sind eigens für dieses Repository erstellt.
- Verwendete Schriften: Atkinson Hyperlegible, Bricolage Grotesque und Caveat, alle unter der SIL Open Font License (siehe `assets/fonts/`).
- Alle Zeichnungen sind eigens erstellt und direkt in die Seiten eingebettet.
