# Phase 3 plan: design the service (vulnerability triage ledger + "fix first" queue)

## Context
Phase 2 is done and pushed (`a8d15c7`). Chosen need: **N1 vulnerability triage**. Chosen service: **I1 + I2** — an external ledger of decisions per finding (status, reason, owner, expiry, re-applied on every sync), AI that proposes "likely false positive / real / accepted risk" with evidence and a human who confirms, plus a ranked "fix first" queue. I3 (change explainer) and I4 (compliance export) are later features.

Brief, Phase 3 deliverables:
- **3 diagrams** (source in `diagrams/src/`): (D1) components + data flow; (D2) one user request end to end, with every AI call and every human step; (D3) where each customer's data goes and who/what can read it.
- **`PHASE3.md`** answering 8 questions: what/for whom; how it connects to Wazuh + what data, **with real API responses from my lab**; tenant isolation + auth; where AI fits, what can go wrong, how it is controlled; how we know answers are good and notice drift; Wazuh API or model down; cost and main risks; main decisions and discarded alternatives.

Open points carried from Phase 2: (a) how 4.8+ exposes findings (server API vs indexer `wazuh-states-vulnerabilities-*`) — check in the lab; (b) external exploitation data (e.g. CISA KEV, EPSS) for ranking — research + verify.

Constraints: CLAUDE.md rules (English, own lab, redact tokens/hostnames/public IPs, sources for claims, no commits without OK), token budget (max 2–3 agents at once, one verifier per batch), PHASE docs one line per paragraph.

## Time budget (13 h left: ~3 h today, ≤10 h tomorrow)
Deadline confirmed: **2026-11-11 at night** (delivery = push + email to HR). No time after tomorrow, so the plan keeps a buffer and Phase 3 stays lean; if something slips, cut depth (optional RBAC user, cost detail), never the required deliverables.

| When | Block | Time |
|------|-------|------|
| Today | Steps 0–3 (plan, lab API, research, design decisions) | ~3 h |
| Tomorrow AM | Steps 4–6 (diagrams, PHASE3.md, verify + commit) — Phase 3 closed by ~14:00 | ~4.5 h |
| Tomorrow PM | Phase 4 (separate plan `03-phase4.md`; much material already exists: CLAUDE.md, agents, hook, ai-log) | ~3.5 h |
| Tomorrow evening | README, final pass of all PHASE files, public-repo check, push, email | ~1 h |
| | Buffer | ~1 h |

## Steps

### Step 0 — Setup (15 min, today)
- Save this plan as `workflow/plans/02-phase3.md`.
- Each prompt saved first in `workflow/prompts/phase3/NN-<name>.md`.

### Step 1 — Real Wazuh API responses from the lab (45 min, today, main session)
Subagents cannot run shell, so the main session does this, each command approved by you. Credentials are passed via env vars you set (`! export ...`), never typed into chat or files.
- Start the containers if down; check version.
- Calls (read-only): `POST /security/user/authenticate`, `GET /` (version), `GET /agents`, `GET /syscollector/{id}/os`, `GET /syscollector/{id}/packages?limit=5`, and the vulnerability state in the indexer `GET wazuh-states-vulnerabilities-*/_search?size=3` (+ check whether the server API still has a vulnerability endpoint in this 4.x version).
- Optional (if time): create a read-only RBAC user/role for the service and show it works — strong evidence for the "least privilege" answer.
- Save redacted outputs in `research/lab/api/NN-<call>.json` (JWT, passwords, hostnames, non-default users, public IPs removed), and a note `research/sources/lab-api-vulnerability-data.md` (`source_type: own-lab`) with what each call shows and which fields the service needs.

### Step 2 — Targeted research (in parallel with Step 1; 2 researchers + 1 verifier)
- **R5 – Connecting & security:** Wazuh API auth (JWT lifetime), RBAC read-only roles, indexer roles/users, how external tools are expected to connect (API vs indexer), port exposure guidance. Prefix `design-wazuh-access-`.
- **R6 – Ranking data & LLM costs:** CISA KEV and FIRST EPSS (what they are, licence, API, update frequency); public prices of a hosted LLM API with no-training/zero-retention terms (for the cost estimate). Prefix `design-ranking-` / `design-llm-`.
- Then **one verifier** for the whole batch. Fix or drop failing claims; log corrections in `research/ai-log.md`.
- Checkpoint commit (proposed): `research: phase 3 lab API responses and sources`.

