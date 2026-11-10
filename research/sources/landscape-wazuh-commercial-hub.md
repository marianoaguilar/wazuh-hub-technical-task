---
title: Wazuh commercial offer - Wazuh Cloud, AI Analyst, professional support and Wazuh Hub
url: multiple, see claims
publisher: Wazuh Inc. (wazuh.com, documentation.wazuh.com, cti.wazuh.com)
source_type: official-docs
wazuh_version: not stated (Cloud docs pages are in the 4.14 docs tree)
accessed: 2026-11-10
question: What already exists to help Wazuh users, especially with AI? (Wazuh's commercial offer and the Wazuh Hub)
---

## Summary
Wazuh sells a managed Wazuh Cloud with published plans by agent count and retention, a 14-day free trial, and an AI Analyst service that emails periodic AI-generated reports (Amazon Bedrock + Anthropic Claude). It also sells professional support in Standard and Premium plans. A "Wazuh Hub" exists publicly at hub.wazuh.com: Wazuh's legal terms (version date October 8, 2026) define it as an account and service-access interface, and the Hub Beta Services Terms name five beta services (introduced by "including, where applicable"): Pharos (vulnerability and threat intelligence), Umbra (identity risk and dark web), Argus (CSPM), Lumen (AI detection and response) and Mobius (agentic SOC). The product sites and docs for these services could not be read (404 or maintenance pages).

## Claims
1. Wazuh Cloud is a hosted service; the vendor says it includes an AI security analyst.
   - Quote: "Powered by an AI security analyst, it reduces alert fatigue and manual effort,"
   - Source: https://wazuh.com/cloud/
   - Confidence: medium (vendor marketing)
2. Wazuh Cloud publishes fixed plans. Small: up to 100 agents, 1 month indexed and 3 months archive retention, Standard support, from $571/month. The page also lists Medium (up to 250 agents, from $923/month), Large (up to 500 agents, from $1467/month) and a Custom plan.
   - Quote: "Small Up to 100 1 month 3 months Standard Starting at $571/month"
   - Source: https://wazuh.com/cloud/
   - Confidence: high (Small row quoted verbatim; Medium and Large figures are from the same page's table, read through the fetch tool's summary)
3. Wazuh Cloud offers a free trial.
   - Quote: "Enjoy a free 14-day trial"
   - Source: https://wazuh.com/cloud/
   - Confidence: high
4. In Wazuh Cloud, Wazuh manages the central components and their infrastructure; the customer remains responsible for security monitoring, investigating alerts and incident response.
   - Quote: "Wazuh Cloud manages the Wazuh central components and their underlying infrastructure"; "Your team remains responsible for security monitoring, investigating alerts, and responding to incidents."
   - Source: https://documentation.wazuh.com/current/cloud-service/index.html
   - Confidence: high
5. The Wazuh AI Analyst is a Wazuh Cloud service that gives posture insights and remediation recommendations, sent as periodic emails with a PDF report (overall assessment, alerts, vulnerabilities, top 10 endpoints).
   - Quote: "provides Wazuh Cloud users with insights into their security posture and offers recommendations"
   - Source: https://documentation.wazuh.com/current/cloud-service/ai-analyst.html
   - Confidence: high
6. AI Analyst uses Amazon Bedrock and Anthropic Claude.
   - Quote: "Data is processed by AWS Bedrock and Anthropic's Claude model solely within the AI pipeline."
   - Source: https://documentation.wazuh.com/current/cloud-service/ai-analyst.html
   - Confidence: high
7. AI Analyst parameters cannot be customised.
   - Quote: "The service uses predefined parameters optimized for comprehensive security assessment."
   - Source: https://documentation.wazuh.com/current/cloud-service/ai-analyst.html
   - Confidence: high
8. Professional support comes in Standard (8/5, 8-hour response SLA, 2 health checks/year) and Premium (24/7 for critical issues, 4-hour response SLA, 4 health checks/year) plans. Separately, the page's general "What you gain" section (not tied to a plan) lists personalised rules, dashboards and integrations as a benefit of professional support.
   - Quote: "Professional support enhances it further with expert guidance and rapid issue resolution."; plan table rows "8/5 (business hours)" vs "24/7 for critical issues", "8 hours" vs "4 hours"; "Improve detection with personalized security rules, dashboards, and third-party integrations."
   - Source: https://wazuh.com/services/
   - Confidence: high
9. Wazuh Hub is defined in Wazuh's legal terms as the account and service-access interface at hub.wazuh.com.
   - Quote: "“Wazuh Hub” means the Wazuh ecosystem account and service-access interface currently available at hub.wazuh.com"
   - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Account_Terms_October_26.pdf (linked from https://wazuh.com/legal-resources/wazuh-hub-account-terms-of-use/)
   - Confidence: high
10. The Hub terms define Free Services and say Wazuh Cloud is governed by separate terms (not a Hub "Service" unless those terms incorporate the Hub terms).
    - Quote: "excluding Wazuh Cloud and other Wazuh offerings expressly governed by separate terms"
    - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Account_Terms_October_26.pdf
    - Confidence: high
11. The Hub terms anticipate AI features and automated response actions in Hub services.
    - Quote: "Certain Services may use artificial intelligence or machine-learning functionality, including authorized third-party service providers"
    - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Account_Terms_October_26.pdf (section 5.4)
    - Confidence: high
12. The Hub Beta Services Terms (version date October 8, 2026) name five beta services, introduced by "including, where applicable" (so the list gives named examples and may not be exhaustive).
    - Quote: "Vulnerability & Threat Intelligence - Wazuh Pharos (Beta) (“Pharos”), Identity Risk & Dark Web Monitoring - Wazuh Umbra (Beta) (“Umbra”), Cloud Security Posture Management - Wazuh Argus (Beta) (“Argus”), AI Detection & Response - Wazuh Lumen (Beta) (“Lumen”), and Agentic SOC - Wazuh Mobius (Beta) (“Mobius”)"
    - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_October_26.pdf (linked from https://wazuh.com/legal-resources/wazuh-hub-beta-services-terms/)
    - Confidence: high
13. Pricing model in the beta terms: Umbra and Argus have Free and Pro tiers; Mobius is metered with usage credits.
    - Quote: "“Mobius Credits” means Mobius usage credits purchased under a Sales Order or otherwise granted by Wazuh"
    - Source: https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_October_26.pdf
    - Confidence: high
14. Wazuh CTI is a public vulnerability database site.
    - Quote: "Wazuh CTI provides access to a comprehensive database of vulnerabilities"
    - Source: https://cti.wazuh.com/
    - Confidence: high

## Inference
- Inference: The Hub is the umbrella for new SaaS services that sit next to Wazuh (one account, beta services, free/pro tiers, credits). Already-claimed areas include an agentic SOC with response functionality including automatic actions (Mobius), CSPM (Argus), identity/dark-web monitoring (Umbra), vulnerability/threat intelligence (Pharos), and "AI Detection & Response" (Lumen; scope not described in the terms, it could mean AI-powered or AI-focused detection and response). A Phase 2 need should avoid duplicating these.
- Inference: Nothing read shows a Hub service aimed at the self-hosted operator's own platform work (rule/decoder authoring and testing, tuning noisy rules, upgrade/config health). A search snippet mentioned a support assistant called "Vesper", but its pages could not be read, so whether that area is covered is UNVERIFIED.

## Open questions
- UNVERIFIED: what Mobius, Lumen, Umbra, Argus, Pharos actually do in detail. The Beta Services Terms give only category names for Pharos and Lumen; sections 5.1 (Umbra), 5.2 (Argus) and 5.4 (Mobius response functionality) add short service-specific conditions, but no product pages or docs could be read.
- UNVERIFIED: existence and scope of "Vesper" (search snippets describe a Wazuh support assistant that reads the indexer and Wazuh API; it is not named in the Beta Services Terms read).
- Which Wazuh Cloud plans include AI Analyst is not stated on the docs page.
- Consulting and training offers were not read (only navigation links seen).

## Not read
- https://hub.wazuh.com/ and https://hub.wazuh.com/docs (HTTP 404 to the fetch tool)
- https://mobius.wazuh.com/ (maintenance page only), https://docs.mobius.wazuh.com/ and /get-started/what-is-mobius (404)
- https://vesper.wazuh.com/ (maintenance page only), https://docs.vesper.wazuh.com/ and /get-started/what-is-vesper (404)
- https://umbra.wazuh.com/ (404), https://docs.lumen.wazuh.com/collectors/overview (404)
- https://documentation.wazuh.com/current/cloud-service/ai-analyst/index.html (404; the .html page was read instead)

## Changes after verification
- Claim 4: "fully managed by Wazuh" replaced by "Wazuh manages the central components and infrastructure; the customer remains responsible for monitoring, investigation and incident response", with both sentences quoted (page re-fetched 2026-11-10); "fully managed" was broader than the page.
- Claim 8: dropped "both including help with custom rules and integrations" per plan; the page (re-fetched 2026-11-10) lists personalised rules, dashboards and integrations only in a general "What you gain" section, now stated as such. Quotes for the plan-table values added. Confidence stays high (now fully backed).
- Claim 12 and Summary: noted that the list of five beta services is introduced by "including, where applicable" (Beta Terms PDF re-read 2026-11-10, section 1.1) (optional fix).
- Inference 1: removed "alert triage" (Mobius) and "AI-usage security" (Lumen), which the terms do not say; Mobius is now "agentic SOC with response functionality including automatic actions" and Lumen "AI Detection & Response, scope not described".
- Open questions: corrected; the Beta Terms do contain service-specific sections 5.1 (Umbra), 5.2 (Argus) and 5.4 (Mobius), not only category names.
- Claims 1-3, 5-7, 9-11, 13-14: unchanged (SUPPORTED).
