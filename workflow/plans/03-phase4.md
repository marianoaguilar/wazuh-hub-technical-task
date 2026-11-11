# Phase 4 plan: how I would build and run the service with AI agents

## Context
Phase 3 is done and committed (`14664ed`, not pushed). Service: **vulnerability triage ledger**
(connector in the customer network, shared Postgres with RLS, AI proposes / person decides,
Claude on Bedrock EU, fix-first list ranked by rules). Deadline: **2026-11-11 at night**
(push + email to HR).

Brief, Phase 4 deliverables:
- **Everything used to direct the agents** during this task: already in the repo (`CLAUDE.md`,
  `.claude/`, `.githooks/`, `workflow/plans/`, `workflow/prompts/`, `research/ai-log.md`);
  transcripts still missing.
- **2 diagrams** (source in `diagrams/src/`): (D4) how I worked during this task and the
  development environment I am comfortable with; (D5) the agent setup I would use to build the
  service: what agents know, what they can do, what they cannot do, and how a task moves from an
  idea to a change in production.
- **`PHASE4.md`** answering 8 questions: how I used AI in phases 2–3 (help + corrections);
  split of work between me and agents; how I check agent output is correct and safe; what I
  would not leave to an agent; user feedback; "the service is down"; keeping the design
  integrated as it grows; documentation backed by every change.

Constraints: CLAUDE.md rules, token budget (max 2–3 agents, ask first, one verifier per batch),
PHASE docs one line per paragraph, same diagram style as Phase 3 (few boxes, plain names,
consistent colours: blue customer, green service, purple AI, orange person).

## Time budget (~3.5 h + ~1 h final pass)

| Block | Time |
|-------|------|
| Step 0–1: plan, decisions | 20 min |
| Step 2: Claude Code facts (1 researcher, in background) | 30 min, parallel |
| Step 3: service agent setup files (example) | 45 min |
| Step 4: diagrams D4, D5 | 45 min |
| Step 5: PHASE4.md | 1 h 15 min |
| Step 6: verify + commits | 30 min |
| Final: README, transcripts, last pass of all PHASE files, public-repo check, push, email | ~1 h |

If time slips: cut Step 3 to a single file, never the diagrams or the 8 answers.

## Steps

### Step 0 — Setup
- This plan in `workflow/plans/03-phase4.md`; prompts in `workflow/prompts/phase4/NN-<name>.md`.

### Step 1 — Decisions (human decision point)
1. My development environment for D4 (editor, OS, tools I am comfortable with).
2. Whether to include a concrete example agent setup for the service (Step 3).
3. Which work I would never leave to an agent (draft from me, the user decides).
4. Transcripts: which sessions to export to `workflow/transcripts/`.
   Decision (2026-11-11): none. Full sessions add a lot of noise and little value; the plans,
   prompts, verification reports and `ai-log.md` already show how the agents were directed.

### Step 2 — Facts about the tooling (1 researcher + verifier at the end)
PHASE4.md will describe Claude Code features (subagents and their `tools:` lists, hooks,
permission rules, sandbox, git worktrees, headless/CI use, skills/MCP). Those claims need
sources: one `researcher` run over the official Claude Code docs, prefix `tooling-claude-code-`.
The final verifier (Step 6) also covers these notes. No other research: Q1 comes from
`research/ai-log.md` and the git history.

### Step 3 — Example agent setup for the service (optional, ~45 min)
A small folder `phase4/agent-setup/` that shows D5 as real files, not deployed anywhere:
- `CLAUDE.md` for the service repo: context, architecture invariants (tenant from token only,
  RLS on every table, AI never writes, KEV rule, no host names leave the connector), how to test,
  definition of done.
- `.claude/settings.json`: deny rules (secrets, prod config, migrations without review), ask on
  push, hooks.
- `.claude/agents/`: `implementer`, `reviewer` (read-only), `eval-runner` (AI exam), maybe
  `docs-keeper`.
- `ci.md` or a short pipeline sketch: tests, tenant-isolation tests, AI exam, security scan,
  docs check, human approval, staging, canary.

### Step 4 — Diagrams
- `diagrams/src/d4-how-i-worked.mmd`: me ↔ Claude Code main session ↔ `researcher` /
  `verifier`; guardrails (CLAUDE.md, guard hook, pre-commit); the loop plan → prompt → research →
  verify → review → write → ai-log → commit; the lab operated by me; my environment.
- `diagrams/src/d5-agent-setup.mmd`: three groups "knows / can do / cannot do" around the
  agents, and the path idea → issue → spec (person approves) → agent in a worktree → CI checks →
  reviewer agent → person reviews and merges → staging → canary → production → monitoring and
  feedback → new issue.
- Render to SVG with the same mermaid-cli command as Phase 3.

### Step 5 — PHASE4.md
Short answer at the top, the two diagrams, then the 8 questions with the brief's wording as
headings. Q1 cites rows of `research/ai-log.md` (13 rows so far: inflated counts, roles guessed
for posters, inferences as facts, invented-looking claims caught by the verifier, my own
mistakes as main session: lab operated without asking, token-heavy fan-out, dense diagrams).
Everything else is design, with `Inference:` where it is opinion and links to Phase 3.

### Step 6 — Verify and close
- One verifier over PHASE4.md + the `tooling-` notes → `research/verification/PHASE4.verify.md`.
- Corrections → `research/ai-log.md`.
- Commits (proposed, after OK): `workflow: phase 4 plan and prompts`, `research: claude code
  tooling sources`, `phase4: example agent setup`, `diagrams: phase 4`, `phase4: answers`.

## Files
- New: `workflow/plans/03-phase4.md`, `workflow/prompts/phase4/*`,
  `research/sources/tooling-*.md`, `research/verification/tooling-*.verify.md`,
  `research/verification/PHASE4.verify.md`, `phase4/agent-setup/*` (optional),
  `diagrams/src/d4-*.mmd`, `diagrams/src/d5-*.mmd`, `diagrams/d4-*.svg`, `diagrams/d5-*.svg`.
- Changed: `PHASE4.md`, `research/README.md`, `research/ai-log.md`, `README.md`.
- Never touched: `PHASE1.md`, `screenshots/`, `.private/` (read only).

## Verification
- 2 diagrams answer the 2 "Draw" bullets; each has its source in `diagrams/src/`.
- All 8 questions answered; Q1 points to concrete ai-log rows.
- PHASE4.verify.md has no `NOT SUPPORTED`.
- `git diff --stat cb1f242 -- PHASE1.md screenshots/` prints nothing; `git ls-files .private`
  prints nothing.
