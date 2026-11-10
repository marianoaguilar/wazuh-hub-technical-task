---
title: Reading package and OS inventory from Wazuh 4.x (syscollector API and inventory indices)
url: multiple, see claims
publisher: Wazuh (documentation.wazuh.com)
source_type: official-docs
wazuh_version: "current" docs (examples use agent v4.14.0; navigation lists 4.14.10 as latest); 4.14.0 release notes
accessed: 2026-11-10
question: How can an external service read vulnerability findings and the package inventory from Wazuh 4.x, and how is that access authenticated and restricted?
---

## Summary
Wazuh 4.x offers two documented ways to read package and OS inventory: the Wazuh server API syscollector endpoints on port 55000 (per agent, plus experimental cross-agent endpoints) and the `wazuh-states-inventory-*` indices in the Wazuh indexer on port 9200. Packages are in `wazuh-states-inventory-packages-*` and OS data in `wazuh-states-inventory-system-*`; the docs list their fields and give `_search` examples. Reading syscollector data needs the RBAC action `syscollector:read`.

## Claims
1. Inventory data is processed on the server and stored in the indexer as global state data.
   - Quote: "This information is processed on the Wazuh server and then sent to the Wazuh indexer, where it is stored as global state data."
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/index.html
   - Confidence: high

2. Packages are indexed in `wazuh-states-inventory-packages-*` and OS data in `wazuh-states-inventory-system-*`.
   - Quote: "indexed in the Wazuh indexer under the `wazuh-states-inventory-packages-*` indices"
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/available-inventory-fields.html
   - Confidence: high

3. Documented package fields: `package.type`, `package.name`, `package.priority`, `package.size`, `package.vendor`, `package.installed`, `package.version`, `package.architecture`, `package.multiarch`, `package.source`, `package.description`, `package.path`. Documented OS fields include `host.hostname`, `host.architecture`, `host.os.name`, `host.os.version`, `host.os.full`, `host.os.platform`, `host.os.kernel.release`, `host.os.type` and others.
   - Quote: (field list, read through a summarising fetch tool) "package.name", "package.version", "host.os.platform"
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/available-inventory-fields.html
   - Confidence: medium

4. The indexer page lists the full set of 4.x inventory indices: hardware, hotfixes, interfaces, networks, packages, ports, processes, protocols, system, browser-extensions, services, groups, users (all `wazuh-states-inventory-<name>-*`).
   - Quote: "`wazuh-states-inventory-packages-*`" (table row: installed software packages)
   - Source: https://documentation.wazuh.com/current/user-manual/wazuh-indexer/wazuh-indexer-indices.html
   - Confidence: high

5. The docs give an indexer `_search` example for packages on port 9200, with term queries on `package.name` and `agent.name`.
   - Quote: "curl -k -u \"<WAZUH_INDEXER_USERNAME>\" https://<WAZUH_INDEXER_IP>:9200/wazuh-states-inventory-packages-*/_search?pretty"
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/viewing-system-inventory-data.html
   - Confidence: high

6. The same page shows the server API path on port 55000: get a token, then call `/syscollector/<AGENT_ID>/<SYSCOLLECTOR_PROPERTY>` (example `/syscollector/010/packages`).
   - Quote: "curl -k -X GET \"https://<WAZUH_SERVER_IP>:55000/syscollector/<AGENT_ID>/<SYSCOLLECTOR_PROPERTY>?pretty=true\""
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/viewing-system-inventory-data.html
   - Confidence: high

7. The `syscollector:read` action covers per-agent endpoints `GET /syscollector/{agent_id}/` hardware, hotfixes, netaddr, netiface, netproto, os, packages, ports, processes, users, groups, browser_extensions, services, and experimental cross-agent endpoints such as `GET /experimental/syscollector/packages` and `GET /experimental/syscollector/os`. Resources: `agent:id` and `agent:group`.
   - Quote: "GET /syscollector/{agent_id}/packages" ... "GET /experimental/syscollector/packages"
   - Source: https://documentation.wazuh.com/current/user-manual/api/rbac/reference.html
   - Confidence: high

8. Inference (not stated by any cited page): the `/experimental/...` endpoints depend on the API option `experimental_features`, which is off by default.
   - Quote: "Enable features under development" (default "false")
   - Source: https://documentation.wazuh.com/current/user-manual/api/configuration.html
   - Confidence: medium (the link between the option and the `/experimental` prefix is not stated in the quoted row; see Inference)

9. Wazuh 4.14.0 added syscollector API endpoints for users, groups, services and browser extensions.
   - Quote: "Added Syscollector users and groups endpoints." / "Added Syscollector services and `browser_extensions` endpoints."
   - Source: https://documentation.wazuh.com/current/release-notes/release-4-14-0.html
   - Confidence: high

## Inference
- Inference: the indexer path is the better fit for a SaaS reader: one credential type (indexer) for both vulnerabilities and packages, cross-agent queries without experimental features, and the same `agent.*`/`package.*` field names in both indices so they can be joined.
- Inference: the server API path is per agent (one call per agent and property), which scales poorly for large fleets, but it is the only path that can be scoped per agent or agent group with Wazuh RBAC (`agent:id`, `agent:group` resources).
- Inference: `experimental_features` probably gates the `/experimental/` endpoints by name; a design should not depend on them in customer clusters.

## Open questions
- UNVERIFIED: pagination limits and parameters of the syscollector endpoints (`limit`, `offset`, `select`) were not read in the API reference (the ReDoc page did not render in the fetch tool).
- UNVERIFIED: whether inventory indices exist and are populated when the indexer connector is not configured on the manager.

## Not read
- https://documentation.wazuh.com/current/user-manual/api/reference.html - ReDoc page, body did not render in the fetch tool.
- https://raw.githubusercontent.com/wazuh/wazuh/v4.14.0/api/api/spec/spec.yaml - fetched but too large; only `info.version: '4.14.0'` and the authenticate description were read, no endpoint claims made from it.
