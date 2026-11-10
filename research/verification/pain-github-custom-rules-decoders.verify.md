---
note: research/sources/pain-github-custom-rules-decoders.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | #21706 page: title "MSSQLSERVER- data parsing", open, opened Feb 2, 2024, label reporter/community, 26 comments, no reactions shown, version 4.7.0-1 in the issue body. The quote is in the original post, which asks for username, database and client IP. |
| 2 | SUPPORTED | Re-fetched. The commenter has the "Member" badge on the page. On Mar 7 this Member proposed a PCRE2 regex decoder with wazuh-logtest output, and posted a revised version on Mar 18. The reporter replied on Mar 8 and Mar 19 that the event uses the windows_eventchannel decoder. Both quotes are on the page, from the same Member: Mar 25 "The decoders that are from `windows_eventchannel` cannot be modified, this is because the decoder is part of the code." and Mar 28 "The version that will allow this customization will be the 5.0." |
| 3 | SUPPORTED | The search page shows 1,347 results. The top results include items not about rules or decoders (#5841, #33038, #16504, #9558), which matches the note's caveat. #7056 is closed, Feb 10, 2021, 24 comments; #5448 is closed, Jul 31, 2020, 20 comments; #23516 is open, opened May 18, 2024, 20 comments. The quote is a listed title. |
| 4 | SUPPORTED | Discussions list (sort: top): #31088 "Working with cdb lists for each agent", Q&A, Jul 24, 2025, 6 votes, 2 comments, answered. #20696 "Numerical comparison in Wazuh Rules", Q&A, Dec 11, 2023, 4 votes, 2 comments, unanswered. |
| 5 | SUPPORTED | #3130 "It's not possible to use labels in custom rules": opened Apr 17, 2019, closed as not planned on Jun 5, 2023, 17 comments, 18 thumbs-up on the original post. The quote is in the body. A Mar 2025 comment says "hostname or CDB hostname list criteria is the closest we can get." |
| 6 | SUPPORTED | #20317 is about Sysmon rule 92214 false positives, has 6 thumbs-up, and the quote is in the original post. Its single reply (Apr 19, 2024) gives one workaround: a custom rule in custom_rules.xml. The note's wording, "the only workaround offered in the thread", matches this. |

## Note-level problems
- None. The front matter is complete (`url: multiple, see claims` is allowed, and every claim cites its own URL). The "Member" role is shown as a badge on the #21706 page. The confidence levels fit the sources. Inferences are labelled. The note contains no personal data and is in English.

## Recommended fixes
- None.
