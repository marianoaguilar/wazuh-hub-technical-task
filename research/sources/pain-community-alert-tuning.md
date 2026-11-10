---
title: Wazuh mailing list threads on alert noise, rule tuning, suppression and default detection coverage
url: multiple, see claims
publisher: Wazuh mailing list (Google Groups)
source_type: forum
wazuh_version: 4.x; 4.14.2 to 4.14.7 where stated
accessed: 2026-11-10
question: What do Wazuh users complain about or ask for help with, outside GitHub?
---

## Summary
Users regularly ask how to silence repeated or false-positive alerts and how to write child rules
with frequency, timeframe, same_srcip or ignore. Some requested behaviours are hard to achieve with
the rule engine. A second strand, from late 2026, questions how much a default install detects at
all: replays of ATT&CK techniques and auditd threads show that several detections need extra
configuration (audit rules, localfile blocks, FIM timing).

## Claims
1. Frequency signal: a group search for "noise" (first 30 results) returned at least 9 tuning/suppression threads with listing (last-activity) dates from Oct 2025 to Aug 2026 (year inferred; the listing omits it), e.g. "Wazuh rules fine tuning." (6 posts), "Silencing alerts for the same user or same srcip over a period of time" (4), "Wazuh supress" (4), "False Postive webshell detection" (10), "Fix False Positive" (3), "Exclude Event ID 4625 (SubStatus 0xC000006F) from Rule 60204 Frequency Correlation" (8), "FİM ignore best practise" (2), "Request for Clarification on Frequent File Changes" (3), "Help needed: Disk usage alerting across multiple agents with ignore/frequency rules" (3).
   - Quote: "Wazuh rules fine tuning." (thread title)
   - Source: https://groups.google.com/g/wazuh/search?q=noise
   - Confidence: high (titles on the page; the classification and tally are mine)
2. A user wanted first-hit-only alerts per source/destination pair for rule 11201 (Feb 2026); replies said the rule engine cannot enrich alerts after creation and the exact behaviour is hard to get.
   - Quote: "it will be a bit difficult to achieve the exact use case you are looking for"
   - Source: https://groups.google.com/g/wazuh/c/AueIHdMM0mI
   - Confidence: medium
3. A suppression rule did not work because level-0 rules are discarded before `if_matched_sid` (Oct 2025).
   - Quote: "rules at level 0 are discarded immediately and will not be used with if_matched_rules."
   - Source: https://groups.google.com/g/wazuh/c/bQwo-NWlnW4
   - Confidence: medium
4. Webshell rules raised false positives on a Laravel app (Jan 2026); a reply blamed overly broad rules and the fix was rewriting the custom webshell rules (100500-100520). (A FIM ignore entry in the same thread was for an unrelated Windows path raised in a side question.)
   - Quote: "The false positives are caused by overly broad webshell rules that classify any PHP file modification as malicious."
   - Source: https://groups.google.com/g/wazuh/c/NJQTwLSMujY
   - Confidence: low
5. A thread (first post Sep 3, 2026) reports that a replay of 24 ATT&CK techniques against a default install raised alerts for 3. Another participant challenged the method (short window vs 12-hour FIM scan, version not recorded). The original poster then conceded that the 3-of-24 figure is not reproducible from what they had published, and ran a re-run on stock 4.14.7 with 4 techniques, in which only one fired at attack time (the other three were attributed to FIM's 12-hour schedule and no audit rules loaded).
   - Quote: "the 3-of-24 is not reproducible from anything we have published" / "out-of-the-box only one fired at attack time."
   - Source: https://groups.google.com/g/wazuh/c/xCNva7qg-R4
   - Confidence: low (disputed in the thread itself)
6. A related thread on 4.14.7 (Sep 2026) states a stock install loads no audit rules, so audit.key-based rules have nothing to match, and the audit.log localfile block depends on install order.
   - Quote: "Adding the localfile by hand is the fix in every case"
   - Source: https://groups.google.com/g/wazuh/c/JFaiCE4ZkUw
   - Confidence: low (one community thread; no poster shown as Wazuh staff)
7. A team evaluating Wazuh for 13 attack categories (Aug 2026) was advised not to rely only on default rules.
   - Quote: "I would not recommend trying to handle everything using only the default Wazuh rules."
   - Source: https://groups.google.com/g/wazuh/c/h7X7TuSWF0g
   - Confidence: low
8. A community answer notes rules and SCA policies are not pulled automatically; they come with upgrades (Jan 2026).
   - Quote: "Wazuh does not automatically pull new rules and SCA policies from the repository unless you upgrade."
   - Source: https://groups.google.com/g/wazuh/c/IvBhJiYuIpQ
   - Confidence: medium

## Inference
- Inference: tuning is done thread by thread with XML child rules, and both "too many alerts" and
  "too few alerts by default" appear. Users would benefit from guided tuning, tested rule packs, and
  coverage checks.

## Open questions
- Reddit threads on alert noise could not be read (see Not read); the mailing list may over-represent
  hands-on administrators.

## Not read
- https://old.reddit.com/r/Wazuh/top/?t=year and https://www.reddit.com/r/Wazuh/top/?t=year — the fetch tool cannot fetch from reddit.com. No Reddit claims are made in these notes.
- reddit.sentinel-team.org snapshot pages appeared in search results; this is a third-party mirror, not Reddit, so it was not used.

## Changes after verification
- Claim 1: SUPPORTED; only added that the listing dates are last-activity dates and the year is inferred (caveat raised in the report, and a rule of this fix round).
- Claim 4: removed "plus FIM ignore entries"; the fix was rewritten webshell rules, and the only FIM ignore in the thread was for an unrelated Windows path (re-fetched page).
- Claim 5: removed "18 posts in listing" (not reproducible; the page shows 8 posts and no total); replaced the quote with the original poster's concession and the 4.14.7 re-run result (1 of 4 fired at attack time); "reviewer" changed to "another participant".
- Claim 6: confidence lowered from medium to low-medium (one community thread, optional fix from the report).
- Claim 7: "14 attack categories" corrected to 13 (counted on the re-fetched page).
- Main session, after second verification: Claim 6: confidence `low-medium` (not an allowed value) changed to `low`, as the second report recommends.
