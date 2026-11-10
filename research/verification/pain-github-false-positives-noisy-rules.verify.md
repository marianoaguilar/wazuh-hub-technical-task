---
note: research/sources/pain-github-false-positives-noisy-rules.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | #19346 page: title as quoted, closed, opened Sep 29, 2023, linked PR #25634, labels level/task and type/bug, 47 thumbs-up. The thumbs-up sorted list shows it first (closed Oct 4, 2024) with 61 next to it. The number is unlabeled in my fetch, but it matches the issue page (29 visible timeline entries plus "34 remaining items", one of them a label event, so about 62 comments). |
| 2 | SUPPORTED | Ubuntu 22.04, Debian 12, Fedora 39 and Pop!_OS 22.04 are on the page, with versions 4.5.3 to 4.13.1. Commenters suggest disabling rootcheck/SCA. Both quotes are on the page. The latest comment (May 1, 2026) carries a "Contributor" badge and contains "this here should be already fixed by them 4.13.1 released last year." The issue is closed. Arch is no longer claimed. |
| 3 | SUPPORTED | #20363: open, opened Nov 21, 2023, no labels, 30 comments, 3 thumbs-up, versions 4.6.0 to 4.14. A commenter (Oct 27, 2025) traces the match to "/dev/null" in the signature regex. No maintainer reply is visible. The quote is in the original post. |
| 4 | SUPPORTED | The search returns 1027 results. #13278 closed Oct 4, 2024 (17), #32142 Debian 13 closed May 18, 2026 (11), #32320 Arch closed May 4, 2026 with the "Duplicate" label (4). The quote matches the title of #32142. The note now says "reports of the same false positive" and uses the Duplicate label only for #32320. |
| 5 | SUPPORTED | #20317: title as quoted, open, opened Nov 17, 2023, 1 comment, 6 thumbs-up, version 4.6.0, rule 92214 at level 15. It fires when Office creates .lnk files on file open. The only reply proposes a custom rule in `custom_rules.xml`. |
| 6 | SUPPORTED | Discussion #23527: General, May 20, 2024, 4 upvotes, 2 comments plus 1 reply, no accepted answer, hundreds of rule 550 alerts on macOS. The quote is on the page (start of a longer sentence). The July 7, 2025 reply links the alerts to Time Machine inode changes and proposes testing `check_inode="no"`. Small wording point: the reply plans to test this, which is close enough to "suggests". |
| 7 | SUPPORTED | The "false positive" list shows #19792 with the quoted title, closed Sep 24, 2025, 74. The noisy-alerts list shows #39652 "[5.0] Standard rule ... (EventID 5379) fires on normal Windows 11 ...", open, opened Sep 26, 2026. The note says the issue pages themselves were not read. |

## Note-level problems
- None. The front matter is complete (`url: multiple, see claims` is fine for a topic note, and every claim cites its own URL). The role attribution in claim 2 ("Contributor") is shown on the page as a badge. Confidence levels fit the sources. Inferences are labelled and kept apart from the claims. No personal data. The note is in English.

## Recommended fixes
- None.
