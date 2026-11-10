---
title: Anthropic Claude API prices, data retention and training terms; Claude on Amazon Bedrock in EU regions - topic note
url: multiple, see claims
publisher: Anthropic; Amazon Web Services
source_type: official-docs
wazuh_version: n/a
accessed: 2026-11-10
question: What are the public per-token prices of current Claude models on the Anthropic API, are API inputs/outputs used for training by default, what is the default retention, is zero data retention offered, and are the same models available on AWS Bedrock in EU regions?
---

## Summary
Anthropic's pricing page (accessed 2026-11-10) lists per-model USD prices per million tokens; for example Claude Opus 5.5 is $4 input / $20 output, Sonnet 5.5 $2 / $10 and Haiku 5.5 $0.10 / $0.50 (prompts up to 100k tokens). The Batch API gives 50% off. Anthropic says commercial (API) inputs and outputs are not used for training by default. The privacy center gives a 30-day default deletion window for API inputs/outputs, while the API retention doc says conversation content is not retained by default except for "Covered Models". ZDR is available by agreement, but not for Covered Models. First-party inference geography is only "global" or "us" (no EU option). On Amazon Bedrock, current Claude models are offered in EU regions through the EU geographic cross-region profile, and AWS says model providers do not see prompts or completions.

## Claims
1. Prices are per million tokens (MTok), in USD. Selected rows (base input / output): Claude Opus 5.5 $4 / $20; Claude Opus 5 $5 / $25; Claude Sonnet 5.5 $2 / $10; Claude Sonnet 5 $2 / $10; Claude Sonnet 4.6 $3 / $15; Claude Haiku 5.5 $0.10 / $0.50 (prompts up to 100,000 tokens) and $0.50 / $2.50 (over 100,000 tokens); Claude Haiku 4.5 $1 / $5; Claude Fable 5.2 $8 / $40.
   - Quote: "| Claude Opus 5.5 | $4 / MTok | $5 / MTok | $8 / MTok | $0.20 / MTok<sup>2</sup> | $20 / MTok |" / "| Claude Haiku 5.5 (for prompts up to 100,000 tokens) | $0.10 / MTok | ... | $0.50 / MTok |"
   - Source: https://platform.claude.com/docs/en/about-claude/pricing#model-pricing
   - Confidence: high (prices change; valid on access date)

2. Prompt caching: cache hits cost 0.05x base input on Opus 5.5 and Sonnet 5.5, 0.025x on Fable/Mythos 5.1-5.2, 0.1x on other models.
   - Quote: "Cache hits and refreshes on Claude Opus 5.5 and Claude Sonnet 5.5 are priced at 0.05x the base input price."
   - Source: https://platform.claude.com/docs/en/about-claude/pricing#model-pricing
   - Confidence: high

3. The Batch API gives a 50% discount on input and output tokens, and it can be combined with prompt caching.
   - Quote: "The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens."
   - Source: https://platform.claude.com/docs/en/about-claude/pricing#batch-processing
   - Confidence: high

4. Claude 4.7 and later models use a newer tokenizer that produces about 30% more tokens for the same text.
   - Quote: "This tokenizer produces approximately 30% more tokens for the same text."
   - Source: https://platform.claude.com/docs/en/about-claude/pricing#model-pricing
   - Confidence: high

5. Training: by default Anthropic does not use inputs or outputs from commercial products (which include the API) for training; exceptions are explicit feedback (e.g. thumbs up/down) or opting in.
   - Quote: "By default, we will not use your inputs or outputs from our commercial products" [to train models]
   - Source: https://privacy.claude.com/en/articles/7996868-is-our-data-used-for-model-training
   - Confidence: high

6. The API retention doc states retained data is never used for training without express permission.
   - Quote: "Retained data is never used for model training without your express permission."
   - Source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#how-anthropic-approaches-data-retention
   - Confidence: high

7. Default retention (commercial privacy center): API inputs and outputs are deleted on the backend within 30 days, with exceptions (features with longer retention such as Files API, a separate agreement such as ZDR, Usage Policy enforcement, legal requirements).
   - Quote: "we automatically delete inputs and outputs on our backend within 30 days of receipt or generation."
   - Source: https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data
   - Confidence: high

8. The API retention doc says conversation content is not retained by default, except Covered Models which require 30-day retention.
   - Quote: "Conversation content (your prompts and Claude’s outputs) is not retained by default; the exception is Covered Models, which require 30-day retention."
   - Source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#how-anthropic-approaches-data-retention
   - Confidence: medium (the wording differs from claim 7; see Open questions)

9. Zero data retention (ZDR) is offered per organization by arrangement with Anthropic sales; under ZDR prompts and responses are not stored at rest after the response is returned. ZDR organizations cannot call the API directly from a browser.
   - Quote: "Under a ZDR arrangement, Anthropic does not store customer prompts or responses at rest after the API response is returned. To request ZDR for your organization, contact the Anthropic sales team."
   - Source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr
   - Confidence: high

