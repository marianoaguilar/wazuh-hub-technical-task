---
title: Wazuh case studies (Groupon, Alignet, FirmGuardian, Guayoyo, Enevo, ITA LA, University of Chichester, iSecNG)
url: multiple, see claims
publisher: Wazuh Inc.
source_type: other
wazuh_version: not stated
accessed: 2026-11-10
question: Who uses Wazuh, and for what? (organisation types, sectors, use cases from customer stories)
---

## Summary
Wazuh publishes case studies on wazuh.com. The ones read cover e-commerce (Groupon), payment
security in Latin America (Alignet), MSSPs and SOC providers (FirmGuardian, Guayoyo, iSecNG),
the energy/OT sector (Enevo), local government (City of Los Angeles ITA) and higher education
(University of Chichester). They are vendor-published marketing material: useful for sectors and
use cases, not for neutral evaluation. Few give numbers on deployment size. Individual names are
not copied; roles are given instead.

## Claims
1. Groupon (e-commerce) uses Wazuh to protect and monitor AWS, and adopted it as an IDS to comply with PCI DSS.
   - Quote: "Industry: Electronic commerce" / "comply with the Payment Card Industry Data Security Standard (PCI DSS)"
   - Source: https://wazuh.com/resources/case-studies/groupon-deploys-wazuh-to-protect-and-monitor-aws/
   - Confidence: medium (vendor case study)

2. Groupon's listed use cases are FIM, log data collection, system inventory and vulnerability detection, with a high volume of AWS data.
   - Quote: "File Integrity Monitoring" / "a very high volume of data from Amazon Web Services"
   - Source: https://wazuh.com/resources/case-studies/groupon-deploys-wazuh-to-protect-and-monitor-aws/
   - Confidence: medium

3. Alignet, a payment and e-commerce security provider in Latin America, focuses its Wazuh use on PCI DSS compliance and automating alerts and responses; it reports post-incident inspections cut from 1 day to 2 hours (vendor-reported).
   - Quote: "They are currently focused on PCI DSS compliance and the automation of alerts and responses." / "Time reduction in post-incident inspections from 1 day to 2 hours."
   - Source: https://wazuh.com/resources/case-studies/alignet-and-wazuh-join-forces-to-enhance-productivity/
   - Confidence: medium

4. FirmGuardian, a cybersecurity company working with regulated industries, uses Wazuh as an MSSP for multiple clients (vulnerability scanning, compliance checks, inventory, custom rules and decoders).
   - Quote: "invaluable for us as an MSSP" / "large-scale data aggregation and analysis for multiple clients"
   - Source: https://wazuh.com/resources/case-studies/firmguardian-customization-meets-compliance/
   - Confidence: medium

5. Guayoyo built a Blue team and a Virtual SOC service on Wazuh and became a Wazuh Partner.
   - Quote: "they decided to create their own Blue team to offer Virtual SOC services" / "they decided to become Wazuh Partners, allowing them to offer more competitive rates"
   - Source: https://wazuh.com/resources/case-studies/guayoyo-virtual-soc-triumph/
   - Confidence: medium

6. Enevo Cybersec (energy sector) uses Wazuh for OT security telemetry from substations and automation systems; the agents' flexibility is cited as the reason for choosing it.
   - Quote: "the flexibility offered with the agents is what made us trust in Wazuh as a long-term Strategic Partner"
   - Source: https://wazuh.com/resources/case-studies/enevo-ot-cybersecurity-strategy/
   - Confidence: medium

7. The City of Los Angeles Information Technology Agency (its Integrated Security Operation Center) uses Wazuh across 40+ city departments. Its log collection focuses on Windows events; its custom rules cover use cases such as Google Password Sync and Netscaler, and the page also lists integrations with Azure, GCP, GitHub, AWS, BitLocker and SysMon. The day-to-day operator quoted is a sysadmin ("Primary Administrator").
   - Quote: "Custom rules can be deployed across 40+ departments in minutes." / "collect logs at scale, particularly focusing on Windows events" / "I personally love the flexibility of Wazuh because, as a Sysadmin, I can think of any use case"
   - Source: https://wazuh.com/resources/case-studies/ita-la-scalable-cybersecurity/
   - Confidence: medium

8. The University of Chichester (higher education, West Sussex, England) uses Wazuh to centralise logs, alongside Azure Sentinel, and reports Wazuh detected ransomware during evaluation.
   - Quote: "The University of Chichester, located in West Sussex, England" / "Wazuh uniquely detected ransomware"
   - Source: https://wazuh.com/resources/case-studies/university-of-chichester-achieving-proactive-defense/
   - Confidence: medium

9. iSecNG, an MSSP serving small and mid-sized businesses across Germany, started on Wazuh Cloud and later moved to self-hosting in a German datacenter.
   - Quote: "Initially, iSecNG deployed Wazuh using Wazuh Cloud to provide SIEM solutions to its clients." / "As demand grew, they transitioned to hosting Wazuh in a German datacenter,"
   - Source: https://wazuh.com/resources/case-studies/isecng-strengthening-cybersecurity-with-wazuh/
   - Confidence: medium

10. iSecNG gives each client a dedicated Wazuh instance, with sizes ranging from small 100GB instances to multi-terabyte clusters, one of them on Kubernetes.
    - Quote: "Clients receive dedicated Wazuh instances to ensure data separation and regulatory compliance." / "Providing a stable and scalable Wazuh cluster based on Kubernetes."
    - Source: https://wazuh.com/resources/case-studies/isecng-strengthening-cybersecurity-with-wazuh/
    - Confidence: medium

## Inference
- Inference: compliance (PCI DSS in particular, NIS2 in Europe) is a recurring driver across case studies.
- Inference: three of eight case studies read are service providers (MSSP / virtual SOC), so MSSPs are a significant and vendor-promoted user group.
- Fact (iSecNG case study, https://wazuh.com/resources/case-studies/isecng-strengthening-cybersecurity-with-wazuh/): the page gives the reasons for the move from Wazuh Cloud to a German datacenter as "gaining full control over infrastructure, compliance, and scalability." Inference: control and compliance at scale matter for MSSPs.

## Open questions
- Case studies rarely give agent counts or data volumes; no deployment-size statistics were found.
- Countries for Guayoyo, FirmGuardian, Enevo and Alignet's headquarters are not stated on the pages read.

## Not read
- https://wazuh.com/uploads/2026/09/case-study-isecng-flexible-security.pdf — found in search, not fetched (web case study used instead).

## Changes after verification
- Claim 7: removed "Windows events" from the custom-rule sources; stated separately that log collection focuses on Windows events, and listed the custom-rule use cases and integrations as the page gives them (re-fetched 2026-11-10). Added the Windows-events quote.
- Inference 3: replaced "the case study does not state the reason beyond growth of demand" (contradicted by the page) with the page's stated reasons, quoted and sourced; kept only the MSSP generalisation as inference.
- Front matter left as is (`url: multiple, see claims`, `source_type: other`): the template allows these for a topic note; the optional change was not needed.
- Main session, after second verification: Claim 9: removed "German MSSP" (the page says it serves companies "all over Germany") and "demand is driven by NIS2" (the page does not tie iSecNG's demand to NIS2).
