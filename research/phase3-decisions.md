# Phase 3: design decisions

Step 3 of [`../workflow/plans/02-phase3.md`](../workflow/plans/02-phase3.md). For each decision the agent proposed options with pros and cons and a recommendation; **I chose**. Facts come from the lab note [`sources/lab-api-vulnerability-data.md`](sources/lab-api-vulnerability-data.md) and the verified `design-*` notes; anything else is marked as inference.

## D1. How the data gets from the customer's Wazuh to the service
| Option | For | Against |
|--------|-----|---------|
| A. The SaaS pulls from the customer's Wazuh API (55000) and indexer (9200) | Nothing to install | Customer must expose the indexer to the internet, against Wazuh's advice to restrict it to trusted networks ([note](sources/design-wazuh-access-indexer-security.md)); the SaaS stores every customer's Wazuh credentials |
| **B. A small connector in the customer network reads locally (read-only user) and pushes over outbound HTTPS** | No inbound ports; Wazuh credentials never leave the customer; names can be pseudonymised before sending | Customer installs and updates a component; we maintain it |
| C. Manual export and upload | No connection at all | Not a service: no regular sync, so decisions cannot be re-applied on each sync |

**Decision (2026-11-10): B, connector.** Recommended by the agent and chosen by me.

## D2. What data leaves the customer network
| Option | For | Against |
|--------|-----|---------|
| A. Everything as returned by Wazuh | Simplest; real names in the UI | The service would store real host names next to their unpatched critical CVEs for every customer: a target map if leaked (inference) |
| **B. Only the fields needed to decide, hosts as pseudonyms** | A leak shows "host-7f3a has CVE-X" without saying whose host it is; less data to move | The UI shows aliases; users add their own labels and criticality |
| C. Only aggregated counts | Almost no risk | The AI cannot reason about false positives; the service loses its main job |

Fields sent per finding (from the lab document, [`lab/api/09`](lab/api/09-indexer-vulnerability-critical-example.json)): `vulnerability.id`, `package.name` / `version` / `architecture` / `type`, `host.os.name` / `version` / `platform` / `kernel` (+ codename from syscollector), `vulnerability.severity`, `score.base` / `score.version`, `scanner.condition` / `source` / `reference`, `detected_at`, `published_at`, `under_evaluation`, and a pseudonymous host id. Not sent: agent names, hostnames, IPs, logs, alerts, the long CVE description (public data the service can fetch itself). The alias → real name table stays in the connector.

**Decision (2026-11-10): B, data minimisation with pseudonyms.** Recommended by the agent and chosen by me.

## D3. Keeping each customer's data separate
| Option | For | Against |
|--------|-----|---------|
| **A. One shared database; every row has a `tenant_id` and the database itself enforces it (PostgreSQL Row-Level Security)** | Cheap and simple to run; isolation does not depend only on application code | One serious flaw in that protection affects all customers |
| B. One database per customer | Strong, easy-to-audit separation | Hundreds of databases to patch, monitor and back up: costly for a new service |
| C. A by default, B for large or regulated customers | Best of both | Two ways of operating; only worth it later |

Rules in every option: the tenant comes from the authenticated session, never from a value in the request; one LLM call never contains data from two tenants; automated tests try cross-tenant reads and must always fail.

**Decision (2026-11-10): A for the first version, C as the planned evolution.** Recommended by the agent and chosen by me.

## D4. How users and connectors authenticate
**Users.**
| Option | For | Against |
|--------|-----|---------|
| A. Own accounts: email + password + MFA | Works for anyone | We store passwords; leavers must be removed by hand |
| B. Company login only (SSO: OIDC/SAML) | No passwords stored; leavers lose access automatically | Small teams without a corporate identity provider cannot sign in |
| **C. Both, through a managed identity provider** | SSO for companies, email + MFA for small teams; we do not write our own login | Dependency on, and cost of, the provider |

Roles per tenant: **viewer** (reads findings and the fix-first queue), **analyst** (confirms or rejects AI proposals, records decisions), **admin** (users and connectors). A decision "accepted risk" always needs an owner and an expiry date.

**Connector.** The admin creates a one-time enrolment code in the UI; the connector exchanges it for its own credential, bound to the tenant. That credential can only push data (it cannot read anything from the service) and the admin can revoke or rotate it.

**Decision (2026-11-10): C for users; roles and connector enrolment as above.** Recommended by the agent and chosen by me.

## D5. Where AI fits and how it is controlled
**5a. Role of the AI.** A deterministic step runs first, with no AI: group findings into units that one action resolves (for example all CVEs of one kernel package), re-apply existing decisions, and send only new, undecided groups to the AI.

| Option | For | Against |
|--------|-----|---------|
| A. The AI decides and closes false positives by itself | No work for users | A mistake hides a real vulnerability without anyone noticing |
| **B. The AI proposes, a person confirms** | The AI does the investigation; the person adds context the AI lacks (for example "is btrfs used on this host?") | Still needs a person, for much less time |
| C. No AI, rules only | Predictable and cheap | Explains nothing new; the odd cases (like the lab kernel finding) are the ones rules miss |

