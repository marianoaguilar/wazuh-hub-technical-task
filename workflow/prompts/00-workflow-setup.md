# Prompt 00: set up the agent workflow

- Date: 2026-11-10
- Tool: Claude Code (main session, plan mode)
- Result: plan [`../plans/00-workflow-setup.md`](../plans/00-workflow-setup.md), approved by me and then implemented

## Prompt

> I'm doing a 72h technical task for a Software Engineer role in the Wazuh Hub team.
> The full brief is in .private/task.pdf (gitignored, never commit it). Read it first.
>
> Current state: PHASE1.md and screenshots/ are done. PHASE1.md was written by me
> WITHOUT AI, as the task requires. You must never edit it.
>
> Phases 2-4 must be done with AI agents, and the repo must make my workflow visible:
> the plan, the commits and everything I use to direct my agents. Before any Phase 2
> work, I want to set up that workflow. Propose (don't write yet):
>
> 1. A CLAUDE.md with: project context, the rules of the task (English deliverables,
>    own lab only, no personal or sensitive data), and working rules for agents
>    (every research claim needs a source URL, never invent sources, flag uncertainty,
>    write results to files, not to chat).
> 2. Two subagents in .claude/agents/:
>    - researcher: web search + fetch, writes notes only under research/sources/.
>    - verifier: read-only, checks that each note's claims are backed by its URLs
>      and reports problems to research/verification/.
> 3. .claude/settings.json permissions: deny any edit to PHASE1.md and screenshots/,
>    deny reading .private/ except the task PDF, ask before git push.
> 4. A folder structure for: research notes, agent prompts, plans, exported session
>    transcripts, an AI corrections log (research/ai-log.md), and diagrams with sources.
> 5. README updates so the structure table covers the new folders.
>
> For each guardrail, tell me explicitly whether it is ENFORCED (permissions/tools)
> or only INSTRUCTED (text in CLAUDE.md or the agent prompt). Then wait for my review.
