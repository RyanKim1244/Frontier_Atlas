# Lesson figures: {"type": "figure", "engine": "asy" | "tikz" | "plot", "code": "...", "caption": "...", "alt": "...", "src": [...]}
# Compiled once to SVG and cached by content hash in pipeline/figs/ (committed), so CI needs no TeX or Asymptote.
import hashlib, os, re, shutil, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", "figs")

TIKZ = r"""\documentclass[tikz,border=4pt]{standalone}
\usepackage{amsmath,amssymb,tikz-cd,pgfplots}\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,calc,decorations.markings,decorations.pathmorphing,patterns,positioning,shapes}
\tikzcdset{labels={font=\small}, arrow style=tikz, diagrams={>={Stealth[length=5pt]}}}
\tikzset{every picture/.append style={line width=0.6pt}}
\begin{document}
%s
\end{document}
"""

STYLE = "v2"  # bump when the preamble or plot style changes, so every figure is rebuilt

def key(b):
    return hashlib.sha256((STYLE + b["engine"] + "\0" + b["code"]).encode()).hexdigest()[:16]

def compile_svg(engine, code, out_svg, png=None):
    with tempfile.TemporaryDirectory() as d:
        run = lambda *a: subprocess.run(a, cwd=d, check=True, capture_output=True, timeout=120)
        if engine == "asy":
            open(os.path.join(d, "f.asy"), "w").write(code)
            run("asy", "-noV", "-f", "pdf", "f.asy")
        elif engine == "tikz":
            open(os.path.join(d, "f.tex"), "w").write(TIKZ % code)
            run("pdflatex", "-interaction=nonstopmode", "-halt-on-error", "f.tex")
        elif engine == "plot":
            # code: matplotlib script that draws on the current figure; we save it.
            prog = ("import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\n"
                    "plt.rcParams.update({'font.size': 11, 'mathtext.fontset': 'cm', 'lines.linewidth': 1.6, 'axes.linewidth': 0.9, 'font.family': 'serif', 'font.serif': ['cmr10', 'DejaVu Serif'], 'axes.formatter.use_mathtext': True, 'axes.unicode_minus': False})\n"
                    + code + "\nplt.savefig('f.pdf', bbox_inches='tight', transparent=True)\n")
            open(os.path.join(d, "f.py"), "w").write(prog)
            run("python3", "-I", "f.py")
        else:
            raise ValueError("unknown figure engine " + engine)
        run("pdftocairo", "-svg", "f.pdf", "f.svg")
        shutil.copy(os.path.join(d, "f.svg"), out_svg)
        if png:
            run("pdftocairo", "-png", "-r", "150", "-singlefile", "f.pdf", "p")
            shutil.copy(os.path.join(d, "p.png"), png)

SCALE = 1.6   # displayed size relative to the TeX point size, so 10pt labels read like body text
MIN_STROKE = 0.75
_rgb = re.compile(r'rgb\(([\d.]+)%,\s*([\d.]+)%,\s*([\d.]+)%\)')

def _themed(c):
    """Map a fixed colour to the site's theme colours (light and dark), keeping its tint."""
    m = _rgb.fullmatch(c.strip())
    if not m: return None
    r, g, b = (float(x) / 100 for x in m.groups())
    mx, mn = max(r, g, b), min(r, g, b)
    if mx - mn < 0.08:   # greys: black is ink, white is paper
        return "color-mix(in srgb, var(--ink) %d%%, var(--paper))" % round((1 - mx) * 100)
    d = mx - mn
    h = (60 * ((g - b) / d % 6) if mx == r else 60 * ((b - r) / d + 2) if mx == g else 60 * ((r - g) / d + 4))
    name = "red" if h < 15 or h >= 340 else "orange" if h < 65 else "green" if h < 170 else "blue" if h < 255 else "purple"
    return "color-mix(in srgb, var(--fig-%s) %d%%, var(--paper))" % (name, max(18, round((1 - mn) * 100)))

def themed_svg(svg, k):
    """Prefix ids (several figures share one page), move colours into theme classes, thicken hairlines, set display size."""
    svg = re.sub(r'<\?xml[^>]*>\s*', "", svg)
    svg = re.sub(r'id="([^"]+)"', lambda m: 'id="f%s-%s"' % (k, m.group(1)), svg)
    svg = re.sub(r'(xlink:href|href)="#([^"]+)"', lambda m: '%s="#f%s-%s"' % (m.group(1), k, m.group(2)), svg)
    svg = re.sub(r'url\(#([^)]+)\)', lambda m: 'url(#f%s-%s)' % (k, m.group(1)), svg)
    classes = {}
    def tag(m):
        t = m.group(0); cls = []
        for prop in ("fill", "stroke"):
            a = re.search(r'\s%s="(rgb\([^"]+\))"' % prop, t)
            if a:
                val = _themed(a.group(1))
                if val:
                    cn = classes.setdefault((prop, val), "f%s-%s%d" % (k, prop[0], len(classes)))
                    cls.append(cn)
        sw = re.search(r'stroke-width="([\d.]+)"', t)
        if sw and float(sw.group(1)) < MIN_STROKE:
            t = t.replace(sw.group(0), 'stroke-width="%g"' % MIN_STROKE)
        if cls: t = t[:-1].rstrip("/") + ' class="%s"' % " ".join(cls) + ("/>" if t.endswith("/>") else ">")
        return t
    svg = re.sub(r'<(path|rect|circle|ellipse|line|polyline|polygon|use|g)\b[^>]*>', tag, svg)
    style = "".join(".%s{%s:%s}" % (cn, prop, val) for (prop, val), cn in classes.items())
    m = re.search(r'<svg\b[^>]*\bwidth="([\d.]+)(?:pt)?"[^>]*\bheight="([\d.]+)(?:pt)?"', svg)
    w, hgt = float(m.group(1)), float(m.group(2))
    svg = re.sub(r'(<svg\b[^>]*?)\swidth="[^"]*"\s+height="[^"]*"', lambda mm: '%s width="%d" height="%d"' % (mm.group(1), round(w * SCALE), round(hgt * SCALE)), svg, count=1)
    svg = re.sub(r'(<svg\b[^>]*>)', lambda mm: mm.group(1) + "<style>" + style + "</style>", svg, count=1)
    return svg

def render(b, OUT):
    k = key(b); os.makedirs(CACHE, exist_ok=True)
    cached = os.path.join(CACHE, k + ".svg")
    if not os.path.exists(cached):
        compile_svg(b["engine"], b["code"], cached)  # fails loudly in CI if a figure was not built and committed
    dst = os.path.join(OUT, "data", "fig"); os.makedirs(dst, exist_ok=True)
    open(os.path.join(dst, k + ".svg"), "w").write(themed_svg(open(cached).read(), k[:6]))
    return {k2: v for k2, v in b.items() if k2 != "code"} | {"svg": "data/fig/" + k + ".svg"}
