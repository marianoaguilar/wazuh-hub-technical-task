# Phase 2: needs catalogue and shortlist

Step 4 of [`../workflow/plans/01-phase2.md`](../workflow/plans/01-phase2.md). Every row cites
verified notes by key and claim number (e.g. `PGV 1` = claim 1 of the note keyed `PGV`). Scores
and the "Inference" lines are my judgement, not facts from the sources.

## Source keys

| Key | Note | Key | Note |
|-----|------|-----|------|
| LAB | [lab-phase1-observations](sources/lab-phase1-observations.md) | PCV | [pain-community-vulnerability-false-positives](sources/pain-community-vulnerability-false-positives.md) |
| UWU | [users-who-uses-wazuh](sources/users-who-uses-wazuh.md) | PCA | [pain-community-alert-tuning](sources/pain-community-alert-tuning.md) |
| UCS | [users-customer-stories](sources/users-customer-stories.md) | PCS | [pain-community-indexer-storage](sources/pain-community-indexer-storage.md) |
| UUC | [users-use-cases](sources/users-use-cases.md) | PCR | [pain-community-reporting](sources/pain-community-reporting.md) |
| UDC | [users-deployment-and-cloud](sources/users-deployment-and-cloud.md) | PCM | [pain-community-multi-tenancy](sources/pain-community-multi-tenancy.md) |
| UMT | [users-mssp-multitenancy](sources/users-mssp-multitenancy.md) | PCU | [pain-community-upgrades](sources/pain-community-upgrades.md) |
| PGV | [pain-github-vulnerability-detection](sources/pain-github-vulnerability-detection.md) | PRS | [pain-community-review-sites](sources/pain-community-review-sites.md) |
| PGF | [pain-github-false-positives-noisy-rules](sources/pain-github-false-positives-noisy-rules.md) | LAI | [landscape-wazuh-ai](sources/landscape-wazuh-ai.md) |
| PGU | [pain-github-upgrades-storage](sources/pain-github-upgrades-storage.md) | LHB | [landscape-wazuh-commercial-hub](sources/landscape-wazuh-commercial-hub.md) |
| PGM | [pain-github-multi-tenancy](sources/pain-github-multi-tenancy.md) | LBH | [landscape-builtin-help](sources/landscape-builtin-help.md) |
| PGC | [pain-github-custom-rules-decoders](sources/pain-github-custom-rules-decoders.md) | LTP | [landscape-third-party](sources/landscape-third-party.md) |
| PGD | [pain-github-dashboard-reporting-compliance](sources/pain-github-dashboard-reporting-compliance.md) | LCA | [landscape-competitor-ai](sources/landscape-competitor-ai.md) |
| LRT | [landscape-rule-tuning-guidance](sources/landscape-rule-tuning-guidance.md) | LPV | [landscape-pharos-vesper](sources/landscape-pharos-vesper.md) |

## Scoring (1–3, higher is better)

- **Evidence**: number and independence of sources, frequency signals.
- **Pain**: time lost, risk, how often it happens.
- **SaaS fit**: can a service outside the customer's servers deliver it using the Wazuh server
  API / indexer data?
- **AI fit**: does AI add real value, or is it a plain feature?
- **Not solved**: 3 = nothing found that covers it; 1 = Wazuh or a common tool already covers it.
- **Data risk**: 3 = only metadata or metrics leave the customer; 2 = inventory or alert content
  leaves but can be minimised; 1 = raw events or several customers' data must leave.

**Gate:** the Hub team builds SaaS services that extend Wazuh with AI, so a need with SaaS fit 1
or AI fit 1 is discarded whatever its total.

## Catalogue

