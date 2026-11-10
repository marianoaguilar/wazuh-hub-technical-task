---
title: GitHub issues on multi-tenant / MSSP operation and agent-group scoping
url: multiple, see claims
publisher: GitHub (wazuh organisation)
source_type: github
wazuh_version: 4.3 to 4.8.1 (varies per issue, see claims)
accessed: 2026-11-10
question: What problems do Wazuh users report on GitHub?
---

## Summary
Users running one Wazuh instance for several clients or environments report that alerts and the
4.8+ vulnerability state indices do not carry agent-group data, so they cannot filter or isolate
per tenant; that RBAC multitenancy works only for local users, not SSO; and that rules are global
with no per-tenant rulesets. Requests date from 2019 to 2025 and most are still open.

## Claims
1. "Allow filter by agent.group in Wazuh Modules/Security events" (#14225): open, opened Jul 12, 2022, labels reporter/operations, type/enhancement, 20 comments, 13 thumbs-up on the original post; supporting comments through Jan 2026; no assignee or milestone shown. One commenter (May 2024) says they cannot report on one client without leaking other clients' information; another commenter calls the feature critical for MSSPs and MSPs; a comment describes the workaround of one label per agent group.
   - Quote: "We need to consider to add this feature out-of-the-box in Wazuh to properly set the Agent's group name into the alerts." / "critical for MSSPs and MSPs"
   - Source: https://github.com/wazuh/wazuh/issues/14225
   - Confidence: high

2. "Vulnerability dashboard not following document level security model" (#24118): open, opened Jun 17, 2024, labels level/task, reporter/community, type/bug, 16 comments, 2 thumbs-up; version 4.8.0. Vulnerability documents lack agent group labels, so group-restricted users see all agents. One commenter (Oct 2024) with several clients gives blocking the index or delaying the upgrade as two possible options. A user comment (Feb 2025) reports that it was removed from the 5.0.0 release project; the page shows no timeline event for this and its metadata shows no projects.
   - Quote: "New vulnerability-detection does not honor the RBAC definitions."
   - Source: https://github.com/wazuh/wazuh/issues/24118
   - Confidence: high

3. A related open request (#32193, opened Sep 26, 2025) asks for agent.group and agent.label fields in wazuh-states-* indices; it appears in the top 25 `wazuh/wazuh` issues by thumbs-up.
   - Quote: "Feature Request: Add agent.group and agent.label fields to wazuh-states-* indices"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+sort%3Areactions-%2B1-desc
   - Confidence: medium (search list only)

4. "Wazuh RBAC - Not working with backend roles - Unable to use Wazuh Multitenancy using SSO" (#17384): open, opened Jun 2, 2023, no labels, no comments, no reactions shown; version 4.4.1.
   - Quote: "Multitenancy and Agents isolation only works with local users, not with SSO"
   - Source: https://github.com/wazuh/wazuh/issues/17384
   - Confidence: medium (single report)

5. "Feature request: Tenant based Rules" (#25370): open, opened Aug 23, 2024, no labels, no comments, no reactions shown; version 4.8.1. It asks for per-customer rules and decoders for MSPs.
   - Quote: "Currently, Wazuh applies a universal ruleset across all managed endpoints."
   - Source: https://github.com/wazuh/wazuh/issues/25370
   - Confidence: medium (single report)

6. "It's not possible to use labels in custom rules" (#3130): opened Apr 17, 2019, closed as not planned Jun 5, 2023, 17 comments, 18 thumbs-up. Users wanted different alert levels per environment (dev, prod, test).
   - Quote: "it's not possible to use labels inside rules."
   - Source: https://github.com/wazuh/wazuh/issues/3130
   - Confidence: high

7. A search for multi-tenancy/MSSP terms returns 298 issues, including "Custom Agent Creation Limits for Multi-Tenancy Groups" (#21851, open, opened Feb 9, 2024) and SSO/SAML permission problems (#16366, position 20 on the list with 16 comments shown, open, opened Mar 13, 2023).
   - Quote: "Subject: New Feature Request - Custom Agent Creation Limits for Multi-Tenancy Groups"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+multi-tenancy+OR+multitenancy+OR+MSSP+sort%3Areactions-%2B1-desc
   - Confidence: medium (search list only)

## Inference
- Inference: multi-tenant operation is done through workarounds (labels, document-level security
  queries that never match, local users). This fits a SaaS/MSSP layer that maps agents to tenants
  and enforces isolation on top of the indexer data.
- Inference: reaction counts are modest (2-18), but the users affected are MSSPs, each with many
  end customers.

## Open questions
- Whether 5.0 adds group fields to state indices (requested in #32193; not verified).

## Not read
- https://github.com/wazuh/wazuh/issues/32193, https://github.com/wazuh/wazuh/issues/21851, https://github.com/wazuh/wazuh/issues/16366: seen only in search lists.

## Changes after verification
- Claim 1: "MSSP commenters say..." changed to one commenter describing data leakage and another calling the feature critical for MSSPs/MSPs; added quote (re-fetched 2026-11-10; a count of 1 commenter, per the page).
- Claim 2 (optional fix): removal from the 5.0.0 project now attributed to a user comment, with no timeline event on the page.
- Claim 5 (optional fix): "MSSPs" changed to "MSPs" to match the page.
- Claim 7: "16 on the list" clarified as "position 20, 16 comments shown" (re-fetched the search list; 16 is the comment count, the position is 20).
- Main session, after second verification: Claim 2: "organisations ... say they must" changed to one commenter giving two options, as on the page.
