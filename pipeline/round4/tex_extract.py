"""Extract exercise STATEMENTS (never answers) from Jiří Lebl's LaTeX books (dual CC BY-NC-SA / CC BY-SA 4.0;
we use them under CC BY-SA 4.0). Output: list of {book, chapter, section, section_title, n, q} with the book's own
numbering (exercise counter is per section and shared by in-text and end-of-section exercises).

Exercises that refer to other parts of the book (\\ref, "previous exercise", figures, tables) are skipped, because
they do not stand on their own."""
import re, json, sys

def strip_comments(t):
    return re.sub(r'(?<!\\)%.*', '', t)

def arg(t, i):
    """t[i] == '{' -> (content, index after closing brace)."""
    assert t[i] == '{', t[i:i + 20]
    d = 0
    for j in range(i, len(t)):
        if t[j] == '\\': continue
        if t[j] == '{' and (j == 0 or t[j - 1] != '\\'): d += 1
        elif t[j] == '}' and t[j - 1] != '\\':
            d -= 1
            if d == 0: return t[i + 1:j], j + 1
    raise ValueError("unbalanced")

def parse_macros(text):
    M = {}
    text = strip_comments(text)
    for m in re.finditer(r'\\(?:re)?newcommand\*?\s*\{?\\([A-Za-z]+)\}?', text):
        name, i = m.group(1), m.end()
        n, default = 0, None
        try:
            while text[i] in ' \t': i += 1
            if text[i] == '[':
                j = text.index(']', i); n = int(text[i + 1:j]); i = j + 1
                if text[i] == '[':
                    j = text.index(']', i); default = text[i + 1:j]; i = j + 1
            while text[i] in ' \t\n': i += 1
            body, _ = arg(text, i)
        except Exception:
            continue
        M[name] = (n, default, body)
    for m in re.finditer(r'\\DeclareMathOperator\*?\{\\([A-Za-z]+)\}\{([^}]*)\}', text):
        M[m.group(1)] = (0, None, r'\operatorname{' + m.group(2) + '}')
    return M

KEEP = set("""R C Z N Q Re Im""".split())  # defined in the site's MathJax config too; expanding is still fine

def expand(t, M, depth=0):
    if depth > 8: return t
    out, i = [], 0
    pat = re.compile(r'\\([A-Za-z]+)')
    while True:
        m = pat.search(t, i)
        if not m: out.append(t[i:]); break
        name = m.group(1)
        if name not in M:
            out.append(t[i:m.end()]); i = m.end(); continue
        n, default, body = M[name]
        out.append(t[i:m.start()]); j = m.end()
        args = []
        if default is not None:
            if j < len(t) and t[j] == '[':
                k = t.index(']', j); args.append(t[j + 1:k]); j = k + 1
            else: args.append(default)
        while len(args) < n:
            while j < len(t) and t[j] in ' \n': j += 1
            if j < len(t) and t[j] == '{':
                a, j = arg(t, j); args.append(a)
            elif j < len(t):
                args.append(t[j]); j += 1
            else: break
        b = body
        for k, a in enumerate(args, 1): b = b.replace('#' + str(k), a)
        # keep a space after control words so "\R x" does not glue
        nxt = t[j:j + 1]
        out.append(expand(b, M, depth + 1) + (' ' if nxt.isalpha() and b and b[-1].isalpha() else ''))
        i = j
    return ''.join(out)

SKIP = re.compile(r'\\(propref|corref|lemmaref|defnref|hyperref|hyperlink|ref|eqref|thmref|thmvref|exerciseref|exercisevref|exampleref|examplevref|chapterref|Chapterref|sectionref|subsectionref|figureref|figurevref|tableref|tablevref|remarkref|appendixref|cite|href|url|includegraphics|myincludegraphics|diffyincludegraphics|inputpdft|myincludepdft|footnote)\b'
                  r'|\\begin\{(tabular|figure|table|tikzpicture|myfig|mywrapfig|mywrapfigsimp|minipage|tikzcd|center)\}'
                  r'|previous exercise|preceding exercise|next exercise|exercise above|above exercise|following exercise|in the text|this section|this chapter|the example|in the example|last exercise|those exercises|earlier exercise', re.I)

DISPLAY = ['equation*', 'equation', 'align*', 'align', 'multline*', 'gather*', 'displaymath']

