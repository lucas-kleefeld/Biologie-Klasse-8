"""Zeichnungen der Reihe 2. Nutzt die Bausteine aus zeichnungen.py."""
import math
import zeichnungen as Z
from zeichnungen import svg, deko, text, pfeil, blob, funkeln, tropfen


# ---------------------------------------------------------------- kleine Bausteine
def figur(x, y, s=1.0, fill="f-blau", haar=None):
    """einfache, geschlechtsneutrale Person"""
    h = f'<path class="s2 d" d="M{-11} {-44} q 11 -14 22 0 q -4 -6 -11 -6 q -7 0 -11 6 z"/>' if haar else ""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path class="s {fill}" d="M-20 30 C -20 2, -12 -14, 0 -14 C 12 -14, 20 2, 20 30 Z"/>'
            f'<circle class="s f-sand" cx="0" cy="-30" r="13"/>{h}</g>')


def herz(x, y, s=1.0, fill="f-rosa-tief"):
    return f'<path transform="translate({x} {y}) scale({s})" class="s2 {fill}" d="M0 10 C -14 0, -16 -10, -8 -12 C -4 -13, -1 -10, 0 -7 C 1 -10, 4 -13, 8 -12 C 16 -10, 14 0, 0 10 Z"/>'


def eizelle(x, y, r=40, kern=True):
    k = f'<circle class="s2 f-gelb" cx="{x + r * 0.15:.1f}" cy="{y - r * 0.1:.1f}" r="{r * 0.28:.1f}"/><circle class="d" cx="{x + r * 0.18:.1f}" cy="{y - r * 0.12:.1f}" r="{r * 0.07:.1f}"/>' if kern else ""
    kranz = "".join(f'<circle class="s2 f-sand" cx="{x + math.cos(math.radians(a)) * r * 1.12:.1f}" cy="{y + math.sin(math.radians(a)) * r * 1.12:.1f}" r="{r * 0.1:.1f}"/>' for a in range(0, 360, 20))
    return f'{kranz}<circle class="s f-rosa" cx="{x}" cy="{y}" r="{r}"/><circle class="s2" cx="{x}" cy="{y}" r="{r * 0.9:.1f}" fill="none" opacity=".6"/>{k}'


def spermium(x, y, s=1.0, w=0):
    return (f'<g transform="translate({x} {y}) rotate({w}) scale({s})">'
            f'<path class="s2" fill="none" d="M6 0 C 18 -6, 26 6, 38 0 S 56 -6, 66 0"/>'
            f'<ellipse class="s2 f-blau" cx="0" cy="0" rx="7" ry="4.5"/><rect class="s2 f-blau-tief" x="6" y="-1.6" width="6" height="3.2" rx="1.5"/></g>')


