---
title: Worktrees; Run Claude Code programmatically; Claude Code GitHub Actions; MCP (Claude Code docs and anthropics/claude-code-action)
url: multiple, see claims
publisher: Anthropic (code.claude.com, github.com/anthropics)
source_type: official-docs
wazuh_version: n/a
accessed: 2026-11-11
question: Phase 4. What the Claude Code docs say about parallel sessions in git worktrees, non-interactive (-p) and CI use, the official GitHub Action, and what MCP is and how it can be restricted.
---

## Summary
Official Claude Code docs describe `claude --worktree <name>` for isolated parallel sessions and `isolation: worktree` for subagents. Non-interactive mode is `claude -p`, with `--allowedTools`, `--output-format json` and a recommended `--bare` mode for CI. The official GitHub Action (`anthropics/claude-code-action@v1`) responds to `@claude` mentions on issues and PRs or runs a fixed prompt, and can review PRs and push commits. MCP connects Claude Code to external tools; MCP tools are gated by `mcp__` permission rules and, for organisations, managed allow/deny lists.

## Claims
1. `claude --worktree <name>` (or `-w`) creates an isolated worktree under `.claude/worktrees/<name>/` on a new branch `worktree-<name>`; running it again with another name gives a second isolated session.
   - Quote: "By default, the worktree is created under `.claude/worktrees/<name>/` at your repository root, on a new branch named `worktree-<name>`"
   - Source: https://code.claude.com/docs/en/worktrees#start-claude-in-a-worktree
   - Confidence: high

2. Worktrees isolate file edits; the docs present them alongside subagents and cross-session messaging as ways to run Claude in parallel.
   - Quote: "Worktrees are one of several ways to run Claude in parallel. They isolate file edits."
   - Source: https://code.claude.com/docs/en/worktrees
   - Confidence: high

3. A custom subagent can always run in its own temporary worktree with `isolation: worktree`; the worktree is removed automatically if the subagent makes no changes.
   - Quote: "make the isolation permanent for a custom subagent by adding `isolation: worktree` to its frontmatter."
   - Source: https://code.claude.com/docs/en/worktrees#isolate-subagents-with-worktrees
   - Confidence: high

4. While a session is in a worktree, Claude Code blocks edits to the main checkout and git commands redirected into it, but does not track files a shell command writes (e.g. `cp`); those fall under permissions and sandboxing.
   - Quote: "None of them tracks which files a shell command writes, so a command that writes into the main checkout without running git there, such as `cp` or a shell redirect, isn't refused by them."
   - Source: https://code.claude.com/docs/en/worktrees#how-claude-code-enforces-isolation
   - Confidence: high

5. "Yes, and don't ask again" approvals given in a worktree are saved to the main checkout's `.claude/settings.local.json` and apply to all worktrees.
   - Quote: "choosing \"Yes, and don't ask again\" for a Bash command in a worktree session saves the rule to the main checkout's `.claude/settings.local.json`."
   - Source: https://code.claude.com/docs/en/worktrees#what-worktrees-share-with-the-main-checkout
   - Confidence: high

6. Non-interactive mode: pass `-p` (or `--print`) with a prompt; `--allowedTools` pre-approves tools using permission-rule syntax.
   - Quote: "Add the `-p` (or `--print`) flag to any `claude` command to run it non-interactively."
   - Source: https://code.claude.com/docs/en/headless
   - Confidence: high

7. `--output-format` supports `text`, `json` and `stream-json`; `--json-schema` gives schema-conforming output in `structured_output`.
   - Quote: "`json`: structured JSON with result, session ID, and metadata"
   - Source: https://code.claude.com/docs/en/headless#get-structured-output
   - Confidence: high

8. In a Manual-mode `-p` run, a call that needs approval is denied unless something approves it; `--permission-mode dontAsk` denies every call that would prompt and is described as useful for locked-down CI.
   - Quote: "`dontAsk`: Claude Code denies every call that would otherwise prompt, which is useful for locked-down CI runs"
   - Source: https://code.claude.com/docs/en/headless#auto-approve-tools
   - Confidence: high

9. `--bare` skips auto-discovery of hooks, skills, subagents, plugins, MCP servers, auto memory and CLAUDE.md; it is recommended for scripted calls. Without `--bare`, a `-p` run loads a project's hooks and `.mcp.json` servers even in an untrusted folder.
   - Quote: "`--bare` is the recommended mode for scripted and SDK calls, and will become the default for `-p` in a future release."
   - Source: https://code.claude.com/docs/en/headless#start-faster-with-bare-mode
   - Confidence: high

