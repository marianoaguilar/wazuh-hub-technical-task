---
title: GitHub issues on upgrades, stability and disk/index storage
url: multiple, see claims
publisher: GitHub (wazuh organisation)
source_type: github
wazuh_version: 4.7 to 4.14 (varies per issue, see claims)
accessed: 2026-11-10
question: What problems do Wazuh users report on GitHub?
---

## Summary
The most commented community issues in `wazuh/wazuh` are upgrade breakages: the 4.8 upgrade
(vulnerability index missing), 4.12 to 4.13 (indexer stops working), and crashes of wazuh-remoted
after 4.13.1. A second cluster is uncontrolled disk growth of the RocksDB indexing queue
(`.sst` files) after 4.8, reaching hundreds of GB. Fixes that users report are often configuration
(certificates, keystore credentials, `/tmp noexec`) that users must find by trial.

## Claims
1. A search for community issues mentioning "after upgrade" returns 361 results; the most commented is "Upgrade to Wazuh 4.8 - Missing indice (wazuh-states-vulnerabilities)" (#24074, 126 on the list).
   - Quote: "Upgrade to Wazuh 4.8 - Missing indice (wazuh-states-vulnerabilities)"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+%22after+upgrade%22+OR+%22after+upgrading%22+reporter%2Fcommunity+sort%3Acomments-desc
   - Confidence: high

2. #24074: opened Jun 12, 2024, closed (completed) Jul 19, 2024, label reporter/community, version 4.8; 27 comments visible plus 99 hidden items; 1 thumbs-up. Causes found by users: wrong certificate paths, host not matching the certificate SAN, missing keystore credentials, a duplicated indexer block in ossec.conf, a vulnerability database that did not extract, indices not green. Some users report the problem after closure.
   - Quote: "Display the message \"Vulnerability detection seems to be disabled or has a problem\""
   - Source: https://github.com/wazuh/wazuh/issues/24074
   - Confidence: high

3. "indexer breaks when upgrading from 4.12 to 4.13" (#32044): open, opened Sep 19, 2025, labels include reporter/community, request/operational, type/bug; 25 comments visible plus 60 hidden items; 0 thumbs-up. Removing `noexec` from `/tmp` and re-entering certificate paths and keystore credentials fixed the problem for individual users. A shard-limit message ("[1000]/[1000] maximum shards open") was found in one user's log; a reply suggested deleting old indices, but no one in the thread confirms this fixed it.
   - Quote: "After following the upgrade guide, wazuh indexer stops working." / "in my case it was because i had noexec on /tmp folder"
   - Source: https://github.com/wazuh/wazuh/issues/32044
   - Confidence: high

4. "Wazuh-remoted (4.13.1/4.14.0) crashing frequently" (#33038): open, opened Nov 6, 2025, labels level/task, reporter/community, request/operational, type/bug; 25 comments visible plus 20 hidden items; 0 thumbs-up on the original post. In Apr 2026 another user reports the same on 4.14.4 with about 8,500 agents; no root cause in the thread.
   - Quote: "process remoted crashes every 1-2 days since upgraded to version 4.13.1, 4.14.0 still has this issue."
   - Source: https://github.com/wazuh/wazuh/issues/33038
   - Confidence: high

5. Other upgrade issues on the same search list: "index_not_found_exception for Vulnerability Detection after attempting upgrade to 4.10" (#27699, 41, closed Feb 5, 2025), "Wazuh-modulesd (4.13.1/4.14.0) crashing frequently" (#32820, 37, closed Oct 31, 2025), "Vulnerability Detection not working after upgrade from 4.9.2 -> 4.10" (#27563, 32, closed Jan 15, 2025).
   - Quote: "Vulnerability Detection not working after upgrade from 4.9.2 -> 4.10"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+%22after+upgrade%22+OR+%22after+upgrading%22+reporter%2Fcommunity+sort%3Acomments-desc
   - Confidence: medium (search list only; numbers are comment counts)

6. "After updating to Wazuh 4.8, disk consumption has become severe." (#24243): opened Jun 21, 2024, closed Aug 25, 2024, label reporter/community, 26 comments, 9 thumbs-up; later comments report the problem up to 4.14. A reply badged "Contributor" (Dec 10, 2024) warned that deleting `.sst` files corrupts the database.
   - Quote: "a large number of .sst files are being created in /var/ossec/queue/indexer/wazuh-states-vulnerabilities-wazuh"
   - Source: https://github.com/wazuh/wazuh/issues/24243
   - Confidence: high

7. "/var/ossec/queue/indexer/wazuh-states-vulnerabilities-wazuh_cluster huge space" (#30476): open, opened Jun 18, 2025, version 4.11.1 (later 4.12.0, 4.13.1), about 20 comments, thumbs-up not shown. The reporter's directory listing shows a total of about 212 GB ("total 212G") with about 246 agents; one other user reports terabytes (about 2.6 TB for the vulnerabilities queue).
   - Quote: "i upgrade from 4.7 to 4.11 and now we have a big problem with .sst files"
   - Source: https://github.com/wazuh/wazuh/issues/30476
   - Confidence: high

## Inference
- Inference: upgrades are a top pain by comment volume (threads of 85-126 items). Most failures are
  in the manager-indexer connection (certificates, credentials, possibly shard limits, index health), which
  a pre-upgrade health check could detect before the upgrade.
- Inference: self-hosted operators lack visibility into internal queue size and indexer backlog;
  disk growth is only noticed when the disk fills.

## Open questions
- Exact comment totals for #24074, #32044, #33038 (part of each thread hidden).
- Whether #34551 (connection-layer issue mentioned in #24243) is still open: not fetched.

## Not read
- https://github.com/wazuh/wazuh/issues/27699, https://github.com/wazuh/wazuh/issues/32820, https://github.com/wazuh/wazuh/issues/27563, https://github.com/wazuh/wazuh/issues/34551: seen only in lists or comments.

## Changes after verification
- Summary: removed "shard limits" from the list of found causes (no confirmed fix in #32044).
- Claim 3: shard limit now described as a log message with no confirmed fix; only `/tmp noexec` and certificates/keystore kept as working fixes; added a quote (re-fetched 2026-11-10).
- Claim 4: "1 thumbs-up" changed to "0 thumbs-up on the original post" (the single 👍 is on an Apr 2026 comment; re-fetched).
- Claim 6: dropped "among the top 25 issues by thumbs-up" (no supporting URL); "a maintainer" changed to "a reply badged Contributor" (role shown on the page, re-fetched).
- Claim 7: "212 GB of SST files" changed to the directory listing total; "other users report terabytes" changed to "one other user" (re-fetched).
- Inference: "shard limits" marked as "possibly", to match claim 3.
