# Research

Sources and notes behind PHASE2.md and PHASE3.md.

## How to read this folder

1. Start with [`../PHASE2.md`](../PHASE2.md): the answers, each with links to the notes below.
2. Then [`phase2-needs.md`](phase2-needs.md): every candidate need, its scores and its notes, and
   [`phase2-ideas.md`](phase2-ideas.md): the service ideas for the chosen need.
3. Open a note in `sources/` only to check a claim: every claim has its URL, a quote and a
   confidence level.
4. The AI mistakes found along the way are in [`ai-log.md`](ai-log.md) (Phase 2: rows 2–9). Each note
   lists what was corrected in its "Changes after verification" section.
5. Reports in `verification/` show the **latest** check of each note. The first-round reports
   (with most of the findings) were overwritten by the second round; their findings survive in
   `ai-log.md` and in each note's "Changes after verification" section.

## How notes are made

1. I write a prompt for the `researcher` agent (saved in `workflow/prompts/`).
2. `researcher` writes one note per source or topic in `sources/`, each claim with a URL and a quote.
3. `verifier` fetches every cited URL and writes a report per note in `verification/`.
4. I review both. Only claims that passed verification are used in the PHASE files.
5. Corrections I make to the AI go in [`ai-log.md`](ai-log.md).

Agent definitions: [`../.claude/agents/`](../.claude/agents/). Rules: [`../CLAUDE.md`](../CLAUDE.md).

## Index

Status: **PASS** = the latest report passes. **PASS\*** = the latest report found one small
problem (so its header still says `NEEDS FIXES`); I fixed it as the report suggested and logged it
in the note, without a further check.

### Own lab
| Note | Topic | Verification |
|------|-------|--------------|
| [lab-phase1-observations](sources/lab-phase1-observations.md) | First-hand needs from Phase 1 | n/a (cites my own lab, no URLs) |

### R1: who uses Wazuh ([prompt](../workflow/prompts/phase2/01-users.md), [fixes](../workflow/prompts/phase2/05a-fixes-users.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [users-who-uses-wazuh](sources/users-who-uses-wazuh.md) | Who uses Wazuh, adoption numbers | [PASS](verification/users-who-uses-wazuh.verify.md) |
| [users-customer-stories](sources/users-customer-stories.md) | Case studies | [PASS\*](verification/users-customer-stories.verify.md) |
| [users-use-cases](sources/users-use-cases.md) | Documented use cases | [PASS](verification/users-use-cases.verify.md) |
| [users-deployment-and-cloud](sources/users-deployment-and-cloud.md) | Deployment, Wazuh Cloud pricing | [PASS](verification/users-deployment-and-cloud.verify.md) |
| [users-mssp-multitenancy](sources/users-mssp-multitenancy.md) | MSSP and multi-tenant use | [PASS](verification/users-mssp-multitenancy.verify.md) |

### R2: problems reported on GitHub ([prompt](../workflow/prompts/phase2/02-pain-github.md), [fixes](../workflow/prompts/phase2/05b-fixes-pain-github.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [pain-github-vulnerability-detection](sources/pain-github-vulnerability-detection.md) | Vulnerability triage | [PASS\*](verification/pain-github-vulnerability-detection.verify.md) |
| [pain-github-false-positives-noisy-rules](sources/pain-github-false-positives-noisy-rules.md) | False positives in default rules | [PASS](verification/pain-github-false-positives-noisy-rules.verify.md) |
| [pain-github-upgrades-storage](sources/pain-github-upgrades-storage.md) | Upgrades, disk growth | [PASS](verification/pain-github-upgrades-storage.verify.md) |
| [pain-github-multi-tenancy](sources/pain-github-multi-tenancy.md) | Multi-tenant gaps | [PASS\*](verification/pain-github-multi-tenancy.verify.md) |
| [pain-github-custom-rules-decoders](sources/pain-github-custom-rules-decoders.md) | Custom rules and decoders | [PASS](verification/pain-github-custom-rules-decoders.verify.md) |
| [pain-github-dashboard-reporting-compliance](sources/pain-github-dashboard-reporting-compliance.md) | Dashboards, reporting, compliance | [PASS](verification/pain-github-dashboard-reporting-compliance.verify.md) |

