---
title: GitHub issues on dashboard usability, reporting, compliance and investigation workflow
url: multiple, see claims
publisher: GitHub (wazuh organisation)
source_type: github
wazuh_version: 3.x to 4.14.1 (varies per issue, see claims)
accessed: 2026-11-10
question: What problems do Wazuh users report on GitHub?
---

## Summary
Long-open requests cover ISO 27001 compliance content (open since 2019, +1 comments into 2026),
scheduled PDF reports sent by email (open since 2019, not prioritised), editing built-in dashboard
visualisations, and sending alerts from the dashboard to a case management system. These are
older, slow-moving requests rather than recent bug reports.

## Claims
1. "Feature request: ISO 27001 compliance integration" (#4091): open, opened Oct 16, 2019, labels level/task, reporter/operations, team/threatintel, type/enhancement; 32 thumbs-up on the original post; 24 comments visible plus 43 hidden items; no assignee or milestone; "+1" comments continue to Feb 9, 2026. A 2025 comment says existing ISO content uses the 2013 version.
   - Quote: "Consider including this new feature in the product roadmap to be available in upcoming releases."
   - Source: https://github.com/wazuh/wazuh/issues/4091
   - Confidence: high

2. #4091 is the second result when `wazuh/wazuh` issues are sorted by thumbs-up, after #19346.
   - Quote: "Feature request: ISO 27001 compliance integration"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+sort%3Areactions-%2B1-desc
   - Confidence: high

3. "Automatic reports in the UI" (#1492, wazuh-dashboard-plugins): open, opened May 29, 2019, labels component/reports, request/operational, type/enhancement, 11 comments, thumbs-up not shown. In May 2021 a contributor said it was not prioritised; in May 2022 it was removed from its milestone and unassigned.
   - Quote: "Ability to schedule automatic PDF reports and send them over email."
   - Source: https://github.com/wazuh/wazuh-dashboard-plugins/issues/1492
   - Confidence: high

4. "Add PDF report feature to Vulnerabilities Inventory rework" (#4068, wazuh-dashboard-plugins) is open since Apr 20, 2022 and appears among the top 25 dashboard-plugin issues by thumbs-up.
   - Quote: "Add PDF report feature to Vulnerabilities Inventory rework"
   - Source: https://github.com/wazuh/wazuh-dashboard-plugins/issues?q=is%3Aissue+sort%3Areactions-%2B1-desc
   - Confidence: medium (search list only)

5. "Add the capability to add/edit Wazuh dashboards visualizations" (#1578, wazuh-dashboard-plugins): open, opened Jul 8, 2019, no comments, 4 thumbs-up.
   - Quote: "It would be really interesting to edit a visualization or add new visualizations to our predefined dashboards"
   - Source: https://github.com/wazuh/wazuh-dashboard-plugins/issues/1578
   - Confidence: medium

6. A user asks for a dashboard button to escalate one or more alerts to a case management system (#33328): open, opened Dec 1, 2025, no comments, no reactions shown, version 4.14.1.
   - Quote: "Analysts currently have no way to manually send a specific alert—or a group of selected alerts—from the Wazuh Dashboard"
   - Source: https://github.com/wazuh/wazuh/issues/33328
   - Confidence: low (single request, no engagement)

7. Users of the new vulnerability detector say missing alert events hurt audits and compliance evidence (#24290, open since Jun 24, 2024, at least 28 comments).
   - Quote: "I hope to see vulnerability events back in the alert index."
   - Source: https://github.com/wazuh/wazuh/issues/24290
   - Confidence: medium

## Inference
- Inference: compliance reporting (ISO 27001:2022 mapping, scheduled reports, audit evidence) is a
  durable demand with high reactions but slow progress in the core product, which makes it a
  candidate for an add-on service.
- Inference: investigation/triage workflow (case management, notes on alerts) shows only weak
  GitHub signals; other sources are needed before relying on it.

## Open questions
- Whether reporting was reworked in recent dashboard versions. UNVERIFIED: a spike about a reporting revamp (#7793 in wazuh-dashboard-plugins) was seen on a search list whose URL was not recorded; its title, state and dates are not checked and must not be used.

## Not read
- https://github.com/wazuh/wazuh-dashboard-plugins/issues/4068 and https://github.com/wazuh/wazuh-dashboard-plugins/issues/7793: seen only in search lists.

## Changes after verification
- Open questions: #7793 details (title, close date) marked UNVERIFIED and not to be used, because the search list where it was seen has no recorded URL (report: note-level problem).
- Claims 1-7: no changes (all SUPPORTED).
