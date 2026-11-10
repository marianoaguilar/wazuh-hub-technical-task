---
title: CISA Known Exploited Vulnerabilities (KEV) catalog - topic note
url: multiple, see claims
publisher: Cybersecurity and Infrastructure Security Agency (CISA)
source_type: official-docs
wazuh_version: n/a
accessed: 2026-11-10
question: What is the CISA KEV catalog, how can it be downloaded (formats, feed URL), how often does it change, and what are its terms of use?
---

## Summary
The KEV catalog is CISA's list of vulnerabilities with reliable evidence of exploitation in the wild. It is published as CSV and JSON files (plus a JSON schema) on cisa.gov and mirrored in the `cisagov/kev-data` GitHub repository. The data is released under CC0 1.0. CISA does not publish a fixed update schedule; the JSON feed carries a `catalogVersion` and `dateReleased`, and on the access date the latest release was 2026-11-09 with 1773 entries.

## Claims
1. CISA describes the KEV catalog as the authoritative source of vulnerabilities exploited in the wild and recommends it as an input to prioritization.
   - Quote: "CISA maintains the authoritative source of vulnerabilities that have been exploited in the wild." / organizations "should use the KEV catalog as an input to their vulnerability management prioritization framework."
   - Source: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
   - Confidence: high

2. A vulnerability is added only if it has a CVE ID, reliable evidence of active exploitation, and a clear remediation action.
   - Quote: "There is reliable evidence that the vulnerability has been actively exploited in the wild." / "There is a clear remediation action for the vulnerability, such as a vendor-provided update."
   - Source: https://www.cisa.gov/known-exploited-vulnerabilities
   - Confidence: high

3. The catalog is downloadable as CSV, JSON, and a JSON schema at these paths on www.cisa.gov: `/sites/default/files/csv/known_exploited_vulnerabilities.csv`, `/sites/default/files/feeds/known_exploited_vulnerabilities.json`, `/sites/default/files/feeds/known_exploited_vulnerabilities_schema.json`.
   - Quote: (download links on the catalog page; link targets as listed above)
   - Source: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
   - Confidence: high

4. The JSON feed has top-level fields `title`, `catalogVersion`, `dateReleased`, `count`; on the access date it showed catalogVersion "2026.11.09", dateReleased "2026-11-09T19:54:37.4945Z" and count 1773. Each entry has the fields cveID, vendorProject, product, vulnerabilityName, dateAdded, shortDescription, requiredAction, dueDate, knownRansomwareCampaignUse, forensicTriage, notes, cwes.
   - Quote: "catalogVersion": "2026.11.09", "count": 1773
   - Source: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
   - Confidence: high (snapshot value; changes over time)

5. Change frequency: neither the catalog page nor the KEV guidance page states an update schedule. The feed snapshot shows several entries added on 2026-11-09 and one on 2026-11-06, Inference (from one snapshot only): the catalog seems to change several times a week at irregular intervals.
   - Quote: (catalog page) no update cadence stated; feed entries show "dateAdded": "2026-11-09" and "2026-11-06"
   - Source: https://www.cisa.gov/known-exploited-vulnerabilities-catalog ; https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
   - Confidence: medium (the frequency is read from one snapshot, not from a stated policy)

6. CISA publishes an official GitHub mirror (`cisagov/kev-data`) with the same three files, updated whenever the KEV is updated, within minutes of cisa.gov.
   - Quote: "Mirror of cisa.gov/kev data files." / the repo "is updated whenever the KEV is updated", "synchronized within minutes of each other."
   - Source: https://github.com/cisagov/kev-data
   - Confidence: high

7. Terms of use: the KEV data is released under Creative Commons 0 (CC0 1.0 Universal); it may be used in any legal manner, is provided as-is, and its use does not allow use of the CISA logo or DHS seal or imply endorsement.
   - Quote: "You may use this data in any legal manner." / distributed under the "Creative Commons 0 1.0 License."
   - Source: https://www.cisa.gov/sites/default/files/licenses/kev/license.txt
   - Confidence: high

8. The GitHub mirror is also under CC0.
   - Quote: "licensed under the CC0 license"
   - Source: https://github.com/cisagov/kev-data
   - Confidence: high

## Inference
- Inference: A SaaS can download the KEV JSON (or poll the GitHub mirror) a few times a day and use `catalogVersion`/`dateReleased` to detect changes cheaply. CC0 allows storing and redistributing the data inside a commercial product, as long as CISA/DHS branding is not used to imply endorsement.
- Inference: `knownRansomwareCampaignUse` and `dateAdded` are useful extra ranking signals (recent KEV addition, ransomware use).

## Open questions
- UNVERIFIED: whether CISA offers a KEV-specific RSS or email alert; the pages read only show site-wide RSS/subscribe links.
- A third-party blog (Socket, not read) claims updates usually happen on US weekdays during business hours; not checked against CISA.

## Not read
- https://socket.dev/blog/cisa-brings-kev-data-to-github - search result only, not fetched; no claim made.
