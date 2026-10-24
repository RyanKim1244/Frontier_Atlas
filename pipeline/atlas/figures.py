# Lesson figures: {"type": "figure", "engine": "asy" | "tikz" | "plot", "code": "...", "caption": "...", "alt": "...", "src": [...]}
# Compiled once to SVG and cached by content hash in pipeline/figs/ (committed), so CI needs no TeX or Asymptote.
import hashlib, os, shutil, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "..", "figs")

TIKZ = r"""\documentclass[tikz,border=4pt]{standalone}
\usepackage{amsmath,amssymb,tikz-cd,pgfplots}\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,calc,decorations.markings,decorations.pathmorphing,patterns,positioning,shapes}
\begin{document}
%s
\end{document}
"""

def key(b):
    return hashlib.sha256((b["engine"] + "\0" + b["code"]).encode()).hexdigest()[:16]

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
            prog = "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nplt.rcParams.update({'font.size': 11, 'mathtext.fontset': 'cm'})\n" + code + "\nplt.savefig('f.pdf', bbox_inches='tight')\n"
            open(os.path.join(d, "f.py"), "w").write(prog)
            run("python3", "-I", "f.py")
        else:
            raise ValueError("unknown figure engine " + engine)
        run("pdftocairo", "-svg", "f.pdf", "f.svg")
        shutil.copy(os.path.join(d, "f.svg"), out_svg)
        if png:
            run("pdftocairo", "-png", "-r", "150", "-singlefile", "f.pdf", "p")
            shutil.copy(os.path.join(d, "p.png"), png)

def render(b, OUT):
    k = key(b); os.makedirs(CACHE, exist_ok=True)
    cached = os.path.join(CACHE, k + ".svg")
    if not os.path.exists(cached):
        compile_svg(b["engine"], b["code"], cached)  # fails loudly in CI if a figure was not built and committed
    dst = os.path.join(OUT, "data", "fig"); os.makedirs(dst, exist_ok=True)
    shutil.copy(cached, os.path.join(dst, k + ".svg"))
    return {k2: v for k2, v in b.items() if k2 != "code"} | {"svg": "data/fig/" + k + ".svg"}
