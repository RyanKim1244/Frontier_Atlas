# Concept page, depth standard (round 5): entry + source-composed lesson

Folder: /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P2
Inputs per concept: brief.json, dossier_<id>.json (research already done), all_concepts.json (valid [[link]] ids),
field_ids.json, and the published lessons of the prerequisites at /home/claude/frontier_atlas/site/data/lessons/<id>.json
(what the reader already knows; reuse their notation).

## The goal
The page exists so a reader can LEARN the concept thoroughly, on their own, from the page: understand it, be able to use it,
and then read research papers that use it without being stopped. Learning comes first; the papers fix how far it must go.
The page is composed from the sources in the dossier, not from the writer's own taste: each explanation follows a named
source, and where sources explain the same thing differently, the page shows the different explanations side by side.

## Learning design (applies to every section)
- Order inside a section: why we need it (a question or a small example that the reader can work through) -> the
  definition -> examples and non-examples -> the theorem -> proof -> a worked computation -> self-check -> exercises.
  Concrete before abstract; small cases before general ones.
- Start each section by naming what the reader will be able to do after it (one sentence, in the section body).
- Recall a prerequisite in one line with a [[link]] at the moment it is used, not at the top of the page.
- Proofs: before a long proof, say its idea in one or two sentences; then the full proof in steps.
- Worked examples (type example) show every step a learner would need; they are the main teaching tool, not decoration.
- Self-check (type check): 2-4 quick questions right after a definition or theorem, each with a short answer the reader
  reveals (catches misunderstanding immediately).
- Exercises (type exercise): ordered from routine to hard (no labels shown); every item has a hint and a full solution the reader reveals.
  Learning without solutions stalls; solutions must be complete and correct (checked like everything else).
