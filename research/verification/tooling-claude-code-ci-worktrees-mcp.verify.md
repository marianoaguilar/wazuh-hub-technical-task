---
note: research/sources/tooling-claude-code-ci-worktrees-mcp.md
verified: 2026-11-11
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | worktrees page: "Pass `--worktree` or `-w` ... created under `.claude/worktrees/<name>/` ... on a new branch named `worktree-<name>`"; "Run the command again with a different name in another terminal to start a second isolated session." |
| 2 | SUPPORTED | "Worktrees are one of several ways to run Claude in parallel. They isolate file edits." Subagents and cross-session messaging named next to it. |
| 3 | SUPPORTED | "make the isolation permanent for a custom subagent by adding `isolation: worktree` to its frontmatter"; "removes automatically when the subagent finishes without changes". |
| 4 | SUPPORTED | "How Claude Code enforces isolation": blocks edits and git redirects into the main checkout; "None of them tracks which files a shell command writes ... `cp` or a shell redirect, isn't refused"; falls under permissions and sandboxing. |
| 5 | SUPPORTED | "What worktrees share": "choosing "Yes, and don't ask again" for a Bash command in a worktree session saves the rule to the main checkout's `.claude/settings.local.json`. The rule applies in the main checkout and in every other worktree". |
| 6 | SUPPORTED | headless page: "Add the `-p` (or `--print`) flag to any `claude` command to run it non-interactively"; `--allowedTools` "uses permission rule syntax". |
| 7 | SUPPORTED | `text` (default), `json` ("structured JSON with result, session ID, and metadata"), `stream-json`; `--json-schema` result in `structured_output`. |
| 8 | SUPPORTED | "In a Manual mode `claude -p` run, a call that needs approval is denied unless something approves it"; "`dontAsk`: Claude Code denies every call that would otherwise prompt, which is useful for locked-down CI runs". |
| 9 | SUPPORTED | `--bare` skips hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory and CLAUDE.md; "recommended mode for scripted and SDK calls"; "Without `--bare`, a `-p` session runs the hooks in a project's `.claude/settings.json` and connects the servers in its `.mcp.json`, even in a folder you've never trusted." |
| 10 | SUPPORTED | github-actions page, first paragraph, verbatim. |
| 11 | SUPPORTED | Interactive vs automation modes section; "By default, results appear in the workflow run log"; `anthropics/claude-code-action@v1`; `/install-github-app` quick setup and manual setup. |
| 12 | SUPPORTED | "Who can trigger runs": write access on issue/PR events; bot actor rejected unless in `allowed_bots`. |
| 13 | SUPPORTED | "Run on a schedule": "For a plain-text prompt, Claude has no shell or GitHub API access until you grant the tools ..., with `--allowedTools` in `claude_args` or a `permissions.allow` rule in the `settings` input." |
| 14 | SUPPORTED | "Define project standards in CLAUDE.md": "Claude follows these guidelines when creating PRs and responding to requests." |
| 15 | SUPPORTED | GitHub README: "The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)"; features list has Code Review, Code Implementation, PR/Issue Integration. |
| 16 | PARTIAL | The mcp page quote is verbatim, but the page calls MCP "an open source standard for AI-tool integrations", not "an open standard" (claim wording). Fix: write "open source standard". |
| 17 | SUPPORTED | Quote verbatim; and "In `claude -p` runs, Agent SDK sessions, and cloud sessions ..., Claude Code can't show that prompt: it loads project-scoped servers without asking." |
| 18 | SUPPORTED | managed-mcp page: `managed-mcp.json` exclusive control; `allowedMcpServers` / `deniedMcpServers`; "Nothing overrides a denylist match." (section "How a server is evaluated"). |
| 19 | SUPPORTED | "A `serverName` entry, in either list, is not a security control ... add `serverCommand` or `serverUrl` entries." |
| 20 | SUPPORTED | permissions page MCP section: "`mcp__puppeteer__puppeteer_navigate` matches the `puppeteer_navigate` tool provided by the `puppeteer` server". |

## Note-level problems
- Front matter complete; language English; no personal data; Inference section separate and labelled.
- Open question says only the first ~100k chars of the MCP page were read; claims 16 and 17 are within what I read (first 100k), so no hidden dependency on the tail.

## Recommended fixes
- Claim 16 (and the Summary): replace "open standard" with "open source standard" as the page words it.
