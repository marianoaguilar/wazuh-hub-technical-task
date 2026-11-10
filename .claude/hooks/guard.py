#!/usr/bin/env python3
"""PreToolUse guard for this repository.

Claude Code runs this before every matching tool call and sends the call as JSON on stdin.
Exit code 2 blocks the call and shows stderr to the agent. Printing a JSON
`permissionDecision: "ask"` makes Claude Code ask the user first.

What it enforces (see CLAUDE.md, "Guardrails"):
  1. No writes to PHASE1.md or screenshots/ (file tools; Bash on a best-effort basis).
  2. In .private/, only .private/task.pdf can be read; Bash may not mention .private at all.
  3. The researcher subagent writes only under research/sources/,
     the verifier subagent only under research/verification/.
  4. Any `git ... push` command needs the user's confirmation.

Uses only the Python standard library (jq is not installed in my environment).
"""
import json
import os
import re
import sys

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
FILE_TOOLS = WRITE_TOOLS | {"Read", "Grep", "Glob"}

PRIVATE_DIR = ".private"
PRIVATE_ALLOWED = ".private/task.pdf"

AGENT_WRITE_DIRS = {
    "researcher": "research/sources/",
    "verifier": "research/verification/",
}

# Bash: commands that mention a protected path together with one of these are blocked.
PROTECTED_IN_BASH = re.compile(r"PHASE1\.md|screenshots(/|\b)")
BASH_WRITE = re.compile(
    r">"                                        # any redirection
    r"|\b(rm|mv|cp|tee|truncate|dd|touch|chmod|chown|ln|shred|install|rsync)\b"
    r"|\bsed\b[^|;&]*\s-[a-zA-Z]*i"             # sed -i
    r"|\bperl\b[^|;&]*\s-[a-zA-Z]*i"            # perl -i
    r"|\bgit\s+(checkout|restore|rm|mv|reset|stash|apply|am|clean|filter-branch|filter-repo)\b"
    r"|\b(python3?|node|ruby|awk)\b"            # interpreters can write anything
)
GIT_PUSH = re.compile(r"\bgit\b[^;&|\n]*\bpush\b")


def block(reason: str) -> None:
    print(f"Blocked by .claude/hooks/guard.py: {reason}", file=sys.stderr)
    sys.exit(2)


def ask(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def rel_to_root(path: str, root: str, cwd: str) -> str:
    """Path relative to the project root, with symlinks and '..' resolved."""
    if not os.path.isabs(path):
        path = os.path.join(cwd, path)
    real = os.path.realpath(path)
    rel = os.path.relpath(real, os.path.realpath(root))
    return rel.replace(os.sep, "/")


def is_under(rel: str, folder: str) -> bool:
    folder = folder.rstrip("/")
    return rel == folder or rel.startswith(folder + "/")


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        block("could not parse the hook input; refusing to guess")

    tool = data.get("tool_name", "")
    ti = data.get("tool_input") or {}
    cwd = data.get("cwd") or os.getcwd()
    root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd
    agent = data.get("agent_type") or ""

    if tool in FILE_TOOLS:
        raw = ti.get("file_path") or ti.get("notebook_path") or ti.get("path") or ""
        rel = rel_to_root(raw, root, cwd) if raw else ""

        # Glob/Grep patterns can point into .private without a path argument.
        pattern = f"{ti.get('pattern', '')} {ti.get('glob', '')}"
        if tool in {"Glob", "Grep"} and PRIVATE_DIR in pattern:
            block("searching inside .private/ is not allowed")

        if rel and is_under(rel, PRIVATE_DIR):
            if not (tool == "Read" and rel == PRIVATE_ALLOWED):
                block(f"only {PRIVATE_ALLOWED} may be read in .private/ (got {tool} on {rel})")

        if tool in WRITE_TOOLS and rel:
            if rel == "PHASE1.md" or is_under(rel, "screenshots"):
                block(f"{rel} is Phase 1 work written without AI and must not be modified")
            allowed_dir = AGENT_WRITE_DIRS.get(agent)
            if allowed_dir and not is_under(rel, allowed_dir):
                block(f"the {agent} agent may only write under {allowed_dir} (got {rel})")
        sys.exit(0)

    if tool == "Bash":
        cmd = ti.get("command", "")
        if PRIVATE_DIR in cmd:
            block("shell commands may not touch .private/ (use the Read tool on .private/task.pdf)")
        if PROTECTED_IN_BASH.search(cmd) and BASH_WRITE.search(cmd):
            block("this shell command could modify PHASE1.md or screenshots/, which are read-only")
        if GIT_PUSH.search(cmd):
            ask("git push publishes the repository; confirm it explicitly")
        sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
