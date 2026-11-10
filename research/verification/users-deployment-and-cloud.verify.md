---
note: research/sources/users-deployment-and-cloud.md
verified: 2026-11-10
result: PASS
---

Re-check after the fixes listed in the note's "## Changes after verification" section. All seven cited URLs were fetched again in this session.

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Quickstart hardware table: 1-25 (4 vCPU, 8 GiB, 50 GB), 26-50 (8 vCPU, 8 GiB, 100 GB), 51-100 (8 vCPU, 8 GiB, 200 GB) for 90 days. The quote is on the page. The install script is fetched from packages.wazuh.com/4.14/, which matches the front matter. |
| 2 | SUPPORTED | Architecture page: single-node is "Recommended for medium environments that require higher performance than an all-in-one setup."; multi-node: "This deployment is recommended for large environments with high event throughput". |
| 3 | SUPPORTED | Deployment options index lists VM image (OVA), AMI, Docker, Kubernetes, offline installation, server/agent from sources, Ansible and Puppet. Both quotes are on the page. |
| 4 | SUPPORTED | Cloud service index contains "which we host and operate" (SaaS edition) and "Your team remains responsible for security monitoring, investigating alerts, and responding to incidents". |
| 5 | SUPPORTED | Technical FAQ lists exactly the nine regions with codes (Tokyo ap-northeast-1, Mumbai ap-south-1, Singapore ap-southeast-1, Sydney ap-southeast-2, Frankfurt eu-central-1, London eu-west-2, Canada ca-central-1, North Virginia us-east-1, Ohio us-east-2). The FAQ body names no cloud provider (AWS appears only in sidebar navigation for unrelated integration pages), so the reworded claim is now right. |
| 6 | SUPPORTED | Glossary: "The region you select cannot be changed after you create an environment." and "It's an AWS S3 bucket to store your logs for a longer time and meet compliance requirements." |
| 7 | SUPPORTED | wazuh.com/cloud: Small "Up to 100" / "$571/month", Medium "Up to 250" / "$923/month", Large "Up to 500" / "$1467/month", Custom with no price. "Starting at" is on the page. |
| 8 | SUPPORTED | Rows in order: Indexed data retention 1 month / 3 months / 3 months / Custom; Archive data retention 3 months / 1 year / 1 year / Custom. Matches the claim. Medium confidence fits a flattened table whose values may change. |
| 9 | SUPPORTED | "Enjoy a free 14-day trial", "No credit card required!" and "Powered by an AI security analyst, it reduces alert fatigue..." are on the page. |
| 10 | SUPPORTED | The fetched page has no MSSP, managed service provider, multi-tenant or multi-tenancy wording. Medium confidence fits a claim that something is missing from one page. |

## Note-level problems
- None. Front matter is complete (`url: multiple, see claims` is valid, and every claim cites its own URL). The summary no longer says Cloud runs on AWS regions; the only AWS statement is the glossary's S3 line (claim 6), and the AWS hosting link is labelled `Inference:`. No role attributions. Confidence levels fit official docs and the vendor page. No personal data. English.

## Recommended fixes
- None.
