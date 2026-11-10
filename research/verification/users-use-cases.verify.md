---
note: research/sources/users-use-cases.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Quote is on the docs page verbatim, along with the four headings and the twelve use cases. The items come in an interleaved order and the text does not link them to headings, which the note now says itself. The grouping is credited to the home page (claim 2) at medium confidence. |
| 2 | SUPPORTED | The wazuh.com home page shows the four groups, each with the three items given in claim 1 (e.g. Endpoint Security: Configuration Assessment, Malware Detection, File Integrity Monitoring; Cloud Security: Container Security, Posture Management, Workload Protection). |
| 3 | SUPPORTED | Page says: "The default Wazuh ruleset supports the PCI DSS, HIPAA, NIST 800-53, TSC, and GDPR frameworks and standards." |
| 4 | SUPPORTED | Page says: "The rule and control mappings described in this section are indicative." and "deploying Wazuh does not, by itself, certify or guarantee compliance with PCI DSS, HIPAA, NIST 800-53...". |
| 5 | SUPPORTED | Cloud service page: "a free and open source platform that provides unified Security Information and Event Management (SIEM) and Extended Detection and Response (XDR) capabilities", protecting "workloads across on-premises, virtualized, cloud, and containerized environments". |
| 6 | SUPPORTED | Groupon page lists "File Integrity Monitoring", "Log Data Collection", "PCI DSS compliance", "System inventory" and "Vulnerability Detection" under "Top Wazuh Use Cases". Chichester page has both quoted sentences ("the university successfully centralized logs from different sources"; "Wazuh uniquely detected ransomware that had evaded detection during previous proof of concepts."). iSecNG page has both quoted phrases (active response mechanisms; "additional Wazuh features such as File Integrity Monitoring (FIM) and Vulnerability Detection"). |

## Note-level problems
- None. Front matter is complete (`url: multiple, see claims` is valid for a topic note, and every claim cites its own URL). Confidence levels fit the sources (high on official docs, medium on home page labels and vendor case studies). The interpretation that was in claim 6 is now an `Inference:` line. The open question about ISO 27001 and NIS2 matches the iSecNG page, which names both. No personal data (only company and institution names). The note is in English.
- Minor, not blocking: the Groupon list also includes "PCI DSS compliance", which claim 6 leaves out. The second inference ("compliance reporting ... appear most often in customer stories") rests on only three stories. It is labelled as inference, so this is acceptable.

## Recommended fixes
- None.
