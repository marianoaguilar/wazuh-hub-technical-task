---
note: research/sources/pain-community-alert-tuning.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | The search page lists 30 results. All 9 named threads appear with the stated post counts: fine tuning (6, Feb 25), Silencing (4, 10/2/25), supress (4, May 29), webshell (10, Feb 2), Fix False Positive (3, Jan 20), Event ID 4625 (8, Aug 26), FIM ignore (2, Jul 1), Frequent File Changes (3, Apr 1), Disk usage (3, Jan 15). The range Oct 2025 to Aug 2026 matches. The new caveats (last-activity dates, inferred year) are accurate. |
| 2 | SUPPORTED | First post Feb 19, 2026, about rule 11201 (only the first hit per srcip/destination should alert). A Feb 19 reply says "no easy way to enrich an already created alert using the rule engine". The quote is in the Feb 25 reply. |
| 3 | SUPPORTED | Thread "Silencing alerts for the same user or same srcip...", Oct 2, 2025. The level-0 suppression rule did not work. The reply contains the exact quote and advises level 1 plus `<no_log>`. |
| 4 | SUPPORTED | Jan 16, 2026, Laravel app. The quote is exact (Jan 23 reply). The fix rewrote rules 100500/100501/100502/100520 (100510 was also changed), and the user confirmed it worked on Jan 25. The only FIM `<ignore>` entry is for a Windows uniagent path in a side question (Jan 19), as the note now says. |
| 5 | SUPPORTED | First post Sep 3, 2026: 24 techniques against a default install, 3 alerted. Another participant asked for the version and noted the 15-25 s window vs FIM's 12-hour scan. The original poster wrote "the 3-of-24 is not reproducible from anything we have published" (Sep 3). The Sep 6 re-run on wazuh-manager 4.14.7-1 used 4 techniques, and "out-of-the-box only one fired at attack time". Two misses were blamed on the FIM 12-hour scan and one on no audit rules loaded. |
| 6 | SUPPORTED | Thread "Stock Wazuh loads no audit rules...", Sep 6-14, 2026, 4.14.7-1. The original post says a stock install loads no audit rules. A reply narrows this: only the watch/syscall rules (80780-80792) that match `audit.key` are affected, while the `audit.type` rules still fire. The note's "audit.key-based rules" wording fits that narrower scope. The localfile block is added only if audit.log exists at install time, so install order matters. A later post adds that the file's existence is the actual condition. The quote is verbatim (Sep 14). |
| 7 | SUPPORTED | First post Aug 13, 2026, with 13 attack categories (counted again). The quote is verbatim in an Aug 13 reply. |
| 8 | SUPPORTED | Thread "Next steps after Wazuh installation and agent onboarding", first post Jan 13, 2026. The quote is verbatim in a Jan 15, 2026 reply. No role is shown, so "community answer" fits. |

## Note-level problems
- Confidence value: claim 6 uses `low-medium`, which is not an allowed value. Only `high`, `medium` or `low` are allowed.
- Front matter: complete (`url: multiple, see claims` is valid; every claim cites its own URL).
- Role attributions: none in the note, which is correct. On all 8 pages no poster is labelled Wazuh staff (no label, badge or Wazuh affiliation).
- Confidence otherwise fits. Claim 1 is `high` on a search listing, which is acceptable because the note says the classification and tally are the researcher's.
- Inference is kept separate. Personal data: none (poster names on the pages were not copied). Language: English.

## Recommended fixes
- Claim 6: change the confidence to `low` (one community thread, no staff confirmation, scope narrowed within the thread) or `medium`. `low` is the better fit.
- Optional, claim 6: say that the localfile block depends on whether audit.log exists at install time (in practice, the install order), as the thread concludes.
