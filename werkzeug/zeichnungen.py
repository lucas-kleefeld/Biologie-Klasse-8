"""Eigene Zeichnungen im Skizzenbuch-Stil. Farben kommen über CSS-Klassen (siehe style.css, Abschnitt Zeichnungen),
damit sie im hellen und dunklen Modus funktionieren.

Klassen:  s = Tintenlinie, s2 = dünne Linie, d = Tintenfläche
          f-blau, f-rosa, f-gruen, f-gelb, f-sand, f-weiss, f-papier = Füllfarben
          k-blau, k-rosa, k-gruen, k-bernstein = farbige Linien
          h = Handschrift-Beschriftung, hk = kleine Handschrift
"""
import math


def svg(viewbox, inhalt, titel, beschreibung="", klasse="ill"):
    import hashlib
    vid = "i" + hashlib.md5(titel.encode()).hexdigest()[:8]
    desc = f'<desc id="{vid}d">{beschreibung}</desc>' if beschreibung else ""
    lab = f'{vid}t {vid}d' if beschreibung else f'{vid}t'
    return (f'<svg class="{klasse}" viewBox="{viewbox}" role="img" aria-labelledby="{lab}" xmlns="http://www.w3.org/2000/svg">'
            f'<title id="{vid}t">{titel}</title>{desc}{inhalt}</svg>')


def deko(viewbox, inhalt, klasse="ill"):
    return f'<svg class="{klasse}" viewBox="{viewbox}" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">{inhalt}</svg>'


# ---------------------------------------------------------------- Bausteine
def virus(x, y, s=1.0, fill="f-rosa", drehung=0):
    pts = " ".join(f"{math.cos(math.radians(a + drehung)) * 14 * s:.1f},{math.sin(math.radians(a + drehung)) * 14 * s:.1f}" for a in range(0, 360, 60))
    stacheln = ""
    for a in range(30, 390, 60):
        r1, r2 = 12.5 * s, 21 * s
        ca, sa = math.cos(math.radians(a + drehung)), math.sin(math.radians(a + drehung))
        stacheln += f'<line class="s" x1="{ca * r1:.1f}" y1="{sa * r1:.1f}" x2="{ca * r2:.1f}" y2="{sa * r2:.1f}"/><circle class="d" cx="{ca * (r2 + 2.5 * s):.1f}" cy="{sa * (r2 + 2.5 * s):.1f}" r="{3 * s:.1f}"/>'
    return (f'<g transform="translate({x} {y})">{stacheln}<polygon class="s {fill}" points="{pts}"/>'
            f'<path class="s2 k-rosa" d="M{-5 * s:.1f} {-3 * s:.1f} q{4 * s:.1f} {-5 * s:.1f} {6 * s:.1f} 0 t{4 * s:.1f} {5 * s:.1f}" fill="none"/></g>')


def antikoerper(x, y, s=1.0, drehung=0, klasse="k-blau"):
    return (f'<g transform="translate({x} {y}) rotate({drehung}) scale({s})">'
            f'<path class="s {klasse}" stroke-width="4" d="M0 22 V4 M0 4 L-10 -9 M0 4 L10 -9" fill="none"/>'
            f'<path class="s {klasse}" stroke-width="3" d="M-15 -6 l5 -6 l4 4 M15 -6 l-5 -6 l-4 4" fill="none"/></g>')


def stab(x, y, laenge=46, dicke=18, drehung=0, fill="f-blau", geissel=True):
    r = dicke / 2
    g = (f'<path class="s2" d="M{laenge / 2} 0 c 8 -6, 14 6, 22 0 s 12 -6, 18 0" fill="none"/>' if geissel else "")
    return (f'<g transform="translate({x} {y}) rotate({drehung})">{g}'
            f'<rect class="s {fill}" x="{-laenge / 2}" y="{-r}" width="{laenge}" height="{dicke}" rx="{r}"/>'
            f'<path class="s2 k-rosa" d="M{-laenge / 4} 1 q 6 -6 10 0 t 10 0" fill="none"/></g>')


def zelle(x, y, rx=34, ry=26, fill="f-gruen", kern=True, drehung=0):
    # leicht unregelmäßiger Umriss
    p = []
    for i in range(12):
        a = math.radians(i * 30)
        f = 1 + 0.06 * math.sin(i * 2.3)
        p.append((math.cos(a) * rx * f, math.sin(a) * ry * f))
    d = f"M{p[0][0]:.1f} {p[0][1]:.1f} " + " ".join(
        f"Q{(p[i][0] + p[(i + 1) % 12][0]) / 2 * 1.06:.1f} {(p[i][1] + p[(i + 1) % 12][1]) / 2 * 1.06:.1f} {p[(i + 1) % 12][0]:.1f} {p[(i + 1) % 12][1]:.1f}"
        for i in range(12)) + "Z"
    k = f'<circle class="s f-weiss" cx="{rx * 0.15:.1f}" cy="{-ry * 0.1:.1f}" r="{min(rx, ry) * 0.32:.1f}"/><circle class="d" cx="{rx * 0.2:.1f}" cy="{-ry * 0.12:.1f}" r="{min(rx, ry) * 0.1:.1f}"/>' if kern else ""
    return f'<g transform="translate({x} {y}) rotate({drehung})"><path class="s {fill}" d="{d}"/>{k}</g>'


def fresszelle(x, y, s=1.0, fill="f-sand"):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path class="s {fill}" d="M-40 -6 C -44 -30, -14 -40, 4 -32 C 20 -44, 46 -30, 40 -8 C 56 4, 40 34, 14 30 C 0 44, -30 40, -34 20 C -52 14, -52 2, -40 -6 Z"/>'
            f'<circle class="s f-weiss" cx="-8" cy="4" r="11"/><circle class="d" cx="-6" cy="4" r="3.5"/></g>')


def pollen(x, y, r=14, fill="f-gelb"):
    sp = ""
    for i in range(14):
        a = math.radians(i * 360 / 14)
        sp += f'<line class="s2" x1="{math.cos(a) * r:.1f}" y1="{math.sin(a) * r:.1f}" x2="{math.cos(a) * (r + 6):.1f}" y2="{math.sin(a) * (r + 6):.1f}"/>'
    return f'<g transform="translate({x} {y})">{sp}<circle class="s {fill}" r="{r}"/><circle class="d" cx="{-r * 0.3:.1f}" cy="{-r * 0.2:.1f}" r="2"/><circle class="d" cx="{r * 0.3:.1f}" cy="{r * 0.25:.1f}" r="2"/></g>'


def tropfen(x, y, s=1.0, fill="f-blau"):
    return f'<path transform="translate({x} {y}) scale({s})" class="s {fill}" d="M0 -14 C 6 -5, 10 0, 10 5 A 10 10 0 0 1 -10 5 C -10 0, -6 -5, 0 -14 Z"/>'


def funkeln(x, y, s=1.0, klasse="k-bernstein"):
    return f'<path transform="translate({x} {y}) scale({s})" class="s2 {klasse}" d="M0 -8 V8 M-8 0 H8 M-5 -5 L5 5 M5 -5 L-5 5" fill="none"/>'


