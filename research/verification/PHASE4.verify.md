---
note: PHASE4.md (draft), plus phase4/agent-setup/README.md and phase4/agent-setup/.claude/settings.json
verified: 2026-11-11
result: NEEDS FIXES
---

Totals for the 35 PHASE4.md rows: 20 SUPPORTED, 12 PARTIAL, 3 NOT SUPPORTED, 0 URL UNREACHABLE. All 6 external docs URLs were fetched. Diagram files (D4, D5) were not checked here.

## Claims: external links
| # | Verdict | Explanation / suggested fix |
|---|---------|-----------------------------|
| 1 | SUPPORTED | memory page: "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead." |
| 2 | SUPPORTED | hooks#common-input-fields: `agent_type` "Present when the session uses `--agent` or the hook fires inside a subagent." |
| 3 | SUPPORTED | sub-agents: "use the `tools` field as an allowlist or the `disallowedTools` field as a denylist." |
| 4 | SUPPORTED | worktrees: `isolation: worktree` for custom subagents (anchor section) and `--worktree` for sessions (same page, earlier section). |
| 5 | PARTIAL | The page says "a deny or ask rule ... isn't a security boundary around the program"; PHASE4 says "a Bash permission rule". Fix: write "a Bash deny or ask rule 'isn't a security boundary around the program'". |
| 6 | SUPPORTED | sandboxing: "tools such as Read, Edit, Write, WebFetch, and WebSearch follow permission rules instead." |

