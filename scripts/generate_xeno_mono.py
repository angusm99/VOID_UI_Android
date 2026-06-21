"""
Regenerate all 121 placeholder Xenocomm icons as WHITE monoline glyphs.

  - 87 concepts that match an existing core drawable: recolour that drawable
    to white (#FFFFFFFF), strip any opaque black bg plate, save as xeno_<c>.xml
  - 36 alien concepts with no core glyph: hand-authored white monoline SVG,
    converted to VectorDrawable

Leaves xeno_ai_core/xeno_chatgpt logic to the same rules (they get clean white art).
Writes XML to drawable/ + drawable-nodpi/ and SVG masters to ICON_MASTER/09_XENOCOMM/.
Does NOT touch the OPEN_DESIGN_TRANSFER folders.
"""
import re
from pathlib import Path

ROOT = Path(r"C:\Users\User\CLAUDE\VOID_UI")
MASTER_XENO = ROOT / "01_ICON_PACK_MASTER" / "ICON_MASTER" / "09_XENOCOMM"
MASTER_TERMINAL = ROOT / "01_ICON_PACK_MASTER" / "ICON_MASTER" / "06_TERMINAL"
RES = ROOT / "02_ANDROID_ICON_PACK_APP" / "VOID_UI_Android" / "app" / "src" / "main" / "res"
DRAWABLE = RES / "drawable"
NODPI = RES / "drawable-nodpi"

WHITE = "#FFFFFFFF"
ANS = "{http://schemas.android.com/apk/res/android}"
# core glyphs measure ~24px effective stroke at 512; thin to ~15 to match authored
STROKE_SCALE = 0.62

# ── minimal SVG→VectorDrawable converter (primitives → path, white forced) ──
def clean(v):
    n = float(v)
    return str(int(round(n))) if abs(n-round(n)) < 1e-6 else f"{n:.3f}".rstrip("0").rstrip(".")

def acol(v):
    if not v or v == "none":
        return None
    lo = v.lower()
    if lo in ("#fff", "#ffffff", "white", "currentcolor"):
        return WHITE
    if lo in ("#000", "#000000", "black"):
        return "#FF000000"
    if lo.startswith("#"):
        h = lo[1:]
        if len(h) == 3: h = "".join(c*2 for c in h)
        if len(h) == 6: return "#FF"+h.upper()
        if len(h) == 8: return "#"+h.upper()
    return v

def af(a, n, d=0):
    r = a.get(n)
    return float(str(r).replace("px","")) if r is not None else d

def circle_path(cx, cy, r):
    return f"M{clean(cx-r)},{clean(cy)} A{clean(r)},{clean(r)} 0,1 0 {clean(cx+r)},{clean(cy)} A{clean(r)},{clean(r)} 0,1 0 {clean(cx-r)},{clean(cy)}"

def rect_path(x, y, w, h, rx=0):
    x2, y2 = x+w, y+h
    if rx <= 0:
        return f"M{clean(x)},{clean(y)} H{clean(x2)} V{clean(y2)} H{clean(x)} Z"
    rx = min(rx, w/2, h/2)
    return (f"M{clean(x+rx)},{clean(y)} H{clean(x2-rx)} Q{clean(x2)},{clean(y)} {clean(x2)},{clean(y+rx)} "
            f"V{clean(y2-rx)} Q{clean(x2)},{clean(y2)} {clean(x2-rx)},{clean(y2)} H{clean(x+rx)} "
            f"Q{clean(x)},{clean(y2)} {clean(x)},{clean(y2-rx)} V{clean(y+rx)} Q{clean(x)},{clean(y)} {clean(x+rx)},{clean(y)} Z")

def points_path(pts, close):
    c = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", pts or "")]
    if len(c) < 4: return None
    pr = list(zip(c[0::2], c[1::2]))
    cmds = [f"M{clean(pr[0][0])},{clean(pr[0][1])}"] + [f"L{clean(x)},{clean(y)}" for x,y in pr[1:]]
    if close: cmds.append("Z")
    return " ".join(cmds)

def style(a):
    fill, stroke = acol(a.get("fill","none")), acol(a.get("stroke"))
    out = []
    if fill:
        out.append(("android:fillColor", fill))
        if "fill-opacity" in a: out.append(("android:fillAlpha", clean(a["fill-opacity"])))
    if stroke:
        out += [("android:strokeColor", stroke), ("android:strokeWidth", clean(af(a,"stroke-width",1)))]
        if "stroke-linecap" in a: out.append(("android:strokeLineCap", a["stroke-linecap"]))
        if "stroke-linejoin" in a: out.append(("android:strokeLineJoin", a["stroke-linejoin"]))
    return out

