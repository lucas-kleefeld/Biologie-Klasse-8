"""Zeichnungen der Reihe 4: Drogen und Sucht."""
import math
import zeichnungen as Z
from zeichnungen import svg, deko, text, pfeil, blob, funkeln


# ---------------------------------------------------------------- Bausteine
def kopf_figur(x, y, s=1.0, fill="f-sand", gesicht="neutral"):
    m = {"froh": "M-8 8 q 8 7 16 0", "traurig": "M-8 12 q 8 -7 16 0", "neutral": "M-7 10 h 14"}[gesicht]
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s {fill}" d="M-34 70 C -34 40, -20 30, 0 30 C 20 30, 34 40, 34 70 Z"/>'
            f'<circle class="s {fill}" cx="0" cy="0" r="24"/><circle class="d" cx="-8" cy="-4" r="2.4"/><circle class="d" cx="8" cy="-4" r="2.4"/>'
            f'<path class="s2" fill="none" d="{m}"/></g>')


def nervenzelle_ende(x, y, s=1.0):
    """Endknöpfchen von oben kommend, Öffnung nach unten"""
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-gelb" d="M-20 -90 C -20 -60, -70 -50, -70 -10 C -70 20, 70 20, 70 -10 C 70 -50, 20 -60, 20 -90 Z"/></g>')


def glas(x, y, s=1.0, art="bier"):
    if art == "bier":
        return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-gelb" d="M-14 -30 L -11 20 H 11 L 14 -30 Z"/>'
                f'<path class="s f-weiss" d="M-15 -30 q 4 -8 10 -4 q 5 -6 10 0 q 6 -4 10 4 z"/><path class="s2" fill="none" d="M14 -20 q 10 0 10 12 q 0 12 -10 12"/></g>')
    if art == "wein":
        return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-rosa-tief" d="M-13 -30 Q -13 -6 0 -4 Q 13 -6 13 -30 Z"/>'
                f'<path class="s2" fill="none" d="M0 -4 V 18 M -10 20 H 10"/></g>')
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-weiss" d="M-9 -6 L -7 18 H 7 L 9 -6 Z"/><path class="f-gelb-weich" d="M-8 4 L -7 16 H 7 L 8 4 Z"/></g>')


def zigarette(x, y, s=1.0, w=0, rauch=True):
    return (f'<g transform="translate({x} {y}) rotate({w}) scale({s})"><rect class="s f-weiss" x="-50" y="-7" width="76" height="14" rx="2"/>'
            f'<rect class="s f-gelb" x="26" y="-7" width="26" height="14" rx="2"/><rect class="s2 f-rosa-tief" x="-54" y="-6" width="6" height="12" rx="2"/>'
            + (f'<path class="s2" fill="none" d="M-60 -10 q -8 -10 0 -20 q 8 -10 0 -20"/>' if rauch else '') + '</g>')


def tablette(x, y, r=12, fill="f-rosa"):
    return f'<circle class="s {fill}" cx="{x}" cy="{y}" r="{r}"/><path class="s2" d="M{x - r * 0.6} {y} H {x + r * 0.6}"/>'


def handy(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect class="s f-weiss" x="-22" y="-40" width="44" height="80" rx="8"/>'
            f'<rect class="f-blau-weich" x="-17" y="-32" width="34" height="58" rx="3"/><circle class="s2" cx="0" cy="33" r="3" fill="none"/>'
            f'<path class="s2 k-rosa" fill="none" d="M-8 -14 c 0 -8 8 -8 8 -2 c 0 -6 8 -6 8 2 c 0 6 -8 12 -8 12 c 0 0 -8 -6 -8 -12 z"/></g>')


def blatt_hanf(x, y, s=1.0):
    g = ""
    for w, l in [(-70, 40), (-40, 55), (0, 66), (40, 55), (70, 40), (-100, 24), (100, 24)]:
        g += f'<path class="s2 f-gruen" transform="rotate({w})" d="M0 0 C -6 {-l * 0.4}, -5 {-l * 0.8}, 0 {-l} C 5 {-l * 0.8}, 6 {-l * 0.4}, 0 0 Z"/>'
    return f'<g transform="translate({x} {y}) scale({s})">{g}<path class="s2 k-gruen" d="M0 0 v 20" fill="none"/></g>'


