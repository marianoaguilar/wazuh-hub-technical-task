# PHASE 2

**Short answer.** I chose **vulnerability triage**. Wazuh finds vulnerable packages well, but in 4.x users have asked for years for a way to record what they decided about each finding (false positive, accepted risk, fix later), and it has not been delivered; they also lack a view of what to fix first. The idea is a SaaS service that keeps those decisions outside the cluster, uses AI to explain likely false positives and ranks the rest into a short "fix first" list.

**How I got here.** I started from my own lab (Phase 1), then ran four research runs with AI agents: who uses Wazuh, problems on GitHub, problems in the community, and what already exists. Each run wrote sourced notes, and a separate verifier agent checked every claim against its URL. Only verified claims are used below. Everything is in [`research/`](research/README.md): the notes, the verification reports, the scored catalogue of needs ([`phase2-needs.md`](research/phase2-needs.md)), the service ideas ([`phase2-ideas.md`](research/phase2-ideas.md)) and the AI mistakes I corrected ([`ai-log.md`](research/ai-log.md)).

**Limits of the evidence.** Community evidence comes mostly from the public Wazuh Google Group and PeerSpot. Reddit, G2, Capterra and Gartner could not be read. Thread counts are our own classification of search results, so they are signals, not statistics.

## Which needs did you find, and where did each one come from?

I found nine needs. The table shows where each one came from; the full evidence, with the notes and quotes behind it, is in [`research/phase2-needs.md`](research/phase2-needs.md).

