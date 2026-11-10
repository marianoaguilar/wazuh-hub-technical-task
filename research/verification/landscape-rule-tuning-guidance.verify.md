---
note: research/sources/landscape-rule-tuning-guidance.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | PARTIAL | Substance is on custom.html ("...are overwritten during the upgrade process"; changes go in `/var/ossec/etc/rules/`; rule 5710 raised from level 5 to 10). The second quote is not verbatim: the page says "add `overwrite="yes"` to indicate that this rule overwrites an already defined rule", not "to indicate the rule overwrites an existing one". |
| 2 | SUPPORTED | custom.html note: "it is currently not possible to overwrite the `if_sid`, `if_group`, `if_level`, `if_matched_sid`..." and "These tags are ignored when present in an overwrite rule, preserving the original values." (The page also lists `if_matched_sid` and `if_matched_group`; the claim omits them but is not wrong.) |
| 3 | SUPPORTED | custom.html example rule 5710 contains `<if_sid>5700</if_sid>`; "Use ID numbers between 100000 and 120000 for custom rules"; test with `wazuh-logtest` after saving, but "you need to restart the Wazuh manager to generate alerts based on these changes". |
| 4 | SUPPORTED | rules.html: if_sid "it matches when a rule ID on the list has previously matched"; overwrite "Used to replace a rule with local changes."; list "Path to the CDB file." |
| 5 | SUPPORTED | rules-classification.html: level 0 "No action taken. Used to avoid false positives."; level 1 "is below the default alert threshold (log_alert_level 3), so these events don't generate alerts". |
| 6 | PARTIAL | Quote, lookup types and absence of "exception"/"whitelist" are confirmed on cdb-list.html. But "its example alerts on users not in a list" is wrong: the page's rule examples (110700, 110701, 110710) alert on source IPs that ARE in a list; the user-outside-a-list case is only a prose illustration, not a rule. Also the lookup list omits `address_match_key_value` (the page lists it). |
| 7 | SUPPORTED | testing.html: "allows the testing and verification of decoders and rules against provided log samples"; "Tools > Ruleset test"; `/var/ossec/bin/wazuh-logtest`; API table with `PUT /logtest` and `DELETE /logtest/sessions/{token}`; API reference link is 4.14. |
| 8 | SUPPORTED | ruleset index.html: "This tool processes only one-liner (no line breaks) logs."; "make custom changes in the `/var/ossec/etc/` directory". No guidance on noisy or most-frequent rules found on the page (absence scoped to this page, as the claim says). |
| 9 | SUPPORTED | v4.14.0 `ruleset/testing` listing shows `ruleset/`, `tests/`, `coverage.py`, `runtests.py`; `tests/` listing includes `sshd.ini`, `apache.ini`, `sysmon_eid_1.ini`. |
| 10 | SUPPORTED | runtests.py: `description='This script tests Wazuh rules.'`; reads `rule`, `alert`, `decoder` and `log ...` keys per section; calls `wazuh-logtest -U rule:alert:decoder`; messages "Log decoded by unexpected decoder..." and "Unexpected alert level..."; prints Rules/Decoders coverage; `sys.exit(1)` on error. Medium confidence is appropriate. |
| 11 | SUPPORTED | `main` `ruleset/` visible listing shows only `mitre/`, `sca/`, `README.md` plus a "View all files" link; `main/ruleset/testing` returned HTTP 404 in this session. The truncation caveat and medium confidence are appropriate. |
| 12 | SUPPORTED | 5.0-rc wazuh-dashboard.html: "You can use Log test to check custom decoders and rules before you rely on them." and "This documentation covers an upcoming release that is still under development." |
| 13 | SUPPORTED | Content Manager rule-testing page: Engine normalizes, then Sigma rules are evaluated; "Draft → Test → Custom"; `/_plugins/_content_manager/logtest` and `/promote`; both quotes present; "Test one change at a time"; benign events to "confirm no false positives"; no regression suite described. |
| 14 | SUPPORTED | threat-hunting.html: "The Rules module on the Wazuh dashboard presents both default and custom rules"; no top/most-frequent rule visualisation (only MITRE technique frequency). |

## Note-level problems
- None. Front matter is complete (`url: multiple, see claims` with a URL per claim). Absence statements in the Summary and Inference are scoped to the pages listed. Inferences are labelled. No personal data. English.

## Recommended fixes
- Claim 1: replace the second quote with the exact page text: "to indicate that this rule overwrites an already defined rule".
- Claim 6: drop or correct "its example alerts on users not in a list" (the rule examples match IPs present in lists; the user case is only prose). Optionally add `address_match_key_value` to the lookup list.
