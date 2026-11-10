---
note: research/sources/pain-community-upgrades.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | PARTIAL | The search page shows "1-30 of many". All 10 listed titles appear among the 30 results, and every post count matches (FortiGate 2, Upgrade Path 5, EoL Policy 2, Indexer-connector 3, Upgrading agents on Windows 10, Active Response 3, Dashboard workers offline 4, RHEL5 remote upgrade 4, After update wazuh-indexer 2, 4.2.7 upgrade 5). The quoted FortiGate title is verbatim. The two OS-upgrade threads that were excluded ("Issue with cleaning up after OS upgrade", "Old kernel vulnerabilities ... kernel upgraded") are on the page. The year is correctly marked as inferred. Remaining imprecision: the sentence attaches "listing dates Jun 5 to Nov 6" to the 10 counted threads, but those 10 run from Jun 10 ("Wazuh version upgrade from 4.2.7") to Nov 2 (FortiGate). Jun 5 to Nov 6 is the span of all 30 results. (My previous report also gave the range loosely, without saying it covered all 30 results.) |
| 2 | SUPPORTED | Thread "FortiGate Decoder Change After Wazuh Patch Upgrade (v4.14.7 to v4.14.9)", posts dated Nov 2, 2026. Logs were decoded as fortigate-firewall-v6 on 4.14.7 and as fortigate-firewall-v5 on 4.14.9. The quote is verbatim, and the reply explains the prematch fix. |
| 3 | SUPPORTED | Thread "CIS Benchmark for Windows 10 Not working after upgrading agents to v4.14.1". The first post is dated Nov 18, 2025. The error quote is verbatim. Post 6 (Nov 20) reproduces the error, and post 7 (Nov 24) contains "We will release 4.14.2 soon, which includes this fix." The thread is not marked resolved. The claim no longer attributes a role to the repliers, which matches the page (no domain or role is shown for posts 6 and 7). |
| 4 | SUPPORTED | Thread "Active Response \| Working in Older version \| Not Working in Newer Version". It has 3 posts (Jul 1, 2 and 7, 2026), all by the same author. The version is v4.14.5 and the quote is verbatim. |
| 5 | SUPPORTED | The thread title gives 4.10.3 to 4.14.5. The upgrade was an in-place apt upgrade, and the workers showed Offline. Posts are dated Jun 26 to 29, 2026. The quote is verbatim from a reply, and no role is claimed for the responder. |
| 6 | SUPPORTED | Thread "Upgrade Path", Oct 27, 2026. The user runs v4.5 all-in-one, and the quote is verbatim (inside a longer sentence). The reply gives the order indexer, manager, dashboard, agents, recommends a VM snapshot or backups, and says to review the release notes for breaking changes. |

## Note-level problems
- None. The front matter is complete (`url: multiple, see claims` is valid, and every claim cites its own URL). Confidence levels are `medium` or `low`, which fits single forum threads and a self-classified tally. No role is attributed anywhere. The inference is labelled. No personal data is in the note (the cited pages show poster names and wazuh.com addresses, and the note correctly leaves them out). The note is in English. The "Changes after verification" section matches the fixes I recommended previously.

## Recommended fixes
- Claim 1: change "with listing (last-activity) dates Jun 5 to Nov 6" to "Jun 10 to Nov 2" (the dates of the 10 counted threads), or say that Jun 5 to Nov 6 is the span of all 30 results.
