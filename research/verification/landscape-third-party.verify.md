---
note: research/sources/landscape-third-party.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | README shows the MIT license and "Supported Wazuh versions: 4.8.0 through 4.14.7.". Tool areas cover alerts, agents, vulnerabilities, compliance and active response. "Read-only by default": the 14 state-changing tools need the `wazuh:write` scope, which is "never granted implicitly". |
| 2 | SUPPORTED | README: "55 tools in 8 toolsets". |
| 3 | SUPPORTED | Re-fetched. "This project is licensed under the MIT License", "A Rust-based server", "A running Wazuh server (v4.12 recommended) with the API enabled and accessible". The named tools cover alerts, agents, vulnerabilities, rules and stats (for example `get_wazuh_alert_summary`, `get_wazuh_running_agents`, `get_wazuh_rules_summary`, `get_wazuh_weekly_stats`). "Compliance Monitoring & Gap Analysis" for PCI-DSS, HIPAA, SOX and GDPR is listed as a capability, and none of the named tools is a compliance tool. The reworded claim matches the page. |
| 4 | SUPPORTED | MIT ("MIT, see LICENSE"), "Agentic SOC for Wazuh built on Strands Agents", "a self-hosted platform", a "13-agent swarm", agents "reach Wazuh only through the Wazuh MCP Server", "Critical actions always need a human". Providers listed: Bedrock, Anthropic, OpenAI-compatible, NVIDIA NIM, vLLM, LiteLLM, Ollama. |
| 5 | SUPPORTED | The exact quote is on the page. Custom integrations: "the name must be any string that begins with `custom-`." |
| 6 | SUPPORTED | Dated October 8, 2025. The page says "Through this integration, Shuffle connects seamlessly with Wazuh to provide out-of-the-box automation for SIEM and XDR use cases." `medium` fits a vendor announcement. |
| 7 | SUPPORTED | Dated April 6th 2022. The exact tested-versions quote is on the page. It uses the custom Python script `custom-w2thive.py`. |

## Note-level problems
- None. Front matter is complete: `url: multiple, see claims` is valid for a topic note, every claim cites its own URL, and the per-claim `source_type` is acceptable. Confidence levels fit the sources. Inferences are labelled, and the first one now points to the notes that source the 5.0 AI Assistant and Mobius. No role attributions. No personal data (GitHub owners appear only in repository URLs). Written in English.

## Recommended fixes
- None.