def pfeil(x1, y1, x2, y2, klasse="s2", bogen=0):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - bogen
    ang = math.atan2(y2 - my, x2 - mx)
    a1 = (x2 - 9 * math.cos(ang - 0.45), y2 - 9 * math.sin(ang - 0.45))
    a2 = (x2 - 9 * math.cos(ang + 0.45), y2 - 9 * math.sin(ang + 0.45))
    return (f'<path class="{klasse}" fill="none" d="M{x1} {y1} Q{mx} {my} {x2} {y2}"/>'
            f'<path class="{klasse}" fill="none" d="M{a1[0]:.1f} {a1[1]:.1f} L{x2} {y2} L{a2[0]:.1f} {a2[1]:.1f}"/>')


def text(x, y, t, klasse="h", anker="middle", drehung=0):
    rot = f' transform="rotate({drehung} {x} {y})"' if drehung else ""
    return f'<text class="{klasse}" x="{x}" y="{y}" text-anchor="{anker}"{rot}>{t}</text>'


def petrischale(x, y, r=60, inhalt=""):
    return (f'<g transform="translate({x} {y})"><ellipse class="s f-weiss" cx="0" cy="6" rx="{r}" ry="{r * 0.42:.1f}"/>'
            f'<ellipse class="s f-gelb" cx="0" cy="0" rx="{r}" ry="{r * 0.42:.1f}"/>'
            f'<ellipse class="s2" cx="0" cy="0" rx="{r - 6}" ry="{r * 0.42 - 4:.1f}" fill="none" opacity=".5"/>{inhalt}</g>')


def blob(x, y, rx, ry, fill, drehung=0):
    return (f'<path transform="translate({x} {y}) rotate({drehung})" class="{fill}" '
            f'd="M{-rx} 0 C {-rx} {-ry * 0.9:.1f}, {-rx * 0.3:.1f} {-ry}, {rx * 0.2:.1f} {-ry} C {rx * 0.9:.1f} {-ry}, {rx} {-ry * 0.4:.1f}, {rx} {ry * 0.1:.1f} '
            f'C {rx} {ry * 0.8:.1f}, {rx * 0.4:.1f} {ry}, {-rx * 0.1:.1f} {ry} C {-rx * 0.8:.1f} {ry}, {-rx} {ry * 0.6:.1f}, {-rx} 0 Z"/>')


# ---------------------------------------------------------------- Startseite
def mikroskop(x, y, s=1.0):
    return f'''<g transform="translate({x} {y}) scale({s})">
  <path class="s f-blau" d="M-70 120 Q -72 104 -56 102 H 60 Q 74 104 72 120 Z"/>
  <path class="s f-weiss" d="M30 102 C 34 70, 56 52, 52 18 C 50 0, 38 -14, 22 -18 L 14 -2 C 26 2, 34 10, 32 26 C 30 50, 10 70, 8 102 Z"/>
  <rect class="s f-sand" x="-52" y="40" width="96" height="12" rx="4"/>
  <path class="s2" d="M-40 40 v-6 M -10 40 v -6" />
  <g transform="rotate(-24 0 -10)">
    <rect class="s f-weiss" x="8" y="-34" width="24" height="30" rx="5"/>
    <rect class="s f-blau" x="-14" y="-90" width="28" height="80" rx="6"/>
    <rect class="s f-sand" x="-18" y="-104" width="36" height="18" rx="5"/>
    <rect class="s f-weiss" x="-9" y="-10" width="18" height="18" rx="3"/>
    <rect class="s f-sand" x="-5" y="8" width="10" height="12" rx="2"/>
  </g>
  <circle class="s f-sand" cx="40" cy="58" r="11"/><circle class="s f-weiss" cx="40" cy="58" r="4"/>
  <circle class="s f-sand" cx="44" cy="82" r="7"/>
  <ellipse class="s f-gelb" cx="-6" cy="84" rx="16" ry="6"/>
  <path class="s2 k-bernstein" d="M-6 78 L -6 52" stroke-dasharray="3 4"/>
</g>'''


def hero_bild():
    lupe_inhalt = (blob(0, 0, 112, 104, "f-papier") +
                   zelle(-40, -38, 40, 30, "f-gruen") + zelle(38, 46, 32, 24, "f-gruen", drehung=20) +
                   stab(30, -48, 42, 15, 25, "f-blau", geissel=False) + stab(-50, 40, 38, 14, -15, "f-blau", geissel=False) +
                   stab(-6, 62, 34, 13, 70, "f-blau", geissel=False) +
                   virus(58, -6, 0.8) + virus(-74, -2, 0.6, drehung=15) +
                   antikoerper(78, -26, 0.8, -60) + antikoerper(40, 8, 0.8, 120))
    inhalt = f'''
  {blob(330, 170, 190, 160, "f-blau-weich", 8)}
  {mikroskop(110, 168, 1.05)}
  <path class="s2" stroke-dasharray="5 6" fill="none" d="M128 70 L 262 66 M 134 92 L 268 262"/>
  <g transform="translate(360 168)">
    <defs><clipPath id="lupeclip"><circle r="114"/></clipPath></defs>
    <circle class="f-weiss" r="120"/>
    <g clip-path="url(#lupeclip)">{lupe_inhalt}</g>
    <circle class="s" r="120" stroke-width="5" fill="none"/>
    <circle class="s2 k-blau" r="128" fill="none" stroke-dasharray="2 8"/>
  </g>
  {text(470, 316, "1000-fach vergrößert", "h", "middle", -4)}
  {pfeil(452, 296, 430, 270)}
  {funkeln(500, 40)}{funkeln(250, 30, 0.7)}{funkeln(30, 280, 0.8, "k-blau")}
  {pollen(512, 112, 9)}{tropfen(40, 40, 0.9)}
'''
    return deko("0 0 540 340", inhalt, "ill hero-bild")


