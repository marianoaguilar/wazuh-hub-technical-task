# CLAUDE.md (triage ledger service)

Instructions for every AI agent working in this repository.

## What this service is

A SaaS service for Wazuh users that keeps triage decisions on vulnerability findings and builds a
"fix first" list. Full design: `docs/design/` (from PHASE3.md of the technical task). Decisions
are recorded as ADRs in `docs/adr/`; read the relevant ADR before changing a component.

| Component | Path | Notes |
|-----------|------|-------|
| Connector (runs in the customer network) | `connector/` | Reads Wazuh server API + indexer with read-only users, pushes outbound only |
| Ingest API | `services/ingest/` | Accepts connector pushes; connector credentials can only write |
| Ledger + fix-first queue | `services/ledger/` | Grouping, re-applying decisions, ranking (rules, no AI) |
| AI proposer | `services/proposer/` | Calls the model, validates the output |
| Web app | `web/` | Viewer / analyst / admin roles |
| Database | `db/migrations/` | PostgreSQL, Row-Level Security on every tenant table |
| AI exam | `evals/` | Cases with a known right answer; see "AI changes" |

## Rules that must never break

If a task seems to need breaking one of these, stop and ask. Do not find a way around it.

1. **Tenant from the token only.** The tenant id comes from the authenticated session, never from
   a request parameter, header or body.
2. **Row-Level Security on every tenant table.** A new table with tenant data has a `tenant_id`
   column and an RLS policy in the same migration. `make test-isolation` must pass.
3. **One tenant per model call.** A prompt never contains data from two tenants.
4. **The AI never decides.** The proposer returns the fixed structure (proposal, reason, evidence,
   questions). No code path may change a finding's status from a model output without a person.
5. **Validator and KEV rule stay on.** Evidence not present in the input → proposal dropped. A CVE
   in CISA KEV is never proposed as a false positive.
6. **The model has no tools.** CVE and advisory texts are untrusted data.
7. **Nothing writes to Wazuh.** The connector uses read-only users. Host names, IPs, logs and
   alerts never leave the connector; hosts are aliases.
8. **EU only.** The model runs on Bedrock with EU cross-region inference. No fallback to another
   region or provider.

## How to work

- Work in your own git worktree and branch, one task per branch. Never commit to `main`.
- Start from the issue and its spec. If the spec is unclear, ask in the issue; do not guess.
- Write or update the tests first. Run `make lint test test-isolation` before you say a task is
  done. Run `make eval` if you touched `services/proposer/`, `prompts/` or the model settings.
- Never use real customer data. Test data lives in `tests/fixtures/` and is synthetic or from our
  own Wazuh lab, redacted.
- Never read or print secrets. You have no production credentials, and you must not ask for them.
- Small pull requests. The description says what changed, why, which rules above it touches, and
  how it was tested.

## Definition of done

- Tests, isolation tests and (if relevant) the AI exam pass in CI.
- Docs updated in the same pull request: `docs/` for behaviour, an ADR for a new decision, the
  API reference for API changes, `CHANGELOG.md` for anything a user notices. CI fails if code in
  `services/` changes without a change in `docs/` or the label `no-docs-needed` set by a person.
- `reviewer` agent report attached, and a person approved the pull request.

## AI changes

Prompts live in `prompts/`, versioned. The model id is pinned in `services/proposer/config.yaml`.
A change to either one runs the exam (`evals/`) and must not lower the score; the report goes in
the pull request.