def convert(q):
    q = re.sub(r'\\label\{[^}]*\}', '', q)
    q = re.sub(r'\\glsadd\{[^}]*\}', '', q)
    q = re.sub(r'\\hspace\*?\{[^}]*\}', ' ', q)
    q = re.sub(r'\\(leavevmode|fill|hfill)\b', '', q)
    q = re.sub(r'\\index\{[^}]*\}', '', q)
    q = re.sub(r'\\(medskip|smallskip|bigskip|noindent|par|avoidbreak|nopagebreak|pagebreak|newline|linebreak|allowbreak|break)\b(\[\d\])?', ' ', q)
    q = re.sub(r'\\coloneqq\b', ':=', q)
    q = re.sub(r'\\eqqcolon\b', '=:', q)
    q = re.sub(r'\\nicefrac\{([^{}]*)\}\{([^{}]*)\}', r'{\1}/{\2}', q)
    q = re.sub(r'\\(enspace|quad|qquad)\b', ' ', q) if False else q
    q = q.replace('\\\\\n', '\\\\ \n')
    # display math
    for env in DISPLAY:
        e = re.escape(env)
        rep = (lambda m: '\n\n$$\\begin{aligned}' + m.group(1).strip() + '\\end{aligned}$$\n\n') if env.startswith(('align', 'gather')) else (lambda m: '\n\n$$' + m.group(1).strip() + '$$\n\n')
        q = re.sub(r'\\begin\{' + e + r'\}(.*?)\\end\{' + e + r'\}', rep, q, flags=re.S)
    q = re.sub(r'\\\[(.*?)\\\]', lambda m: '\n\n$$' + m.group(1).strip() + '$$\n\n', q, flags=re.S)
    q = re.sub(r'\\begin\{split\}', r'\\begin{aligned}', q); q = re.sub(r'\\end\{split\}', r'\\end{aligned}', q)
    # lists: enumerate / itemize / tasks / exparts -> labelled paragraphs
    def lists(q):
        for env in ('enumerate', 'itemize', 'tasks', 'exparts'):
            m = re.search(r'\\begin\{' + env + r'\}(\[[^\]]*\])?(\([^)]*\))?(.*?)\\end\{' + env + r'\}', q, flags=re.S)
            while m:
                body = m.group(3)
                parts = [p.strip() for p in re.split(r'\\(?:item|task)\b(?:\[[^\]]*\])?', body)[1:]]
                if env == 'itemize': lines = ['- ' + p for p in parts]
                else: lines = ['(' + 'abcdefghijklmnopqrstuvwxyz'[k] + ') ' + p for k, p in enumerate(parts)]
                q = q[:m.start()] + '\n\n' + '\n\n'.join(lines) + '\n\n' + q[m.end():]
                m = re.search(r'\\begin\{' + env + r'\}(\[[^\]]*\])?(\([^)]*\))?(.*?)\\end\{' + env + r'\}', q, flags=re.S)
        return q
    q = lists(q)
    # units package
    q = re.sub(r'\\unitfrac\[([^\]]*)\]\{([^}]*)\}\{([^}]*)\}', r'\1 \2/\3', q)
    q = re.sub(r'\\unitfrac\{([^}]*)\}\{([^}]*)\}', r'\1/\2', q)
    q = re.sub(r'\\unit\[([^\]]*)\]\{([^}]*)\}', r'\1 \2', q)
    q = re.sub(r'\\unit\{([^}]*)\}', r'\1', q)
    # text formatting (outside math these become plain text)
    for cmd in ('emph', 'textit', 'textbf', 'textsl', 'textrm', 'textsf', 'texttt', 'myquote', 'mbox'):
        while True:
            m = re.search(r'\\' + cmd + r'\{', q)
            if not m: break
            a, j = arg(q, m.end() - 1)
            q = q[:m.start()] + (('“' + a + '”') if cmd == 'myquote' else a) + q[j:]
    def text_only(seg):
        seg = seg.replace('``', '“').replace("''", '”').replace('---', '—').replace('--', '–')
        seg = re.sub(r'(?<!\\)~', ' ', seg).replace('\\ldots', '…').replace('\\dots', '…')
        seg = re.sub(r'\\(enspace|quad|qquad)\b', ' ', seg)
        return seg
    pieces = re.split(r'(\$\$.*?\$\$|\$[^$]*\$)', q, flags=re.S)
    q = ''.join(p if i % 2 else text_only(p) for i, p in enumerate(pieces))
    q = re.sub(r'[ \t]+', ' ', q)
    q = re.sub(r' *\n *', '\n', q)
    q = re.sub(r'\n{3,}', '\n\n', q)
    # punctuation after display math goes inside it
    q = re.sub(r'\$\$\s*\n\n\s*([.,;:])', r'\1$$\n\n', q)
    q = re.sub(r'\$\$([.,;:])', r'\1$$', q)
    q = re.sub(r'\\postdisplaypenalty\s*=\s*\d+', '', q)
    q = re.sub(r'\\widebar\b', r'\\overline', q)
    # no blank lines inside display math (they would split the paragraph)
    q = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + re.sub(r'\s*\n\s*\n\s*', ' ', m.group(1)) + '$$', q, flags=re.S)
    # a forced line break in text becomes a paragraph break
    pieces = re.split(r'(\$\$.*?\$\$|\$[^$]*\$)', q, flags=re.S)
    q = ''.join(p if i % 2 else p.replace('\\\\', '\n\n') for i, p in enumerate(pieces))
    # single newlines inside a paragraph are spaces (except list lines)
    paras = []
    for p in q.strip().split('\n\n'):
        paras.append(re.sub(r'\n', ' ', p))
    return '\n\n'.join(x.strip() for x in paras if x.strip())