## Claims: this repository
| # | Verdict | Explanation / suggested fix |
|---|---------|-----------------------------|
| 7 | SUPPORTED | Table rows for `CLAUDE.md`, `.claude/agents/{researcher,verifier}.md`, `.claude/settings.json`, `guard.py`, `.githooks/pre-commit` match the files (pre-commit blocks PHASE1.md, screenshots/ and `.private/`). |
| 8 | PARTIAL | "One plan per phase": `workflow/plans/` has 00-workflow-setup, 01-phase2, 02-phase3, 03-phase4; none for Phase 1, and 00 is not a phase. Fix: "One plan per phase from 2 on, plus the setup plan". |
| 9 | PARTIAL | "saved before it ran" cannot be checked from the files; the prompts exist (18 files for setup + phases 2-3, 2 for phase 4). Fix: drop "before it ran" or confirm with `git log` dates. |
| 10 | NOT SUPPORTED | `workflow/transcripts/` contains only `.gitkeep`; plan 03 also says "transcripts still missing". Fix: export the sessions before publishing, or write "to be added". |
| 11 | SUPPORTED | `research/` holds notes, verification reports, `phase3-decisions.md`, `README.md`, `ai-log.md`. |
| 12 | PARTIAL | researcher "can only read the web and write notes in research/sources/": tools are WebSearch, WebFetch, Read, Glob, Grep, Write, Edit; it can also read local files (the write limit is the hook). Fix: "searches the web and can write only in research/sources/". |
| 13 | SUPPORTED | verifier tools: Read, Glob, Grep, WebFetch, Write (no WebSearch); `guard.py` limits its writes to `research/verification/`. |
| 14 | PARTIAL | "3 plans": phases 2-3 have 2 plans (01, 02); 3 only if the setup plan 00 is counted; 4 on disk with 03-phase4. Fix: "3 plans (setup, Phase 2, Phase 3)". |
| 15 | SUPPORTED | Prompts under `workflow/prompts/phase2/` (12) + `phase3/` (5) = 17 (the setup prompt `00-workflow-setup.md` is not counted). |
| 16 | SUPPORTED | 33 non-lab notes in `research/sources/` before the tooling notes, and 33 matching `*.verify.md` files. (The 2 lab notes have no report, correctly excluded.) |
| 17 | SUPPORTED | `PHASE2.verify.md` and `PHASE3.verify.md` exist. |
| 18 | SUPPORTED | `ai-log.md` has 13 rows. |
| 19 | SUPPORTED | ai-log row 9 (9 statements, PHASE2) and row 13 (12 statements, PHASE3); `research/README.md` agrees. |
| 20 | PARTIAL | "two or three options per decision with pros and cons": D1-D5 and D8 have option tables; D6 and D7 are a single proposal / failure table with no options. Fix: "for most decisions". |
| 21 | NOT SUPPORTED | "every decision says 'recommended by the agent and chosen by me'": D6 and D7 say "Proposed by the agent and accepted by me". Fix: "every decision says it was proposed or recommended by the agent and chosen or accepted by me". |
| 22 | SUPPORTED | Table rows and examples match ai-log rows 3/4/13 (examples), 2 (Wazuh staff), 1 and 10, 7, 12, 6. All 13 rows are covered; row 5 (inferences stated as facts) fits "more than the source says" loosely. |
| 23 | PARTIAL | "most common mistake, by far": 7 of 13 log rows are in that category; "by far" is your judgement. Fix: "the most common mistake (7 of the 13 log rows)" or prefix `Inference:`. |
| 24 | SUPPORTED | `guard.py` reads `agent_type`, blocks Phase 1 writes, gives researcher/verifier their folders, asks before `git push`; `settings.json` also has an `ask` rule for push. |
| 25 | SUPPORTED | ai-log row 7 is the token-budget row. |
| 26 | PARTIAL | The 7 layers match `pipeline.md` except "code security scans": pipeline step 5 lists "dependency and secret scan" only. Fix: drop "code" or add it to `pipeline.md`. |
| 27 | PARTIAL | "no production credentials or customer data where agents run ([`settings.json`])": settings.json only denies reads of `infra/prod/**`, `secrets/`, `.env` and `aws`/`kubectl` commands; it cannot ensure no credentials exist on the machine, and the sandbox default still lets commands READ `~/.ssh` and `~/.aws/credentials` unless `filesystem.denyRead` is set. Fix: move the link to the "permission rules" part, and say "no production credentials on the machine" is an environment rule (and consider `sandbox.filesystem.denyRead`). |
| 28 | PARTIAL | Short answer: "everything that must never happen ... is blocked by something the agent cannot change". In the example, `Edit(./.claude/**)` etc. only cover the built-in edit tools ("Edit rules apply to all built-in tools that edit files"); a Bash command can still write there, because the sandbox allows writes to the working directory and Bash deny rules are not a boundary. Real stops are the sandbox `denyWrite`, the hook (not included), branch protection and CODEOWNERS. Fix: add `sandbox.filesystem.denyWrite` for `.claude/`, `.github/`, `CODEOWNERS`, `evals/cases/`, or soften "cannot change" to "cannot change without a person noticing in review". |
| 29 | SUPPORTED | Split table roles exist as `reviewer`, `eval-runner`, `docs-keeper` (+ `implementer`) in `phase4/agent-setup/.claude/agents/`; reviewer is read-only (`tools: Read, Glob, Grep`). |
| 30 | PARTIAL | "runbook for each failure in the Phase 3 table (customer's Wazuh, connector, model, our service, database)": D7 / PHASE3 table has rows for the customer's Wazuh API or connector, the model, and the service; there is no "database" row. Fix: list the rows as they are, or add the database row to PHASE3 if intended. |
| 31 | SUPPORTED | EU only and pinned model (D5/D6), validator (D6), "separate database for large or regulated customers" (D3 C, PHASE3.md). |
| 32 | SUPPORTED | `phase2-ideas.md` has "what changed between syncs" and "Compliance evidence pack" ideas (I3/I4), not the chosen ones. |
| 33 | SUPPORTED | `CLAUDE.example.md` definition of done: docs in the same PR; CI fails if `services/` changes without `docs/` unless label `no-docs-needed` set by a person. |
| 34 | PARTIAL | "every claim here has a source, every note has a verification report, and `research/README.md` says where each note is used": PHASE4 contains many design statements without a source (by nature); the 2 lab notes have no report; `research/README.md` is an index of note, topic and verification, with no "where used" column (and does not yet list the tooling notes or PHASE4). Fix: "every research claim", "every web note", and add the column or drop "where each note is used". |
| 35 | NOT SUPPORTED | "most incidents follow a deploy" is a statement about the world with no source and no `Inference:`. Fix: source it, write `Inference:`, or reword as your practice ("I would look first at what changed"). |

## Opinions and proposals that should carry `Inference:` (or be reworded)
- "most incidents follow a deploy" (row 35).
- "The most common mistake, by far ..." and "A rule in the prompt did not stop it; a second agent ... did" (What I learned): interpretation of the log, not a logged fact.
- Already labelled and fine: the two `Inference:` lines (line of "the same in all five", "agents ... do not see slow drift", docs habit).
- Not checkable from files: "One Claude Code session in VS Code" (your own statement; fine).

