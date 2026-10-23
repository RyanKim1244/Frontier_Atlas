# Round 2 writer task: concept entry + lesson

For each concept in your brief you write two things: the concept's catalog entry (what appears at the top of its page and in lists), and its lesson. The lesson format and all quality rules are in ../lessons/lesson_spec.md — read it and follow it exactly. This file adds the catalog entry and a few round-specific notes.

## Output
A JSON array, one object per brief concept, same order:
```json
{
  "id": "derivative",
  "entry": {
    "sum": "2–3 sentences, may use $...$ TeX. What it is and the one idea to remember.",
    "key": ["1–3 key statements as TeX WITHOUT surrounding $ (they are shown as display math)"],
    "why": "1–2 sentences: why it matters, concrete.",
    "msc": ["MSC2020 codes you are sure of, e.g. 26A24"],
    "links": [{"field": "<field id from field_ids.json>", "note": "one sentence: how this concept is used in that field"}],
    "refs": ["1–3 standard textbooks, 'Author, Title'"],
    "aliases": ["other names / search terms"]
  },
  "lesson": { "minutes": 15, "blocks": [...], "sources": [...], "checks": [...] }
}
```
- `links`: 1–3 connections to fields OTHER than the concept's own `fields` (given in the brief). Only field ids from field_ids.json.
- `msc`: leave the list empty rather than guess a code.

## Notes for this round
- The `stage` in the brief says where readers usually meet the concept (school, undergraduate, graduate). Pitch the lesson there: a school-stage lesson must be readable by a strong 15-year-old; an undergraduate lesson may assume the listed prerequisites and nothing else.
- Calculus lessons: give the intuition (pictures in words, small numeric tables) before epsilon–delta; precise definitions still required. Real-analysis lessons: full rigour.
- Prefer classic textbook-style examples and your own constructions. Do not work out Putnam, IMO or USAMO problems; the site has those in its problem bank without solutions.
- Exercises: 2–4 short ones without solutions.
- `checks`: use sympy/numpy/fractions to verify every derivative, integral, series value, matrix computation, probability or numeric claim you state. For symbolic identities, use sympy simplification; for numeric ones, exact arithmetic where possible.
- [[links]] may point to any id in all_concepts.json (it includes the other new concepts of this round).
