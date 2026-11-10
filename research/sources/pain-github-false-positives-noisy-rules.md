---
title: GitHub issues and discussions on false positives and noisy built-in rules
url: multiple, see claims
publisher: GitHub (wazuh organisation)
source_type: github
wazuh_version: 4.5.3 to 4.14 (varies per issue, see claims)
accessed: 2026-11-10
question: What problems do Wazuh users report on GitHub?
---

## Summary
The most reacted bug in `wazuh/wazuh` is a rootcheck false positive ("Trojaned version of file")
that users report across many distributions and versions from 2023 to 2026. Other reports show
built-in rules firing at high levels on normal activity (Sysmon rule 92214 at level 15) and FIM
rule 550 flooding macOS users. Users fix these with their own custom rules or by disabling modules.

## Claims
1. "Trojaned version of file '/bin/diff' detected" (#19346): opened Sep 29, 2023, closed (linked to PR #25634), labels level/task, type/bug; 47 thumbs-up on the original post; 61 comments per the issue list. It is the first result when `wazuh/wazuh` issues are sorted by thumbs-up.
   - Quote: "Trojaned version of file '/bin/diff' detected"
   - Source: https://github.com/wazuh/wazuh/issues/19346 ; https://github.com/wazuh/wazuh/issues?q=is%3Aissue+sort%3Areactions-%2B1-desc
   - Confidence: high

2. In #19346 users on Ubuntu, Debian, Fedora and Pop!_OS report the same false positive across versions 4.5.3 to 4.13.1; some commenters suggest disabling rootcheck/SCA and say such false positives damage trust. The latest visible comment (May 1, 2026, a reply badged "Contributor") says the problem should already be fixed by 4.13.1 and asks whether a new report is a different issue. The issue is closed.
   - Quote: "These types of alarming false positives damage the trustworthiness of the product as a whole." / "Because this here should be already fixed by them 4.13.1 released last year."
   - Source: https://github.com/wazuh/wazuh/issues/19346
   - Confidence: medium (summary of a long thread)

3. A related report for /bin/mail (#20363) is open, opened Nov 21, 2023, no labels, 30 comments, 3 thumbs-up on the original post; versions from 4.6.0 to 4.14. A commenter traced the cause to a signature regex that matches "/dev/null"; the page shows no maintainer reply.
   - Quote: "The Wazuh dashboard reported two files as trojanized - this is a very new system so I was a bit surprised."
   - Source: https://github.com/wazuh/wazuh/issues/20363
   - Confidence: high

4. The search list for "false positive" shows more rootcheck reports of the same false positive: #13278 (closed Oct 4, 2024, 17 on the list), #32142 Debian 13 (closed May 18, 2026, 11 on the list), #32320 Arch (closed May 4, 2026, label "Duplicate", 4 on the list). The search returns 1027 issues.
   - Quote: "False positive on \"Trojaned version of file detected.\" in Debian 13 (Trixie)"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+%22false+positive%22+sort%3Areactions-%2B1-desc
   - Confidence: medium (search list; the list number is the comment count)

5. Sysmon rule 92214 fires at level 15 when Office opens files and creates LNK files. Issue #20317: open, opened Nov 17, 2023, 1 comment, 6 thumbs-up, version 4.6.0. The only reply proposes a custom rule as a workaround.
   - Quote: "Rule 92214 creates maximum-level false-positive alerts when opening office files."
   - Source: https://github.com/wazuh/wazuh/issues/20317
   - Confidence: medium (single report with 6 reactions)

6. GitHub Discussion #23527 (General, May 20, 2024): 4 upvotes, 3 comments, no accepted answer. A user complains about hundreds of FIM rule 550 alerts on macOS; a 2025 reply links them to Time Machine inode changes and suggests `check_inode="no"`.
   - Quote: "I don't want to miss REAL alerts because they get lost in the hundreds of false positives"
   - Source: https://github.com/wazuh/wazuh/discussions/23527
   - Confidence: medium

7. Windows SCA false positive "guest account assumes guest account exists" (#19792) closed Sep 24, 2025 with 74 on the search list (comment count), and a 5.0 report that rule for EventID 5379 fires on normal Windows 11 activity (#39652, open, opened Sep 26, 2026).
   - Quote: "Windows SCA check for guest account assumes guest account exists (false positive)"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+%22false+positive%22+sort%3Areactions-%2B1-desc ; https://github.com/wazuh/wazuh/issues?q=is%3Aissue+%22too+many+alerts%22+OR+noisy+OR+%22alert+flood%22+sort%3Areactions-%2B1-desc
   - Confidence: medium (search lists only; issue pages not read)

## Inference
- Inference: false positives in default content (rootcheck signatures, SCA checks, Sysmon rules)
  are a high-frequency signal: the single most reacted bug is one. Users handle them one by one with
  local overrides; the threads read do not show a shared way to report, track or distribute a fix before a release.
- Inference: few GitHub issues use the words "alert fatigue" directly; the pain shows up as specific
  noisy rules. Forum sources may give a better signal for general tuning pain.

## Open questions
- Whether the rootcheck module is removed in 5.0 (a commenter in #20363 says so and links #30911; not verified).

## Not read
- https://github.com/wazuh/wazuh/issues/19792 and https://github.com/wazuh/wazuh/issues/39652: seen only in search lists.
- https://github.com/wazuh/wazuh/issues/30911: referenced in a comment, not fetched.

## Changes after verification
- Claim 1: comment count changed from "29 visible plus 34 hidden" to "61 comments per the issue list" (report: visible split did not match the page).
- Claim 2: removed "Arch" (only a hostname in #19346; Arch is in #32320); replaced "latest comment says the problem persists" with what the May 1, 2026 comment says (should be fixed by 4.13.1); added the "damage the trustworthiness" quote and the closed state (re-fetched 2026-11-10). Confidence unchanged (medium).
- Claim 4: "duplicates" changed to "reports of the same false positive"; "Duplicate" label kept only for #32320 (report: list marks only #32320 as duplicate).