## phase4/agent-setup/ against the tooling notes and the docs
| Item | Verdict | Explanation |
|------|---------|-------------|
| README: rule order deny, ask, allow; "an allow can never open a hole in a deny" | SUPPORTED | permissions page, note `tooling-claude-code-permissions-hooks-sandbox` claim 1. |
| README: Bash rules are "not a security boundary", `git -C . push` is not `git push` | SUPPORTED | permissions "What a Bash rule doesn't match" table lists exactly `git -C . push origin main`. |
| README: "UNVERIFIED: the key name `sandbox.enabled`" | SUPPORTED (key is documented) | sandboxing page: "set `sandbox.enabled` to `true` in a settings file such as `~/.claude/settings.json`" with a JSON example `{"sandbox": {"enabled": true, ...}}`. The settings page defers to the settings reference for sandbox keys. Fix: remove the UNVERIFIED line (and add the key to the tooling note). |
| settings.json: `"sandbox": {"enabled": true, "allowUnsandboxedCommands": false}` | SUPPORTED | Both keys documented: "You can disable the unsandboxed retry by setting `"allowUnsandboxedCommands": false` in your sandbox settings." |
| settings.json: rule syntax (`Read(./.env)`, `Edit(./.github/**)`, `Bash(make test *)`, `Bash(git push --force *)`) | SUPPORTED | Same syntax as the docs (gitignore patterns, trailing ` *` prefix). `Bash(make test *)` does not match `make test-isolation`, which has its own rule: correct. |
| settings.json: deny/ask/allow precedence in the file | SUPPORTED | `ask: Bash(git push *)` and `deny: Bash(git push --force *)` coexist correctly (deny is checked first). |
| README: "`CLAUDE.example.md` is not named `CLAUDE.md` because Claude Code also reads CLAUDE.md files in subfolders" | PARTIAL | True on the memory page ("Files in subdirectories load on demand"), but this fact is not in any tooling note, and the README says its facts are "checked in" the permissions note. Fix: add the claim to a tooling note. |
| settings.json: hook command points to `.claude/hooks/guard.py` | PARTIAL | The file is not in `phase4/agent-setup/` (the README says so). The hook, the per-agent write folders of `eval-runner` and `docs-keeper`, and those two agents' "write only under ..." rules are therefore instructions only in the example. Fix: say so in `pipeline.md` step 3 ("Enforced by") or include a guard.py. |
| settings.json: missing `sandbox.failIfUnavailable` | PARTIAL | Sandboxing page: "By default, when the platform doesn't support the sandbox or the dependency check at startup fails, Claude Code runs commands without sandboxing. To make Claude Code exit at startup instead, set `sandbox.failIfUnavailable` to `true`." The setup relies on the sandbox, so add `"failIfUnavailable": true`. |
| settings.json: no `network.allowedDomains` / `filesystem.denyRead` / `denyWrite` | PARTIAL | Network defaults to an empty allowlist (fine). Reads default to "Most of the machine, including credential files such as `~/.ssh`"; writes default to the working directory (so `.claude/` is writable by Bash). Documented keys: `sandbox.filesystem.denyRead`, `sandbox.filesystem.denyWrite`. |
| UNVERIFIED risk (not a finding): `Edit(./.claude/**)` for an `implementer` subagent running in a worktree | UNVERIFIED | Worktrees live under `<repo>/.claude/worktrees/<name>/`. The pages I read do not say how a `./`-relative deny pattern resolves for a subagent isolated in a worktree. If it resolves against the main checkout, it could deny all of the implementer's edits. Test in the lab before presenting it as working. |
| Minor: `implementer` is told to open a pull request, but no `gh pr create` rule exists | PARTIAL | Not in allow, so it prompts; in `-p`/`dontAsk` runs it would be denied. Add an allow rule if the agent should do it. |

## Note-level problems
- Language English; no personal data; no external-link problems beyond the PARTIALs above.
- `research/README.md` is out of date for Phase 4 (no tooling notes, no PHASE4 row).
- `phase4/agent-setup/README.md` carries a stale UNVERIFIED marker (see above).

## Recommended fixes (priority order)
1. Row 10: `workflow/transcripts/` is empty; the table row and the plan promise it. Export or reword.
2. Rows 21, 35: correct "every decision says ..." and remove or label "most incidents follow a deploy".
3. Row 28 and settings.json: add `sandbox.filesystem.denyWrite` for the protected paths, `sandbox.failIfUnavailable: true`, optionally `denyRead` for credentials; or soften "cannot change".
4. README: delete the UNVERIFIED `sandbox.enabled` line; add `sandbox.enabled`, `failIfUnavailable` and the subfolder-CLAUDE.md fact to the tooling note.
5. Rows 8, 14, 30, 34, 20, 26, 12, 5, 23: narrow wording as described in each row.
