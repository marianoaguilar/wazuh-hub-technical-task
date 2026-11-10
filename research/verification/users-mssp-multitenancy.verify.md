---
note: research/sources/users-mssp-multitenancy.md
verified: 2026-11-10
result: PASS
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | The definition quote is verbatim on the multi-tenancy page, which also describes the Global, Private and Custom tenants. |
| 2 | SUPPORTED | The page does not mention MSSPs or isolation of indexed data. The separation it describes covers saved objects and role access to tenants. "This tenant is shared between every Wazuh dashboard user." is verbatim. |
| 3 | SUPPORTED | Both quotes are on the blog post. Its scenario has a managed SOC provider with Organizations A and B, each with a cluster (server plus indexer), and a central CCS environment (indexer plus dashboard). |
| 4 | SUPPORTED | The quote is on the page. The post says CCS helps organizations, MSSPs included, onboard customers without compromising data confidentiality. |
| 5 | SUPPORTED | Both quotes are in the thread. The reply mentions at least one all-in-one VM per client plus one for the MSSP and links to the Wazuh CCS blog post. The follow-up question about ports is unanswered. |
| 6 | SUPPORTED | Both strings are under "Service augmentation" in the partner plan comparison (Gold/Platinum). The note correctly says the tier mapping is unclear. |
| 7 | SUPPORTED | Both iSecNG quotes are verbatim, and the page calls iSecNG an MSSP. The FirmGuardian URL is now cited, its quote is verbatim, and the page gives no architecture details (no clusters, instances or multi-tenancy). |
| 8 | SUPPORTED | The quote is verbatim. The page says Guayoyo offers "Virtual SOC services". |

## Note-level problems
- None. I checked these points:
  - Front matter is complete. `url: multiple, see claims` is valid because every claim cites its own URL, and `source_type: other` fits the mixed sources.
  - `wazuh_version` matches the pages: 4.14.10 is the newest release listed, and the blog shows 4.8.2 in its byline and 4.14.1 in its setup section.
  - The Summary no longer gives the forum replier a role. The thread shows no role, badge or affiliation, and the note now says so.
  - The Summary and the Inference quote the partner page's one-line description of the multi-tenancy console, and the quote is accurate.
  - Confidence levels fit the sources, and inferences are labelled.
  - No personal data and no forum names are copied. The note is in English.
- Minor: the "Changes after verification" section calls the partner-console inference "Inference 2", but it is the third Inference bullet. This does not affect correctness.

## Recommended fixes
- None.
