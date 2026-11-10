# AI corrections log

Every time I had to correct an AI agent during Phases 2–4, I add a row here: wrong claims,
invented or misread sources, bad reasoning, ignored rules or wrong assumptions. This log is
the evidence for the PHASE4.md question "where did you have to correct it?".

| # | Date | Phase | Agent | What the AI did | Why it was wrong | How I caught it | Fix | Commit |
|---|------|-------|-------|-----------------|------------------|-----------------|-----|--------|
| 1 | 2026-11-10 | Setup | Claude Code (main) | Described my lab as "Wazuh 4.x on virtual machines I own" in the plan and in CLAUDE.md | Assumption, not fact: the brief allows VMs or containers, and the agent never checked PHASE1.md. The server, indexer and dashboard run in Docker; the agent runs on my own Ubuntu machine | I reviewed CLAUDE.md after the setup commit | Lab description fixed in CLAUDE.md; correction note added to `workflow/plans/00-workflow-setup.md` | see `git log -- CLAUDE.md` |
