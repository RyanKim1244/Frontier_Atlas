# Lesson specification (Frontier Atlas concept pages)

A concept page today has a 2–3 sentence summary and a few key statements. A lesson turns it into something a motivated high-school or first-year reader can actually learn from, start to finish, without another book open. Audience: strong olympiad students and curious adults studying as a hobby. Language: English.

## Output format

One JSON file per batch: a JSON array of lesson objects, one per concept, in the order of the brief.

```json
{
  "id": "congruences",
  "minutes": 15,
  "blocks": [ { "type": "...", "title": "...", "body": "..." } ],
  "sources": [ { "ref": "Niven, Zuckerman & Montgomery, An Introduction to the Theory of Numbers", "where": "§2.1" } ],
  "checks": [ { "claim": "2^100 mod 13 = 3", "python": "assert pow(2,100,13) == 3" } ]
}
```

`minutes`: honest reading time.

### Block types (use in roughly this order; not every type is required)
- `intro` — no title. 1–2 short paragraphs: the question this concept answers and why someone would care. Concrete, no hype.
- `section` — title required. Explanatory prose: intuition first, then precision. Most of the teaching lives here. 2–5 of these.
- `definition` — title = the term. The precise definition, then one sentence of meaning.
- `theorem` — title = the name (e.g. "Bézout's identity"). The exact statement.
- `proof` — title optional (e.g. "Proof of Bézout's identity"). A complete, correct proof at the reader's level. Must follow the theorem it proves.
- `example` — title optional. Fields: `body` = the worked problem statement, `solution` = the full worked solution. Solutions are folded on the page until the reader opens them. 2–4 examples per lesson, increasing in difficulty; at least one should be olympiad-flavoured.
- `pitfall` — common mistakes or false generalisations, as a short list or paragraph.
- `connection` — how this concept is used later or in other fields. Refer to other concepts with links (see below).
- `exercise` — 2–4 short self-check questions with no solutions (the site already has a problem bank). Body is a numbered list in plain text ("1. ...\n2. ...").

### Text conventions inside `body` / `solution`
- Paragraphs separated by a blank line (`\n\n`). No markdown headings, no bold/italics markup, no HTML, no backticks.
- Math in TeX: inline `$...$`, display `$$...$$`. Use standard LaTeX supported by MathJax (\mathbb, \pmod, \equiv, \gcd, \binom, \lfloor, \sum, \prod, \dfrac, \le, aligned environments inside $$...$$ are fine). Never a literal dollar sign other than math delimiters.
- Lists: lines starting with "1. ", "2. " or "- " are allowed inside a body.
- Link to another concept with `[[concept-id]]` (shows its title) or `[[concept-id|link text]]`. Only use ids from all_concepts.json. Link prerequisites where you rely on them and the "leads to" concepts in the connection block.

## Quality rules (these matter more than length)
1. Correctness first. Every statement, number and proof must be right. If you state a numeric fact or compute an example, add a `checks` entry with a Python snippet (standard library or sympy) whose assertion verifies it. Aim for 3–8 checks per lesson.
2. Write it yourself. Do not reproduce text from textbooks, Wikipedia, AoPS or any other source; explain in your own words. Standard theorem statements are fine.
3. Sources: cite 1–4 real, well-known references the reader can look up (books listed in the brief's `references`, or other standard texts/papers you are certain exist). Give the section or chapter only if you are sure; otherwise omit `where`. Never invent URLs.
4. Stay consistent with the brief: same notation as `key_statements`, and do not contradict `summary`.
5. Level: assume only the listed prerequisites. Build intuition with a small example before the general statement. Prefer one clear proof over several sketchy ones.
6. Length: typically 900–1800 words per lesson. Foundational concepts (divisibility, congruences) can be longer; narrow techniques shorter.
7. No answers to IMO/USAMO problems from the site's bank should be given away; you may use classic textbook examples instead.
