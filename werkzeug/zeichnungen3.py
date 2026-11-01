"""Zeichnungen der Reihe 3: Leben in Gewässern."""
import math
import zeichnungen as Z
from zeichnungen import svg, deko, text, pfeil, blob, funkeln, zelle

WASSER = "f-blau-weich"


# ---------------------------------------------------------------- Bausteine
def fisch(x, y, s=1.0, fill="f-gelb", w=0, spiegel=False):
    sx = -s if spiegel else s
    return (f'<g transform="translate({x} {y}) rotate({w}) scale({sx} {s})">'
            f'<path class="s {fill}" d="M-26 0 C -14 -16, 14 -16, 24 0 C 14 16, -14 16, -26 0 Z"/>'
            f'<path class="s {fill}" d="M24 0 L 40 -12 L 37 0 L 40 12 Z"/>'
            f'<circle class="d" cx="-15" cy="-3" r="2.4"/><path class="s2" fill="none" d="M-5 -10 q 6 10 0 20"/></g>')


def hecht(x, y, s=1.0, spiegel=False):
    sx = -s if spiegel else s
    return (f'<g transform="translate({x} {y}) scale({sx} {s})">'
            f'<path class="s f-gruen" d="M-48 0 C -40 -9, 20 -11, 34 -2 C 20 9, -40 9, -48 0 Z"/>'
            f'<path class="s f-gruen" d="M34 -2 L 50 -12 L 46 0 L 50 10 Z"/><path class="s f-gruen" d="M14 -8 L 22 -16 L 26 -6 Z"/>'
            f'<circle class="d" cx="-34" cy="-2" r="2.2"/><path class="s2" fill="none" d="M-48 1 H -36"/>'
            + "".join(f'<circle class="s2" cx="{-10 + k * 9}" cy="{-1 + (k % 2) * 3}" r="1.6" fill="none"/>' for k in range(4)) + '</g>')


def schilf(x, y, h=120, n=3):
    g = ""
    for k in range(n):
        dx = (k - (n - 1) / 2) * 9
        g += f'<path class="s k-gruen" stroke-width="3" fill="none" d="M{x + dx} {y} C {x + dx - 2} {y - h * 0.5}, {x + dx + 6} {y - h * 0.8}, {x + dx + 4} {y - h}"/>'
        g += f'<path class="s2 f-gruen" d="M{x + dx + 1} {y - h * 0.45} q 16 -10 28 -34 q -18 10 -28 26 z"/>'
    g += f'<rect class="s f-sand" x="{x + 2}" y="{y - h - 26}" width="9" height="24" rx="4.5"/>'
    return g


def seerose(x, y, r=26, bluete=True):
    blatt = f'<path class="s f-gruen" d="M{x} {y} m {-r} 0 a {r} {r * 0.35} 0 1 0 {2 * r} 0 a {r} {r * 0.35} 0 0 0 {-r * 0.9} {-r * 0.3} l {-r * 0.1} {r * 0.3} z"/>'
    b = ""
    if bluete:
        b = "".join(f'<ellipse class="s2 f-weiss" cx="{x + 6 + math.cos(math.radians(a)) * 7:.1f}" cy="{y - 8 + math.sin(math.radians(a)) * 3:.1f}" rx="6" ry="9" transform="rotate({a + 90} {x + 6 + math.cos(math.radians(a)) * 7:.1f} {y - 8 + math.sin(math.radians(a)) * 3:.1f})"/>' for a in range(180, 361, 45))
        b += f'<circle class="s2 f-gelb" cx="{x + 6}" cy="{y - 10}" r="4"/>'
    return blatt + b


def tauchpflanze(x, y, h=80):
    g = f'<path class="s k-gruen" stroke-width="2.5" fill="none" d="M{x} {y} C {x - 6} {y - h * 0.4}, {x + 8} {y - h * 0.7}, {x} {y - h}"/>'
    for k in range(1, 8):
        yy = y - h * k / 8
        g += f'<path class="s2 k-gruen" fill="none" d="M{x} {yy} q -10 -4 -14 -10 M {x} {yy} q 10 -4 14 -10"/>'
    return g


def welle(x0, x1, y, amp=4, klasse="s2 k-blau"):
    d = f"M{x0} {y}"
    x = x0
    while x < x1:
        d += f" q 10 {-amp} 20 0 t 20 0"
        x += 40
    return f'<path class="{klasse}" fill="none" d="{d}"/>'


