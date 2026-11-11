---
note: research/sources/tooling-claude-code-permissions-hooks-sandbox.md
verified: 2026-11-11
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | permissions page: "Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome, and rule specificity doesn't change the order." |
| 2 | SUPPORTED | "Bash rules match the whole command text, with `*` standing in for any text"; the space before a trailing `*` is described under wildcard patterns (`Bash(ls *)` vs `Bash(ls*)`). |
| 3 | SUPPORTED | Section "What a Bash rule doesn't match": quote is verbatim; table lists `Bash(git push *)` not stopping `git -C . push`; page points to sandboxing and PreToolUse hook. |
| 4 | SUPPORTED | "How path patterns match": gitignore syntax, four pattern types (`//path`, `~/path`, `/path`, `path`/`./path`). |
| 5 | SUPPORTED | Warning box: "The single leading slash anchors at the settings source, not the filesystem root." |
| 6 | SUPPORTED | "`Edit` rules apply to all built-in tools that edit files. Claude makes a best-effort attempt to apply `Read(path)` deny rules..." verbatim. |
| 7 | SUPPORTED | MCP section: `mcp__<server>__*`, and "`mcp__puppeteer` matches any tool provided by the `puppeteer` server" (bare form is documented). |
| 8 | SUPPORTED | "Use `Agent(AgentName)` rules to control which subagents Claude can use". |
| 9 | SUPPORTED | "Sandboxing provides OS-level enforcement that restricts shell commands' filesystem and network access. It applies to Bash, PowerShell, and Monitor tool commands and their child processes." |
| 10 | SUPPORTED | hooks page lifecycle table lists all named events (SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, SubagentStart, SubagentStop, Stop, SessionEnd, WorktreeCreate, WorktreeRemove, and more). The quoted "Tool calls: ..." string is a summary label, not verified verbatim; the event names are. |
| 11 | SUPPORTED | Common input fields: session_id, transcript_path, cwd, hook_event_name sent to every hook; "The `tool_name`, `tool_input`, and `tool_use_id` fields are event-specific." |
| 12 | SUPPORTED | Table row `agent_type`: "Agent name ... Present when the session uses `--agent` or the hook fires inside a subagent." `agent_id` row also present. |
| 13 | SUPPORTED | "Exit with code 2 to block the action ... a `PreToolUse` hook blocks the tool call" and "Even a `permissionDecision` of `"allow"` doesn't let the action through." (stderr-to-Claude detail not re-checked, not needed for the claim's core). |
| 14 | SUPPORTED | PreToolUse decision control (read via offset 100000): permissionDecision allow/deny/ask/defer with permissionDecisionReason; "Deny and ask rules are still evaluated regardless of what the hook returns". |
| 15 | SUPPORTED | "The hook can deny the call, but staying silent doesn't approve it." |
| 16 | SUPPORTED | sandboxing table: Writes = working directory, per-user temp directory, added directories; Reads = "Most of the machine, including credential files such as `~/.ssh`"; Network = proxy, "allowed domains, which start empty". |
| 17 | SUPPORTED | "macOS: uses Seatbelt", "Linux: uses bubblewrap", "WSL2: uses bubblewrap"; "On native Windows, Claude Code runs commands unsandboxed." |
| 18 | SUPPORTED | "tools such as Read, Edit, Write, WebFetch, and WebSearch follow permission rules instead"; "command hooks, local MCP servers ... run with your full access". |
| 19 | SUPPORTED | Page says: "Claude analyzes the failure and may retry the command with the `dangerouslyDisableSandbox` parameter", "You can disable the unsandboxed retry by setting `"allowUnsandboxedCommands": false` in your sandbox settings", and `sandbox.excludedCommands` runs commands outside the sandbox. The note's "quote" is a paraphrase, but the page says all of it. Confidence `medium` can be raised to `high`. |

## Note-level problems
- Claim 10 and 19 present a paraphrase inside the "Quote:" field (labelled "as given on the page" / "as summarised"). The page does contain the facts, but the quote field is not verbatim. Replace with the verbatim sentences found above.
- Front matter complete, language English, no personal data, inferences are labelled `Inference:` in a separate section.
- The sandboxing page tail (~11k chars), the end of the hooks page and `sandbox.enabled` as a documented key: `sandbox.enabled` IS documented ("set `sandbox.enabled` to `true` in a settings file such as `~/.claude/settings.json`"); the note does not mention this key, although `phase4/agent-setup/` depends on it (see PHASE4 reports).

## Recommended fixes
- Replace the non-verbatim quotes in claims 10 and 19 with exact page sentences (given above); raise claim 19 to `high`.
- Add a claim for `sandbox.enabled`, `sandbox.failIfUnavailable` ("By default, when the platform doesn't support the sandbox or the dependency check at startup fails, Claude Code runs commands without sandboxing"), and `sandbox.filesystem.denyWrite` / `network.allowedDomains`, with the sandboxing URL, so the README of `phase4/agent-setup/` can cite the note instead of saying UNVERIFIED.
- Add: the sandbox default still lets commands READ credential files (`~/.ssh`, `~/.aws/credentials`) unless `filesystem.denyRead` is set.
