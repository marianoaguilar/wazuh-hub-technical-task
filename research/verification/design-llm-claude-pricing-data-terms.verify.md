---
note: research/sources/design-llm-claude-pricing-data-terms.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Pricing table rows match: Opus 5.5 $4/$20, Opus 5 $5/$25, Sonnet 5.5 $2/$10, Sonnet 5 $2/$10, Sonnet 4.6 $3/$15, Haiku 5.5 $0.10/$0.50 (up to 100k) and $0.50/$2.50 (over 100k), Haiku 4.5 $1/$5, Fable 5.2 $8/$40. |
| 2 | SUPPORTED | Footnotes: 0.025x on Fable 5.2/Mythos 5.2/Fable 5.1/Mythos 5.1; 0.05x on Opus 5.5 and Sonnet 5.5; 0.1x general. |
| 3 | SUPPORTED | "The Batch API allows asynchronous processing ... with a 50 percent discount on both input and output tokens."; "Batch API and prompt caching discounts can be combined." |
| 4 | SUPPORTED | "Claude 4.7 and later models ... This tokenizer produces approximately 30% more tokens for the same text." |
| 5 | SUPPORTED | Privacy article: "By default, we will not use your inputs or outputs from our commercial products" (API is included); exceptions feedback and opt-in. |
| 6 | SUPPORTED | API retention page: "Retained data is never used for model training without your express permission." |
| 7 | SUPPORTED | Privacy article: delete "within 30 days of receipt or generation"; exceptions Files API, agreed terms such as ZDR, Usage Policy enforcement, legal compliance. |
| 8 | SUPPORTED | "Conversation content (your prompts and Claude's outputs) is not retained by default; the exception is Covered Models, which require 30-day retention." |
| 9 | SUPPORTED | ZDR text, sales contact, per-organization; ZDR organizations cannot call the API from a browser (CORS). |
| 10 | SUPPORTED | Fable 5.2, Mythos 5.2, 5.1, Fable 5, Mythos 5 designated Covered Models; "ZDR is therefore not available for any of them unless expressly authorized by Anthropic." |
| 11 | SUPPORTED | Current limitations: inference geo only "us" and "global"; workspace geo only "us". Pricing section: 1.1x for US-only inference on Claude 4.6 and later. |
| 12 | SUPPORTED | Opening paragraph: on Claude Models on Google Cloud (Google managed) and Amazon Bedrock the cloud provider is the data processor. |
| 13 | SUPPORTED | Model IDs `anthropic.claude-opus-5-5`, `-sonnet-5-5`, `-haiku-5-5`, `-haiku-4-5`; eight EU regions with Global, EU endpoint types; "Regional endpoints carry a 10 percent pricing premium over global endpoints" with inference profiles (US, EU, JP, AU). |
| 14 | PARTIAL | The AWS compatibility page confirms Sonnet 5.5 and Haiku 5.5 in all eight EU regions with Geo and Global supported and in-Region not supported. The Claude Opus 5.5 rows, including the claimed exception (in-Region on bedrock-runtime in eu-west-2), were not visible in the tool output, so they could not be confirmed. The page is about 729k characters and was read through a summariser. |
| 15 | SUPPORTED | Cross-Region inference page table: geographic "Within geographic boundaries (such as US, EU, and APAC)"; global "Approximately 10% savings", routed worldwide. |
| 16 | SUPPORTED | Data protection page: "Because the model providers don't have access to those accounts, they don't have access to Amazon Bedrock logs or to customer prompts and completions." |
| 17 | SUPPORTED | Data retention page: modes none/default/aws_review; Fable 5/5.1/5.2 require `aws_review` (retained up to 30 days, reviewed by AWS, not shared with provider); Opus 4.8 allows `none`; with cross-region inference, retained data is stored in the destination Regions. |

## Note-level problems
- Claim 14: the Opus 5.5 EU rows and the London exception are unverified; the note already flags the page was read in chunks, but states the exception as fact.
- Inferences are labelled; the Batches-not-supported-on-Bedrock remark is correct (Features not supported lists Message Batches). Front matter complete. No personal data. English.

## Recommended fixes
- Claim 14: drop the "exception: Opus 5.5 in-Region on bedrock-runtime in eu-west-2 London" or re-read the Opus 5.5 table; limit the claim to Sonnet 5.5 and Haiku 5.5 until confirmed.
