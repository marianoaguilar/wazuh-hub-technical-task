---
title: Wazuh mailing list threads on upgrades and behaviour changes after upgrading
url: multiple, see claims
publisher: Wazuh mailing list (Google Groups)
source_type: forum
wazuh_version: 4.5 to 4.14.9 (per thread, see claims)
accessed: 2026-11-10
question: What do Wazuh users complain about or ask for help with, outside GitHub?
---

## Summary
Upgrades are a recurring source of questions: which path to follow from old versions, and why
something changed or broke afterwards (decoders matching differently, an SCA policy failing to parse,
Active Response no longer acting, dashboard showing workers offline). Several threads end without a
confirmed root cause in the visible content.

## Claims
1. Frequency signal: a group search for "after upgrade" (first 30 results) returned 10 threads (by my classification) clearly about Wazuh upgrade paths, EoL or post-upgrade breakage, with listing (last-activity) dates Jun 10 to Nov 2 for the 10 counted threads (Jun 5 to Nov 6 for all 30 results; the listing shows no year; 2026 is inferred). The 10 counted: "FortiGate Decoder Change After Wazuh Patch Upgrade (v4.14.7 to v4.14.9)" (2 posts), "Upgrade Path" (5), "Wazuh Software EoL Policy" (2), "Indexer-connector fails to initialize for agents enrolled after a date threshold — persists across worker/master nodes and after 4.14.5→4.14.7 upgrade" (3), "Upgrading agents fails on multiple Windows endpoints" (10), "Active Response | Working in Older version | Not Working in Newer Version" (3), "Dashboard Server Management shows Worker nodes Offline after upgrading from 4.10.3 to 4.14.5 ..." (4), "Wazuh remote upgrade for RHEL5 agent" (4), "After update wazuh-indexer not initialize in cluster mode" (2), "Wazuh version upgrade from 4.2.7 to a latest version" (5). Not counted: borderline results and two threads about OS (not Wazuh) upgrades.
   - Quote: "FortiGate Decoder Change After Wazuh Patch Upgrade (v4.14.7 to v4.14.9)" (thread title)
   - Source: https://groups.google.com/g/wazuh/search?q=after%20upgrade
   - Confidence: medium (titles on the page; classification and tally are mine; year inferred; search results are a snapshot from 2026-11-10)
2. After a patch upgrade 4.14.7 to 4.14.9, FortiGate logs switched from the v6 to the v5 decoder because a prematch regex was fixed (Nov 2026).
   - Quote: "The issue was related to the prematch regular expression used by the fortigate-firewall-v5 decoder"
   - Source: https://groups.google.com/g/wazuh/c/1shFwfPmWE4
   - Confidence: medium
3. After upgrading to 4.14.1, the Windows 10 CIS SCA policy failed to parse (first post Nov 18, 2025); a reply in the thread (Nov 20) reproduced the error, and a later reply (Nov 24) said 4.14.2 would include the fix. Latest status on the page: not marked resolved; fix expected in 4.14.2.
   - Quote: "Failed to load YAML document in /var/ossec/ruleset/sca/cis_win10_enterprise.yml:201" / "We will release 4.14.2 soon, which includes this fix."
   - Source: https://groups.google.com/g/wazuh/c/SuwsRnZjbSw
   - Confidence: medium (one forum thread; the page does not show the role of the repliers who reproduced it and announced the fix)
4. After upgrading to 4.14.5, a Windows Active Response script stopped terminating processes; the thread had no replies other than the author's follow-ups (Jul 2026).
   - Quote: "the Active Response no longer suspends or terminates the unauthorized application"
   - Source: https://groups.google.com/g/wazuh/c/EVdyYgBD_fg
   - Confidence: low
5. After an in-place upgrade 4.10.3 to 4.14.5, the dashboard showed workers offline; a responder could not reproduce it on a rerun (Jun 2026).
   - Quote: "I ran the upgrade again, replicating your environment, and everything worked correctly."
   - Source: https://groups.google.com/g/wazuh/c/3Z9v4whEaAo
   - Confidence: low
6. A user on 4.5 all-in-one asked how to upgrade (Oct 2026); the reply gave the order indexer, manager, dashboard, agents and advised backups and reviewing breaking changes.
   - Quote: "now planning to upgrade to latest version"
   - Source: https://groups.google.com/g/wazuh/c/YiD3GGMpCho
   - Confidence: medium

## Inference
- Inference: users running custom decoders, rules and integrations cannot easily predict what an upgrade
  will change. A pre-upgrade impact check (diff of ruleset, test logs against new decoders) is a plausible need.

## Open questions
- No data on what share of users stay on old versions.

## Changes after verification
- Claim 1: the count of 12 could not be reproduced; changed to an explicit list of 10 titles re-read on the search page; year marked as inferred; dates marked as last-activity dates; confidence lowered from high to medium.
- Claim 3: "Wazuh staff reproduced it and planned a fix" replaced by "a reply reproduced it and a later reply said 4.14.2 would include the fix" (the page does not show those repliers' roles); added the 4.14.2 quote and the latest status shown; confidence lowered from high to medium.
- Claim 7 (performance-counter events on 4.14.1): dropped; the thread does not mention an upgrade, so it does not support this note's topic.
- Main session, after second verification: Claim 1: date range corrected to the 10 counted threads (Jun 10 to Nov 2); Jun 5 to Nov 6 is the span of all 30 results.