def larve(x, y, s=1.0, typ="stein", fill="f-sand"):
    if typ == "stein":       # Steinfliegenlarve: zwei Schwanzfäden
        k = '<path class="s2" fill="none" d="M18 0 l 16 -6 M 18 0 l 16 6"/>'
    elif typ == "eintag":    # drei Schwanzfäden, Kiemen
        k = '<path class="s2" fill="none" d="M18 0 l 16 -7 M 18 0 l 18 0 M 18 0 l 16 7"/>' + "".join(f'<path class="s2" fill="none" d="M{-4 + j * 6} -5 l 2 -5 M {-4 + j * 6} 5 l 2 5"/>' for j in range(3))
    elif typ == "koecher":   # Köcher aus Steinchen
        return (f'<g transform="translate({x} {y}) scale({s})">' + "".join(f'<circle class="s2 f-sand" cx="{-16 + j * 6}" cy="{(j % 2) * 3 - 1.5}" r="4"/>' for j in range(6))
                + '<circle class="s2 f-gelb" cx="20" cy="0" r="5"/><path class="s2" fill="none" d="M24 -2 l 6 -4 M 24 2 l 6 4"/></g>')
    elif typ == "flohkrebs":
        return (f'<g transform="translate({x} {y}) scale({s})"><path class="s {fill}" d="M-18 4 C -18 -14, 18 -14, 18 4 Z"/>' + "".join(f'<path class="s2" fill="none" d="M{-12 + j * 6} 4 v 8"/>' for j in range(5))
                + '<path class="s2" fill="none" d="M18 0 q 8 -10 14 -8 M 18 2 q 10 -4 14 0"/></g>')
    elif typ == "assel":
        return (f'<g transform="translate({x} {y}) scale({s})"><ellipse class="s f-blau-tief" cx="0" cy="0" rx="18" ry="9"/>' + "".join(f'<path class="s2" fill="none" d="M{-12 + j * 6} -8 v 8"/>' for j in range(5))
                + "".join(f'<path class="s2" fill="none" d="M{-14 + j * 7} 8 l -3 6 M {-14 + j * 7} -8 l -3 -6"/>' for j in range(5)) + '<path class="s2" fill="none" d="M18 -3 l 10 -6 M 18 3 l 10 6"/></g>')
    elif typ == "zuckmuecke":
        return f'<g transform="translate({x} {y}) scale({s})"><path class="s" fill="none" style="stroke:var(--eosin)" stroke-width="6" stroke-linecap="round" d="M-20 4 C -10 -10, 4 10, 20 -4"/></g>'
    elif typ == "tubifex":
        return f'<g transform="translate({x} {y}) scale({s})"><path class="s" fill="none" style="stroke:var(--eosin)" stroke-width="3" stroke-linecap="round" d="M-8 10 C -4 -4, 4 0, 2 -14 M 4 10 C 8 0, 14 2, 12 -12 M -14 10 C -18 0, -12 -6, -16 -16"/><path class="s f-sand" d="M-24 10 H 24 V 16 H -24 Z"/></g>'
    else:
        k = ""
    body = f'<ellipse class="s {fill}" cx="0" cy="0" rx="18" ry="6"/><circle class="s {fill}" cx="-20" cy="0" r="5"/>'
    beine = "".join(f'<path class="s2" fill="none" d="M{-10 + j * 8} -5 l -4 -8 M {-10 + j * 8} 5 l -4 8"/>' for j in range(3))
    fuehler = '<path class="s2" fill="none" d="M-24 -2 l -10 -6 M -24 2 l -10 6"/>'
    return f'<g transform="translate({x} {y}) scale({s})">{beine}{body}{fuehler}{k}</g>'


def wasserfloh(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-blau-weich" d="M-12 -14 C 10 -20, 22 0, 14 16 C 8 24, -10 20, -14 8 Z"/>'
            f'<circle class="s2 f-blau-tief" cx="-10" cy="-10" r="4"/><circle class="d" cx="-11" cy="-11" r="1.6"/>'
            f'<path class="s2" fill="none" d="M-12 -10 C -26 -24, -34 -10, -40 -18 M -12 -10 C -24 -2, -34 -4, -40 2"/>'
            f'<path class="s2 k-rosa" fill="none" d="M-4 -6 C 4 0, 0 8, 6 14"/></g>')


def alge(x, y, r=6):
    return f'<circle class="s2 f-gruen" cx="{x}" cy="{y}" r="{r}"/><circle class="d" cx="{x - r * 0.2:.1f}" cy="{y - r * 0.2:.1f}" r="{r * 0.18:.1f}"/>'


# ---------------------------------------------------------------- Abbildungen
def see_profil(breite=760, hoehe=330):
    """See-Querschnitt mit Ufer links"""
    boden = "M0 100 L 120 100 C 160 102, 180 120, 210 150 C 260 200, 360 290, 520 300 C 620 305, 700 300, 760 296 L 760 330 L 0 330 Z"
    return (f'<path class="f-blau-weich" d="M120 100 C 160 102, 180 120, 210 150 C 260 200, 360 290, 520 300 C 620 305, 700 300, 760 296 L 760 100 Z"/>'
            + welle(130, 760, 100) + f'<path class="s f-sand" d="{boden}"/>')