def emit(d, a):
    if not d: return []
    s = style(a) or [("android:fillColor", "#00000000")]
    return ["    <path"] + [f'        {k}="{v}"' for k,v in s] + [f'        android:pathData="{d}"/>']

ATTR_RE = re.compile(r'(\S+?)="([^"]*)"')
def parse_attrs(tag):
    a = {}
    for m in ATTR_RE.finditer(tag):
        a[m.group(1)] = m.group(2)
    if "style" in a:
        for part in a["style"].split(";"):
            if ":" in part:
                k,v = part.split(":",1); a[k.strip()] = v.strip()
    return a

def convert_svg_body(body):
    """body = inner SVG markup (no <svg> wrapper). Returns list of <path> lines."""
    out = []
    for m in re.finditer(r'<(path|line|circle|rect|polyline|polygon)\b([^>]*)/?>', body):
        tag, attrs = m.group(1), parse_attrs(m.group(2))
        if tag == "path":
            out += emit(attrs.get("d"), attrs)
        elif tag == "line":
            out += emit(f"M{clean(af(attrs,'x1'))},{clean(af(attrs,'y1'))} L{clean(af(attrs,'x2'))},{clean(af(attrs,'y2'))}", attrs)
        elif tag == "circle":
            out += emit(circle_path(af(attrs,"cx"), af(attrs,"cy"), af(attrs,"r")), attrs)
        elif tag == "rect":
            out += emit(rect_path(af(attrs,"x"), af(attrs,"y"), af(attrs,"width"), af(attrs,"height"), af(attrs,"rx")), attrs)
        elif tag == "polyline":
            out += emit(points_path(attrs.get("points"), False), attrs)
        elif tag == "polygon":
            out += emit(points_path(attrs.get("points"), True), attrs)
    return out

def wrap_xml(paths):
    return "\n".join(['<vector xmlns:android="http://schemas.android.com/apk/res/android"',
                      '    android:width="512dp"', '    android:height="512dp"',
                      '    android:viewportWidth="512"', '    android:viewportHeight="512">',
                      *paths, '</vector>', ''])

def wrap_svg(body):
    return f'<svg viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">\n{body}\n</svg>\n'

# ── recolour an existing core drawable to white, strip bg plate ──
def recolor_drawable(text):
    # Strip ANY full-canvas background plate: a fill-only path (no stroke) whose
    # data starts at the origin (M0 ...). Covers square (M0 0 H..V..), rounded-rect
    # app-icon plates (M0 24c0-13.25...), and 64/108/512 variants alike.
    def strip_plate(m):
        tag = m.group(0)
        if "strokeColor" in tag:
            return tag  # stroked shape — never a plate
        pd = re.search(r'pathData="([^"]*)"', tag)
        fc = re.search(r'fillColor="([^"]*)"', tag)
        if not pd or not fc:
            return tag
        fill = fc.group(1)
        if fill == "@android:color/transparent" or fill.upper() == "#00000000":
            return tag
        data = pd.group(1).lstrip()
        if re.match(r"M\s*0[\s,cChHvVlLzZ]", data):
            return ""  # background plate starting at origin — drop it
        return tag
    text = re.sub(r"<path\b.*?/>", strip_plate, text, flags=re.DOTALL)
    # thin core-glyph strokes ~35% so they match the lighter authored weight.
    # account for group scale so effective stroke lands near the 15px target.
    def scale_w(m):
        return f'android:strokeWidth="{round(float(m.group(1)) * STROKE_SCALE, 2)}"'
    text = re.sub(r'android:strokeWidth="([\d.]+)"', scale_w, text)
    # force every remaining non-transparent colour to white
    def repl(m):
        attr, val = m.group(1), m.group(2)
        if val.upper() == "#00000000":
            return m.group(0)
        return f'{attr}="{WHITE}"'
    text = re.sub(r'(android:strokeColor)="(#[0-9A-Fa-f]{6,8})"', repl, text)
    text = re.sub(r'(android:fillColor)="(#[0-9A-Fa-f]{6,8})"', repl, text)
    return text

# ── default monoline style for authored glyphs ──
S = 'fill="none" stroke="#FFFFFF" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"'
ST = 'fill="none" stroke="#FFFFFF" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"'
F = 'fill="#FFFFFF"'

