# Research

Sources and notes behind PHASE2.md and PHASE3.md.

## How notes are made

1. I write a prompt for the `researcher` agent (saved in `workflow/prompts/`).
2. `researcher` writes one note per source or topic in `sources/`, each claim with a URL and a quote.
3. `verifier` fetches every cited URL and writes a report per note in `verification/`.
4. I review both. Only claims that passed verification are used in the PHASE files.
5. Corrections I make to the AI go in [`ai-log.md`](ai-log.md).

Agent definitions: [`../.claude/agents/`](../.claude/agents/). Rules: [`../CLAUDE.md`](../CLAUDE.md).

## Index

| Note | Topic | Verification | Used in |
|------|-------|--------------|---------|
