---
title: Wazuh indexer access control, ports, network exposure and how integrations read data
url: multiple, see claims
publisher: Wazuh (documentation.wazuh.com); OpenSearch Project (docs.opensearch.org)
source_type: official-docs
wazuh_version: "current" docs (navigation lists 4.14.10 as latest); one 5.0-rc page marked as such; OpenSearch docs 2.19
accessed: 2026-11-10
question: How can an external service read vulnerability findings and the package inventory from Wazuh 4.x, and how is that access authenticated and restricted?
---

## Summary
The Wazuh indexer REST API listens on TCP 9200 and uses HTTP basic authentication by default; it can also issue short-lived on-behalf-of JWTs if enabled. Wazuh documents creating a read-only indexer user through the dashboard (internal user plus a role with `cluster_composite_ops_ro` and `read` on an index pattern); the underlying OpenSearch security plugin also supports creating roles, mappings and users through `_plugins/_security/api/`. Wazuh advises restricting network access to the indexer to trusted networks and offers an endpoint allowlist. Wazuh's own third-party integration guide (Logstash) reads the indexer on 9200 with administrator credentials.

## Claims
1. Default ports: 55000/TCP for the Wazuh server RESTful API and 9200/TCP for the Wazuh indexer RESTful API; both can be changed.
   - Quote: "Wazuh server RESTful API" (55000, TCP) / "Wazuh indexer RESTful API" (9200, TCP) / "Users can modify these port numbers when necessary."
   - Source: https://documentation.wazuh.com/current/getting-started/architecture.html
   - Confidence: high

2. Indexer API uses HTTP basic auth by default on TCP 9200 and requires authentication.
   - Quote: "HTTP basic authentication is enabled by default" / "listens for incoming requests on TCP port `9200` and requires authentication"
   - Source: https://documentation.wazuh.com/current/user-manual/indexer-api/getting-started.html
   - Confidence: high

3. The indexer can issue JWTs via `POST /_plugins/_security/api/generateonbehalfoftoken` after enabling `on_behalf_of` (signing and encryption keys) in `/etc/wazuh-indexer/opensearch-security/config.yml`; the request sets `durationSeconds` (example 180) and the token is sent as `Authorization: Bearer`.
   - Quote: "curl -k -u <WAZUH_INDEXER_USER>:<WAZUH_INDEXER_PASSWORD> -XPOST \"https://localhost:9200/_plugins/_security/api/generateonbehalfoftoken\""
   - Source: https://documentation.wazuh.com/current/user-manual/indexer-api/getting-started.html
   - Confidence: high

4. Wazuh documents a read-only indexer user via the dashboard: create an internal user (Indexer management > Security > Internal users), create a role with cluster permission `cluster_composite_ops_ro`, index pattern with `read` permission, `global_tenant` read-only, then map the user to the role. The docs use index pattern `*`.
   - Quote: (steps read through a summarising fetch tool) cluster permission "cluster_composite_ops_ro", index permission "read"
   - Source: https://documentation.wazuh.com/current/user-manual/user-administration/rbac.html
   - Confidence: medium

5. The same page warns not to map read-only users to `kibana_user` / `kibanauser` because they grant write access to dashboard settings.
   - Quote: (read through a summarising fetch tool) do not map the user to `kibana_user` or the `kibanauser` backend role.
   - Source: https://documentation.wazuh.com/current/user-manual/user-administration/rbac.html
   - Confidence: medium

6. OpenSearch security REST API: create a role with `PUT _plugins/_security/api/roles/<role>` whose body has `cluster_permissions`, `index_permissions` (with `index_patterns`, `allowed_actions` such as `read`, optional `dls`/`fls`/`masked_fields`) and `tenant_permissions`; map with `PUT _plugins/_security/api/rolesmapping/<role>`; create a user with `PUT _plugins/_security/api/internalusers/<username>`.
   - Quote: "PUT _plugins/_security/api/roles/<role>" / "PUT _plugins/_security/api/rolesmapping/<role>" / "PUT _plugins/_security/api/internalusers/<username>"
   - Source: https://docs.opensearch.org/2.19/security/access-control/api/
   - Confidence: medium (OpenSearch upstream docs; the OpenSearch version under Wazuh indexer 4.14 was not confirmed)

7. OpenSearch predefined role `readall` grants search on all indexes (broader than one index pattern).
   - Quote: "Grants permissions for cluster-wide searches like `msearch` and search permissions for all indexes."
   - Source: https://docs.opensearch.org/2.19/security/access-control/users-roles/
   - Confidence: medium