def see_zonen():
    i = see_profil()
    # Erlenbruch
    i += '<path class="s2 k-bernstein" stroke-width="5" d="M50 100 V 40" fill="none"/><circle class="s f-gruen" cx="50" cy="34" r="26"/><circle class="s f-gruen" cx="84" cy="50" r="18"/><path class="s2 k-bernstein" stroke-width="4" d="M84 100 V 64" fill="none"/>'
    i += schilf(150, 112, 90) + schilf(180, 130, 80)
    i += seerose(240, 100, 22) + seerose(285, 100, 18, False) + '<path class="s2 k-gruen" fill="none" d="M240 104 V 176 M 285 104 V 196"/>'
    i += tauchpflanze(340, 240, 120) + tauchpflanze(380, 262, 130) + tauchpflanze(420, 278, 120)
    i += fisch(560, 170, 0.9, "f-gelb", spiegel=True) + hecht(650, 220, 1.0) + fisch(600, 250, 0.7, "f-gelb")
    i += "".join(alge(500 + k * 37 % 230, 120 + (k * 23) % 40, 4) for k in range(8))
    i += larve(560, 296, 0.7, "tubifex") + larve(700, 292, 0.8, "zuckmuecke")
    # Zonenbeschriftung
    zonen = [(50, "Erlenbruch"), (165, "Röhricht"), (262, "Schwimmblatt"), (380, "Tauchblatt"), (610, "Freiwasser")]
    for k, (x, t) in enumerate(zonen):
        i += text(x, 362, t, "hk")
    i += text(630, 324, "Bodenzone", "hk")
    for x0, x1 in [(0, 110), (110, 210), (210, 310), (310, 470), (470, 760)]:
        i += f'<path class="s2" d="M{x0 + 4} 340 H {x1 - 4}" /><path class="s2" d="M{x0 + 4} 335 v 10 M {x1 - 4} 335 v 10"/>'
    return svg("0 0 760 372", i, "Die Zonen eines Sees im Querschnitt",
               "Vom Ufer aus: Erlenbruchzone mit Bäumen, Röhrichtzone mit Schilf, Schwimmblattzone mit Seerosen, Tauchblattzone mit Unterwasserpflanzen und die Freiwasserzone mit Plankton und Fischen. Am Grund liegt die Bodenzone mit Zuckmückenlarven und Schlammröhrenwürmern.")


def seerosenblatt():
    # Querschnitt durch ein Schwimmblatt, schematisch
    i = '<rect class="f-blau-weich" x="0" y="160" width="640" height="80"/>' + welle(0, 640, 160)
    i += '<rect class="s f-gruen" x="60" y="128" width="520" height="40" rx="10"/>'
    i += "".join(f'<rect class="s2 f-gruen-weich" x="{80 + k * 30}" y="132" width="22" height="12" rx="3"/>' for k in range(16))
    i += "".join(f'<circle class="s2 f-weiss" cx="{100 + k * 60}" cy="156" r="7"/>' for k in range(8))
    i += "".join(f'<path class="s2" d="M{110 + k * 90} 128 v -6 M {116 + k * 90} 128 v -6" />' for k in range(6))
    i += '<path class="s2 k-bernstein" d="M66 127 H 574" stroke-width="3"/>'
    labels = [((300, 122), (300, 60), "Wachsschicht"), ((116, 124), (120, 30), "Spaltöffnungen oben"), ((470, 138), (520, 70), "Zellen mit Chloroplasten"),
              ((340, 156), (300, 214), "Lufträume")]
    for (x1, y1), (x2, y2), t in labels:
        i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2} {y2 + (6 if y2 < y1 else -18)}"/><circle class="d" cx="{x1}" cy="{y1}" r="2.6"/>' + text(x2, y2, t, "hk")
    i += text(40, 226, "Wasser", "hk", "start")
    return svg("0 0 640 240", i, "Querschnitt durch das Schwimmblatt einer Seerose (schematisch)",
               "Das Blatt liegt auf dem Wasser. Oben eine Wachsschicht und die Spaltöffnungen, darunter dicht gepackte Zellen mit Chloroplasten, unten große Lufträume, die Auftrieb geben.")


NETZ_KNOTEN = {
    "algen": (110, 290, "Algen", "f-gruen"), "pflanzen": (300, 300, "Wasserpflanzen", "f-gruen"),
    "floh": (90, 200, "Wasserfloh", "f-blau-weich"), "schnecke": (290, 210, "Schnecke", "f-sand"), "muecke": (470, 230, "Mückenlarve", "f-sand"),
    "rotauge": (160, 120, "Rotauge", "f-gelb"), "barsch": (350, 120, "Barsch", "f-gelb"), "libelle": (520, 140, "Libellenlarve", "f-sand"),
    "hecht": (230, 36, "Hecht", "f-gruen"), "reiher": (460, 40, "Graureiher", "f-weiss"),
    "destruenten": (560, 310, "Bakterien, Pilze", "f-rosa"),
}
NETZ_KANTEN = [("algen", "floh"), ("algen", "schnecke"), ("pflanzen", "schnecke"), ("pflanzen", "rotauge"), ("algen", "muecke"),
               ("floh", "rotauge"), ("floh", "barsch"), ("muecke", "barsch"), ("muecke", "libelle"), ("schnecke", "rotauge"),
               ("rotauge", "hecht"), ("barsch", "hecht"), ("rotauge", "reiher"), ("barsch", "reiher"), ("libelle", "barsch")]


def nahrungsnetz():
    i = ""
    for a, b in NETZ_KANTEN:
        x1, y1 = NETZ_KNOTEN[a][:2]
        x2, y2 = NETZ_KNOTEN[b][:2]
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        i += pfeil(round(x1 + ux * 26, 1), round(y1 + uy * 20, 1), round(x2 - ux * 30, 1), round(y2 - uy * 22, 1), "s2")
    i += text(560, 348, "zersetzen alle toten Lebewesen", "hk")
    for k, (x, y, t, f) in NETZ_KNOTEN.items():
        w = max(84, len(t) * 10)
        i += f'<rect class="s {f}" x="{x - w / 2}" y="{y - 17}" width="{w}" height="34" rx="17"/>' + text(x, y + 6, t, "hk")
    for y, t in [(40, "Konsumenten 3. Ordnung"), (125, "Konsumenten 2. Ordnung"), (215, "Konsumenten 1. Ordnung"), (300, "Produzenten")]:
        i += text(816, y, t, "hk", "end")
    return svg("0 0 820 360", i, "Ein vereinfachtes Nahrungsnetz im See",
               "Algen und Wasserpflanzen sind die Produzenten. Wasserfloh, Schnecke und Mückenlarve fressen Algen oder Pflanzen. Rotauge, Barsch und Libellenlarve fressen diese Tiere. Hecht und Graureiher stehen an der Spitze. Bakterien und Pilze zersetzen abgestorbene Lebewesen.")


