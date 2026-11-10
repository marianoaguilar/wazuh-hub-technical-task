# Prompt 08: impartial review of the research file structure

- Date: 2026-11-10
- Agent: `Plan` (read-only, no edits)
- Plan step: Phase 2, between Step 3 and Step 4 (`workflow/plans/01-phase2.md`)

## Prompt

> You are an impartial reviewer. Read CLAUDE.md, README.md, research/README.md and
> `.private/task.pdf` (the brief; the only file you may read in `.private/`; do not quote it).
>
> Question: the repository now has 26 notes in `research/sources/` and 23 reports in
> `research/verification/`. The owner worries this clutters the repository. Decide the best way
> to organise this material for the people who will review the repository, given what the brief
> asks for.
>
> Consider at least: keeping the structure as it is; merging notes and reports into one file per
> research run; keeping only a summary in the repo; and any better option you see. Judge each on:
> what the brief asks for (visibility of the AI workflow and of sources), how easy it is for a
> reviewer to follow, traceability from PHASE2.md claims to sources, the cost of doing it, and
> the risk of breaking links or losing evidence.
>
> To save tokens, do not read every note: list the folders, open 2-3 notes and 2-3 reports as
> samples, and read the indexes.
>
> Answer in at most 25 lines: your recommended option, why, the concrete steps (files to move,
> merge or add), and the main drawback.