8. Wazuh advises restricting network access to the indexer to trusted networks, using security groups and firewalls.
   - Quote: "We advise restricting network access to the Wazuh indexer." / "limit the exposure of the Wazuh indexer API to only trusted networks"
   - Source: https://documentation.wazuh.com/current/user-manual/indexer-api/securing-indexer-api.html
   - Confidence: high

9. The 5.0-rc version of the same page states the port explicitly (not 4.x, kept for context).
   - Quote: "Expose the Wazuh indexer API port, `9200` by default, only to trusted networks."
   - Source: https://documentation.wazuh.com/5.0-rc/user-manual/indexer-api/securing-indexer-api.html
   - Confidence: medium (pre-release docs)

10. The indexer supports an endpoint/method allowlist in `/etc/wazuh-indexer/opensearch-security/allowlist.yml`, explicit-deny, not applied to the `admin` user; changes are loaded with `securityadmin.sh`.
   - Quote: "only the endpoints specified in the allowlist are accessible" / "This does not apply to the admin user."
   - Source: https://documentation.wazuh.com/current/user-manual/indexer-api/securing-indexer-api.html
   - Confidence: high

11. The docs recommend changing its default password (`PUT _plugins/_security/api/account`).
   - Quote: "The password for the default administrative user admin can be changed via the Wazuh dashboard"
   - Source: https://documentation.wazuh.com/current/user-manual/indexer-api/securing-indexer-api.html
   - Confidence: high

12. Wazuh's integrations guide (Elastic Stack, OpenSearch, Splunk, Amazon Security Lake) documents two methods: a "Wazuh indexer integration" that forwards data from the indexer, and a "Wazuh server integration" that reads `/var/ossec/logs/alerts/alerts.json`.
   - Quote: "forwards analyzed security data from the Wazuh indexer to the third-party security platform indexer" / "operates by reading the /var/ossec/logs/alerts/alerts.json file"
   - Source: https://documentation.wazuh.com/current/integrations-guide/index.html
   - Confidence: high

13. The Elastic Stack guide's Logstash input polls the indexer on 9200 every minute (`schedule => "* * * * *"`, range `now-1m` on `@timestamp`, index `wazuh-alerts-4.x-*`) and uses the "Wazuh indexer administrator username and password" from the Logstash keystore; it does not describe a least-privilege user.
   - Quote: "hosts => [\"<WAZUH_INDEXER_ADDRESS>:9200\"]" / "Wazuh indexer administrator username and password"
   - Source: https://documentation.wazuh.com/current/integrations-guide/elastic-stack/index.html
   - Confidence: high

## Inference
- Inference: the least-privilege indexer identity for the design is a dedicated internal user mapped to a custom role with `read` (search) on only `wazuh-states-vulnerabilities-*` and `wazuh-states-inventory-packages-*` / `-system-*`, plus the minimum cluster permission; no write, no admin. Wazuh's own example uses `*` and the integration guide uses admin, so the design is stricter than the documented examples.
- Inference: the allowlist does not restrict non-admin users to specific indices in a fine-grained way (it is per endpoint and method); index-level restriction should come from the role, network restriction from customer firewalls.
- Inference: since Wazuh advises limiting 9200 to trusted networks, a SaaS should not require customers to expose 9200 or 55000 to the internet; an outbound connector inside the customer network (pull locally, push to SaaS) or a fixed-IP allowlist are the two options consistent with that guidance.
- Inference: on-behalf-of JWTs could give short-lived indexer tokens, but they must be minted with basic-auth credentials and need extra config, so they do not remove the need for a stored credential.

## Open questions
- UNVERIFIED: the OpenSearch version under Wazuh indexer 4.14 (not stated in the 4.14.0 release notes read).
- UNVERIFIED: exact minimum cluster permission for `_search` over an index pattern (Wazuh uses `cluster_composite_ops_ro`; not tested).
- No official 4.x Wazuh statement was found that explicitly says "do not expose port 55000 to the internet".

## Not read
- https://documentation.wazuh.com/current/user-manual/wazuh-indexer/security.html - HTTP 404 (page exists only in 5.0 docs).
- https://documentation.wazuh.com/5.0-rc/user-manual/wazuh-indexer/security.html and https://wazuh.github.io/wazuh-indexer-plugins/ref/security/access-control.html - seen in search results, not fetched; they target 5.x.
- https://groups.google.com/g/wazuh/c/gb5RDmy1Yfo ("Read-Only rights for Vulnerability Dashboard Only") - seen in search results only; no claims made.
