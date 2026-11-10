# Prompt 01 (R5): how an external service can read vulnerability data from Wazuh, safely

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with prompt 02)
- Plan step: Phase 3, Step 2 (`workflow/plans/02-phase3.md`)

## Prompt

> Context: Phase 3 designs a SaaS service that reads the vulnerability findings and package
> inventory of a customer's Wazuh 4.x deployment (latest 4.x) and stores triage decisions outside
> the cluster. It must read with the least privilege possible and never write to Wazuh.
>
> Research question: **How can an external service read vulnerability findings and the package
> inventory from Wazuh 4.x, and how is that access authenticated and restricted?**
>
> Cover, using official sources first (documentation.wazuh.com for the latest 4.x, the
> `wazuh/wazuh` and `wazuh/wazuh-indexer` repos, the Wazuh API reference):
> 1. Where vulnerability findings live since 4.8: the `wazuh-states-vulnerabilities-*` index in
>    the Wazuh indexer, its main fields, and whether the Wazuh server API still exposes a
>    vulnerability endpoint (it existed before 4.8). How the docs say to query them.
> 2. Package and OS inventory: the syscollector endpoints of the Wazuh server API (and the
>    inventory indices in the indexer, if the docs mention them for 4.x).
> 3. Wazuh server API authentication: `POST /security/user/authenticate`, JWT lifetime and how
>    it is configured, how to create a user with a read-only role (RBAC: roles, policies, rules),
>    and any built-in read-only role.
> 4. Wazuh indexer access control: internal users, roles and permissions to give a user
>    read-only access to one index pattern (the OpenSearch security plugin as documented by
>    Wazuh).
> 5. Network: default ports (55000 API, 9200 indexer) and any Wazuh guidance about exposing them
>    to the internet or restricting them.
> 6. How existing third-party integrations read Wazuh data (only if documented by Wazuh).
>
> Output: topic notes under `research/sources/` with the prefix `design-wazuh-access-`
> (for example `design-wazuh-access-vulnerability-index.md`, `design-wazuh-access-rbac.md`).
> At most 4 notes. Topic notes may use `url: multiple, see claims`. Use the note template from
> your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent endpoints, field names, ports, versions or defaults; if a page cannot
> be fetched, say so; mark confidence; keep inference apart from claims; no personal data;
> English only.
>
> When done, reply with at most 10 lines: files written and the main facts the design can rely on.
