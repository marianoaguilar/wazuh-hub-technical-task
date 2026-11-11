---
note: research/sources/tooling-claude-code-instructions-agents.md
verified: 2026-11-11
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | memory page: "A project CLAUDE.md can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`"; `./CLAUDE.local.md` is the personal local scope; managed policy location is described. User scope `~/.claude/CLAUDE.md` is named on the sub-agents page. |
| 2 | SUPPORTED | "Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` from your current working directory and every directory above it." / "All discovered files are concatenated into context rather than overriding each other." |
| 3 | SUPPORTED | "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead." |
| 4 | SUPPORTED | sub-agents "What loads at startup": "Every level of the CLAUDE.md hierarchy the main conversation loads ... The built-in Explore and Plan agents skip this." `omitClaudeMd` confirmed in the frontmatter table. |
| 5 | SUPPORTED | "Each subagent starts with a fresh, isolated context window. It doesn't see your conversation history ..." plus the fork exception; "Subagents receive only this system prompt plus basic environment details ..., not the Claude Code system prompt." |
| 6 | SUPPORTED | memory page: "The main conversation's auto memory isn't loaded into subagents; the exception is a fork". |
| 7 | SUPPORTED | "Subagents are Markdown files with YAML frontmatter"; scopes table: managed settings (1), `--agents` flag (2), `.claude/agents/` (3), `~/.claude/agents/` (4), plugins (5); "uses the one from the higher-priority location". |
| 8 | SUPPORTED | Frontmatter table lists name and description (required), tools, disallowedTools, model, permissionMode, hooks, isolation, omitClaudeMd, skills, memory (plus others: maxTurns, mcpServers, background, effort, color...). The note says "include", so it is not exhaustive. Caveat: my read also went through the fetch tool's summariser, not the raw page. |
| 9 | SUPPORTED | "To restrict tools, use the `tools` field as an allowlist or the `disallowedTools` field as a denylist"; `tools` "Inherits every tool available to subagents if omitted." |
| 10 | SUPPORTED | `model`: "`sonnet`, `opus`, `haiku`, `fable`, a full model ID such as `claude-opus-5-5`, or `inherit`." |
| 11 | SUPPORTED | "By default, a subagent can spawn subagents of its own, up to three layers below the main conversation."; "omit `Agent` from its `tools` list or add it to `disallowedTools`" keeps one subagent from spawning. |
| 12 | SUPPORTED | skills page: "Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`."; project path `.claude/skills/<skill-name>/SKILL.md`. |
| 13 | SUPPORTED | `allowed-tools`: "Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message." |

## Note-level problems
- None. Front matter complete; English; no personal data; Inference section separate and labelled; unread page tails are disclosed under Open questions.

## Recommended fixes
- None required. Optional: in claim 13 add that the page says `allowed-tools` "doesn't restrict tools" (every tool stays available), so it is not the same as a subagent's `tools` allowlist.