def kalender(x, y, s=1.0, markiert=(1, 2, 3, 4, 5), eisprung=14):
    zellen = ""
    for t in range(1, 29):
        cx, cy = ((t - 1) % 7) * 18 - 54, ((t - 1) // 7) * 16 - 8
        fill = "f-rosa-tief" if t in markiert else "f-gelb" if t == eisprung else "f-weiss"
        zellen += f'<rect class="s2 {fill}" x="{cx - 7}" y="{cy - 6}" width="14" height="12" rx="2"/>'
    return (f'<g transform="translate({x} {y}) scale({s})"><rect class="s f-weiss" x="-70" y="-40" width="140" height="102" rx="8"/>'
            f'<rect class="s f-rosa" x="-70" y="-40" width="140" height="22" rx="8"/><path class="s" d="M-70 -18 H 70" fill="none"/>'
            f'<path class="s" d="M-40 -48 v 14 M 40 -48 v 14" fill="none"/>{zellen}</g>')


def regenbogen(x, y, r=60, staerke=8):
    farben = ["#e45d5d", "#f0a540", "#f2d34f", "#6cc07a", "#5aa3dc", "#9a72c9"]
    return "".join(f'<path d="M{x - r + i * staerke} {y} A {r - i * staerke} {r - i * staerke} 0 0 1 {x + r - i * staerke} {y}" fill="none" stroke="{f}" stroke-width="{staerke}" stroke-linecap="butt"/>' for i, f in enumerate(farben))


# ---------------------------------------------------------------- Abbildungen
def hormonsteuerung():
    kasten = lambda x, y, w, titel, unter, fill: (f'<rect class="s {fill}" x="{x - w / 2}" y="{y - 30}" width="{w}" height="60" rx="14"/>'
                                                 + text(x, y - 4, titel, "h") + text(x, y + 18, unter, "hk"))
    i = (kasten(310, 40, 250, "Hypothalamus", "im Gehirn: gibt das Startsignal", "f-blau-weich")
         + pfeil(310, 72, 310, 104, "s2")
         + kasten(310, 136, 250, "Hirnanhangdrüse", "schüttet Hormone ins Blut aus", "f-blau")
         + pfeil(250, 168, 130, 206, "s2", -6) + pfeil(370, 168, 490, 206, "s2", -6)
         + kasten(120, 238, 190, "Eierstöcke", "bilden Östrogen", "f-rosa")
         + kasten(500, 238, 190, "Hoden", "bilden Testosteron", "f-blau-weich")
         + pfeil(120, 270, 120, 300, "s2") + pfeil(500, 270, 500, 300, "s2")
         + text(120, 318, "Brüste, Becken,", "hk") + text(120, 338, "Menstruation", "hk") + text(500, 318, "Stimmbruch,", "hk") + text(500, 338, "Bart, Muskeln", "hk")
         + text(310, 226, "bei allen:", "hk") + text(310, 246, "Wachstum, Haare,", "hk") + text(310, 266, "Haut, Schweiß", "hk"))
    return svg("0 0 620 350", i, "Hormonelle Steuerung der Pubertät",
               "Der Hypothalamus im Gehirn gibt ein Signal an die Hirnanhangdrüse. Diese schüttet Hormone aus, die die Eierstöcke zur Bildung von Östrogen und die Hoden zur Bildung von Testosteron anregen. Die Geschlechtshormone lösen die körperlichen Veränderungen aus.")


def weibliche_organe():
    cx = 380
    gebaermutter = (f'<path class="s f-rosa" d="M{cx - 62} 82 Q {cx} 58 {cx + 62} 82 Q {cx + 78} 148 {cx + 26} 206 L {cx + 20} 232 H {cx - 20} L {cx - 26} 206 Q {cx - 78} 148 {cx - 62} 82 Z"/>'
                    f'<path class="s2 f-rosa-tief" d="M{cx - 40} 92 Q {cx} 84 {cx + 40} 92 Q {cx + 30} 150 {cx + 6} 196 H {cx - 6} Q {cx - 30} 150 {cx - 40} 92 Z"/>'
                    f'<path class="s2 f-rosa-weich" d="M{cx - 28} 98 Q {cx} 92 {cx + 28} 98 Q {cx + 18} 146 {cx + 4} 190 H {cx - 4} Q {cx - 18} 146 {cx - 28} 98 Z"/>')
    scheide = f'<path class="s f-rosa" d="M{cx - 20} 232 L {cx - 24} 318 H {cx + 24} L {cx + 20} 232 Z"/><path class="s2" fill="none" d="M{cx} 236 V 314" opacity=".6"/>'

    def seite(sg):
        ex, ey = cx + sg * 160, 168
        weg = f"M{cx + sg * 58} 88 C {cx + sg * 110} 74, {cx + sg * 170} 78, {cx + sg * 188} 112 S {cx + sg * 192} 150, {cx + sg * 182} 150"
        leiter = f'<path d="{weg}" fill="none" stroke="var(--tinte)" stroke-width="13" stroke-linecap="round"/>'
        leiter2 = f'<path d="{weg}" fill="none" stroke="var(--ill-rosa)" stroke-width="8" stroke-linecap="round"/>'
        fransen = "".join(f'<path class="s2" fill="none" d="M{cx + sg * 182} 150 q {sg * (-6 + k * 5)} 10 {sg * (-10 + k * 7)} 20"/>' for k in range(5))
        stock = (f'<ellipse class="s f-gelb" cx="{ex}" cy="{ey + 22}" rx="34" ry="21"/>'
                 + "".join(f'<circle class="s2 f-weiss" cx="{ex + dx}" cy="{ey + 22 + dy}" r="{r}"/>' for dx, dy, r in [(-14, -4, 5), (2, 6, 4), (14, -6, 7), (-2, -10, 3)]))
        band = f'<path class="s2" fill="none" d="M{ex + (-sg) * 30} {ey + 24} Q {cx + sg * 90} {ey + 40} {cx + sg * 52} 150" stroke-dasharray="4 4"/>'
        return leiter + leiter2 + fransen + band + stock

    i = seite(-1) + seite(1) + gebaermutter + scheide
    beschr = [((cx - 160, 196), (170, 270), "Eierstock", "end"), ((cx - 120, 80), (170, 46), "Eileiter", "end"),
              ((cx - 186, 160), (170, 150), "Eileitertrichter", "end"), ((cx + 40, 110), (600, 52), "Gebärmutter", "start"),
              ((cx + 22, 140), (600, 120), "Gebärmutter-", "start"), ((cx + 18, 226), (600, 220), "Muttermund", "start"),
              ((cx + 22, 290), (600, 300), "Scheide", "start")]
    for (x1, y1), (x2, y2), t, a in beschr:
        i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2 + (8 if a == "end" else -8)} {y2 - 6}"/><circle class="d" cx="{x1}" cy="{y1}" r="3"/>' + text(x2, y2, t, "h", a)
    i += text(600, 144, "schleimhaut", "h", "start")
    return svg("0 0 780 330", i, "Innere weibliche Geschlechtsorgane (Ansicht von vorn, schematisch)",
               "In der Mitte die birnenförmige Gebärmutter mit ihrer Schleimhaut, nach unten der Muttermund und die Scheide. Seitlich führen die beiden Eileiter mit trichterförmigen Enden zu den Eierstöcken, in denen Follikel mit Eizellen liegen.")