The AI returns a fixed structure per group: proposal (`likely_false_positive` / `real` / `needs_context`), reason, the evidence fields it used, questions for the analyst. Controls:
- Every cited evidence value must exist in the input; otherwise the proposal is discarded.
- A CVE in CISA KEV ([note](sources/design-ranking-cisa-kev.md)) can never be proposed as a false positive.
- CVE and advisory texts are untrusted data (prompt injection); the model can only return the fixed structure and has no tools: it cannot write to Wazuh or change a status.
- Decisions expire and are reopened when the package version changes.

**5b. Where the model runs.**
| Option | For | Against |
|--------|-----|---------|
| 1. Anthropic API directly | No training on API data by default; zero data retention by agreement | Only "global" or "us" inference locations, no EU ([note](sources/design-llm-claude-pricing-data-terms.md)) |
| **2. Same models through AWS Bedrock, EU cross-region inference** | Processing stays in the EU; a no-retention mode exists; the model provider has no access to prompts or completions ([note](sources/design-llm-claude-pricing-data-terms.md)) | Depends on AWS; Opus 5.5 EU availability not confirmed (Sonnet 5.5 and Haiku 5.5 are) |
| 3. Open model on our own servers | Full control | GPUs to run; quality likely lower (inference, not researched) |

**Decision (2026-11-10): 5a = B (AI proposes, person confirms), 5b = 2 (Bedrock, EU).** Recommended by the agent and chosen by me.

## D6. Knowing the AI gives good answers, and noticing when it stops
- **Before every change (offline evaluation).** A golden set of cases with a known right answer, reviewed by a person: forum cases from Phase 2 (patched PHP packages flagged against a newer branch, Ubuntu kernel CVEs marked "Solved" after a feed change) and lab findings (the kernel/btrfs finding). Every change of prompt, model or model version runs the set; a lower score than the current version blocks the release.
- **In production (online signals).** Share of AI proposals that analysts accept (a sudden drop raises an alert); share of proposals discarded because they cite evidence not in the input; decisions reopened (a "false positive" that turned out real: each one reviewed); a "this proposal is wrong" button.
- A weekly random sample of proposals is reviewed by our team; bad cases are added to the golden set.
- The exact model version is pinned; a new version is used only after it passes the golden set.

**Decision (2026-11-10): as above.** Proposed by the agent and accepted by me.

## D7. When the Wazuh API, the connector, the model or the service is down
The service is not in Wazuh's critical path: it only reads, so the customer's Wazuh keeps detecting and alerting whatever happens to the service.

| What is down | What happens | What the user sees |
|--------------|--------------|--------------------|
| Customer's Wazuh API / indexer, or the connector loses connection | The service keeps working on the last snapshot; the connector retries with backoff and buffers locally | "Data from 6 h ago, connector not reporting"; email to the admin after a threshold; decisions can still be read and edited |
| The model (Bedrock) | Everything that is not AI keeps working (ledger, re-applied decisions, fix-first queue); new groups wait as "pending AI review" | "AI proposal pending"; the analyst may decide by hand |
| The service itself | The connector buffers and sends later; Wazuh is not affected | The UI is down; a public status page |

Rules: when the model is down, never fall back to anything that decides on its own; never fail over to a model or region outside the EU. A fallback model is allowed only if it is in the EU and has passed the same golden set (D6).

**Decision (2026-11-10): as above.** Proposed by the agent and accepted by me.

## D8. How the fix-first queue is ordered
Context: the lab has 105 Critical and 1861 High findings on one host ([`lab/api/08`](lab/api/08-indexer-vulnerabilities-by-severity.json)); ordering by severity alone leaves a list of almost 2000 "urgent" items. Wazuh 4.x does not use KEV or EPSS ([note](sources/design-ranking-wazuh-kev-epss-support.md)).

| Option | For | Against |
|--------|-----|---------|
| A. Severity (CVSS) only | Simple | Adds nothing to what Wazuh shows |
| **B. Fixed tiers computed by rules; the AI only explains** | Useful, explainable and reproducible: the same data always gives the same order | KEV and EPSS must be downloaded daily (free) |
| C. The AI orders freely | Could weigh nuances | Not reproducible, hard to audit |

Tiers in B: (1) CVE in CISA KEV ([note](sources/design-ranking-cisa-kev.md)); (2) high EPSS ([note](sources/design-ranking-first-epss.md)); (3) within a tier, assets the user marked as important (internet-facing, production; see D2); (4) CVSS only as a tie-breaker. KEV goes first regardless of EPSS, and EPSS is not multiplied by CVSS, as FIRST advises ([note](sources/design-ranking-first-epss.md)). The queue lists actions, not CVEs: "upgrade package X on 12 hosts → closes 340 findings, 2 in KEV". The AI writes the reason for each position; the order is computed by the rules.

**Decision (2026-11-10): B.** Recommended by the agent and chosen by me.