### Step 3 — Design decisions (1 h, today) — **human decision point**
I draft `research/phase3-decisions.md`: each decision with 2–3 options, my recommendation and why; you choose. Expected decisions:
1. **Connection:** small outbound-only connector in the customer network (pulls Wazuh API/indexer, pushes to SaaS) vs SaaS pulling directly (needs inbound exposure of 55000/9200). Recommended: connector.
2. **Data that leaves:** findings + OS/package versions, agent names pseudonymised; no logs/alerts.
3. **Tenancy:** shared Postgres with `tenant_id` + row-level security + per-tenant encryption keys, vs DB per tenant.
4. **Auth:** OIDC/SSO for users, roles (viewer/triager/approver); per-connector credential (mTLS or signed token), rotatable.
5. **AI:** hosted LLM with structured output and an evidence checklist (package version, distro, fixed version, advisory link); AI only proposes, a person confirms, decisions expire; deterministic rules first, LLM only for the hard cases; no tool can write to Wazuh.
6. **Quality:** golden set from lab + forum false-positive cases (Phase 2 notes), human accept/reject rate as live signal, alarms on drop.
7. **Degradation:** Wazuh down → last snapshot with "stale since"; model down → ledger and queue still work, AI proposals queued.
8. **Ranking:** CVSS + KEV/EPSS + user-set asset criticality, explained by AI.
Checkpoint commit (proposed): `research: phase 3 design decisions`.

### Step 4 — Diagrams (1.5 h, tomorrow)
Mermaid sources in `diagrams/src/` (`d1-components.mmd`, `d2-triage-request.mmd` as sequence diagram, `d3-data-boundaries.mmd`), rendered to SVG in `diagrams/` with `npx @mermaid-js/mermaid-cli` (GitHub also renders the Mermaid inline). D2 example request: "triage the new findings of this week" → sync → rules → LLM proposal → human confirms/rejects → ledger re-applied → fix-first queue.

### Step 5 — Write PHASE3.md (2 h, tomorrow)
Short answer at the top (like PHASE2.md), then the 8 questions with the brief's wording as headings, real redacted API snippets, the diagrams embedded, a cost table (infra + LLM per tenant/month, with assumptions marked as inference), risks (incl. Pharos overlap), decisions vs discarded alternatives. Only verified claims, with links. You review; your corrections go to `ai-log.md`.

### Step 6 — Verify and close (1 h, tomorrow)
- One verifier over URLs cited in PHASE3.md → `research/verification/PHASE3.verify.md`.
- Update `research/README.md`, `README.md` (new folders `research/lab/`, diagrams).
- Commits (proposed): `diagrams: phase 3`, `phase3: answers`.
- Transcript export optional (your call, as in Phase 2).

## Files
- New: `workflow/plans/02-phase3.md`, `workflow/prompts/phase3/*`, `research/lab/api/*.json`, `research/sources/lab-api-vulnerability-data.md`, `research/sources/design-*.md`, `research/verification/*`, `research/phase3-decisions.md`, `diagrams/src/*.mmd`, `diagrams/*.svg`.
- Changed: `PHASE3.md`, `research/README.md`, `research/ai-log.md`, `README.md`.
- Never touched: `PHASE1.md`, `screenshots/`, `.private/` (read only).

## Verification
- 3 diagrams answer the 3 "Draw" bullets; each has its source in `diagrams/src/`.
- All 8 questions answered; at least one real, redacted lab API response per data source used.
- `grep -rE 'eyJ[A-Za-z0-9_-]{10,}'` over `research/lab/` finds no JWT; no public IPs/hostnames.
- PHASE3.verify.md has no `NOT SUPPORTED`.
- `git diff cb1f242 --stat -- PHASE1.md screenshots/` prints nothing.
