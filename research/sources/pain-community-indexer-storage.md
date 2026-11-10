---
title: Wazuh mailing list threads and PeerSpot reviews on indexer disk usage, retention and resource limits
url: multiple, see claims
publisher: Wazuh mailing list (Google Groups); PeerSpot
source_type: forum
wazuh_version: 4.11 to 4.14.6 (per thread, see claims)
accessed: 2026-11-10
question: What do Wazuh users complain about or ask for help with, outside GitHub?
---

## Summary
A recurring operational complaint is that the Wazuh indexer (OpenSearch) grows until disks fill,
small all-in-one installs degrade over time, and retention must be managed by hand with Index State
Management (ISM) policies. Replies in the threads (the pages do not show the repliers' roles) give
the same advice each time: ISM retention, fewer replicas on single nodes, disabling archives, more disk or more nodes.
PeerSpot reviewers echo storage and maintenance load.

## Claims
1. Frequency signal: a group search for "disk space indexer" (first 30 results) returned 6 threads whose titles are about disk or storage growth, with last-activity dates from Jan to Aug (2026): "Wazuh Indexer High Disk Usage" (7 posts), "GB's of data in /queue/indexer/wazuh-states-vulnerabilities-wazuh_cluster/" (2), "Wazuh manager's system disk overload" (4), "Folder /var/ossec/queue/indexer/wazuh-states-vulnerabilities-wazuh with high disk space" (5), "Wazuh quickstart works initially but dashboard loses events over time on small single-node setup (disk pressure?)" (6), "Indexer Storage Usage Increasing in Wazuh" (4).
   - Quote: "Wazuh Indexer High Disk Usage" (thread title)
   - Source: https://groups.google.com/g/wazuh/search?q=disk%20space%20indexer
   - Confidence: high (titles and counts on the page; the tally is mine; search results are a snapshot taken on 2026-11-10)
2. A user on 4.14.6 found the indexer directory at 1.3 TB (first post Aug 24, 2026); the advice was ISM rollover/deletion policies (which apply automatically to indices created after the policy exists, while existing indices need the policy applied manually), and not to delete directories on disk.
   - Quote: "Do not remove the indices directory."
   - Source: https://groups.google.com/g/wazuh/c/pU-OC2D0n_M
   - Confidence: medium
3. On a small single-node install (4 vCPU, 8 GB RAM, 38 GB disk, 2-3 agents; first post Jan 5, 2026) the quickstart worked at first, then the dashboard lost events as OpenSearch hit disk watermarks; a reply in the thread called this expected for small single-node setups, and a later reply said there is no HIDS-only mode without the indexer.
   - Quote: "this behaviour is expected in small, single-node Wazuh deployments and is not the result of a simple misconfiguration."
   - Source: https://groups.google.com/g/wazuh/c/afBxk9gpHZI
   - Confidence: medium
4. A user saw indexer data grow to about 68 GB even after slowing the vulnerability feed update (first post Jan 12, 2026); the reply listed deleting old indices and agents, retention policies, zero replicas on single nodes, or adding nodes.
   - Quote (reply, Jan 13, 2026): "You need to do all these steps to resolve the storage issue."
   - Source: https://groups.google.com/g/wazuh/c/AfvaXspKhyI
   - Confidence: low
5. On 4.14.1 (Feb 2026), the vulnerability-states queue folder grew to about 40% of /var/ossec because the indexer cluster was red.
   - Quote: "The problem was resolved. The cluster was in red status for a problem with one worker."
   - Source: https://groups.google.com/g/wazuh/c/dniDd0NTEvM
   - Confidence: low
6. After changing ISM retention and indexer passwords, a primary indexer would not start (first post Dec 10, 2025; 14 posts in listing); the thread shows no confirmed fix in the visible content.
   - Quote: "the primary indexer is failing to load"
   - Source: https://groups.google.com/g/wazuh/c/q8O56OZ2xkQ
   - Confidence: low
7. A reply to a post-install question recommends JVM heap tuning, one primary shard on single nodes, ILM deletion policies and proactive resource monitoring (Jan 2026).
   - Quote: "To avoid running out of resources, I recommend monitoring server resource usage proactively."
   - Source: https://groups.google.com/g/wazuh/c/IvBhJiYuIpQ
   - Confidence: low
8. PeerSpot reviewers report storage and maintenance load: one (Dec 24, 2025) reports about twelve outage tickets in a year due to storage; one (Jun 3, 2025) reports indexer timeouts; one (Jul 10, 2024) needs two people to maintain it. PeerSpot shows 51 reviews, 3.7/5.
   - Quote: "In one year, we faced about twelve tickets regarding the system going down due to storage issues." / "The indexer frequently times out, requiring system restarts."
   - Source: https://www.peerspot.com/products/wazuh-reviews
   - Confidence: low (single reviews each)

## Inference
- Inference: running and sizing the indexer is a repeated self-hosting burden, especially for small
  teams on all-in-one installs. This is a need a managed service or a sizing/health assistant could serve.

## Open questions
- Listing dates are last-activity dates; first-post dates come from opened threads.
- Google Groups shows no vote counts; some thread pages show a view count (e.g. the claim 6 thread shows "133 views"), listings do not.

## Changes after verification
- Summary: "Replies from Wazuh staff and community members" changed to "Replies in the threads"; no cited page shows a poster's role.
- Claim 1: added that the search results are a snapshot from 2026-11-10 (optional fix).
- Claim 2: reworded the ISM point to match the page (automatic for new indices, manual for existing ones); re-fetched.
- Claim 3: "a Wazuh representative" changed to "a reply in the thread"; the re-fetched page shows no title, badge or affiliation.
- Claim 4: quote replaced; the old quote was the original poster's words, the new one is from the Jan 13, 2026 reply (re-fetched).
- Claim 7: "A community reply" changed to "A reply"; the page does not show the replier's role.
- Note: `source_type: forum` also covers PeerSpot (a review site); left as is (minor, flagged by the report).
- Main session, after second verification: Open questions: corrected the statement that Google Groups has no view counts (the claim 6 thread page shows one).
