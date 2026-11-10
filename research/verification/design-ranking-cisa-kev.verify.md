---
note: research/sources/design-ranking-cisa-kev.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Catalog page: "CISA maintains the authoritative source of vulnerabilities that have been exploited in the wild." and "Organizations should use the KEV catalog as an input to their vulnerability management prioritization framework." |
| 2 | SUPPORTED | KEV page lists CVE ID, "reliable evidence that the vulnerability has been actively exploited in the wild", and "a clear remediation action ... such as a vendor-provided update". |
| 3 | SUPPORTED | Catalog page links: `/sites/default/files/csv/known_exploited_vulnerabilities.csv`, `/sites/default/files/feeds/known_exploited_vulnerabilities.json`, `/sites/default/files/feeds/known_exploited_vulnerabilities_schema.json`. |
| 4 | SUPPORTED | JSON header: catalogVersion 2026.11.09, dateReleased 2026-11-09T19:54:37.4945Z, count 1773; entry fields cveID ... cwes all match. |
| 5 | PARTIAL | Absence of a stated schedule is confirmed on both CISA pages. The feed shows dateAdded 2026-11-09 (four entries), 2026-11-06, 2026-11-04, 2026-11-03, 2026-10-30. "Changes several times a week at irregular intervals" is the researcher's inference from a snapshot, written as a claim. |
| 6 | SUPPORTED | GitHub: "Mirror of cisa.gov/kev data files", "updated whenever the KEV is updated", "synchronized within minutes of each other", three files. |
| 7 | SUPPORTED | License file: "distributed under the Creative Commons 0 1.0 License", "You may use this data in any legal manner", as-is, no logo/seal use, no endorsement. |
| 8 | SUPPORTED | Repository is licensed under CC0 (the page says this matches cisa.gov). |

## Note-level problems
- Claim 5 puts an inference ("several times a week at irregular intervals") in the claims list; it already carries `medium` but should be under Inference.
- Front matter complete. No personal data. English.

## Recommended fixes
- Claim 5: keep only "no update schedule is stated on the catalog or KEV pages"; move the frequency statement to the Inference section.