def energiepyramide():
    stufen = [("Hecht", 10, "f-gruen", "1 Einheit"), ("Rotauge", 100, "f-gelb", "10 Einheiten"), ("Wasserfloh", 1000, "f-blau-weich", "100 Einheiten"), ("Algen", 10000, "f-gruen-weich", "1000 Einheiten")]
    i = ""
    for k, (t, _, f, e) in enumerate(stufen):
        w = 120 + k * 120
        y = 20 + k * 60
        i += f'<rect class="s {f}" x="{320 - w / 2}" y="{y}" width="{w}" height="52" rx="6"/>' + text(320, y + 33, t, "h") + text(320 + w / 2 + 16, y + 33, e, "hk", "start")
        if k < 3:
            i += f'<path class="s2 k-rosa" fill="none" d="M{320 - w / 2 - 6} {y + 80} q -40 -10 -60 -40"/>' + text(320 - w / 2 - 70, y + 34, "90 % Verlust", "hk", "end")
    i += text(320, 290, "Energie, die in jeder Stufe gespeichert ist", "hk")
    return svg("-70 0 790 300", i, "Energiepyramide eines Sees",
               "Vier Stufen: Algen speichern 1000 Energieeinheiten, Wasserflöhe 100, Rotaugen 10, Hechte 1. Von Stufe zu Stufe gehen etwa 90 Prozent der Energie als Wärme und durch Bewegung verloren.")


def see_jahreszeiten():
    def becken(ox, titel, oben, mitte, unten, eis=False, zirk=False):
        g = f'<g transform="translate({ox} 0)">'
        g += f'<path class="s f-sand" d="M0 40 L 20 200 H 160 L 180 40 Z"/>'
        if zirk:
            g += f'<path class="f-blau" d="M6 44 L 24 194 H 156 L 174 44 Z"/>'
            g += '<path class="s2 k-blau" fill="none" d="M90 92 C 40 92, 40 176, 90 176 C 140 176, 140 92, 96 92"/>' + pfeil(104, 92, 94, 92, "s2 k-blau") + pfeil(80, 176, 92, 176, "s2 k-blau")
        else:
            g += f'<path class="f-rosa" d="M6 44 L 13 100 H 167 L 174 44 Z"/>' if oben == "warm" else f'<path class="f-blau-weich" d="M6 44 L 13 100 H 167 L 174 44 Z"/>'
            g += f'<path class="f-blau-weich" d="M13 100 L 16 124 H 164 L 167 100 Z"/>'
            g += f'<path class="f-blau" d="M16 124 L 24 194 H 156 L 164 124 Z"/>'
            g += '<path class="s2" stroke-dasharray="4 4" d="M13 100 H 167 M 16 124 H 164"/>'
        if eis:
            g += '<rect class="s f-weiss" x="4" y="36" width="172" height="12" rx="3"/>'
        g += f'<path class="s" fill="none" d="M0 40 L 20 200 H 160 L 180 40"/>'
        g += text(90, 24, titel, "h") + text(90, 72 if not zirk else 138, oben if not zirk else mitte, "hk") + (text(90, 160, unten, "hk") if not zirk else "")
        return g + "</g>"
    i = (becken(0, "Frühling", "", "4 °C", "", zirk=True) + becken(200, "Sommer", "warm", "", "4–6 °C")
         + becken(400, "Herbst", "", "8 °C", "", zirk=True) + becken(600, "Winter", "kalt", "", "4 °C", eis=True))
    i = i.replace('>warm<', '>über 20 °C<').replace('>kalt<', '>0–4 °C<')
    i += text(300, 116, "Sprungschicht", "hk") + text(390, 230, "Zirkulation: der See wird durchmischt", "hk") + text(90, 230, "Zirkulation", "hk") + text(690, 230, "Stagnation", "hk") + text(290, 230, "Stagnation", "hk")
    i = i.replace(text(390, 230, "Zirkulation: der See wird durchmischt", "hk"), text(490, 230, "Zirkulation", "hk"))
    return svg("0 0 780 240", i, "Temperaturschichtung eines Sees im Jahreslauf",
               "Im Frühling und Herbst ist der See überall gleich warm und wird vom Wind durchmischt (Zirkulation). Im Sommer liegt warmes Wasser über einer Sprungschicht und kaltem Tiefenwasser von 4 bis 6 Grad. Im Winter liegt unter dem Eis kaltes Wasser, am Grund 4 Grad (Stagnation).")


