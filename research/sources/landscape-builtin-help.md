---
title: Built-in Wazuh help for tuning, rule testing, vulnerabilities, compliance, reporting and multi-tenancy
url: multiple, see claims
publisher: Wazuh Inc. (documentation.wazuh.com)
source_type: official-docs
wazuh_version: current docs (4.14.x) unless noted; reporting module claim is from the 5.0 pre-release docs (the page calls itself an upcoming release still under development; "rc" comes only from the URL path)
accessed: 2026-11-10
question: What already exists to help Wazuh users, especially with AI? (built-in help for common pains)
---

## Summary
The official pages read describe noise reduction, rule testing, vulnerability detection, compliance mapping and dashboard tenants. Noise is reduced by editing XML rules (overwrite, level, noalert, ignore, frequency/timeframe). Rules and decoders are tested with wazuh-logtest (CLI, dashboard "Ruleset test" and API). Vulnerability detection matches software inventory against Wazuh CTI. The ruleset maps alerts to PCI DSS, HIPAA, NIST 800-53, TSC and GDPR. Dashboard tenants separate saved objects. The official pages read do not describe prioritisation signals (EPSS/KEV) or data isolation by tenant. No 4.x reporting page could be read (the URL tried returned 404), so 4.x reporting is UNVERIFIED; the 5.0 pre-release docs describe scheduled and on-demand reporting.

## Claims
1. Default rules are customised by copying them to `/var/ossec/etc/rules/` and adding `overwrite="yes"` (for example to change the level).
   - Quote: "copy the rules to a file under the `/var/ossec/etc/rules/` directory"
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html
   - Confidence: high
2. Overwriting has limits: the parent-rule links cannot be changed.
   - Quote: "it is currently not possible to overwrite the `if_sid`, `if_group`, `if_level`"
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html
   - Confidence: high
3. Rule XML options for noise control include `noalert`, `ignore`, and `frequency`/`timeframe`.
   - Quote: "The time (in seconds) to ignore this rule after it triggers(to avoid floods)."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html
   - Confidence: high
4. `noalert` suppresses alerts for a matching rule.
   - Quote: "Does not trigger an alert if the rule matches."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html
   - Confidence: high
5. wazuh-logtest tests decoders and rules against sample logs, from the CLI, the dashboard (Tools > Ruleset test) and the server API `/logtest` endpoint.
   - Quote: "allows the testing and verification of decoders and rules against provided log samples"
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/testing.html
   - Confidence: high
6. Vulnerability detection finds vulnerable OS packages and applications using the Wazuh CTI vulnerability repository (with an offline option).
   - Quote: "helps users discover vulnerabilities in the operating system and applications installed on the monitored endpoints"
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/index.html
   - Confidence: high
7. The default ruleset supports five compliance frameworks; others can be added through rule groups.
   - Quote: "The default Wazuh ruleset supports the PCI DSS, HIPAA, NIST 800-53, TSC, and GDPR frameworks and standards."
   - Source: https://documentation.wazuh.com/current/compliance/index.html
   - Confidence: high
8. Wazuh does not certify compliance.
   - Quote: "does not, by itself, certify or guarantee compliance"
   - Source: https://documentation.wazuh.com/current/compliance/index.html
   - Confidence: high
9. Dashboard multi-tenancy separates saved objects (index patterns, visualisations, dashboards). The page does not say it isolates the underlying alert data, and it must be enabled in the dashboard config.
   - Quote: "Tenants in the Wazuh dashboard are containments for saving index patterns, visualizations, dashboards, and other objects."
   - Source: https://documentation.wazuh.com/current/user-manual/wazuh-dashboard/multi-tenancy.html
   - Confidence: high
10. Wazuh 5.0 (pre-release docs) adds a reporting module with scheduled and on-demand reports (PDF/PNG/CSV/XLSX) and email delivery.
    - Quote: "both scheduled and on-demand report generation"
    - Source: https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-indexer/modules/reporting.html
    - Confidence: high

## Inference
- Inference: Out of the box, the pages read describe low-level building blocks rather than guided workflows.
- Inference: Tuning in 4.x, as described on the cited pages, means editing XML, restarting the manager and checking with logtest. The cited pages provide the tools but give no guidance on *which* rules are noisy or *what* change is safe. This looks like a gap that an assisted service could fill.
- Inference: The vulnerability detection page does not mention exploitability-based prioritisation. That needs checking against the dashboard docs before it is called a gap.
- Inference: UNVERIFIED: Multi-tenancy for MSSPs needs RBAC/DLS plus tenants to be combined by hand (community threads seen in search results suggest so; they were not read, so no source backs this).

## Open questions
- UNVERIFIED: whether the vulnerability dashboard exposes CVSS scores/severity filters (dashboard docs page returned 404).
- UNVERIFIED: 4.x dashboard PDF reporting details (the 4.x reporting page URL tried returned 404).
- Community advice on tuning (Google Group threads) was seen in search results only and not read.

## Not read
- https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/dashboard.html (404)
- https://documentation.wazuh.com/current/user-manual/wazuh-dashboard/generating-reports.html (404)
- Google Groups threads on tuning and multi-tenancy seen in search results (not fetched)

## Changes after verification
- Front matter `wazuh_version`: "5.0 RC" replaced by "5.0 pre-release docs"; the page text does not say "RC", only the URL path does (optional fix from the report).
- Summary, first sentence: the general statement "Wazuh gives users low-level building blocks rather than guided workflows" moved to Inference and limited to the pages read; it was an inference stated as fact.
- Summary, reporting: "In 4.x the read pages show no scheduled reporting" replaced by "no 4.x reporting page could be read (404), so 4.x reporting is UNVERIFIED"; no read source backed a 4.x absence.
- Inference 1 (tuning): "Wazuh provides ... no guidance" limited to "the cited pages give no guidance"; an absence on a page is not an absence in Wazuh.
- Inference 3 (MSSP multi-tenancy): prefixed with `UNVERIFIED:`; the community threads it relies on were not read.
- Claims 1-10: unchanged (all SUPPORTED).