### R3: problems reported in the community ([prompt](../workflow/prompts/phase2/03-pain-community.md), [fixes](../workflow/prompts/phase2/05c-fixes-pain-community.md))
Mostly the public Wazuh Google Group and PeerSpot. Reddit could not be fetched; G2, Capterra and
Gartner returned 403; Stack Overflow / Server Fault were not covered.

| Note | Topic | Verification |
|------|-------|--------------|
| [pain-community-vulnerability-false-positives](sources/pain-community-vulnerability-false-positives.md) | Vulnerability false positives | [PASS](verification/pain-community-vulnerability-false-positives.verify.md) |
| [pain-community-indexer-storage](sources/pain-community-indexer-storage.md) | Indexer storage, retention | [PASS\*](verification/pain-community-indexer-storage.verify.md) |
| [pain-community-reporting](sources/pain-community-reporting.md) | Reporting | [PASS](verification/pain-community-reporting.verify.md) |
| [pain-community-multi-tenancy](sources/pain-community-multi-tenancy.md) | Multi-tenancy | [PASS](verification/pain-community-multi-tenancy.verify.md) |
| [pain-community-alert-tuning](sources/pain-community-alert-tuning.md) | Alert tuning, suppression | [PASS\*](verification/pain-community-alert-tuning.verify.md) |
| [pain-community-upgrades](sources/pain-community-upgrades.md) | Upgrades changing behaviour | [PASS\*](verification/pain-community-upgrades.verify.md) |
| [pain-community-review-sites](sources/pain-community-review-sites.md) | PeerSpot reviews | [PASS](verification/pain-community-review-sites.verify.md) |

### R4: what already exists ([prompt](../workflow/prompts/phase2/04-landscape.md), [fixes](../workflow/prompts/phase2/05d-fixes-landscape.md), [extra pass](../workflow/prompts/phase2/06-rule-tuning-and-pharos.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [landscape-wazuh-ai](sources/landscape-wazuh-ai.md) | Wazuh's own AI work | [PASS](verification/landscape-wazuh-ai.verify.md) |
| [landscape-wazuh-commercial-hub](sources/landscape-wazuh-commercial-hub.md) | Wazuh Cloud, support, Hub beta services | [PASS](verification/landscape-wazuh-commercial-hub.verify.md) |
| [landscape-builtin-help](sources/landscape-builtin-help.md) | Built-in tuning, testing, reporting | [PASS](verification/landscape-builtin-help.verify.md) |
| [landscape-third-party](sources/landscape-third-party.md) | Third-party AI and SOAR tools | [PASS](verification/landscape-third-party.verify.md) |
| [landscape-competitor-ai](sources/landscape-competitor-ai.md) | AI assistants in other SIEMs | [PASS\*](verification/landscape-competitor-ai.verify.md) |
| [landscape-rule-tuning-guidance](sources/landscape-rule-tuning-guidance.md) | Rule tuning and testing guidance | [PASS\*](verification/landscape-rule-tuning-guidance.verify.md) (2 claims fixed) |
| [landscape-pharos-vesper](sources/landscape-pharos-vesper.md) | Wazuh Pharos and Vesper | [PASS\*](verification/landscape-pharos-vesper.verify.md) (summary wording fixed) |

### PHASE2.md itself ([prompt](../workflow/prompts/phase2/09-verify-phase2.md))
| File | Topic | Verification |
|------|-------|--------------|
| [`../PHASE2.md`](../PHASE2.md) | Phase 2 answers | [NEEDS FIXES → fixed](verification/PHASE2.verify.md) (0 not supported; 9 partial, all reworded, see `ai-log.md` row 9) |

### Phase 3: own lab API responses ([plan step 1](../workflow/plans/02-phase3.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [lab-api-vulnerability-data](sources/lab-api-vulnerability-data.md) | Real, redacted Wazuh API and indexer responses from my lab (`lab/api/`); claims 10–14 (2026-11-11): test of the connector's read-only indexer role (`lab/api/10`) | n/a (cites my own lab, no URLs) |