def maennliche_organe():
    cx = 310
    blase = f'<ellipse class="s f-gelb-weich" cx="{cx}" cy="78" rx="62" ry="46"/>'
    blaeschen = "".join(f'<path class="s f-sand" d="M{cx + sg * 58} 116 c {sg * 18} -8, {sg * 26} 6, {sg * 20} 16 c {sg * 8} 8, {sg * -6} 18, {sg * -16} 12 c {sg * -10} 4, {sg * -14} -14, {sg * -4} -28 z"/>' for sg in (-1, 1))
    prostata = f'<ellipse class="s f-blau-tief" cx="{cx}" cy="150" rx="36" ry="20"/>'
    roehre = f'<path class="s" fill="none" stroke-width="7" d="M{cx} 122 V 300" style="stroke:var(--ill-gelb)"/><path class="s2" fill="none" d="M{cx - 4} 122 V 300 M {cx + 4} 122 V 300"/>'
    penis = (f'<path class="s f-sand" d="M{cx - 26} 186 V 296 Q {cx - 26} 322 {cx} 322 Q {cx + 26} 322 {cx + 26} 296 V 186 Z"/>'
             f'<rect class="s2 f-rosa-weich" x="{cx - 20}" y="192" width="12" height="96" rx="6"/><rect class="s2 f-rosa-weich" x="{cx + 8}" y="192" width="12" height="96" rx="6"/>')
    sack = f'<path class="s f-sand" d="M{cx - 30} 196 C {cx - 140} 196, {cx - 150} 316, {cx - 70} 316 Q {cx} 306 {cx + 70} 316 C {cx + 150} 316, {cx + 140} 196, {cx + 30} 196 Z"/>'

    def seite(sg):
        hx = cx + sg * 80
        hoden = f'<ellipse class="s f-blau" cx="{hx}" cy="262" rx="28" ry="36"/>'
        neben = f'<path class="s f-blau-tief" d="M{hx + sg * 20} 232 c {sg * 18} 4, {sg * 18} 50, {sg * 6} 64 c {sg * -4} -16, {sg * -4} -46, {sg * -6} -64 z"/>'
        leiter = f'<path class="s" fill="none" stroke-width="5" style="stroke:var(--methylenblau)" d="M{hx + sg * 28} 236 C {hx + sg * 50} 180, {cx + sg * 140} 120, {cx + sg * 110} 50 C {cx + sg * 96} 20, {cx + sg * 70} 30, {cx + sg * 72} 70 C {cx + sg * 74} 110, {cx + sg * 30} 128, {cx + sg * 8} 146"/>'
        return hoden + neben + leiter

    i = sack + seite(-1) + seite(1) + blase + blaeschen + prostata + penis + roehre
    beschr = [((cx - 80, 270), (150, 306), "Hoden", "end"), ((cx - 102, 246), (150, 226), "Nebenhoden", "end"),
              ((cx - 139, 120), (150, 130), "Spermienleiter", "end"), ((cx - 40, 64), (150, 46), "Harnblase", "end"),
              ((cx + 74, 122), (470, 70), "Bläschendrüse", "start"), ((cx + 30, 152), (470, 150), "Prostata", "start"),
              ((cx + 4, 240), (470, 222), "Harn-Samen-Röhre", "start"), ((cx + 16, 272), (470, 276), "Schwellkörper", "start")]
    for (x1, y1), (x2, y2), t, a in beschr:
        i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2 + (8 if a == "end" else -8)} {y2 - 6}"/><circle class="d" cx="{x1}" cy="{y1}" r="3"/>' + text(x2, y2, t, "h", a)
    return svg("0 0 640 330", i, "Männliche Geschlechtsorgane (Ansicht von vorn, schematisch)",
               "Unten im Hodensack liegen die beiden Hoden mit den Nebenhoden. Von dort führen die Spermienleiter in einem Bogen nach oben zur Harnblase und münden unter ihr in die Harn-Samen-Röhre, die von der Prostata umgeben ist. Daneben liegen die Bläschendrüsen. Die Harn-Samen-Röhre führt durch den Penis mit seinen Schwellkörpern nach außen.")


