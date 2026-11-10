---
note: research/sources/pain-community-multi-tenancy.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Re-fetched today. The search page shows 30 results ("1–30 of many"), from "Multi-tenant Deployment of Wazuh in medium-sized Companies" (3/1/23) to "Wazuh 5 Security Analytics – Tenant separation..." (Oct 11). The first 11 results run from Oct 11 down to "Two or more company to monitor" (3/14/25), so the count of 11 checks out. All six example titles and post counts match (9, 7, 7, 6, 6, 6). The quoted title "Wazuh architecture for multiple customers" is listed with 8/13/24 and 5 posts. The new caveats are accurate: "Oct 11" and "Apr 8" show no year (the note marks 2026 as inferred), and the dates are last-activity dates. The thread "Wazuh Multi Tenancy inquiry" was first posted Mar 16, 2026 but is listed as Apr 8. The note calls the result order Google's ranking and the list a first-page sample, which is a fair framing. |
| 2 | SUPPORTED | Thread "Wazuh Multi Tenancy inquiry", first post Mar 16, 2026. A Mar 27, 2026 reply has the quote word for word, plus "Data isolation is entirely the job of DLS on the indexer role" and "Separate indices are not needed" (so the alerts index is shared). |
| 3 | SUPPORTED | Thread "Multi-tenancy", first post May 8, 2025. A May 8 reply links a cross-cluster search guide and suggests one agent group per client with labels. The quote appears in that reply. A Sep 29, 2025 post on v4.13.0 says Discover is restricted, but the client "still sees all agents and their vulnerabilities". |
| 4 | SUPPORTED | Thread "multi tenant internal user not showing vulnerability detection data". The poster is on 4.12 and uses a DLS filter on agent.labels.group. In Discover the alerts show, but the Vulnerability Dashboard and Inventory are empty. An Aug 23, 2025 reply has the quote. The last of 7 posts (Nov 8, 2025) asks for updates and gets no answer. |
| 5 | SUPPORTED | Thread "True multitenancy infrastracture", first post Mar 11, 2025. The goal is a multi-tenant setup, and the thread mentions Docker Swarm and cross-cluster search (CCS). A Mar 20, 2025 post has the quote word for word. |

## Note-level problems
- None. The front matter is complete. `url: multiple, see claims` is valid because every claim cites its own URL.
- Confidence values are all valid levels and fit the sources: `high` only on claim 1, a count of what the page shows with the tallies marked as the researcher's own, and `medium`/`low` on the single forum threads.
- The inference is kept in its own section, prefixed `Inference:`. The note is in English.
- The note never calls anyone "Wazuh staff". No fetched page shows a staff label for any poster. Some replies imply an affiliation ("our Wazuh Cloud service", "confirmed internally"), but the pages do not state one.
- No personal data: the note contains no poster names, usernames or emails.

## Recommended fixes
- None.
