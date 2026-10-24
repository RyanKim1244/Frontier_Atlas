# Review after a split (you did not do the split)

Folder: /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P1
Read page_spec.md and review_spec.md (Role R standard) first. A reviewed page was split into one page per concept
(split_spec.md describes what the splitter was allowed to do). Most blocks are unchanged and already reviewed.

Your tasks, editing split_<original>.json in place:
1. Review every block listed in changes_<original>.json (new intros, connections, entries, edited cross-references, new views
   and conventions blocks) to the Role R standard: correct, faithful to the cited sources (open them for views and conventions),
   no copied wording. The splitter added some views blocks only because a validator then demanded two per page; that rule
   is gone (one is enough). Keep such a block only if its items are genuinely different explanations that the cited sources
   really give; otherwise delete it.
2. Check each page reads on its own: nothing refers to material that is now on another page without a [[link]]; each page's
   prerequisites in brief.json cover what it uses; requires and sources match the page.
3. Formulas that do not fit on a phone. Run
   /tmp/claude-0/-home-claude/2a7609d2-6c9f-53e8-b759-a809c7b46790/scratchpad/round5/P1/widemath.sh split_<original>.json
   It lists every formula wider than its column at 390px, with its TeX. Fix them all, keeping the mathematics identical:
   - long exact sequences and chains: break across lines with \begin{aligned} ... \end{aligned} (or gathered), breaking
     after an arrow or relation, aligned sensibly;
   - long inline formulas: move to display, or split into two formulas joined by words;
   - long equation chains: aligned with one step per line;
   - large diagrams written as arrays: redraw as a tikz-cd figure if the diagram matters, else stack it.
   Re-run until the list is empty, except for diagrams that cannot shrink (say which, and why).
4. validate.py and /home/claude/frontier_atlas/pipeline/round4/run_checks.py must pass on the file.
Write review_split_<original>.json: [{"id", "issues": [{"severity", "where", "problem", "fix"}], "wide_math_fixed": n, "wide_math_left": [...]}].
Reply briefly.
