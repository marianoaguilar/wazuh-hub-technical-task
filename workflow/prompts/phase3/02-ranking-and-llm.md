# Prompt 02 (R6): ranking data (KEV, EPSS) and LLM API terms and prices

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with prompt 01)
- Plan step: Phase 3, Step 2 (`workflow/plans/02-phase3.md`)

## Prompt

> Context: Phase 3 designs a SaaS service for Wazuh users that keeps triage decisions on
> vulnerability findings and builds a ranked "fix first" queue. An LLM proposes "likely false
> positive / real / accepted risk" with evidence, and a person confirms. We need facts for two
> parts of the design: the ranking, and the cost and data handling of the LLM.
>
> Research questions:
> 1. **CISA Known Exploited Vulnerabilities (KEV) catalog:** what it is, how it can be
>    downloaded (formats, URL of the feed), how often it changes, and its terms of use.
> 2. **FIRST EPSS:** what the score means, how it is published (API, CSV), update frequency,
>    and its terms of use.
> 3. Whether Wazuh itself already uses KEV or EPSS in vulnerability detection (Wazuh docs, the
>    Wazuh CTI pages, `wazuh/wazuh` issues). Say clearly if you find nothing.
> 4. **LLM API, prices and data terms:** the public per-token prices of the current Anthropic
>    Claude models on the Anthropic API (official pricing page), whether API inputs/outputs are
>    used for training by default, the default data retention, and whether zero data retention
>    is offered. Also whether the same models are available through AWS Bedrock in EU regions
>    (official AWS page). Official vendor pages only; record the access date, because prices
>    change.
>
> Output: topic notes under `research/sources/` with prefixes `design-ranking-` (KEV, EPSS,
> Wazuh use) and `design-llm-` (prices and data terms). At most 4 notes. Topic notes may use
> `url: multiple, see claims`. Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent prices, model names, URLs or terms; if a page cannot be fetched, say
> so and do not describe what it "probably" says; mark confidence; keep inference apart from
> claims; English only.
>
> When done, reply with at most 10 lines: files written and the main facts the design can rely on.
