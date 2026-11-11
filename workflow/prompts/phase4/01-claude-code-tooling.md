# Prompt 01 (R7): Claude Code features used to direct and restrict agents

- Date: 2026-11-11
- Agent: `researcher` (background, while the main session drafts the example agent setup)
- Plan step: Phase 4, Step 2 (`workflow/plans/03-phase4.md`)

## Prompt

> Context: Phase 4 explains how I direct AI agents during this task and how I would set up
> agents to build a SaaS service. PHASE4.md and an example agent setup will describe Claude Code
> features. Each statement about the tool needs an official source.
>
> Research questions (official Anthropic Claude Code documentation only, code.claude.com /
> docs.claude.com / docs.anthropic.com, plus the official `anthropics` GitHub repositories):
> 1. **Memory / CLAUDE.md:** where Claude Code reads project instructions from, and whether
>    subagents also follow them.
> 2. **Subagents:** how they are defined (`.claude/agents/*.md`, frontmatter fields such as
>    `tools`, `model`), and whether the `tools` list restricts what a subagent can call.
> 3. **Permissions:** `allow` / `ask` / `deny` rules in `settings.json`, their order of
>    precedence, and the rule syntax for Edit/Read paths and Bash commands.
> 4. **Hooks:** `PreToolUse` and others; what a hook receives on stdin (including any field that
>    identifies the subagent), and how exit code 2 or a JSON decision blocks or asks.
> 5. **Sandboxing:** what the Bash sandbox restricts (file system, network).
> 6. **Git worktrees / parallel sessions:** what the docs say about running agents in separate
>    worktrees.
> 7. **Headless and CI use:** non-interactive mode (`-p`), and the official GitHub Actions
>    integration (what it can do on a PR or issue).
> 8. **Skills and MCP:** what each one is, in one or two sentences, and how MCP servers can be
>    limited by permissions.
>
> Output: at most 3 topic notes under `research/sources/` with prefix `tooling-claude-code-`
> (for example `-instructions-agents`, `-permissions-hooks-sandbox`, `-ci-worktrees-mcp`). Topic
> notes may use `url: multiple, see claims`. Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent field names, flags, file paths or behaviours; if a page cannot be
> fetched, say so; if the docs do not say something, write that it is not stated; mark
> confidence; keep inference apart from claims; English only.
>
> When done, reply with at most 10 lines: files written and the facts PHASE4.md can rely on.
