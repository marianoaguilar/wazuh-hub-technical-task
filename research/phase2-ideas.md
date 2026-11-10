# Phase 2: service ideas for N1 (vulnerability triage)

Step 5 of [`../workflow/plans/01-phase2.md`](../workflow/plans/01-phase2.md). The chosen need is
N1 in [`phase2-needs.md`](phase2-needs.md). Source keys (e.g. `PGV 1`) are the same as in that
file. "Inference" lines and the keep/drop decisions are my judgement, not facts from the sources.

## What any idea has to fix (from the evidence)
1. No place to record a decision on a finding: acknowledged, false positive, accepted risk, with
   who / why / until when (PGV 1, 2, 3, 4).
2. Too many findings to review by hand; filters "don't scale" (PGV 1, 2; PCV 8).
3. False positives whose cause users must work out alone: backports, installed KBs, feed changes
   (PCV 3, 5; PGV 7).
4. Bursts of new findings nobody can explain (PCV 6, 7).
5. Incomplete history of resolved vulnerabilities (no alerts for 4.8.0 agents, none "by design" on
   inventory refresh), which hurts audits (PGV 8; PGD 7; PCV 9).

## Ideas

### I1. Triage ledger with AI false-positive review
- **What it does.** Keeps an external record of a decision per finding (status, reason, owner,
  expiry) and re-applies it every time the findings are synced. For each finding or group of
  findings, an AI step proposes "likely false positive / real / accepted risk" with a short
  explanation and the evidence it used (package version, distro, fixed version). A person
  confirms or rejects; nothing is hidden without a human decision.
- **Data from Wazuh.** Vulnerability findings (CVE ID, package, version, severity, agent OS) and
  the package inventory. Agent names can be replaced by pseudonymous IDs.
  UNVERIFIED: the exact API endpoint or indexer index that exposes findings in 4.8+; it has to be
  checked in the lab in Phase 3.
- **Where AI fits.** Reasoning over package version + distro + CVE data to explain false
  positives (the cases in PCV 3, 5 and PGV 7), grouping similar findings so one decision covers
  many.
- **Fixes:** 1, 2, 3 (and 5 partly, because decisions are kept with dates).
- **Status: KEEP (core).** It answers the gap Wazuh has open (PGV 6, "State case management",
  On hold) from outside the cluster.

### I2. "Fix first" prioritised queue
- **What it does.** Orders the remaining (not dismissed) findings into a short work list: which
  hosts and packages to patch first, and why.
- **Data from Wazuh.** Same as I1, plus an asset criticality the user sets (e.g. "internet-facing").
- **Where AI fits.** Writing the reason for each position in the queue and turning many CVEs into
  a few actions ("upgrade package X on 12 hosts closes 140 findings"). Inference: the grouping
  into actions is plain logic; AI adds the explanation.
- **Fixes:** 2.
- **Status: KEEP, as part of I1.** UNVERIFIED: using external exploitation data (for example lists
  of CVEs exploited in the wild) has not been researched; it needs a researcher pass and
  verification before Phase 3 relies on it.

### I3. Change explainer and digest
- **What it does.** Compares snapshots of findings between syncs and explains what changed:
  "300 new findings come from a kernel upgrade on 2 hosts", "40 CVEs marked Solved after a feed
  change, no package changed".
- **Where AI fits.** Explaining the cause of a burst in plain words (the cases in PCV 5, 7).
- **Fixes:** 4, and 5 (the snapshots are the missing history).
- **Status: KEEP AS A FEATURE of I1, DROP as a standalone service.** A periodic report alone
  overlaps with the Wazuh Cloud AI Analyst, which already emails PDF reports that cover
  vulnerabilities (LHB 5), and with 5.0 scheduled reports (LBH 10).

### I4. Compliance evidence pack
- **What it does.** Exports, for an audit, who accepted which risk, when, and when each finding
  was resolved.
- **Fixes:** 5.
- **Status: DROP as a separate service; keep as an export of I1.** Reporting is already served
  (N4 discarded in `phase2-needs.md`); the only new part is the triage history, which I1 already
  stores.

### I5. Second-opinion scanner (own detection engine)
- **What it does.** Re-scans the inventory against distro advisories to "correct" Wazuh results.
- **Status: DROP.** It duplicates the core detector and the Wazuh CTI feed (LBH 6), means
  maintaining vulnerability feeds, and is the idea most likely to overlap with Pharos, whose
  category is "Vulnerability & Threat Intelligence" (LPV 1). Inference: it competes with Wazuh
  instead of extending it.

### I6. Chat assistant "ask about my vulnerabilities"
- **What it does.** Natural-language questions over the findings.
- **Status: DROP.** Crowded: the 5.0 dashboard AI Assistant (LAI 8, 9), open-source MCP servers
  that already expose vulnerability tools (LTP 1, 3), competitor assistants (LCA 1–6). A chat does
  not store decisions, so it does not fix problem 1.

### I7. Automatic remediation (patching hosts)
- **What it does.** Applies upgrades on agents after triage.
- **Status: DROP.** It needs write access to customer hosts, which is a much bigger risk and the
  same SaaS-fit problem that discarded N7; response actions are also the area of Hub service
  Mobius (LHB 12, 13). Inference: it can come later as a hand-off (a ticket or a command for the
  admin), not as automatic action.

## Summary

| # | Idea | Fixes | Main reason | Status |
|---|------|-------|-------------|--------|
| I1 | Triage ledger + AI false-positive review | 1, 2, 3, (5) | The open gap (PGV 6) | **Keep (core)** |
| I2 | Prioritised "fix first" queue | 2 | Small extension of I1 | Keep, inside I1 |
| I3 | Change explainer / digest | 4, 5 | Standalone overlaps AI Analyst (LHB 5) | Feature of I1 |
| I4 | Compliance evidence pack | 5 | Reporting already served (N4) | Export of I1 |
| I5 | Second-opinion scanner | 3 | Duplicates CTI / possible Pharos overlap | Drop |
| I6 | Chat over vulnerabilities | 2 | Crowded (LAI 8, LTP 1, 3) | Drop |
| I7 | Automatic remediation | — | Host write access; Mobius area | Drop |

## Recommendation (agent; the choice is yours)
Inference: **I1 with I2 as the MVP**, and I3 / I4 as later features. One service with one clear
job: "decide once, remember the decision, and get an explained, short list of what to fix".
Its position next to Pharos: Pharos (by its category) is about vulnerability and threat data; this
service is about the user's decisions on that data. That cannot be confirmed while Pharos has no
public description (LPV 1–7), and `PHASE2.md` has to say so.

## Open items before Phase 3
- UNVERIFIED: how findings are exposed in 4.8+ (API endpoint or indexer index); check in the lab.
- UNVERIFIED: external exploitation data for prioritisation (I2); needs one researcher pass + verifier.

## Decision (human)
2026-11-10: I chose **I1 + I2** (triage ledger with AI false-positive review, plus the
prioritised "fix first" queue) as the service for Phase 3. I3 and I4 stay as later features;
I5, I6 and I7 are dropped for the reasons above.
