---
note: research/sources/design-wazuh-access-inventory.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | System inventory index page: "This information is processed on the Wazuh server and then sent to the Wazuh indexer, where it is stored as global state data." |
| 2 | SUPPORTED | Available fields page: `sys_programs` data is indexed under `wazuh-states-inventory-packages-*`, `sys_osinfo` under `wazuh-states-inventory-system-*`. |
| 3 | SUPPORTED | All 12 `package.*` fields match. Host fields `host.hostname`, `host.architecture`, `host.os.name/version/full/platform/kernel.release/type` and more are listed. |
| 4 | SUPPORTED | Indices page lists hardware, hotfixes, interfaces, networks, packages, ports, processes, protocols, system, browser-extensions, services, groups, users. |
| 5 | SUPPORTED | Viewing page: indexer `_search` on `wazuh-states-inventory-packages-*` at port 9200, with a term query on `package.name` and a bool query using term on `agent.name`. |
| 6 | SUPPORTED | Same page: token via `GET .../security/user/authenticate?raw=true`, then `GET :55000/syscollector/<AGENT_ID>/<SYSCOLLECTOR_PROPERTY>?pretty=true`; example `/syscollector/010/packages`. |
| 7 | SUPPORTED | RBAC reference lists `GET /syscollector/{agent_id}/` hardware, hotfixes, netaddr, netiface, netproto, os, packages, ports, processes, users, groups, browser_extensions, services, plus `GET /experimental/syscollector/...` (including packages and os), with resources `agent:id` and `agent:group`. |
| 8 | PARTIAL | Configuration page shows `experimental_features`, default false, "features under development". The page does not say that the `/experimental/...` endpoints depend on it. The link is the researcher's own inference (already flagged medium, and repeated in Inference). |
| 9 | SUPPORTED | 4.14.0 release notes: "Added Syscollector users and groups endpoints." and "Added Syscollector services and `browser_extensions` endpoints." |

## Note-level problems
- Claim 8 states as fact a dependency (`experimental_features` gates `/experimental/`) that no cited page states. The Inference section says "probably", so the claim text contradicts it.
- Claim 5 "Open questions" and the "Not read" list are honest. Front matter complete. No personal data. English.

## Recommended fixes
- Claim 8: split into the verified part (the option exists, default false, "enable features under development") and move the link to `/experimental` endpoints to Inference only.
