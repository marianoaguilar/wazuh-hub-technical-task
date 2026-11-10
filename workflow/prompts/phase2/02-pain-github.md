# Prompt 02 (R2): problems users report on GitHub

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with prompts 01, 03, 04)
- Plan step: Phase 2, Step 2 (`workflow/plans/01-phase2.md`)

## Prompt

> Research question: **What problems do Wazuh users report on GitHub?**
>
> Look at the public repositories of the Wazuh organisation (github.com/wazuh), mainly
> `wazuh/wazuh` (issues and GitHub Discussions) and `wazuh/wazuh-dashboard-plugins`, plus other
> repos if they turn out relevant. Focus on problems that affect users operating Wazuh, not
> internal development tasks. Themes to look for (do not limit yourself to them):
> - alert fatigue, noisy rules, false positives, tuning rules and decoders;
> - understanding alerts and events, and investigating them;
> - vulnerability detection results (volume, false positives, prioritisation);
> - writing custom rules/decoders and testing them;
> - upgrades, scaling, performance, index/storage management;
> - dashboard usability, reporting, compliance reports;
> - multi-tenant / MSSP operation.
>
> For each theme record a **frequency signal**: the issues or discussions you read, with their
> reaction count (👍), comment count, state (open/closed) and dates, as shown on the page. Write
> "not shown" when the page does not show a number; never estimate. Prefer the last 2 years.
> If GitHub search pages cannot be fetched, use web search with `site:github.com/wazuh` and
> fetch the individual issue pages.
>
> Output: topic notes under `research/sources/` with the prefix `pain-github-` (for example
> `pain-github-alert-fatigue.md`), one per theme with real evidence. At most 7 notes. Topic
> notes may use `url: multiple, see claims`. Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent issue numbers, counts or quotes; mark confidence; keep inference
> apart from claims; no personal data (never record GitHub usernames; write "a user reports");
> English only.
>
> When done, reply with at most 10 lines: files written and the strongest themes, with their
> frequency signals.
