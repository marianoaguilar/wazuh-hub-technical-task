---
note: research/sources/landscape-builtin-help.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | custom.html: "have to copy the rules to a file under the `/var/ossec/etc/rules/` directory on the Wazuh server", "add `overwrite="yes"`" and the example of changing rule 5710 from level 5 to 10 are on the page. |
| 2 | SUPPORTED | custom.html: "it is currently not possible to overwrite the `if_sid`, `if_group`, `if_level`, `if_matched_sid`" (plus `if_matched_group`); those tags are ignored in overwrite rules. |
| 3 | SUPPORTED | rules.html: `ignore` quote matches word for word ("triggers(to avoid floods)"); `noalert`, `frequency` and `timeframe` are documented as rule options. |
| 4 | SUPPORTED | rules.html, `noalert`: "Does not trigger an alert if the rule matches." |
| 5 | SUPPORTED | testing.html: quote is on the page; the CLI (`/var/ossec/bin/wazuh-logtest`), dashboard "Tools > Ruleset test" and the API PUT `/logtest` endpoint are listed. |
| 6 | SUPPORTED | vulnerability-detection/index.html: quote is on the page; it names the Wazuh CTI vulnerabilities repository and an "Offline vulnerabilities repository". |
| 7 | SUPPORTED | compliance/index.html: quote is word for word; custom standards are added "by adding the compliance identifier in the `<group>` tag of rules". |
| 8 | SUPPORTED | compliance/index.html: "deploying Wazuh does not, by itself, certify or guarantee compliance". |
| 9 | SUPPORTED | multi-tenancy.html: quote is word for word; enabled with `opensearch_security.multitenancy.enabled` in `opensearch_dashboards.yml`. The page does not mention isolation of alert data, indices or DLS, so the absence statement limited to "the page" is accurate. |
| 10 | SUPPORTED | 5.0-rc reporting.html: "both scheduled and on-demand report generation", PDF/PNG/CSV/XLSX, email notifications for delivery; the page says "This documentation covers an upcoming release that is still under development". The page text does not say "RC", which matches the corrected front matter. |

## Note-level problems
- None. Front matter is complete (`url: multiple, see claims` is valid; every claim cites its own URL). `source_type: official-docs` fits all claims. `high` confidence fits official documentation. The fixes listed in "Changes after verification" were applied: the summary statement about building blocks is now an inference limited to the pages read, 4.x reporting is marked UNVERIFIED (404), Inference 2 is limited to the cited pages, and the MSSP multi-tenancy inference carries `UNVERIFIED:`. The absence of EPSS/KEV on the vulnerability page was re-checked and is accurate. No personal data. English.

## Recommended fixes
- None.
