# Sourcing exercises for concept pages (problem bank under each concept)

Frontier Atlas shows, below each concept's lesson, a list of exercises from real textbooks and notes (statement only, with
credit and licence; solutions are never copied). You collect such exercises for the concepts listed in your task.

## Hard rules
1. Licence: only sources whose licence allows commercial reuse and modification of the text: CC BY, CC BY-SA, CC0,
   GFDL, public domain. NOT: NC, ND, "free to read", all-rights-reserved (Hatcher, Vakil, Milne, MIT OCW, Atiyah-Macdonald,
   Eisenbud, Weibel's book... are out), unless the work's own page states such a licence. Read the licence on the source's own
   site and record the URL where it is stated. pipeline survey of licences:
   /home/claude/frontier_atlas/pipeline/round5/research/sources.json (use it; confirm per source).
   Candidates to check: Stacks Project (GFDL; has exercise sections and exercises inside chapters), Evan Chen's Napkin
   (CC BY-SA 4.0 text), Judson AATA (GFDL), Hefferon, Beezer, Open Logic, HoTT book, Lebl's books, lecture notes that state
   CC BY/BY-SA, arXiv papers or notes under CC BY / BY-SA / CC0 (the licence shown on the arXiv abstract page).
2. Directly related only. An exercise goes to a concept only if solving it requires working with that concept itself
   (its definitions, theorems, computations). Not if the concept is merely mentioned, used in passing as background, or the
   exercise is really about a neighbouring concept. When in doubt, leave it out. Each exercise gets one primary concept;
   add a second only if it is equally central.
3. Statement only, copied faithfully (it is licensed text; keep the wording, fix nothing silently). Convert to TeX with $...$
   for inline and $$...$$ for display, MathJax-compatible; no macros the site lacks (use \mathbb, \operatorname, etc.).
   The statement must be self-contained: if it refers to "the ring of Exercise 3" or local notation, either include the
   needed definition from the source in brackets [Here R denotes ...] or skip the exercise.
4. Never include solutions or hints from the source.
5. Prefer exercises that build skill in steps: routine computations, standard results, harder ones. Aim for 8-25 per concept
   if the licensed sources have them; fewer is fine; zero if none qualify (say so).

## Output
exercises_<batch>.json: [{"id": "STK-<tag>" | "NAP-<chapter>-<n>" | ..., "concept": "<id>", "also": [], "coll": "Stacks Project" | "Napkin" | ...,
 "credit": "author, title", "title": "short label, e.g. 'Stacks 10.9 · Exercise 3' or 'Napkin 51.4 · Problem 5'",
 "section": "section name in the source", "q": "statement", "url": "link to the exact place", "license": "GFDL 1.2" | "CC BY-SA 4.0" | ...,
 "license_url": "...", "level": "routine" | "standard" | "challenging" (used only to order the list easy -> hard; never shown), "why": "one line: which part of the concept it exercises"}]
Every q must pass: balanced $; renders in MathJax 3/4 (no \newcommand). Also write sources_<batch>.json listing each source
with the licence evidence URL. Reply briefly: counts per concept, sources used, sources rejected and why.

## Link-only practice
Also collect publicly reachable pages with practice the licence does not let us copy (university past exams, qualifying /
prelim exams, course problem sets, exercise sections of NC/ND books) that directly fit the concept. Output
practice_links_<batch>.json in the format of pipeline/round5/practice_links/README.md. Never copy their text.
