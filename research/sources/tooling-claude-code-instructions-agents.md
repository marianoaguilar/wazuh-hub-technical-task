---
title: How Claude remembers your project; Subagents; Skills (Claude Code docs)
url: multiple, see claims
publisher: Anthropic (code.claude.com)
source_type: official-docs
wazuh_version: n/a
accessed: 2026-11-11
question: Phase 4. Where Claude Code reads project instructions (CLAUDE.md), whether subagents follow them, how subagents are defined and restricted, and what skills are.
---

## Summary
Official Claude Code documentation on project instructions (CLAUDE.md), custom subagents (`.claude/agents/*.md`) and skills. CLAUDE.md is loaded as context at session start from the working directory and every directory above it; it is guidance, not enforced configuration. Custom subagents load the same CLAUDE.md hierarchy unless they opt out, and their `tools` frontmatter field acts as an allowlist. Skills are `SKILL.md` instruction files that Claude uses when relevant or that the user invokes with `/skill-name`.

## Claims
1. Project instructions can live in `./CLAUDE.md` or `./.claude/CLAUDE.md`; other scopes are a managed policy file, `~/.claude/CLAUDE.md` (user) and `./CLAUDE.local.md` (local, personal).
   - Quote: "A project CLAUDE.md can be stored in either `./CLAUDE.md` or `./.claude/CLAUDE.md`."
   - Source: https://code.claude.com/docs/en/memory
   - Confidence: high

2. Claude Code loads CLAUDE.md and CLAUDE.local.md from the current working directory and every directory above it; the files are concatenated, not overriding each other.
   - Quote: "Claude Code loads `CLAUDE.md` and `CLAUDE.local.md` from your current working directory and every directory above it." / "All discovered files are concatenated into context rather than overriding each other."
   - Source: https://code.claude.com/docs/en/memory#how-claude-md-files-load
   - Confidence: high

3. CLAUDE.md is context, not enforced configuration; the docs point to a PreToolUse hook to block an action regardless of what Claude decides.
   - Quote: "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead."
   - Source: https://code.claude.com/docs/en/memory
   - Confidence: high

4. Custom subagents load every level of the CLAUDE.md hierarchy that the main conversation loads; the built-in Explore and Plan agents skip it, and a custom subagent can opt out with `omitClaudeMd`.
   - Quote: "every level of the CLAUDE.md hierarchy the main conversation loads, including `~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, managed policy files [...]. The built-in Explore and Plan agents skip this."
   - Source: https://code.claude.com/docs/en/sub-agents#what-loads-at-startup
   - Confidence: high

5. A subagent starts with a fresh, isolated context window and does not see the parent conversation history (forks are the exception); its system prompt is its own prompt, not the Claude Code system prompt.
   - Quote: "Each subagent starts with a fresh, isolated context window. It doesn't see your conversation history, the skills you've already invoked, or the files Claude has already read."
   - Source: https://code.claude.com/docs/en/sub-agents#what-loads-at-startup
   - Confidence: high

6. The main conversation's auto memory is not loaded into subagents (except forks).
   - Quote: "The main conversation's auto memory isn't loaded into subagents; the exception is a fork, which inherits the parent conversation and system prompt."
   - Source: https://code.claude.com/docs/en/memory
   - Confidence: high

7. Subagents are Markdown files with YAML frontmatter; project subagents live in `.claude/agents/`, user subagents in `~/.claude/agents/`. Other scopes are managed settings, the `--agents` CLI flag and plugins; on a name clash the higher-priority location wins.
   - Quote: "Subagents are Markdown files with YAML frontmatter." / "**Project subagents** (`.claude/agents/`) are ideal for subagents specific to a codebase."
   - Source: https://code.claude.com/docs/en/sub-agents
   - Confidence: high

8. Frontmatter fields include `name` and `description` (required), `tools`, `disallowedTools`, `model`, `permissionMode`, `hooks`, `isolation`, `omitClaudeMd`, `skills` and `memory`.
   - Quote: "`tools`: Tools the subagent can use, as a comma-separated string such as `Read, Grep, Bash` or a YAML list. Inherits every tool available to subagents if omitted."
   - Source: https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
   - Confidence: high (field names as returned by the fetch of the official page)

9. The `tools` field is an allowlist and `disallowedTools` a denylist; if `tools` is omitted the subagent inherits all tools available to subagents.
   - Quote: "To restrict tools, use the `tools` field as an allowlist or the `disallowedTools` field as a denylist."
   - Source: https://code.claude.com/docs/en/sub-agents
   - Confidence: high

10. `model` accepts an alias (`sonnet`, `opus`, `haiku`, ...), a full model ID, or `inherit`.
    - Quote: "`sonnet`, `opus`, `haiku`, `fable`, a full model ID such as `claude-opus-5-5`, or `inherit`."
    - Source: https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields
    - Confidence: high

11. By default a subagent can spawn its own subagents up to three layers deep; omitting `Agent` from `tools` stops one subagent from spawning.
    - Quote: "By default, a subagent can spawn subagents of its own, up to three layers below the main conversation."
    - Source: https://code.claude.com/docs/en/sub-agents
    - Confidence: high

12. Skills: a `SKILL.md` file with instructions that Claude adds to its toolkit and uses when relevant, or that the user invokes with `/skill-name`. Project skills live at `.claude/skills/<skill-name>/SKILL.md`.
    - Quote: "Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit."
    - Source: https://code.claude.com/docs/en/skills
    - Confidence: high

13. A skill's `allowed-tools` frontmatter grants tools without asking only during the turn that invokes the skill.
    - Quote: "Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message."
    - Source: https://code.claude.com/docs/en/skills
    - Confidence: high

## Inference
- Inference: this repo's setup (CLAUDE.md at root, `researcher`/`verifier` in `.claude/agents/` with a `tools:` list) matches the documented mechanism: both agents receive CLAUDE.md, and the `tools` list is an enforced allowlist, while the rules written in CLAUDE.md are only instructions. That is consistent with the "enforced vs instructed" table in CLAUDE.md.

## Open questions
- The sub-agents page is about 117k characters; the last ~17k were not read. The full frontmatter field list was taken from the fetch summary, not a verbatim table copy.
- The skills page tail (~19k characters) was not read.
