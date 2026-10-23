# Round 4 notes (new concepts: entry + lesson)

The site groups mathematics by topic only, never by school year or course. Each concept here is ONE page for the whole topic, read by a strong 15-year-old meeting it for the first time and by a university student coming back to it.

- `stage` is only where readers usually first meet the topic. Start the lesson at that level, with intuition and small worked numbers, then go as far as the topic naturally goes (precise definitions, the main theorem with proof or a clearly-labelled proof sketch, a glimpse of the advanced version). A school-stage lesson can end with a section that a university reader will appreciate; a graduate-stage lesson must still open with motivation a strong undergraduate can follow.
- `curriculum_sources` lists the textbook chapters and curriculum units this topic was found in. Use them only to judge scope (what belongs on this page); do not copy any wording.
- Prerequisites are pages the reader can follow. Link them with [[id]] where used, and link `leads_to` concepts in the connection block. Do not re-teach a prerequisite at length.
- Statistics lessons: use small made-up data sets you compute yourself (say so: "a made-up sample of 8 heights"); verify every statistic, p-value and interval with scipy/numpy in `checks`. State the assumptions of every test.
- Physics-facing topics (tensors, differential forms, Hilbert spaces, Lie groups, calculus of variations, heat/wave/Laplace): mention the physical meaning where it is standard (e.g. Euler–Lagrange and the principle of least action), but keep the page mathematical.
- Examples: your own constructions or classic textbook-style exercises. Do not work out IMO, USAMO or Putnam problems.
- `checks`: Python with the standard library, sympy, numpy, scipy or mpmath. Verify every computed number, identity, derivative, integral, matrix and small case.
- entry.links: 1–3 links to fields other than the concept's own `fields`, field ids only from field_ids.json.