def mohn(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s2 k-gruen" fill="none" d="M0 20 V 60"/>'
            f'<path class="s f-gruen-weich" d="M-18 6 C -20 -14, 20 -14, 18 6 C 16 22, -16 22, -18 6 Z"/>'
            f'<path class="s2 f-gruen" d="M-14 -8 L -8 -16 L 0 -10 L 8 -16 L 14 -8 Z"/></g>')


def koka(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s2 k-gruen" fill="none" d="M0 40 V -30"/>'
            + "".join(f'<ellipse class="s2 f-gruen" cx="{side * 14}" cy="{yy}" rx="12" ry="6" transform="rotate({side * -25} {side * 14} {yy})"/>' for side in (-1, 1) for yy in (-20, 0, 20))
            + '</g>')


def kolben(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-weiss" d="M-8 -40 V -10 L -30 26 Q -32 34 -22 34 H 22 Q 32 34 30 26 L 8 -10 V -40 Z"/>'
            f'<path class="f-rosa-weich" d="M-20 16 L -27 28 Q -28 31 -22 31 H 22 Q 28 31 27 28 L 20 16 Z"/><path class="s2" d="M-12 -40 H 12"/></g>')


# ---------------------------------------------------------------- Abbildungen
def stufen():
    farben = ["f-gruen", "f-gelb", "f-rosa-weich", "f-rosa"]
    namen = ["Genuss", "Missbrauch", "Gewöhnung", "Abhängigkeit"]
    unter = [["bewusst, selten,", "kann verzichten"], ["zu oft, zu viel,", "um Probleme zu vergessen"], ["braucht immer mehr", "(Toleranz)"], ["Kontrollverlust,", "starkes Verlangen"]]
    i = ""
    for k in range(4):
        x, y = 20 + k * 180, 200 - k * 50
        i += f'<rect class="s {farben[k]}" x="{x}" y="{y}" width="176" height="{90 + k * 50}" rx="6"/>'
        i += text(x + 88, y + 30, namen[k], "h") + text(x + 88, y + 52, unter[k][0], "hk") + text(x + 88, y + 72, unter[k][1], "hk")
    i += kopf_figur(108, 130, 0.8, "f-sand", "froh") + kopf_figur(648, -20, 0.8, "f-sand", "traurig")
    i += pfeil(40, 330, 720, 330, "s2") + text(380, 356, "Die Grenzen sind fließend", "hk")
    return svg("0 -50 740 420", i, "Vier Stufen auf dem Weg zur Sucht",
               "Eine Treppe mit vier Stufen: Genuss (bewusst, selten, kann verzichten), Missbrauch (zu oft, zu viel, um Probleme zu vergessen), Gewöhnung (braucht immer mehr, Toleranz) und Abhängigkeit (Kontrollverlust, starkes Verlangen).")


def synapse_bild(rezeptoren=6, droge=False, breite=360, beschriften=True):
    i = nervenzelle_ende(180, 120)
    i += f'<path class="s f-gelb" d="M30 250 C 60 214, 300 214, 330 250 L 330 300 H 30 Z"/>'
    # Bläschen
    for k, (bx, by) in enumerate([(140, 60), (180, 74), (220, 60), (160, 94), (200, 96)]):
        i += f'<circle class="s2 f-weiss" cx="{bx}" cy="{by}" r="13"/>' + "".join(f'<circle class="s2 f-blau-tief" cx="{bx + dx}" cy="{by + dy}" r="3"/>' for dx, dy in [(-4, -3), (4, 2), (-2, 5)])
    # Rezeptoren
    pos = [90 + k * 180 / max(1, rezeptoren - 1) for k in range(rezeptoren)] if rezeptoren > 1 else [180]
    for rx in pos:
        i += f'<path class="s f-rosa" d="M{rx - 10} 226 v -12 h 6 v 6 h 8 v -6 h 6 v 12 z"/>'
    # Botenstoffe im Spalt
    n = 14 if droge else 5
    for k in range(n):
        bx = 100 + (k * 53) % 160
        by = 150 + (k * 29) % 50
        i += f'<circle class="s2 f-blau-tief" cx="{bx}" cy="{by}" r="4"/>'
    if beschriften:
        for (x1, y1), (x2, y2), t in [((150, 60), (40, 36), "Bläschen"), ((200, 160), (300, 150), "Botenstoff"), ((pos[-1], 214), (330, 196), "Rezeptor"),
                                      ((60, 10), (30, 2), ""), ((96, 184), (60, 190), "Spalt")]:
            if not t:
                continue
            i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2 + (14 if x2 < x1 else -14)} {y2 - 6}"/>' + text(x2, y2, t, "hk", "end" if x2 < x1 else "start")
        i += text(250, 46, "1. Nervenzelle", "hk", "start") + text(180, 284, "2. Nervenzelle", "hk")
    return i