| # | Need | Where it came from |
|---|------|--------------------|
| N1 | **Vulnerability triage**: acknowledge, explain and prioritise CVE findings | GitHub issues, the Wazuh Google Group and my lab (details in the third answer) |
| N2 | **Alert noise**: finding noisy rules and tuning them safely | The most reacted bug in `wazuh/wazuh` is a rootcheck false positive ([#19346](https://github.com/wazuh/wazuh/issues/19346), 47 👍); forum tuning threads; my lab (a repeating rule 40704 alert) |
| N3 | **Custom decoders and rules** for unsupported log formats | Fields that cannot be decoded ([#21706](https://github.com/wazuh/wazuh/issues/21706)); rules by agent label requested since 2019 ([#3130](https://github.com/wazuh/wazuh/issues/3130)). |
| N4 | **Reporting and compliance reports** | "Automatic reports in the UI" requested since 2019 ([#1492](https://github.com/wazuh/wazuh-dashboard-plugins/issues/1492)), ISO 27001 content ([#4091](https://github.com/wazuh/wazuh/issues/4091), 32 👍); forum reporting threads |
| N5 | **Explaining alerts** to less experienced users | My lab (hard to interpret events, unclear next steps); 3 of 10 dated [PeerSpot](https://www.peerspot.com/products/wazuh-pros-and-cons) dislikes cite missing AI/ML |
| N6 | **Multi-tenancy for MSSPs** | Filter by agent group ([#14225](https://github.com/wazuh/wazuh/issues/14225)); vulnerability data ignores document-level security ([#24118](https://github.com/wazuh/wazuh/issues/24118)); dashboard tenants only separate saved objects ([docs](https://documentation.wazuh.com/current/user-manual/wazuh-dashboard/multi-tenancy.html)) |
| N7 | **Upgrades that break things** | The most commented community issue in a search for "after upgrade" is an upgrade failure ([#24074](https://github.com/wazuh/wazuh/issues/24074)); others report the same ([#32044](https://github.com/wazuh/wazuh/issues/32044)); about 10 forum threads |
| N8 | **Indexer storage growth** | Disk growth after 4.8 ([#24243](https://github.com/wazuh/wazuh/issues/24243)); forum threads; PeerSpot outage reports |
| N9 | **Getting started**: choosing an install method, what to do next | My lab only; PeerSpot opinions on the docs are split |

To compare them I scored each need from 1 to 3 on six criteria: evidence, pain, SaaS fit, AI fit, not already solved, and data risk. The Hub team builds SaaS services that extend Wazuh with AI, so a need that scores 1 on SaaS fit or AI fit is discarded whatever its total. Scores and reasoning: [`research/phase2-needs.md`](research/phase2-needs.md).

## Which ones did you discard, and why?

| # | Need | Score | Why it was discarded |
|---|------|-------|----------------------|
| N4 | Reporting | 13 | **Already served.** Wazuh 5.0 (pre-release docs) adds scheduled reports with email delivery ([docs](https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-indexer/modules/reporting.html)). The Wazuh Cloud AI Analyst already emails periodic PDF reports ([docs](https://documentation.wazuh.com/current/cloud-service/ai-analyst.html)). |
| N5 | Explaining alerts | 12 | **The most crowded space.** The 5.0 dashboard (pre-release docs) adds an AI Assistant ([docs](https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-dashboard/wazuh-dashboard-configurations.html#ai-assistant)). The Hub already lists Lumen (AI Detection & Response) and Mobius (Agentic SOC) as beta services ([terms](https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_October_26.pdf)), open-source MCP servers exist ([example](https://github.com/gensecaihq/Wazuh-MCP-Server)), and the four main competitors I checked have their own assistants ([note](research/sources/landscape-competitor-ai.md)). Inference: it would also need raw alerts sent to an LLM. |
| N6 | MSSP multi-tenancy | 12 | **AI adds little.** It is data isolation and access control inside the core product, and the partners page already lists a "centralised multi-tenancy console" ([partners](https://wazuh.com/partners/)). |
| N7 | Upgrades | 14 | **Not a SaaS fit.** Fixing it needs access to the customer's hosts and packages. In Wazuh Cloud, Wazuh manages the central components and their infrastructure ([docs](https://documentation.wazuh.com/current/cloud-service/index.html)), so hosted customers do not upgrade them themselves (inference). |
| N8 | Indexer storage | 12 | **No real need for AI.** The advice in the forum is deleting old indices, retention policies, zero replicas on single nodes or adding nodes ([example thread](https://groups.google.com/g/wazuh/c/AfvaXspKhyI)). Inference: that is rule-based advice. |
| N9 | Getting started | 11 | **Weak evidence.** Only my own experience supports it, and PeerSpot opinions on the documentation are split: some reviewers praise it, one cites a learning curve ([reviews](https://www.peerspot.com/products/wazuh-reviews)). |

The shortlist was N1 (16), N2 (15) and N3 (13). N2 and N3 could make one "ruleset tuning" service, and they were the alternative to N1. I kept N1 because it has the strongest and most independent evidence, the clearest workaround that users say does not work, and less sensitive data to send outside (package inventory instead of raw logs).

## Which one did you choose, who would benefit from it and how do they handle it today?

### The need: vulnerability triage
Wazuh correlates each agent's software inventory with vulnerability information from the Wazuh CTI repository ([docs](https://documentation.wazuh.com/current/user-manual/capabilities/vulnerability-detection/index.html)). The problem is what happens next:

- **Too many findings.** Users report "thousands of unfixed CVEs" and say filtering "doesn't scale" to "1000+ CVE/OS/host" combinations ([#26874](https://github.com/wazuh/wazuh/issues/26874)). One user saw about 2,327 findings on an up-to-date Ubuntu 24.04 host ([thread](https://groups.google.com/g/wazuh/c/DfawqXY7yi0)).
- **Many false positives, and users must work out why.** Examples: patched PHP 7.4 packages flagged High because they were compared with the PHP 8.2 fix ([thread](https://groups.google.com/g/wazuh/c/tq7fgojXObg)), and Ubuntu kernel CVEs marked "Solved" after Canonical changed its feed format ([thread](https://groups.google.com/g/wazuh/c/mTUXo6txzTU)).
- **No way to record a decision.** I found no way in 4.x to acknowledge, exclude or annotate a finding, and the requests for it were not delivered. They have existed since 2022: [#4413](https://github.com/wazuh/wazuh-dashboard-plugins/issues/4413) was closed as not planned in March 2026. In [#26819](https://github.com/wazuh/wazuh/issues/26819) a maintainer says exclusions will be done at indexer level in 5.x, with no version given. A roadmap issue, "State case management", proposes triage fields and is **On hold** ([#37485](https://github.com/wazuh/wazuh/issues/37485)).
- **Incomplete history.** Users report that for 4.8.0 agents no alerts are created in `wazuh-alerts-*`, and a reply says that on inventory refresh "by design we will not alert you" ([#24290](https://github.com/wazuh/wazuh/issues/24290)). They say this hurts audits, because there is no full record of when a vulnerability was resolved.

How often it comes up: in the Google Group's default listing, 13 of about 28 visible threads were about vulnerability detection, and a search for "false positive" returned 22 vulnerability threads in the first 30 results ([listing](https://groups.google.com/g/wazuh), [search](https://groups.google.com/g/wazuh/search?q=false%20positive); our classification). I found it myself too: in Phase 1, reviewing which detected vulnerabilities mattered was left as a next step ([note](research/sources/lab-phase1-observations.md), item 6).

### Who would benefit
- **Anyone who uses vulnerability detection.** It is one of Wazuh's documented use cases ([docs](https://documentation.wazuh.com/current/getting-started/use-cases/index.html)), and Groupon lists it among its own ([case study](https://wazuh.com/resources/case-studies/groupon-deploys-wazuh-to-protect-and-monitor-aws/)).
- Inference: **small teams** without time to review findings by hand.
- **MSSPs** that scan vulnerabilities for many clients, such as FirmGuardian ([case study](https://wazuh.com/resources/case-studies/firmguardian-customization-meets-compliance/)). Inference: they face the problem once per client.
- Inference: **teams that go through audits**, which need to show who accepted each risk and why. This links to the incomplete history reported in [#24290](https://github.com/wazuh/wazuh/issues/24290).

### How they handle it today

| Workaround | Why it falls short |
|------------|--------------------|
| Dashboard filters and saved searches | They "don't scale" and do not record who decided, why or when ([#26874](https://github.com/wazuh/wazuh/issues/26874)) |
| Custom suppression rules | They stop new alerts but leave existing findings visible ([#4413](https://github.com/wazuh/wazuh-dashboard-plugins/issues/4413)) |
| Spreadsheets kept by hand | Mentioned by a commenter in [#26819](https://github.com/wazuh/wazuh/issues/26819) |
| Waiting for a feed update, or checking each CVE by hand against distro advisories | Slow, and the same work every time ([thread](https://groups.google.com/g/wazuh/c/1C9sSXLO7b8), [thread](https://groups.google.com/g/wazuh/c/6tYTimSfZmI)) |

### Risk I am aware of
The Wazuh Hub lists a beta service, **Pharos**, in the "Vulnerability & Threat Intelligence" category ([terms](https://wazuh.com/docs/legal-resources/Wazuh_Hub_Beta_Services_Terms_October_26.pdf)). I found no public page that says what it does ([note](research/sources/landscape-pharos-vesper.md)), so I cannot rule out an overlap. Inference: by its category, Pharos is about vulnerability and threat data. My service is about the user's decisions on that data, so it could complement Pharos rather than repeat it.

## Which service ideas did you consider before reaching yours, and what made you drop them?

I listed seven ideas for N1 ([`research/phase2-ideas.md`](research/phase2-ideas.md)). I kept two as one service and turned two more into later features.

| Idea | Decision | Reason |
|------|----------|--------|
| **I1. Triage ledger with AI false-positive review.** Stores a decision per finding (status, reason, owner, expiry) and re-applies it on every sync. AI proposes "likely false positive / real / accepted risk" with its evidence, and a person confirms. | **Chosen (core)** | It fills the gap that [#37485](https://github.com/wazuh/wazuh/issues/37485) describes and that is On hold |
| **I2. "Fix first" queue.** Turns the remaining findings into a few explained actions ("upgrade package X on 12 hosts"). | **Chosen, part of I1** | It answers "too many findings" and reuses I1's data |
| I3. Change explainer and digest | Later feature of I1 | As a standalone report it overlaps with the Wazuh Cloud AI Analyst, whose reports already cover vulnerabilities ([docs](https://documentation.wazuh.com/current/cloud-service/ai-analyst.html)) |
| I4. Compliance evidence pack | Later export of I1 | Reporting is already served (N4); the only new part is the triage history, which I1 already stores |
| I5. Second-opinion scanner (own detection engine) | Dropped | It duplicates the core detector and the Wazuh CTI feed, and is the most likely overlap with Pharos |
| I6. Chat assistant over vulnerabilities | Dropped | Crowded: the 5.0 AI Assistant (pre-release docs) and MCP servers that already expose vulnerability tools ([example](https://github.com/gbrigandi/mcp-server-wazuh)); a chat also does not store decisions |
| I7. Automatic patching of hosts | Dropped | It needs write access to customer hosts (the problem that discarded N7), and response actions are the area of the Hub's Mobius service (see N5) |

### What Phase 3 has to check first
- How Wazuh 4.8+ exposes vulnerability findings (server API or indexer). I will check it in my lab before designing the data flow.
- Whether external data on actively exploited CVEs is worth using to rank the "fix first" queue. It needs its own research and verification.