def karte_bild(nr):
    if nr == 1:
        i = (fresszelle(70, 74, 0.95) + virus(150, 50, 0.85) + virus(186, 92, 0.7, drehung=20) + virus(128, 108, 0.6, drehung=10) +
             antikoerper(168, 22, 0.8, 140) + antikoerper(208, 60, 0.8, -110) + funkeln(30, 24, 0.6))
    elif nr == 2:
        i = ('<path class="s f-rosa" d="M26 30 Q 26 16 40 16 H 116 Q 130 16 130 30 V 66 Q 130 80 116 80 H 64 L 46 98 L 50 80 H 40 Q 26 80 26 66 Z"/>'
             '<path class="s k-rosa" stroke-width="3" fill="var(--eosin)" d="M78 64 C 60 52, 58 36, 70 34 C 76 33, 78 38, 78 40 C 78 38, 80 33, 86 34 C 98 36, 96 52, 78 64 Z"/>'
             '<path class="s f-blau" d="M110 54 Q 110 42 122 42 H 204 Q 216 42 216 54 V 92 Q 216 104 204 104 H 194 L 198 122 L 178 104 H 122 Q 110 104 110 92 Z"/>'
             '<circle class="d" cx="142" cy="73" r="4"/><circle class="d" cx="163" cy="73" r="4"/><circle class="d" cx="184" cy="73" r="4"/>'
             + funkeln(220, 24, 0.7) + funkeln(20, 112, 0.6, "k-rosa"))
    elif nr == 3:
        i = ('<path class="s f-blau" d="M0 84 C 30 74, 50 94, 80 84 S 130 74, 160 84 S 210 94, 240 84 V 140 H 0 Z"/>'
             '<path class="s2 k-blau" fill="none" d="M20 108 c 10 -6, 20 6, 30 0 M 150 122 c 10 -6, 20 6, 30 0 M 90 128 c 8 -5, 16 5, 24 0"/>'
             '<g transform="translate(120 106)"><path class="s f-gelb" d="M-26 0 C -14 -16, 14 -16, 24 0 C 14 16, -14 16, -26 0 Z"/><path class="s f-gelb" d="M24 0 L 40 -12 L 38 12 Z"/><circle class="d" cx="-14" cy="-3" r="2.6"/><path class="s2" fill="none" d="M-4 -10 q 6 10 0 20"/></g>'
             '<path class="s k-gruen" stroke-width="3" fill="none" d="M196 86 C 194 60, 200 40, 198 18 M 210 88 C 212 64, 216 44, 222 30 M 184 88 C 180 70, 176 58, 170 46"/>'
             '<rect class="s f-sand" x="193" y="10" width="10" height="26" rx="5"/><rect class="s f-sand" x="217" y="22" width="9" height="22" rx="4.5"/>'
             '<circle class="s f-gelb" cx="44" cy="34" r="16"/>' + "".join(f'<line class="s2 k-bernstein" x1="{44 + math.cos(math.radians(a)) * 22:.1f}" y1="{34 + math.sin(math.radians(a)) * 22:.1f}" x2="{44 + math.cos(math.radians(a)) * 29:.1f}" y2="{34 + math.sin(math.radians(a)) * 29:.1f}"/>' for a in range(0, 360, 45)))
    else:
        i = ('<path class="s f-sand" d="M70 96 C 40 96, 34 66, 50 52 C 44 30, 70 18, 88 26 C 100 10, 130 12, 138 28 C 160 22, 180 40, 172 60 C 186 74, 174 100, 150 96 C 140 108, 112 110, 104 100 C 94 108, 76 106, 70 96 Z"/>'
             '<path class="s2" fill="none" d="M88 26 C 92 44, 80 50, 92 62 M 120 22 C 114 40, 130 48, 120 66 M 150 46 C 136 54, 150 70, 140 82 M 70 60 C 80 70, 70 80, 86 88"/>'
             '<path class="s k-bernstein" stroke-width="3" fill="none" d="M196 40 A 34 34 0 1 1 168 116"/>'
             '<path class="s k-bernstein" stroke-width="3" fill="none" d="M160 108 L 168 116 L 158 122"/>'
             '<path class="s k-bernstein" stroke-width="3" fill="none" d="M44 112 A 34 34 0 0 1 30 54"/>'
             '<path class="s k-bernstein" stroke-width="3" fill="none" d="M22 62 L 30 54 L 36 64"/>' + funkeln(212, 20, 0.6))
    return deko("0 0 240 140", i, "ill karte-bild")


# ---------------------------------------------------------------- Reihe 1 Kopf
def reihe1_kopf():
    i = ('<path class="s f-sand" d="M0 40 C 60 30, 120 50, 180 40 S 300 30, 360 42 S 470 50, 520 40 V 70 H 0 Z"/>'
         '<path class="f-papier" d="M240 36 L 258 72 L 276 38 Z"/>'
         + text(30, 30, "Haut", "hk", "start")
         + virus(258, 96, 0.8) + virus(232, 134, 0.7, drehung=20) + virus(292, 128, 0.75, drehung=12)
         + fresszelle(140, 170, 1.1) + virus(132, 172, 0.45)
         + '<circle class="s f-blau" cx="380" cy="160" r="30"/>' + text(380, 167, "T", "h")
         + '<circle class="s f-blau-tief" cx="450" cy="210" r="26"/>' + text(450, 217, "B", "h")
         + antikoerper(432, 104, 0.9, -150) + antikoerper(470, 140, 0.9, -110) + antikoerper(340, 222, 0.9, 40) + antikoerper(498, 196, 0.8, -70)
         + text(140, 236, "Fresszelle", "hk") + text(362, 118, "Helferzelle", "hk") + text(450, 256, "Plasmazelle", "hk")
         + pfeil(184, 150, 346, 156, "s2 gestrichelt", 20) + pfeil(398, 186, 430, 196, "s2", 0)
         + funkeln(60, 110, 0.8) + funkeln(500, 90, 0.7, "k-blau"))
    return deko("0 0 520 270", i, "ill kopf-bild")