- End of each major section: a short summary of what to remember (type summary, 3-6 lines).
- Pitfalls where learners actually go wrong (from the dossier's confusions).
- No padding: every paragraph must teach something; no restating, no hype.

## Output schema
JSON array, one object per concept: {"id", "entry", "lesson"}.
- entry: {"sum", "key", "why", "msc", "links", "refs", "aliases"} exactly as before:
  sum 2-3 sentences ($TeX$ allowed); key 1-3 TeX statements without $; why 1-2 sentences; msc codes only if sure;
  links 1-3 {"field","note"} to fields NOT among the concept's own fields (ids from field_ids.json); refs real textbooks; aliases.
- lesson: {"v": 2, "minutes", "sources", "requires", "blocks", "checks"}

### sources
[{"k": "short-key", "ref": "Author, Title (year)", "where": "ch./§ if sure", "url": "only a URL you opened", "kind": "textbook" | "notes" | "paper" | "survey" | "Q&A" | "reference" | "blog"}]
Include every source the page follows (from the dossier), and the dossier's papers with kind "paper".

### requires
The dossier's requirements, after merging: [{"item": "text, may use $TeX$ and [[links]]", "priority": "core" | "common" | "specialised", "where": "section title on this page, or [[id]] of another page"}].
Every core and common item must be taught on this page (or on an existing page you link). Specialised items: teach if
reasonable, else give where: "not covered here; see [n]" naming a source key.

### blocks
Types from before: intro, section (title), definition (title), theorem (title), proof, example (body + solution),
pitfall, connection. Learning types:
- exercise: {"type": "exercise", "title": "optional", "items": [{"q": "...", "hint": "...", "solution": "..."}]}
  (every item has hint and solution; items ordered from easiest to hardest; no difficulty labels)
- check: {"type": "check", "items": [{"q": "...", "a": "short answer, one or two sentences"}]}
- summary: {"type": "summary", "body": "3-6 lines: what to remember"}
Other types:
- views: {"type": "views", "title": "...", "body": "optional lead-in", "items": [{"label": "2-4 words, e.g. 'Fractions', 'Universal property', 'Geometric'", "body": "...", "src": ["k"]}]}
  Different explanations of ONE thing (a definition, a theorem, a construction). 2-5 items, each from a different source
  or tradition. Use for every central notion of the page.
- conventions: {"type": "conventions", "title": "...", "body": "optional", "rows": [{"who": "source or tradition", "text": "its convention", "src": ["k"]}]}
  Wherever the dossier found sources disagree on signs, indexing, notation or normalisation.
- figure: {"type": "figure", "engine": "asy" | "tikz" | "plot", "code": "...", "caption": "...", "alt": "text description", "src": ["k"]}
  asy: Asymptote source (use `import geometry;` etc., never `olympiad`). tikz: the body of a standalone document
  (\begin{tikzpicture}...\end{tikzpicture} or \begin{tikzcd}...\end{tikzcd}; packages tikz-cd, pgfplots, amsmath available).
  plot: a matplotlib script drawing on the current figure (plt is imported; do not call savefig). Figure style (the site recolours figures for light and dark themes and shows them at 1.6x their TeX size):
  - Colours: black for the main drawing; for emphasis only pure-ish red, blue, green, orange, purple (any shade; light tints
    are fine for filled regions). They are mapped to theme colours. Never rely on colour alone: also label or dash.
  - No background fills behind the whole figure; no white boxes.
  - Natural size 7-12 cm wide (asy size(9cm) etc.); labels at normal text size (asy default, tikz \normalsize; tikz-cd arrow
    labels are already \small); lines at least 0.6pt.
  - Look at both renderings before finishing: figtest.py writes PNGs to figpng/.
  Use figures where a
  picture genuinely helps (commutative diagrams, exact sequences as diagrams, geometric pictures). Test-compile each one:
  python3 -I /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P2/figtest.py draft.json
  which writes PNGs to figpng/; look at them with Read.
- Any block may carry "src": ["k", ...]: the sources that block follows. Shown as "Following [1] [3]".

### Composition rules
1. Every section, definition-level explanation, views item and convention row carries src keys from `sources`.
   Proofs and examples carry src when they follow a source's argument. Paraphrase only: never copy sentences.
2. Do not add framings, analogies or claims that are in no source. If something standard is needed and the dossier lacks it,
   find a source (WebSearch/WebFetch), open it, add it to sources, and cite it.
3. Cover the full scope: everything core and common in `requires`, and the union of the textbook chapter contents in the
   dossier as far as they are needed by papers. Depth over breadth is NOT the trade here: both are required.
4. Main theorems get complete proofs (following a cited source). A proof left out must say where it is (source key + section).
5. Every section that teaches something ends with an exercise block (2-6 graded items, each with hint and full solution;
   computations in solutions get checks). Worked examples
   (with solutions) throughout: at least one per major section, including computations of the kind papers actually do.
6. Pitfalls from the dossier's confusions (Math SE etc.), with src.
7. `checks`: Python (stdlib, sympy, numpy) verifying every computed number, small case, and symbolic identity. Many algebraic
   claims can be checked on examples (e.g. compute a localisation, a Tor group of Z-modules, a cohomology dimension).
8. Text conventions as before: paragraphs separated by \n\n; inline $..$, display $$..$$; lists "1. " / "- "; no markdown
   headings, bold, HTML or backticks; [[id]] or [[id|text]] links only to ids in all_concepts.json; no literal dollar signs.
9. Length: there is no target. It follows from the scope fixed in the outline (below). minutes = honest reading time.
11. One concept per page. If the material splits into distinct concepts (each with its own definitions, main theorems and
    its own chapter or section in the textbooks), it becomes several pages linked by prerequisites. Do not absorb a
    neighbouring concept because a paper needs it: list it in `requires` with where: "separate page: <title>" and report it.

## Outline first
Before writing, produce outline_<id>.json: the list of subtopics, for each the textbook sections that treat it (from the
dossier, with how much space each source gives it), the requirements it serves, and a decision: on this page, on a separate
existing page ([[id]]), or a separate new page (proposed id + title). The page is then written to that outline.
10. Audience: has the prerequisite pages; wants to read research. Open with motivation an undergraduate can follow.

Phone width: every formula must fit a 390px phone screen. Break long exact sequences and equation chains with
aligned/gathered; move long inline formulas to display. Check with
/tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P2/widemath.sh <file.json> (lists every formula
wider than its column, with TeX); the list must be empty except for diagrams that cannot shrink.

Validate before replying:
python3 -I /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P2/validate.py <file.json>
python3 -I /home/claude/frontier_atlas/pipeline/round4/run_checks.py <file.json>
