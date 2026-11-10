---
title: Deployment models and Wazuh Cloud (docs and wazuh.com/cloud)
url: multiple, see claims
publisher: Wazuh Inc.
source_type: official-docs
wazuh_version: "current" docs (quickstart installs from the 4.14 branch; newest release listed 4.14.10)
accessed: 2026-11-10
question: Who uses Wazuh, and for what? (how it is deployed and offered: self-hosted vs Wazuh Cloud, sizes)
---

## Summary
Wazuh is mainly self-hosted: the docs describe all-in-one, single-node and multi-node
deployments and many install methods (OVA, AMI, Docker, Kubernetes, Ansible, Puppet, offline,
sources). The quickstart all-in-one setup is sized for up to 100 endpoints. Wazuh Cloud is the
vendor-hosted SaaS edition: Wazuh runs the central components in a region chosen by the customer
(the docs list nine regions; archive data is stored in an AWS S3 bucket), and the customer still
does the security monitoring and response. Public tiers are priced by active agents.

## Claims
1. The quickstart (all-in-one) hardware table covers 1-25, 26-50 and 51-100 agents (4-8 vCPU, 8 GiB RAM, 50-200 GB for 90 days) and says this usually covers up to 100 endpoints.
   - Quote: "This is usually enough for monitoring up to 100 endpoints and for 90 days of queryable/indexed alert data."
   - Source: https://documentation.wazuh.com/current/quickstart.html
   - Confidence: high

2. The architecture page describes single-node deployments for medium environments and multi-node (clustered) deployments for large ones.
   - Quote: "Recommended for medium environments that require higher performance than an all-in-one setup." / "This deployment is recommended for large environments with high event throughput"
   - Source: https://documentation.wazuh.com/current/getting-started/architecture.html
   - Confidence: high

3. Documented deployment options include a pre-built OVA, an AWS AMI, Docker, Kubernetes, offline installation, installation from sources, Ansible and Puppet.
   - Quote: "Wazuh provides a pre-built virtual machine image (OVA) that you can directly import" / "Using Docker, you can install and configure the Wazuh deployment as a single-host architecture."
   - Source: https://documentation.wazuh.com/current/deployment-options/index.html
   - Confidence: high

4. Wazuh Cloud is a SaaS edition that Wazuh hosts and operates; the customer stays responsible for monitoring, investigating alerts and incident response.
   - Quote: "which we host and operate" / "Your team remains responsible for security monitoring, investigating alerts, and responding to incidents"
   - Source: https://documentation.wazuh.com/current/cloud-service/index.html
   - Confidence: high

5. Wazuh Cloud environments are hosted in cloud provider regions in Asia Pacific (Tokyo, Mumbai, Singapore, Sydney), Europe (Frankfurt, London) and North America (Canada, North Virginia, Ohio), each listed with a region code. The FAQ answers do not name the cloud provider.
   - Quote: "Available regions:" / "Frankfurt: eu-central-1" / "North Virginia: us-east-1"
   - Source: https://documentation.wazuh.com/current/cloud-service/your-environment/technical-faq.html
   - Confidence: high

6. The region cannot be changed after creating an environment, and archive data is stored in an AWS S3 bucket.
   - Quote: "cannot be changed after you create an environment" / "AWS S3 bucket to store your logs for a longer time and meet compliance requirements"
   - Source: https://documentation.wazuh.com/current/cloud-service/glossary.html
   - Confidence: high

7. wazuh.com/cloud lists monthly tiers by active agents: Small from $571/month (up to 100 agents), Medium from $923/month (up to 250), Large from $1467/month (up to 500), and a Custom plan.
   - Quote: "Starting at" $571/month, "Up to 100" active agents (as rendered for the Small plan)
   - Source: https://wazuh.com/cloud/
   - Confidence: medium (prices extracted from a pricing table; they may change)

8. Retention per tier, as extracted from the same table: Small 1 month indexed / 3 months archive; Medium and Large 3 months indexed / 1 year archive.
   - Quote: "Indexed data retention" / "Archive data retention" (row labels)
   - Source: https://wazuh.com/cloud/
   - Confidence: medium (table text was flattened; values matched to rows by position, and the verifier found the order consistent with the row labels for all three plans; values may change)

9. Wazuh Cloud offers a 14-day free trial without a credit card, and the page markets an AI security analyst.
   - Quote: "Enjoy a free 14-day trial." / "Powered by an AI security analyst."
   - Source: https://wazuh.com/cloud/
   - Confidence: high

10. The wazuh.com/cloud page does not mention MSSPs or multi-tenancy.
    - Quote: (absence) — no MSSP or multi-tenant wording found on the page
    - Source: https://wazuh.com/cloud/
    - Confidence: medium (absence of evidence, based on one read of the page)

## Inference
- Inference: the region codes in claim 5 (e.g. eu-central-1, us-east-1) match AWS region naming, and claim 6 says archive data is in an AWS S3 bucket, so Wazuh Cloud likely runs on AWS; the region FAQ itself does not say so.
- Inference: the public Cloud tiers stop at 500 agents before "Custom", while the free self-hosted quickstart targets up to 100 endpoints; larger users either cluster self-hosted or negotiate a custom Cloud plan.
- Inference: since Cloud leaves monitoring and response to the customer, a gap remains for managed detection/response, which MSSPs fill (see users-mssp-multitenancy.md).

## Open questions
- No public figure for the split of users between self-hosted and Wazuh Cloud was found.
- No public statistics on typical deployment size (agents per deployment) were found.
- The docs FAQ region list differs between doc versions (noted in search results); only the "current" page was read.

## Changes after verification
- Claim 5: removed "named with AWS region codes"; now says each region has a code and the FAQ answers do not name the provider (re-fetched 2026-11-10). The AWS link moved to an `Inference:` line.
- Summary: replaced "runs the central components on AWS regions" with a region-neutral wording; the only AWS mention kept is the glossary's S3 statement (claim 6). Also dropped "deploys agents" from the summary, as claim 4's quote covers monitoring and response only.
- Claim 8: confidence raised from low to medium, as the report suggests (positional mapping checked against row labels for all three plans).
