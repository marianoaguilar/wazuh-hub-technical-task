---
note: research/sources/design-ranking-wazuh-kev-epss-support.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Vulnerability detection index page: Wazuh CTI vulnerabilities repository or an offline copy; the page does not mention EPSS, KEV or prioritization. |
| 2 | SUPPORTED | Current "How it works": security databases MSU, NVD, OSV, CISA; neither EPSS nor KEV appears. |
| 3 | SUPPORTED | 5.0-beta "How it works": same list including CISA; no EPSS, KEV or prioritization wording. |
| 4 | SUPPORTED | CTI CVE page shows filters Min CVSS Score, Min CVSS Severity, Date, Order by, quick filters; no EPSS, KEV or exploited field. "Comprehensive database of vulnerabilities" appears. In this session the page loaded, so the "did not fully load" remark may be out of date. Confidence `low` is conservative. |
| 5 | PARTIAL | Title, open state, 2023-01-11, no linked branches or PRs, the 2023 reply about the "upcoming refactor" and the 2026 requests for EPSS/KEV in 5.x are confirmed, as is the absence of an official reply. "A team member" is a role attribution: the page shows an assignee and a reply, but no label or badge was seen that states team or maintainer status. |
| 6 | SUPPORTED | #36000: closed as completed 2026-05-12, project XDR+SIEM/Release 5.0.0, PR #36030 "Added new CVE5 fields", KEV and EPSS `metrics.other` tasks. |
| 7 | SUPPORTED | Page does not say where KEV/EPSS are exposed. Section 6 requires the scanner to "correctly deserialize and expose the associated content payload", which does not name a destination; the quoted sentence in the note was not seen verbatim. |
| 8 | PARTIAL | Search counts match: EPSS 4 results (#38399, #36000, #31571, #15872), KEV 7 results (#40532, #40314, #39952, #39354, #36000, #24000, #15872). But #31571 is a pull request, not an issue, so "4 issues" is inaccurate. The note's quote is a title of #36000, not a search-page quote. |

## Note-level problems
- Claim 5: role attribution "team member" is not shown by a label on the page.
- Claim 8: "4 issues" includes one pull request.
- Front matter complete. Inferences labelled. No personal data (usernames not copied). English.

## Recommended fixes
- Claim 5: write "a reply from the issue assignee" instead of "a team member", or cite a page that shows the role.
- Claim 8: say "4 results (3 issues and 1 pull request)".
