---
title: Wazuh official guidance and tooling for rule tuning and ruleset testing
url: multiple, see claims
publisher: Wazuh Inc. (documentation.wazuh.com, wazuh/wazuh GitHub, wazuh.github.io)
source_type: official-docs
wazuh_version: 4.x "current" docs (sidebar shows 4.14.10 as latest release; testing page links API reference 4.14); wazuh/wazuh tag v4.14.0; 5.0-rc docs and wazuh-indexer-plugins docs (Wazuh 5.x)
accessed: 2026-11-10
question: Does the official Wazuh documentation or blog give guidance or tooling for finding noisy rules, tuning/silencing them safely, testing rule/decoder changes before deploying, and checking that a change did not break other rules?
---

## Summary
The official 4.x docs explain how to change rules (copy a default rule to `/var/ossec/etc/rules/`
with `overwrite="yes"`, child rules with `if_sid`, level 0 "used to avoid false positives", CDB lists
via `<list>`), and how to test single log samples with `wazuh-logtest` from the CLI, the dashboard
(Tools > Ruleset test) and the server API (`PUT /logtest`). The `wazuh/wazuh` repository (v4.14.0)
ships a ruleset test harness (`ruleset/testing/runtests.py` plus `.ini` test files) that runs
`wazuh-logtest` against expected decoder/rule/level results; I found no user documentation for it.
The pages I read do not describe how to find the rules that generate the most alerts, and do not
describe regression testing of a custom ruleset. The Wazuh 5.x docs add a Content Manager logtest
with a Draft → Test → Custom promotion chain, again for single events.

## Claims
1. Default rule files are overwritten on upgrade, so changes to them must go in `/var/ossec/etc/rules/`; a default rule is changed by copying it there and adding `overwrite="yes"`.
   - Quote: "overwritten during the upgrade process" ... add `overwrite="yes"` "to indicate that this rule overwrites an already defined rule" (exact page text, per the verification report; the example changes SSH rule 5710 from level 5 to 10)
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html
   - Confidence: high
2. When overwriting a rule, `if_sid`, `if_group` and `if_level` cannot be changed; they are ignored and the original values are kept.
   - Quote: "currently not possible to overwrite the `if_sid`, `if_group`, `if_level`" ... these tags "are ignored when present in an overwrite rule."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html
   - Confidence: high
3. The custom rules page shows child rules built with `<if_sid>` (example parent 5700) and recommends custom rule IDs between 100000 and 120000. It says saving rule files is enough to test them with `wazuh-logtest`, but the manager must be restarted to produce alerts.
   - Quote: "need to restart the Wazuh manager to generate alerts based on these changes"
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html
   - Confidence: high
4. The rules syntax reference defines `if_sid`, `overwrite` and `list`.
   - Quote: "it matches when a rule ID on the list has previously matched." / overwrite: "Used to replace a rule with local changes." / list: "Path to the CDB file."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html
   - Confidence: high
5. Level 0 is documented as the level for ignoring events and avoiding false positives; levels below the default alert threshold do not produce alerts.
   - Quote: "No action taken. Used to avoid false positives."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/rules/rules-classification.html
   - Confidence: high
6. CDB lists are documented for allow/deny lists and used in rules with the `<list>` tag (`match_key`, `not_match_key`, `address_match_key`, `not_address_match_key`, `match_key_value` with `check_value`). That page does not use the words "exception" or "whitelist" for suppressing rules; its rule examples match IP addresses that are present in a list (the user case is described only in prose).
   - Quote: "The main use case of this feature is to create a white/black list of users, file hashes, IP addresses, or domain names."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/cdb-list.html
   - Confidence: high
7. `wazuh-logtest` tests decoders and rules against sample logs. You can run it from the dashboard (Tools > Ruleset test), the command line (`/var/ossec/bin/wazuh-logtest`) or the server API (`PUT /logtest`, `DELETE /logtest/sessions/{token}`).
   - Quote: "allows the testing and verification of decoders and rules against provided log samples on the Wazuh server."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/testing.html
   - Confidence: high
8. The ruleset overview page says `wazuh-logtest` only processes single-line logs and that custom changes belong in `/var/ossec/etc/`. According to the fetch, it has no guidance on noisy rules or on finding the rules that trigger most often.
   - Quote: "processes only one-liner (no line breaks) logs."
   - Source: https://documentation.wazuh.com/current/user-manual/ruleset/index.html
   - Confidence: high
9. The `wazuh/wazuh` repository at tag v4.14.0 has a ruleset test harness in `ruleset/testing/`: `runtests.py`, `coverage.py`, and a `tests/` folder of `.ini` files (e.g. `sshd.ini`, `apache.ini`, `sysmon_eid_1.ini`).
   - Quote: (directory listing) "`coverage.py`", "`runtests.py`", "`tests/`"
   - Source: https://github.com/wazuh/wazuh/tree/v4.14.0/ruleset/testing and https://github.com/wazuh/wazuh/tree/v4.14.0/ruleset/testing/tests
   - Confidence: high
