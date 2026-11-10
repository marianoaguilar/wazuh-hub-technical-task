---
note: research/sources/users-customer-stories.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Page gives "Industry: Electronic commerce" and says "Wazuh has become their intrusion detection system of choice to comply with the Payment Card Industry Data Security Standard"; AWS monitoring is the key challenge. |
| 2 | SUPPORTED | Page lists "File Integrity Monitoring", "Log Data Collection", "System inventory", "Vulnerability Detection"; the challenge is "protecting and monitoring a very high volume of data from Amazon Web Services". |
| 3 | SUPPORTED | Both quotes are on the page. Alignet focuses on "the growing E-commerce market", offers EMV 3D Secure authentication, and aims to be one of the "safest, and most innovative Payment Providers in Latin America". |
| 4 | SUPPORTED | "regulated industries", "invaluable for us as an MSSP", "large-scale data aggregation and analysis for multiple clients"; vulnerability scanning, compliance checks and inventory analysis appear as requirements, plus "add custom detections, rules, and decoders". |
| 5 | SUPPORTED | Both quotes are on the page; it also says they "use Wazuh for SOC purposes". |
| 6 | SUPPORTED | Energy sector (hydropower, solar parks, substations); "security telemetry from various sources such as electrical substations and automation systems" sent to a SIEM engine where Wazuh plays a key role; agent-flexibility quote is on the page. |
| 7 | SUPPORTED | Fixed. ITA and ITA-ISOC named; "40+ departments" quote; "collect logs at scale, particularly focusing on Windows events"; custom rules "covering use cases like Google Password Sync, Netscaler, and integrations with Azure, GCP, GitHub, AWS, BitLocker" and SysMon; Sysadmin quote and "Primary Administrator" title are on the page. |
| 8 | SUPPORTED | "located in West Sussex, England"; "centralized logs from different sources"; Azure Sentinel used; "Wazuh uniquely detected ransomware that had evaded detection during previous proof of concepts", during the evaluation phase. |
| 9 | PARTIAL | Both quotes are on the page (Wazuh Cloud first, then a German datacenter); it describes an MSSP helping "small and middle sizes companies all over Germany". But (a) the page does not say iSecNG is German or where it is based; this is implied, not stated; (b) "demand is driven by NIS2" is stronger than the page, which says "With the European NIS2 directive approaching, organizations are taking proactive steps to implement endpoint and attack monitoring solutions" and does not link NIS2 to growth in iSecNG's demand. |
| 10 | SUPPORTED | "Clients receive dedicated Wazuh instances to ensure data separation and regulatory compliance."; "small 100GB instances or large-scale clusters with multiple terabytes of hot storage"; "Providing a stable and scalable Wazuh cluster based on Kubernetes." |

## Note-level problems
- Inference section, item 3 (fixed): the sourced quote "gaining full control over infrastructure, compliance, and scalability." is on the iSecNG page, in the same sentence as "As demand grew, they transitioned to hosting Wazuh in a German datacenter". It is labelled as a fact with its URL, and the generalisation is labelled `Inference:`. OK.
- Inference 1 says NIS2 is a recurring driver; the page shows it only as a general driver for organisations (see claim 9). It is labelled as inference, so it is acceptable, but it rests on the weaker wording.
- Front matter complete; `url: multiple, see claims` is valid because every claim cites its own URL.
- Confidence: `medium` for vendor case studies is appropriate.
- No role attributions to Wazuh staff. Personal data: none. The ITA, Enevo and FirmGuardian pages name individuals; the note uses roles only.
- Language: English.

## Recommended fixes
- Claim 9: change "a German MSSP" to "an MSSP serving small and mid-sized companies across Germany", and "demand is driven by NIS2" to "the page cites the approaching NIS2 directive as a reason organisations adopt endpoint and attack monitoring" (or add the NIS2 quote).
