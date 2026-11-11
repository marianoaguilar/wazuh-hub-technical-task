# Prompt 02: verify the tooling notes and the PHASE4.md draft

- Date: 2026-11-11
- Agent: `verifier` (one run for the whole batch)
- Plan step: Phase 4, Step 6 (`workflow/plans/03-phase4.md`)

## Prompt

> Check two things and write one report per item under `research/verification/`.
>
> 1. The three new notes `research/sources/tooling-claude-code-*.md` (as usual, one report per
>    note). The researcher said a few quotes came through a fetch summary rather than verbatim
>    (the hooks event list, the subagent frontmatter field list, the unsandboxed-retry
>    behaviour): check those first.
> 2. The draft `PHASE4.md` → `research/verification/PHASE4.verify.md`. Check:
>    - every external link: does the page say what the sentence claims, without widening it?
>    - every claim about this repository (counts of plans, prompts, notes, reports, ai-log rows;
>      what the ai-log rows say; what `.claude/`, `CLAUDE.md`, `phase3-decisions.md` and
>      `phase4/agent-setup/` contain): read the files and check them;
>    - opinions and design proposals do not need a source, but must not be written as facts about
>      the world; flag any that should carry `Inference:`.
>    Also check `phase4/agent-setup/README.md` and `phase4/agent-setup/.claude/settings.json`
>    against the tooling notes (rule syntax, precedence, sandbox keys).
>
> Verdicts per claim: SUPPORTED / PARTIAL / NOT SUPPORTED / URL UNREACHABLE, with a one-line
> suggested fix for anything not SUPPORTED. Do not edit any file outside
> `research/verification/`. Reply with at most 10 lines: counts per verdict and the most
> important fixes.
