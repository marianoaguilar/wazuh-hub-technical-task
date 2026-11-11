# Example agent setup for the triage ledger service

This folder shows, as real files, the agent setup of diagram D5 in [`PHASE4.md`](../../PHASE4.md):
what the agents that build the service know, what they can do and what they cannot do. It is an
example for the service repository. It is **not used by this repository** and is not deployed
anywhere.

| File | In the service repo it would be | What it shapes |
|------|-------------------------------|----------------|
| [`CLAUDE.example.md`](CLAUDE.example.md) | `CLAUDE.md` | What every agent **knows**: context, architecture rules that must never break, how to test, definition of done |
| [`.claude/settings.json`](.claude/settings.json) | `.claude/settings.json` | What agents **can and cannot do**: allow / ask / deny rules, sandbox, hooks |
| [`.claude/agents/`](.claude/agents/) | `.claude/agents/` | Four roles with their own tools: `implementer`, `reviewer`, `eval-runner`, `docs-keeper` |
| [`pipeline.md`](pipeline.md) | `docs/process/pipeline.md` | How a task moves from an idea to production, and which checks are enforced outside the agent |

`CLAUDE.example.md` is not named `CLAUDE.md` on purpose: Claude Code also reads `CLAUDE.md` files
in subfolders, so the service's rules would mix with the rules of this task repository.

## Notes on `settings.json`

Facts from the Claude Code docs, checked in
[`research/sources/tooling-claude-code-permissions-hooks-sandbox.md`](../../research/sources/tooling-claude-code-permissions-hooks-sandbox.md):

- Rules are evaluated deny, then ask, then allow, so an `allow` can never open a hole in a `deny`.
- Bash rules match the command text and are "not a security boundary": `git -C . push` is not
  `git push`. That is why the real limits are elsewhere: the sandbox for shell commands, the
  `guard.py` hook (as in this task's repository, it reads `agent_type` to give each agent its own
  write folder, for example `eval-runner` only under `evals/reports/`), and, strongest of all,
  branch protection on GitHub and no production credentials on the development machine.
- The agent's own settings, agents and hooks, `.github/`, `CODEOWNERS` and the exam cases are
  denied twice: `Edit` rules stop the file tools, and `sandbox.filesystem.denyWrite` stops shell
  commands, because `Edit` rules do not cover Bash. An agent must not change its own rules, the CI
  that checks it or the answers of the exam. Only those files are listed, not all of `.claude/`:
  Claude Code keeps worktrees under `.claude/worktrees/`, and the `implementer` works there.
- `sandbox.failIfUnavailable` makes Claude Code stop instead of running commands unsandboxed, and
  `denyRead` hides credential files that the sandbox would otherwise let commands read (sandbox
  keys checked in [`PHASE4.verify.md`](../../research/verification/PHASE4.verify.md)).
- UNVERIFIED: the exact path syntax inside `sandbox.filesystem` (written here like the permission
  rules), and whether the worktree folder works with these deny rules. Both need a test before use.
- `guard.py` is not included here; [the one in this repository](../../.claude/hooks/guard.py) shows
  the pattern.

## The idea in three lines

1. **Know:** agents get the rules from files in the repo (CLAUDE.md, the design decisions, the
   docs), not from my memory of a chat.
2. **Can / cannot:** what must never happen is blocked by layers outside the prompt (permissions,
   sandbox, hooks, branch protection, required CI checks, no production credentials on the dev
   machine). None is enough alone; together an agent cannot get past them without a person noticing.
3. **Flow:** every change goes through a person twice: when the task is defined and when it is
   merged.
