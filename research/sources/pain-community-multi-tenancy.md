---
title: Wazuh mailing list threads on multi-tenancy and serving several customers (MSSP use)
url: multiple, see claims
publisher: Wazuh mailing list (Google Groups)
source_type: forum
wazuh_version: 4.12 to 4.13 and 5.x (per thread, see claims)
accessed: 2026-11-10
question: What do Wazuh users complain about or ask for help with, outside GitHub?
---

## Summary
People who want one Wazuh deployment for several customers or teams keep asking how to isolate data.
The answers are a mix of agent groups and labels, indexer roles with document-level security (DLS),
API RBAC, and cross-cluster search with separate clusters. Threads show gaps: dashboard "tenants" do
not isolate data, and in 4.12 vulnerability state data could not be filtered by group label.

## Claims
1. Frequency signal: a group search for "multi-tenant" returned 30 threads on the first page with listing (last-activity) dates from Mar 2023 to Oct 2026; 11 of them have listing dates from Mar 2025 to Oct 2026 (the two newest, "Oct 11" and "Apr 8", show no year; 2026 is inferred from the date format). The order is Google's ranking, so this is a first-page sample, not a total. Examples: "Wazuh Multi Tenancy inquiry" (9 posts), "multi tenant internal user not showing vulnerability detection data" (7), "Multi-tenancy" (7), "True multitenancy infrastracture" (6), "Two or more company to monitor" (6), "Wazuh 5 Security Analytics – Tenant separation of findings with separated event data streams" (6).
   - Quote: "Wazuh architecture for multiple customers" (thread title, 8/13/24, 5 posts)
   - Source: https://groups.google.com/g/wazuh/search?q=multi-tenant
   - Confidence: high (titles and counts on the page; tallies are mine)
2. A reply explains that dashboard tenants separate saved objects only, and data isolation needs DLS on indexer roles over the shared alerts index (first post Mar 16, 2026).
   - Quote: "Tenants isolate dashboard objects, and does not isolate data."
   - Source: https://groups.google.com/g/wazuh/c/_gjAFm6i5fI
   - Confidence: medium
3. A respondent describes two approaches: a separate indexer cluster per client with cross-cluster search, or agent groups with labels plus RBAC; a later user on 4.13.0 reports Discover was restricted but Overview and Vulnerabilities still showed all agents (first post May 8, 2025).
   - Quote: "give users access only to their own agents"
   - Source: https://groups.google.com/g/wazuh/c/isfTPrB-Nnk
   - Confidence: medium
4. On 4.12, a tenant user restricted by DLS on agent.labels.group saw alerts but an empty Vulnerability Detection view; a reply said this filtering was not available in that version, and the thread ended unresolved in Nov 2025.
   - Quote: "the vulnerability filtering feature with DLS by agent.labels.group is not available in the current Wazuh version."
   - Source: https://groups.google.com/g/wazuh/c/9HPuBf_Oxyc
   - Confidence: medium
5. A user building a multi-tenant Docker Swarm cross-cluster setup had to rebuild the indexer image to expose port 9300 (first post Mar 11, 2025).
   - Quote: "Fixed it by rebuilding the docker image of the wazuh indexer and adding the expose 9300 in the docker file"
   - Source: https://groups.google.com/g/wazuh/c/eoIYpXEoho4
   - Confidence: low

## Inference
- Inference: multi-customer operation (MSSPs, service providers, or one company with several units) is a
  steady topic over three years, and isolation is assembled by hand from several mechanisms with
  known gaps. This points to a need for a managed multi-tenant layer.

## Open questions
- These threads do not show how many MSSPs run Wazuh; only that the question recurs.
- Behaviour in 4.14 and 5.x for vulnerability-state DLS is not covered here.

## Changes after verification
- Report result was PASS; no claim was PARTIAL or NOT SUPPORTED.
- Claim 1: applied the optional fix: listing dates are last-activity dates, the year of the two newest results is inferred, and the result order is Google's ranking (first-page sample, not a total).
- No poster in claims 2-5 is described as Wazuh staff; the pages do not show any role, so none was added.