### R5: connecting to Wazuh ([prompt](../workflow/prompts/phase3/01-wazuh-access.md), [verification prompt](../workflow/prompts/phase3/03-verify-design-notes.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [design-wazuh-access-server-api-rbac](sources/design-wazuh-access-server-api-rbac.md) | Server API auth and RBAC | [NEEDS FIXES → fixed](verification/design-wazuh-access-server-api-rbac.verify.md) |
| [design-wazuh-access-indexer-security](sources/design-wazuh-access-indexer-security.md) | Indexer users, roles, exposure | [NEEDS FIXES → fixed](verification/design-wazuh-access-indexer-security.verify.md) |
| [design-wazuh-access-vulnerability-index](sources/design-wazuh-access-vulnerability-index.md) | Where 4.8+ keeps findings | [NEEDS FIXES → fixed](verification/design-wazuh-access-vulnerability-index.verify.md) |
| [design-wazuh-access-inventory](sources/design-wazuh-access-inventory.md) | Syscollector inventory endpoints | [NEEDS FIXES → fixed](verification/design-wazuh-access-inventory.verify.md) |

### R6: ranking data and the model ([prompt](../workflow/prompts/phase3/02-ranking-and-llm.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [design-ranking-cisa-kev](sources/design-ranking-cisa-kev.md) | CISA KEV catalog | [NEEDS FIXES → fixed](verification/design-ranking-cisa-kev.verify.md) |
| [design-ranking-first-epss](sources/design-ranking-first-epss.md) | FIRST EPSS | [PASS](verification/design-ranking-first-epss.verify.md) |
| [design-ranking-wazuh-kev-epss-support](sources/design-ranking-wazuh-kev-epss-support.md) | Whether Wazuh uses KEV/EPSS | [NEEDS FIXES → fixed](verification/design-ranking-wazuh-kev-epss-support.verify.md) |
| [design-llm-claude-pricing-data-terms](sources/design-llm-claude-pricing-data-terms.md) | Claude prices, data terms, Bedrock EU | [NEEDS FIXES → fixed](verification/design-llm-claude-pricing-data-terms.verify.md) |

All R5/R6 fixes: 12 partial claims reworded inline, see `ai-log.md` row 11.

### Phase 3 decisions, diagrams and PHASE3.md
| File | Topic | Verification |
|------|-------|--------------|
| [phase3-decisions.md](phase3-decisions.md) | Decisions D1–D8 with options; I chose each | n/a (my decisions; facts link to the notes above) |
| [`../diagrams/src/`](../diagrams/src/) d1–d3 | Phase 3 diagrams | [outside review](verification/phase3-diagrams.review.md) ([prompt](../workflow/prompts/phase3/04-review-diagrams.md)), see `ai-log.md` row 12 |
| [`../PHASE3.md`](../PHASE3.md) | Phase 3 answers | [NEEDS FIXES → fixed](verification/PHASE3.verify.md) ([prompt](../workflow/prompts/phase3/05-verify-phase3.md)) (0 not supported; 12 partial, all reworded, see `ai-log.md` row 13) |

### R7: Claude Code tooling ([prompt](../workflow/prompts/phase4/01-claude-code-tooling.md), [verification prompt](../workflow/prompts/phase4/02-verify-phase4.md))
| Note | Topic | Verification |
|------|-------|--------------|
| [tooling-claude-code-instructions-agents](sources/tooling-claude-code-instructions-agents.md) | CLAUDE.md, subagents, skills | [PASS](verification/tooling-claude-code-instructions-agents.verify.md) |
| [tooling-claude-code-permissions-hooks-sandbox](sources/tooling-claude-code-permissions-hooks-sandbox.md) | Permissions, hooks, sandbox | [NEEDS FIXES → fixed](verification/tooling-claude-code-permissions-hooks-sandbox.verify.md) (2 quotes made verbatim, sandbox claim added) |
| [tooling-claude-code-ci-worktrees-mcp](sources/tooling-claude-code-ci-worktrees-mcp.md) | Worktrees, headless/CI, GitHub Action, MCP | [NEEDS FIXES → fixed](verification/tooling-claude-code-ci-worktrees-mcp.verify.md) (1 wording fixed) |

### PHASE4.md and the example agent setup
| File | Topic | Verification |
|------|-------|--------------|
| [`../PHASE4.md`](../PHASE4.md), [`../phase4/agent-setup/`](../phase4/agent-setup/) | Phase 4 answers and example setup | [NEEDS FIXES → fixed](verification/PHASE4.verify.md) (3 not supported, 12 partial, all reworded, see `ai-log.md` rows 14–15) |
