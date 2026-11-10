---
note: research/sources/landscape-competitor-ai.md
verified: 2026-11-10
result: NEEDS FIXES
---

Re-check after the fixes listed in the note's "## Changes after verification" section. All four cited URLs were fetched again in this session.

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Microsoft Learn intro: "generative AI-powered security solution"; quote present word for word; integrates with Defender XDR, Sentinel, Intune, Entra "and other third-party services such as ServiceNow and Jamf"; "Plugins from Microsoft and third-party security products" in "How does Security Copilot work?". |
| 2 | SUPPORTED | "Security Copilot primary use cases": "**Build KQL queries or analyze suspicious scripts**: ... with natural language translation". |
| 3 | SUPPORTED | Gemini in Google SecOps page: YARA-L quote present; NL search ("build, edit, and run searches ... using natural language prompts"); case summary widget; "create and edit a playbook with prompts"; Triage and Investigation Agent. |
| 4 | SUPPORTED | Same page: the agent "analyzes security alerts to determine whether the alerts are true or false positives". Now worded as "Google says" (fix applied). |
| 5 | SUPPORTED | Elastic docs: quote present; "can connect to multiple large language model (LLM) providers"; "Elastic Managed LLMs are available out-of-the box"; requires "An Enterprise subscription" or a Serverless project "with the EASE or Security Analytics Complete feature tier". Now worded as "Elastic says" (fix applied). |
| 6 | SUPPORTED | Splunk product page: quote present; "Describe what you want to search in plain English, and the assistant translates it into accurate SPL"; "With Agent Mode enabled, users enter a prompt". |

## Note-level problems
- Previous fixes check out. Claims 4 and 5 now say "Google says" and "Elastic says". The Splunk sentence in the Summary matches the page: "Model Runtime allows Splunk to determine the best model for each prompt" and "Users can limit the model to only use Splunk-hosted models, but doing so will disable Agent Mode." "major" is gone, and the vendor list is marked as the researcher's choice.
- **The Summary still says more than the sources for Splunk (minor).** "Each does natural-language querying ..., summaries of alerts and cases, and investigation help." The cited Splunk page does not mention summaries of alerts or cases. It only mentions "Accelerate investigations using Agent Mode" and "executing searches within the assistant with summarized findings". Elastic mentions alert summaries ("Alert summarization Quick Prompt") but not case summaries. Microsoft ("triage complex security alerts into actionable summaries") and Google (case summary widget) support the summary part. So "each" is broader than the pages say.
- The Inference line ("Among the Wazuh sources read, nothing covers AI-assisted Wazuh rule/decoder generation") refers to other notes and cannot be checked here. It is correctly labelled `Inference:`.
- The front matter is complete (`url: multiple, see claims` is valid; `source_type: other` is accepted). Confidence levels fit the sources (high for vendor docs read as "the vendor says", medium for the Splunk marketing page). No personal data. The note is in English.

## Recommended fixes
- Summary: change "Each does natural-language querying ..., summaries of alerts and cases, and investigation help" to something the pages support, e.g. "Each does natural-language querying (KQL, SPL, YARA-L or Elastic queries) and investigation help; Microsoft, Google and Elastic also mention alert or case summaries."