10. `runtests.py` reads the `.ini` tests. Each section sets the expected `rule`, `alert` (level) and `decoder`, plus sample log lines. The script sends each log to `wazuh-logtest -U rule:alert:decoder`, prints failures such as "Log decoded by unexpected decoder" or "Unexpected alert level", reports rule/decoder coverage, and exits with status 1 if any test fails.
    - Quote: argparse description "This script tests Wazuh rules." (summary of the script by the fetch tool; the code was read through the tool, not line by line)
    - Source: https://raw.githubusercontent.com/wazuh/wazuh/v4.14.0/ruleset/testing/runtests.py
    - Confidence: medium (official code, but read through a summarising fetch tool)
11. On the `main` branch, the `ruleset/` directory listing shows only `mitre/`, `sca/` and `README.md`. The 4.x `testing/`, `rules/` and `decoders/` folders are not visible there.
    - Quote: (directory listing) "`mitre/`", "`sca/`", "`README.md`"
    - Source: https://github.com/wazuh/wazuh/tree/main/ruleset (and https://github.com/wazuh/wazuh/tree/main/ruleset/testing returned HTTP 404)
    - Confidence: medium (the listing may be truncated: the page shows "View all files")
12. Wazuh 5.0 docs (pre-release) say the dashboard has a "Log test" tool for checking custom decoders and rules.
    - Quote: "You can use **Log test** to check custom decoders and rules before you rely on them."
    - Source: https://documentation.wazuh.com/5.0-rc/getting-started/components/wazuh-dashboard.html
    - Confidence: high (page says it "covers an upcoming release that is still under development")
13. In Wazuh 5.x (wazuh-indexer-plugins Content Manager docs), logtest runs an event through Engine normalization and then Sigma rule evaluation. Content follows a "Draft → Test → Custom" promotion chain, with endpoints such as `POST /_plugins/_content_manager/logtest` and `/_plugins/_content_manager/promote`. The page advises testing one change at a time and checking benign events for false positives. It does not describe a regression suite.
    - Quote: "Rules are evaluated the way a deployed threat detector evaluates them." / "Overly broad rules generate noise."
    - Source: https://wazuh.github.io/wazuh-indexer-plugins/ref/modules/content-manager/rule-testing.html
    - Confidence: high
14. The threat hunting use-case page mentions a dashboard Rules module that lists rules. The fetch found no visualisation of top or most frequent rules on that page.
    - Quote: "The Rules module on the Wazuh dashboard presents both default and custom rules"
    - Source: https://documentation.wazuh.com/current/getting-started/use-cases/threat-hunting.html
    - Confidence: high

## Inference
- Inference, per item asked:
  - **Finding noisy rules:** none of the pages I read (custom.html, rules-classification.html, ruleset index.html, testing.html, cdb-list.html, threat-hunting.html, 5.0-rc wazuh-dashboard.html, the Content Manager rule-testing page) give a method or tool for ranking rules by alert volume. Users would have to build their own dashboard aggregation on `rule.id`. That last point is my inference, not a documented procedure.
  - **Tuning safely:** the mechanisms are documented (overwrite, `if_sid` child rules, level 0, CDB lists). The pages read give no end-to-end "safe tuning" workflow, and none explains how to scope a suppression narrowly.
  - **Testing before deploying:** well covered for single events (`wazuh-logtest` via CLI, dashboard and API; 5.x Content Manager logtest).
  - **Checking nothing else broke:** a harness exists in the repo (`runtests.py` + `.ini` files), but the docs I read do not mention it, and it targets the shipped ruleset plus `test_*` files. Running it against a user's own custom rules and real sample logs is not a documented user workflow.
- Inference: the candidate need "see which rules are noisy, propose a narrow exception, and regression-test it against sample logs before deploy" is only partly served. Wazuh has the building blocks but no guided, packaged workflow.

## Open questions
- No official wazuh.com/blog post on rule tuning or alert noise turned up in my searches. Two searches returned only Google Group threads and third-party guides, which were not read and are not cited. UNVERIFIED that no such blog post exists.
- Whether `runtests.py` is documented anywhere for users (e.g. contributing guide or development docs) was not confirmed.
- What replaces `ruleset/testing` on `main` (5.0) was not confirmed. The Content Manager logtest is the 5.x documented path.
- The second part of the rules syntax page (characters after 100000) was not read.

## Not read
- https://documentation.wazuh.com/5.0-rc/user-manual/capabilities/log-data-collection/log-data-analysis.html (search result only, not fetched)
- https://www.decryptiondigest.com/blog/wazuh-tuning-false-positive-reduction-guide, https://cookbook.solomonneas.dev/security/wazuh-triage/ and several Google Group threads (search results only, third-party, not fetched)

## Changes after verification
- Main session, after verification: Claim 1: quote replaced with the exact page wording.
- Main session, after verification: Claim 6: the CDB example matches IPs present in a list, not users absent from it.
