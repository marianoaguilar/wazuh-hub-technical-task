# Prompt 06: rule tuning guidance and Wazuh Pharos

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with the 05-fixes prompts)
- Plan step: Phase 2, Step 3 → input to Step 4 (`workflow/plans/01-phase2.md`)

## Prompt

> Two narrow questions. They decide whether two candidate needs are already served.
>
> **A. Rule tuning guidance.** Does the official Wazuh documentation (latest 4.x, and 5.0 docs if
> published) or the Wazuh blog give guidance or tooling for: finding which rules generate the
> most alerts/noise; tuning or silencing noisy rules safely (rule overwrite, `if_sid` child rules,
> `level 0`, `<list>`/CDB exceptions); testing a rule or decoder change before deploying it
> (`wazuh-logtest`, the ruleset test API endpoint, the dashboard "Ruleset test"); and checking
> that a change did not break other rules. Search documentation.wazuh.com, wazuh.com/blog and
> the `wazuh/wazuh` repository (e.g. any ruleset test framework). For each item say exactly what
> exists and where.
>
> **B. Wazuh Pharos and Vesper.** Find any public page that describes what "Wazuh Pharos"
> (a Hub beta service, "Vulnerability & Threat Intelligence") or "Vesper" (seen in search
> snippets as a Wazuh support assistant) actually does: product pages, docs, blog posts,
> announcements, release notes, the Hub terms. Known unreachable: hub.wazuh.com pages,
> vesper.wazuh.com (maintenance), docs.vesper.wazuh.com (404); try other URLs. If nothing public
> describes them beyond their names, say so plainly. Do not describe what they "probably" do.
>
> Output: two notes, `research/sources/landscape-rule-tuning-guidance.md` and
> `research/sources/landscape-pharos-vesper.md`. Topic notes may use `url: multiple, see claims`.
> Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent features or URLs; an absence is reported only as "the pages I read
> (list) do not mention X"; mark confidence; keep inference apart; no personal data; English only.
>
> When done, reply with at most 10 lines: files written and the answer to A and B.
