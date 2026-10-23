# Frontier Atlas

An atlas of mathematics from school to the research frontier: concepts shared across fields, AI-written lessons checked by a second model and by computation, and textbook, olympiad and research problems with their current status. Readers post solutions and discussion on each problem's page.

## Layout

| Path | What it is |
|---|---|
| `site/` | The deployed static site. `index.html` is generated; `config.js` holds the Supabase URL and public anon key. |
| `pipeline/atlas/` | Build script, concept catalog modules and the page template (`template.html`). |
| `pipeline/lessons/`, `pipeline/round2/` | Reviewed AI lessons (`final_*.json`), reviewer reports, writer and reviewer specs. |
| `pipeline/round3/` | Exercise extraction from openly licensed PreTeXt textbooks. |
| `pipeline/src/` | Derived problem inputs (olympiad conversions, Erdős and Green lists, Putnam statements). |
| `supabase/migrations/` | Database schema and row-level security for accounts, posts, votes, progress and reviews. |
| `supabase/tests/` | Policy tests that run on plain Postgres with a small stand-in for Supabase's `auth` schema. |

## Build

```sh
pip install numpy sympy mpmath
python3 -I pipeline/atlas/build.py      # writes site/index.html and site/data/
python3 -m http.server -d site 8000     # http://localhost:8000
```

Pushing to `main` builds and deploys to GitHub Pages (`.github/workflows/pages.yml`).

## Backend

Accounts and community data live in Supabase. Run `supabase/migrations/20261023000000_init.sql` once in the project's SQL editor. Setup steps (providers, redirect URLs, making yourself an editor) are in [docs/SETUP.md](docs/SETUP.md).

With `supabaseUrl` left empty in `site/config.js`, the site runs read-only and keeps "marked solved" in the browser.

To test the policies locally against Postgres 15+:

```sh
cd supabase/tests && PSQL="psql -h localhost -U postgres" sh run.sh
```

## Content and licenses

Problem statements keep their sources' licenses: Understanding Linear Algebra (CC BY 4.0), Applied Combinatorics (CC BY-SA 4.0; derived exercises shared under CC BY-SA 4.0), compfiles and formal-conjectures (Apache-2.0), PutnamBench informal statements, erdosproblems.com status via teorth/erdosproblems. Credits are shown on the Problems page. Reader posts are licensed CC BY-SA 4.0 (see the site's Terms). `site/vendor/supabase-2.117.3.js` is supabase-js (MIT).
