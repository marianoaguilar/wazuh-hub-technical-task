---
note: research/sources/pain-github-multi-tenancy.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Re-fetched. Title, open, Jul 12, 2022, labels reporter/operations and type/enhancement, 20 comments, 13 thumbs-up, no assignee or milestone, latest comment Jan 5, 2026. One commenter (May 18, 2024) says they cannot report on one client without leaking other clients' information. A Feb 24, 2023 comment contains "critical for MSSPs and MSPs" verbatim. An Apr 2023 comment describes one label per group. The first quote appears verbatim in the body. The previous fix is correct. |
| 2 | PARTIAL | Re-fetched. Title, open, Jun 17, 2024, labels level/task, reporter/community and type/bug, 16 comments, 2 thumbs-up, version 4.8.0, quote verbatim, and the body says the documents "do not include agent group labels". The Feb 19, 2025 user comment about removal from the XDR+SIEM/Release 5.0.0 project exists, the timeline has no project event and the metadata says "No projects". All correct. Problem: "Organisations with several clients say they must block the index or delay upgrading" is broader than the page. Only one commenter (Oct 1, 2024) lists these two things, and as options, not as something they must do. Other commenters raise multi-tenant privacy concerns but do not say this. My previous report missed this. |
| 3 | SUPPORTED | Re-fetched. #32193 is at position 25 (the last entry) on page 1 of the thumbs-up sort. It is open, opened Sep 26, 2025, and the title matches the quote. |
| 4 | SUPPORTED | Re-fetched. Title, open, Jun 2, 2023, no labels, no comments or reactions shown, version 4.4.1, and the quote appears verbatim in the body. |
| 5 | SUPPORTED | Re-fetched. Title, open, Aug 23, 2024, no labels, no comments or reactions shown, version 4.8.1, and the quote appears verbatim. It asks for rules and decoders "per customer or tenant" and uses "managed service providers (MSPs)", which matches the note. |
| 6 | SUPPORTED | Re-fetched. Title, opened Apr 17, 2019, closed as not planned Jun 5, 2023, 17 comments, 18 thumbs-up, and the quote appears in the body ("we noticed that it's not possible to use labels inside rules."). A Sep 2020 comment asks to adjust the alert level by environment, and a Mar 2025 comment names dev, prod and test. Minor: the 2025 comment is about scoping rules by group, not alert levels, so the "(dev, prod, test)" detail mixes two comments. This is acceptable. |
| 7 | SUPPORTED | Re-fetched. The search returns 298 results. #21851 is at position 7: open, opened Feb 9, 2024, and the title matches the quote. #16366 "SAML Authentication Permission Issues (Authentik)" is at position 20: open, opened Mar 13, 2023, 16 comments. The previous fix is correct. |

## Note-level problems
- None. The front matter is complete (`url: multiple, see claims` is allowed, and every claim cites its own URL). The confidence levels fit the sources: `high` only for issues with many comments or reactions, `medium` for single reports and search lists. The note makes no claims about roles (staff or maintainer). Inferences are labelled, and pages seen only in search lists are listed under "Not read". There is no personal data and the note is in English. The "Changes after verification" section is accurate.

## Recommended fixes
- Claim 2: change "Organisations with several clients say they must block the index or delay upgrading" to "One commenter serving several clients (Oct 2024) lists two options: block access to the vulnerability index or not upgrade past 4.8.0. Other commenters raise multi-tenant privacy concerns."
- Optional, claim 6: say that one 2020 comment asks for alert levels per environment, and that a 2025 comment mentions dev, prod and test for rule scoping by group.
