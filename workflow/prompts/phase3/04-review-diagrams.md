# Prompt 04: outside review of the three Phase 3 diagrams

- Date: 2026-11-11
- Agent: `general-purpose` (one run, read-only except its report)
- Plan step: Phase 3, Step 4 (`workflow/plans/02-phase3.md`)

## Prompt

> You are an outside reviewer (a senior engineer in the Wazuh Hub team) who sees three diagrams
> for the first time. They belong to the design of a SaaS service for Wazuh users: a triage
> ledger for vulnerability findings, where AI proposes "likely false positive / real / needs
> context", a person confirms, decisions are re-applied on each sync, and a ranked "fix first"
> list is produced. The diagrams will be shown in a short presentation, so they must be simple
> and understandable at a glance; details go in the text of PHASE3.md, not in the diagrams.
>
> The brief asks for exactly these three drawings:
> 1. The components of the service and how the data flows between them.
> 2. One user request from start to end, with every call the AI makes and every point where a
>    person takes part.
> 3. Where the data of each customer goes, and who or what can read it on the way.
>
> Read the Mermaid sources in `diagrams/src/` (`d1-components.mmd`, `d2-triage-request.mmd`,
> `d3-data-boundaries.mmd`) and look at the rendered images in
> `<scratchpad>/d1-components.png`, `d2.png` and `d3-data-boundaries.png`.
> For context only, `research/phase3-decisions.md` lists the design decisions (D1-D8) the
> diagrams must be consistent with.
>
> Check: (a) does each diagram answer its brief bullet; (b) is it understandable without
> explanation; (c) contradictions with the decisions file or between diagrams; (d) misleading
> or overclaiming labels (for example security promises stronger than the design gives);
> (e) anything missing that the brief bullet needs. Do not ask for more detail just for
> completeness: simplicity is a requirement. The user already decided to keep the names
> "Web app" and "Analyst" as they are.
>
> Write your findings to `research/verification/phase3-diagrams.review.md`: per diagram, a short
> verdict and at most 5 findings, each with severity (must fix / should fix / optional) and a
> concrete suggested change. Do not edit any other file. Reply in at most 10 lines.
