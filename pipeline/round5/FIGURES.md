# Figures (plan)

## Lessons (AI-written)
- New block type `figure`: {"type": "figure", "engine": "tikz" | "asy" | "plot", "code": "...", "caption": "...", "alt": "..."}.
  - tikz: TikZ / tikz-cd / pgfplots source (the standard language of mathematical drawing). Built at site-build time:
    pdflatex (standalone) -> pdftocairo -svg -> site/data/figures/<hash>.svg. Both tools are available in the build image
    (CI needs texlive-pictures + poppler-utils).
  - plot: a small Python spec (function graphs, slope fields, phase portraits, histograms) rendered with matplotlib to SVG.
  - SVGs are post-processed to use currentColor so they follow light/dark mode; width capped to the column, scrolls on mobile.
- Review: the reviewer gets a PNG rendering of every figure (Playwright screenshot) and checks it against the text,
  the same way it re-runs numeric checks. A figure that does not match is an error.
- Interactive figures (dragging points, sliders) later, with JSXGraph (LGPL/MIT) only where interaction teaches something.
- Commutative diagrams: small square diagrams can use MathJax's AMScd (\begin{CD}); anything larger goes through tikz-cd.

- asy: Asymptote (the language AoPS uses for olympiad diagrams). Best for Euclidean geometry: the bundled `geometry` module gives
  circumcircles, projections, orthocentres, intersections by construction, so points are computed, not hand-placed.
  Build: `asy -f pdf` then `pdftocairo -svg` (direct `-f svg` needs dvisvgm; the PDF route is tested). CI: `apt-get install asymptote`.
  AoPS's `olympiad.asy` is not bundled with Asymptote; use `geometry` unless its licence is checked first.
  Rule of thumb: geometry figures → asy; diagrams, commutative diagrams, schematic pictures → tikz; function graphs → plot.

## Problems from open textbooks
- About 270 Lebl exercises and some ULA/AC exercises were skipped because they need a figure. The books' figures are in
  their repos under the same licence (Lebl: figures/*.pdf, .xp; ULA: latex-image / sage blocks).
  Plan: convert the referenced figure to SVG (pdftocairo, or compile the latex-image block), attach it to the statement
  as `figure`, credit it like the statement, and re-admit the exercise.
- Exercises that refer to "the figure above" in the running text but whose figure is not a separate file stay excluded.

## Olympiad and research problems
- Where an olympiad geometry problem is hard to read without a figure, a figure drawn by us in asy (from the statement, never copied) may be added, marked as ours.

- Statements stay as published (no added diagrams: a diagram can give away a construction).
- Optional "figure" for geometry problems only when the official statement has one, redrawn in TikZ from the statement,
  reviewed like a lesson figure.

## Community posts
- Phase 1: TikZ code blocks in posts, rendered to SVG by a small server function (Supabase Edge Function or a queue) with
  a size/time limit; never run untrusted LaTeX in the browser.
- Phase 2: image upload to Supabase Storage (size limit, PNG/JPEG/SVG sanitised), for photos of handwritten work.
