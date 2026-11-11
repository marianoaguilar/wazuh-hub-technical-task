# Wazuh Hub – Technical Task

Technical task for the Software Engineer position in the Wazuh Hub team. It has five phases: get to know Wazuh, find a need of Wazuh users, design a SaaS service for it, plan how to build it with AI agents, and present the work.

## Summary

- **Lab.** Wazuh 4.14 (server, indexer and dashboard) in Docker, and a Wazuh agent on my Ubuntu laptop ([PHASE1](PHASE1.md), written without AI).
- **Need.** Vulnerability triage: Wazuh finds many vulnerabilities, but users have no way to record what they decided about each finding, nor to see what to fix first ([PHASE2](PHASE2.md)).
- **Service.** A vulnerability triage ledger: a read-only connector in the customer network (its access tested in my lab), an AI that proposes and a person who decides, and a "fix first" list ranked by rules ([PHASE3](PHASE3.md)).
- **Building it with AI agents.** The same loop I used for this task: plan → prompt → research → independent verification → my review → commit, with the hard limits enforced by tools, not by instructions ([PHASE4](PHASE4.md)).

**Where to start.** Read the summary, then PHASE1 → PHASE2 → PHASE3 → PHASE4. Every claim links to its source; [`research/`](research/) holds the evidence and how it was checked.

## Repository structure

| Path | Content |
|------|---------|
| [`PHASE1.md`](PHASE1.md), [`screenshots/`](screenshots/) | Getting to know Wazuh: lab, findings and lessons (written without AI) |
| [`PHASE2.md`](PHASE2.md) | Finding a need of Wazuh users |
| [`PHASE3.md`](PHASE3.md) | Design of the SaaS service |
| [`PHASE4.md`](PHASE4.md) | Plan to build and run the service with AI agents |
| [`diagrams/`](diagrams/) | Diagrams (rendered); their sources are in [`diagrams/src/`](diagrams/src/) |
| [`research/README.md`](research/README.md) | Index of the research: each note, the prompt behind it and its verification status |
| [`research/phase2-needs.md`](research/phase2-needs.md), [`research/phase2-ideas.md`](research/phase2-ideas.md) | Phase 2: scored catalogue of needs, and service ideas for the chosen one |
| [`research/phase3-decisions.md`](research/phase3-decisions.md) | Phase 3: design decisions, the options for each and the one I chose |
| [`research/lab/api/`](research/lab/api/) | Real, redacted responses from my lab's Wazuh API and indexer |
| [`research/sources/`](research/sources/) | Research notes, one per source or topic, every claim with its URL |
| [`research/verification/`](research/verification/) | Reports that check each note's claims against its sources |
| [`research/ai-log.md`](research/ai-log.md) | Log of the mistakes I caught in the AI's work and how I corrected them |
| [`phase4/agent-setup/`](phase4/agent-setup/) | Phase 4: example agent setup for building the service (not used by this repository) |
| [`CLAUDE.md`](CLAUDE.md) | Context and rules every AI agent follows in this repository |
| [`.claude/agents/`](.claude/agents/) | Subagent definitions: `researcher` and `verifier` |
| [`.claude/hooks/`](.claude/hooks/), [`.claude/settings.json`](.claude/settings.json) | Guardrails: permissions and a hook that blocks forbidden actions |
| [`.githooks/`](.githooks/) | Git pre-commit hook that protects Phase 1 and the private brief |
| [`workflow/plans/`](workflow/plans/) | Plans for each step of the work |
| [`workflow/prompts/`](workflow/prompts/) | Prompts I gave to the agents |

## How I work with agents

Phases 2–4 are done with AI agents (Claude Code). [`CLAUDE.md`](CLAUDE.md) sets the rules: every claim needs a source, no invented sources, uncertainty is flagged, and Phase 1 is never touched. The `researcher` agent collects sourced notes and the `verifier` agent checks them against their URLs before I use them. I take the decisions; the agents prepare the options. Plans and prompts are kept in [`workflow/`](workflow/), and every correction I made to the AI (15 so far) is in [`research/ai-log.md`](research/ai-log.md). CLAUDE.md says which guardrails are enforced by tools and which are only instructions.

To enable the git hook after cloning: `git config core.hooksPath .githooks`

## Author

Mariano Aguilar Olmo