def stoffkreislauf():
    pos = {"p": (320, 50, "Produzenten", "Algen, Wasserpflanzen", "f-gruen"), "k": (560, 170, "Konsumenten", "Tiere", "f-gelb"),
           "t": (320, 290, "totes Material", "Leichen, Kot, Laub", "f-sand"), "d": (80, 170, "Destruenten", "Bakterien, Pilze", "f-rosa")}
    i = ""
    for k, (x, y, t, u, f) in pos.items():
        i += f'<rect class="s {f}" x="{x - 90}" y="{y - 32}" width="180" height="64" rx="16"/>' + text(x, y - 4, t, "h") + text(x, y + 20, u, "hk")
    i += pfeil(412, 60, 520, 132, "s", 10) + text(500, 84, "werden gefressen", "hk")
    i += pfeil(530, 206, 412, 280, "s", 10) + text(530, 270, "sterben ab", "hk")
    i += pfeil(228, 282, 110, 206, "s", 10) + text(116, 270, "werden zersetzt", "hk")
    i += pfeil(110, 132, 228, 60, "s", 10) + text(96, 84, "Mineralstoffe", "hk") + text(96, 104, "und CO₂", "hk")
    i += Z.funkeln(320, 160, 1.4) + text(320, 200, "Lichtenergie", "hk")
    i += pfeil(320, 150, 320, 90, "s2 k-bernstein")
    return svg("0 0 640 330", i, "Stoffkreislauf im See",
               "Produzenten werden von Konsumenten gefressen. Beide sterben ab und werden zu totem Material. Destruenten zersetzen es zu Mineralstoffen und Kohlenstoffdioxid, die wieder von den Produzenten aufgenommen werden. Energie kommt als Licht hinzu.")


def einzeller():
    pantoffel = ('<g transform="translate(110 120)"><path class="s f-sand" d="M-70 -10 C -60 -46, 40 -44, 70 -16 C 80 0, 70 24, 40 30 C 10 34, -10 14, -30 24 C -60 36, -76 16, -70 -10 Z"/>'
                 + "".join(f'<path class="s2" fill="none" d="M{-70 + k * 10} {-14 - (8 if 2 < k < 12 else 0)} l -3 -6"/>' for k in range(14))
                 + '<circle class="s2 f-blau-weich" cx="-40" cy="-8" r="8"/><circle class="s2 f-blau-weich" cx="40" cy="-6" r="8"/>'
                 + '<ellipse class="s2 f-rosa" cx="0" cy="-4" rx="12" ry="8"/><circle class="s2 f-gelb" cx="20" cy="10" r="5"/><circle class="s2 f-gelb" cx="-14" cy="12" r="4"/>'
                 + '<path class="s2" fill="none" d="M-6 22 q 10 -10 22 -4"/></g>' + text(110, 200, "Pantoffeltierchen", "h"))
    amoebe = ('<g transform="translate(330 120)"><path class="s f-blau-weich" d="M-40 -6 C -60 -30, -30 -50, -14 -30 C -6 -60, 30 -50, 24 -24 C 54 -30, 64 0, 40 10 C 56 30, 20 48, 6 30 C -6 52, -44 44, -30 20 C -56 22, -60 4, -40 -6 Z"/>'
              '<ellipse class="s2 f-rosa" cx="0" cy="0" rx="10" ry="8"/><circle class="s2 f-gelb" cx="20" cy="14" r="5"/></g>' + text(330, 200, "Amöbe", "h"))
    euglena = ('<g transform="translate(540 120)"><path class="s f-gruen-weich" d="M-60 0 C -50 -22, 30 -24, 50 0 C 30 24, -50 22, -60 0 Z"/>'
               + "".join(f'<ellipse class="s2 f-gruen" cx="{-30 + k * 16}" cy="{(k % 2) * 8 - 4}" rx="6" ry="3.5"/>' for k in range(5))
               + '<circle cx="-48" cy="-4" r="4" fill="#d9483b"/><path class="s2" fill="none" d="M-60 0 C -80 -20, -96 6, -116 -12"/><ellipse class="s2 f-rosa" cx="10" cy="2" rx="7" ry="5"/></g>'
               + text(520, 200, "Augentierchen", "h"))
    i = pantoffel + amoebe + euglena
    for (x1, y1), (x2, y2), t in [((70, 112), (40, 30), "Wimpern"), ((110, 116), (140, 30), "Zellkern"), ((150, 114), (230, 50), "pulsierende Vakuole"),
                                  ((530, 116), (560, 40), "Chloroplasten"), ((492, 116), (440, 50), "Augenfleck"), ((440, 108), (420, 84), "Geißel")]:
        i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2} {y2 + 6}"/><circle class="d" cx="{x1}" cy="{y1}" r="2.4"/>' + text(x2, y2, t, "hk")
    return svg("0 0 660 216", i, "Einzeller aus dem Teich (schematisch, nicht im gleichen Maßstab)",
               "Das Pantoffeltierchen mit Wimpern, Zellkern und pulsierenden Vakuolen, die formveränderliche Amöbe mit Scheinfüßchen und das grüne Augentierchen mit Chloroplasten, rotem Augenfleck und Geißel.")