def synapse():
    i = synapse_bild()
    i += pfeil(180, 0, 180, 30, "s2 k-bernstein") + text(196, 12, "Signal", "hk", "start")
    return svg("-40 -10 430 310", i, "Aufbau einer Synapse (schematisch)",
               "Das Ende der ersten Nervenzelle enthält Bläschen mit Botenstoffen. Die Botenstoffe werden in den Spalt ausgeschüttet und binden an Rezeptoren der zweiten Nervenzelle.")


def toleranz():
    i = ""
    for k, (rez, dro, t1, t2) in enumerate([(6, False, "vorher", "normale Menge Botenstoff"), (6, True, "Droge", "sehr viel Dopamin"), (2, False, "nach häufigem Konsum", "weniger Rezeptoren")]):
        i += f'<g transform="translate({k * 280} 0) scale(.7)">{synapse_bild(rez, dro, beschriften=False)}</g>'
        i += text(k * 280 + 126, 230, t1, "h") + text(k * 280 + 126, 254, t2, "hk")
        if k < 2:
            i += pfeil(k * 280 + 252, 110, k * 280 + 290, 110, "s2")
    return svg("0 0 820 264", i, "Das Gehirn gewöhnt sich an die Droge",
               "Drei Synapsen: vorher mit vielen Rezeptoren und normaler Menge Botenstoff; mit Droge sehr viel Dopamin im Spalt; nach häufigem Konsum sind nur noch wenige Rezeptoren übrig.")


def alkohol_weg():
    i = ('<path class="s f-sand" d="M200 20 C 160 20, 150 60, 160 90 C 120 100, 100 130, 100 200 L 110 420 H 290 L 300 200 C 300 130, 280 100, 240 90 C 250 60, 240 20, 200 20 Z"/>'
         '<path class="s f-rosa-weich" d="M178 150 C 190 120, 250 130, 246 170 C 240 200, 200 196, 190 186 Z"/>'
         '<path class="s f-rosa-tief" d="M120 180 C 140 150, 180 160, 178 186 C 170 210, 130 214, 120 180 Z"/>'
         '<path class="s2 f-rosa" d="M150 230 C 140 250, 260 250, 250 230 C 260 270, 140 260, 150 290 C 140 310, 260 310, 250 300 C 260 330, 150 330, 150 340"/>'
         '<path class="s f-rosa-weich" d="M166 40 C 170 30, 230 30, 234 40 C 230 70, 170 70, 166 40 Z"/>'
         '<path class="s2" fill="none" d="M200 72 V 130"/>')
    i += glas(60, 60, 1.0, "bier") + pfeil(84, 50, 160, 54, "s2 k-bernstein")
    labels = [((180, 54), (330, 40), "Mund"), ((214, 160), (330, 130), "Magen"), ((150, 186), (40, 200), "Leber: baut ab"), ((210, 280), (330, 280), "Dünndarm: Aufnahme ins Blut")]
    for (x1, y1), (x2, y2), t in labels:
        i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2 - 6 if x2 > x1 else x2 + 6} {y2 - 6}"/><circle class="d" cx="{x1}" cy="{y1}" r="2.5"/>' + text(x2, y2, t, "hk", "start" if x2 > x1 else "end")
    i += '<path class="s2 k-rosa" fill="none" stroke-width="3" d="M260 300 C 360 300, 360 120, 300 90"/>' + pfeil(310, 96, 296, 88, "s2 k-rosa") + text(460, 190, "mit dem Blut", "hk") + text(460, 212, "zu allen Organen", "hk") + text(460, 234, "und ins Gehirn", "hk")
    return svg("-70 0 680 430", i, "Der Weg des Alkohols durch den Körper",
               "Alkohol gelangt über Mund und Magen in den Dünndarm und von dort ins Blut. Mit dem Blut erreicht er alle Organe und das Gehirn. Die Leber baut ihn ab.")