10. Covered Models (Claude Fable 5.2, Mythos 5.2, Fable 5.1, Mythos 5.1, Fable 5, Mythos 5) require 30-day retention, so ZDR is not available for them unless expressly authorized.
    - Quote: "are designated Covered Models ... and require 30-day data retention; ZDR is therefore not available for any of them unless expressly authorized by Anthropic."
    - Source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements
    - Confidence: high

11. First-party data residency: `inference_geo` supports only "global" (default) and "us"; workspace geo (storage at rest) is only "us". US-only inference costs 1.1x on Claude 4.6 and later models.
    - Quote: "Inference geo: Only "us" and "global" are available." / "Workspace geo: Only "us" is currently available."
    - Source: https://platform.claude.com/docs/en/manage-claude/data-residency#current-limitations
    - Confidence: high

12. On Amazon Bedrock (and Google-managed Vertex), the cloud provider, not Anthropic, is the data processor.
    - Quote: "On Claude Models on Google Cloud (Google managed) and Amazon Bedrock, the cloud provider is the data processor"
    - Source: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
    - Confidence: high

13. Anthropic's Bedrock page lists current models on Bedrock (e.g. `anthropic.claude-opus-5-5`, `anthropic.claude-sonnet-5-5`, `anthropic.claude-haiku-5-5`, `anthropic.claude-haiku-4-5`) and EU regions eu-central-1, eu-central-2, eu-north-1, eu-south-1, eu-south-2, eu-west-1, eu-west-2, eu-west-3 with an "EU" endpoint type; regional endpoints carry a 10% premium over global.
    - Quote: "Regional endpoints carry a 10 percent pricing premium over global endpoints. To route across multiple regions within a geography, use an inference profile (US, EU, JP, or AU)."
    - Source: https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock#regions
    - Confidence: high

14. The official AWS regional availability page shows Claude Sonnet 5.5 and Haiku 5.5 supported in all listed EU regions through Geo (geographic cross-Region) and Global inference; in-Region inference is mostly "Not supported". The Opus 5.5 EU rows could not be confirmed by the verifier.
    - Quote: (table rows, e.g. Claude Sonnet 5.5) "eu-central-1 (Frankfurt) | Not supported | Not supported | Supported | Supported"
    - Source: https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html
    - Confidence: medium (very long page read in chunks by a summarising tool; Haiku 4.5 row not reached)

15. AWS: geographic cross-Region inference keeps processing within the geography (e.g. EU); global routes worldwide and is about 10% cheaper.
    - Quote: "Data residency | Within geographic boundaries (such as US, EU, and APAC)" / "Cost | Standard pricing | Approximately 10% savings"
    - Source: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html
    - Confidence: high

16. AWS: model providers have no access to Bedrock logs or to customer prompts and completions.
    - Quote: "Because the model providers don't have access to those accounts, they don't have access to Amazon Bedrock logs or to customer prompts and completions."
    - Source: https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html
    - Confidence: high

17. AWS Bedrock data retention modes: `none` (ZDR), `default`, `aws_review`; Claude Fable 5/5.1/5.2 require `aws_review` (prompts and completions retained in AWS up to 30 days, possible human review by AWS, not shared with the provider); models like Claude Opus 4.8 allow `none`. With cross-region inference, retained data is stored in the destination Region.
    - Quote: "none | Zero data retention. No request or response data is written to durable storage by AWS or shared with the model provider." / "user prompts and completions are retained within the AWS boundary for up to 30 days"
    - Source: https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html
    - Confidence: high

## Inference
- Inference: For an EU-hosted SaaS, the Anthropic first-party API cannot pin inference or storage to the EU (only global/us). Bedrock with the EU geographic profile is the documented way to keep inference inside the EU, with retention mode `none` on models that allow it.
- Inference: Triage proposals are not time-critical, so the Batch API (50% off) suits nightly runs on the first-party API; note Anthropic's Bedrock page lists Message Batches as not supported on Claude in Amazon Bedrock.
- Inference: Avoid Covered Models (Fable/Mythos) for customer vulnerability data if ZDR is a requirement.
- Inference: Cost estimate example (to be computed in PHASE3, not a sourced fact): price per finding = (input tokens x input price + output tokens x output price) / 1,000,000.

## Open questions
- The privacy center ("delete within 30 days") and the API retention doc ("not retained by default") use different wording for default retention; the design should state the conservative reading (up to 30 days) unless clarified.
- UNVERIFIED: Bedrock per-token prices for EU regions (https://aws.amazon.com/bedrock/pricing/ not read).
- UNVERIFIED: whether the claude.com/pricing page shows the same numbers as the docs pricing page (not read).
- Haiku 4.5 EU availability on the AWS page not reached in the chunks read.

## Not read
- https://aws.amazon.com/bedrock/pricing/ - not fetched (time budget).
- https://privacy.claude.com/en/articles/7996885-will-anthropic-train-on-my-inputs-and-outputs - fetched, but its wording ("chats or coding sessions") looked aimed at Claude apps rather than the API, so no claim is based on it.
