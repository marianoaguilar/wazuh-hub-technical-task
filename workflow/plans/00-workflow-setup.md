# Agent workflow setup (before Phase 2)

## Context
The brief (`.private/task.pdf`) says Phases 2–4 are done with AI agents. The repo must show "your plan, your commits and everything you used to direct your agents", and also "your research: the sources you used and the notes, prompts or conversations that led you to your choice", plus "the diagrams and their sources". Ground rules: English deliverables, own lab only, no real malware, no sensitive or personal data. Phase 1 (`PHASE1.md`, `screenshots/`) is finished, was written without AI, and must stay untouched.

Repo today: `README.md`, `PHASE1.md`, `screenshots/` (4 PNGs), untracked `PHASE2.md` (only the question headings) and `.gitignore` (contains `.private`). There is no `.claude/` folder yet.

## Key limit of Claude Code (this drives the ENFORCED / INSTRUCTED labels)
- `Read(...)` and `Edit(...)` permission rules only cover Claude's file tools (Read/Grep/Glob and Edit/Write/NotebookEdit). **They do not cover Bash.** `cat .private/x` or `sed -i ... PHASE1.md` are not blocked by them. So I add a PreToolUse hook that also checks Bash commands, and I give the subagents no Bash tool.
- Order of precedence is deny > ask > allow. You can't write "deny `.private/**`, but allow `task.pdf`" as rules, because the deny always wins. The hook makes that exception instead.
- Permission rules apply to the whole session. You can't set them per subagent. A subagent's limits come from its `tools:` list. A path limit for one specific agent needs the hook, and the hook needs to know which agent made the call (see the uncertainty note below).

## 1. `CLAUDE.md` (root) — outline
- **Project context**: Wazuh Hub technical task, 5 phases, 72h. Where things live (folder table). The lab is Wazuh 4.x on my own VMs.
- **Task rules**: deliverables in English. Only my own lab: never call or scan hosts I don't own. No real malware. No personal or sensitive data. Redact JWTs, passwords, API keys, real hostnames and public IPs from Wazuh API output before saving it (Phase 3 needs real API responses). Never edit `PHASE1.md` or `screenshots/`; reading them for context is OK. Never read anything in `.private/` except `task.pdf`, and never copy its text into the repo verbatim.
- **Agent working rules**: every research claim has a source URL next to it. Never invent sources, URLs, quotes or numbers. If a page can't be fetched, say so. Flag uncertainty explicitly with `UNVERIFIED:` / confidence levels. Write results to files (paths given per task), and keep chat replies to a short summary plus the file paths. Official Wazuh docs/GitHub beat forums, and forums beat blogs. Write down the access date.
- **Workflow**: plan in `workflow/plans/` → prompt saved in `workflow/prompts/` → researcher → verifier → I review → write the PHASEn.md answer → commit. Log every AI mistake I correct in `research/ai-log.md`. Small commits with prefixes (`workflow:`, `phase2:`, `research:`…). Never `git push` without asking.

## 2. Subagents in `.claude/agents/`
**`researcher.md`**
- `tools: WebSearch, WebFetch, Read, Glob, Grep, Write, Edit`. No Bash.
- Prompt: one note per source or topic in `research/sources/<topic>-<slug>.md`, using a fixed template: front matter `url`, `title`, `publisher`, `source_type` (official-docs | github | forum | reddit | blog | other), `accessed`. Then a list of claims, each with a short quote and its URL, a confidence level, and open questions. Never write outside `research/sources/`.

**`verifier.md`**
- `tools: Read, Glob, Grep, WebFetch, Write`. No WebSearch, so it can only check the URLs the note cites and can't go looking for new ones. No Edit, no Bash.
- Prompt: for each note, fetch every URL and mark each claim as SUPPORTED / PARTIAL / NOT SUPPORTED / URL UNREACHABLE. Write `research/verification/<note-name>.verify.md`. Never change notes.

## 3. `.claude/settings.json`
```json
{
  "permissions": {
    "deny": [
      "Edit(/PHASE1.md)", "Write(/PHASE1.md)",
      "Edit(/screenshots/**)", "Write(/screenshots/**)",
      "Read(/.private/*/**)"
    ],
    "ask": ["Bash(git push:*)"]
  },
  "hooks": {
    "PreToolUse": [{ "matcher": "Read|Grep|Glob|Edit|Write|NotebookEdit|Bash",
                     "hooks": [{ "type": "command", "command": ".claude/hooks/guard.sh" }] }]
  }
}
```
`.claude/hooks/guard.sh` (bash + `jq`) reads the tool call JSON and exits with code 2 (block, with a reason) when:
- a file tool targets `.private/` and the path isn't `.private/task.pdf`;
- a Bash command mentions `.private`;
- a Bash command mentions `PHASE1.md` or `screenshots/` together with a write pattern (`>`, `sed -i`, `rm`, `mv`, `cp`, `tee`, `truncate`, `git checkout --`/`restore`);
- Edit or Write comes from the researcher outside `research/sources/`, or from the verifier outside `research/verification/`.

Extra safety net outside Claude: `.githooks/pre-commit` (turned on with `git config core.hooksPath .githooks`). It rejects any commit that changes `PHASE1.md`, `screenshots/` or anything under `.private/`. Also add `.claude/settings.local.json` to `.gitignore`.

