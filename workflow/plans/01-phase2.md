# Phase 2 plan: find a need of Wazuh users

## Context
Phase 2 of the brief: learn who uses Wazuh and how (using my lab, the Wazuh docs and any other useful source), then choose one need that a SaaS service built on top of Wazuh could serve. The Hub team builds SaaS services that extend Wazuh with AI, so the need should be one where such a service makes sense.

Deliverables:
- `PHASE2.md` answering 4 questions:
  1. Which needs did you find, and where did each one come from?
  2. Which ones did you discard, and why?
  3. Which one did you choose, who would benefit from it and how do they handle it today?
  4. Which service ideas did you consider before reaching yours, and what made you drop them?
- **Research**: the sources, notes, prompts and conversations that led to the choice.

The workflow is already set up (commit `e924229`): `CLAUDE.md`, the `researcher` and `verifier` agents, the guard hook, and the `research/` and `workflow/` folders. Decisions so far:
- **No new lab queries in Phase 2.** The lab evidence is `PHASE1.md` and `screenshots/`. Real API responses come in Phase 3.
- **Commits:** I propose each one (files + message) and wait for your OK.
- **Language:** everything in English.

## Steps

### Step 0: Setup (small)
- Save this plan as `workflow/plans/01-phase2.md`.
- Small change to `.claude/agents/researcher.md`: allow topic notes that cite several sources (front matter `url: multiple, see claims`). Every claim still has its own URL.
- Write each prompt to `workflow/prompts/phase2/NN-<name>.md` **before** running it, so every prompt is visible.

### Step 1: First-hand needs from my lab (main session, no web)
Read `PHASE1.md` and write `research/sources/lab-phase1-observations.md`. Each item points to a section of PHASE1.md or a screenshot instead of a URL (`source_type: own-lab`). Candidate needs already visible there:
- **Alert noise and triage:** a repeating rule 40704 alert (cups-browsed), and having to search the internet to understand it.
- **Getting started:** not knowing what to do next in the dashboard, and choosing an install method.
- **Hard-to-read events:** too much data, hard to interpret.
- **Vulnerability triage:** the "next day" item 3 in PHASE1.md.

These are one user's experience (mine). Step 2 has to show whether other users share them.

### Step 2: Web research, 4 researcher runs in parallel
Each run gets a narrow question and its own note prefix.

| Run | Question | Main sources | Note prefix |
|----|----------|--------------|-------------|
| R1 | Who uses Wazuh, and for what? Segments, company sizes, typical use cases, compliance drivers, MSSPs, Wazuh Cloud | documentation.wazuh.com, wazuh.com (use cases, customer stories), Wazuh blog | `users-` |
| R2 | What problems do users report? Most-reacted/commented issues and discussions about usability, alert fatigue, rules/decoders, upgrades, scaling, vulnerability detection | github.com/wazuh (issues, discussions) | `pain-github-` |
| R3 | Same question in the community: recurring complaints and questions | Wazuh forum / Google group, Reddit (r/Wazuh, r/sysadmin, r/cybersecurity), Stack Overflow / Server Fault, blogs | `pain-community-` |
| R4 | What already exists? Wazuh's own AI/LLM features and integrations, Wazuh Cloud, what is public about the Hub team, third-party tools and competing SIEM AI assistants | wazuh.com, Wazuh blog, GitHub, vendor pages | `landscape-` |

Rules for every run (they come from `CLAUDE.md` and the agent prompt; repeated in each prompt):
- Every claim has a URL.
- No personal data from forum posts.
- For pain points, record a **frequency signal**: issue reactions/comments, number of independent threads, and dates. These feed the scoring in Step 4.
- Prefer content from the last 2 years and the latest Wazuh 4.x.

R4 matters most for avoiding a wrong choice: it stops us from choosing a need that Wazuh already serves.

