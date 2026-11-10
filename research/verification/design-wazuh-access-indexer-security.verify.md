---
note: research/sources/design-wazuh-access-indexer-security.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | Architecture page: server REST API TCP 55000, indexer REST API TCP 9200, "Users can modify these port numbers when necessary." |
| 2 | SUPPORTED | Indexer API getting-started: "HTTP basic authentication is enabled by default"; "listens for incoming requests on TCP port `9200` and requires authentication". |
| 3 | SUPPORTED | `on_behalf_of` is not enabled by default; set in `config.yml` with signing and encryption keys; `POST https://localhost:9200/_plugins/_security/api/generateonbehalfoftoken`, `durationSeconds` example "180"; used as `Authorization: Bearer`. |
| 4 | SUPPORTED | RBAC page: internal user, role with `cluster_composite_ops_ro`, index `*` with `read`, `global_tenant` read only, mapping. |
| 5 | SUPPORTED | Warning not to map to `kibana_user` role or `kibanauser` backend role (write access to dashboard configuration). |
| 6 | SUPPORTED | OpenSearch 2.19 API page: PUT roles (cluster_permissions, index_permissions with index_patterns, allowed_actions, dls, fls, masked_fields; tenant_permissions), rolesmapping, internalusers. Read through a summarising tool; the OpenSearch version under Wazuh indexer 4.14 is not stated (flagged in the note). |
| 7 | SUPPORTED | Users-roles page: `readall` "Grants permissions for cluster-wide searches like `msearch` and search permissions for all indexes." |
| 8 | SUPPORTED | Securing-indexer-API page advises restricting network access with security groups or firewalls to trusted networks. Exact quote wording came through the summariser. |
| 9 | SUPPORTED | 5.0-rc page: "Expose the Wazuh indexer API port, 9200 by default, only to trusted networks." |
| 10 | SUPPORTED | `allowlist.yml` in `/etc/wazuh-indexer/opensearch-security/`; "only the endpoints specified in the allowlist are accessible"; admin exempt; `securityadmin.sh` loads changes. |
| 11 | PARTIAL | Page recommends changing the default password of the built-in `admin` user, in the dashboard or with `PUT _plugins/_security/api/account`. "The installer creates" the user and "administrative access to the indexer API" are not stated as such, and the quoted wording differs from what the page returned ("It is recommended that the default password is changed"). |
| 12 | SUPPORTED | Integrations guide: indexer integration "forwards analyzed security data from the Wazuh indexer to the third-party security platform indexer"; server integration "operates by reading the /var/ossec/logs/alerts/alerts.json file"; platforms Elastic Stack, OpenSearch, Splunk, Amazon Security Lake. |
| 13 | SUPPORTED | Elastic Stack guide: `hosts => ["<WAZUH_INDEXER_ADDRESS>:9200"]`, `schedule => "* * * * *"`, range `now-1m` on `@timestamp`, index `wazuh-alerts-4.x-*`, credentials from the Logstash keystore using the indexer administrator's credentials. "Does not describe a least-privilege user" is an absence, consistent with the summary. |

## Note-level problems
- Claim 11 attributes installer behaviour to the page; the page only says the default admin password should be changed.
- Several quotes are marked "read through a summarising fetch tool"; confidence `medium` on those is appropriate.
- Front matter complete (publisher lists two sites, valid). Inferences are labelled. No personal data. English.

## Recommended fixes
- Claim 11: rephrase as "Wazuh recommends changing the default password of the built-in `admin` user (dashboard, or `PUT _plugins/_security/api/account`)" and drop "the installer creates", or cite a page that says it.