def promille_stufen():
    stufen = [(0, 0.2, "f-gruen-weich", ""), (0.2, 0.5, "f-gelb-weich", "Enthemmung"), (0.5, 0.8, "f-gelb", "längere Reaktionszeit"),
              (0.8, 1.0, "f-rosa-weich", "Tunnelblick"), (1.0, 2.0, "f-rosa", "Rausch"), (2.0, 3.0, "f-rosa-tief", "Betäubung"), (3.0, 4.0, "f-blau-tief", "Lebensgefahr")]
    X0, X1 = 30, 790

    def px(v):
        return X0 + v / 4 * (X1 - X0)
    i = ""
    for a, b, f, t in stufen:
        i += f'<rect class="s2 {f}" x="{px(a):.1f}" y="60" width="{px(b) - px(a):.1f}" height="40"/>'
    for k, (a, b, f, t) in enumerate(stufen):
        if t:
            y = 30 if k % 2 else 134
            i += f'<path class="s2" d="M{(px(a) + px(b)) / 2:.1f} {y + (8 if y < 60 else -26)} V {60 if y < 60 else 100}"/>' + text((px(a) + px(b)) / 2, y, t, "hk")
    for v in [0, 0.5, 1, 2, 3, 4]:
        i += f'<path class="s2" d="M{px(v):.1f} 100 v 8"/>' + text(px(v), 170, str(v).replace(".", ",") + " ‰", "hk")
    i += f'<path class="s" fill="none" d="M{X0} 60 H {X1} V 100 H {X0} Z"/>'
    return svg("0 0 820 190", i, "Wirkungen des Alkohols bei Erwachsenen (Richtwerte)",
               "Eine Skala von 0 bis 4 Promille: ab 0,2 Enthemmung, ab 0,5 längere Reaktionszeit, ab 0,8 Tunnelblick, 1 bis 2 Rausch, 2 bis 3 Betäubung, ab 3 Lebensgefahr.")


def zigarette_bild():
    i = zigarette(330, 150, 2.2, 0, False)
    for x, y, t, u, f in [(150, 40, "Nikotin", "macht abhängig", "f-gelb"), (360, 40, "Teer", "verklebt die Lunge, Krebs", "f-sand"), (570, 40, "Kohlenstoffmonoxid", "weniger Sauerstoff im Blut", "f-blau-weich")]:
        i += f'<rect class="s {f}" x="{x - 100}" y="{y - 26}" width="200" height="60" rx="14"/>' + text(x, y, t, "h") + text(x, y + 22, u, "hk")
        i += pfeil(x, y + 36, 200 + (x - 150) * 0.6, 126, "s2")
    i += text(340, 220, "und mehrere tausend weitere Stoffe", "hk")
    return svg("0 0 700 236", i, "Die wichtigsten Schadstoffe im Tabakrauch",
               "Eine Zigarette, darüber drei Kästen: Nikotin macht abhängig; Teer verklebt die Lunge und verursacht Krebs; Kohlenstoffmonoxid sorgt für weniger Sauerstoff im Blut.")


def herkunft():
    i = (blatt_hanf(90, 90, 0.9) + text(90, 170, "Hanf", "h") + text(90, 194, "Cannabis", "hk")
         + koka(250, 96, 1.2) + text(250, 170, "Kokastrauch", "h") + text(250, 194, "Kokain, Crack", "hk")
         + mohn(410, 80, 1.3) + text(410, 170, "Schlafmohn", "h") + text(410, 194, "Heroin", "hk")
         + kolben(580, 96, 1.3) + tablette(626, 120, 10, "f-rosa") + tablette(646, 108, 8, "f-blau") + text(590, 170, "Labor", "h") + text(590, 194, "Ecstasy, Amphetamin", "hk"))
    i += '<path class="s2 gestrichelt" d="M500 20 V 200"/>' + text(250, 230, "aus Pflanzen gewonnen", "hk") + text(590, 230, "synthetisch hergestellt", "hk")
    return svg("0 0 700 240", i, "Woher illegale Drogen stammen", "Cannabis aus Hanf, Kokain und Crack aus dem Kokastrauch, Heroin aus Schlafmohn; Ecstasy und Amphetamin werden im Labor hergestellt.")


