---
title: Does Wazuh use CISA KEV or FIRST EPSS in vulnerability detection? - topic note
url: multiple, see claims
publisher: Wazuh (documentation, GitHub, CTI)
source_type: official-docs
wazuh_version: 4.14.x (docs "current"), 5.0-beta docs, 5.0.0 GitHub work
accessed: 2026-11-10
question: Does Wazuh itself already use KEV or EPSS in vulnerability detection?
---

## Summary
In the Wazuh 4.x documentation ("current", release notes up to 4.14.10) the vulnerability detection pages do not mention EPSS or KEV, and they describe no exploit-based prioritization. CISA appears only as one of the "security databases" behind the Wazuh CTI feed. An open feature request to integrate EPSS exists since January 2023 with no linked work. A closed 5.0.0 task (#36000) added parsing of KEV and EPSS payloads in the CVE 5.0 content model to the manager scanner, but no page read says these values are shown in alerts, the indexer or the dashboard.

## Claims
1. The Wazuh "current" vulnerability detection page sources data from the Wazuh CTI vulnerabilities repository (or an offline copy) and does not mention EPSS, KEV or prioritization.
   - Quote: "Wazuh vulnerabilities repository in our Cyber Threat Intelligence (CTI) platform."
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/index.html
   - Confidence: high (absence checked on this page only)

2. The "How it works" page (current docs, release notes up to 4.14.10) lists CISA as one of the security databases, next to MSU, NVD and OSV; EPSS and KEV are not mentioned.
   - Quote: "Microsoft Security Updates (MSU), National Vulnerability Database (NVD), Open Source Vulnerabilities (OSV)," and "Cybersecurity and Infrastructure Security Agency (CISA)."
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/how-it-works.html
   - Confidence: high

3. The 5.0-beta "How it works" page has the same list of sources including CISA, and still does not mention EPSS, KEV or prioritization.
   - Quote: "Cybersecurity and Infrastructure Security Agency (CISA)."
   - Source: https://documentation.wazuh.com/5.0-beta/user-manual/capabilities/vulnerability-detection/how-it-works.html
   - Confidence: high

4. The Wazuh CTI CVE explorer offers filters by CVSS score, severity and date; no EPSS, KEV or "exploited" field was visible (the page did not fully load).
   - Quote: the page "provides access to a comprehensive database of vulnerabilities"
   - Source: https://cti.wazuh.com/vulnerabilities/cves
   - Confidence: low (page loaded partly; absence not conclusive)

5. Issue #15872 "Feature Request: Integrate EPSS to vulnerability detection" is open since 2023-01-11, has no linked branches or PRs; in 2023 a commenter said the approach was being considered for an upcoming refactor, and in 2026 users asked again for EPSS and KEV in 5.x without an official reply visible.
   - Quote: "Feature Request: Integrate EPSS to vulnerability detection"
   - Source: https://github.com/wazuh/wazuh/issues/15872
   - Confidence: high (state as of access date)

6. Issue #36000 (closed as completed 2026-05-12, board "XDR+SIEM/Release 5.0.0", PR #36030 "Added new CVE5 fields") adapts the manager vulnerability scanner to the CVE 5.0 content model, including `metrics.other` entries of type KEV and EPSS.
   - Quote: "Add `metrics.other` support for KEV payloads" / "Add `metrics.other` support for EPSS payloads"
   - Source: https://github.com/wazuh/wazuh/issues/36000
   - Confidence: high

7. Issue #36000 does not say whether KEV or EPSS data is exposed in alerts, the indexer or the dashboard.
   - Quote: "The manager vulnerability scanner must be updated to support these new fields and structures."
   - Source: https://github.com/wazuh/wazuh/issues/36000
   - Confidence: medium

8. A GitHub issue search in wazuh/wazuh for "EPSS" returned 4 results (issues #38399, #36000, #15872 and pull request #31571) and for "KEV" returned 7 (including #40532, #40314, #39952, #39354, #36000, #24000, #15872); only #15872 and #36000 were read and are relevant here.
   - Quote: (search result titles, e.g.) "Adapt vulnerability scanner and FlatBuffers schema to support enhanced CVE 5.0 vulnerability content model"
   - Source: https://github.com/wazuh/wazuh/issues?q=EPSS ; https://github.com/wazuh/wazuh/issues?q=KEV
   - Confidence: medium (search results may match in comments; not each issue was read)

## Inference
- Inference: In Wazuh 4.x, users who want "fix first" ranking by KEV/EPSS must enrich findings outside Wazuh. This supports the gap the Phase 3 service fills.
- Inference: Wazuh 5.0 is moving toward carrying KEV/EPSS in its CVE content. The design should treat Wazuh-provided KEV/EPSS fields as an optional input when present and keep its own KEV/EPSS fetch as the baseline, so it works with 4.x and does not compete with a feature Wazuh may ship.

## Open questions
- UNVERIFIED: whether Wazuh 5.0 findings in `wazuh-states-vulnerabilities` include KEV or EPSS fields (field reference not read).
- Issues #38399, #31571, #40532, #40314, #39952, #39354, #24000 not read in full; #24000 page content was truncated.
- What "CISA" as a source means in the Wazuh feed (KEV, Vulnrichment, or something else) is not stated on the pages read.

## Not read
- https://n8n.io/workflows/17782-prioritize-and-report-wazuh-vulnerabilities-with-epss-and-cisa-kev/ - community workflow seen in search results only; not fetched, no claim made.
- https://documentation.wazuh.com/5.0-rc/user-manual/capabilities/vulnerability-detection/index.html - search result only; not fetched.
