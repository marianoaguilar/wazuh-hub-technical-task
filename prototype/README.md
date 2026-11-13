# Mini prototype: the triage ledger

Post-delivery work (2026-11-13), on branch `prototype`. Plan: [`workflow/plans/04-prototype.md`](../workflow/plans/04-prototype.md).

It shows the core idea of [PHASE3](../PHASE3.md) with real data from my lab: **a person's decision is stored and re-applied on every sync, it reopens when it expires or the package changes, and what is left becomes a "fix first" list** ranked by rules (D8: KEV, then EPSS, then CVSS as a tie-breaker).

## What it covers of the Phase 3 flow

| Phase 3 step | Prototype |
|--------------|-----------|
| Connector reads findings with a read-only user, only the fields needed | One `curl` as `triage-connector`, six fields (see below). No host aliases, no push |
| Group findings by the action that fixes them | `group_by_package` (by binary package) |
| Re-apply past decisions; reopen on expiry or package change | `apply_ledger`, ledger in `ledger.json` instead of PostgreSQL |
| AI proposes, validator checks, person confirms | **Not built.** The person writes the decision in `ledger.json` |
| Fix-first list ranked by rules | `rank`: KEV, then max EPSS, then max CVSS. Host importance left out: the lab has one host |

## Result with my lab data (2026-11-13)

- 6582 findings → **98 groups**. Severity counts match the dashboard (105 Critical, 1867 High, 3041 Medium, 587 Low).
- 2 groups have a CVE in CISA KEV (`nodejs`, `libnode72`: CVE-2023-44487, EPSS 1.0) and go first although their CVSS is 7.5.
- `node-lodash-packages` (CVSS 10.0, low EPSS) drops out of the top 10 once EPSS is used.
- Two kernel packages hold 5100 of the 6582 findings. The host runs 6.8.0-149; `linux-image-6.8.0-138-generic` is an old kernel still installed. One decision (`fix_pending`, remove it) takes 2550 findings out of the list; on 2026-11-21 it expires and the group comes back as `reopened: expired`.
- Both kernels have **exactly the same 2550 CVEs**, so removing the old one lowers the noise, not the risk. Inference: upgrading 138 → 149 fixed none of them according to Wazuh, so these findings are likely not version comparisons; the one kernel finding I inspected in Phase 3 had `scanner.condition: "Package default status"` ([lab/api/09](../research/lab/api/09-indexer-vulnerability-critical-example.json)). This is the kind of group the AI step (`needs_context`) and a person's decision are meant for.

## Run it

```bash
# 1. Export findings (I run it; asks for the triage-connector password)
curl -sk -u triage-connector \
  "https://localhost:9200/wazuh-states-vulnerabilities-*/_search?size=10000&_source=agent.id,package.name,package.version,vulnerability.id,vulnerability.severity,vulnerability.score.base" \
  -o prototype/data/findings.json
# 2. Public ranking data
curl -sSfL -o prototype/data/kev.json https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
curl -sSfL -o prototype/data/epss.csv.gz https://epss.empiricalsecurity.com/epss_scores-current.csv.gz
# 3. Tests and demo
cd prototype
python3 -m unittest -v test_triage
python3 triage.py                      # with the decision in ledger.json
python3 triage.py --today 2026-11-21   # after the decision expires
```

`prototype/data/` is git-ignored: lab data stays out of the repository. Python 3 standard library only.

## Process

A light version of [`phase4/agent-setup/pipeline.md`](../phase4/agent-setup/pipeline.md): plan approved by me first, acceptance tests written before the code (and seen failing), code, tests run before the commit, my review, commit only with my OK, no merge to `main`.

## Next steps (not built)

- **Group by source package.** `imagemagick`, `imagemagick-6-common`, `libmagickcore-6.q16-6`… are one software fixed by one upgrade, same for `ffmpeg` and `libav*`. The vulnerability index has no source field; the server API inventory has it (`source: openssl`).
- AI proposal + validator for new groups; host aliases in the connector; PostgreSQL with RLS instead of a JSON file.
- Inference: the same ledger could hold decisions on failed SCA checks (98 failed in my lab), a different data source with the same problem.

Data sources: [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (CC0), [FIRST EPSS](https://www.first.org/epss/) (attribution requested).
