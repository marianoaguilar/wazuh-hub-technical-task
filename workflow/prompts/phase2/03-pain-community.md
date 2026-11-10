# Prompt 03 (R3): problems users report in the community

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with prompts 01, 02, 04)
- Plan step: Phase 2, Step 2 (`workflow/plans/01-phase2.md`)

## Prompt

> Research question: **What do Wazuh users complain about or ask for help with, outside GitHub?**
>
> Sources: the Wazuh community forum / Google group (wazuh mailing list) if public, Reddit
> (r/Wazuh, r/sysadmin, r/cybersecurity, r/homelab, r/msp), Stack Overflow / Server Fault, and
> blog posts or reviews by people who run Wazuh (including review sites such as G2, Capterra,
> Gartner Peer Insights or PeerSpot if their pages can be fetched).
>
> Find the recurring themes: what is hard, slow, confusing or missing when running Wazuh
> (for example alert noise, learning curve, rule tuning, interpreting alerts, vulnerability
> results, resource usage, upgrades, reporting, compliance, MSSP operation). Also note what users
> say they like, because that helps judge what is already well served.
>
> For each theme record a **frequency signal**: how many independent threads/posts/reviews you
> read that mention it, with their dates and, when shown, upvotes or comment counts. Never
> estimate numbers that the page does not show. Prefer the last 2 years.
> If Reddit pages cannot be fetched directly, try the `old.reddit.com` URL; if that fails too,
> list them under "Not read" and do not use them.
>
> Output: topic notes under `research/sources/` with the prefix `pain-community-` (for example
> `pain-community-learning-curve.md`), one per theme with real evidence. At most 7 notes. Topic
> notes may use `url: multiple, see claims`. Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent posts, counts or quotes; mark confidence (a single forum post is
> `low`); keep inference apart from claims; no personal data (never record usernames, names or
> company names of posters; write "a Reddit user reports"); English only.
>
> When done, reply with at most 10 lines: files written and the strongest themes, with their
> frequency signals.
