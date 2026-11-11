# Review: Phase 3 diagrams (D1-D3)

Reviewer role: outside senior engineer, Wazuh Hub team, seeing the diagrams for the first time.
Date: 2026-11-11. Inputs: `diagrams/src/d1-components.mmd`, `d2-triage-request.mmd`, `d3-data-boundaries.mmd`, the rendered PNGs, and `research/phase3-decisions.md` (D1-D8).
Scope: (a) answers the brief bullet, (b) readable without explanation, (c) contradictions, (d) overclaiming labels, (e) missing essentials. Simplicity is a requirement; no finding asks for detail only for completeness. "Web app" and "Analyst" are kept as decided.

## Cross-diagram (applies to all three)

- **should fix: "real names" is ambiguous.** D1 says "removes real names" / "no real names", D2 "real names removed", D3 "no names" / "real names included". A viewer may read "names" as people's names. D2 in the decisions file removes host names, agent names and IPs. Suggested change: use one wording everywhere, for example "host names and IPs replaced by aliases" (D1 connector box and D3 customer box) and "aliases only" on the arrows and in D2 step 1.
- **should fix: "locked apart" overclaims the isolation.** D3 in the decisions file is one shared database with a `tenant_id` and PostgreSQL Row-Level Security, not separate databases. "Each customer locked apart" (D1) and "🔒 customers locked apart" (D3) suggest physical separation. Suggested change: "one database, each customer's rows kept apart by the database" (or, shorter, "customers separated by the database (row-level)").

## D1. Components and data flow

**Verdict:** answers the bullet. It is readable at a glance: the colours, the outbound-only arrow and "proposes, never decides" carry the main message. Only labels need fixing (the cross-diagram points above, plus the ones below).

1. **should fix: the label on the AI arrow says "new findings", but the decisions say new, undecided *groups*.** D5a says only new, undecided groups go to the AI after the rules step. "New findings" suggests raw findings are sent. Suggested change: label the arrow "new groups only".
2. **optional: the second AI use is not visible.** D8 says the AI also writes the reason for each fix-list item, and D2 shows it as step 6. In D1 the only arrow back is "proposal". Suggested change: label the return arrow "proposal / fix-list reasons, checked before saving". This keeps one arrow and adds no box.
3. **optional: email and login providers appear in D2 (📧) and D3 but not in D1.** This is acceptable for simplicity. If you want the three diagrams to match, add one small grey box "Login + email providers" linked to the Web app, with no label. Otherwise leave it out.

## D2. One user request, start to end

**Verdict:** it mostly answers the bullet. The AI calls (🤖) and the human steps (👤) are clearly marked, and the closing note about re-applying decisions is good. Two problems: the "user request" is not named, and the key human step ("confirm or reject the proposal") is hidden behind an example that mixes up the decision types.

1. **should fix: the diagram never says what the user request is.** It opens with "Every 6 hours, no person involved", so a viewer asks "where is the request?". The request ("review the new findings") only appears in a source comment. Suggested change: add a top note "Request: the analyst reviews this week's new findings. Steps 1-7 prepare it in the background." Or change step 8 to "👤 Opens the review (the request)".
2. **should fix: step 9 hides the confirm/reject step and mixes up decision types.** The service's core idea is "AI proposes, a person confirms" (D5a), but no step says "confirms or rejects". The example also answers a "needs context" question with "accepted risk". In the lab kernel/btrfs case, the answer "btrfs not used" makes it a false positive, not an accepted risk. Suggested change: "9. 👤 Answers the question and confirms or changes the proposal → e.g. false positive, or accepted risk (owner + expiry)".
3. **should fix: the AI call count is not honest yet.** The brief asks for *every* AI call. Step 3 is drawn once but runs once per new group. Step 4's "🤖 one retry" is an AI call with no arrow, and D5 in the decisions file only says "otherwise the proposal is discarded" (no retry). Suggested change: write step 3 as "🤖 For each new group: 'Is this a real risk?'". Then either drop the retry (match D5) or keep it and add "one retry" to D5 and PHASE3.md, so that the diagram and the decisions agree.
4. **optional: the AI lane label is "AI · EU", while D1 says "AWS Bedrock · EU".** Suggested change: "AI model · AWS Bedrock EU", the same as D1 and D3.
5. **optional: step 7 sends the email straight from Service to Analyst.** That is fine for simplicity. Only make sure the PHASE3.md text says the email has no vulnerability details, because D3 promises that ("no vulnerability data").

## D3. Where each customer's data goes and who can read it

**Verdict:** a good structure: three zones, each with "Data / Who sees it", and the arrows carry the main rules (outbound only, one customer per question). But the "who sees it" answers are too strong in two places, and one of them contradicts D6. This diagram is the one most likely to be challenged in the meeting.

1. **must fix: "Who sees it: that customer's users, by role" leaves out our own team, which contradicts D6.** D6 says "a weekly random sample of proposals is reviewed by our team". Those proposals contain the customer's (pseudonymised) findings. Operators with database access are also not mentioned. Suggested change: add the line "Our team: a random sample of AI proposals, for quality review (aliases only)" to the Database box.
2. **should fix: the AI box overclaims.** "Processed and not stored; the model maker cannot see it" reads as "nobody sees it". AWS processes the data. The decisions file only says that "a no-retention mode exists" (D5b), so "not stored" holds only if that mode is turned on, and the text should say that it is. Suggested change: "Who sees it: AWS processes it in the EU, not stored (no-retention mode); the model maker has no access".
3. **should fix: "Login and email providers: no vulnerability data" says what they do *not* get, not what they get.** The bullet asks who reads what. They receive user identities (names, email addresses) and the notification emails. Suggested change: "Login and email providers: user accounts and notification emails; no vulnerability data".
4. **optional: "encrypted" is not in the decisions file and is vague.** Suggested change: "encrypted at rest", and add it to PHASE3.md (or drop the word), so that the diagram makes no promise the text does not back.
5. **optional: the strongest privacy point is only implied.** The alias → real name table never leaves the connector (D2). Suggested change: add the line "alias ↔ host name table stays here" to the customer box. It is short, and it explains why the leak in the service zone is "host-7f3a has CVE-X" without saying whose host it is.

## Summary

| Diagram | Must fix | Should fix | Optional |
|---------|----------|------------|----------|
| All (cross-diagram) | 0 | 2 | 0 |
| D1 | 0 | 1 | 2 |
| D2 | 0 | 3 | 2 |
| D3 | 1 | 2 | 2 |