def keimzellen():
    i = eizelle(170, 140, 100) + text(170, 286, "Eizelle: etwa 0,1 mm", "h")
    i += spermium(370, 110, 2.0) + text(450, 160, "Spermienzelle: etwa 0,06 mm", "h")
    i += f'<path class="s2" fill="none" d="M356 96 L 340 60"/>' + text(340, 50, "Kopf mit Zellkern", "hk")
    i += f'<path class="s2" fill="none" d="M388 110 L 410 72"/>' + text(440, 64, "Mittelstück", "hk")
    i += f'<path class="s2" fill="none" d="M470 108 L 500 80"/>' + text(530, 74, "Schwanz", "hk")
    i += text(300, 236, "Zellkern", "hk", "start") + f'<path class="s2" fill="none" d="M296 230 L 190 132"/>'
    i += text(60, 40, "Eihülle", "hk") + f'<path class="s2" fill="none" d="M74 50 L 92 74"/>'
    i += '<path class="s2" d="M430 200 H 550" /><path class="s2" d="M430 194 v 12 M 550 194 v 12"/>' + text(490, 190, "0,06 mm", "hk")
    return svg("0 0 620 300", i, "Eizelle und Spermienzelle im gleichen Maßstab",
               "Die runde Eizelle ist etwa 0,1 Millimeter groß und von einer Hülle aus kleinen Zellen umgeben. Die Spermienzelle ist mit Kopf, Mittelstück und Schwanz nur etwa 0,06 Millimeter lang, ihr Kopf ist viel kleiner als der Zellkern der Eizelle.")


def zyklus_kreis():
    cx, cy, r = 220, 190, 140
    i = ""
    def bogen(t0, t1, fill, rr=r, br=34):
        a0, a1 = math.radians((t0 - 1) / 28 * 360 - 90), math.radians(t1 / 28 * 360 - 90)
        r1, r2 = rr, rr - br
        gross = 1 if (t1 - t0 + 1) > 14 else 0
        p = (f"M{cx + math.cos(a0) * r1:.1f} {cy + math.sin(a0) * r1:.1f} A {r1} {r1} 0 {gross} 1 {cx + math.cos(a1) * r1:.1f} {cy + math.sin(a1) * r1:.1f} "
             f"L {cx + math.cos(a1) * r2:.1f} {cy + math.sin(a1) * r2:.1f} A {r2} {r2} 0 {gross} 0 {cx + math.cos(a0) * r2:.1f} {cy + math.sin(a0) * r2:.1f} Z")
        return f'<path class="s {fill}" d="{p}"/>'
    i += bogen(1, 5, "f-rosa-tief") + bogen(6, 13, "f-gelb") + bogen(14, 14, "f-blau-tief") + bogen(15, 28, "f-blau-weich")
    for t in range(1, 29):
        a = math.radians((t - 0.5) / 28 * 360 - 90)
        if t in (1, 7, 14, 21, 28):
            i += text(round(cx + math.cos(a) * (r + 18), 1), round(cy + math.sin(a) * (r + 18) + 6, 1), str(t), "hk")
    i += text(cx, cy - 6, "28 Tage", "h") + text(cx, cy + 18, "(durchschnittlich)", "hk")
    # innen: kleine Bilder
    i += f'<g transform="translate({cx + 30} {cy - 78})">' + tropfen(0, 0, 0.8, "f-rosa-tief") + tropfen(12, 8, 0.6, "f-rosa-tief") + '</g>'
    i += f'<g transform="translate({cx + 70} {cy + 30})"><circle class="s2 f-gelb" r="14"/><circle class="s2 f-weiss" cx="4" cy="-2" r="6"/></g>'
    i += f'<g transform="translate({cx - 70} {cy + 40})"><circle class="s2 f-gelb" r="14"/></g>'
    leg = [("f-rosa-tief", "Menstruation", "Tag 1–5: Schleimhaut wird abgestoßen"),
           ("f-gelb", "Follikelreifung", "Eizelle reift im Follikel heran"),
           ("f-blau-tief", "Eisprung", "etwa Tag 14: Eizelle wird frei"),
           ("f-blau-weich", "Gelbkörperphase", "Schleimhaut bereit für Einnistung")]
    for k, (f, t, u) in enumerate(leg):
        y = 70 + k * 64
        i += f'<rect class="s {f}" x="410" y="{y - 16}" width="26" height="26" rx="6"/>' + text(446, y, t, "h", "start") + text(446, y + 22, u, "hk", "start")
    return svg("0 0 700 380", i, "Ablauf des Menstruationszyklus als Kreis",
               "Ein Kreis aus 28 Tagen: Tag 1 bis 5 Menstruation, Tag 6 bis 13 Follikelreifung, etwa Tag 14 Eisprung, Tag 15 bis 28 Gelbkörperphase. Danach beginnt der Zyklus von vorn.")


