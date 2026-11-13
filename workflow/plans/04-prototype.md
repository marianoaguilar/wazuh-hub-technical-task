# Plan 04: mini prototype of the triage ledger (post-delivery)

## Context
Delivery is done (tag `delivery` = `fe914f3`). Defence today, 2026-11-13 at 15:30. This is optional, post-delivery work on a separate branch `prototype`; `main` and the tag are not touched.

Goal: show, with real data from my lab, the core idea of Phase 3: **a person's decision is stored and re-applied on every sync, and what is left becomes a short "fix first" list.**

Timebox: 11:30–13:15. If it does not work by 13:15, stop and go to the mock defence.

## Scope

In:
1. **Export (I run it).** One `curl` as the read-only user `triage-connector` to `wazuh-states-vulnerabilities-*/_search`, only the fields the triage needs (`agent.id`, `package.name`, `package.version`, `vulnerability.id`, `vulnerability.severity`, `vulnerability.score.base`). Saved to `prototype/data/findings.json`, which is git-ignored (lab data stays out of the repo).
2. **Ranking data.** CISA KEV catalogue (public JSON, CC0) downloaded to `prototype/data/`. EPSS only if time is left.
3. **Script `prototype/triage.py`** (Python standard library only):
   - group findings by package name (the action that fixes them: upgrade that package);
   - read `prototype/ledger.json` (decisions: status, reason, owner, expiry, package version at decision time);
   - re-apply each decision; a decision is **reopened** if it expired or the package version changed;
   - print the "fix first" list of open groups, ranked KEV first, then highest CVSS (D8 order, without EPSS if skipped).
4. **Demo** (3 runs): run → record one decision → run (group is gone) → set the expiry in the past → run (group is back, marked "reopened: expired").
5. `prototype/README.md`: what it shows, how to run it, what is left out.

Out: AI proposal, web UI, Postgres, auth, connector service, aliases for host names. In the defence: "the AI proposes, the person confirms; here I prototyped confirm and re-apply".

## Acceptance tests (written first, `prototype/test_triage.py`, unittest)
1. A valid decision is re-applied: the group is not in the fix-first list.
2. A decision whose expiry is in the past is reopened ("reopened: expired").
3. A decision taken for another package version is reopened ("reopened: package changed").
4. Ranking: a group with a KEV CVE comes before a group with a higher CVSS but no KEV CVE.

## Process (light version of `phase4/agent-setup/pipeline.md`)
Plan approved by me (step 2) → branch `prototype`, tests first, then code, then README (step 3) → tests run locally before each commit (step 5) → I review the code with Claude (step 6; no separate reviewer agent, token budget) → commit only with my OK, no merge to `main` (step 7). Steps 8–11 do not apply.

## Changes during the work
- EPSS added (time allowed it), with acceptance test 5: without KEV, a group with higher EPSS goes before a group with higher CVSS. Ranking is now KEV → EPSS → CVSS, as in D8.

## Rules
- I run the lab command; Claude only gives it and reads the result (lab-work-by-user).
- No hostnames or tokens in committed files; `prototype/data/` git-ignored.
- Commits only after my OK, prefix `prototype:`; no push unless I ask.
