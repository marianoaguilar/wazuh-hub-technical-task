---
note: PHASE3.md
verified: 2026-11-11
result: NEEDS FIXES
---

All web URLs below were fetched in this session. Nothing was reused from other reports except where stated (claims 31 and 32 also cite the design-* reports for context).

## Claims

### Lab files (`research/lab/api/*.json`)
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | "6554 findings": 07 `count` = 6554; 08 `hits.total` = 6554. |
| 2 | SUPPORTED | 105 Critical, 1861 High, 3045 Medium, 587 Low, 956 "-" (no severity) all match 08. The sum is 6554. |
| 3 | SUPPORTED | 2809 packages = `total_affected_items` in 05. |
| 4 | SUPPORTED | Version 4.14.10 = `api_version` in 01. Ubuntu 22.04.5 is in 03 and 09. |
| 5 | SUPPORTED | Critical example in 09: CVE-2026-98959, base 9.8 (v3.1), `scanner.condition` "Package default status", source "Canonical Security Tracker", package `linux-image-6.8.0-138-generic`, kernel `6.8.0-138-generic` (the running kernel), description starts with "btrfs: fix xattr replace...". The JSON block in the note matches 09 field by field (`detected_at`, `published_at`, reference). |
| 6 | SUPPORTED | `libssl3` / `3.0.2-0ubuntu1.30` / source openssl / amd64 / deb match 04. |
| 7 | SUPPORTED | `GET /vulnerability/001` returns "404 - Not Found" (06). |
| 8 | SUPPORTED | "hostname contained a personal name and the laptop model" matches the `_redacted` field of 03. No real name appears in PHASE3. |
| 9 | PARTIAL | "In my lab this package (libssl3) has no finding": the only evidence is `research/sources/lab-api-vulnerability-data.md` item 7, which says "response not saved, shown in chat". No file in `research/lab/api/` backs it, and the cited file 04 does not show it. |
| 10 | SUPPORTED | "~2000 urgent items" = 105 + 1861 = 1966. |

### Internal links
| # | Verdict | Explanation |
|---|---------|-------------|
| 11 | SUPPORTED | All anchors resolve. `phase3-decisions.md#d1` to `#d7` match the headings under GitHub slug rules. `PHASE2.md#the-need-vulnerability-triage`, `#who-would-benefit` and `#risk-i-am-aware-of` match their headings. The files `research/phase3-decisions.md`, `research/verification/phase3-diagrams.review.md`, `research/ai-log.md` (rows 10, 11, 12 exist) and `research/lab/api/` all exist. The D8 anchor is not linked and the D8 text matches the decisions file. |
| 12 | PARTIAL | Tension with the decisions file. "Data is encrypted at rest" and "audited access" (and the support-case exception) appear in PHASE3 (D3 paragraph and the "Data leak" risk row), but D3 in `phase3-decisions.md` says none of them. They are new security promises that the linked decision does not contain. |
| 13 | PARTIAL | "Thousands of findings become a few dozen groups" (D5) contradicts the cost section's "about 300 groups on the first sync". Neither number is measured. |
| 14 | PARTIAL | PHASE3 "Wazuh 4.x has no place to record what was decided" is stated flat. `PHASE2.verify.md` claim 1 rated the same statement PARTIAL (an absence claim stronger than the sources), and PHASE2 itself hedges it ("I found no way"). |
| 15 | PARTIAL | "For whom" repeats three PHASE2 statements that PHASE2 labels `Inference:` (small teams, MSSPs "face the problem once per client", audit teams). PHASE3 drops the label. |
| 16 | PARTIAL | Pharos "has no public description". PHASE2 says only "I found no public page" and "I cannot rule out an overlap". PHASE3 states it more strongly. |

