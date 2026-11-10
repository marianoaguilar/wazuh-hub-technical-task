---
title: GitHub issues and discussions on writing custom rules and decoders
url: multiple, see claims
publisher: GitHub (wazuh organisation)
source_type: github
wazuh_version: 4.7 (main issue); others not stated
accessed: 2026-11-10
question: What problems do Wazuh users report on GitHub?
---

## Summary
Users ask on GitHub how to parse fields that built-in decoders do not extract, how to scope rules
by agent label or per agent, and how to do numeric comparisons in rules. In one long thread, a
commenter badged "Member" says the Windows eventchannel decoders cannot be modified and that the
version allowing this customisation will be 5.0. Signals here are moderate (comment counts, few
reactions).

## Claims
1. "MSSQLSERVER- data parsing" (#21706): open, opened Feb 2, 2024, label reporter/community, 26 comments, no reactions visible; version 4.7.0-1. The user cannot get username, database and client IP decoded.
   - Quote: "The data appears in the log, but it is not decoded to be able to use it."
   - Source: https://github.com/wazuh/wazuh/issues/21706
   - Confidence: high

2. In #21706 a commenter badged "Member" proposed a regex decoder tested in wazuh-logtest. The reporter replied that it would not help because the events use the windows_eventchannel decoder. The same Member then wrote (Mar 25 and Mar 28, 2024) that windows_eventchannel decoders cannot be modified because they are part of the code, and that customisation will come in 5.0.
   - Quote: "The decoders that are from `windows_eventchannel` cannot be modified, this is because the decoder is part of the code." / "The version that will allow this customization will be the 5.0."
   - Source: https://github.com/wazuh/wazuh/issues/21706
   - Confidence: medium (summary of the thread)

3. A broad free-text search of `wazuh/wazuh` issues (query `label:module/ruleset OR logtest OR decoder reporter/community`) returns 1347 results, many of them not about rules or decoders; examples of parsing problems on the list sorted by comments are "Unable to parse Cisco FTD logs and alerts not generated" (#7056, 24, closed Feb 10, 2021), "Creating custom decoders and rules from scratch for log" (#5448, 20, closed Jul 31, 2020) and "Add a decoder for Ubiquiti devices" (#23516, 20, open, opened May 18, 2024).
   - Quote: "Creating custom decoders and rules from scratch for log"
   - Source: https://github.com/wazuh/wazuh/issues?q=is%3Aissue+label%3Amodule%2Fruleset+OR+logtest+OR+decoder+reporter%2Fcommunity+sort%3Acomments-desc
   - Confidence: medium (search list; the number is the comment count; several items are older than 2 years)

4. Top-voted GitHub Discussions include rule-writing questions: "Working with cdb lists for each agent" (#31088, Q&A, Jul 24, 2025, 6 votes, 2 comments, answered) and "Numerical comparison in Wazuh Rules" (#20696, Q&A, Dec 11, 2023, 4 votes, 2 comments, unanswered).
   - Quote: "Numerical comparison in Wazuh Rules"
   - Source: https://github.com/wazuh/wazuh/discussions?discussions_q=sort%3Atop
   - Confidence: medium (discussion list page only)

5. Using agent labels in custom rules was requested from 2019 (#3130, 17 comments, 18 thumbs-up) and closed as not planned in Jun 2023; users fall back to hostname matching or CDB lists.
   - Quote: "it's not possible to use labels inside rules."
   - Source: https://github.com/wazuh/wazuh/issues/3130
   - Confidence: high

6. For a built-in false positive (Sysmon rule 92214, #20317, 6 thumbs-up), the only workaround offered in the thread is a hand-written custom rule.
   - Quote: "A new LNK file appears with every open office file."
   - Source: https://github.com/wazuh/wazuh/issues/20317
   - Confidence: medium

## Inference
- Inference: writing decoders for new log sources and overriding built-in rules is a skill users
  lack; questions are answered one by one in threads. A tool that drafts and tests decoders/rules
  against sample logs (like wazuh-logtest, but guided) addresses a real need, though GitHub shows a
  moderate frequency; the forum likely shows more.
- Inference: the 5.0 engine change may change the rule/decoder format, which matters for any tool
  built on the 4.x XML format.

## Open questions
- The format of rules/decoders in Wazuh 5.0: not checked in this note.

## Not read
- https://github.com/wazuh/wazuh/discussions/31088, https://github.com/wazuh/wazuh/discussions/20696, https://github.com/wazuh/wazuh/issues/23516: seen only in list pages.

## Changes after verification
- Summary: "a maintainer" changed to "a commenter badged Member" (role shown on the page, re-fetched 2026-11-10); 5.0 wording aligned with the quote.
- Claim 2: replaced the reporter's quote with the Member's two statements; the "did not apply" objection now attributed to the reporter (re-fetched). Confidence unchanged (medium).
- Claim 3: 1347 described as the result count of a broad free-text query, many results not about rules/decoders; "among the most commented" replaced with "examples on the list sorted by comments".
- Claim 6 (optional fix): "needs" softened to "the only workaround offered in the thread".