# ---------------------------------------------------------------- Lerntext-Köpfe
def lt_kopf(slug):
    if slug in EXTRA_KOEPFE:
        return EXTRA_KOEPFE[slug]()
    if slug == "01-gesund-oder-krank":
        i = (blob(300, 110, 270, 92, "f-rosa-weich", -2)
             # Thermometer
             + '<g transform="translate(90 112) rotate(-18)"><rect class="s f-weiss" x="-11" y="-76" width="22" height="104" rx="11"/><circle class="s f-weiss" cx="0" cy="40" r="20"/>'
               '<rect class="f-rosa-tief" x="-5" y="-30" width="10" height="66"/><circle class="f-rosa-tief" cx="0" cy="40" r="13"/>'
               '<path class="s2" d="M5 -60 h6 M5 -48 h6 M5 -36 h6 M5 -24 h6 M5 -12 h6 M5 0 h6"/></g>'
             + text(140, 40, "39,2 °C", "h", "start", -6)
             # Niesen: Tröpfchenwolke
             + '<path class="s f-weiss" d="M220 120 C 214 94, 240 80, 258 92 C 266 74, 300 74, 304 96 C 326 94, 334 120, 316 130 C 322 150, 290 158, 280 146 C 262 160, 228 152, 232 136 C 214 136, 210 124, 220 120 Z"/>'
             + "".join(tropfen(x, y, s, "f-blau") for x, y, s in [(346, 96, 0.55), (362, 124, 0.45), (340, 150, 0.5), (378, 104, 0.35), (384, 146, 0.35)])
             + virus(258, 118, 0.55) + virus(292, 128, 0.5, drehung=20)
             + text(272, 186, "Hatschi!", "h", "middle", 4)
             # Seife und Blasen
             + '<rect class="s f-gelb" x="440" y="118" width="84" height="44" rx="14"/><path class="s2" fill="none" d="M454 130 q 10 -6 20 0"/>'
             + "".join(f'<circle class="s2 f-weiss" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(470, 100, 10), (494, 82, 14), (520, 104, 8), (456, 74, 7), (530, 66, 9)])
             + funkeln(560, 120, 0.7))
    elif slug == "02-bakterien-und-viren":
        i = (blob(300, 112, 270, 94, "f-blau-weich", 3)
             + petrischale(120, 120, 78, '<circle class="s f-weiss" cx="-30" cy="-6" r="10"/><circle class="s f-weiss" cx="12" cy="8" r="13"/><circle class="s f-weiss" cx="40" cy="-10" r="7"/><circle class="s f-weiss" cx="-8" cy="-18" r="6"/><circle class="s f-weiss" cx="-46" cy="12" r="5"/>')
             + text(120, 192, "Bakterienkolonien", "hk")
             # Zweiteilung
             + stab(270, 92, 54, 20, 0, "f-blau", geissel=False) + pfeil(304, 94, 342, 70, "s2", 6) + pfeil(304, 100, 342, 128, "s2", -6)
             + stab(372, 62, 44, 18, -8, "f-blau", geissel=False) + stab(372, 134, 44, 18, 8, "f-blau", geissel=False)
             + text(330, 178, "Zweiteilung", "hk")
             # Virus groß
             + virus(490, 98, 1.5) + text(490, 172, "Virus", "hk")
             + funkeln(560, 40, 0.7) + funkeln(236, 38, 0.6, "k-blau"))
    elif slug == "03-das-immunsystem":
        i = (blob(300, 110, 270, 94, "f-gruen-weich", -3)
             + '<path class="s f-blau" d="M300 26 L 362 46 C 364 112, 344 160, 300 186 C 256 160, 236 112, 238 46 Z"/>'
             + '<path class="s2 f-weiss" d="M300 42 L 348 58 C 348 110, 332 146, 300 168 C 268 146, 252 110, 252 58 Z"/>'
             + antikoerper(300, 104, 1.6)
             + virus(160, 70, 0.8) + virus(130, 140, 0.7, drehung=20) + virus(440, 64, 0.75) + virus(470, 140, 0.85, drehung=12)
             + pfeil(186, 80, 226, 92, "s2", 0) + pfeil(414, 76, 374, 90, "s2", 0)
             + '<path class="s2 k-rosa" fill="none" d="M232 96 l -14 -10 M 232 104 l -16 4 M 368 96 l 14 -10 M 368 104 l 16 4"/>'
             + fresszelle(76, 190, 0.6) + zelle(530, 188, 26, 18, "f-sand")
             + funkeln(560, 40, 0.7) + funkeln(60, 40, 0.6, "k-blau"))
    elif slug == "04-impfen":
        kuh = ('<g transform="translate(110 112)">'
               '<path class="s f-sand" d="M-46 -40 C -66 -52, -76 -40, -64 -30 M 46 -40 C 66 -52, 76 -40, 64 -30" fill="none"/>'
               '<ellipse class="s f-weiss" cx="-50" cy="-22" rx="16" ry="9" transform="rotate(-20 -50 -22)"/><ellipse class="s f-weiss" cx="50" cy="-22" rx="16" ry="9" transform="rotate(20 50 -22)"/>'
               '<path class="s f-weiss" d="M-36 -40 C -40 -6, -38 30, -30 46 C -20 66, 20 66, 30 46 C 38 30, 40 -6, 36 -40 C 20 -52, -20 -52, -36 -40 Z"/>'
               '<path class="d" opacity=".85" d="M-30 -30 C -20 -36, -10 -26, -16 -14 C -24 -6, -34 -14, -30 -30 Z M 14 -2 C 24 -10, 34 0, 28 12 C 20 18, 10 10, 14 -2 Z"/>'
               '<ellipse class="s f-rosa" cx="0" cy="44" rx="30" ry="18"/><ellipse class="d" cx="-11" cy="44" rx="4" ry="5"/><ellipse class="d" cx="11" cy="44" rx="4" ry="5"/>'
               '<circle class="d" cx="-16" cy="6" r="4"/><circle class="d" cx="16" cy="6" r="4"/></g>')
        spritze = ('<g transform="translate(300 104) rotate(-28)">'
                   '<rect class="s f-weiss" x="-60" y="-14" width="100" height="28" rx="4"/><rect class="f-blau" x="-20" y="-10" width="56" height="20"/>'
                   '<rect class="s f-weiss" x="-60" y="-14" width="100" height="28" rx="4" fill="none"/>'
                   '<path class="s2" d="M-40 -14 v8 M-28 -14 v8 M-16 -14 v8 M-4 -14 v8 M8 -14 v8 M20 -14 v8"/>'
                   '<path class="s f-sand" d="M-60 -6 H -84 V 6 H -60"/><rect class="s f-sand" x="-96" y="-18" width="12" height="36" rx="3"/>'
                   '<path class="s" d="M40 -5 H 54 L 86 0 L 54 5 H 40"/></g>')
        ausweis = ('<g transform="translate(470 108) rotate(6)">'
                   '<rect class="s f-gelb" x="-58" y="-74" width="116" height="148" rx="6"/><path class="s2" d="M-46 -74 V 74"/>'
                   + text(6, -40, "Impfausweis", "hk") +
                   '<path class="s2" d="M-34 -16 H 46 M -34 2 H 46 M -34 20 H 46 M -34 38 H 30"/>'
                   '<circle class="s k-blau" cx="30" cy="48" r="13" fill="none"/><path class="s2 k-blau" d="M22 48 l 6 6 l 10 -12" fill="none"/></g>')
        i = blob(300, 112, 280, 96, "f-gelb-weich", 2) + kuh + spritze + ausweis + funkeln(214, 40, 0.7) + funkeln(560, 196, 0.6, "k-blau")
    elif slug == "05-antibiotika-und-resistenz":
        schimmel = ('<g><path class="s f-gruen" d="M-18 -8 C -22 -22, -2 -26, 4 -16 C 16 -24, 30 -10, 20 0 C 26 12, 8 20, 0 12 C -10 22, -28 12, -18 -8 Z"/>'
                    '<circle class="d" cx="-6" cy="-6" r="2"/><circle class="d" cx="8" cy="2" r="2"/><circle class="d" cx="0" cy="-12" r="2"/></g>')
        kolonien = "".join(f'<circle class="s f-weiss" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(-72, -2, 7), (-58, 18, 6), (62, -8, 8), (74, 12, 6), (-40, -20, 5), (44, 20, 5), (56, -24, 5)])
        i = (blob(300, 112, 280, 96, "f-gruen-weich", -2)
             + petrischale(170, 118, 110, '<ellipse cx="0" cy="0" rx="40" ry="20" fill="none" class="s2 k-gruen" stroke-dasharray="4 5"/>' + schimmel + kolonien)
             + text(170, 200, "Fleming 1928", "h")
             + text(286, 56, "kein Wachstum!", "hk", "start", -4) + pfeil(284, 62, 216, 106, "s2", 18)
             + '<g transform="translate(450 110) rotate(-30)"><rect class="s f-weiss" x="-50" y="-20" width="100" height="40" rx="20"/><path class="f-rosa" d="M0 -20 H 30 A 20 20 0 0 1 30 20 H 0 Z"/><rect class="s" x="-50" y="-20" width="100" height="40" rx="20" fill="none"/><path class="s2" d="M0 -20 V 20"/></g>'
             + '<g transform="translate(530 160) rotate(20)"><rect class="s f-weiss" x="-30" y="-12" width="60" height="24" rx="12"/><path class="f-blau" d="M0 -12 H 18 A 12 12 0 0 1 18 12 H 0 Z"/><rect class="s" x="-30" y="-12" width="60" height="24" rx="12" fill="none"/><path class="s2" d="M0 -12 V 12"/></g>'
             + funkeln(560, 50, 0.7))
    else:  # Allergien
        blume = ('<g transform="translate(120 120)">'
                 '<path class="s k-gruen" stroke-width="3" fill="none" d="M0 10 C 4 40, -4 60, 0 90"/>'
                 '<path class="s f-gruen" d="M0 56 C 18 40, 40 44, 44 52 C 30 64, 12 64, 0 56 Z"/>'
                 + "".join(f'<ellipse class="s f-rosa" cx="{math.cos(math.radians(a)) * 24:.1f}" cy="{math.sin(math.radians(a)) * 24 - 10:.1f}" rx="16" ry="10" transform="rotate({a} {math.cos(math.radians(a)) * 24:.1f} {math.sin(math.radians(a)) * 24 - 10:.1f})"/>' for a in range(0, 360, 60)) +
                 '<circle class="s f-gelb" cx="0" cy="-10" r="14"/></g>')
        milch = ('<g transform="translate(420 112)"><path class="s f-weiss" d="M-30 -60 H 30 L 24 60 H -24 Z"/>'
                 '<path class="f-papier" d="M-27 -20 H 27 L 24 56 H -24 Z" opacity=".0"/><path class="s2" fill="none" d="M-27 -24 C -14 -16, 14 -32, 27 -24"/>'
                 + text(0, 26, "Milch", "hk") + '</g>')
        nuss = ('<g transform="translate(528 150) rotate(-20)"><path class="s f-sand" d="M-26 -10 C -30 -26, -6 -30, 0 -18 C 6 -30, 30 -26, 26 -10 C 30 6, 8 10, 0 2 C -8 10, -30 6, -26 -10 Z" transform="scale(1 1.3)"/>'
                '<path class="s2" fill="none" d="M-16 -16 l 4 4 M 10 -18 l 4 4 M -4 -4 l 4 4"/></g>' + text(528, 206, "Erdnuss", "hk"))
        i = (blob(300, 112, 280, 96, "f-rosa-weich", 3) + blume
             + pollen(220, 64, 11) + pollen(262, 104, 9) + pollen(236, 146, 8) + pollen(300, 60, 7)
             + pfeil(176, 90, 204, 74, "s2 gestrichelt", 6)
             + text(320, 170, "Hatschi!", "h", "middle", -6)
             + milch + nuss + funkeln(500, 40, 0.7))
    return deko("0 0 600 220", i, "ill lt-kopf")


# ---------------------------------------------------------------- Abbildungen in den Texten
def uebertragungswege():
    def kachel(x, titel, inhalt):
        return f'<g transform="translate({x} 0)"><rect class="s2 f-papier" x="4" y="4" width="142" height="142" rx="18"/>{inhalt}{text(75, 132, titel, "hk")}</g>'
    a = kachel(0, "Tröpfchen", '<path class="s f-weiss" d="M30 64 C 26 46, 46 36, 58 46 C 66 32, 90 36, 90 54 C 104 56, 104 76, 90 80 C 88 94, 64 96, 58 86 C 44 96, 26 84, 30 64 Z"/>'
               + "".join(tropfen(x, y, 0.45) for x, y in [(110, 52), (118, 76), (106, 96), (124, 100)]) + virus(62, 66, 0.5))
    b = kachel(150, "Kontakt", '<path class="s f-sand" d="M24 66 H 92 Q 104 66 104 78 Q 104 90 92 90 H 40"/><rect class="s f-blau" x="96" y="50" width="22" height="64" rx="8"/>'
               + virus(54, 54, 0.45) + virus(78, 48, 0.4, drehung=20))
    c = kachel(300, "Nahrung", '<path class="s f-sand" d="M44 90 C 30 64, 52 34, 80 40 C 108 46, 112 80, 90 92 C 80 98, 70 96, 64 104 L 52 116 C 46 122, 36 114, 42 108 L 54 96 C 50 94, 46 94, 44 90 Z"/>'
               + stab(76, 64, 26, 10, 20, "f-blau", False) + stab(94, 80, 22, 9, -30, "f-blau", False))
    d = kachel(450, "Tiere", '<g transform="translate(75 70)">' + "".join(f'<path class="s2" fill="none" d="M{sx * 10} {y} q {sx * 16} {-8} {sx * 26} {y2}"/>' for sx in (-1, 1) for y, y2 in ((-8, -10), (0, 4), (8, 14), (14, 22)))
               + '<ellipse class="s f-rosa-tief" cx="0" cy="6" rx="22" ry="28"/><circle class="s f-sand" cx="0" cy="-26" r="10"/><path class="s2" d="M-4 -34 l -4 -8 M 4 -34 l 4 -8" fill="none"/></g>')
    return svg("0 0 600 150", a + b + c + d, "Übertragungswege von Krankheitserregern",
               "Vier gezeichnete Kacheln: eine Niesen-Wolke mit Tröpfchen, eine Türklinke mit Viren, eine Hähnchenkeule mit Bakterien und eine Zecke.")


def krankheitsverlauf():
    stationen = [(60, "Infektion"), (190, "Inkubationszeit"), (330, "Ausbruch"), (450, "Genesung"), (560, "Immunität")]
    i = ('<rect class="f-rosa-weich" x="270" y="20" width="130" height="150" rx="14"/>' + text(335, 40, "Symptome", "hk")
         + '<path class="s k-rosa" stroke-width="4" fill="none" d="M40 160 C 120 158, 180 140, 230 100 S 300 40, 340 46 S 420 110, 470 150 S 560 162, 590 162"/>'
         + text(120, 128, "Erreger", "hk", "middle", -14)
         + '<path class="s k-blau" stroke-width="4" fill="none" stroke-dasharray="1 8" d="M40 168 C 160 168, 250 160, 300 120 S 380 50, 440 50 S 540 80, 590 84"/>'
         + text(520, 66, "Antikörper", "hk", "middle", 8)
         + '<line class="s" x1="30" y1="188" x2="590" y2="188"/>')
    for x, t in stationen:
        i += f'<circle class="s f-weiss" cx="{x}" cy="188" r="9"/>' + text(x, 218, t, "hk")
    i += virus(60, 150, 0.45)
    return svg("0 0 620 230", i, "Verlauf einer Infektionskrankheit",
               "Eine Zeitleiste mit den Stationen Infektion, Inkubationszeit, Ausbruch, Genesung und Immunität. Die Zahl der Erreger steigt bis zum Ausbruch an und fällt dann. Die Antikörper steigen verzögert an und bleiben danach erhöht.")


def zweiteilung():
    i = stab(60, 100, 44, 18, 0, "f-blau", False) + text(60, 150, "1", "h")
    pos = [(170, [(70,), (130,)]), ]
    i += pfeil(88, 92, 136, 70, "s2") + pfeil(88, 108, 136, 130, "s2")
    for y in (70, 130):
        i += stab(170, y, 40, 16, 0, "f-blau", False)
    i += text(170, 180, "2", "h") + text(110, 30, "20 min", "hk")
    i += pfeil(196, 66, 236, 46, "s2") + pfeil(196, 74, 236, 88, "s2") + pfeil(196, 126, 236, 112, "s2") + pfeil(196, 134, 236, 154, "s2")
    for y in (46, 88, 112, 154):
        i += stab(270, y, 36, 14, 0, "f-blau", False)
    i += text(270, 192, "4", "h") + text(220, 24, "40 min", "hk")
    for k, y in enumerate((36, 56, 78, 98, 102 + 6, 122, 144, 164)):
        pass
    ys = [30, 52, 74, 96, 116, 138, 160, 182]
    for y in ys:
        i += stab(390, y, 30, 12, 0, "f-blau", False)
    i += '<path class="s2" fill="none" d="M300 46 L 360 30 M 300 46 L 360 52 M 300 88 L 360 74 M 300 88 L 360 96 M 300 112 L 360 116 M 300 112 L 360 138 M 300 154 L 360 160 M 300 154 L 360 182"/>'
    i += text(450, 110, "8", "h") + text(340, 16, "60 min", "hk")
    i += text(540, 90, "… nach 5 Stunden:", "hk") + text(540, 124, "32 768", "h")
    return svg("0 0 620 200", i, "Vermehrung von Bakterien durch Zweiteilung",
               "Ein Bakterium teilt sich in zwei, nach 40 Minuten sind es vier, nach 60 Minuten acht. Nach fünf Stunden sind es 32 768 Bakterien.")


def abwehr_koerper():
    i = ('<g transform="translate(300 0)">'
         '<circle class="s f-sand" cx="0" cy="62" r="44"/>'
         '<path class="s f-sand" d="M-70 260 C -70 170, -54 128, -20 116 H 20 C 54 128, 70 170, 70 260 Z"/>'
         '<path class="s f-weiss" d="M-14 150 C -30 154, -30 200, 6 204 C 30 206, 34 176, 20 170 C 8 166, 10 150, -14 150 Z"/>'
         '<path class="s2 k-rosa" fill="none" d="M-12 186 h 4 M -2 192 h 4 M 6 182 h 4"/>'
         '<ellipse class="s f-weiss" cx="-16" cy="56" rx="8" ry="5"/><ellipse class="s f-weiss" cx="16" cy="56" rx="8" ry="5"/>'
         '<circle class="d" cx="-16" cy="56" r="2.5"/><circle class="d" cx="16" cy="56" r="2.5"/>'
         '<path class="s2" fill="none" d="M0 62 v 12 h -5"/><path class="s2" fill="none" d="M-12 88 q 12 8 24 0"/>'
         + tropfen(-26, 70, 0.4) + '</g>')
    labels = [(300 - 26, 70, 190, 40, "Tränen", "spülen Erreger weg"),
              (300, 74, 190, 120, "Nase", "Schleim fängt Erreger"),
              (310, 90, 470, 40, "Speichel", "schädigt Bakterien"),
              (366, 210, 480, 130, "Haut", "dichte Schutzschicht"),
              (300, 178, 480, 220, "Magen", "Säure tötet Erreger")]
    for x1, y1, x2, y2, t, u in labels:
        anker = "end" if x2 < 300 else "start"
        dx = -6 if x2 < 300 else 6
        i += f'<path class="s2" fill="none" d="M{x1} {y1} L {x2} {y2}"/><circle class="d" cx="{x1}" cy="{y1}" r="3"/>'
        i += text(x2 + dx, y2 - 2, t, "h", anker) + text(x2 + dx, y2 + 18, u, "hk", anker)
    return svg("0 0 620 270", i, "Äußere Schranken des Körpers",
               "Eine gezeichnete Person mit Beschriftungen: Tränen spülen Erreger weg, Nasenschleim und Flimmerhärchen fangen Erreger, Speichel schädigt Bakterien, die Haut ist eine dichte Schutzschicht und Magensäure tötet Erreger.")


def zeitstrahl_impfen():
    ereignisse = [(70, "1796", "Jenner", "Kuhpocken-Impfung"), (185, "1876", "Koch", "Erreger nachgewiesen"),
                  (300, "1885", "Pasteur", "Tollwut-Impfung"), (415, "1890", "Behring", "Heilserum"), (530, "1980", "WHO", "Pocken ausgerottet")]
    i = '<path class="s" stroke-width="3" fill="none" d="M20 100 C 160 96, 300 104, 600 98"/>' + pfeil(586, 98, 610, 98, "s")
    for k, (x, j, w, t) in enumerate(ereignisse):
        oben = k % 2 == 0
        y = 100
        i += f'<circle class="s f-gelb" cx="{x}" cy="{y}" r="11"/>'
        if oben:
            i += f'<path class="s2" d="M{x} {y - 11} V 58"/>' + text(x, 34, j, "h") + text(x, 52, w, "hk")
            i += text(x, 140, t, "hk")
        else:
            i += f'<path class="s2" d="M{x} {y + 11} V 142"/>' + text(x, 166, j, "h") + text(x, 184, w, "hk")
            i += text(x, 72, t, "hk")
    return svg("0 0 620 196", i, "Zeitstrahl zur Geschichte des Impfens",
               "1796 Jenner: Kuhpocken-Impfung. 1876 Koch: Erreger nachgewiesen. 1885 Pasteur: Tollwut-Impfung. 1890 Behring: Heilserum. 1980 WHO: Pocken ausgerottet.")


def gemeinschaftsschutz():
    import random
    rnd = random.Random(7)
    def feld(ox, geimpft_anteil, titel):
        g = f'<g transform="translate({ox} 0)"><rect class="s2 f-papier" x="4" y="4" width="282" height="200" rx="18"/>' + text(145, 30, titel, "h")
        pos = [(30 + c * 38, 56 + r * 34) for r in range(4) for c in range(7)]
        idx = list(range(len(pos))); rnd.shuffle(idx)
        geimpft = set(idx[: int(len(pos) * geimpft_anteil)])
        start = 10
        for n, (x, y) in enumerate(pos):
            if n == start:
                g += f'<circle class="s f-rosa-tief" cx="{x}" cy="{y}" r="11"/>'
            elif n in geimpft:
                g += f'<circle class="s f-blau" cx="{x}" cy="{y}" r="11"/><path class="s2" fill="none" d="M{x - 5} {y} l 4 4 l 7 -8"/>'
            else:
                krank = geimpft_anteil < 0.5 and rnd.random() < 0.7
                g += f'<circle class="s {"f-rosa" if krank else "f-weiss"}" cx="{x}" cy="{y}" r="11"/>'
        return g + "</g>"
    i = feld(0, 0.2, "wenige geimpft") + feld(320, 0.85, "viele geimpft")
    i += '<g transform="translate(0 214)">'
    i += '<circle class="s f-rosa-tief" cx="20" cy="0" r="8"/>' + text(34, 6, "erkrankt, steckt an", "hk", "start")
    i += '<circle class="s f-rosa" cx="200" cy="0" r="8"/>' + text(214, 6, "angesteckt", "hk", "start")
    i += '<circle class="s f-blau" cx="330" cy="0" r="8"/>' + text(344, 6, "geimpft", "hk", "start")
    i += '<circle class="s f-weiss" cx="450" cy="0" r="8"/>' + text(464, 6, "nicht geimpft, gesund", "hk", "start") + "</g>"
    return svg("0 0 620 230", i, "Gemeinschaftsschutz durch Impfen",
               "Zwei Gruppen von je 28 Menschen. Links sind wenige geimpft, und von einer kranken Person aus haben sich viele angesteckt. Rechts sind die meisten geimpft, und die Krankheit kann sich nicht ausbreiten.")


def resistenz_bilder():
    def schale(ox, blau, rot, titel, tropfen_an=False):
        import random
        rnd = random.Random(ox)
        inner = ""
        for _ in range(blau):
            inner += f'<circle class="s2 f-blau" cx="{rnd.uniform(-46, 46):.0f}" cy="{rnd.uniform(-16, 16):.0f}" r="5"/>'
        for _ in range(rot):
            inner += f'<circle class="s2 f-rosa-tief" cx="{rnd.uniform(-46, 46):.0f}" cy="{rnd.uniform(-16, 16):.0f}" r="5"/>'
        t = "".join(tropfen(x, y, 0.5, "f-gelb") for x, y in ((-18, -46), (6, -56), (26, -44))) if tropfen_an else ""
        return f'<g transform="translate({ox} 0)">{petrischale(70, 100, 62, inner)}<g transform="translate(70 100)">{t}</g>{text(70, 168, titel, "hk")}</g>'
    i = (schale(0, 22, 1, "1. zufällig eine resistent") + schale(150, 22, 1, "2. Antibiotikum", True)
         + schale(300, 2, 1, "3. resistente überleben") + schale(450, 2, 18, "4. sie vermehren sich"))
    i += pfeil(132, 100, 160, 100, "s2") + pfeil(282, 100, 310, 100, "s2") + pfeil(432, 100, 460, 100, "s2")
    return svg("0 0 600 180", i, "Entstehung einer Antibiotikaresistenz in vier Schritten",
               "Vier Petrischalen: 1. Viele empfindliche Bakterien und ein resistentes. 2. Ein Antibiotikum wird zugegeben. 3. Nur das resistente und wenige empfindliche Bakterien überleben. 4. Die resistenten Bakterien vermehren sich und überwiegen.")


def allergie_ablauf():
    mast = lambda x, y, ak=True: (zelle(x, y, 40, 30, "f-sand") + ("".join(antikoerper(x + math.cos(math.radians(a)) * 46, y + math.sin(math.radians(a)) * 36, 0.55, a + 90) for a in (-150, -90, -30, 30, 150)) if ak else ""))
    i = (f'<g>{pollen(70, 60, 12)}{pfeil(70, 82, 70, 110, "s2")}{zelle(70, 150, 40, 30, "f-sand")}{text(70, 210, "1. Erstkontakt:", "hk")}{text(70, 228, "Antikörper entstehen", "hk")}</g>'
         + pfeil(130, 150, 176, 150, "s2")
         + f'<g transform="translate(160 0)">{mast(100, 150)}{pollen(100, 88, 9)}{pollen(154, 112, 8)}{text(100, 210, "2. Zweitkontakt:", "hk")}{text(100, 228, "Allergen bindet", "hk")}</g>'
         + pfeil(318, 150, 356, 150, "s2")
         + f'<g transform="translate(340 0)">{mast(70, 150)}' + "".join(f'<circle class="d k-rosa" style="fill:var(--eosin)" cx="{70 + math.cos(math.radians(a)) * r:.0f}" cy="{150 + math.sin(math.radians(a)) * r * 0.6:.0f}" r="3.5"/>' for a, r in ((10, 70), (40, 66), (60, 56), (130, 68), (200, 72), (250, 70), (300, 66), (340, 74))) + f'{text(70, 210, "3. Histamin wird", "hk")}{text(70, 228, "ausgeschüttet", "hk")}</g>'
         + pfeil(470, 150, 500, 150, "s2")
         + f'<g transform="translate(500 0)">{text(60, 110, "Niesen", "h")}{text(60, 140, "Juckreiz", "h")}{text(60, 170, "Schwellung", "h")}{text(60, 228, "4. Beschwerden", "hk")}</g>')
    return svg("0 0 620 240", i, "Ablauf einer allergischen Reaktion",
               "1. Beim Erstkontakt mit einem Allergen wie Pollen bildet das Immunsystem Antikörper. 2. Beim Zweitkontakt bindet das Allergen an Antikörper auf Mastzellen. 3. Die Mastzellen schütten Histamin aus. 4. Es kommt zu Niesen, Juckreiz und Schwellungen.")


# ---------------------------------------------------------------- kleine Symbole für Listen
def symbol(name):
    v = "0 0 64 64"
    if name == "01-gesund-oder-krank":
        i = '<g transform="translate(32 34) rotate(-20)"><rect class="s f-weiss" x="-6" y="-26" width="12" height="40" rx="6"/><circle class="s f-weiss" cx="0" cy="16" r="10"/><rect class="f-rosa-tief" x="-2.5" y="-8" width="5" height="22"/><circle class="f-rosa-tief" cx="0" cy="16" r="6"/></g>'
    elif name == "02-bakterien-und-viren":
        i = stab(26, 26, 30, 12, -20, "f-blau", False) + virus(42, 44, 0.55)
    elif name == "03-das-immunsystem":
        i = '<path class="s f-blau" d="M32 8 L 52 14 C 52 36, 46 50, 32 58 C 18 50, 12 36, 12 14 Z"/>' + antikoerper(32, 32, 0.8)
    elif name == "04-impfen":
        i = '<g transform="translate(32 32) rotate(-40)"><rect class="s f-weiss" x="-18" y="-7" width="30" height="14" rx="3"/><rect class="f-blau" x="-6" y="-4" width="16" height="8"/><path class="s" d="M12 -3 H 18 L 28 0 L 18 3 H 12 M -18 0 H -26 M -28 -8 V 8" fill="none"/></g>'
    elif name == "05-antibiotika-und-resistenz":
        i = '<g transform="translate(32 32) rotate(-35)"><rect class="s f-weiss" x="-22" y="-10" width="44" height="20" rx="10"/><path class="f-rosa" d="M0 -10 H 12 A 10 10 0 0 1 12 10 H 0 Z"/><rect class="s" x="-22" y="-10" width="44" height="20" rx="10" fill="none"/><path class="s2" d="M0 -10 V 10"/></g>'
    elif name == "06-allergien-und-unvertraeglichkeiten":
        i = pollen(32, 32, 13)
    elif name == "lichtmikroskop":
        return deko("-120 -120 250 250", mikroskop(0, -6, 0.95), "ill symbol")
    elif name == "schluessel-schloss":
        i = virus(22, 32, 0.6) + antikoerper(46, 36, 0.8, -90)
    elif name == "immunreaktion":
        i = fresszelle(32, 32, 0.55) + virus(30, 34, 0.3)
    elif name == "antibiotika-resistenz":
        i = petrischale(32, 36, 24, '<circle class="s2 f-blau" cx="-8" cy="0" r="4"/><circle class="s2 f-rosa-tief" cx="6" cy="-2" r="4"/><circle class="s2 f-rosa-tief" cx="12" cy="4" r="4"/>')
    elif name == "quiz-grundwissen":
        i = '<path class="s f-gelb" d="M10 14 Q 10 8 16 8 H 48 Q 54 8 54 14 V 38 Q 54 44 48 44 H 28 L 18 54 L 20 44 H 16 Q 10 44 10 38 Z"/><text class="h" x="32" y="36" text-anchor="middle">?</text>'
    elif name == "zuordnen-abwehrzellen":
        i = '<circle class="s f-blau" cx="14" cy="18" r="6"/><circle class="s f-rosa" cx="14" cy="46" r="6"/><rect class="s f-weiss" x="40" y="12" width="16" height="12" rx="3"/><rect class="s f-weiss" x="40" y="40" width="16" height="12" rx="3"/><path class="s2" fill="none" d="M20 18 C 30 18, 30 46, 40 46 M 20 46 C 30 46, 30 18, 40 18"/>'
    elif name == "sortieren-bakterien-viren":
        i = '<path class="s f-blau" d="M8 30 H 28 V 54 H 8 Z"/><path class="s f-rosa" d="M36 30 H 56 V 54 H 36 Z"/>' + stab(18, 16, 16, 7, 0, "f-blau", False) + virus(46, 16, 0.35)
    elif name == "lueckentext-impfen":
        i = '<rect class="s f-weiss" x="8" y="10" width="48" height="44" rx="5"/><path class="s2" d="M14 22 H 28 M 44 22 H 50 M 14 34 H 22 M 38 34 H 50 M 14 46 H 34"/><rect class="s2 f-gelb" x="30" y="16" width="12" height="11" rx="2"/><rect class="s2 f-gelb" x="24" y="28" width="12" height="11" rx="2"/>'
    elif name == "sortieren-allergie-unvertraeglichkeit":
        i = '<path class="s f-weiss" d="M20 10 H 44 L 40 56 H 24 Z"/><path class="s2" fill="none" d="M21 24 C 28 28, 36 20, 43 24"/>' + pollen(48, 46, 6)
    elif name in EXTRA_SYMBOLE:
        i = EXTRA_SYMBOLE[name]()
    else:
        i = ""
    return deko(v, i, "ill symbol")


# ---------------------------------------------------------------- Ergänzungen
def krankheiten_kopf():
    # Steckbrief-Karteikarten mit Bakterium und Virus, Lupe, Arztkoffer
    karte = lambda x, y, d, inhalt, titel: (f'<g transform="translate({x} {y}) rotate({d})"><rect class="s f-weiss" x="-70" y="-62" width="140" height="124" rx="8"/>'
                                          f'<rect class="f-gelb" x="-70" y="-62" width="140" height="26" rx="8"/><path class="s" fill="none" d="M-70 -36 H 70"/>'
                                          + text(0, -43, titel, "hk") + inhalt +
                                          '<path class="s2" d="M-50 36 H 50 M -50 48 H 30"/></g>')
    b = karte(150, 112, -6, stab(0, 0, 70, 26, -12, "f-blau", True), "Bakterium")
    v = karte(320, 104, 5, virus(0, 0, 1.25), "Virus")
    koffer = ('<g transform="translate(486 130)"><rect class="s f-sand" x="-56" y="-38" width="112" height="78" rx="10"/>'
              '<path class="s" fill="none" d="M-20 -38 V -52 H 20 V -38"/><rect class="f-rosa-tief" x="-7" y="-22" width="14" height="44"/><rect class="f-rosa-tief" x="-22" y="-7" width="44" height="14"/></g>')
    i = blob(300, 112, 280, 96, "f-blau-weich", -2) + b + v + koffer + funkeln(240, 30, 0.7) + funkeln(560, 50, 0.6, "k-blau")
    return deko("0 0 600 220", i, "ill lt-kopf")


def virusvermehrung():
    # Sechs Schritte der Virusvermehrung in einer Wirtszelle
    def zelle_bg(x, y):
        return (f'<g transform="translate({x} {y})"><rect class="s f-sand" x="-62" y="-50" width="124" height="100" rx="34"/>'
                f'<circle class="s f-weiss" cx="16" cy="6" r="16"/><circle class="d" cx="18" cy="6" r="4"/></g>')
    erbgut = lambda x, y, s=1: f'<path transform="translate({x} {y}) scale({s})" class="s2 k-rosa" stroke-width="2.4" fill="none" d="M-8 -2 q 4 -7 8 0 t 8 0"/>'
    hulle = lambda x, y, s=0.55: f'<polygon transform="translate({x} {y}) scale({s})" class="s2 f-rosa" points="0,-12 10,-6 10,6 0,12 -10,6 -10,-6"/>'
    k = []
    xs = [80, 230, 380, 530, 680, 830]
    titel = ["1. Andocken", "2. Eindringen", "3. Erbgut freisetzen", "4. Vermehren", "5. Zusammenbau", "6. Freisetzung"]
    for n, x in enumerate(xs):
        g = zelle_bg(x, 90)
        if n == 0: g += virus(x, 28, 0.8)
        if n == 1: g += virus(x - 20, 66, 0.65)
        if n == 2: g += erbgut(x - 24, 84, 1.2) + ''.join(f'<path class="s2 f-rosa" d="M{x - 40 + j * 7} {104 + (j % 2) * 4} l 5 -3" />' for j in range(4))
        if n == 3: g += erbgut(x - 34, 72) + erbgut(x - 20, 100) + erbgut(x - 40, 110) + hulle(x - 30, 88) + hulle(x + 44, 114, 0.45) + hulle(x - 8, 120, 0.45) + hulle(x + 42, 70, 0.45)
        if n == 4: g += ''.join(virus(px, py, 0.5) for px, py in [(x - 36, 70), (x - 30, 108), (x + 42, 112), (x - 6, 124)])
        if n == 5: g += ''.join(virus(px, py, 0.5) for px, py in [(x - 74, 40), (x + 68, 34), (x + 76, 130), (x - 70, 140)]) + virus(x - 30, 100, 0.5)
        k.append(g + text(x, 172, titel[n], "hk"))
    pf = ''.join(pfeil(x + 66, 90, x + 84, 90, "s2") for x in xs[:-1])
    return svg("0 0 910 186", "".join(k) + pf, "Vermehrung eines Virus in sechs Schritten",
               "1. Das Virus dockt an die Wirtszelle an. 2. Es dringt ein. 3. Die Hülle löst sich, das Erbgut wird frei. 4. Die Zelle vervielfältigt das Virus-Erbgut und stellt Hüllbausteine her. 5. Neue Viren werden zusammengebaut. 6. Die Viren verlassen die Zelle.")


def _sym_krank():
    return stab(22, 26, 26, 11, -20, "f-blau", False) + virus(44, 42, 0.6)


def _sym_training():
    return ('<rect class="s f-weiss" x="12" y="8" width="40" height="50" rx="5"/><rect class="s f-sand" x="22" y="4" width="20" height="9" rx="3"/>'
            '<path class="s2 k-gruen" fill="none" d="M18 24 l 4 4 l 7 -8 M 18 38 l 4 4 l 7 -8"/><path class="s2" d="M33 26 H 46 M 33 40 H 46 M 18 52 H 42"/>')


def _sym_reihenfolge():
    return ('<rect class="s f-blau" x="10" y="8" width="44" height="12" rx="4"/><rect class="s f-rosa" x="10" y="26" width="44" height="12" rx="4"/>'
            '<rect class="s f-gelb" x="10" y="44" width="44" height="12" rx="4"/><text class="hk" x="16" y="18" style="font-size:12px">1</text>'
            '<text class="hk" x="16" y="36" style="font-size:12px">2</text><text class="hk" x="16" y="54" style="font-size:12px">3</text>')


def _sym_schreiben():
    return ('<rect class="s f-weiss" x="8" y="10" width="38" height="46" rx="4"/><path class="s2" d="M14 22 H 38 M 14 32 H 38 M 14 42 H 30"/>'
            '<g transform="rotate(35 46 32)"><rect class="s f-gelb" x="42" y="6" width="9" height="40" rx="2"/><path class="s f-sand" d="M42 46 L 46.5 56 L 51 46 Z"/></g>')


def _sym_quiz():
    return ('<path class="s f-gelb" d="M10 14 Q 10 8 16 8 H 48 Q 54 8 54 14 V 38 Q 54 44 48 44 H 28 L 18 54 L 20 44 H 16 Q 10 44 10 38 Z"/><text class="h" x="32" y="36" text-anchor="middle">?</text>')


EXTRA_KOEPFE = {"07-krankheiten-steckbriefe": krankheiten_kopf}
EXTRA_SYMBOLE = {
    "07-krankheiten-steckbriefe": _sym_krank,
    "sortieren-krankheiten": _sym_krank,
    "quiz-wer-bin-ich": _sym_quiz,
    "ka-fachbegriffe": _sym_training,
    "ka-wissenscheck": _sym_training,
    "ka-lueckentext-bakterien": _sym_training,
    "ka-virusvermehrung": _sym_reihenfolge,
    "ka-krankheitsverlauf": _sym_reihenfolge,
    "ka-krankheit-beschreiben": _sym_schreiben,
}
