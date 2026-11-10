---
title: Who uses Wazuh (vendor adoption figures, customer list, independent review data)
url: multiple, see claims
publisher: Wazuh Inc.; GitHub; PeerSpot
source_type: other
wazuh_version: not stated (site pages accessed while docs "current" lists 4.14.10 as newest release)
accessed: 2026-11-10
question: Who uses Wazuh, and for what? (organisation types, roles, adoption numbers)
---

## Summary
Wazuh's own website gives headline adoption numbers (protected endpoints, enterprise users,
downloads per year) and a list of customer logos covering large enterprises, government and
universities. The vendor also says it is used by Fortune 500 companies and "thousands" of
organisations. Independent review data (PeerSpot) suggests a large share of reviewers come from
small businesses, with visitors spread across many sectors. All adoption figures below are
vendor-stated unless marked otherwise.

## Claims
1. Vendor-stated adoption figures on the Wazuh home page: 15+ million protected endpoints,
   100+ thousand enterprise users, 30+ million downloads per year.
   - Quote: "15+ Million Protected endpoints" / "100+ Thousand Enterprise users" / "30+ Million Downloads per year"
   - Source: https://wazuh.com/
   - Confidence: high (that the vendor states it); the numbers themselves are vendor-stated and not independently verified

2. The home page presents Wazuh as the most widely used open source security solution (vendor claim).
   - Quote: "The world's most widely used open source security solution"
   - Source: https://wazuh.com/
   - Confidence: high (as a vendor statement)

3. The same three figures are repeated on the About us page, which also says the company started in 2015 and has more than 200 staff.
   - Quote: "Since our inception in 2015" / "Our team currently consists of more than 200 professionals distributed all around the world."
   - Source: https://wazuh.com/about-us/
   - Confidence: high

4. The vendor says its users include Fortune 500 companies and that thousands of users and organisations use it daily.
   - Quote: "Our platform has become the go-to choice for numerous enterprises, including Fortune 500 companies and tech giants." / "thousands of users and organizations rely on our solution daily"
   - Source: https://wazuh.com/about-us/
   - Confidence: medium (vendor statement, not quantified)

5. The "Our customers" page shows logos of large companies and public bodies, among them Mercado Libre, Ricoh, Thales, Banco Internacional, Dubai Police, Indra, Telefónica, Temenos, eBay, Intuit, Mondelez, Rappi, Standard Life, NASA, Cisco and FIS. Sector and country are not stated for logos.
   - Quote: (logo bar, no text) — the page lists the logos without description; testimonial example: "Wazuh is a unique tool, perfect for startups like Woop that are looking for top-tier security at a competitive cost."
   - Source: https://wazuh.com/our-customers/
   - Confidence: medium (logo presence only; scope of use per customer unknown)

6. Testimonial job titles on the "Our customers" page show the roles that operate Wazuh: IT Security Manager (Groupon), Chief Information Security Officer (Alignet), Lead Platform Architect (FirmGuardian), Co-founder and Director (Guayoyo), Primary Administrator / sysadmin (ITA), IT Service Development Manager (University of Chichester), Site Reliability Engineer (Woop), Founder & CEO (Netbyte). The company for each title comes from the case-study link next to the testimonial; Woop and Netbyte have no case-study link; Woop is named in its testimonial text (see claim 5), Netbyte was identified only from a logo file name. The page itself does not name "Los Angeles" or call Guayoyo a virtual SOC provider; those two facts come from the case studies cited below.
   - Quote: "I love the flexibility of Wazuh because, as a sysadmin, I can think of any use case"
   - Source: https://wazuh.com/our-customers/
   - Quote (ITA case study): "About the City of Los Angeles Information Technology Agency (ITA)"
   - Source: https://wazuh.com/resources/case-studies/ita-la-scalable-cybersecurity/
   - Quote (Guayoyo case study): "they decided to create their own Blue team to offer Virtual SOC services"
   - Source: https://wazuh.com/resources/case-studies/guayoyo-virtual-soc-triumph/
   - Confidence: medium (roles are from vendor-selected testimonials; names deliberately not copied; Netbyte attribution is low, from a logo file name only)

7. The main Wazuh GitHub repository shows about 17.6k stars and 2.6k forks, and describes the product as unified XDR and SIEM.
   - Quote: "Wazuh - The Open Source Security Platform. Unified XDR and SIEM protection for endpoints and cloud workloads."
   - Source: https://github.com/wazuh/wazuh
   - Confidence: high (counts as shown on 2026-11-10; they change over time)

8. Independent (PeerSpot, reviews platform): the Wazuh reviews page shows 51 reviews, an average rating of 7.4/10, 81% willing to recommend, and ranks Wazuh #5 in SIEM and #2 in Log Management Software.
   - Quote: "#5 in top Security Information and Event Management (SIEM)" / "81%" willing to recommend (as rendered on the page)
   - Source: https://www.peerspot.com/products/wazuh-reviews
   - Confidence: low (self-selected reviewers; a search snippet showed different PeerSpot figures on another page, see Open questions)

9. Independent (PeerSpot): reviewers by company size are Small Business 23, Midsize Enterprise 12, Large Enterprise 9; visitors by industry are led by Comms Service Provider (13%), University (9%), Manufacturing (8%), Computer Software (8%), Government (6%), Outsourcing (6%) and Financial Services (6%).
   - Quote: "Small Business" 23 / "Midsize Enterprise" 12 / "Large Enterprise" 9; "Comms Service Provider" 13%, "University" 9%
   - Source: https://www.peerspot.com/products/wazuh-reviews
   - Confidence: low (small sample, platform-specific; page text was read by an extraction tool, numbers as reported)

## Inference
- Inference: the user base spans from startups and small businesses (strong in review data) to large enterprises and public bodies (customer logos, Los Angeles ITA). The vendor's "100+ thousand enterprise users" is not defined (organisations or people?), so it should be quoted only as a vendor claim.
- Inference: the roles that operate Wazuh day to day are mostly security engineers/SOC staff and sysadmins; MSSP owners appear as a distinct group (see users-mssp-multitenancy.md).

## Open questions
- How Wazuh defines "enterprise users" and "protected endpoints" and how they are counted.
- No official breakdown of users by region, sector or size was found.
- UNVERIFIED: a search snippet reported a PeerSpot figure of "375" reviews and "1st" in SIEM by mindshare on a different PeerSpot page; that page was not fetched, so it is not used.
- Roles such as students/learners and consultants are not quantified in any source read.

## Not read
- https://www.g2.com/products/wazuh/reviews — HTTP 403.
- https://msspalert.com/news/wazuh-offers-free-open-source-security-platform — HTTP 403.

## Changes after verification
- Claim 6: changed "City of Los Angeles ITA" to "ITA" and "Co-founder/Director of a virtual SOC provider" to "Co-founder and Director", because the Our customers page does not state Los Angeles or "virtual SOC" (only URL slugs did).
- Claim 6: added the ITA and Guayoyo case-study URLs (fetched 2026-11-10) with quotes that do state "City of Los Angeles" and "Virtual SOC services".
- Claim 6: stated that company attributions come from the case-study links next to testimonials, and that Netbyte comes only from a logo file name (lower confidence for it).
