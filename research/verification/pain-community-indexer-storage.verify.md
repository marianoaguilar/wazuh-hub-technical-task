---
note: research/sources/pain-community-indexer-storage.md
verified: 2026-11-10
result: NEEDS FIXES
---

Re-verification after the note's "Changes after verification" section. I re-fetched all eight cited URLs in this session.

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | The search page shows "1-30 of many". All 6 titles appear with the stated post counts (7, 2, 4, 5, 6, 4) and dates Aug 25, Jul 15, Mar 31, Feb 16, Jan 26 and Jan 12. Older entries show "12/30/25", so the year 2026 is implied. The note now says the results are a snapshot. |
| 2 | SUPPORTED | 4.14.6, 1.3T, first post Aug 24 2026, and the advice on ISM rollover/removal are on the page. The page says policies "apply automatically to indices created after the policy is established" and "For existing indices, you will need to apply the policy manually", which the note now matches. The quote "Do not remove the indices directory." is verbatim. |
| 3 | SUPPORTED | The page shows 4 vCPU, 8 GB RAM, a 38 GB root filesystem, 2-3 agents, a first post on Jan 5 2026 and the flood-stage disk watermark. The quote is verbatim (Jan 16 2026 reply). The Jan 26 reply says there is no separate "HIDS-only" deployment mode and that the dashboard depends on a healthy OpenSearch backend. "Without the indexer" is a fair paraphrase of that. The note no longer attributes a role. |
| 4 | SUPPORTED | 68.3G, the feed interval raised from 60 min to 24 h, and the Jan 12 2026 first post are on the page. The replies list deleting agents and old indices, ILM retention, zero replicas on single nodes and adding a node. The quote is verbatim in the Jan 13 2026 reply, as the note now says. |
| 5 | SUPPORTED | v4.14.1, Feb 13-16 2026, the folder at about 40% of /var/ossec, and the verbatim closing quote (Feb 16) are all on the page. |
| 6 | SUPPORTED | The thread "Wazuh Primary Indexer Failed State" has a first post on Dec 10 2025, ISM retention changed from 60 to 45 days, and passwords changed with wazuh-password-tool.sh. The quote is a fragment of "the primary indexer is failing to load _ManagedIndexMetaData_". The group listing shows 14 posts for this title, while the thread page shows only 4 messages. No confirmed fix is visible. |
| 7 | SUPPORTED | "Next steps after Wazuh installation and agent onboarding" (Jan 13-15 2026) has the JVM heap, one-primary-shard, ILM deletion and monitoring advice. The quote is verbatim in the Jan 15 reply. No role is attributed any more. |
| 8 | SUPPORTED | PeerSpot shows 51 reviews and 3.7/5. Both quotes are verbatim, dated Dec 24 2025 and Jun 3 2025. The Jul 10 2024 review says "I need two people to maintain it constantly and to monitor Wazuh". The last ~1.9k characters of the page were not read; this does not affect these findings. |

## Note-level problems
- Open questions: "No view or vote counts exist on Google Groups" is contradicted by a cited page. The thread https://groups.google.com/g/wazuh/c/q8O56OZ2xkQ shows "133 views". This is a small factual error in the note, but it is a factual error.
- Minor, already acknowledged by the researcher: `source_type: forum` also covers PeerSpot, which is a review site. Accepted as is; it does not change the result.
- Roles are fixed: the Summary and claims 3 and 7 no longer attribute staff or community roles. None of the pages shows a role label.
- Front matter is complete, and `url: multiple, see claims` is valid because every claim cites its own URL. The note is in English. The confidence levels (one high, for a direct page tally; medium or low for single threads and reviews) fit the sources. The inference is labelled as inference. No personal data: no poster names, emails or company or mail-server names were copied.

## Recommended fixes
- Open questions: replace "No view or vote counts exist on Google Groups" with something like "Google Groups shows view counts on thread pages (for example, 133 views on q8O56OZ2xkQ) but no votes". Or drop the line.