GLYPHS = {
"ai_core": f'<circle cx="256" cy="256" r="128" {S}/><circle cx="256" cy="256" r="66" {S}/>'
    f'<line x1="256" y1="128" x2="256" y2="92" {S}/><line x1="256" y1="384" x2="256" y2="420" {S}/>'
    f'<line x1="128" y1="256" x2="92" y2="256" {S}/><line x1="384" y1="256" x2="420" y2="256" {S}/>'
    f'<line x1="346" y1="166" x2="372" y2="140" {S}/><line x1="166" y1="346" x2="140" y2="372" {S}/>'
    f'<line x1="346" y1="346" x2="372" y2="372" {S}/><line x1="166" y1="166" x2="140" y2="140" {S}/>'
    f'<circle cx="256" cy="256" r="16" {F}/>',
"alarm": f'<circle cx="256" cy="286" r="104" {S}/><line x1="178" y1="190" x2="146" y2="158" {S}/>'
    f'<line x1="334" y1="190" x2="366" y2="158" {S}/><line x1="256" y1="286" x2="256" y2="220" {S}/>'
    f'<line x1="256" y1="286" x2="306" y2="312" {S}/>',
"biolume": f'<path d="M256 140 C 338 140 372 224 336 300 C 304 366 208 366 176 300 C 140 224 174 140 256 140 Z" {S}/>'
    f'<circle cx="226" cy="244" r="14" {F}/><circle cx="292" cy="232" r="10" {F}/><circle cx="262" cy="300" r="12" {F}/>',
"black_hole": f'<path d="M104 256 A152 60 0 1 0 408 256 A152 60 0 1 0 104 256" {S}/>'
    f'<path d="M150 256 A106 40 0 1 0 362 256 A106 40 0 1 0 150 256" {ST}/>'
    f'<circle cx="256" cy="256" r="50" {S}/><circle cx="256" cy="256" r="14" {F}/>',
"brain": f'<path d="M256 156 C 212 146 174 172 178 212 C 148 226 146 272 180 290 C 180 330 222 348 256 334 '
    f'C 290 348 332 330 332 290 C 366 272 364 226 334 212 C 338 172 300 146 256 156 Z" {S}/>'
    f'<line x1="256" y1="160" x2="256" y2="334" {ST}/>'
    f'<path d="M212 206 C 232 224 232 250 214 268" {ST}/><path d="M300 206 C 280 224 280 250 298 268" {ST}/>',
"bug": f'<circle cx="256" cy="284" r="72" {S}/><circle cx="256" cy="190" r="34" {S}/>'
    f'<line x1="240" y1="166" x2="224" y2="138" {S}/><line x1="272" y1="166" x2="288" y2="138" {S}/>'
    f'<line x1="184" y1="252" x2="146" y2="232" {S}/><line x1="184" y1="300" x2="146" y2="300" {S}/>'
    f'<line x1="184" y1="340" x2="150" y2="366" {S}/><line x1="328" y1="252" x2="366" y2="232" {S}/>'
    f'<line x1="328" y1="300" x2="366" y2="300" {S}/><line x1="328" y1="340" x2="362" y2="366" {S}/>',
"cell": f'<rect x="150" y="150" width="212" height="212" rx="52" {S}/><circle cx="256" cy="256" r="48" {F}/>',
"chart_down": f'<path d="M158 138 V374 H394" {S}/>'
    f'<polyline points="186,206 248,262 300,232 372,332" {S}/>'
    f'<polyline points="372,288 372,332 328,332" {S}/>',
"coin": f'<circle cx="256" cy="256" r="112" {S}/><circle cx="256" cy="256" r="78" {ST}/>'
    f'<line x1="256" y1="198" x2="256" y2="314" {S}/>',
"comet": f'<circle cx="324" cy="196" r="48" {S}/>'
    f'<line x1="288" y1="232" x2="150" y2="370" {S}/><line x1="318" y1="252" x2="210" y2="372" {S}/>'
    f'<line x1="262" y1="222" x2="150" y2="312" {S}/>',
"crystal": f'<polygon points="256,138 342,212 302,374 210,374 170,212" {S}/>'
    f'<line x1="170" y1="212" x2="342" y2="212" {ST}/><line x1="256" y1="138" x2="256" y2="374" {ST}/>',
"equalizer": f'<line x1="190" y1="360" x2="190" y2="240" {S}/><line x1="246" y1="360" x2="246" y2="160" {S}/>'
    f'<line x1="302" y1="360" x2="302" y2="208" {S}/><line x1="358" y1="360" x2="358" y2="288" {S}/>',
"frequency": f'<path d="M138 256 Q 178 168 218 256 T 298 256 T 378 256" {S}/>',
"galaxy": f'<path d="M256 256 C 322 196 372 264 326 328 C 290 376 214 360 192 312" {S}/>'
    f'<path d="M256 256 C 190 316 140 248 186 184 C 222 136 298 152 320 200" {S}/>'
    f'<circle cx="256" cy="256" r="16" {F}/>',
"git": f'<circle cx="204" cy="172" r="24" {S}/><circle cx="204" cy="352" r="24" {S}/><circle cx="320" cy="256" r="24" {S}/>'
    f'<line x1="204" y1="196" x2="204" y2="328" {S}/><path d="M204 256 H300" {S}/><line x1="320" y1="232" x2="320" y2="200" {ST}/>',
"healing": f'<circle cx="256" cy="256" r="118" {S}/><line x1="256" y1="196" x2="256" y2="316" {S}/>'
    f'<line x1="196" y1="256" x2="316" y2="256" {S}/>',
"hive_mind": f'<polygon points="256,150 296,174 296,222 256,246 216,222 216,174" {S}/>'
    f'<polygon points="186,258 226,282 226,330 186,354 146,330 146,282" {S}/>'
    f'<polygon points="326,258 366,282 366,330 326,354 286,330 286,282" {S}/>',
"inference": f'<path d="M148 256 H322" {S}/><polyline points="296,228 330,256 296,284" {S}/>'
    f'<circle cx="360" cy="256" r="20" {F}/>',
"meditation": f'<circle cx="256" cy="178" r="36" {S}/><path d="M256 220 V286" {S}/>'
    f'<path d="M168 332 Q 256 288 344 332 Q 256 372 168 332 Z" {S}/>'
    f'<path d="M256 256 L196 312" {ST}/><path d="M256 256 L316 312" {ST}/>',
"mycelium": f'<path d="M256 372 V256" {S}/><path d="M256 300 C 220 280 196 246 188 200" {S}/>'
    f'<path d="M256 300 C 292 280 316 246 324 200" {S}/><path d="M256 256 C 230 240 214 214 208 182" {ST}/>'
    f'<path d="M256 256 C 282 240 298 214 304 182" {ST}/>'
    f'<circle cx="188" cy="194" r="12" {F}/><circle cx="324" cy="194" r="12" {F}/><circle cx="256" cy="160" r="12" {F}/>',
"nebula": f'<path d="M196 220 C 150 220 150 286 196 290 C 188 332 250 348 272 318 C 318 340 360 296 332 262 '
    f'C 360 224 320 184 286 200 C 270 168 214 176 196 220 Z" {S}/>'
    f'<circle cx="226" cy="252" r="9" {F}/><circle cx="288" cy="270" r="9" {F}/><circle cx="258" cy="300" r="7" {F}/>',
"network": f'<line x1="256" y1="256" x2="406" y2="256" {ST}/><line x1="256" y1="256" x2="331" y2="386" {ST}/>'
    f'<line x1="256" y1="256" x2="181" y2="386" {ST}/><line x1="256" y1="256" x2="106" y2="256" {ST}/>'
    f'<line x1="256" y1="256" x2="181" y2="126" {ST}/><line x1="256" y1="256" x2="331" y2="126" {ST}/>'
    f'<circle cx="406" cy="256" r="18" {S}/><circle cx="331" cy="386" r="18" {S}/><circle cx="181" cy="386" r="18" {S}/>'
    f'<circle cx="106" cy="256" r="18" {S}/><circle cx="181" cy="126" r="18" {S}/><circle cx="331" cy="126" r="18" {S}/>'
    f'<circle cx="256" cy="256" r="24" {S}/>',
"neural": f'<circle cx="172" cy="180" r="18" {S}/><circle cx="172" cy="332" r="18" {S}/>'
    f'<circle cx="256" cy="256" r="18" {S}/><circle cx="340" cy="180" r="18" {S}/><circle cx="340" cy="332" r="18" {S}/>'
    f'<line x1="190" y1="180" x2="238" y2="246" {ST}/><line x1="190" y1="332" x2="238" y2="266" {ST}/>'
    f'<line x1="274" y1="246" x2="322" y2="180" {ST}/><line x1="274" y1="266" x2="322" y2="332" {ST}/>',
"pause": f'<line x1="212" y1="160" x2="212" y2="352" stroke="#FFFFFF" stroke-width="40" stroke-linecap="round"/>'
    f'<line x1="300" y1="160" x2="300" y2="352" stroke="#FFFFFF" stroke-width="40" stroke-linecap="round"/>',
"planet": f'<circle cx="256" cy="256" r="92" {S}/>'
    f'<path d="M168 296 A150 38 -22 1 0 360 214" {ST}/>',
"play": f'<polygon points="198,160 364,256 198,352" {S}/>',
"processor": f'<rect x="180" y="180" width="152" height="152" rx="18" {S}/><rect x="222" y="222" width="68" height="68" {ST}/>'
    f'<line x1="212" y1="180" x2="212" y2="150" {S}/><line x1="256" y1="180" x2="256" y2="150" {S}/><line x1="300" y1="180" x2="300" y2="150" {S}/>'
    f'<line x1="212" y1="332" x2="212" y2="362" {S}/><line x1="256" y1="332" x2="256" y2="362" {S}/><line x1="300" y1="332" x2="300" y2="362" {S}/>'
    f'<line x1="180" y1="212" x2="150" y2="212" {S}/><line x1="180" y1="256" x2="150" y2="256" {S}/><line x1="180" y1="300" x2="150" y2="300" {S}/>'
    f'<line x1="332" y1="212" x2="362" y2="212" {S}/><line x1="332" y1="256" x2="362" y2="256" {S}/><line x1="332" y1="300" x2="362" y2="300" {S}/>',
"pulse": f'<polyline points="138,256 206,256 236,176 286,344 316,256 374,256" {S}/>',
"quantum": f'<circle cx="256" cy="256" r="16" {F}/>'
    f'<path d="M256 156 A60 150 0 1 0 256 356 A60 150 0 1 0 256 156" {ST}/>'
    f'<path d="M169 206 A60 150 60 1 0 343 306 A60 150 60 1 0 169 206" {ST}/>'
    f'<path d="M169 306 A60 150 -60 1 0 343 206 A60 150 -60 1 0 169 306" {ST}/>',
"sensor": f'<circle cx="256" cy="256" r="16" {F}/>'
    f'<path d="M306 206 A70 70 0 0 1 306 306" {S}/><path d="M340 172 A118 118 0 0 1 340 340" {ST}/>'
    f'<path d="M206 306 A70 70 0 0 1 206 206" {S}/>',
"sonar": f'<circle cx="256" cy="256" r="56" {ST}/><circle cx="256" cy="256" r="106" {ST}/>'
    f'<circle cx="256" cy="256" r="10" {F}/><line x1="256" y1="256" x2="340" y2="172" {S}/>',
"spore": f'<circle cx="256" cy="256" r="22" {S}/>'
    + "".join(f'<line x1="256" y1="256" x2="{256+int(96* __import__("math").cos(a))}" y2="{256+int(96* __import__("math").sin(a))}" {ST}/>'
              f'<circle cx="{256+int(112* __import__("math").cos(a))}" cy="{256+int(112* __import__("math").sin(a))}" r="8" {F}/>'
              for a in [i*0.5236 for i in range(12)]),
"telepathy": f'<path d="M256 150 C 206 150 186 192 196 226 C 176 240 186 280 214 280 L214 312 L298 312 L298 280 '
    f'C 326 280 336 240 316 226 C 326 192 306 150 256 150 Z" {S}/>'
    f'<path d="M150 200 A150 150 0 0 0 150 312" {ST}/><path d="M362 200 A150 150 0 0 1 362 312" {ST}/>',
"translation": f'<rect x="142" y="166" width="180" height="132" rx="24" {S}/><polyline points="196,298 196,338 240,298" {S}/>'
    f'<line x1="184" y1="206" x2="280" y2="206" {ST}/><line x1="184" y1="246" x2="248" y2="246" {ST}/>'
    f'<path d="M318 322 H392" {ST}/><path d="M355 300 V344" {ST}/>',
"virus": f'<circle cx="256" cy="256" r="78" {S}/>'
    + "".join(f'<line x1="{256+int(78* __import__("math").cos(a))}" y1="{256+int(78* __import__("math").sin(a))}" '
              f'x2="{256+int(118* __import__("math").cos(a))}" y2="{256+int(118* __import__("math").sin(a))}" {S}/>'
              f'<circle cx="{256+int(126* __import__("math").cos(a))}" cy="{256+int(126* __import__("math").sin(a))}" r="9" {F}/>'
              for a in [i*0.7854 for i in range(8)])
    + f'<circle cx="238" cy="248" r="9" {F}/><circle cx="278" cy="272" r="9" {F}/>',
"volume": f'<polygon points="170,216 210,216 258,176 258,336 210,296 170,296" {S}/>'
    f'<path d="M300 212 A70 70 0 0 1 300 300" {S}/><path d="M330 180 A116 116 0 0 1 330 332" {ST}/>',
"clock": f'<circle cx="256" cy="256" r="112" {S}/><line x1="256" y1="256" x2="256" y2="172" {S}/>'
    f'<line x1="256" y1="256" x2="318" y2="288" {S}/><circle cx="256" cy="256" r="12" {F}/>',
"vpn": f'<path d="M256 130 L362 172 V266 C362 330 314 368 256 390 C198 368 150 330 150 266 V172 Z" {S}/>'
    f'<circle cx="256" cy="248" r="26" {S}/><line x1="256" y1="274" x2="256" y2="312" {S}/>',
# ── Terminal-pack concepts (white monoline) ──
"ammobox": f'<rect x="156" y="216" width="200" height="156" rx="12" {S}/><rect x="178" y="184" width="156" height="34" rx="8" {S}/>'
    f'<line x1="214" y1="262" x2="214" y2="330" {ST}/><line x1="256" y1="262" x2="256" y2="330" {ST}/><line x1="298" y1="262" x2="298" y2="330" {ST}/>',
"archive": f'<rect x="150" y="156" width="212" height="48" rx="8" {S}/><path d="M170 204 V356 H342 V204" {S}/><line x1="222" y1="252" x2="290" y2="252" {S}/>',
"back": f'<line x1="346" y1="256" x2="174" y2="256" {S}/><polyline points="224,206 174,256 224,306" {S}/>',
"biohazard": f'<circle cx="256" cy="194" r="42" {S}/><circle cx="200" cy="306" r="42" {S}/><circle cx="312" cy="306" r="42" {S}/><circle cx="256" cy="270" r="18" {F}/>',
"canteen": f'<rect x="188" y="198" width="136" height="174" rx="42" {S}/><rect x="230" y="166" width="52" height="36" rx="6" {S}/><line x1="324" y1="250" x2="356" y2="250" {S}/>',
"chip_cpu": f'<rect x="186" y="186" width="140" height="140" rx="14" {S}/><rect x="222" y="222" width="68" height="68" {ST}/>'
    f'<line x1="218" y1="186" x2="218" y2="156" {S}/><line x1="294" y1="186" x2="294" y2="156" {S}/>'
    f'<line x1="218" y1="326" x2="218" y2="356" {S}/><line x1="294" y1="326" x2="294" y2="356" {S}/>'
    f'<line x1="186" y1="218" x2="156" y2="218" {S}/><line x1="186" y1="294" x2="156" y2="294" {S}/>'
    f'<line x1="326" y1="218" x2="356" y2="218" {S}/><line x1="326" y1="294" x2="356" y2="294" {S}/>',
"dashboard": f'<path d="M148 318 A114 114 0 0 1 364 318" {S}/><line x1="256" y1="318" x2="322" y2="246" {S}/><circle cx="256" cy="318" r="14" {F}/>',
"error": f'<circle cx="256" cy="256" r="116" {S}/><line x1="212" y1="212" x2="300" y2="300" {S}/><line x1="300" y1="212" x2="212" y2="300" {S}/>',
"explosion": f'<polygon points="256,134 290,210 366,196 318,260 380,300 300,306 314,382 256,326 198,382 212,306 132,300 194,260 146,196 222,210" {S}/>',
"fist": f'<rect x="186" y="222" width="156" height="124" rx="30" {S}/><line x1="218" y1="222" x2="218" y2="198" {S}/><line x1="256" y1="222" x2="256" y2="194" {S}/>'
    f'<line x1="294" y1="222" x2="294" y2="198" {S}/><path d="M186 268 H160 A18 18 0 0 0 160 304 H186" {S}/>',
"flashlight": f'<polygon points="210,158 302,158 286,216 226,216" {S}/><rect x="224" y="216" width="64" height="156" rx="8" {S}/><line x1="256" y1="118" x2="256" y2="146" {ST}/>',
"fullscreen": f'<polyline points="152,212 152,152 212,152" {S}/><polyline points="300,152 360,152 360,212" {S}/>'
    f'<polyline points="360,300 360,360 300,360" {S}/><polyline points="212,360 152,360 152,300" {S}/>',
"gear_cog": f'<circle cx="256" cy="256" r="60" {S}/><circle cx="256" cy="256" r="22" {ST}/>'
    + "".join(f'<line x1="{256+round(60*__import__("math").cos(a))}" y1="{256+round(60*__import__("math").sin(a))}" '
              f'x2="{256+round(98*__import__("math").cos(a))}" y2="{256+round(98*__import__("math").sin(a))}" '
              f'stroke="#FFFFFF" stroke-width="15" stroke-linecap="round"/>' for a in [i*0.7854 for i in range(8)]),
"google_maps": f'<path d="M256 148 C 202 148 164 190 164 242 C 164 312 256 384 256 384 C 256 384 348 312 348 242 C 348 190 310 148 256 148 Z" {S}/>'
    f'<circle cx="256" cy="238" r="34" {S}/>',
"helmet": f'<path d="M150 286 A108 108 0 0 1 366 286 Z" {S}/><line x1="150" y1="286" x2="366" y2="286" {S}/><rect x="300" y="250" width="60" height="36" rx="6" {S}/>',
"linechart": f'<path d="M158 138 V374 H394" {S}/><polyline points="186,322 246,250 300,284 372,188" {S}/>',
"maximize": f'<rect x="166" y="166" width="180" height="180" rx="14" {S}/><polyline points="264,200 312,200 312,248" {ST}/><polyline points="248,312 200,312 200,264" {ST}/>',
"medkit": f'<rect x="150" y="200" width="212" height="160" rx="20" {S}/><rect x="216" y="176" width="80" height="26" rx="6" {S}/>'
    f'<line x1="256" y1="240" x2="256" y2="320" {S}/><line x1="216" y1="280" x2="296" y2="280" {S}/>',
"minimize": f'<rect x="166" y="166" width="180" height="180" rx="14" {S}/><polyline points="200,264 248,264 248,312" {ST}/><polyline points="312,248 264,248 264,200" {ST}/>',
"package": f'<polygon points="256,148 360,206 360,330 256,388 152,330 152,206" {S}/><line x1="152" y1="206" x2="256" y2="264" {ST}/>'
    f'<line x1="360" y1="206" x2="256" y2="264" {ST}/><line x1="256" y1="264" x2="256" y2="388" {ST}/>',
"piechart": f'<circle cx="256" cy="256" r="112" {S}/><line x1="256" y1="256" x2="256" y2="144" {S}/><line x1="256" y1="256" x2="352" y2="300" {S}/>',
"power_nuclear": f'<path d="M204 198 A82 82 0 1 0 308 198" {S}/><line x1="256" y1="150" x2="256" y2="250" {S}/>',
"question": f'<path d="M210 214 A46 46 0 1 1 256 282 V304" {S}/><circle cx="256" cy="352" r="11" {F}/>',
"radar": f'<circle cx="256" cy="256" r="112" {S}/><circle cx="256" cy="256" r="62" {ST}/><line x1="256" y1="256" x2="342" y2="178" {S}/><circle cx="304" cy="298" r="9" {F}/>',
"radiation": f'<circle cx="256" cy="256" r="22" {F}/>'
    + "".join((lambda al, ar: f'<polygon points="{256+round(42*__import__("math").cos(al))},{256+round(42*__import__("math").sin(al))} '
              f'{256+round(106*__import__("math").cos(al))},{256+round(106*__import__("math").sin(al))} '
              f'{256+round(106*__import__("math").cos(ar))},{256+round(106*__import__("math").sin(ar))} '
              f'{256+round(42*__import__("math").cos(ar))},{256+round(42*__import__("math").sin(ar))}" {F}/>')(th-0.49, th+0.49)
              for th in [1.5708, 3.6652, 5.7596]),
"shield": f'<path d="M256 132 L360 172 V268 C360 330 314 366 256 388 C198 366 152 330 152 268 V172 Z" {S}/><polyline points="216,254 246,286 304,222" {S}/>',
"skull": f'<path d="M170 252 A86 92 0 0 1 342 252 V300 A30 30 0 0 1 312 330 H306 V362 H206 V330 H200 A30 30 0 0 1 170 300 Z" {S}/>'
    f'<circle cx="216" cy="260" r="22" {F}/><circle cx="296" cy="260" r="22" {F}/><line x1="240" y1="330" x2="240" y2="362" {ST}/><line x1="272" y1="330" x2="272" y2="362" {ST}/>',
"sort": f'<line x1="170" y1="196" x2="320" y2="196" {S}/><line x1="170" y1="256" x2="280" y2="256" {S}/><line x1="170" y1="316" x2="240" y2="316" {S}/>'
    f'<polyline points="330,278 358,316 386,278" {ST}/><line x1="358" y1="196" x2="358" y2="316" {ST}/>',
"success": f'<circle cx="256" cy="256" r="116" {S}/><polyline points="208,258 244,296 312,220" {S}/>',
"twitter_x": f'<line x1="166" y1="166" x2="346" y2="346" {S}/><line x1="346" y1="166" x2="166" y2="346" {S}/>',
"vault": f'<rect x="142" y="142" width="228" height="228" rx="20" {S}/><circle cx="256" cy="256" r="78" {S}/><circle cx="256" cy="256" r="14" {F}/>'
    f'<line x1="256" y1="178" x2="256" y2="148" {ST}/><line x1="256" y1="334" x2="256" y2="364" {ST}/><line x1="178" y1="256" x2="148" y2="256" {ST}/><line x1="334" y1="256" x2="364" y2="256" {ST}/>',
"warning": f'<path d="M256 152 L372 358 H140 Z" {S}/><line x1="256" y1="232" x2="256" y2="296" {S}/><circle cx="256" cy="330" r="9" {F}/>',
"wrench": f'<path d="M330 182 A56 56 0 1 0 300 280 L210 370 A28 28 0 0 1 170 330 L260 240 A56 56 0 0 1 330 182 Z" {S}/>',
"zoomin": f'<circle cx="232" cy="232" r="86" {S}/><line x1="294" y1="294" x2="364" y2="364" {S}/><line x1="232" y1="198" x2="232" y2="266" {ST}/><line x1="198" y1="232" x2="266" y2="232" {ST}/>',
"zoomout": f'<circle cx="232" cy="232" r="86" {S}/><line x1="294" y1="294" x2="364" y2="364" {S}/><line x1="198" y1="232" x2="266" y2="232" {ST}/>',
}