### Step 3: Verify
- Run `verifier` on every new note. Reports go to `research/verification/`.
- I go through the reports. Claims marked `NOT SUPPORTED` / `URL UNREACHABLE` are fixed by a researcher re-run or dropped.
- Every mistake I correct goes into `research/ai-log.md`.
- Update the index in `research/README.md` (note → verification status → used in).
- **Checkpoint commit (proposed):** `research: phase 2 sources and verification`.

### Step 4: Needs catalogue and shortlist (main session)
Write `research/phase2-needs.md`: one row per need with
- its sources: links to notes, and through them to URLs;
- who has it (segment from R1);
- how they handle it today.

Each need is scored 1–3 on:
- **Evidence:** number and independence of sources, and the frequency signals.
- **Pain:** time lost, risk, how often it happens.
- **SaaS on top of Wazuh fit:** can it be served from outside, using the Wazuh API / indexer data?
- **AI fit:** does AI add real value, or is it a plain feature?
- **Not already solved:** by Wazuh itself or by a common tool (from R4).
- **Data risk:** how sensitive the data that has to leave the customer is.

Each discarded need gets a written reason; that answers PHASE2.md question 2.

**Human decision point:** I present the top 3 with their scores. **You choose the need.** The agent only recommends.

### Step 5: Service ideas for the chosen need
- Write `research/phase2-ideas.md` with 4–6 service ideas for the chosen need. For each: what it does, the data it needs from Wazuh, where AI fits, and why it is kept or dropped (cost, data risk, overlap with Wazuh features, weak evidence, too broad for one service).
- If an idea needs a fact that isn't in the notes, run one targeted researcher pass and verify it.
- **Human decision point:** you choose the idea that goes into Phase 3. The dropped ideas and their reasons answer question 4.
- **Checkpoint commit (proposed):** `research: phase 2 needs catalogue and service ideas`.

### Step 6: Write PHASE2.md
- Draft the answers to the 4 questions using only verified claims, each with links to the notes/URLs. Keep it short and readable for the team, and keep the existing headings.
- You review and edit it. Every correction you make to the draft goes into `research/ai-log.md`.
- Final check: run `verifier` over the URLs cited in PHASE2.md (report: `research/verification/PHASE2.verify.md`).
- **Checkpoint commit (proposed):** `phase2: answers`.

### Step 7: Close the phase
- You export this session with `/export` into `workflow/transcripts/phase2-<date>.md`. I check it for personal data (emails, tokens, home paths beyond the username) before proposing the commit.
- Update `README.md` only if new files need a row in the structure table (e.g. `research/phase2-needs.md`, `research/phase2-ideas.md`).
- **Checkpoint commit (proposed):** `workflow: phase 2 transcript and index`.

## Files created or changed
- New: `workflow/plans/01-phase2.md`, `workflow/prompts/phase2/0[1-6]-*.md`, `research/sources/*.md`, `research/verification/*.verify.md`, `research/phase2-needs.md`, `research/phase2-ideas.md`, `workflow/transcripts/phase2-*.md`.
- Changed: `PHASE2.md`, `research/README.md`, `research/ai-log.md`, `.claude/agents/researcher.md` (small), maybe `README.md`.
- Never touched: `PHASE1.md`, `screenshots/`, anything in `.private/` except reading `task.pdf`.

## Time budget
About 4–5 h of the 15 h total:
- research and verification: ~2 h, mostly agents in parallel;
- catalogue and choice: ~1 h;
- ideas: ~45 min;
- PHASE2.md and review: ~1 h.

## Verification (end of phase)
- Every need in PHASE2.md links to at least one note, and every note has a verification report with `PASS`, or with its failing claims removed from use.
- No URL in PHASE2.md is missing from the notes. The final verifier report on PHASE2.md has no `NOT SUPPORTED`.
- Each of the 4 questions is answered, including the discarded needs (with reasons) and the dropped service ideas (with reasons).
- `git log` shows the checkpoint commits. `workflow/prompts/phase2/` holds every prompt that was used. `research/ai-log.md` has the corrections.
- PHASE1.md and screenshots/ are unchanged since `cb1f242`. Check with `git diff cb1f242 --stat -- PHASE1.md screenshots/`, which should print nothing.
