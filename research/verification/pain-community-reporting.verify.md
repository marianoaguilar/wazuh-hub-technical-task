---
note: research/sources/pain-community-reporting.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Re-fetched the search page. It shows "1-30 of many", and all six named titles match with their post counts and dates: Seeking Reporting Solutions (2, Jun 26), Scheduling Reporting Send To Email (8), Automatic PDF reports (6, 2/14/25), PDF Report pagination? (4, 5/22/25), Wazuh Monthly Report (2), Wazuh Reporting (4, 12/16/24). I reproduced the tally of 11 reporting threads from 12/16/24 to Jun 26, plus 6 from 4/18/24 to 10/15/24 (Problems with report, Export Scheduled Report Definition CSVs, OpenSearch reports send email, Error generating reports, Custom reports, Report format). The note now says the dates are last-activity dates and that a live search can change. Which threads count as "reporting" is still a judgment call, and the note labels the tally as the researcher's own. |
| 2 | SUPPORTED | The first post is dated Jun 25, 2026. Both quotes appear verbatim. The user asks for reports on alerts, inventory, vulnerabilities and FIM, full exports and scheduled email delivery. The reply suggests the indexer search API (PIT/search_after), the reporting plugin, Grafana and Power BI. |
| 3 | SUPPORTED | The first post is dated Apr 29, 2025, and the quote appears verbatim. The May 22, 2025 reply says "This is an expected limitation of the reporting feature when using visualizations". It also says the feature uses a plugin from OpenSearch developers that "uses a headless browser that takes a screenshot of the visualization". The note now uses "expected", the word on the page. |
| 4 | SUPPORTED | The first post is dated Jan 7, 2026, and the user asks for a daily emailed report. The quote appears verbatim in the reply. The reply also mentions custom dashboards sent as PDF with opensearch-reporting-cli, and a "cornjob" (sic, cron). |
| 5 | SUPPORTED | The first post is dated Jan 23, 2026, and the quote appears verbatim. The reply says "Filter for one month of alerts or data, and click on Generate Report to generate a PDF report." |
| 6 | SUPPORTED | The first post is dated Apr 9, 2026, and the quote appears verbatim. All six listed gaps are in the post (it lists others too). The reply sends case management to "external tools or ticketing systems" and says "We are working on improving it in the upcoming 5.x versions" about correlation. |

## Note-level problems
- None. The front matter is complete (`url: multiple, see claims` is valid, and each claim cites its own URL). Each confidence level is one of high / medium / low and fits its source. Claim 1 is `high` only for the titles shown on the page, and the tally is labeled as the researcher's own. Single-thread claims are `medium` or `low`. The inference is labeled. The note is in English. It contains no forum user names, emails or companies. It does not describe anyone as Wazuh staff, which is correct: none of the fetched pages shows a role label or affiliation for any poster.

## Recommended fixes
- None. When this material is used in PHASE2.md, do not describe the repliers as Wazuh staff, because the pages do not say so.