def zeigerorganismen():
    reihen = [("1 unbelastet", "f-blau-weich", [("stein", "Steinfliegenlarve"), ("eintag", "Eintagsfliegenlarve"), ("koecher", "Köcherfliegenlarve")]),
              ("2 mäßig belastet", "f-gruen-weich", [("flohkrebs", "Bachflohkrebs")]),
              ("3 stark belastet", "f-gelb-weich", [("assel", "Wasserassel")]),
              ("4 sehr stark belastet", "f-rosa-weich", [("zuckmuecke", "Rote Zuckmückenlarve"), ("tubifex", "Schlammröhrenwurm")])]
    pos = [(0, 0, 500), (510, 0, 190), (0, 170, 190), (200, 170, 500)]
    i = ""
    for (titel, f, tiere), (x, y, w) in zip(reihen, pos):
        i += f'<rect class="s2 {f}" x="{x + 4}" y="{y + 4}" width="{w - 8}" height="156" rx="16"/>' + text(x + w / 2, y + 32, titel, "h")
        schritt = (w - 20) / len(tiere)
        for k, (typ, name) in enumerate(tiere):
            cx = x + 10 + schritt * (k + 0.5)
            i += larve(cx, y + 86, 1.3, typ) + text(cx, y + 140, name, "hk")
    i += text(350, 352, "Je höher die Stufe, desto weniger Sauerstoff im Wasser.", "hk")
    return svg("0 0 700 362", i, "Zeigerorganismen für die Gewässergüte",
               "Unbelastetes Wasser: Steinfliegen-, Eintagsfliegen- und Köcherfliegenlarven. Mäßig belastet: Bachflohkrebs. Stark belastet: Wasserassel. Sehr stark belastet: Rote Zuckmückenlarve und Schlammröhrenwurm.")


def eutrophierung():
    schritte = [("Nährstoffe", ["Dünger und", "Abwasser", "gelangen ins", "Wasser"]), ("Algenblüte", ["Algen", "vermehren sich", "massenhaft"]),
                ("Algen sterben", ["und sinken", "zum Grund"]), ("Zersetzung", ["Destruenten", "verbrauchen", "Sauerstoff"]), ("O₂-Mangel", ["Fische sterben,", "Faulschlamm", "entsteht"])]
    i = ""
    for k, (t, zeilen) in enumerate(schritte):
        x = 10 + k * 166
        f = ["f-sand", "f-gruen", "f-gruen-weich", "f-rosa-weich", "f-rosa"][k]
        i += f'<rect class="s {f}" x="{x}" y="40" width="146" height="210" rx="14"/>' + text(x + 73, 26, f"{k + 1}.", "h")
        i += text(x + 73, 138, t, "h") + "".join(text(x + 73, 168 + j * 22, z, "hk") for j, z in enumerate(zeilen))
        if k < 4:
            i += pfeil(x + 148, 145, x + 164, 145, "s2")
        cx = x + 73
        if k == 0:
            i += f'<path class="s f-weiss" d="M{cx - 20} 60 h 40 v 30 h -40 z"/>' + "".join(f'<circle class="d" cx="{cx - 8 + j * 8}" cy="{98 + (j % 2) * 6}" r="2"/>' for j in range(3))
        elif k == 1:
            i += "".join(alge(cx - 30 + (j * 13) % 60, 64 + (j * 7) % 40, 5) for j in range(10))
        elif k == 2:
            i += "".join(alge(cx - 30 + j * 12, 66 + j * 8, 4) for j in range(5)) + pfeil(cx + 34, 64, cx + 34, 104, "s2")
        elif k == 3:
            i += "".join(f'<circle class="s2 f-weiss" cx="{cx - 24 + j * 16}" cy="{100 - (j % 2) * 8}" r="5"/>' for j in range(4)) + text(cx, 74, "O₂", "hk")
        else:
            i += fisch(cx, 86, 0.8, "f-weiss", 180)
    return svg("0 0 840 260", i, "Ablauf der Eutrophierung",
               "1. Dünger und Abwasser bringen Nährstoffe ins Wasser. 2. Algen vermehren sich massenhaft. 3. Die Algen sterben und sinken zum Grund. 4. Destruenten zersetzen sie und verbrauchen Sauerstoff. 5. Es entsteht Sauerstoffmangel, Fische sterben.")


FIGUREN = {
    "see_zonen": (see_zonen, "Die Zonen eines Sees vom Ufer bis zur Mitte (schematisch)."),
    "seerosenblatt": (seerosenblatt, "Schwimmblatt der Seerose im Querschnitt (schematisch)."),
    "nahrungsnetz": (nahrungsnetz, "Ein vereinfachtes Nahrungsnetz im See. Die Pfeile zeigen, wohin Stoffe und Energie gelangen."),
    "energiepyramide": (energiepyramide, "Nur etwa ein Zehntel der Energie gelangt in die nächste Stufe."),
    "see_jahreszeiten": (see_jahreszeiten, "Temperaturschichtung eines tiefen Sees im Jahreslauf."),
    "stoffkreislauf": (stoffkreislauf, "Stoffe laufen im Kreis, Energie kommt als Licht hinzu."),
    "einzeller": (einzeller, "Drei Einzeller aus dem Teich (nicht im gleichen Maßstab)."),
    "zeigerorganismen": (zeigerorganismen, "Zeigerorganismen verraten die Wassergüte."),
    "eutrophierung": (eutrophierung, "Wie ein See „umkippt“."),
}


