---
note: research/sources/pain-github-dashboard-reporting-compliance.md
verified: 2026-11-10
result: PASS
---

Re-verification after the fixes listed in the note's "## Changes after verification" section. All seven cited URLs were fetched again in this session.

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | #4091 page: open, opened Oct 16, 2019. Labels: level/task, reporter/operations, team/threatintel, type/enhancement. No assignee or milestone. 32 thumbs-up on the original post. 24 visible comments plus "43 remaining items". Last visible comment is dated Feb 9, 2026. An Oct 4, 2025 comment says the existing content is iso_27001-2013. The quote is in the "Request" section. |
| 2 | SUPPORTED | The thumbs-up-sorted search shows #19346 first and #4091 "Feature request: ISO 27001 compliance integration" second. |
| 3 | SUPPORTED | #1492 page: open, opened May 29, 2019. Labels: component/reports, request/operational, type/enhancement. 11 comments, no thumbs-up count shown. May 26, 2021 comment: "was not prioritized yet". Removed from its milestone on May 5, 2022 and unassigned on May 23, 2022. The quote is in the description. |
| 4 | SUPPORTED | The dashboard-plugins thumbs-up-sorted list (25 items) shows #4068 at position 16, open, opened Apr 20, 2022. The quote is the issue title. Confidence `medium` fits. |
| 5 | SUPPORTED | #1578 page: open, opened Jul 8, 2019. No comments (only a label event). 4 thumbs-up. The quote is present. |
| 6 | SUPPORTED | #33328 page: open, opened Dec 1, 2025. No comments, no reactions. Version v4.14.1. It asks for a "Send to Case Management" button for one or more alerts. The quote is present. |
| 7 | SUPPORTED | #24290 page: open, opened Jun 24, 2024. 28 visible comments plus 11 hidden items, so "at least 28" is correct. The quote is in the original post. Comments mention SOC2 audit evidence (Feb 14, 2025) and a formal audit being affected (Oct 3, 2025). |

## Note-level problems
- None.
- Front matter is complete (`url: multiple, see claims` is valid; every claim cites its own URL).
- Confidence levels fit the sources. Inferences are labelled `Inference:`. No role attributions. No personal data in the note. The note is in English.
- The previous problem is fixed: the #7793 details are now marked `UNVERIFIED:`, flagged as not to be used, and listed under "Not read".
- Minor observation, not blocking: the front matter field `wazuh_version: 3.x to 4.14.1` gives a lower bound (3.x) that no claim states. Only 4.14.1 (#33328) appears on a cited page.

## Recommended fixes
- None. Optional: change `wazuh_version` to the versions the cited pages state (for example "4.14.1 for #33328; other issues do not state a version").
