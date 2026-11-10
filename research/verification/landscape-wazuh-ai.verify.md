---
note: research/sources/landscape-wazuh-ai.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Proof of Concept guide page. The quote is in the use-case intro. FIM, the Active Response module and ChatGPT enrichment are all described. Calling it a documented PoC and not a product feature is correct. |
| 2 | SUPPORTED | The page says `yara.chatgpt_response` holds the ChatGPT insight (the decoder spells it `YARA.chatgpt_response`). The prompt quote "In one paragraph, tell me about the impact and how to mitigate" is in the scripts. The page has no explicit version label, and the sample URL `.../refs/heads/4.14/resources/samples/mirai` is on the page, which backs "appears to be the 4.14 docs". The unsupported "4.9 to 4.14" text was removed. |
| 3 | SUPPORTED | Dated June 13, 2025, uses Wazuh 4.12.0. The quote is on the page. Llama 3 runs through Ollama on the Wazuh server, `threat_hunter.py` reads the Wazuh archives (`archives.json`), and the post serves a browser chat interface on port 8000 (a separate page, not a dashboard plugin). |
| 4 | SUPPORTED | "may sometimes provide inaccurate or bad responses" is on the page. |
| 5 | SUPPORTED | Dated January 7, 2025, and no Wazuh version is stated (only OpenSearch 2.13.0 plugin versions). The quote is on the page. The post installs the assistant and ML Commons dashboard plugins (plus others) and an Amazon Bedrock connector, which gives a chat interface in the dashboard. |
| 6 | SUPPORTED | Dated June 4, 2026, uses Wazuh 4.14.5. The quote is on the page. The post uses local `qwen3:8b` through Ollama with native tool calling over the Wazuh server API and the `wazuh-alerts-*` index, with least-privilege read-only service accounts. |
| 7 | SUPPORTED | The full sentence on the page ends "...derived exclusively from data retrieved through the Wazuh server API and the Wazuh indexer API". The claim now matches it. |
| 8 | SUPPORTED | The 5.0-rc page has an "AI Assistant" section ("conversational interface for exploring security data using natural language"). The quote is on the page. |
| 9 | SUPPORTED | "You can configure an OpenAI-compatible service or Anthropic." is on the page. |
| 10 | SUPPORTED | The banner says the documentation covers "an upcoming release that is still under development." |
| 11 | SUPPORTED | The release notes index lists 4.14.10, dated 5 November 2026, as the newest release. No 5.0 entry appears. |
| 12 | SUPPORTED | PR #10033 "Update Wazuh Dashboard" was merged on August 24, 2026 into base branch `5.0.0`. The quote is in the description (italics markup removed). |

## Note-level problems
- None. The front matter is complete (`url: multiple, see claims`, and every claim cites its own URL). `publisher` now lists only sources that claims cite. `source_type` gives one type per claim, which the caller accepts. The summary and `wazuh_version` use the page's own wording for 5.0. No role attributions are made. High confidence fits: all sources are Wazuh-owned. Inferences and UNVERIFIED items are kept apart from the claims. There is no personal data, and the note is in English.

## Recommended fixes
- None.