def weg_eizelle():
    # Eileiter als Röhre von links (Eierstock) nach rechts (Gebärmutter)
    weg = "M110 150 C 190 80, 300 80, 400 110 S 520 150, 560 130"
    i = ('<path class="s f-rosa" d="M560 50 Q 650 60 660 140 Q 660 230 610 270 L 570 270 Q 510 210 530 130 Q 540 60 560 50 Z"/>'
         '<path class="s2 f-rosa-tief" d="M566 80 Q 620 80 632 140 Q 630 210 598 246 Q 558 206 556 140 Q 556 90 566 80 Z"/>')
    i += f'<path d="{weg}" fill="none" stroke="var(--tinte)" stroke-width="34" stroke-linecap="round"/><path d="{weg}" fill="none" stroke="var(--ill-rosa)" stroke-width="28" stroke-linecap="round"/>'
    i += '<ellipse class="s f-gelb" cx="70" cy="214" rx="46" ry="28"/><circle class="s2 f-weiss" cx="86" cy="200" r="10"/>'
    i += "".join(f'<path class="s2" fill="none" d="M100 162 q {-10 + k * 5} 10 {-16 + k * 6} 22"/>' for k in range(5))
    stationen = [(108, 152, 1, "1"), (200, 104, 1, "2"), (290, 92, 2, "3"), (380, 104, 4, "4"), (480, 132, 9, "5"), (594, 196, 16, "6")]
    for x, y, n, nr in stationen:
        i += f'<circle class="s2 f-rosa-weich" cx="{x}" cy="{y}" r="13"/>'
        if n == 1:
            i += f'<circle class="s2 f-gelb" cx="{x}" cy="{y}" r="8"/>'
        else:
            for j in range(n):
                a = j / n * math.tau
                d0 = 4 if n <= 4 else 6.5
                i += f'<circle class="s2 f-gelb" cx="{x + math.cos(a) * d0:.1f}" cy="{y + math.sin(a) * d0:.1f}" r="{5 if n == 2 else 4 if n <= 4 else 2.8}"/>'
        ny = y - 32 if nr != "6" else y - 40
        nx = x if nr != "1" else x - 26
        i += f'<circle class="s f-weiss" cx="{nx}" cy="{ny}" r="12"/>' + text(nx, ny + 7, nr, "h")
    i += spermium(170, 128, 0.45, 200) + spermium(160, 112, 0.45, 180)
    i += text(70, 270, "Eierstock", "h") + text(330, 158, "Eileiter", "h") + text(610, 36, "Gebärmutter", "h")
    leg = [("1", "Eisprung", "Tag 0"), ("2", "Befruchtung", "nach Stunden"), ("3", "Zweizellstadium", "Tag 1–2"),
           ("4", "Vierzellstadium", "Tag 2–3"), ("5", "Zellkugel", "Tag 4–5"), ("6", "Einnistung", "Tag 6–7")]
    for k, (nr, t, d) in enumerate(leg):
        x = 30 + (k % 3) * 226
        y = 314 + (k // 3) * 50
        i += f'<circle class="s f-weiss" cx="{x}" cy="{y}" r="12"/>' + text(x, y + 7, nr, "h") + text(x + 20, y + 6, f"{t} ({d})", "hk", "start")
    return svg("0 0 700 380", i, "Weg der Eizelle vom Eisprung bis zur Einnistung",
               "1. Beim Eisprung verlässt die Eizelle den Eierstock und gelangt in den Eileiter. 2. Dort wird sie befruchtet. 3. und 4. Auf dem Weg durch den Eileiter teilt sie sich mehrmals. 5. Nach etwa vier bis fünf Tagen ist eine Zellkugel entstanden. 6. Nach sechs bis sieben Tagen nistet sie sich in der Gebärmutterschleimhaut ein.")


def lebensformen():
    def gruppe(x, titel, figuren):
        g = f'<g transform="translate({x} 0)"><rect class="s2 f-papier" x="4" y="4" width="152" height="166" rx="18"/>'
        for fx, fy, s, f in figuren:
            g += figur(fx, fy, s, f)
        return g + text(80, 160, titel, "hk") + "</g>"
    i = (gruppe(0, "Eltern mit Kind", [(48, 100, 1, "f-blau"), (112, 100, 1, "f-gelb"), (80, 116, 0.6, "f-rosa")])
         + gruppe(162, "Alleinerziehend", [(60, 100, 1, "f-gruen"), (110, 116, 0.6, "f-gelb"), (130, 120, 0.5, "f-blau")])
         + gruppe(324, "Regenbogenfamilie", [(48, 100, 1, "f-rosa"), (112, 100, 1, "f-rosa-tief"), (80, 118, 0.6, "f-blau")])
         + gruppe(486, "Patchwork", [(40, 100, 1, "f-blau"), (100, 100, 1, "f-gruen"), (128, 118, 0.55, "f-gelb"), (70, 120, 0.5, "f-rosa"), (18, 122, 0.45, "f-rosa-tief")])
         + gruppe(648, "Großeltern und Enkel", [(46, 100, 0.95, "f-sand"), (106, 100, 0.95, "f-blau-weich"), (76, 120, 0.55, "f-gelb")])
         + gruppe(810, "allein lebend", [(80, 100, 1, "f-gelb")]))
    i += herz(84, 34, 0.9) + herz(408, 34, 0.9) + herz(570, 34, 0.9) + herz(736, 34, 0.9)
    return svg("0 0 970 176", i, "Verschiedene Lebens- und Familienformen",
               "Sechs gezeichnete Gruppen: Eltern mit Kind, ein alleinerziehender Elternteil mit zwei Kindern, eine Regenbogenfamilie mit zwei Müttern und Kind, eine Patchworkfamilie, Großeltern mit Enkelkind und eine allein lebende Person.")


FIGUREN = {
    "hormonsteuerung": (hormonsteuerung, "Hormone steuern die Pubertät (vereinfacht)."),
    "weibliche_organe": (weibliche_organe, "Die inneren weiblichen Geschlechtsorgane, Ansicht von vorn (schematisch)."),
    "maennliche_organe": (maennliche_organe, "Die männlichen Geschlechtsorgane, Ansicht von vorn (schematisch)."),
    "keimzellen": (keimzellen, "Eizelle und Spermienzelle im gleichen Maßstab."),
    "zyklus_kreis": (zyklus_kreis, "Die Abschnitte eines 28-tägigen Zyklus."),
    "weg_eizelle": (weg_eizelle, "Von der Befruchtung bis zur Einnistung (schematisch, nicht maßstabsgetreu)."),
    "lebensformen": (lebensformen, "Familien und Lebensformen sind vielfältig."),
}


# ---------------------------------------------------------------- Kopfbilder
def reihe2_kopf():
    i = (regenbogen(400, 210, 110, 11)
         + '<path class="s f-rosa" d="M40 40 Q 40 20 60 20 H 190 Q 210 20 210 40 V 100 Q 210 120 190 120 H 100 L 72 146 L 78 120 H 60 Q 40 120 40 100 Z"/>'
         + herz(126, 70, 2.0, "f-rosa-tief")
         + eizelle(110, 220, 34) + spermium(190, 200, 0.9, 200) + spermium(196, 236, 0.9, 165)
         + kalender(430, 70, 0.8)
         + figur(330, 214, 1.05, "f-blau") + figur(470, 214, 1.05, "f-gelb")
         + funkeln(270, 40, 0.8, "k-rosa") + funkeln(500, 140, 0.7, "k-blau"))
    return deko("0 0 520 260", i, "ill kopf-bild")


def kopf(slug):
    if slug == "01-pubertaet":
        i = (blob(300, 112, 280, 96, "f-rosa-weich", 2)
             + '<rect class="s f-sand" x="70" y="20" width="34" height="190" rx="4"/>'
             + "".join(f'<path class="s2" d="M70 {y} h {14 if k % 2 else 22}"/>' for k, y in enumerate(range(30, 210, 14)))
             + figur(160, 176, 0.85, "f-gelb") + figur(230, 168, 1.05, "f-blau") + figur(310, 158, 1.3, "f-gruen")
             + text(160, 214, "10", "hk") + text(230, 214, "12", "hk") + text(310, 214, "14 Jahre", "hk")
             + '<g transform="translate(450 120)"><rect class="s f-blau-weich" x="-24" y="-40" width="48" height="90" rx="12"/><rect class="s f-weiss" x="-14" y="-58" width="28" height="20" rx="5"/><path class="s2" d="M-14 -6 H 14 M -14 6 H 14" fill="none"/></g>'
             + '<path class="s f-weiss" d="M500 50 Q 500 34 516 34 H 570 Q 586 34 586 50 V 76 Q 586 92 570 92 H 530 L 516 108 L 518 92 H 516 Q 500 92 500 76 Z"/>'
             + text(543, 70, "Hallo?!", "hk") + funkeln(390, 40, 0.8))
    elif slug == "02-geschlechtsorgane":
        i = (blob(300, 112, 280, 96, "f-gelb-weich", -2) + eizelle(220, 112, 62)
             + spermium(360, 70, 1.2, 190) + spermium(380, 120, 1.2, 175) + spermium(350, 170, 1.2, 160) + spermium(470, 96, 1.1, 182) + spermium(480, 150, 1.0, 168)
             + funkeln(90, 40, 0.8, "k-rosa") + funkeln(560, 190, 0.7, "k-blau"))
    elif slug == "03-zyklus":
        kurve = lambda pts, k: '<path class="s ' + k + '" stroke-width="3.5" fill="none" d="M' + " L ".join(f"{x} {y}" for x, y in pts) + '"/>'
        i = (blob(300, 112, 280, 96, "f-blau-weich", 2) + kalender(150, 104, 1.15)
             + '<rect class="s f-weiss" x="300" y="40" width="250" height="150" rx="12"/>'
             + kurve([(316, 160), (360, 150), (400, 80), (420, 70), (440, 140), (480, 110), (520, 150), (536, 160)], "k-rosa")
             + kurve([(316, 168), (420, 168), (440, 150), (480, 70), (520, 120), (536, 168)], "k-blau")
             + '<path class="s2" d="M420 46 V 184" stroke-dasharray="4 5"/>' + text(420, 210, "Eisprung", "hk")
             + funkeln(570, 30, 0.7))
    elif slug == "04-schwangerschaft":
        i = (blob(300, 112, 280, 96, "f-rosa-weich", -3)
             + '<path class="s" fill="#2b3135" d="M130 200 L 60 70 A 150 150 0 0 1 300 70 L 230 200 Z"/>'
             + '<path d="M150 150 C 130 120, 150 92, 178 96 C 200 98, 214 120, 206 140 C 220 150, 214 172, 196 170 C 182 176, 160 172, 150 150 Z" fill="#c9ced2" opacity=".85"/>'
             + '<circle cx="172" cy="118" r="20" fill="#dfe3e6" opacity=".9"/>'
             + '<g transform="translate(400 120)"><rect class="s f-weiss" x="-26" y="-50" width="52" height="96" rx="16"/><rect class="s f-blau-weich" x="-26" y="-6" width="52" height="52" rx="12"/><path class="s f-sand" d="M-14 -50 Q 0 -78 14 -50 Z"/><path class="s2" d="M-16 -30 H 16 M -16 -18 H 16"/></g>'
             + '<g transform="translate(510 150)"><path class="s f-sand" d="M-16 -36 C -30 -20, -26 20, -6 30 C 6 34, 16 20, 12 0 C 10 -20, 6 -40, -16 -36 Z"/>'
             + "".join(f'<circle class="s2 f-sand" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(-20, -48, 6), (-8, -54, 5), (4, -54, 4.5), (14, -48, 4), (20, -40, 3.5)]) + '</g>'
             + herz(560, 60, 1.3) + funkeln(330, 40, 0.8))
    elif slug == "05-verhuetung":
        i = (blob(300, 112, 280, 96, "f-gruen-weich", 2)
             + '<g transform="translate(170 116) rotate(-8)"><rect class="s f-blau" x="-70" y="-70" width="140" height="140" rx="10"/><path class="s2" d="M-70 -54 H 70 M -70 54 H 70 M -54 -70 V 70 M 54 -70 V 70" stroke-dasharray="3 5"/><circle class="s f-blau-weich" r="38"/><circle class="s2" r="28" fill="none"/></g>'
             + '<g transform="translate(400 112) rotate(6)"><rect class="s f-weiss" x="-90" y="-56" width="180" height="112" rx="14"/>'
             + "".join(f'<circle class="s2 {"f-weiss" if (c + r) % 5 == 0 else "f-rosa"}" cx="{-66 + c * 26}" cy="{-30 + r * 30}" r="9"/>' for r in range(3) for c in range(7)) + '</g>'
             + '<path class="s f-gelb" d="M548 40 L 584 52 C 586 96, 572 124, 548 140 C 524 124, 510 96, 512 52 Z"/><path class="s2 k-gruen" fill="none" d="M534 88 l 10 10 l 20 -24"/>')
    else:
        i = (blob(300, 112, 280, 96, "f-gelb-weich", -2) + regenbogen(300, 196, 150, 13)
             + figur(230, 168, 1.2, "f-blau") + figur(370, 168, 1.2, "f-rosa")
             + herz(300, 64, 2.2) + herz(150, 60, 1.1, "f-rosa") + herz(470, 70, 1.3, "f-rosa")
             + funkeln(90, 150, 0.8, "k-blau") + funkeln(530, 160, 0.8, "k-rosa"))
    return deko("0 0 600 220", i, "ill lt-kopf")


# ---------------------------------------------------------------- Symbole
def _s(i):
    return lambda: i


SYMBOLE = {
    "01-pubertaet": _s('<rect class="s f-sand" x="12" y="8" width="12" height="48" rx="3"/><path class="s2" d="M12 16 h6 M12 24 h8 M12 32 h6 M12 40 h8 M12 48 h6"/>' + figur(42, 40, 0.7, "f-gruen")),
    "02-geschlechtsorgane": _s(eizelle(26, 32, 14, False) + spermium(46, 28, 0.35, 190)),
    "03-zyklus": _s(kalender(32, 32, 0.38)),
    "04-schwangerschaft": _s('<path class="s f-sand" d="M24 46 C 10 34, 16 12, 32 14 C 46 16, 52 32, 44 42 C 52 50, 44 58, 34 54 C 30 56, 26 52, 24 46 Z"/><circle class="s2 f-sand" cx="30" cy="22" r="8"/>'),
    "05-verhuetung": _s('<path class="s f-gelb" d="M32 6 L 54 14 C 54 38, 46 50, 32 58 C 18 50, 10 38, 10 14 Z"/><path class="s2 k-gruen" fill="none" d="M22 32 l 7 7 l 14 -16"/>'),
    "06-freundschaft-liebe-vielfalt": _s(regenbogen(32, 44, 26, 4) + herz(32, 24, 1.2)),
    "zyklus": _s('<circle class="s f-weiss" cx="32" cy="32" r="24"/><path class="s f-rosa-tief" d="M32 8 A 24 24 0 0 1 49 15 L 41 23 A 12 12 0 0 0 32 20 Z"/><path class="s2 k-rosa" fill="none" stroke-width="2.5" d="M14 40 Q 26 20 32 34 T 50 28"/>'),
    "schwangerschaft": _s('<path class="s f-rosa-weich" d="M10 52 Q 10 10 32 10 Q 54 10 54 52 Z"/><path class="s f-sand" d="M26 44 C 16 36, 20 20, 32 22 C 42 24, 44 34, 38 40 C 42 46, 36 50, 30 48 Z"/>'),
    "verhuetung": _s("".join(f'<circle class="s2 {"f-rosa-tief" if k < 3 else "f-weiss"}" cx="{12 + (k % 5) * 10}" cy="{14 + (k // 5) * 12}" r="4"/>' for k in range(20))),
    "r2-pubertaet-sortieren": _s('<path class="s f-rosa" d="M8 30 H 28 V 54 H 8 Z"/><path class="s f-blau" d="M36 30 H 56 V 54 H 36 Z"/>' + figur(32, 20, 0.4, "f-gelb")),
    "r2-organe-zuordnen": Z._sym_training,
    "r2-zyklus-lueckentext": _s(kalender(32, 32, 0.38)),
    "r2-weg-eizelle": Z._sym_reihenfolge,
    "r2-mythos-fakt": _s('<path class="s f-gelb" d="M10 14 Q 10 8 16 8 H 48 Q 54 8 54 14 V 38 Q 54 44 48 44 H 28 L 18 54 L 20 44 H 16 Q 10 44 10 38 Z"/><text class="h" x="32" y="34" text-anchor="middle" style="font-size:18px">?!</text>'),
    "r2-verhuetung-zuordnen": _s('<path class="s f-gelb" d="M32 6 L 54 14 C 54 38, 46 50, 32 58 C 18 50, 10 38, 10 14 Z"/>'),
    "r2-quiz": Z._sym_quiz,
    "r2-fachbegriffe": Z._sym_training,
    "r2-wissenscheck": Z._sym_training,
    "r2-schreiben": Z._sym_schreiben,
}

for _slug in ["01-pubertaet", "02-geschlechtsorgane", "03-zyklus", "04-schwangerschaft", "05-verhuetung", "06-freundschaft-liebe-vielfalt"]:
    Z.EXTRA_KOEPFE[_slug] = (lambda s=_slug: kopf(s))
Z.EXTRA_SYMBOLE.update(SYMBOLE)

VORWORT = """
  <aside class="wusstest r2-hinweis" style="margin-top:2rem">
    <strong>Fragen sind erwünscht</strong>
    <p>In dieser Reihe geht es um Themen, die manchen Menschen peinlich sind. Dabei ist jede Frage berechtigt. Du kannst sie im Unterricht stellen, deiner Lehrkraft oder einer anderen Vertrauensperson. Anonyme Hilfe gibt es bei der <strong>Nummer gegen Kummer: 116 111</strong>.</p>
  </aside>"""