10. Claude Code GitHub Actions: mention `@claude` in a PR or issue comment to have Claude analyse code, implement changes and push commits; or give a `prompt` to run on any GitHub event.
    - Quote: "Mention `@claude` in a pull request or issue comment to have Claude analyze code, implement changes, and push commits."
    - Source: https://code.claude.com/docs/en/github-actions
    - Confidence: high

11. Two modes: interactive (no `prompt`, waits for the trigger phrase, replies as a comment) and automation (a `prompt` input, results in the workflow log by default). The workflow step is `anthropics/claude-code-action@v1`; setup via `/install-github-app` or manually.
    - Quote: "**Automation mode**: when the workflow provides a `prompt` input, Claude runs without waiting for a mention"
    - Source: https://code.claude.com/docs/en/github-actions#interactive-and-automation-modes
    - Confidence: high

12. By default only users with write access can trigger runs on issue/PR events, and bot actors are rejected unless listed in `allowed_bots`.
    - Quote: "on issue and pull request events, the triggering user must have write access to the repository."
    - Source: https://code.claude.com/docs/en/github-actions#who-can-trigger-runs
    - Confidence: high

13. In automation mode with a plain prompt, Claude has no shell or GitHub API access until tools are granted with `--allowedTools` in `claude_args` or a `permissions.allow` rule.
    - Quote: "For a plain-text prompt, Claude has no shell or GitHub API access until you grant the tools the prompt needs"
    - Source: https://code.claude.com/docs/en/github-actions#run-on-a-schedule
    - Confidence: high

14. The action follows a `CLAUDE.md` in the repository root when creating PRs and responding to requests.
    - Quote: "Claude follows these guidelines when creating PRs and responding to requests."
    - Source: https://code.claude.com/docs/en/github-actions#define-project-standards-in-claudemd
    - Confidence: high

15. The action's README lists code review, code implementation, PR/issue integration, and states it runs on your own GitHub runner.
    - Quote: "The action executes entirely on your own GitHub runner (Anthropic API calls go to your chosen provider)"
    - Source: https://github.com/anthropics/claude-code-action
    - Confidence: high

16. MCP: Claude Code connects to external tools and data sources through the Model Context Protocol, an open source standard; MCP servers give it access to tools, databases and APIs.
    - Quote: "MCP servers give Claude Code access to your tools, databases, and APIs."
    - Source: https://code.claude.com/docs/en/mcp
    - Confidence: high

17. Project-scoped MCP servers are stored in `.mcp.json` at the project root; interactive sessions ask for approval before using them, but `-p` runs load them without asking.
    - Quote: "For security reasons, Claude Code prompts for approval in interactive sessions before using project-scoped servers from `.mcp.json` files."
    - Source: https://code.claude.com/docs/en/mcp
    - Confidence: high

18. Organisations can restrict MCP servers with `managed-mcp.json` (exclusive control) or `allowedMcpServers` / `deniedMcpServers` in settings; a denylist match always wins.
    - Quote: "A server that matches any denylist entry, by URL, command, or name, is blocked. Nothing overrides a denylist match."
    - Source: https://code.claude.com/docs/en/managed-mcp#how-a-server-is-evaluated
    - Confidence: high

19. `serverName` entries are not a security control; `serverUrl` / `serverCommand` should be used to enforce which servers run.
    - Quote: "A `serverName` entry, in either list, is not a security control."
    - Source: https://code.claude.com/docs/en/managed-mcp#how-servername-entries-match
    - Confidence: high

20. Individual MCP tools are also gated by permission rules (`mcp__<server>__<tool>`); see claim 7 in `tooling-claude-code-permissions-hooks-sandbox.md`.
    - Quote: "`mcp__puppeteer__puppeteer_navigate` matches the `puppeteer_navigate` tool provided by the `puppeteer` server"
    - Source: https://code.claude.com/docs/en/permissions
    - Confidence: high

## Inference
- Inference: for a build plan with parallel agents, one worktree per agent (or `isolation: worktree` subagents) plus a CI job running `claude -p --bare` with an explicit `--allowedTools` list and `dontAsk` mode is the documented pattern; PR review can be delegated to `claude-code-action` with a human merging.
- Inference: a Wazuh-specific MCP server (e.g. read-only Wazuh API access) would be gated per tool via `mcp__<server>__<tool>` allow/deny rules.

## Open questions
- The MCP page is ~157k characters; only the first ~100k were read.
- The worktrees page does not state a limit on the number of parallel worktrees: not stated.
