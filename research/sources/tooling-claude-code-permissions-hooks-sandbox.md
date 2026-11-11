---
title: Configure permissions; Hooks reference; Sandboxing (Claude Code docs)
url: multiple, see claims
publisher: Anthropic (code.claude.com)
source_type: official-docs
wazuh_version: n/a
accessed: 2026-11-11
question: Phase 4. How Claude Code permission rules (allow/ask/deny) work and are ordered, the rule syntax for paths and Bash, what PreToolUse hooks receive and how they block, and what the Bash sandbox restricts.
---

## Summary
Official Claude Code docs on three guardrail layers. Permission rules in settings are evaluated deny, then ask, then allow; Bash rules match command text and are explicitly not a security boundary. Hooks receive JSON on stdin (including `agent_type` inside a subagent) and can block a tool call with exit code 2 or a JSON `permissionDecision`. The OS-level sandbox (Seatbelt on macOS, bubblewrap on Linux) limits file writes and network for shell commands and their child processes, but not the built-in Read/Edit/WebFetch tools.

## Claims
1. Rules are evaluated deny, then ask, then allow; the first match in that order wins and specificity does not change it. An allow rule cannot carve an exception out of a deny rule.
   - Quote: "Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome, and rule specificity doesn't change the order."
   - Source: https://code.claude.com/docs/en/permissions
   - Confidence: high

2. Bash rules match the command text, with `*` as a wildcard; `Bash(npm run *)` matches any `npm run ...` command, and the space before a trailing `*` matters.
   - Quote: "Bash rules match the whole command text, with `*` standing in for any text."
   - Source: https://code.claude.com/docs/en/permissions
   - Confidence: high

3. A Bash deny/ask rule is not a security boundary: it does not match the same program invoked in another form (for example `git -C . push` vs `Bash(git push *)`). The docs point to the sandbox or a PreToolUse hook for stronger enforcement.
   - Quote: "It doesn't match the same program invoked in a different form, so a deny or ask rule covers the invocation Claude usually produces and isn't a security boundary around the program."
   - Source: https://code.claude.com/docs/en/permissions#bash-rule-limits
   - Confidence: high

4. Read and Edit rules use gitignore pattern syntax: `//path` is absolute, `~/path` is from home, `/path` is relative to the settings source, and `path` / `./path` is relative to the current directory.
   - Quote: "Read and Edit rules both use gitignore pattern syntax with four distinct pattern types"
   - Source: https://code.claude.com/docs/en/permissions#read-and-edit
   - Confidence: high

5. A single leading slash is not an absolute path; it anchors at the settings source.
   - Quote: "The single leading slash anchors at the settings source, not the filesystem root. Use `//Users/alice/file` for absolute paths."
   - Source: https://code.claude.com/docs/en/permissions#read-and-edit
   - Confidence: high

6. `Edit` rules apply to all built-in file-editing tools; `Read` deny rules are applied best-effort to Grep, Glob and similar built-in read tools.
   - Quote: "`Edit` rules apply to all built-in tools that edit files. Claude makes a best-effort attempt to apply `Read(path)` deny rules to all built-in tools that read files like Grep and Glob."
   - Source: https://code.claude.com/docs/en/permissions#read-and-edit
   - Confidence: high

7. MCP tools use `mcp__<server>__<tool>` names; `mcp__<server>__*` (or `mcp__<server>`) matches every tool of a server.
   - Quote: "To match every tool from an MCP server, write `mcp__<server>__*`. To match one tool, write its full name, `mcp__<server>__<tool>`."
   - Source: https://code.claude.com/docs/en/permissions
   - Confidence: high

8. `Agent(AgentName)` rules control which subagents Claude can use.
   - Quote: "Use `Agent(AgentName)` rules to control which subagents Claude can use"
   - Source: https://code.claude.com/docs/en/permissions
   - Confidence: high

9. Permissions and sandboxing are complementary layers: permissions cover every tool; the sandbox is OS-level enforcement for shell commands and their children.
   - Quote: "Sandboxing provides OS-level enforcement that restricts shell commands' filesystem and network access. It applies to Bash, PowerShell, and Monitor tool commands and their child processes."
   - Source: https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing
   - Confidence: high

10. Hook events include `PreToolUse`, `PostToolUse`, `PermissionRequest`, `UserPromptSubmit`, `Stop`, `SubagentStart`, `SubagentStop`, `SessionStart`, `SessionEnd`, `WorktreeCreate`, `WorktreeRemove` and others.
    - Quote: the event names `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SubagentStart`, `SubagentStop`, `Stop`, `SessionEnd`, `WorktreeCreate`, `WorktreeRemove` appear in the page's lifecycle table (checked by the verifier; the earlier quote was a summary label, not verbatim)
    - Source: https://code.claude.com/docs/en/hooks
    - Confidence: high

