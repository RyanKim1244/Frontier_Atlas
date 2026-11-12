# School concept page, v2 (Frontier Atlas)

Replaces page_spec.md for school concepts. Same JSON schema (see page_spec.md "Output schema"); different aims and limits.
Why v2: v1 pages tried to serve young children, their parents and older readers at once, ran 45-80 minutes, repeated a fixed
section template, summarised teachers' guides instead of teaching mathematics, and cited a source on nearly every block.

## Reader
A teenager or adult who wants to understand this foundation properly, perhaps for the first time, perhaps to repair gaps,
on the way to university mathematics. They can read fluently and are not afraid of symbols once explained.
Not written for a young child and not for teachers: no classroom activities, no advice to adults, no "try this with counters".

## What a good page does
1. Says in two or three sentences what the concept is and why it matters.
2. Gives the precise definition(s), with the everyday meaning connected to the precise one. Explain each symbol once.
3. States the key facts and shows WHY each is true: a short convincing argument a careful reader can follow (a real proof
   where one is short; otherwise the idea of one). Mathematics, not lesson description.
4. Teaches through a small number of well-chosen worked examples (each showing a different point), not many similar ones.
5. Names the 1-3 misconceptions that actually trip learners (from sources), each resolved in a few lines.
6. Shows a second viewpoint only when it adds understanding (e.g. the number line view of subtraction; the area view of
   distributivity). At most two views blocks; none if there is no genuinely different viewpoint.
7. Ends with "Looking ahead": how the idea grows (e.g. parity -> modular arithmetic [[congruences]]; place value -> other
   bases [[digits-bases]]), linking only ids in all_concepts.json.
8. Exercises: one exercise block per major section, 3-6 items that each test something different, from routine to
   genuinely thoughtful (a "why" question or a small proof); every item has hint and full solution.
9. Self-check blocks only where a quick check catches a likely misunderstanding (at most 3 per page). Summary: one, at the end.

## Limits
- Reading time: typically 10-20 minutes for an early-school concept, up to 30 for a rich one (column algorithms, division).
  Length follows scope, but scope is the mathematics of this one concept, not its pedagogy.
- No fixed per-section template. No "After this section you will be able to" sentences. No "Try this first" activities.
- Sources: cite at section level (the section block's src) and on views/conventions items. Do not put src on every
  example, pitfall or proof unless it follows a specific argument. Never talk about the sources in the text ("In IM lesson 3
  the class ..."): teach the content.
- Figures: only where a picture explains (number line, array for multiplication, area model, base-ten picture). 2-5 per page.
- Conventions block only for real differences that a reader will meet (British vs American names, notation such as ÷ vs /,
  layouts of the written method). English only; no non-English words or sources.
- One concept per page, decided by classification, never by length (as before).

## Lessons from cluster 1 (judges' most common complaints; avoid them from the start)
- Length: aim for 2,500-3,500 words of text (excluding figure code); never over 4,500. Economy was the lowest score on every page.
- Say each idea once. One fact gets one home (definition, theorem, figure or pitfall), never four. Exercises must not repeat
  worked examples.
- No curriculum or source talk anywhere in the text: no "Common Core", "Year 4", "England asks", "Illustrative Mathematics
  uses", "a study of children found". A conventions row is a notation or name the reader will meet (÷ vs /, "carry" vs
  "regroup"), never a syllabus expectation. If there is no such difference, no conventions block.
- Contexts for an adult reader (money, measurement, time, data), not stickers, sweets or birds on a roof.
- Rigour: state hypotheses (a ≤ n for whole-number subtraction, b ≥ 1 for division), prove uniqueness when "the" is used,
  argue general claims generally (not only for 47). Do not label trivial facts as theorems.
- Views blocks only for a genuinely different picture; a view that restates the definition is padding.

## Checks (unchanged)
Every number on the page is asserted in `checks`. Before finishing:
python3 -I /home/claude/frontier_atlas/pipeline/school/specs/validate2.py <file.json>   (OK)
python3 -I /home/claude/frontier_atlas/pipeline/round4/run_checks.py <file.json>        (0 failed)
python3 -I /home/claude/frontier_atlas/pipeline/school/specs/figtest.py <file.json>     (look at every PNG)
