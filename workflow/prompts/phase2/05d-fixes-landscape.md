# Prompt 05d (R4 fixes): apply verification findings to the `landscape-` notes

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with the other 05-fixes prompts and prompt 06)
- Plan step: Phase 2, Step 3 (`workflow/plans/01-phase2.md`)

## Prompt

> Fix the notes `research/sources/landscape-*.md` using their verification reports
> `research/verification/landscape-*.verify.md`.
>
> For each note:
> 1. Read the note and its report.
> 2. Fix every claim marked `PARTIAL` or `NOT SUPPORTED` and every note-level problem the report
>    lists. Either reword the claim so it says only what the cited page says (re-fetch the page to
>    check), add the missing URL of a page you fetch now, move the content to `Inference:` /
>    `UNVERIFIED:`, or drop it. Lower the confidence when the evidence is weaker than stated.
> 3. Do not touch claims marked `SUPPORTED`, except to apply an optional fix the report suggests.
> 4. Do not add new claims or new themes.
> 5. Add a section `## Changes after verification` at the end of the note listing each change
>    in one line (claim number, what changed, why).
>
> Specific rules, from mistakes found in this round:
> - Never call a poster "Wazuh staff", "maintainer", "Wazuh representative" or "Wazuh-side" unless
>   the page itself shows that role. Otherwise write "a reply in the thread".
> - Counts must be exactly what the page shows. One commenter is "a commenter". A 👍 on a comment
>   is not a 👍 on the issue. A search result count is not a theme count.
> - Give the latest status of each issue/thread as shown on the page (open/closed, "fixed in X").
> - An absence on a page is only an absence on that page: "the page X does not mention Y", never
>   "Wazuh has no Y".
> - Dates from Google Group listings are last-activity dates; say so.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent sources, numbers or quotes; no personal data; English only. Edit only
> the `landscape-` notes.
>
> When done, reply with at most 10 lines: notes changed, claims dropped, confidence changes.
