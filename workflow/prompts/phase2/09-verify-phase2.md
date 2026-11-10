# Prompt 09: verify PHASE2.md

- Date: 2026-11-10
- Agent: `verifier` (one agent)
- Plan step: Phase 2, Step 6 (`workflow/plans/01-phase2.md`)

## Prompt

> Read CLAUDE.md first. Verify `PHASE2.md` following your agent definition, treating it like a
> note: every factual statement next to an external URL must be supported by that URL. Write one
> report to `research/verification/PHASE2.verify.md`.
> - Fetch each distinct external URL once. If a URL was already checked in a report in
>   `research/verification/`, you may reuse that report's evidence instead of fetching again,
>   but say so in your report.
> - Links to notes in `research/sources/` are not URLs to fetch; check only that the statement
>   matches the cited note's claims (and that the note's verification report passed for them).
> - Statements marked `Inference:` or `UNVERIFIED:`, and statements about my own lab, are out of
>   scope; just list them.
> - Pay attention to wording that widens what a source says (counts, "most", "since", "all",
>   version numbers, issue states and dates).
> - Reply with at most 5 lines: overall result and the statements that are not SUPPORTED.
