---
note: research/sources/landscape-wazuh-commercial-hub.md
verified: 2026-11-10
result: PASS
---

Re-verification after the fixes listed in the note's "## Changes after verification" section.
All cited URLs were fetched again in this session (2026-11-10). The fetch tool's text model could
not decode the two legal PDFs, so the tool saved them as binaries and I read them page by page:
all 8 pages of the Beta Services Terms, and pages 1-5 of the Account Terms, which hold every cited
section. Both PDFs show "Version date: October 8, 2026". The HTML landing pages
(`/legal-resources/wazuh-hub-account-terms-of-use/` and `/legal-resources/wazuh-hub-beta-services-terms/`)
link to these exact PDFs as "Current version" / "October 2026".

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | wazuh.com/cloud/: "Powered by an AI security analyst, it reduces alert fatigue and manual effort..." is on the page. Confidence medium (vendor marketing) fits. |
| 2 | SUPPORTED | wazuh.com/cloud/ pricing table: Small up to 100 agents, 1 month / 3 months, Standard, "Starting at $571/month"; Medium up to 250, "$923/month"; Large up to 500, "$1467/month"; Custom "A service customized to your needs." All figures match. |
| 3 | SUPPORTED | "Enjoy a free 14-day trial" on wazuh.com/cloud/. |
| 4 | SUPPORTED | cloud-service/index.html: "Wazuh Cloud manages the Wazuh central components and their underlying infrastructure" and "remains responsible for security monitoring, investigating alerts, and responding to incidents". Both quotes are on the page. Fixed since the previous report. |
| 5 | SUPPORTED | ai-analyst.html: "provides Wazuh Cloud users with insights into their security posture" plus remediation recommendations; periodic emails; "The AI Analyst report attached as a PDF"; sections Overall assessment, Alert analysis, Vulnerability analysis, Endpoint analysis (top 10 endpoints by alert volume). |
| 6 | SUPPORTED | ai-analyst.html: "Data is processed by AWS Bedrock and Anthropic's Claude model solely within the AI pipeline." (exact). |
| 7 | SUPPORTED | ai-analyst.html FAQ: "Not currently. The service uses predefined parameters optimized for comprehensive security assessment." |
| 8 | SUPPORTED | wazuh.com/services/: the quote is on the page. Plan table: "8/5 (business hours)" vs "24/7 for critical issues", response SLA "8 hours" vs "4 hours", health checks "2 per year" vs "4 per year". The "What you gain" sentence "Improve detection with personalized security rules, dashboards, and third-party integrations." is present, and the claim now correctly presents it as general, not tied to a plan. Fixed since the previous report. |
| 9 | SUPPORTED | Account Terms PDF p.2, section 1.1: "“Wazuh Hub” means the Wazuh ecosystem account and service-access interface currently available at hub.wazuh.com, including the Organization and shared account-level functionality..." |
| 10 | SUPPORTED | Account Terms PDF p.1-2: "Free Service" is defined; "“Service” means a Wazuh product, service, plan or feature made accessible through the Wazuh Hub, excluding Wazuh Cloud and other Wazuh offerings expressly governed by separate terms unless those separate terms incorporate these Hub Terms." |
| 11 | SUPPORTED | Account Terms PDF p.5, section 5.4 "AI-enabled features and automated actions": the quote is verbatim, and the section goes on to cover enabling "automated or response actions". |
| 12 | SUPPORTED | Beta Services Terms PDF p.1: "Version date: October 8, 2026". The section 1.1 "Beta Service" definition contains the quoted list verbatim, introduced by "including, where applicable", as the claim now notes. |
| 13 | SUPPORTED | Beta Terms 1.1: "Free Tier" and "Pro Tier" are each defined as a tier "of Umbra or Argus"; the "Mobius Credits" definition is verbatim; section 3.5 "Usage and metering" covers Mobius Credits consumption. |
| 14 | SUPPORTED | cti.wazuh.com: "Wazuh CTI provides access to a comprehensive database of vulnerabilities, enabling you to quickly identify and address..." |

## Note-level problems
- None.
- Front matter: `title`, `url` (`multiple, see claims`, with each claim citing its own URL), `publisher`, `source_type` and `accessed` are all present. Observation, not a problem: `source_type: official-docs` also covers the vendor's marketing pages (wazuh.com/cloud/, /services/) and the legal PDFs. All are official Wazuh sources, and claim 1 states that it is marketing.
- Confidence levels fit the sources: official docs and legal terms are `high`, and the marketing statement is `medium`.
- Inferences are labelled `Inference:`. The fixed Inference 1 now matches the terms: Mobius is "agentic SOC with response functionality including automatic actions" (Beta Terms 5.4), and Lumen's scope is "not described". The "Vesper" mention is marked UNVERIFIED and is not presented as a claim.
- The Open questions entry about sections 5.1 (Umbra), 5.2 (Argus) and 5.4 (Mobius) now matches the PDF. Note that 5.3 is a general "AI-enabled features" section, not service-specific.
- No role attributions and no personal data. The note is in English.

## Recommended fixes
- None.
