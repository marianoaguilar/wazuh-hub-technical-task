---
title: Wazuh's own AI/LLM work (docs, blog PoCs, 5.0 AI Assistant)
url: multiple, see claims
publisher: Wazuh Inc. (documentation.wazuh.com, wazuh.com/blog, github.com/wazuh)
source_type: official-docs (claims 1-2, 8-11); blog (claims 3-7, Wazuh blog); github (claim 12)
wazuh_version: 4.12 to 4.14 (blog/PoC), 5.0 pre-release docs (AI Assistant; "rc" comes only from the URL path)
accessed: 2026-11-10
question: What already exists to help Wazuh users, especially with AI? (Wazuh's own AI/LLM work)
---

## Summary
Wazuh has published several AI/LLM examples for self-hosted users: an official proof-of-concept guide that enriches YARA alerts with ChatGPT, and blog posts that add a chatbot over archived logs (local Llama 3), a Claude 3.5 Haiku chat box in the dashboard (OpenSearch Assistant + Amazon Bedrock) and an agentic threat-hunting app (local Qwen3). None of these is a shipped 4.x product feature; they are do-it-yourself guides. The upcoming Wazuh 5.0 (pre-release docs marked "an upcoming release that is still under development"; not yet in the stable release notes) documents a built-in dashboard "AI Assistant" where the admin brings an OpenAI-compatible or Anthropic provider. Wazuh Cloud's AI Analyst is covered in `landscape-wazuh-commercial-hub.md`.

## Claims
1. Official PoC guide (documented integration, not a product feature): Wazuh documents a proof of concept that combines FIM, a YARA active-response script and ChatGPT to explain detected malware.
   - Quote: "we integrate Wazuh with YARA to detect when a malicious file is added to a monitored endpoint"
   - Source: https://documentation.wazuh.com/current/proof-of-concept-guide/leveraging-llms-for-alert-enrichment.html
   - Confidence: high
2. In that guide the ChatGPT answer is stored in the alert in a field named `yara.chatgpt_response`, and the prompt asks for impact and mitigation. The page has no explicit version label; it appears to be the 4.14 docs because its sample download URLs point to the `4.14` branch.
   - Quote: "In one paragraph, tell me about the impact and how to mitigate"; sample URL "https://raw.githubusercontent.com/wazuh/wazuh-documentation/refs/heads/4.14/resources/samples/mirai"
   - Source: https://documentation.wazuh.com/current/proof-of-concept-guide/leveraging-llms-for-alert-enrichment.html
   - Confidence: high
3. Blog PoC (June 13, 2025, Wazuh 4.12.0): a custom Python script (`threat_hunter.py`) runs Llama 3 locally through Ollama over the Wazuh archive logs and serves a separate chatbot web page, not a dashboard plugin.
   - Quote: "This blog post explores how AI can enhance Wazuh threat hunting using large language models (LLMs)."
   - Source: https://wazuh.com/blog/leveraging-artificial-intelligence-for-threat-hunting-in-wazuh/
   - Confidence: high
4. The same post warns that LLM output can be wrong.
   - Quote: "may sometimes provide inaccurate or bad responses"
   - Source: https://wazuh.com/blog/leveraging-artificial-intelligence-for-threat-hunting-in-wazuh/
   - Confidence: high
5. Blog PoC (January 7, 2025, Wazuh version not stated): Claude 3.5 Haiku is added as a chat box in the Wazuh dashboard by installing OpenSearch assistant/ML Commons plugins and a connector to Amazon Bedrock.
   - Quote: "This blog post describes how to integrate the Claude 3.5 Haiku model into the Wazuh dashboard."
   - Source: https://wazuh.com/blog/leveraging-claude-haiku-in-the-wazuh-dashboard-for-llm-powered-insights/
   - Confidence: high
6. Blog PoC (June 4, 2026, Wazuh 4.14.5): an agentic AI app using the local Qwen3 model with tool calling over the Wazuh server API and indexer, with read-only service accounts.
   - Quote: "This blog post demonstrates how to integrate Agentic AI with Wazuh to automate threat hunting tasks"
   - Source: https://wazuh.com/blog/threat-hunting-with-agentic-ai/
   - Confidence: high
7. The agentic post states that results are grounded only in data from the Wazuh server API and the Wazuh indexer API.
   - Quote: "all results produced during an investigation are derived exclusively from data retrieved through the Wazuh server API"
   - Source: https://wazuh.com/blog/threat-hunting-with-agentic-ai/
   - Confidence: high
8. Wazuh 5.0 (pre-release docs): the dashboard documentation describes a built-in AI Assistant with a conversational interface over security data.
   - Quote: "Analysts can ask questions about vulnerabilities, security findings, and agent activity."
   - Source: https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-dashboard/wazuh-dashboard-configurations.html#ai-assistant
   - Confidence: high
9. The 5.0 AI Assistant is bring-your-own-model: the admin configures an OpenAI-compatible service or Anthropic.
   - Quote: "You can configure an OpenAI-compatible service or Anthropic."
   - Source: https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-dashboard/wazuh-dashboard-configurations.html#ai-assistant
   - Confidence: high
10. The 5.0 docs are marked as covering an unreleased version.
    - Quote: "an upcoming release that is still under development"
    - Source: https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-dashboard/wazuh-dashboard-configurations.html
    - Confidence: high
11. The current stable release notes list 4.14.10 (5 November 2026) as newest; 5.0 is not listed.
    - Quote: "4.14.10" ... "5 November 2026"
    - Source: https://documentation.wazuh.com/current/release-notes/index.html
    - Confidence: high
12. The AI Assistant documentation was merged into the 5.0.0 docs branch in August 2026.
    - Quote: "adds documentation for the new _Email_ notification channel and the _AI Assistant_ configuration"
    - Source: https://github.com/wazuh/wazuh-documentation/pull/10033
    - Confidence: high

## Inference
- Inference: For self-hosted 4.x, Wazuh's AI offering is a set of PoC recipes. Each one needs the user to wire scripts, models and credentials by hand. 5.0 will make a natural-language assistant a product feature, so "chat over my Wazuh data" alone will soon be served by core Wazuh.
- Inference: The PoCs cover enrichment of single alerts, Q&A over logs and hunting. None of the pages read covers AI help for writing or testing rules/decoders, tuning noisy rules, or explaining configuration problems.

## Open questions
- UNVERIFIED: whether the 5.0 AI Assistant can call tools/actions or only query data; the page read does not mention tool calls.
- UNVERIFIED: 5.0 general availability date.
- A Wazuh blog post about ChatGPT with Nmap appeared in search results (https://wazuh.com/?p=17592) but was not fetched.

## Not read
- https://www.securityinfowatch.com/cybersecurity/press-release/55297075/wazuh-wazuh-introduces-ai-powered-threat-hunting-using-local-llm-integration (third-party press release, not fetched; official blog read instead)
- https://thehackernews.com/2026/08/wazuh-and-ai-for-enhanced-soc-workflows.html (not fetched)
- LinkedIn posts about 5.0 beta/RC seen in search results (not fetched; personal profiles)

## Changes after verification
- Claim 2: dropped "versioned copies of the same guide exist from 4.9 to 4.14 according to search results" (not on the cited page); the 4.14 attribution now rests on the page's sample download URLs pointing to the `4.14` branch (re-fetched 2026-11-10), quoted. Confidence stays high for the field and prompt.
- Claim 7: added "and the Wazuh indexer API" to match the full sentence on the page (optional fix; re-fetched 2026-11-10).
- Front matter `publisher`: removed "newreleases.io"; no claim cites it.
- Front matter `source_type`: now states the type per claim (official-docs, blog, github).
- Summary and `wazuh_version`: "release candidate" replaced by the page's own wording ("upcoming release that is still under development"); "rc" appears only in the URL path.
- Claims 1, 3-6, 8-12: unchanged (SUPPORTED).