# ── concept → existing core drawable matching (same logic as analysis) ──
def is_core(stem):
    if stem.startswith(("xeno_","terminal_","circuitry_","sports_","nation_")):
        return False
    if "_v" in stem and stem.rsplit("_v",1)[-1].isdigit():
        return False
    return True

def build_match(prefix="xeno_"):
    core = {p.stem.removeprefix("ic_"): p.stem for p in DRAWABLE.glob("*.xml") if is_core(p.stem)}
    SYN = {"algorithm":"code","crypto":"blockchain","data_stream":"database","deep_learning":"neural",
           "deploy":"cloud_upload","encode":"code","encrypt":"lock","machine_learning":"neural",
           "memory_bank":"database","payment":"wallet","ping":"signal","receive":"download",
           "security":"shield","store":"shop","sync":"refresh","transmit":"upload","unlock":"lock",
           "vpn":"shield","chart_up":"analytics","memory":"database",
           "barchart":"analytics","google_maps":"map","twitter_x":"x_twitter"}
    match = {}
    for p in sorted(DRAWABLE.glob(f"{prefix}*.xml")):
        c = p.stem[len(prefix):]
        if c in GLYPHS:
            continue  # hand-authored
        for cand in (c, c.replace("_",""), c.split("_")[0], SYN.get(c,"")):
            if cand and cand in core:
                match[c] = core[cand]; break
    return match