11. Command hooks receive JSON on stdin with common fields `session_id`, `transcript_path`, `cwd`, `hook_event_name` (and others); `tool_name`, `tool_input` and `tool_use_id` are event-specific (present for tool events such as PreToolUse).
    - Quote: "The `tool_name`, `tool_input`, and `tool_use_id` fields are event-specific."
    - Source: https://code.claude.com/docs/en/hooks#common-input-fields
    - Confidence: high

12. When a hook fires inside a subagent, the input contains `agent_id` and `agent_type` (the agent name).
    - Quote: "Agent name (for example, `\"Explore\"` or `\"security-reviewer\"`). Present when the session uses `--agent` or the hook fires inside a subagent."
    - Source: https://code.claude.com/docs/en/hooks#common-input-fields
    - Confidence: high

13. For PreToolUse, exit code 2 blocks the tool call and stderr is shown to Claude as the reason; a JSON "allow" cannot override an exit-2 block.
    - Quote: "Exit with code 2 to block the action" / "Even a `permissionDecision` of `\"allow\"` doesn't let the action through."
    - Source: https://code.claude.com/docs/en/hooks
    - Confidence: high

14. PreToolUse JSON output uses `hookSpecificOutput.permissionDecision` (`allow` / `deny` / `ask` / `defer`) with `permissionDecisionReason`; `deny` prevents the call, `ask` prompts the user. Settings deny and ask rules are still evaluated whatever the hook returns.
    - Quote: "Deny and ask rules are still evaluated regardless of what the hook returns."
    - Source: https://code.claude.com/docs/en/hooks#pretooluse-decision-control
    - Confidence: high

15. A hook that exits 0 with no output does not approve the call; it continues through the normal permission flow.
    - Quote: "The hook can deny the call, but staying silent doesn't approve it."
    - Source: https://code.claude.com/docs/en/hooks
    - Confidence: high

16. Sandbox defaults: writes only to the working directory, a per-user temp directory and added directories; reads to most of the machine; network only through a local proxy with an allowlist that starts empty.
    - Quote: "No direct route out. Connections go through a proxy on your machine that checks each host against your allowed domains, which start empty."
    - Source: https://code.claude.com/docs/en/sandboxing
    - Confidence: high

17. The sandbox uses Seatbelt on macOS and bubblewrap on Linux/WSL2; native Windows runs commands unsandboxed.
    - Quote: "**Linux**: uses bubblewrap for isolation"
    - Source: https://code.claude.com/docs/en/sandboxing
    - Confidence: high

18. The sandbox does not cover built-in file and web tools (Read, Edit, Write, WebFetch, WebSearch); those follow permission rules. Hooks and local MCP servers also run outside the sandbox.
    - Quote: "tools such as Read, Edit, Write, WebFetch, and WebSearch follow permission rules instead."
    - Source: https://code.claude.com/docs/en/sandboxing
    - Confidence: high

19. Claude can retry a failed command unsandboxed unless `allowUnsandboxedCommands` is `false`; commands in `excludedCommands` run unsandboxed.
    - Quote: "Claude analyzes the failure and may retry the command with the `dangerouslyDisableSandbox` parameter" and "You can disable the unsandboxed retry by setting `"allowUnsandboxedCommands": false` in your sandbox settings"
    - Source: https://code.claude.com/docs/en/sandboxing
    - Confidence: high

20. The sandbox is turned on with `sandbox.enabled`; by default, if the platform cannot sandbox, commands run unsandboxed unless `sandbox.failIfUnavailable` is `true`. By default commands can read most of the machine, including credential files such as `~/.ssh`, unless `sandbox.filesystem.denyRead` is set; writes default to the working directory, and `sandbox.filesystem.denyWrite` narrows them.
    - Quote: "set `sandbox.enabled` to `true` in a settings file such as `~/.claude/settings.json`"; "By default, when the platform doesn't support the sandbox or the dependency check at startup fails, Claude Code runs commands without sandboxing. To make Claude Code exit at startup instead, set `sandbox.failIfUnavailable` to `true`."; reads default to "Most of the machine, including credential files such as `~/.ssh`"
    - Source: https://code.claude.com/docs/en/sandboxing
    - Confidence: high (added by the main session from the verifier report `research/verification/PHASE4.verify.md`)

## Inference
- Inference: a guard hook that reads `agent_type` from stdin and exits 2 (as `.claude/hooks/guard.py` in this repo is described to do) is the documented way to restrict writes per subagent; Bash deny rules alone would not be a reliable boundary, which is why CLAUDE.md calls the Bash check "best effort".
- Inference: for an unattended build agent, the docs suggest layering: deny rules + PreToolUse hook + sandbox network allowlist.

## Open questions
- The hooks page is ~293k characters; only the first ~200k were read. Exact verbatim wording of the per-event exit-code table was taken via the fetch summary.
- The sandboxing page tail (~11k characters) was not read.
