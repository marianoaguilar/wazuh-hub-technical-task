# CLAUDE.md

Instructions for every AI agent working in this repository (main session and subagents).

## Project context

This repository is my answer to a 72-hour technical task for a Software Engineer role in the
Wazuh Hub team. The task has five phases:

| Phase | Topic | Deliverable | AI allowed |
|-------|-------|-------------|------------|
| 1 | Get to know Wazuh | `PHASE1.md`, `screenshots/` | **No** (already done, by me) |
| 2 | Find a need of Wazuh users | `PHASE2.md` + research | Yes |
| 3 | Design a SaaS service for it | `PHASE3.md` + diagrams | Yes |
| 4 | Plan how to build it with AI agents | `PHASE4.md` + diagrams + agent setup | Yes |
| 5 | Present the work | meeting, no file | — |

The brief asks that the repository makes the AI workflow visible: the plan, the commits and
everything used to direct the agents. That is why plans, prompts, transcripts, research notes,
verification reports and the AI corrections log live in the repo.

My lab: the Wazuh 4.x server, indexer and dashboard run in Docker containers, and the Wazuh
agent runs on my own Ubuntu machine. `PHASE1.md` describes it. "Own lab" means only these
containers and this machine.

### Where things live

| Path | Content |
|------|---------|
| `PHASE1.md`, `screenshots/` | Phase 1. Read-only for agents. |
| `PHASE2.md` … `PHASE4.md` | Answers to each phase. |
| `research/sources/` | Research notes, one per source or topic (written by `researcher`). |
| `research/verification/` | Verification reports (written by `verifier`). |
| `research/ai-log.md` | Log of every AI mistake I caught and corrected. |
| `research/README.md` | Index: note → verification status → where it is used. |
| `workflow/plans/` | Plans for each step of the work. |
| `workflow/prompts/` | Prompts I gave to agents, per phase. |
| `workflow/transcripts/` | Exported agent sessions. |
| `diagrams/src/` | Diagram sources. Rendered files go in `diagrams/`. |
| `.claude/` | Agent definitions, guard hook and permissions. |
| `.githooks/` | Git hooks (pre-commit guard). |

## Rules of the task (from the brief)

1. **English.** Every deliverable, note, report, prompt and commit message is written in English.
2. **Own lab only.** Never send requests to, scan or test any machine I do not own. Examples of
   Wazuh API calls must come from my lab.
3. **No real malware, no sensitive data, no personal data.** Before saving any output from the
   lab (Wazuh API responses, logs, configs), redact tokens (JWT), passwords, API keys, real
   hostnames, usernames that are not lab defaults, and public IP addresses. Private lab IPs may
   stay. Never save personal data about anyone, including people quoted in forums: cite the URL,
   not the person.
4. **Phase 1 is done without AI.** Never edit, rewrite, "fix" or reformat `PHASE1.md` or anything
   in `screenshots/`. Reading them for context is fine.
5. **The brief is private.** The only file you may read in `.private/` is `.private/task.pdf`.
   Never copy the brief into the repository verbatim; paraphrase short requirements when needed.
6. **Diagram sources.** Every diagram has its source file in `diagrams/src/`.

## Working rules for agents

- **Every research claim needs a source URL** next to it, and the source must actually say it.
  Use the most authoritative source available: official Wazuh documentation and the Wazuh GitHub
  repositories first, then the Wazuh forum, mailing list, Slack and community sites (Reddit,
  Stack Overflow), then blogs. Record the access date.
- **Never invent sources.** No made-up URLs, titles, quotes, numbers, version numbers or issue
  numbers. If a page cannot be fetched, say so and do not describe what it "probably" says.
- **Flag uncertainty.** Mark every claim with a confidence level (`high` / `medium` / `low`).
  Prefix anything you could not check with `UNVERIFIED:`. Separate facts from your own inference
  (`Inference:`).
- **Write results to files, not to chat.** Each task names its output path. In chat, reply with a
  short summary (at most ~10 lines) and the paths of the files you wrote.
- **Stay in your lane.** Do only what the task asks. Do not edit files you were not asked to edit.
- **Personal or sensitive data found by accident** (in a forum post, a log, a screenshot): do not
  copy it, and mention the problem in your summary.

## Workflow

1. **Plan.** I write or approve a plan in `workflow/plans/NN-<name>.md`.
2. **Prompt.** The prompt I give to an agent is saved in `workflow/prompts/phaseN/NN-<name>.md`.
3. **Research.** The `researcher` subagent writes notes in `research/sources/`.
4. **Verify.** The `verifier` subagent checks each note against its URLs and writes a report in
   `research/verification/`.
5. **Review.** I read the notes and reports. Claims marked `NOT SUPPORTED` or `URL UNREACHABLE` are
   fixed or dropped before they are used.
6. **Write.** Only verified claims go into `PHASEn.md`, with their source links.
7. **Log corrections.** Every time I correct the AI (wrong claim, invented source, bad reasoning,
   ignored rule), add a row to `research/ai-log.md`.
8. **Commit.** Small commits as the work progresses, with a prefix: `workflow:`, `research:`,
   `phase2:`, `phase3:`, `phase4:`, `diagrams:`, `docs:`. **Agents never commit on their own:**
   propose the files to stage and the commit message, then wait for my explicit OK.
9. **Transcripts.** Exported sessions go to `workflow/transcripts/` only after I check them for
   personal data.

Never run `git push` unless I ask for it in this session. Never use `git commit --no-verify` or
`git add -f`.

## Guardrails: what is enforced and what is only instructed

| Guardrail | How |
|-----------|-----|
| No edits to `PHASE1.md` / `screenshots/` | Enforced: permission deny rules, `.claude/hooks/guard.py` (also checks Bash, best effort), `.githooks/pre-commit` |
| Only `.private/task.pdf` can be read in `.private/` | Enforced: `guard.py` for file tools; any Bash command that mentions `.private` is blocked |
| `.private/` is never committed | Enforced: `.gitignore` + `.githooks/pre-commit` |
| Ask before `git push` | Enforced: `ask` permission rule + `guard.py` |
| `researcher` writes only in `research/sources/`, `verifier` only in `research/verification/` | Enforced: `guard.py` (reads `agent_type` from the hook input) |
| Subagents cannot run shell commands; `verifier` cannot search or edit | Enforced: `tools:` list of each agent |
| Agents commit only after my explicit OK | Instructed (this file) |
| Sources, no invented sources, uncertainty, files not chat, English, own lab, no personal data | Instructed (this file and the agent prompts). Sources are checked by `verifier`; the rest by my review before each commit |