# ---------------------------------------------------------------- Kopfbilder
def reihe3_kopf():
    i = ('<path class="f-blau-weich" d="M0 90 H 520 V 260 H 0 Z"/>' + welle(0, 520, 90, 5)
         + '<path class="s f-sand" d="M0 230 C 120 220, 200 250, 300 236 S 460 226, 520 240 V 260 H 0 Z"/>'
         + schilf(40, 140, 110) + schilf(70, 150, 90) + seerose(160, 90, 24) + seerose(210, 92, 18, False)
         + tauchpflanze(250, 234, 100) + hecht(390, 150, 1.2) + fisch(300, 190, 0.8, "f-gelb", spiegel=True) + fisch(460, 210, 0.7, "f-gelb")
         + wasserfloh(140, 190, 0.8) + "".join(alge(330 + k * 23 % 160, 110 + (k * 11) % 30, 4) for k in range(7))
         + '<circle class="s f-gelb" cx="470" cy="40" r="22"/>' + "".join(f'<line class="s2 k-bernstein" x1="{470 + math.cos(math.radians(a)) * 30:.1f}" y1="{40 + math.sin(math.radians(a)) * 30:.1f}" x2="{470 + math.cos(math.radians(a)) * 38:.1f}" y2="{40 + math.sin(math.radians(a)) * 38:.1f}"/>' for a in range(0, 360, 45))
         + funkeln(300, 40, 0.8, "k-blau"))
    return deko("0 0 520 260", i, "ill kopf-bild")


def kopf(slug):
    hint = blob(300, 112, 280, 96, "f-blau-weich", 2)
    if slug == "01-oekosystem-see":
        i = ('<path class="f-blau-weich" d="M60 110 H 560 V 200 H 60 Z"/>' + welle(60, 560, 110)
             + '<path class="s f-sand" d="M40 110 C 120 112, 150 200, 300 206 S 520 190, 580 110 V 220 H 40 Z"/>'
             + schilf(90, 126, 90) + seerose(180, 110, 20) + tauchpflanze(240, 196, 70) + fisch(380, 160, 0.9, "f-gelb") + hecht(470, 140, 0.9, True)
             + '<g transform="translate(520 60)"><path class="s f-weiss" d="M-30 10 C -30 -10, 0 -16, 10 -4 L 34 -12 L 22 2 C 20 20, -20 26, -30 10 Z"/><circle class="d" cx="2" cy="-2" r="2"/><path class="s2 k-bernstein" stroke-width="3" fill="none" d="M10 -4 L 30 -10"/></g>')
    elif slug == "02-wasserpflanzen-fotosynthese":
        i = (hint + '<g transform="translate(150 110)"><rect class="s f-weiss" x="-50" y="-70" width="100" height="140" rx="10"/><rect class="f-blau-weich" x="-46" y="-40" width="92" height="106"/>'
             + tauchpflanze(0, 60, 90) + "".join(f'<circle class="s2 f-weiss" cx="{4 + (k % 2) * 6}" cy="{-30 - k * 12}" r="{3 + k % 2}"/>' for k in range(4)) + '</g>'
             + '<circle class="s f-gelb" cx="300" cy="60" r="26"/>' + "".join(f'<line class="s2 k-bernstein" x1="{300 + math.cos(math.radians(a)) * 34:.1f}" y1="{60 + math.sin(math.radians(a)) * 34:.1f}" x2="{300 + math.cos(math.radians(a)) * 44:.1f}" y2="{60 + math.sin(math.radians(a)) * 44:.1f}"/>' for a in range(0, 360, 45))
             + seerose(430, 140, 40) + text(330, 180, "CO₂ + H₂O → Zucker + O₂", "h") + pfeil(280, 90, 200, 120, "s2 k-bernstein"))
    elif slug == "03-nahrungsbeziehungen":
        i = (hint + alge(80, 120, 10) + alge(100, 100, 8) + alge(70, 96, 7) + pfeil(120, 110, 170, 110, "s2") + wasserfloh(210, 110, 1.2)
             + pfeil(250, 110, 290, 110, "s2") + fisch(340, 110, 1.1, "f-gelb") + pfeil(390, 110, 430, 110, "s2") + hecht(500, 110, 1.2))
    elif slug == "04-see-im-jahreslauf":
        i = hint
        for k, (f, t) in enumerate([("f-gruen", "Frühling"), ("f-rosa", "Sommer"), ("f-gelb", "Herbst"), ("f-blau", "Winter")]):
            x = 90 + k * 140
            i += f'<path class="s f-sand" d="M{x - 50} 70 L {x - 40} 170 H {x + 40} L {x + 50} 70 Z"/><path class="{f}" d="M{x - 46} 74 L {x - 38} 166 H {x + 38} L {x + 46} 74 Z"/>' + text(x, 54, t, "h")
        i += '<rect class="s f-weiss" x="462" y="68" width="96" height="10" rx="3"/>' + '<circle class="s f-gelb" cx="300" cy="36" r="12"/>'
    elif slug == "05-kleinstlebewesen":
        i = (hint + '<circle class="s f-weiss" cx="220" cy="110" r="90"/>' + '<g transform="translate(180 100) scale(.6)">' + einzeller_klein() + '</g>'
             + wasserfloh(260, 140, 1.3) + "".join(alge(160 + k * 21 % 120, 60 + (k * 17) % 100, 5) for k in range(6))
             + '<path class="s f-sand" d="M300 170 L 360 230" stroke-width="16" style="stroke:var(--tinte)"/><path d="M300 170 L 360 230" stroke-width="10" style="stroke:var(--ill-sand)"/>'
             + '<g transform="translate(470 110)"><path class="s f-weiss" d="M-14 -70 h 28 v 90 q 0 30 -14 30 q -14 0 -14 -30 z"/><rect class="s f-rosa" x="-18" y="-90" width="36" height="22" rx="6"/><path class="f-blau-weich" d="M-12 0 h 24 v 20 q 0 28 -12 28 q -12 0 -12 -28 z"/></g>')
    else:
        i = (hint + '<path class="f-blau-weich" d="M40 120 C 140 100, 240 140, 340 120 S 520 100, 580 130 V 180 C 480 160, 380 190, 280 170 S 120 160, 40 180 Z"/>'
             + "".join(f'<ellipse class="s f-sand" cx="{80 + k * 70}" cy="{150 + (k % 2) * 10}" rx="22" ry="12"/>' for k in range(7))
             + larve(150, 70, 1.2, "stein") + larve(300, 60, 1.2, "flohkrebs") + larve(450, 70, 1.1, "koecher")
             + '<g transform="translate(540 50)"><rect class="s f-weiss" x="-16" y="-30" width="32" height="64" rx="6"/><rect class="f-gruen" x="-12" y="-6" width="24" height="10"/><rect class="f-gelb" x="-12" y="8" width="24" height="10"/></g>')
    return deko("0 0 600 220", i, "ill lt-kopf")