### Web URLs
| # | Verdict | Explanation |
|---|---------|-------------|
| 17 | SUPPORTED | securing-indexer-api.html: "We advise restricting network access to the Wazuh indexer ... to limit the exposure of the Wazuh indexer API to only trusted networks." The page does not say "do not expose to the internet". The statement "pulling would need the indexer exposed" is the author's reasoning. |
| 18 | SUPPORTED | release-4-8-0.html: "Removed `PUT /vulnerability`, `GET /vulnerability/{agent_id}`" plus `last_scan` and `summary/{field}`, with the instruction to use the indexer. |
| 19 | SUPPORTED | rbac/reference.html: `readonly` role "can read all the information of the system"; policies `agents_read_*` and `syscollector_read_*` exist. |
| 20 | SUPPORTED | api/configuration.html: `auth_token_exp_timeout` default 900. |
| 21 | SUPPORTED | user-administration/rbac.html, "Creating and setting a Wazuh read-only user": cluster permission `cluster_composite_ops_ro`, index pattern `*`, index permission `read`. The narrower role is correctly labelled `Inference:` and "not tested". |
| 22 | PARTIAL | how-it-works.html: "Wazuh 4.x documents neither [KEV nor EPSS] in its vulnerability detection". The page does not mention KEV or EPSS. This is an absence claim based on one page. The conclusion "so this ranking adds something new" is an inference with no `Inference:` label. |
| 23 | SUPPORTED | cisa.gov KEV catalog page exists and is the KEV catalog. |
| 24 | SUPPORTED | KEV license.txt: "The KEV database is distributed under the Creative Commons 0 1.0 License." |
| 25 | SUPPORTED | first.org/epss/using-epss: "treat it as actively exploited ... regardless of EPSS score"; "Do not multiply an EPSS score by an ordinal (such as CVSS)". |
| 26 | SUPPORTED | first.org/epss/: EPSS "estimates the probability that a published CVE will be exploited in the wild in the next 30 days" and publishes the score every day. The claim merges two sentences. |
| 27 | SUPPORTED | AWS cross-region-inference.html: geographic profiles (US, EU) keep "data residency within geographic boundaries" and route "within the geography". |
| 28 | PARTIAL | AWS data-retention.html: a mode `none` (zero data retention) exists, but it is per Region and per model (`allowed_modes`). Some models require retention (e.g. Fable 5, up to 30 days). The note hedges with "where the model allows it". The page does not say whether Sonnet 5.5, the model costed in this document, allows `none`. The page also says retained data is stored in the destination Region when cross-region inference is on. |
| 29 | SUPPORTED | AWS data-protection.html: model providers have no access to the Model Deployment Accounts, so "they don't have access to Amazon Bedrock logs or to customer prompts and completions". |
| 30 | SUPPORTED | Anthropic data-residency, "Current limitations": "Inference geo: Only "us" and "global" are available." |
| 31 | SUPPORTED | privacy.claude.com: "By default, we will not use your inputs or outputs from our commercial products" to train models. The page says "commercial products", not "API" explicitly. |
| 32 | SUPPORTED | pricing page: Claude Sonnet 5.5 = $2 / MTok input, $10 / MTok output. The batch discount is "50 percent ... on both input and output tokens" (Sonnet 5.5 batch $1 / $5). Also in `design-llm-claude-pricing-data-terms.verify.md`. |
| 33 | SUPPORTED | claude-in-amazon-bedrock, Regions: "Regional endpoints carry a 10 percent pricing premium over global endpoints." The page says the premium applies to regional endpoints. For EU inference profiles, the AWS page lists geographic cross-region inference as "Standard pricing". PHASE3 marks the EU price as UNVERIFIED, so this is acceptable. |
| 34 | SUPPORTED | Forum thread tq7fgojXObg: PHP 7.4.33 flagged High against a PHP 8.2.35 fixed version, confirmed as a false positive. |
| 35 | SUPPORTED | Forum thread mTUXo6txzTU: Ubuntu kernel CVEs marked resolved after Canonical changed its feed format. |
| 36 | PARTIAL | github #26819: the comment says "Implementing exclusions at the Indexer level is a much cleaner and easier-to-implement solution" and "I'm still not sure which exact 5.x version will include the feature". But the commenter's label on the page is "Member", not "maintainer". PHASE3 and PHASE2 call him "a maintainer". |
| 37 | PARTIAL | github #36000: the issue is "Adapt vulnerability scanner and FlatBuffers schema ... CVE 5.0", closed as completed 2026-05-12, with task lines "Add `metrics.other` support for KEV payloads" and "... EPSS payloads". The page does not confirm that the scanner "parses KEV and EPSS data" (the task boxes show as unchecked). "Plans to support" would fit; "parses" is stronger. The same issue is rated SUPPORTED for the task list in `design-ranking-wazuh-kev-epss-support.verify.md` (claim 6). |

