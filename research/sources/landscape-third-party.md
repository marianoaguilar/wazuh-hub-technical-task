---
title: Third-party AI and automation on top of Wazuh (MCP servers, agentic SOC projects, SOAR integrations)
url: multiple, see claims
publisher: GitHub projects; Wazuh Inc. (documentation, blog)
source_type: github (claims 1-4); official-docs (claim 5); blog (claims 6-7, Wazuh blog)
wazuh_version: 4.2 to 4.14 (see each claim)
accessed: 2026-11-10
question: What already exists to help Wazuh users, especially with AI? (third-party tools)
---

## Summary
Several open-source MCP servers let AI assistants (for example Claude Desktop) query Wazuh alerts, agents, vulnerabilities and compliance data, and in one case trigger active responses. An open-source "agentic SOC" for Wazuh builds multi-agent triage on top of one of these MCP servers. For automation, Wazuh's integrator natively supports Shuffle (SOAR) and others. Wazuh announced a technology partnership with Shuffle in 2025, and a 2022 Wazuh blog post shows a custom TheHive integration.

## Claims
1. gensecaihq/Wazuh-MCP-Server is an MIT-licensed MCP server for Wazuh with 55 tools (alerts, agents, vulnerabilities, compliance, active response), read-only by default, supporting Wazuh 4.8.0 to 4.14.7.
   - Quote: "Supported Wazuh versions: 4.8.0 through 4.14.7."
   - Source: https://github.com/gensecaihq/Wazuh-MCP-Server
   - Confidence: high
2. The same project exposes 55 tools in 8 toolsets.
   - Quote: "55 tools in 8 toolsets"
   - Source: https://github.com/gensecaihq/Wazuh-MCP-Server
   - Confidence: high
3. gbrigandi/mcp-server-wazuh is an MIT-licensed MCP server written in Rust, recommending Wazuh 4.12, with named tools for alerts, agents, vulnerabilities, rules and stats. Its README lists compliance monitoring and gap analysis (PCI-DSS, HIPAA, SOX, GDPR) as a capability, but none of the tools named on the page is a compliance tool.
   - Quote: "A running Wazuh server (v4.12 recommended)"; "Compliance Monitoring & Gap Analysis for regulatory frameworks like PCI-DSS, HIPAA, SOX, and GDPR"
   - Source: https://github.com/gbrigandi/mcp-server-wazuh
   - Confidence: high
4. gensecaihq/Wazuh-Autopilot is an MIT-licensed, self-hosted multi-agent SOC for Wazuh that works through the Wazuh MCP Server, with human approval for critical actions and support for Bedrock, Anthropic, OpenAI-compatible, NVIDIA NIM, vLLM, LiteLLM and Ollama.
   - Quote: "Agentic SOC for Wazuh built on Strands Agents."
   - Source: https://github.com/gensecaihq/Wazuh-Autopilot
   - Confidence: high
5. The Wazuh integrator natively supports Slack, PagerDuty, VirusTotal, Shuffle and Maltiverse, plus custom integrations.
   - Quote: "The allowed values are `slack`, `pagerduty`, `virustotal`, `shuffle`, `maltiverse`."
   - Source: https://documentation.wazuh.com/current/user-manual/manager/integration-with-external-apis.html
   - Confidence: high
6. Wazuh and Shuffle announced a technology partnership (blog post dated October 8, 2025); the vendor says Shuffle gives out-of-the-box automation for Wazuh.
   - Quote: "Shuffle connects seamlessly with Wazuh to provide out-of-the-box automation for SIEM and XDR use cases."
   - Source: https://wazuh.com/blog/wazuh-and-shuffle-announce-technology-partnership-to-deliver-integrated-security-automation/
   - Confidence: medium (vendor announcement)
7. A Wazuh blog post (April 2022, tested on Wazuh 4.2.5 and TheHive 4.1.18-1) forwards Wazuh alerts to TheHive with a custom Python integration.
   - Quote: "The integration is tested on Wazuh version 4.2.5 and TheHive version 4.1.18-1."
   - Source: https://wazuh.com/blog/using-wazuh-and-thehive-for-threat-protection-and-incident-response/
   - Confidence: high

## Inference
- Inference: "Natural-language access to Wazuh data" and "agentic alert triage" are already crowded. Open-source MCP servers, an open-source agentic SOC, Wazuh's own blog PoCs, the 5.0 AI Assistant (sourced in landscape-wazuh-ai.md) and the Hub's Mobius beta (sourced in landscape-wazuh-commercial-hub.md) all target them.
- Inference: Third-party projects focus on SOC analyst work (alerts, incidents, response). None of those read targets ruleset engineering (decoder/rule authoring, regression testing with logtest, tuning) as its main job.

## Open questions
- Popularity numbers (stars) change over time. They were seen on the pages (268 stars for Wazuh-MCP-Server, 63 for Wazuh-Autopilot) but are not used as claims.
- Not checked: n8n or other workflow templates for Wazuh, and commercial MSSP add-ons.

## Not read
- https://www.atricore.com/blog/wazuh-mcp-server-bridging-siem-data-with-ai-assistants (not fetched)
- https://github.com/ryanyi2/wazuh-agentic-soc (not fetched)
- https://www.neura.market/workflow/wazuh-alert-triage-ai-reporting-with-gpt-4o-mini-telegram (not fetched)
- https://wazuh.com/blog/automating-security-reporting-and-response-with-wazuh-and-shuffle/ (not fetched)

## Changes after verification
- Claim 3: reworded; compliance gap analysis is now described as a capability the README lists (quote added), not as a tool, because the page (re-fetched 2026-11-10) names no compliance tool. Confidence stays high (README of the project).
- Front matter `source_type`: now states the type per claim (github, official-docs, blog) instead of only "github" (optional fix from the report).
- Inference 1: added pointers to the notes that source the 5.0 AI Assistant (landscape-wazuh-ai.md) and Mobius (landscape-wazuh-commercial-hub.md) (optional fix from the report).
- Claims 1, 2, 4-7: unchanged (SUPPORTED).