TEXT_OK = set('emph item task'.split())
def leftover_text_macros(q):
    """Control words outside math that the site cannot render."""
    outside = re.sub(r'\$\$.*?\$\$|\$[^$]*\$', ' ', q, flags=re.S)
    return sorted(set(re.findall(r'\\([A-Za-z]+)', outside)))

def extract(book, folder, files, preambles):
    M = {}
    for p in preambles: M.update(parse_macros(open(p).read()))
    for k in list(M):  # never expand reference/figure macros: they must stay visible to SKIP
        if k.endswith(('ref', 'vref')) or 'includegraphics' in k or k in ('myquote', 'ignore'):
            if k == 'ignore': M[k] = (1, None, '')
            elif k != 'myquote': del M[k]
    out, skipped = [], []
    for f, ch in files:
        t = strip_comments(open(folder + '/' + f).read())
        sec, n, title = 0, 0, ''
        pos = 0
        for m in re.finditer(r'\\section\{|\\begin\{exercise\}(\[[^\]]*\])?', t):
            if m.group(0).startswith('\\section'):
                title, _ = arg(t, m.end() - 1); sec += 1; n = 0; continue
            n += 1
            end = t.index('\\end{exercise}', m.end())
            raw = t[m.end():end]
            raw = re.sub(r'\\exsol\{', r'\\ignore{', raw)
            ident = dict(book=book, chapter=ch, section=f'{ch}.{sec}', section_title=re.sub(r'\\texorpdfstring\{.*', '', title).strip(), n=n)
            if SKIP.search(raw):
                skipped.append(dict(ident, why='reference/figure')); continue
            q = convert(expand(raw, M))
            bad = leftover_text_macros(q)
            if bad:
                skipped.append(dict(ident, why='macros ' + ','.join(bad))); continue
            if q.count('$') % 2 or len(q) < 15:
                skipped.append(dict(ident, why='unbalanced/short')); continue
            out.append(dict(ident, q=q))
    return out, skipped

if __name__ == '__main__':
    base = sys.argv[1]
    BA = [("ch-vol1-intro.tex", 0), ("ch-real-nums.tex", 1), ("ch-seq-ser.tex", 2), ("ch-contfunc.tex", 3), ("ch-der.tex", 4), ("ch-riemann.tex", 5),
          ("ch-seq-funcs.tex", 6), ("ch-metric.tex", 7), ("ch-several-vars-ders.tex", 8), ("ch-one-dim-ints-sv.tex", 9), ("ch-multivar-int.tex", 10), ("ch-approximate.tex", 11)]
    DQ = [("ch-intro.tex", 0), ("ch-first-order-ode.tex", 1), ("ch-higher-order-ode.tex", 2), ("ch-systems.tex", 3), ("ch-fourier-and-pde.tex", 4),
          ("ch-eigenvalue-probs.tex", 5), ("ch-laplace.tex", 6), ("ch-power-ser.tex", 7), ("ch-nonlin-systems.tex", 8)]
    ra = base + '/jirilebl_ra'; dq = base + '/jirilebl_diffyqs'
    a, sa = extract('BA', ra, BA, [ra + '/realanal.tex', ra + '/realanal2.tex'])
    b, sb = extract('DQ', dq, DQ, [dq + '/diffyqssetup.sty', dq + '/diffyqs.tex'])
    json.dump(a + b, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
    json.dump(sa + sb, open(sys.argv[2].replace('.json', '_skipped.json'), 'w'), ensure_ascii=False, indent=1)
    print('BA', len(a), 'skipped', len(sa), '| DQ', len(b), 'skipped', len(sb))
    from collections import Counter
    print(Counter(s['why'].split(' ')[0] for s in sa + sb))
    print(Counter(w for s in sa + sb if s['why'].startswith('macros') for w in s['why'][7:].split(',')).most_common(25))
