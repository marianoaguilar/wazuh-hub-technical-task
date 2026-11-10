---
title: Use cases and Regulatory compliance (Wazuh documentation)
url: multiple, see claims
publisher: Wazuh Inc.
source_type: official-docs
wazuh_version: "current" docs (newest release listed in the docs navigation: 4.14.10; pages do not state a version)
accessed: 2026-11-10
question: Who uses Wazuh, and for what? (main use cases)
---

## Summary
The Wazuh documentation groups its main use cases into four areas: endpoint security, threat
intelligence, security operations and cloud security, with twelve use cases in total. The
compliance section says the default ruleset maps to PCI DSS, HIPAA, NIST 800-53, TSC and GDPR,
and warns that the mappings are indicative and do not by themselves guarantee compliance. The
wazuh.com home page uses the same four groups.

## Claims
1. The docs use-cases page shows four headings (Endpoint security, Threat intelligence, Security operations, Cloud security) and twelve use cases (configuration assessment, malware detection, file integrity monitoring, threat hunting, log data analysis, vulnerability detection, incident response, regulatory compliance, IT hygiene, container security, posture management, workload protection). The page text does not show which use case sits under which heading (the items appear interleaved, as in a four-column grid); the grouping of three use cases per heading is confirmed by the wazuh.com home page (claim 2).
   - Quote: "Below you can find examples of some of the most common use cases of the Wazuh platform."
   - Source: https://documentation.wazuh.com/current/getting-started/use-cases/index.html
   - Confidence: high (headings and use cases); medium (grouping, taken from the home page)

2. The wazuh.com home page uses the same four groups and the same use cases (Endpoint Security, Threat Intelligence, Security Operations, Cloud Security). These are menu/section labels, not prose, so no sentence quote is available.
   - Quote: (labels only) "Endpoint Security" / "Cloud Security"
   - Source: https://wazuh.com/
   - Confidence: medium (labels as extracted by the fetch tool)

3. The default ruleset supports five compliance frameworks: PCI DSS, HIPAA, NIST 800-53, TSC and GDPR.
   - Quote: "the PCI DSS, HIPAA, NIST 800-53, TSC, and GDPR frameworks and standards"
   - Source: https://documentation.wazuh.com/current/compliance/index.html
   - Confidence: high

4. The docs state the compliance mappings are indicative and that deploying Wazuh does not by itself guarantee compliance.
   - Quote: "The rule and control mappings described in this section are indicative." / "does not, by itself, certify or guarantee compliance with PCI DSS, HIPAA, NIST 800-53"
   - Source: https://documentation.wazuh.com/current/compliance/index.html
   - Confidence: high

5. The docs describe Wazuh as a unified SIEM and XDR platform for on-premises, virtualised, cloud and containerised workloads.
   - Quote: "Wazuh is a free and open source platform that provides unified Security Information and Event Management (SIEM)"
   - Source: https://documentation.wazuh.com/current/cloud-service/index.html
   - Confidence: high

6. Customer stories name these use cases: log data collection, system inventory, FIM and vulnerability detection (Groupon, listed under "Top Wazuh Use Cases"); log centralisation and ransomware detection (University of Chichester); active response, plus FIM and vulnerability detection as additional features (iSecNG).
   - Quote (Groupon): "Log Data Collection" / "System inventory"
   - Source: https://wazuh.com/resources/case-studies/groupon-deploys-wazuh-to-protect-and-monitor-aws/
   - Quote (Chichester): "the university successfully centralized logs from different sources." / "Wazuh uniquely detected ransomware that had evaded detection during previous proof of concepts."
   - Source: https://wazuh.com/resources/case-studies/university-of-chichester-achieving-proactive-defense/
   - Quote (iSecNG): "Active response mechanisms, enabling automated reactions to detected threats" / "utilizes additional Wazuh features such as File Integrity Monitoring (FIM) and Vulnerability Detection"
   - Source: https://wazuh.com/resources/case-studies/isecng-strengthening-cybersecurity-with-wazuh/
   - Confidence: medium (vendor case studies)

## Inference
- Inference: the use cases named in these customer stories broadly correspond to the documented ones, although the labels differ (for example "Log Data Collection" vs. the docs' "Log data analysis", "System inventory" vs. "IT hygiene").
- Inference: compliance reporting and log centralisation are the use cases that appear most often in customer stories, while the docs give equal weight to all twelve.
- Inference: the disclaimer in claim 4 means compliance evidence and reporting is left to the user, a possible gap for a SaaS service (to be checked in pain-point research).

## Open questions
- No source read ranks the use cases by how often they are used.
- Other frameworks (ISO 27001, NIS2) appear in case studies (iSecNG) but are not in the docs' list of default mappings; not checked whether the docs cover them elsewhere.

## Changes after verification
- Claim 1: said the docs page lists the headings and use cases but its text does not show the grouping; the grouping is taken from the home page (claim 2). Split confidence: high for the lists, medium for the grouping. Re-fetched 2026-11-10.
- Claim 6: added the University of Chichester and iSecNG case-study URLs (fetched 2026-11-10) with quotes; corrected the iSecNG part (FIM is an "additional" feature there, alongside vulnerability detection); removed "match the documented ones" from the claim.
- Inference: added a line with the "match the documented ones" interpretation moved out of claim 6, noting the label differences.
- Front matter left as is (`url: multiple, see claims`), allowed by the template for a topic note.