def ursachendreieck():
    i = '<path class="s f-papier" d="M330 40 L 560 330 H 100 Z"/>'
    for x, y, t, u, f in [(330, 50, "Person", "Gefühle, Selbstwert, Neugier", "f-gelb"), (110, 320, "Umfeld", "Freunde, Familie, Werbung", "f-blau-weich"), (550, 320, "Suchtmittel", "Wirkung, Verfügbarkeit", "f-rosa")]:
        i += f'<rect class="s {f}" x="{x - 110}" y="{y - 32}" width="220" height="66" rx="16"/>' + text(x, y - 4, t, "h") + text(x, y + 20, u, "hk")
    i += text(330, 230, "Sucht", "h") + text(330, 256, "entsteht im Zusammenspiel", "hk")
    return svg("-10 0 680 370", i, "Das Ursachendreieck der Sucht",
               "Ein Dreieck mit den Ecken Person (Gefühle, Selbstwert, Neugier), Umfeld (Freunde, Familie, Werbung) und Suchtmittel (Wirkung, Verfügbarkeit). In der Mitte steht: Sucht entsteht im Zusammenspiel.")


KREIS = [("Problem", "Stress, Streit, Kummer"), ("Griff zum Suchtmittel", "um sich besser zu fühlen"), ("kurze Erleichterung", "das Problem ist kurz vergessen"),
         ("Problem bleibt", "und wird oft größer"), ("neue Probleme", "Schule, Familie, Geld"), ("mehr Konsum", "Gewöhnung: man braucht mehr")]


def teufelskreis():
    i, cx, cy, r = "", 360, 230, 160
    farben = ["f-blau-weich", "f-rosa-weich", "f-gruen-weich", "f-gelb-weich", "f-gelb", "f-rosa"]
    P = [(cx + math.cos(math.radians(-90 + k * 60)) * r * 1.5, cy + math.sin(math.radians(-90 + k * 60)) * r * 1.12) for k in range(6)]

    def rand(x, y, dx, dy):
        t = min(116 / abs(dx) if dx else 1e9, 40 / abs(dy) if dy else 1e9)
        return x + dx * t, y + dy * t
    for k in range(6):
        (x1, y1), (x2, y2) = P[k], P[(k + 1) % 6]
        dx, dy = x2 - x1, y2 - y1
        sx, sy = rand(x1, y1, dx, dy)
        ex, ey = rand(x2, y2, -dx, -dy)
        i += pfeil(round(sx, 1), round(sy, 1), round(ex, 1), round(ey, 1), "s2")
    for k, (t, u) in enumerate(KREIS):
        x, y = P[k]
        i += f'<rect class="s {farben[k]}" x="{x - 105:.1f}" y="{y - 30:.1f}" width="210" height="60" rx="14"/>' + text(x, y - 4, t, "h") + text(x, y + 20, u, "hk")
    i += text(cx, cy + 8, "Teufelskreis", "h")
    return svg("-30 20 780 430", i, "Der Teufelskreis der Sucht",
               "Ein Kreislauf aus sechs Stationen: Problem, Griff zum Suchtmittel, kurze Erleichterung, das Problem bleibt und wird größer, neue Probleme kommen dazu, mehr Konsum, und wieder von vorn.")


FIGUREN = {
    "stufen": (stufen, "Vom Genuss zur Abhängigkeit: Die Übergänge sind fließend."),
    "synapse": (synapse, "An der Synapse wird das Signal mit Botenstoffen weitergegeben (schematisch)."),
    "toleranz": (toleranz, "Wird die Synapse oft überflutet, baut die Zelle Rezeptoren ab (schematisch)."),
    "alkohol_weg": (alkohol_weg, "Der Weg des Alkohols durch den Körper (vereinfacht)."),
    "promille_stufen": (promille_stufen, "Wirkungen bei Erwachsenen. Bei Jugendlichen wirken schon kleinere Mengen stärker."),
    "zigarette": (zigarette_bild, "Drei der gefährlichsten Stoffe im Tabakrauch."),
    "herkunft": (herkunft, "Herkunft einiger illegaler Drogen."),
    "ursachendreieck": (ursachendreieck, "Sucht hat nie nur eine Ursache."),
    "teufelskreis": (teufelskreis, "Mit jeder Runde wird es schwerer, auszusteigen."),
}


