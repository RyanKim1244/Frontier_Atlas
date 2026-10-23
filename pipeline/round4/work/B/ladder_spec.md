# Bridge ladders: from textbook and olympiad problems up to research problems

Frontier Atlas has textbook exercises, olympiad problems and research problems (Erdős problems, Ben Green's list, Millennium problems). For many concepts there is a gap: dozens of open research problems and almost nothing a student can solve first. A ladder fills that gap for one concept: an ordered list of 6–10 problems, each one step closer to the research frontier.

## What a rung is
Each rung is a precise problem statement (no solution) that is one of:
- **classic**: a well-known exercise or folklore fact (e.g. "a Sidon set in {1,…,n} has at most √(2n)+1 elements"), with a textbook or survey where it appears;
- **theorem**: a published theorem posed as a problem ("Prove that …" or "Show that …"), with the paper that proved it;
- **special case**: a solved special case or weaker version of one of the brief's research problems, with the paper that solved it.

Order the rungs from the first a strong olympiad student could do to the strongest known results right below the open problem. Do NOT assign difficulty numbers; the order is the only signal. The last rungs should name, in `bridges_to`, the research problems (ids from the brief) they lead into. Early rungs may have empty `bridges_to`.

Every statement must be mathematically exact: all hypotheses, quantifiers, ranges. For asymptotic results state the form precisely (e.g. "|A| ≤ √n + O(n^{1/4})"). If you are not sure of the exact constant or exponent in a published result, either state a weaker version you are sure of, or leave that rung out. Never invent a result, author, year or paper.

## Citations
`source`: for classic rungs, a real textbook/survey ("Halberstam & Roth, Sequences", "Tao & Vu, Additive Combinatorics, §…" only if sure of the section). For theorem and special-case rungs: authors, title (if you are sure), year, and venue or arXiv id if you are sure. The reviewer will look every citation up; anything that cannot be confirmed will be removed, so cite only what you know.

## Output
JSON array, one object per concept in the brief, same order:
```json
{"concept": "sidon-sets",
 "ladder": [
   {"title": "Short descriptive title (no 'Problem 1')",
    "kind": "classic | theorem | special-case",
    "q": "Statement in the site's text format: paragraphs separated by blank lines, math in $...$ / $$...$$, no markdown.",
    "concepts": ["sidon-sets", "...other concept ids it uses (from all_concepts.json)"],
    "source": "…",
    "year": 1941,
    "bridges_to": ["ERDOS-30"],
    "note": "One sentence: what this rung adds over the previous one / why it matters for the research problem."}
 ]}
```
`year` = year of the result (omit for classic rungs if unknown).

Text format: no solutions, no hints that give the answer, no markdown, no HTML, no literal dollar signs. Do not reproduce statements of IMO/USAMO/Putnam problems (the site already has them); you may list one in `existing_easier_problems` context but rungs must be your own wording of classic/published results. Write statements in your own words.

Before finishing: validate the JSON, balanced `$`, concept ids exist, `bridges_to` ids exist in the brief.
