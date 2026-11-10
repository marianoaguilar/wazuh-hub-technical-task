---
note: research/sources/pain-github-upgrades-storage.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Search page re-fetched: 361 results; #24074 "Upgrade to Wazuh 4.8 - Missing indice (wazuh-states-vulnerabilities)" is first with 126 comments. |
| 2 | SUPPORTED | #24074: opened Jun 12, 2024, closed as completed Jul 19, 2024, label reporter/community, version 4.8, 27 visible comments plus "99 remaining items", one thumbs-up on the original post. Quote is in the original post. All six causes appear in comments; nine comments come after closure, several still reporting the problem. |
| 3 | SUPPORTED | #32044: open, Sep 19, 2025, labels include reporter/community, request/operational, type/bug; 25 visible plus "60 remaining items"; no reactions on the original post. Both quotes appear. Fixes that worked: removing `noexec` from `/tmp` and re-entering certificate paths and keystore credentials. The "[1000]/[1000] maximum shards open" message is mentioned, deleting old indices was suggested, and no one confirms it fixed the problem. |
| 4 | SUPPORTED | #33038: title, open, Nov 6, 2025, labels level/task, reporter/community, request/operational, type/bug; 25 visible plus "20 remaining items"; no reactions on the original post (the only thumbs-up is on the Apr 29, 2026 comment). Quote appears. Apr 29, 2026 comment reports 4.14.4 with "~8556 connected agents" ("about 8,500" is a fair rounding). No root cause identified. |
| 5 | SUPPORTED | Search list shows #27699 (41, closed Feb 5, 2025), #32820 (37, closed Oct 31, 2025), #27563 (32, closed Jan 15, 2025) with these titles. `medium` confidence and its explanation fit. |
| 6 | SUPPORTED | #24243: title, opened Jun 21, 2024, closed Aug 25, 2024, reporter/community, 26 comments, 9 thumbs-up, quote in the original post, later reports on 4.14.0 / 4.14.1 / fresh 4.14. Dec 10, 2024 reply ("deleting any sst file will corrupt the database") carries the "Contributor" badge on the page. |
| 7 | SUPPORTED | #30476: title, open, Jun 18, 2025, versions 4.11.1 / 4.12.0 / 4.13.1, about 20 comments, no reactions shown. Quote appears; reporter's listing shows "total 212G" and "We had only 246 agents". Exactly one other user reports terabytes ("2.6T" for the vulnerabilities queue). |

## Note-level problems
- None. Front matter is complete (`url: multiple, see claims` with a URL on every claim). Confidence levels fit the sources (GitHub issue pages for issue facts, `medium` for the search-list claim). Inferences are labelled and kept apart from claims; "possibly shard limits" now matches claim 3. Role attribution ("Contributor") matches the badge on the page. No personal data (no usernames in the note). English only.

## Recommended fixes
- None.
