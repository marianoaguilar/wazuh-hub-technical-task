---
title: Wazuh mailing list threads on reports (PDF, scheduled, monthly, full exports)
url: multiple, see claims
publisher: Wazuh mailing list (Google Groups)
source_type: forum
wazuh_version: not stated in most threads (4.x)
accessed: 2026-11-10
question: What do Wazuh users complain about or ask for help with, outside GitHub?
---

## Summary
Users repeatedly ask how to produce periodic reports (monthly, daily, emailed, PDF) for management or
compliance. Answers point to per-dashboard "Generate report", the OpenSearch reporting plugin, the
`<report>` block in ossec.conf, cron plus reporting CLI, or exporting data through the APIs into
Grafana/Power BI. Known limits mentioned: PDFs are screenshots of one visualization (no table
pagination), and dashboard CSV export is not reliable for large datasets.

## Claims
1. Frequency signal: a group search for "report pdf" (first 30 results) returned 11 reporting threads with listing (last-activity, not first-post) dates from Dec 2024 to Jun 2026 (a live search can change over time), e.g. "Seeking Reporting Solutions for Wazuh (Export, PDF, Pagination, Dashboards)" (2 posts), "Scheduling Reporting Send To Email" (8), "Automatic PDF reports" (6, 2/14/25), "PDF Report pagination?" (4, 5/22/25), "Wazuh Monthly Report" (2), "Wazuh Reporting" (4, 12/16/24); plus 6 more reporting threads from Apr to Oct 2024.
   - Quote: "Seeking Reporting Solutions for Wazuh (Export, PDF, Pagination, Dashboards)" (thread title)
   - Source: https://groups.google.com/g/wazuh/search?q=report%20pdf
   - Confidence: high (titles on the page; the tally is mine)
2. A user wanted custom reports across alerts, inventory, vulnerabilities and FIM, full exports and scheduled email delivery, and found the dashboard too limited (first post Jun 25, 2026); the reply said dashboard CSV export is not reliable for large datasets and suggested the indexer search API, the reporting plugin, Grafana or Power BI.
   - Quote: "Wazuh dashboard seems limited for advanced reporting/export" / "Not reliably via the dashboard CSV export since the UI is meant for small queries to render."
   - Source: https://groups.google.com/g/wazuh/c/-bYUdw0mqAI
   - Confidence: medium
3. A user's PDF report of a large table came out as one page (first post Apr 29, 2025); a reply called it an expected limitation of the OpenSearch reporting plugin, which captures the visualization with a headless browser.
   - Quote: "The report is always only 1 page!? Any idea?"
   - Source: https://groups.google.com/g/wazuh/c/D3DiKF_6Gho
   - Confidence: medium
4. A user asked for a daily emailed summary report (first post Jan 7, 2026); answers combined ossec.conf `<report>`, custom dashboards, opensearch-reporting-cli and cron.
   - Quote: "You can configure <report> from the ossec.conf to get a daily summary report of your alerts."
   - Source: https://groups.google.com/g/wazuh/c/rPn3fO7yZlg
   - Confidence: medium
5. A user asked how to pull monthly logs for a report (Jan 23, 2026); the reply pointed to "Generate Report" in each dashboard with a one-month filter.
   - Quote: "I have implemented wazuh in my organization so i want pull out monthly logs for the report"
   - Source: https://groups.google.com/g/wazuh/c/aMzWy_NAxT8
   - Confidence: low
6. A long product feedback post (Apr 9, 2026) lists PDF export, case management, log correlation, remote agent deployment, ISO 27001 coverage and backup/restore as gaps; the reply says case management is left to external tools and correlation improvements are planned for 5.x.
   - Quote: "Many reports cannot be exported in PDF format, limiting the ease of sharing and compliance reporting."
   - Source: https://groups.google.com/g/wazuh/c/ZBp3kkJicAQ
   - Confidence: low

## Inference
- Inference: reporting is a steady, low-volume but persistent request over two years. Users want
  periodic, readable, complete reports (often for managers or auditors), and the answers are DIY
  assemblies of several tools.

## Open questions
- Whether newer releases (5.x) change reporting; not covered by these threads.

## Changes after verification
- Report result was PASS; no claim was PARTIAL or NOT SUPPORTED.
- Claim 1: applied the optional fix: search-listing dates are last-activity dates, and a live search can change.
- Claim 3: applied the optional fix: "known limitation" changed to "expected limitation", the word used on the page.
- No reply is described as Wazuh staff; the pages do not show any role.
