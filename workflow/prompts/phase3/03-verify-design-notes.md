# Prompt 03: verify the Phase 3 design notes (one verifier for the batch)

- Date: 2026-11-10
- Agent: `verifier` (one run for all notes of prompts 01 and 02)
- Plan step: Phase 3, Step 2 (`workflow/plans/02-phase3.md`)

## Prompt

> Verify these 8 notes in `research/sources/`, one report per note in `research/verification/`
> (`<note-name>.verify.md`), using the report format of your agent definition:
> `design-wazuh-access-vulnerability-index.md`, `design-wazuh-access-inventory.md`,
> `design-wazuh-access-server-api-rbac.md`, `design-wazuh-access-indexer-security.md`,
> `design-ranking-cisa-kev.md`, `design-ranking-first-epss.md`,
> `design-ranking-wazuh-kev-epss-support.md`, `design-llm-claude-pricing-data-terms.md`.
>
> Check every claim against the URL it cites: SUPPORTED, PARTIAL (the claim widens what the page
> says), NOT SUPPORTED or URL UNREACHABLE. Pay special attention to: exact numbers (prices, JWT
> lifetime, ports, versions, catalog counts), endpoint and field names, quotes marked as possibly
> summarised by the fetch tool, and statements of absence ("Wazuh never mentions…"). Fetch each
> distinct URL once and reuse it for all claims that cite it.
>
> When done, reply with at most 10 lines: per note, the counts of each verdict, and the claims
> that must be fixed before use.
