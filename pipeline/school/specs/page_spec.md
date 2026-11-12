# School concept page (Frontier Atlas): entry + source-composed lesson

Work folder: given in your task (called W below). Inputs in W: brief.json (the cluster's concepts: id, title, fields,
prerequisites, stage, curriculum_refs, later_concepts), dossier_*.json (research already done for the cluster),
all_concepts.json (the ONLY valid [[link]] ids), field_ids.json. Published pages of prerequisites, if any, are at
/home/claude/frontier_atlas/site/data/lessons/<id>.json (reuse their notation).

## The goal
Frontier Atlas lets a learner climb from counting to research mathematics. This page must let a learner LEARN the concept
thoroughly from the page alone, and be the solid base the later pages (brief.json later_concepts) build on.
The page is composed from the sources in the dossier, not from the writer's taste: each explanation follows a named source;
where sources explain or represent the same thing differently, the page shows them side by side.

## Audience and voice
- Main path: a young learner at the stage in brief.json reading with a parent or teacher, or an older learner filling a gap.
  Plain words, short sentences, one idea at a time, concrete before symbolic (objects -> pictures -> words -> symbols).
  Explain every symbol the first time it appears. No condescension, no hype, no emoji.
- Last section "Looking ahead" (for older readers): how this idea grows into later mathematics, with [[links]] only to ids in
  all_concepts.json (e.g. place value -> [[digits-bases]]; properties of operations -> rings). One to three short paragraphs.
- Adults helping a child: where the dossier's sources give teaching advice (common misconceptions, what to say, what
  materials to use), put it in pitfall blocks titled for the adult (e.g. "For adults: ...").

## Learning design (every section)
- Order inside a section: a question or small activity the reader can do -> the idea -> examples and non-examples ->
  the rule or fact -> why it is true (an explanation a learner at this stage can follow; a proof where one fits) -> a worked
  example -> self-check -> exercises.
- Open each section by saying what the reader will be able to do after it (one sentence, in the section body).
- Worked examples (type example) show every step; they are the main teaching tool.
- Self-check (type check): 2-4 quick questions right after a new idea, each with a short answer.
- Exercises (type exercise) end every teaching section: 3-8 items ordered from routine to harder (no labels shown),
  each with hint and full solution.
- Summary (type summary) at the end of each major section: 3-6 lines.
- Pitfalls where learners really go wrong (from the dossier's misconceptions), with src.
- Figures: use them wherever a picture teaches (ten frames, dot patterns, number lines, base-ten blocks, arrays, bar models).
- One concept per page, decided by classification, never by length: another concept (its own definitions and facts, its own
  topic in the sources) gets at most a one-line recall with a [[link]] if it is in all_concepts.json, or a requires item with
  where: "separate page: <title>". Never absorb, never split, because of length. No length target; minutes = honest reading time.

## Output schema
A JSON array with one object: {"id", "entry", "lesson"}.
- entry: {"sum", "key", "why", "msc", "links", "refs", "aliases"}:
  sum 2-3 sentences ($TeX$ allowed); key 1-3 TeX statements without $ (the central facts, e.g. 3+5=5+3); why 1-2 sentences;
  msc codes only if sure (else []); links 0-3 {"field","note"} to fields NOT among the concept's own fields (ids from
  field_ids.json); refs: real books or curricula; aliases: other names (including British/American variants).
- lesson: {"v": 2, "minutes", "sources", "requires", "blocks", "checks"}

### sources
[{"k": "short-key", "ref": "Author or body, Title (year)", "where": "ch./§/standard code if sure", "url": "only a URL you or the dossier opened",
  "kind": "curriculum" | "textbook" | "research" | "reference" | "notes" | "Q&A" | "blog"}]
Every source the page follows. Open textbooks (OpenStax, Illustrative Mathematics: CC BY 4.0) and national curricula are the
main sources; mathematics-education research (e.g. on counting principles, misconceptions) where the dossier has it.

### requires
What the curricula expect for this concept (from brief.json curriculum_refs and the dossier): [{"item": "text", "priority":
"core" | "common" | "specialised", "where": "section title on this page, or [[id]], or separate page: <title>"}].
Every core and common item must be taught on this page or on a linked page.

### blocks
Types: intro, section (title), definition (title), theorem (title; for a rule or fact), proof (why it is true), example
(body + solution), pitfall, connection, and:
- exercise: {"type": "exercise", "title": "optional", "items": [{"q", "hint", "solution"}]}
- check: {"type": "check", "items": [{"q", "a"}]}
- summary: {"type": "summary", "body": "..."}
- views: {"type": "views", "title", "body": "optional lead-in", "items": [{"label": "2-4 words", "body", "src": ["k"]}]}
  Different representations or explanations of ONE idea (objects, ten frame, number line, words, symbols, a country's method),
  2-5 items, each from a different source or tradition. At least one views block per page; one for every central idea.
- conventions: {"type": "conventions", "title", "body": "optional", "rows": [{"who", "text", "src": ["k"]}]}
  Where English-language countries or books differ: number words (British and American), names of methods
  ("borrowing", "exchanging", "regrouping"), notation (division signs, decimal separator, thousands separator), layout of written methods.
- figure: {"type": "figure", "engine": "asy" | "plot", "code", "caption", "alt": "text description", "src": ["k"]}
  asy: Asymptote source (`import geometry;` allowed, never `olympiad`; size(8cm) or so). plot: matplotlib drawing on the
  current figure (plt is imported; do not call savefig). Black for the main drawing; emphasis only in pure-ish red, blue, green,
  orange, purple (light tints fine for fills); never colour alone (also label or pattern); no whole-figure background; labels
  at normal size; lines at least 0.6pt. Compile and LOOK at every figure: python3 -I /home/claude/frontier_atlas/pipeline/school/specs/figtest.py <file.json>
  writes PNGs to figpng/ next to the file; open them with Read. A figure must match its caption and the text exactly
  (count the dots).
- Any block may carry "src": ["k", ...] (shown as "Following [1] [3]").

### Composition rules
1. Every section, definition, views item and convention row carries src keys. Paraphrase only; never copy sentences.
2. No framings, claims or teaching advice that are in no source. If something standard is missing from the dossier, find a
   source (WebSearch/WebFetch), open it, add it to sources, cite it.
3. Cover everything core and common in requires.
4. checks: Python snippets {"python": "..."} (stdlib, sympy, numpy) verifying every number on the page: every example,
   exercise solution, self-check answer and every count in a figure caption. Assert, do not print.
5. Text: paragraphs separated by \n\n; inline $..$, display $$..$$; lists "1. " / "- "; no markdown headings, bold, HTML or
   backticks; [[id]] or [[id|text]] links only to ids in all_concepts.json; no literal dollar signs (write "dollars").
6. Phone width: every formula must fit a 390px screen; keep displays short, break long chains with aligned.
7. Language: English only (British and American variants both named where they differ). No Korean or other non-English words,
   number names or examples, and no non-English sources (this includes the Korean curriculum and Korean-language papers or wikis).

## Before you finish
python3 -I /home/claude/frontier_atlas/pipeline/school/specs/validate.py <file.json>   (must print OK)
python3 -I /home/claude/frontier_atlas/pipeline/round4/run_checks.py <file.json>        (0 failed)
python3 -I /home/claude/frontier_atlas/pipeline/school/specs/figtest.py <file.json>     (then look at every PNG)
