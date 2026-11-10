---
note: PHASE2.md
verified: 2026-11-10
result: NEEDS FIXES
---

Method. Fetched in this session: the vulnerability-detection docs page and GitHub #37485. All other external URLs were checked
by reusing the verification reports in `research/verification/` (all dated 2026-11-10, fetched that day), as allowed. Links to
`research/sources/` notes were checked against the note text and its report. Lab-only statements and `Inference:` / `UNVERIFIED:` lines are listed at the end, not graded.

## Claims (only non-SUPPORTED rows are expanded; the rest are grouped)
| # | Statement (section) | Verdict | Explanation |
|---|---------------------|---------|-------------|
| 1 | "In 4.x there is no way to acknowledge, exclude or annotate a finding" (need section; also in Short answer) | PARTIAL | The cited issues (#4413 closed not planned, #26874 closed, #26819, #37485 on hold) show that requests were not delivered. No cited page states that 4.x has no such feature. It is an absence claim stronger than the sources. |
| 2 | "An internal issue, 'State case management' ... (#37485)" | PARTIAL | The page shows title, Open, Roadmap "On hold", Classification (`unclassified`, `triaged`, `false positive`) and Notes fields. It does not label the issue as internal (it is a public issue and has a comment from an outside user). Drop "internal". |
| 3 | N7: "The most commented community issues in a search for 'after upgrade' (#24074, #32044)" | PARTIAL | Only #24074 is shown first in that search (126 comments, `pain-github-upgrades-storage` claim 1). #32044 is a separate claim and is not shown in the search list; the note lists #27699, #32820 and #27563 as the other items in the search. |
| 4 | N5 discard: "so does every competitor's assistant ([note])" | PARTIAL | The note covers four vendors (Microsoft, Google SecOps, Elastic, Splunk), chosen by the researcher. "Every competitor" is broader. The note's report also says the Splunk summary wording is broader than the page. |
| 5 | N7 discard: "Wazuh Cloud already removes the problem for hosted customers" (cloud-service/index.html) | PARTIAL | The page supports "Wazuh Cloud manages the Wazuh central components and their underlying infrastructure". It does not say upgrade problems disappear. This is an inference. |
| 6 | N8 discard: advice is "retention policies, replicas and sizing" (thread AfvaXspKhyI), "which is rule-based" | PARTIAL | The thread reply lists deleting old indices and agents, retention policies, zero replicas on single nodes and adding nodes. "Sizing" is a loose reading of "adding nodes". It is one thread (note confidence low), and "rule-based" is the author's own judgement. |
| 7 | N9 discard: "several PeerSpot reviewers praise the documentation" | PARTIAL | The review-sites report shows two dated praise quotes (Sep 15, 2025 and Jul 3, 2026). "Several" is a stretch for two, and the report also shows learning-curve complaints. |
| 8 | Workaround table: "They stop new alerts but leave existing findings visible (#4413)"; "Spreadsheets ... commenters in #26819" | PARTIAL | #4413: a member-badged commenter noted existing alerts stay on the UI and the requester said the rule "basically drops new ones" (OK). #26819: the report shows one commenter "tracking this with a spreadsheet"; "commenters" in the plural is slightly wider. Minor. |
| 9 | Vulnerability need: "Wazuh compares each agent's package inventory with its CTI vulnerability feed and lists the CVEs that match" (docs) | PARTIAL | Fetched. The page says the module "correlates this software inventory data with vulnerability information" from the Wazuh CTI repository (or an offline copy). It does not use "CVE" or "lists the CVEs that match"; it says the module helps "discover vulnerabilities". Wording is close but more specific than the page. |

SUPPORTED (no issue found), grouped:
- GitHub issues, from the reports of `pain-github-*`: #26874 (both quotes, "doesn't scale"), #26819 (maintainer = Member badge, "5.x", no version given), #4413 (since Aug 2022, closed not planned Mar 2026), #24290 (4.8.0 alerts, "by design we will not alert you"), #37485 (On hold, triage-like fields), #18024 (Windows KBs), #19346 (47 thumbs-up, first in thumbs-up sort, bug label), #21706, #3130 (since 2019), #1492 (since 2019), #4091 (32 thumbs-up), #14225, #24118, #24074, #24243 (disk growth after 4.8).
- Google Group threads, from `pain-community-vulnerability-false-positives` report (PASS): listing 13 of ~28 (note: the fetch was truncated, the statement says "about 28" and "our classification"); search 22 of 30; tq7fgojXObg (PHP 7.4 vs 8.2 fix, "High"); mTUXo6txzTU (Canonical feed format, "Solved"); 6tYTimSfZmI (hundreds of alerts after kernel upgrade, rules 23502/23504); DfawqXY7yi0 (about 2,327, Ubuntu 24.04); EETPTa9KrD8 (no resolution events); 1C9sSXLO7b8 (CTI delay).
- PeerSpot, from `pain-community-review-sites` and `users-who-uses-wazuh` reports: 3 of 10 dated cons cite AI/ML; Small Business 23 of 44 reviewers (23+12+9).
- Docs and landscape, from `landscape-builtin-help`, `landscape-wazuh-ai`, `landscape-wazuh-commercial-hub`, `users-mssp-multitenancy`, `landscape-third-party`, `users-use-cases` and `users-customer-stories` reports: 5.0-rc reporting (scheduled, email, pre-release banner); AI Analyst (periodic emailed PDF, vulnerability analysis section); 5.0-rc AI Assistant; Hub beta list with Pharos (Vulnerability & Threat Intelligence), Lumen, Mobius; Mobius response functionality; two MCP servers (vulnerability tools); partners page "centralised multi-tenancy console"; multi-tenancy docs (tenants separate saved objects); vulnerability detection among documented use cases; Groupon use-case list; FirmGuardian as MSSP.
- Note links: statements for N1 to N9 match the claims of the cited notes (checked against note text); every cited note has a PASS report except those listed below.

## Cited notes whose report is not PASS (so PHASE2 statements on them need care)
- `pain-github-vulnerability-detection`: NEEDS FIXES (claim 2: the Contributor who wrote the Dec 2 comment and the one who closed #26874 are two different accounts). PHASE2 does not repeat this detail.
- `pain-github-multi-tenancy`: NEEDS FIXES (claim 2 says organisations "must" block the index; PHASE2 only uses the PARTIAL-free parts: filter by agent group and the DLS title).
- `pain-community-upgrades`: NEEDS FIXES (date range only; counts fine).
- `pain-community-indexer-storage`: NEEDS FIXES (open question about view counts; no effect on PHASE2).
- `landscape-competitor-ai`: NEEDS FIXES (Summary wording on Splunk summaries; related to claim 4 above).
- `landscape-pharos-vesper`: NEEDS FIXES (absence statements scoped too broadly in the note). PHASE2 says "I found no public page that says what it does", which matches the narrowed claim.
- `users-customer-stories`: NEEDS FIXES (claim 9, iSecNG, not used in PHASE2).

## Out of scope, listed only
- Lab statements: Phase 1 observations (alert 40704, "hard to interpret events", item 6 next step), lab environment, N9 "my lab only".
- Inference: "teams that go through audits"; "by its category, Pharos is about vulnerability and threat data ... could complement Pharos".
- UNVERIFIED: how 4.8+ exposes findings; use of external exploitation data.
- Unlabelled reasoning stated as fact (not external claims, but check): "It would also need raw alerts sent to an LLM" (N5), "AI adds little" (N6), "They face the problem once per client" (MSSPs), "Fixing it needs access to the customer's hosts and packages" (N7), scores and totals (own scoring in `phase2-needs.md`).

## Note-level problems
- No front matter is required for PHASE2.md. English. No personal data seen (users and posters are cited by URL only; the researcher names such as the issue authors are not copied).
- Wording that widens sources: items 1 to 9 above.
- Unlabelled inferences presented as statements: "It would also need raw alerts sent to an LLM"; "They face the problem once per client"; "Wazuh Cloud already removes the problem".
- Wazuh 5.0 content is cited from `5.0-rc` pre-release docs; PHASE2 says "pre-release docs" for reporting (good) but not for the AI Assistant (N5 and I6 rows). Add the same qualifier.

## Recommended fixes
- Reword the "no way to record a decision" statement: "I found no built-in way ... in the sources I read; the requests below were closed or are on hold".
- Remove "internal" before "issue" for #37485.
- N7: cite #24074 alone for "most commented in the search" and describe #32044 separately (for example "also long-running").
- N5: change "every competitor's assistant" to "the assistants of Microsoft, Google, Elastic and Splunk".
- N7 discard: change "removes the problem" to "Wazuh Cloud manages the central components" or prefix with `Inference:`.
- N8 discard: say "one thread's reply lists retention policies, replicas and more nodes", and drop or label "which is rule-based".
- N9 discard: "two PeerSpot reviewers praise the documentation".
- Vulnerability docs sentence: use the page's wording ("correlates the software inventory with vulnerability data from the Wazuh CTI repository").
- Add "(pre-release docs)" to the 5.0 AI Assistant mentions.
