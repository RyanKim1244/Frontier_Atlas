"""Extract end-of-section exercises (statements only) from PreTeXt sources into the Atlas text format."""
import re, json, sys, os, glob
import xml.etree.ElementTree as ET
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")

def macros_from(path):
    s = open(path, encoding="utf8").read()
    m = re.search(r"<macros>(.*?)</macros>", s, re.S)
    defs = {}
    if not m: return defs
    body = m.group(1).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    for mm in re.finditer(r"\\(?:re)?newcommand\{\\([A-Za-z]+)\}(?:\[(\d)\])?\{", body):
        i = mm.end(); depth = 1
        while depth and i < len(body):
            depth += {"{": 1, "}": -1}.get(body[i], 0); i += 1
        defs[mm.group(1)] = (int(mm.group(2) or 0), body[mm.end():i - 1])
    return defs

def read_arg(s, i):
    while i < len(s) and s[i] == " ": i += 1
    if i < len(s) and s[i] == "{":
        depth, j = 1, i + 1
        while depth and j < len(s):
            depth += {"{": 1, "}": -1}.get(s[j], 0); j += 1
        return s[i + 1:j - 1], j
    return (s[i], i + 1) if i < len(s) else ("", i)

def expand(tex, defs, depth=0):
    if depth > 6: return tex
    out, i = [], 0
    pat = re.compile(r"\\([A-Za-z]+)")
    while True:
        m = pat.search(tex, i)
        if not m: out.append(tex[i:]); break
        out.append(tex[i:m.start()])
        name = m.group(1)
        if name in defs:
            n, body = defs[name]; j = m.end(); args = []
            for _ in range(n): a, j = read_arg(tex, j); args.append(a)
            for k, a in enumerate(args, 1): body = body.replace("#" + str(k), a)
            out.append("{" + expand(body, defs, depth + 1) + "}"); i = j
        else:
            out.append(m.group(0)); i = m.end()
    return "".join(out).replace("\\amp", "&")

SKIP = {"image", "figure", "sidebyside", "tabular", "xref", "webwork", "program", "latex-image", "datafile", "interactive", "video", "url", "table", "listing", "console"}
class Skip(Exception): pass
def text(el, defs, lab=""):
    parts = []
    def inline(e):
        t = e.tag
        if t in SKIP: raise Skip(t)
        if t == "sage":
            inp = e.find("input")
            if inp is not None and (inp.text or "").strip(): raise Skip("sage")
            return ""
        if t == "m": return "$" + expand(e.text or "", defs).strip() + "$"
        if t in ("me", "men"): return "\n\n$$" + expand(e.text or "", defs).strip() + "$$\n\n"
        if t in ("md", "mdn"):
            rows = [expand("".join(r.itertext()), defs).strip() for r in e.findall("mrow")] or [expand(e.text or "", defs).strip()]
            return "\n\n$$\\begin{aligned}" + " \\\\ ".join(rows) + "\\end{aligned}$$\n\n" if len(rows) > 1 else "\n\n$$" + rows[0] + "$$\n\n"
        if t in ("ol", "ul"):
            out = []
            marker = e.get("marker", "a." if t == "ol" else "-")
            for k, li in enumerate(e.findall("li")):
                lab2 = ("-" if t == "ul" else label(marker, k))
                out.append("\n\n" + lab2 + " " + inner(li).strip())
            return "".join(out) + "\n\n"
        if t == "q": return "“" + inner(e) + "”"
        if t == "c": return inner(e)
        if t in ("ellipsis",): return "…" + (e.tail or "")
        simple = {"ie": "i.e.", "eg": "e.g.", "etc": "etc.", "nbsp": " ", "mdash": "—", "ndash": "–", "lsq": "‘", "rsq": "’", "lq": "“", "rq": "”", "copyright": "©", "times": "×"}
        if t in simple: return simple[t]
        if t == "p": return "\n\n" + inner(e).strip() + "\n\n"
        return inner(e)
    def inner(e):
        s = e.text or ""
        for ch in e:
            s += inline(ch) + (ch.tail or "")
        return s
    return inline(el)
def label(marker, k):
    if marker.startswith("1"): return f"{k + 1}."
    if marker.startswith("i"): return ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"][k % 10] + "."
    if marker.startswith("A"): return chr(65 + k) + "."
    return f"({chr(97 + k)})"

def exercise_text(ex, defs):
    st = ex.find("statement")
    chunks = []
    if st is not None: chunks.append(text(st, defs))
    else:
        for ch in ex:
            if ch.tag in ("hint", "answer", "solution", "title", "task"): continue
            chunks.append(text(ch, defs))
    tasks = ex.findall("task")
    for k, tk in enumerate(tasks):
        tst = tk.find("statement")
        chunks.append("\n\n" + label("a.", k) + " " + (text(tst, defs) if tst is not None else "".join(text(c, defs) for c in tk if c.tag not in ("hint", "answer", "solution"))).strip())
    s = "".join(chunks)
    s = re.sub(r"[ \t]*\n[ \t]*", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"(?<!\n)\n(?!\n)", " ", s)
    s = re.sub(r"[ \t]{2,}", " ", s).strip()
    s = re.sub(r"\$\$\s*\n\n\s*([.,;:])", r"\1$$\n\n", s)
    s = re.sub(r"\$\$([.,;:])", r"\1$$", s)
    return s

def parse_file(path):
    raw = open(path, encoding="utf8").read()
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    raw = re.sub(r'xmlns(:\w+)?="[^"]*"', "", raw)
    raw = re.sub(r"<(/?)xi:", r"<\1xi_", raw)
    raw = raw.replace("&nbsp;", " ")
    return ET.fromstring(raw)

def extract(files_concepts, defs, book, coll, link):
    out, skipped = [], {}
    for rel, concepts, sec in files_concepts:
        path = rel
        root = parse_file(path)
        for k, ex in enumerate(root.iter("exercise"), 1):
            try:
                q = exercise_text(ex, defs)
            except Skip as e:
                skipped[str(e)] = skipped.get(str(e), 0) + 1; continue
            if len(q) < 25: continue
            out.append(dict(book=book, coll=coll, sec=sec, num=k, q=q, concepts=concepts, link=link))
    return out, skipped