def einzeller_klein():
    return ('<path class="s f-sand" d="M-70 -10 C -60 -46, 40 -44, 70 -16 C 80 0, 70 24, 40 30 C 10 34, -10 14, -30 24 C -60 36, -76 16, -70 -10 Z"/>'
            '<ellipse class="s2 f-rosa" cx="0" cy="-4" rx="12" ry="8"/>')


def _s(i):
    return lambda: i


SYMBOLE = {
    "01-oekosystem-see": _s('<path class="f-blau-weich" d="M6 30 H 58 V 54 H 6 Z"/>' + welle(6, 58, 30, 3) + schilf(14, 50, 34, 1) + fisch(38, 44, 0.45, "f-gelb")),
    "02-wasserpflanzen-fotosynthese": _s(tauchpflanze(32, 58, 48) + '<circle class="s2 f-weiss" cx="40" cy="14" r="4"/><circle class="s2 f-weiss" cx="44" cy="6" r="3"/>'),
    "03-nahrungsbeziehungen": _s(alge(10, 32, 5) + pfeil(16, 32, 24, 32, "s2") + fisch(40, 32, 0.45, "f-gelb")),
    "04-see-im-jahreslauf": _s('<path class="s f-sand" d="M8 14 L 14 56 H 50 L 56 14 Z"/><path class="f-rosa" d="M11 18 L 13 30 H 51 L 53 18 Z"/><path class="f-blau" d="M14 36 L 16 52 H 48 L 50 36 Z"/>'),
    "05-kleinstlebewesen": _s(wasserfloh(36, 32, 0.9)),
    "06-gewaesser-untersuchen-schuetzen": _s(larve(32, 32, 0.9, "stein")),
    "see": _s('<path class="f-blau-weich" d="M4 24 H 60 V 56 H 4 Z"/>' + welle(4, 60, 24, 3) + '<path class="s f-sand" d="M4 24 C 20 26, 26 52, 40 54 S 56 50, 60 46 V 60 H 4 Z"/>'),
    "nahrungsnetz": _s('<circle class="s2 f-gruen" cx="14" cy="48" r="6"/><circle class="s2 f-gelb" cx="32" cy="30" r="6"/><circle class="s2 f-gruen" cx="50" cy="12" r="6"/><circle class="s2 f-sand" cx="50" cy="44" r="6"/><path class="s2" d="M18 44 L 28 34 M 36 26 L 46 16 M 18 48 L 44 44 M 48 38 L 36 34" fill="none"/>'),
    "raeuber-beute": _s('<path class="s k-rosa" stroke-width="2.5" fill="none" d="M4 36 C 14 10, 24 10, 32 36 S 50 62, 60 36"/><path class="s k-blau" stroke-width="2.5" fill="none" d="M4 44 C 18 44, 22 18, 36 18 S 52 44, 60 44"/>'),
    "fotosynthese": _s('<rect class="s f-weiss" x="18" y="10" width="28" height="46" rx="6"/><rect class="f-blau-weich" x="21" y="22" width="22" height="31"/>' + tauchpflanze(32, 52, 26) + '<circle class="s2 f-weiss" cx="36" cy="18" r="3"/>'),
    "r3-zonen": Z._sym_training, "r3-erzeuger": _s(alge(18, 30, 7) + Z.fresszelle(42, 34, 0.25)), "r3-nahrungskette": Z._sym_reihenfolge,
    "r3-fotosynthese-lueckentext": _s(tauchpflanze(32, 58, 48)), "r3-zeiger": _s(larve(32, 32, 0.9, "assel")), "r3-quiz": Z._sym_quiz,
    "r3-fachbegriffe": Z._sym_training, "r3-eutrophierung": Z._sym_reihenfolge,
    "r3-jahreslauf": _s('<path class="s f-sand" d="M8 14 L 14 56 H 50 L 56 14 Z"/><path class="f-blau" d="M11 18 L 16 52 H 48 L 53 18 Z"/><rect class="s2 f-weiss" x="8" y="12" width="48" height="6" rx="2"/>'), "r3-schreiben": Z._sym_schreiben,
}

for _slug in ["01-oekosystem-see", "02-wasserpflanzen-fotosynthese", "03-nahrungsbeziehungen", "04-see-im-jahreslauf", "05-kleinstlebewesen", "06-gewaesser-untersuchen-schuetzen"]:
    Z.EXTRA_KOEPFE[_slug] = (lambda s=_slug: kopf(s))
Z.EXTRA_SYMBOLE.update(SYMBOLE)