# ---------------------------------------------------------------- Kopfbilder
def reihe4_kopf():
    i = (blob(260, 140, 240, 110, "f-gelb-weich", -3)
         + glas(110, 150, 1.6, "bier") + glas(170, 160, 1.4, "wein") + zigarette(300, 100, 1.2, -12)
         + handy(420, 150, 1.2) + tablette(300, 190, 14, "f-rosa") + tablette(336, 204, 11, "f-blau")
         + '<g transform="translate(260 40)"><circle class="s f-weiss" cx="0" cy="0" r="26"/><path class="s k-rosa" stroke-width="4" d="M-18 -18 L 18 18"/></g>'
         + funkeln(470, 50, 0.9) + funkeln(60, 60, 0.7, "k-rosa"))
    return deko("0 0 520 260", i, "ill kopf-bild")


def kopf(slug):
    hint = blob(300, 112, 280, 96, "f-gelb-weich", 2)
    if slug == "01-genuss-gewoehnung-abhaengigkeit":
        i = hint
        for k, f in enumerate(["f-gruen", "f-gelb", "f-rosa-weich", "f-rosa"]):
            i += f'<rect class="s {f}" x="{110 + k * 100}" y="{170 - k * 36}" width="100" height="{40 + k * 36}" rx="4"/>'
        i += kopf_figur(160, 90, 0.8, "f-sand", "froh") + kopf_figur(470, 22, 0.6, "f-sand", "traurig")
    elif slug == "02-sucht-im-gehirn":
        i = (hint + '<path class="s f-rosa-weich" d="M150 150 C 110 150, 100 80, 150 60 C 170 20, 260 20, 290 50 C 340 40, 380 80, 360 120 C 380 160, 320 180, 290 160 C 260 180, 180 180, 150 150 Z"/>'
             + '<path class="s2" fill="none" d="M170 70 q 20 20 0 40 M 220 50 q -10 30 20 50 q 20 20 0 50 M 290 70 q 30 20 10 50"/>'
             
             + f'<g transform="translate(430 30) scale(.45)">{synapse_bild(5, True, beschriften=False)}</g>' + pfeil(370, 110, 420, 100, "s2"))
    elif slug == "03-alkohol":
        i = (hint + glas(170, 130, 2.2, "bier") + glas(300, 140, 2.0, "wein") + glas(410, 150, 2.0, "schnaps")
             + '<g transform="translate(500 70)"><rect class="s f-weiss" x="-26" y="-30" width="52" height="96" rx="10"/><text class="h" x="0" y="20" text-anchor="middle">‰</text></g>')
    elif slug == "04-rauchen-und-dampfen":
        i = (hint + zigarette(200, 110, 1.8, -8)
             + '<g transform="translate(420 110) rotate(10)"><rect class="s f-blau" x="-16" y="-60" width="32" height="110" rx="12"/><rect class="s f-weiss" x="-8" y="-76" width="16" height="18" rx="4"/><circle class="s2 f-gelb" cx="0" cy="30" r="5"/></g>'
             + '<path class="s2" fill="none" d="M430 20 q 20 10 10 22 q -10 12 10 24"/>')
    elif slug == "05-illegale-drogen":
        i = hint + blatt_hanf(150, 120, 0.8) + koka(270, 110, 1.0) + mohn(370, 90, 1.1) + kolben(470, 120, 1.0) + tablette(510, 160, 10, "f-rosa")
    else:
        i = (hint + '<circle class="s2 f-weiss" cx="300" cy="110" r="70"/>'
             + '<path class="s k-bernstein" fill="none" stroke-width="4" d="M250 70 A 60 60 0 1 1 240 120"/>' + pfeil(246, 110, 240, 124, "s k-bernstein")
             + kopf_figur(130, 80, 0.9, "f-sand", "neutral") + kopf_figur(470, 80, 0.9, "f-blau-weich", "froh")
             + '<path class="s2 f-weiss" d="M500 30 h 70 v 34 h -40 l -14 12 v -12 h -16 z"/>' + text(535, 54, "Hilfe", "hk"))
    return deko("0 0 600 220", i, "ill lt-kopf")


def _s(i):
    return lambda: i


