---
title: Public descriptions of Wazuh Pharos and Vesper
url: multiple, see claims
publisher: Wazuh Inc. (wazuh.com legal resources, vesper.wazuh.com)
source_type: official-docs
wazuh_version: n/a
accessed: 2026-11-10
question: Does any public page describe what "Wazuh Pharos" (Hub beta, Vulnerability & Threat Intelligence) or "Vesper" (Wazuh support assistant) actually does?
---

## Summary
Of the pages I could read (listed below), the only one that names Pharos is the Wazuh Hub Beta Services Terms (version date
October 8, 2026). It gives the category "Vulnerability & Threat Intelligence" and nothing more: there
is no service-specific section for Pharos. The September 3, 2026 version does not name Pharos, nor does page 1 of the August 19, 2026
version (pages 2–7 were not read). The only page I could read for Vesper is a
maintenance page. Its documentation and the Pharos documentation return HTTP 404 to the fetch
tool. Search engine snippets describe both services in some detail, but I could not open the pages
behind those snippets, so no claim below relies on them.

## Claims
1. The Hub Beta Services Terms (version date October 8, 2026) list Pharos as a beta service in the "Vulnerability & Threat Intelligence" category.
   - Quote: "including, where applicable, Vulnerability & Threat Intelligence - Wazuh Pharos (Beta) (“Pharos”), Identity Risk & Dark Web Monitoring - Wazuh Umbra (Beta) (“Umbra”)"
   - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_October_26.pdf (section 1.1, page 1; linked as current from https://wazuh.com/legal-resources/wazuh-hub-beta-services-terms/)
   - Confidence: high
2. Section 5 ("Service-specific conditions") of the October 2026 terms has subsections only for Umbra (5.1), Argus (5.2), AI-enabled features in general (5.3) and Mobius response functionality (5.4). There is no Pharos subsection, so the terms do not describe what Pharos does.
   - Quote: "5.3. AI-enabled features. A Beta Service may use artificial intelligence or machine-learning functionality"
   - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_October_26.pdf (pages 5–6)
   - Confidence: high
3. The September 3, 2026 version of the terms defines "Beta Service" with only Umbra, Argus and Mobius as examples. It does not name Pharos or Vesper.
   - Quote: "including, where applicable, Wazuh Umbra, Wazuh Argus and Wazuh Mobius, whether access is granted under a Sales Order or otherwise."
   - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_September_2026.pdf (page 1; all 7 pages read)
   - Confidence: high
4. The August 19, 2026 version uses the same Umbra/Argus/Mobius wording in its "Beta Service" definition.
   - Quote: "including, where applicable, Wazuh Umbra, Wazuh Argus and Wazuh Mobius"
   - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_August_2026.pdf (page 1 read only)
   - Confidence: high
5. vesper.wazuh.com serves only a maintenance page and does not say what Vesper is.
   - Quote: "Vesper is undergoing maintenance."
   - Source: https://vesper.wazuh.com/
   - Confidence: high
6. The public Wazuh CTI site does not mention Pharos, Vesper or the Hub.
   - Quote: "Wazuh CTI provides access to a comprehensive database of vulnerabilities."
   - Source: https://cti.wazuh.com/
   - Confidence: high
7. The Hub legal landing pages I read do not mention Pharos or Vesper: the Beta Services Terms page (title "Wazuh Hub Beta Services Terms | Wazuh") and the Account Terms of Use page.
   - Quote: "If a Wazuh Hub service is identified as Beta, the Wazuh Hub Beta Services Terms explain what that means for you."
   - Source: https://wazuh.com/?p=32048 and https://wazuh.com/?p=32046 and https://wazuh.com/legal-resources/wazuh-hub-beta-services-terms/
   - Confidence: high

## Inference
- Inference: the pages I read give Pharos only a name and a category ("Vulnerability & Threat Intelligence"). They do not describe what it does, how it connects to Wazuh, or how it is priced. For Vesper, they give nothing beyond the name and a maintenance notice.
- Inference: Pharos first appears in the October 8, 2026 terms (absent from the September version and from page 1 of the August version), which suggests it is a recent addition. Vesper is not named in any version read, so it may not be a Hub beta service under these terms.
- Inference: search engine snippets (not read, see below) suggest that Pharos is about CVE intelligence over the Wazuh CTI catalog with a read-only connector, and that Vesper is an AI support assistant built on community Q&A that can connect to a deployment. If either is accurate, Vesper could overlap with a "help self-hosted operators" need. This is UNVERIFIED and must not be used as fact.

## Open questions
- UNVERIFIED: what Pharos does (features, connector, pricing). The documentation site returned 404.
- UNVERIFIED: what Vesper does, whether it is an official Wazuh or Wazuh Labs service, and whether it connects to a user's deployment. Search snippets claim this, but the pages behind them could not be read.
- No Wazuh blog post or release note announcing Pharos, Vesper or the Hub was found in three searches.

## Not read
- https://docs.pharos.wazuh.com/ and https://docs.pharos.wazuh.com/get-started/what-is-pharos and https://docs.pharos.wazuh.com/search/corpus (HTTP 404 to the fetch tool; they appear in search results with descriptive snippets)
- https://pharos.wazuh.com/ (HTTP 404)
- https://docs.vesper.wazuh.com/ , /answers/reading-answers , /get-started/first-question (HTTP 404; they appear in search results with descriptive snippets). /get-started/what-is-vesper was reported unreachable earlier and was not retried.
- https://hub.wazuh.com/docs (HTTP 404)
- https://docs.mobius.wazuh.com/ (HTTP 404)
- https://fleet.wazuh.com/wazuh/ (HTTP 404)
- Pages 2–7 of the August 2026 Beta Services Terms PDF were not read.

## Changes after verification
- Main session, after verification: Summary: absence claim scoped to the pages read.
- Main session, after verification: Summary and Inference: the August 2026 terms are described as "page 1 does not name Pharos", since pages 2–7 were not read.