def main(prefix="xeno_", master_dir=MASTER_XENO):
    match = build_match(prefix)
    real = {p.stem[len(prefix):] for p in DRAWABLE.glob(f"{prefix}*.xml")}
    missing = [c for c in sorted(real) if c not in match and c not in GLYPHS]

    n_auth = n_match = 0
    # 1. authored glyphs (only those that are real icons in this pack)
    for c, body in GLYPHS.items():
        if c not in real:
            continue
        paths = convert_svg_body(body)
        if not paths:
            print(f"  !! no paths for authored {c}"); continue
        xml = wrap_xml(paths)
        (DRAWABLE / f"{prefix}{c}.xml").write_text(xml, encoding="utf-8")
        (NODPI / f"{prefix}{c}.xml").write_text(xml, encoding="utf-8")
        (master_dir / f"{prefix}{c}.svg").write_text(wrap_svg(body), encoding="utf-8")
        n_auth += 1
    # 2. recoloured core glyphs
    for c, src in match.items():
        src_file = DRAWABLE / f"{src}.xml"
        if not src_file.exists():
            print(f"  !! source missing {src} for {prefix}{c}"); continue
        xml = recolor_drawable(src_file.read_text(encoding="utf-8"))
        (DRAWABLE / f"{prefix}{c}.xml").write_text(xml, encoding="utf-8")
        (NODPI / f"{prefix}{c}.xml").write_text(xml, encoding="utf-8")
        n_match += 1

    print(f"[{prefix}] authored white glyphs: {n_auth}")
    print(f"[{prefix}] recoloured core glyphs: {n_match}")
    print(f"[{prefix}] total regenerated: {n_auth + n_match} / {len(real)}")
    if missing:
        print(f"[{prefix}] UNHANDLED ({len(missing)}): {missing}")

if __name__ == "__main__":
    main()