SYMBOLE = {
    "01-genuss-gewoehnung-abhaengigkeit": _s('<rect class="s f-gruen" x="6" y="44" width="14" height="14"/><rect class="s f-gelb" x="20" y="34" width="14" height="24"/><rect class="s f-rosa-weich" x="34" y="22" width="14" height="36"/><rect class="s f-rosa" x="48" y="10" width="12" height="48"/>'),
    "02-sucht-im-gehirn": _s('<path class="s f-rosa-weich" d="M14 40 C 4 40, 4 20, 16 16 C 20 6, 40 6, 46 14 C 58 12, 62 26, 56 34 C 60 44, 46 50, 40 44 C 34 50, 20 50, 14 40 Z"/>'),
    "03-alkohol": _s(glas(32, 36, 0.9, "bier")),
    "04-rauchen-und-dampfen": _s(zigarette(36, 40, 0.55, -20)),
    "05-illegale-drogen": _s(tablette(24, 36, 11, "f-rosa") + tablette(42, 26, 9, "f-blau")),
    "06-teufelskreis-hilfe": _s('<path class="s k-bernstein" fill="none" stroke-width="3" d="M20 18 A 18 18 0 1 1 14 36"/>' + pfeil(16, 30, 14, 38, "s2 k-bernstein")),
    "teufelskreis": _s('<path class="s k-bernstein" fill="none" stroke-width="3" d="M20 18 A 18 18 0 1 1 14 36"/>' + pfeil(16, 30, 14, 38, "s2 k-bernstein")),
    "belohnungssystem": _s('<path class="s f-gelb" d="M14 4 V 14 C 14 22, 6 22, 6 28 H 58 C 58 22, 50 22, 50 14 V 4"/><path class="s f-gelb" d="M6 56 C 10 46, 54 46, 58 56 Z"/>' + "".join(f'<circle class="s2 f-blau-tief" cx="{x}" cy="{y}" r="3"/>' for x, y in [(22, 38), (34, 34), (44, 40), (30, 42)])),
    "promille": _s(glas(22, 36, 0.8, "wein") + '<text class="h" x="46" y="44" text-anchor="middle">‰</text>'),
    "r4-stufen": Z._sym_training, "r4-stoffgebunden": _s(handy(32, 32, 0.6)), "r4-synapse-lueckentext": _s('<path class="s f-gelb" d="M14 4 V 14 C 14 22, 6 22, 6 28 H 58 C 58 22, 50 22, 50 14 V 4"/><path class="s f-gelb" d="M6 56 C 10 46, 54 46, 58 56 Z"/>'),
    "r4-alkohol-wirkung": _s(glas(32, 36, 0.9, "wein")), "r4-teufelskreis": Z._sym_reihenfolge, "r4-mythos": _s('<circle class="s f-gruen" cx="22" cy="32" r="14"/><circle class="s f-rosa" cx="44" cy="32" r="14"/><path class="s2" fill="none" d="M15 32 l 5 5 l 9 -10 M 38 26 l 12 12 M 50 26 l -12 12"/>'),
    "r4-quiz": Z._sym_quiz, "r4-fachbegriffe": Z._sym_training, "r4-drogen-zuordnen": _s(blatt_hanf(32, 40, 0.4)), "r4-schreiben": Z._sym_schreiben,
}

VORWORT = """
  <aside class="wusstest" style="margin-top:2rem">
    <strong>Fakten statt Angstmachen</strong>
    <p>In dieser Reihe geht es darum, wie Suchtmittel wirken und wie Abhängigkeit entsteht. Wenn dich ein Thema persönlich betrifft oder du dir Sorgen um jemanden machst, kannst du mit einer Lehrkraft, der Schulsozialarbeit oder anonym mit der <strong>Nummer gegen Kummer: 116 111</strong> sprechen. Weitere Hilfsangebote findest du in Lerntext 6.</p>
  </aside>"""

for _slug in ["01-genuss-gewoehnung-abhaengigkeit", "02-sucht-im-gehirn", "03-alkohol", "04-rauchen-und-dampfen", "05-illegale-drogen", "06-teufelskreis-hilfe"]:
    Z.EXTRA_KOEPFE[_slug] = (lambda s=_slug: kopf(s))
Z.EXTRA_SYMBOLE.update(SYMBOLE)
