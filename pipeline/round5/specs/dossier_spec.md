# Source dossier for one concept page (Frontier Atlas, round 5 pilot)

Frontier Atlas is a study site whose concept pages must let a reader actually read research papers that use the concept.
Before anything is written, we collect what real sources say. The page will be composed from this dossier, not from
the writer's own preferences. Your job is research only: do not write the lesson.

Folder: /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P2
Inputs: brief.json (the concept: id, title, prerequisites, later pages that depend on it).

## What to collect

A. Requirements from papers. Pick 4-6 recent arXiv papers (2021-2026, from different subfields) that use the concept
   substantially. For each, open it (abstract page plus the HTML or PDF of the introduction/preliminaries sections) and list
   what it assumes the reader already knows about this concept, without explaining: definitions, theorems, notation,
   standard computations, standard tricks. Note where in the paper (section). Also include what the later pages in
   brief.json (e.g. schemes, sheaf cohomology) will need from this page.

B. Textbook coverage. For 3-6 standard texts or lecture notes on this subject, record the table of contents of the relevant
   chapter(s) (headings only). Prefer sources you can actually open (open lecture notes, open books, publisher TOC pages).
   Any licence is fine for reading; we never copy text.

C. Explanations. From at least 8 distinct sources of different kinds (textbooks, lecture notes, survey articles,
   MathOverflow and Math StackExchange answers, nLab, Wikipedia, expository blogs by working mathematicians such as Tao,
   Baez, Vakil's notes, Conrad's handouts, Keith Conrad's expository papers, etc.), record each distinct way the concept is
   explained. Group them:
   - intuition / mental pictures
   - motivation and history (what problem it was invented for)
   - definitions, including equivalent or alternative definitions, and how the sources prove they agree
   - viewpoints (geometric, algebraic, categorical, analytic, physical...)
   - conventions that differ between sources (signs, indexing, notation, left vs right, normalisations): which source uses which
   - standard examples and counterexamples that many sources use
   - computation methods (how one actually calculates it in practice)
   - common confusions (Math SE questions are a good signal) and how answers resolve them
   For each item: a summary in your own words (max ~80 words; no copied sentences, short quoted phrases at most),
   and the exact source (author, title, section/page or URL; MO/MSE question URL). Only cite sources you actually opened.
   If a summary is from memory rather than from an opened page, mark it "unverified".

D. A merged requirements list: the union of A and B, deduplicated, each item tagged with which papers/texts need it and
   a priority (core: needed by most papers; common; specialised).

## Output
Write dossier_<id>.json:
{
 "id": "...",
 "papers": [{"arxiv": "2301.01234", "title": "...", "subfield": "...", "assumes": [{"item": "...", "where": "§2"}]}],
 "texts": [{"ref": "...", "url": "...", "toc": ["..."]}],
 "explanations": {"intuition": [{"summary": "...", "source": "...", "url": "...", "verified": true}], "motivation": [...],
                  "definitions": [...], "viewpoints": [...], "conventions": [...], "examples": [...],
                  "computation": [...], "confusions": [...]},
 "requirements": [{"item": "...", "priority": "core|common|specialised", "needed_by": ["2301.01234", "Atiyah-Macdonald ch.3", "page: schemes"]}],
 "notes": ["anything uncertain"]
}
Write the file early and update it as you go so work is not lost. Validate it parses. Reply briefly: counts per section, and doubts.
