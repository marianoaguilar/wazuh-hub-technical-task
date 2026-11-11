# Prompt 05: verify the claims and links in PHASE3.md

- Date: 2026-11-11
- Agent: `verifier` (one run)
- Plan step: Phase 3, Step 6 (`workflow/plans/02-phase3.md`)

## Prompt

> Verify `PHASE3.md` (repository root). Write one report to
> `research/verification/PHASE3.verify.md`, using the report format of your agent definition.
>
> For every statement that cites a source, check it against that source:
> - **Web URLs:** fetch each distinct URL once and check that it supports the statement:
>   SUPPORTED, PARTIAL (the statement widens what the page says), NOT SUPPORTED or URL UNREACHABLE.
> - **Lab files** (`research/lab/api/*.json`): check that numbers, field values and versions in
>   PHASE3.md match the file exactly.
> - **Internal links** (`research/phase3-decisions.md#...`, `PHASE2.md#...`): check that the file
>   exists, that the anchor matches a heading, and that PHASE3.md does not contradict it.
> To save tokens: if a URL was already checked for the same statement in an existing report in
> `research/verification/` (the `design-*` reports and `PHASE2.verify.md`), you may reuse that
> verdict and cite the report instead of fetching again.
> Also flag statements of fact with no source and no `Inference:` label, and any inference
> presented as fact. Pay special attention to: prices and the cost arithmetic, security promises
> (data retention, who can access data), and claims about what Wazuh does or does not do.
>
> Do not edit PHASE3.md. Reply in at most 10 lines: counts of each verdict and the statements
> that must be fixed.
