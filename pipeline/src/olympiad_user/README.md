# Adding olympiad problems by hand

Put one or more `.json` files in this folder (any name, e.g. `kmo.json`). Each file is a list of problems:

```json
[
  {
    "contest": "KMO",
    "year": 2023,
    "num": "3",
    "q": "Find all positive integers $n$ such that $2^n + 1$ is divisible by $n^2$.",
    "tags": ["divisibility", "lifting-exponent"],
    "source_url": "https://..."
  }
]
```

- `contest`: short name shown on the site (IMO, USAMO, KMO, ISL, ...). With IMO/USAMO the AoPS wiki link is added automatically.
- `year`, `num`: as in the source. The problem id becomes `KMO-2023-P3`; keep (contest, year, num) unique.
- `q`: the statement, with `$...$` for inline math and `$$...$$` for display math (LaTeX as on AoPS).
- `tags`: optional concept ids (the part after `#concept-` in a concept page's address). Unknown ids are ignored.
  Leave it empty if unsure; Claude classifies new problems (tags, and which concept pages list them) in the next session.
- `source_url`: optional link to where the statement was taken from.

No solutions. Save, commit, push (or use GitHub's "Add file" button in this folder); the site rebuilds automatically.