## 4. Folder structure
```
CLAUDE.md
.claude/agents/{researcher,verifier}.md
.claude/hooks/guard.sh
.claude/settings.json
.githooks/pre-commit
research/
  sources/          researcher notes (one per source/topic)
  verification/     verifier reports
  ai-log.md         AI corrections log: date | phase | what AI said | why wrong | how caught | fix | commit
  README.md         index: notes → verification status → used in PHASEn.md
workflow/
  plans/            plans (this one is saved first, as 00-workflow-setup.md)
  prompts/          prompts I gave to agents, numbered per phase (phase2/01-…md)
  transcripts/      exported sessions (/export), checked for personal data before commit
diagrams/
  src/              diagram sources (Mermaid .mmd / draw.io), required by the brief
  *.svg|png         rendered output, with the same name as the source
```

## 5. README update
Add these rows to the structure table: `CLAUDE.md`, `.claude/` (agents, hooks, permissions), `.githooks/`, `research/` (+ `sources/`, `verification/`, `ai-log.md`), `workflow/` (`plans/`, `prompts/`, `transcripts/`), `diagrams/` (+ `src/`). Add a short "How I work with agents" paragraph linking to `CLAUDE.md` and `workflow/`. Keep the existing rows as they are.

## Guardrails: ENFORCED vs INSTRUCTED
| Guardrail | Status | Mechanism / gap |
|---|---|---|
| No edits to `PHASE1.md` / `screenshots/` from file tools | **ENFORCED** | deny rules |
| Same, through Bash | **ENFORCED (best effort)** | the hook matches strings in the command, so unusual commands could get past it |
| Same, at commit time | **ENFORCED** | git pre-commit hook (`--no-verify` skips it, and only a person would run that) |
| No reading `.private/` except `task.pdf` | **ENFORCED** for file tools (hook + deny on subfolders); **best effort** for Bash (the hook blocks any Bash command that mentions `.private`) | |
| `.private/` never committed | **ENFORCED** | `.gitignore` + pre-commit (`git add -f` skips `.gitignore`, the pre-commit still catches it) |
| Ask before `git push` | **ENFORCED** for `git push …` | `ask` rule; odd forms like `git -C . push` don't match the prefix, so the hook also checks for `push` |
| Researcher/verifier have no Bash; verifier has no WebSearch and no Edit | **ENFORCED** | `tools:` lists |
| Researcher writes only in `research/sources/`, verifier only in `research/verification/` | **ENFORCED if the hook can tell which agent made the call**, otherwise **INSTRUCTED** | see the uncertainty note |
| Verifier never changes notes | **ENFORCED** that it can't Edit; overwriting a note with Write is blocked only by the hook path check above | |
| Every claim has a source URL, never invent sources | **INSTRUCTED**, then **checked** by the verifier | no tool can enforce it, so the verifier is the control |
| Flag uncertainty | **INSTRUCTED** | |
| Results go to files, not chat | **INSTRUCTED** | |
| English deliverables | **INSTRUCTED** | |
| Own lab only, no malware, no personal/sensitive data, redact API output | **INSTRUCTED** | I review before every commit |
| Transcripts free of personal data | **INSTRUCTED**, and I review them by hand | |

**Uncertainty to check before implementing:** whether the PreToolUse hook input says which subagent made the call (an `agent_type`-style field) in the installed Claude Code version. I'll check the docs or run a quick test. If it doesn't, the per-agent path limits stay INSTRUCTED and I'll label them that way.

## Verification (after implementation)
- Ask Claude to edit `PHASE1.md` → blocked. Run `echo x >> PHASE1.md` through Bash → blocked by the hook.
- Read `.private/task.pdf` → allowed. Read any other file in `.private/`, or run `cat .private/task.pdf` → blocked.
- `git push` → asks first.
- Run the researcher on a tiny topic → the note appears in `research/sources/`. Ask it to write somewhere else → refused or blocked. Run the verifier → report appears in `research/verification/`.
- Stage a change to `PHASE1.md` and commit → the pre-commit hook rejects it. Then `git restore`.
- `git status` shows `.private/` is still ignored. Commit as `workflow: agent setup`, with this plan saved in `workflow/plans/`.

## Implementation notes (2026-11-10)
- **Hook in Python, not bash + jq**: `jq` is not installed, so the guard is `.claude/hooks/guard.py` (standard library only).
- **Per-agent write paths are ENFORCED**: in Claude Code 2.1.322 the PreToolUse hook input includes `agent_type` (with `agent_id`) when the call comes from a subagent. The uncertainty above is resolved.
- **Only `Edit(...)` deny rules**: `Edit` rules already cover every built-in file-editing tool, so no separate `Write(...)` rules were added.
- **`/path` in project settings** resolves from the project root (checked in the CLI's own schema text).
- **Tests**: 26 guard cases pass (allow/block/ask). The pre-commit hook rejects a PHASE1 change, a screenshot rename and a forced `.private` add, and allows a normal commit (tested in a throwaway repo).
- **The guard was live during setup**: it blocked two of my own shell commands only because their text mentioned protected paths (a test on a throwaway repo, and a heredoc). That is expected for a text match.
- **Correction (from my review)**: the lab is not on VMs. The Wazuh server, indexer and dashboard run in Docker, and the agent runs on my own Ubuntu machine. CLAUDE.md is fixed; the plan text above is left as approved. Logged in `research/ai-log.md` (#1).
- **Known gap in the Bash guard, found while testing**: it matches the command text. A command that writes its actions into a script file first and then runs the script is not inspected. So the Bash guard stays "best effort", and the git pre-commit hook is the last line of defence for PHASE1.md and screenshots/.
