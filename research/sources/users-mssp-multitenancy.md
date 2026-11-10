---
title: MSSPs and multi-tenant use of Wazuh (dashboard tenants, cross-cluster search, partner program)
url: multiple, see claims
publisher: Wazuh Inc.; Wazuh Google group
source_type: other
wazuh_version: "current" docs (newest release listed 4.14.10); blog header says 4.8.2 while its setup section says 4.14.1
accessed: 2026-11-10
question: Who uses Wazuh, and for what? (MSSPs and multi-tenant use: documented or not, and how)
---

## Summary
The Wazuh documentation has a "multi-tenancy" page, but its tenants only separate saved
dashboard objects (index patterns, visualisations, dashboards); it does not describe isolating
customers' security data and does not mention MSSPs. For MSSPs, Wazuh's blog and an answer in
the community group (affiliation not stated) point to a cluster-per-customer design joined by
cross-cluster search (CCS). The iSecNG MSSP case study describes dedicated instances per client.
The partner page lists a "Centralized Console for Multi-tenancy" as a partner benefit, described
only in one line: "Multi-tenant WUI presents data and provides control of different environments."

## Claims
1. Dashboard tenants are containers for saved objects (index patterns, visualisations, dashboards), with Global, Private and Custom tenants.
   - Quote: "Tenants in the Wazuh dashboard are containments for saving index patterns, visualizations, dashboards, and other objects."
   - Source: https://documentation.wazuh.com/current/user-manual/wazuh-dashboard/multi-tenancy.html
   - Confidence: high

2. The multi-tenancy docs page does not mention MSSPs or isolation of indexed security data; isolation described is about saved objects and role access to tenants.
   - Quote: the Global tenant is "shared between every Wazuh dashboard user."
   - Source: https://documentation.wazuh.com/current/user-manual/wazuh-dashboard/multi-tenancy.html
   - Confidence: medium (absence of evidence, one reading)

3. A Wazuh blog post shows CCS for a managed SOC provider with two customers: each customer has its own cluster (server and indexer) where data stays, and a central indexer+dashboard queries them.
   - Quote: "allows alerts from remote Wazuh clusters to be queried and viewed at a centralized location" / "Customer logs are retained within the customer environment."
   - Source: https://wazuh.com/blog/managing-multiple-wazuh-clusters-with-cross-cluster-search/
   - Confidence: high (official blog)

4. The same post frames CCS as a way for MSSPs to onboard customers while keeping data separate.
   - Quote: "Each customer's log is kept separate, and access is tightly controlled"
   - Source: https://wazuh.com/blog/managing-multiple-wazuh-clusters-with-cross-cluster-search/
   - Confidence: high

5. In the Wazuh Google group, a user asks how an MSSP can separate client environments; the answer recommends CCS with agents connecting to a per-customer manager, which implies at least one VM per client (all-in-one) plus one for the MSSP. A follow-up question about ports is left unanswered.
   - Quote: "You can achieve this with cross-cluster-search." / "Agents would register and connect to each manager (cluster) corresponding to their customer"
   - Source: https://groups.google.com/g/wazuh/c/-141kWNG2Yc
   - Confidence: medium (forum, answer links to the official blog post)

6. The Wazuh partners page lists, among plan features, a cloud environment for up to 100 agents and a centralised multi-tenancy console.
   - Quote: "Wazuh Platinum Cloud Environment - Supports up to 100 Agents" / "Centralized Console for Multi-tenancy"
   - Source: https://wazuh.com/partners/
   - Confidence: medium (feature table text was not clearly mapped to Gold/Platinum tiers)

7. The iSecNG case study (an MSSP) says clients receive dedicated Wazuh instances, and that iSecNG operates multiple clusters tailored to different client needs. The FirmGuardian case study (also an MSSP) mentions data aggregation and analysis for multiple clients but gives no architecture details.
   - Quote: "Clients receive dedicated Wazuh instances to ensure data separation and regulatory compliance." / "operate a fully scalable environment with multiple clusters tailored to different client needs"
   - Source: https://wazuh.com/resources/case-studies/isecng-strengthening-cybersecurity-with-wazuh/
   - Quote (FirmGuardian): "This has been invaluable for us as an MSSP, as we deal with large-scale data aggregation and analysis for multiple clients."
   - Source: https://wazuh.com/resources/case-studies/firmguardian-customization-meets-compliance/
   - Confidence: medium

8. A virtual SOC provider (Guayoyo) became a Wazuh Partner to offer more competitive rates.
   - Quote: "they decided to become Wazuh Partners, allowing them to offer more competitive rates"
   - Source: https://wazuh.com/resources/case-studies/guayoyo-virtual-soc-triumph/
   - Confidence: medium

## Inference
- Inference: Wazuh does not document a native, data-isolating multi-tenant mode in the open source product; MSSPs build multi-tenancy themselves from one cluster per customer plus CCS, which costs at least one deployment per client to run and upgrade.
- Inference: iSecNG's dedicated instances per client suggest a cluster-per-client model rather than one shared multi-tenant deployment; the page does not draw this contrast itself.
- Inference: the "Centralized Console for Multi-tenancy" on the partners page, described there only as "Multi-tenant WUI presents data and provides control of different environments.", suggests the vendor offers something for partners; which product or service sits behind it (e.g. a managed CCS setup) is not explained on the pages read.

## Open questions
- What exactly the partner "Centralized Console for Multi-tenancy" is.
- Whether RBAC / agent groups in the Wazuh server API are documented as an MSSP option (not checked).
- UNVERIFIED: search snippets reported a GitHub issue (wazuh/wazuh-kubernetes #357) saying dashboard multitenancy does not work with SSO, and a Google group thread where a reply describes an MSSP environment in the partner program (the poster's role is not checked); neither page was fetched, so no claims are made.

## Not read
- https://www.github.com/wazuh/wazuh-kubernetes/issues/357 — seen in search results only, not fetched.
- https://groups.google.com/g/wazuh/c/oWyIXfF92WI — seen in search results only, not fetched.
- https://groups.google.com/g/wazuh/c/vcDA7quhTqc — seen in search results only, not fetched.
- https://wazuh.com/docs/legal-resources/Wazuh_Partner_Program_Terms_October_2026.pdf — not fetched.
- https://wazuh.com/mssp/ — HTTP 404.
- https://msspalert.com/news/wazuh-offers-free-open-source-security-platform — HTTP 403.

## Changes after verification
- Summary: replaced "a Wazuh-side answer" with "an answer in the community group (affiliation not stated)"; the re-fetched thread shows no role or badge for the replier.
- Summary and Inference 2: replaced "without further detail" / "not described" with the partner page's one-line description, quoted (re-fetched 2026-11-10); kept the open question on what product sits behind it.
- Claim 7: added the FirmGuardian case-study URL (fetched 2026-11-10) and quote, and said it gives no architecture details; added iSecNG's "multiple clusters" quote; moved "rather than a shared multi-tenant platform" to an `Inference:` line.
- Open questions: in the UNVERIFIED search-snippet item, replaced "a Wazuh representative" with "a reply" (role not shown on any page fetched), following the round's rule on poster roles.
- Front matter: `source_type` changed from `official-docs` to `other`, since the note mixes official docs, official blog, vendor marketing/case studies and a forum thread (the template has no `mixed` value).