### Arithmetic and prices
| # | Verdict | Explanation |
|---|---------|-------------|
| 38 | SUPPORTED | 3,000 input tokens x $2/M = $0.006; 500 output tokens x $10/M = $0.005; total $0.011 per proposal. 300 x $0.011 = $3.30. About 30 per week x 4.3 weeks = about 130 per month. All consistent. |
| 39 | SUPPORTED | "A few dollars per customer": 130 x $0.011 = about $1.43, plus fix-list explanations. Plausible. The assumptions (100 hosts, 300 and 30 groups, token counts) are labelled "Inference ... not measured". |

## Note-level problems
- Front matter: PHASE3.md is a deliverable, not a research note, and has no front matter (not required).
- **Security promises with no source or decision behind them:** "Data is encrypted at rest", "Our team can read a tenant's data only for the weekly quality sample or a support case, through audited access", and "audited access" in the risk table. Neither `phase3-decisions.md` (D3, D6) nor any cited source contains these. D6 mentions only the weekly sample, not a support-case access or audited access. They must be marked as design commitments (or "Inference:") or added to the decisions file.
- **Unsourced facts without an `Inference:` label:**
  - "`-0ubuntu1.30` means Ubuntu has applied its own security patches (a backport)" and "comparing only 3.0.2 with an upstream fix version is a classic source of false positives". No URL is cited. The forum threads cover similar cases, but this version-scheme claim is not cited.
  - Line 27: the claim that the condition is "not 'installed version lower than the fixed one'" describes other Wazuh conditions and cites nothing.
  - "Our own login is a classic source of bugs" (D4 row) and "hundreds of databases are costly to run" (D3) are opinions, not labelled.
  - "Even with a large margin of error, the AI is not the main cost" is a conclusion from unmeasured assumptions. It sits right after the Inference label but should be labelled.
- **Conditional security statements to double-check:** "Claude models through AWS Bedrock ... with the no-retention mode on where the model allows it" is hedged correctly. AWS states some Claude models require retention (up to 30 days) and that retained data is stored in the destination Region. The sentence "the Wazuh credentials never leave the customer" and "no port is opened" are design properties, not facts about the cited sources, and are fine as design statements.
- No personal data. The agent name and hostname are replaced by placeholders, and the note says that a personal name was in the hostname without giving it. Language: English.
- The "Short answer" names `likely_false_positive` / `real` / `needs_context`, while PHASE2 names "likely false positive / real / accepted risk". It is an evolution, but the difference is not explained.

## Recommended fixes
- Claim 12 / note-level: add encryption at rest, audited access and the support-case exception to `phase3-decisions.md` D3 (or label them "design commitment, not yet researched"). Do not present them as confirmed facts.
- Claim 13: reconcile "a few dozen groups" (line 108) with "about 300 groups on the first sync" (line 157). Label the number as an assumption.
- Claim 36: replace "a maintainer" with "a Wazuh team member (the page shows the label Member)", or say only "a commenter labelled Member". Do the same in PHASE2.
- Claim 37: replace "the 5.0 scanner parses KEV and EPSS data" with "the 5.0 scanner work includes tasks to support KEV and EPSS data (#36000)".
- Claim 22: add `Inference:` before "so this ranking adds something new", and say "the vulnerability detection page I checked does not mention them".
- Claim 9: save the `libssl3` query response as `research/lab/api/` file, or write "I did not save the response".
- Claim 14, 15 and 16: keep the hedging of PHASE2 ("I found no way", "Inference:", "I found no public page") when repeating these statements.
- Add a source or `Inference:` to the `-0ubuntu1.30` backport explanation (line 76) and to line 27's remark about `scanner.condition`.
- Claim 28 (optional): state that the no-retention mode is per Region and per model, and that Sonnet 5.5 support for it was not checked.