### N1. Vulnerability triage: acknowledge, explain and prioritise CVE findings
- **Evidence.** GitHub: no way to acknowledge, exclude or annotate CVEs (PGV 1, 3, 4; #26874 5 👍,
  22 comments; #26819 7 👍, still Open on its page; #4413 closed as not planned in Mar 2026);
  for 4.8.0 agents no alerts in wazuh-alerts-* and "by design" no alert on inventory refresh, so
  resolution history is incomplete (PGV 8; PGD 7; PCV 9); some changes still raise alerts (PCV 7). Forum: 13 of the ~28
  visible threads in the default listing are about vulnerability detection (PCV 1); 22 of 30
  results for "false positive" (PCV 2); cases: patched packages flagged (PCV 3), feed changes
  marking CVEs "Solved" (PCV 5), bursts of hundreds of alerts users had to reason out (PCV 6, 7),
  thousands of findings on an up-to-date host (PCV 8). Lab: reviewing which detected
  vulnerabilities matter was left as a next step (LAB 6).
- **Who.** Anyone using vulnerability detection, a core use case (UUC 1, UCS 2); MSSPs doing
  vulnerability scanning for clients (UCS 4).
- **How they handle it today.** Custom suppression rules, which stop new alerts but leave existing
  findings (PGV 5; PCV 6); filters and saved searches, which "don't scale" (PGV 2); waiting for a
  feed update or reasoning it out themselves (PCV 4, 7).
- **Already served?** Not in 4.x (LBH 6 describes detection only). An internal "State case
  management" issue proposes triage fields and is On hold (PGV 6). Hub beta service **Pharos**
  is in the "Vulnerability & Threat Intelligence" category, and no public page says what it does
  (LPV 1, 2).
- **Scores.** Evidence 3 · Pain 3 · SaaS fit 3 · AI fit 3 · Not solved 2 · Data risk 2 = **16**
- Inference: AI fits well here: explaining why a finding is a false positive (backported
  patches, old kernels, superseded KBs) and ranking what to fix first are reasoning tasks over
  inventory + CVE data. The main risk is overlap with Pharos and the 5.x roadmap.

### N2. Alert noise: finding noisy rules and tuning them safely
- **Evidence.** GitHub: the most reacted bug is a rootcheck false positive (#19346, 47 👍, 2023–
  2026; reported fixed by 4.13.1) (PGF 1, 2); more noisy defaults: #20363 open (PGF 3), Sysmon
  rule 92214 at level 15 (PGF 5), hundreds of FIM rule 550 alerts on macOS (PGF 6). Forum: at
  least 9 tuning/suppression threads Oct 2025–Aug 2026 (PCA 1), suppression rules that do not
  work as expected (PCA 2, 3, 4). Lab: a repeating level-5 alert filled the dashboard and needed
  outside research (LAB 1, 2); harmless FIM changes look like suspicious ones (LAB 8).
- **Who.** Every operator; most visible for small teams without a dedicated rules engineer
  (PeerSpot reviewers are mostly small businesses, UWU 9).
- **How they handle it today.** Hand-written child rules, level 0, overwrite, CDB lists, or
  disabling modules (PGF 2, 5; LRT 1–6); single-log testing with `wazuh-logtest` (LRT 7). No page
  read explains how to find the rules that fire most (LRT 8, 14). A ruleset regression harness
  exists in the repo but is not documented for users (LRT 9, 10).
- **Already served?** The mechanisms are documented (LBH 1–5), but not the workflow (find noise →
  propose a change → test → check nothing else broke). Wazuh 5.x adds a Draft → Test → Custom
  content chain (LRT 13). Competitors market triage agents that judge true/false positives (LCA 4).
- **Scores.** Evidence 3 · Pain 2 · SaaS fit 3 · AI fit 3 · Not solved 2 · Data risk 2 = **15**
- Inference: AI can draft the child rule and explain it; `PUT /logtest` (LRT 7) lets a service
  test the change through the API before the user deploys it.

### N3. Custom decoders and rules for unsupported log formats
- **Evidence.** Fields not decoded, Windows eventchannel decoders not modifiable until 5.0
  (PGC 1, 2; #21706, 26 comments); requests for rules scoped by agent label (PGC 5, #3130 18 👍;
  PGM 6); top-voted rule-writing discussions (PGC 4). Case studies use custom rules and decoders
  (UCS 4, 7).
- **Who.** Teams onboarding non-standard sources; MSSPs (UCS 4).
- **How they handle it today.** Regex decoders tested in `wazuh-logtest`, hostname matching or
  CDB lists as workarounds (PGC 2, 5).
- **Already served?** Partly: logtest (LBH 5) and, in 5.x, the content promotion chain (LRT 13).
- **Scores.** Evidence 2 · Pain 2 · SaaS fit 2 · AI fit 3 · Not solved 2 · Data risk 2 = **13**
- Inference: close to N2 (same ruleset, same test tools); it could be one service with N2.

### N4. Reporting and compliance reports
- **Evidence.** Scheduled PDF reports open since 2019 (PGD 3), ISO 27001 content 32 👍 since 2019
  (PGD 1); 11 forum reporting threads Dec 2024–Jun 2026 (PCR 1), PDF and CSV limits (PCR 2, 3).
- **How they handle it today.** Per-dashboard "Generate report", `<report>` in ossec.conf, cron +
  reporting CLI, export to Grafana/Power BI (PCR 2–5).
- **Already served?** Wazuh 5.0 adds scheduled reports with email delivery (LBH 10); Wazuh Cloud's
  AI Analyst emails periodic PDF reports (LHB 5, 6).
- **Scores.** Evidence 3 · Pain 2 · SaaS fit 3 · AI fit 2 · Not solved 1 · Data risk 2 = **13**
- **Discarded:** Wazuh is already shipping both the plain feature (5.0) and the AI version (AI Analyst).

### N5. Explaining alerts and guided investigation for less experienced users
- **Evidence.** Lab only, plus weak external signals: hard to interpret events, not knowing what to
  do next (LAB 2, 3, 4); 3 of 10 dated PeerSpot excerpts cite missing AI/ML (PRS 2).
- **Already served?** Strongly covered: the 5.0 dashboard AI Assistant (LAI 8, 9), AI Analyst in
  Cloud (LHB 5), Hub beta services Lumen and Mobius (agentic SOC) (LHB 12), open-source MCP servers
  and an agentic SOC (LTP 1–4), and every competitor's assistant (LCA 1–6).
- **Scores.** Evidence 2 · Pain 2 · SaaS fit 3 · AI fit 3 · Not solved 1 · Data risk 1 = **12**
- **Discarded:** the most crowded space, including Wazuh's own 5.0 assistant and Hub services; it
  also needs raw alert content sent to an LLM.

### N6. Multi-tenancy for MSSPs
- **Evidence.** GitHub: filter by agent.group (#14225, 13 👍, open since 2022), vulnerability data
  ignores document-level security (#24118), tenant-based rules (#25370) (PGM 1–5). Forum: 11
  threads Mar 2025–Oct 2026, 30 since 2023 (PCM 1); dashboard tenants do not isolate data
  (PCM 2; UMT 1, 2).
- **Who.** MSSPs and SOC providers (UCS 4, 5, 9, 10).
- **How they handle it today.** One cluster per customer plus cross-cluster search (UMT 3, 4, 5, 7;
  PCM 3), or agent groups + DLS + RBAC with gaps (PCM 3, 4).
- **Scores.** Evidence 3 · Pain 3 · SaaS fit 2 · AI fit 1 · Not solved 2 · Data risk 1 = **12**
- **Discarded (gate: AI fit 1):** a data-isolation and access-control problem in the core product;
  AI adds little. A partner "centralised multi-tenancy console" is already listed (UMT 6).

### N7. Upgrades that break things
- **Evidence.** The most commented community issues: #24074 (126 items), #32044 (85+), #33038 (PGU
  1–4); about 10 forum threads Jun–Nov 2026 (PCU 1–5).
- **How they handle it today.** Trial and error on certificates, keystore, `/tmp noexec` (PGU 2, 3).
- **Scores.** Evidence 3 · Pain 3 · SaaS fit 1 · AI fit 2 · Not solved 3 · Data risk 2 = **14**
- **Discarded (gate: SaaS fit 1):** fixing it needs access to the customer's hosts and packages;
  Wazuh Cloud already removes it for hosted customers (UDC 4).

### N8. Indexer storage growth and retention
- **Evidence.** RocksDB / queue disk growth (PGU 6, 7); 6 forum threads (PCS 1–4); PeerSpot storage
  outages (PCS 8).
- **How they handle it today.** ISM retention policies, fewer replicas, more disk or nodes (PCS 2–4, 7).
- **Scores.** Evidence 2 · Pain 2 · SaaS fit 2 · AI fit 1 · Not solved 2 · Data risk 3 = **12**
- **Discarded (gate: AI fit 1):** rule-based sizing and ISM advice; no need for AI.

### N9. Getting started: choosing an install method and what to do next
- **Evidence.** Lab only (LAB 4, 5); PeerSpot opinions on documentation are split (PRS 5).
- **Scores.** Evidence 1 · Pain 1 · SaaS fit 2 · AI fit 2 · Not solved 2 · Data risk 3 = **11**
- **Discarded:** weak evidence beyond my own experience; several reviewers praise the docs.

## Summary table

| # | Need | Ev. | Pain | SaaS | AI | Not solved | Data | Total | Status |
|---|------|-----|------|------|----|-----------|------|-------|--------|
| N1 | Vulnerability triage | 3 | 3 | 3 | 3 | 2 | 2 | **16** | Shortlist |
| N2 | Alert noise and rule tuning | 3 | 2 | 3 | 3 | 2 | 2 | **15** | Shortlist |
| N7 | Upgrades that break | 3 | 3 | 1 | 2 | 3 | 2 | 14 | Discarded (gate) |
| N3 | Custom decoders and rules | 2 | 2 | 2 | 3 | 2 | 2 | **13** | Shortlist |
| N4 | Reporting, compliance reports | 3 | 2 | 3 | 2 | 1 | 2 | 13 | Discarded (served) |
| N5 | Explaining alerts | 2 | 2 | 3 | 3 | 1 | 1 | 12 | Discarded (served) |
| N6 | MSSP multi-tenancy | 3 | 3 | 2 | 1 | 2 | 1 | 12 | Discarded (gate) |
| N8 | Indexer storage | 2 | 2 | 2 | 1 | 2 | 3 | 12 | Discarded (gate) |
| N9 | Getting started | 1 | 1 | 2 | 2 | 2 | 3 | 11 | Discarded (evidence) |

## Limits of this evidence
- Community evidence is mostly one forum (Wazuh Google Group) plus PeerSpot; Reddit, G2, Capterra
  and Gartner could not be read.
- Thread counts are the researcher's classification of search results, not exact measures.
- What Pharos, Lumen and Mobius do is not public (LPV 1–7), so "Not solved" for N1, N2 and N5 may
  be overstated.

## Recommendation (agent; the choice is yours)
Inference: **N1, vulnerability triage**. It has the strongest and most independent evidence
(GitHub, forum, my lab), a clear "today" workaround that users say does not work, data that the
Wazuh API and indexer already expose, and a real job for AI (explaining false positives,
prioritising). Its main risk is overlap with Pharos and the 5.x "State case management" idea;
Phase 3 would have to position the service next to them (for example as the triage layer on top
of detection, for 4.x users now). **N2 + N3 combined (ruleset tuning)** is the alternative with less
overlap risk but somewhat weaker pain.

## Decision (human)
2026-11-10: I chose **N1, vulnerability triage**, after an explanation of the catalogue and of N1
from the basics. Condition: every claim used in `PHASE2.md` must be justified with verified
sources, and the Pharos overlap and the limits above must be stated openly. Next step:
[`phase2-ideas.md`](phase2-ideas.md).
