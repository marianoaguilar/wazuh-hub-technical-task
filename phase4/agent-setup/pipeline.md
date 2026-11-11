# From an idea to production

Who does what at each step. "Enforced" means the agent cannot skip it.

| # | Step | Who | Enforced by |
|---|------|-----|-------------|
| 1 | Idea, bug or user feedback becomes an issue | Person (me or the team); an agent may draft it | — |
| 2 | Spec: what, why, which ADR and which "never break" rules it touches, acceptance tests | Agent drafts, **person approves** | Issue label `spec-approved` needed to start |
| 3 | Implementation in its own worktree and branch: tests first, then code, then docs | `implementer` agent | Permissions + hook (`.claude/settings.json`), sandbox |
| 4 | Pull request | `implementer` | Branch protection: no direct push to `main` |
| 5 | CI: lint, unit tests, tenant-isolation tests, AI exam (if AI touched), dependency and secret scan, docs check | CI | Required checks in branch protection |
| 6 | Review against the rules and the spec | `reviewer` agent (read-only), then **person** | Required approval from a code owner; `CODEOWNERS` adds a second person for `db/migrations/`, `services/ingest/auth/`, `services/proposer/`, `prompts/` |
| 7 | Merge | **Person** | Only people can merge |
| 8 | Deploy to staging, smoke tests with lab data | CI/CD | Pipeline |
| 9 | Canary: a small share of tenants, watch errors and AI signals | CI/CD, person watches | Automatic rollback on error-rate alarm |
| 10 | Production | **Person** presses the button | Protected environment with manual approval |
| 11 | Monitoring: uptime, errors, AI acceptance rate, validator drops, reopened decisions | Alarms; on-call person | Alarms page the on-call person |
| 12 | What we learn (incident, bad AI case, feedback) becomes a new issue, test or exam case | Person; agent drafts | — |

## What agents never have

- Production credentials, cloud console access or database access outside the local test
  database.
- Real customer data.
- The right to merge, to deploy to production or to change CI, branch protection or `CODEOWNERS`.
