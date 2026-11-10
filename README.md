# Wazuh Hub – Technical Task

Technical task for the Software Engineer position in the Wazuh Hub team.

The task has five phases: get to know Wazuh, find a need of Wazuh users,
design a SaaS service for it, plan how to build it with AI agents, and
present the work.

## Repository structure

| Path | Content |
|------|---------|
| `PHASE1.md` | Getting to know Wazuh: lab, findings and lessons (written without AI) |
| `PHASE2.md` | Finding a need of Wazuh users |
| `PHASE3.md` | Design of the SaaS service |
| `PHASE4.md` | Plan to build and run the service with AI agents |
| `screenshots/` | Screenshots of my Wazuh lab |
| `research/sources/` | Research notes, one per source or topic, every claim with its URL |
| `research/verification/` | Reports that check each note's claims against its sources |
| `research/ai-log.md` | Log of the mistakes I caught in the AI's work and how I corrected them |
| `diagrams/` | Diagrams (rendered); their sources are in `diagrams/src/` |
| `CLAUDE.md` | Context and rules every AI agent follows in this repository |
| `.claude/agents/` | Subagent definitions: `researcher` and `verifier` |
| `.claude/hooks/`, `.claude/settings.json` | Guardrails: permissions and a hook that blocks forbidden actions |
| `.githooks/` | Git pre-commit hook that protects Phase 1 and the private brief |
| `workflow/plans/` | Plans for each step of the work |
| `workflow/prompts/` | Prompts I gave to the agents |
| `workflow/transcripts/` | Exported agent sessions |

## How I work with agents

Phases 2–4 are done with AI agents (Claude Code). [`CLAUDE.md`](CLAUDE.md) sets the rules: every
claim needs a source, no invented sources, uncertainty is flagged, and Phase 1 is never touched.
The `researcher` agent collects sourced notes and the `verifier` agent checks them against their
URLs before I use them. Plans, prompts and sessions are kept in [`workflow/`](workflow/), and
every correction I make to the AI goes in [`research/ai-log.md`](research/ai-log.md).
CLAUDE.md says which guardrails are enforced by tools and which are only instructions.

To enable the git hook after cloning: `git config core.hooksPath .githooks`


## Author

Mariano Aguilar Olmo