---
title: AI assistants in other SIEM/XDR products (vendor pages)
url: multiple, see claims
publisher: Microsoft, Google Cloud, Elastic, Splunk
source_type: other
wazuh_version: n/a
accessed: 2026-11-10
question: What already exists to help Wazuh users, especially with AI? (competitor AI assistants)
---

## Summary
All four vendors checked (the researcher's choice of vendors) say they ship AI assistants. Each does natural-language querying (KQL, SPL, YARA-L or Elastic queries) and investigation help; Microsoft, Google and Elastic also mention alert or case summaries. Several now add agents (Google's triage agent, Splunk's Agent Mode, Microsoft's agent ecosystem). Elastic lets customers connect several LLM providers, and Splunk says its Model Runtime picks the model for each prompt (customers can only limit it to Splunk-hosted models, which disables Agent Mode). Everything here is "the vendor says", taken from the vendors' own pages.

## Claims
1. Microsoft says Security Copilot is a generative-AI assistant for incident response, threat hunting, intelligence gathering and posture management, integrated with Defender XDR, Sentinel, Intune, Entra and third-party plugins.
   - Quote: "Security Copilot helps support security professionals in various end-to-end scenarios such as incident response, threat hunting, intelligence gathering, posture management, and more."
   - Source: https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot
   - Confidence: high (vendor docs)
2. Microsoft lists natural-language KQL query building and script analysis as a primary use case.
   - Quote: "Build KQL queries or analyze suspicious scripts"
   - Source: https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot#security-copilot-primary-use-cases
   - Confidence: high
3. Google says Gemini in Google SecOps offers natural-language search, YARA-L rule generation, case summaries, playbook editing and a Triage and Investigation Agent.
   - Quote: "Use a natural language prompt to generate a YARA-L rule."
   - Source: https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle
   - Confidence: high
4. Google says its Triage and Investigation Agent analyzes alerts to determine whether they are true or false positives.
   - Quote: "analyzes security alerts to determine whether the alerts are true or false positives"
   - Source: https://docs.cloud.google.com/chronicle/docs/secops/gemini-chronicle
   - Confidence: high
5. Elastic says its AI Assistant for Security helps with alert investigation, incident response and query generation. Elastic's docs say it can use several LLM providers, including Elastic-managed LLMs, and needs an Enterprise subscription (or specific Serverless tiers).
   - Quote: "assists with tasks such as alert investigation, incident response, and query generation"
   - Source: https://www.elastic.co/docs/solutions/security/ai/ai-assistant
   - Confidence: high
6. Splunk says its AI Assistant turns plain English into SPL and offers an agentic "Agent Mode".
   - Quote: "Transform data analysis from manual, multi-step processes into intelligent agentic workflows."
   - Source: https://www.splunk.com/en_us/products/splunk-ai-assistant-for-spl.html
   - Confidence: medium (vendor marketing page)

## Inference
- Inference: Users switching from or comparing with commercial SIEMs will expect NL search, alert/case summaries and AI-assisted detection-rule writing. Google explicitly ships rule generation (YARA-L). Among the Wazuh sources read, nothing covers AI-assisted Wazuh rule/decoder generation.

## Open questions
- Pricing of these assistants was not collected.
- CrowdStrike Charlotte AI, SentinelOne Purple AI and others were not checked.

## Not read
- https://cloud.google.com/security/products/security-operations (fetch returned only the title)
- https://cloud.google.com/security/products/security-operations/gemini (404)

## Changes after verification
- Claim 4: reworded to "Google says its Triage and Investigation Agent analyzes alerts ..."; it stated a vendor capability as fact.
- Claim 5: reworded to "Elastic says ..."; it stated a vendor capability as fact.
- Summary: "Elastic and Splunk let customers choose or route between LLM providers" replaced; the Splunk page (re-fetched 2026-11-10) says "Model Runtime allows Splunk to determine the best model for each prompt" and that users "can limit the model to only use Splunk-hosted models, but doing so will disable Agent Mode", so Splunk, not the customer, does the routing.
- Summary: "major" removed; the vendor list is now marked as the researcher's choice.
- Claims 1-3 and 6: unchanged (SUPPORTED). No confidence changes.
- Main session, after second verification: Summary: "summaries of alerts and cases" limited to Microsoft, Google and Elastic (the Splunk page does not mention them), wording from the second report.
