---
title: Wazuh server API authentication, JWT lifetime and RBAC for a read-only client
url: multiple, see claims
publisher: Wazuh (documentation.wazuh.com)
source_type: official-docs
wazuh_version: "current" docs (navigation lists 4.14.10 as latest); spec.yaml at tag v4.14.0
accessed: 2026-11-10
question: How can an external service read vulnerability findings and the package inventory from Wazuh 4.x, and how is that access authenticated and restricted?
---

## Summary
The Wazuh server API (port 55000) issues a JWT on `POST /security/user/authenticate` with basic auth; tokens expire after 900 seconds by default (`auth_token_exp_timeout`, changed with `PUT /security/config`). Access is controlled by RBAC: users get roles, roles group policies (actions on resources) and optional rules; the default mode is white list. There is a built-in `readonly` role and narrower ones such as `agents_readonly`; custom least-privilege roles can be built from policies like `syscollector_read`. The API listens on all interfaces by default and has rate and login-attempt limits.

## Claims
1. Tokens are obtained with basic auth on `POST /security/user/authenticate`.
   - Quote: "Perform a call with `basicAuth` to `POST /security/user/authenticate`"
   - Source: https://raw.githubusercontent.com/wazuh/wazuh/v4.14.0/api/api/spec/spec.yaml (also https://documentation.wazuh.com/current/user-manual/api/getting-started.html)
   - Confidence: high

2. A docs example also obtains a raw token with GET on the same path.
   - Quote: "TOKEN=$(curl -u <USER> -k -X GET \"https://<WAZUH_SERVER_IP>:55000/security/user/authenticate?raw=true\")"
   - Source: https://documentation.wazuh.com/current/user-manual/capabilities/system-inventory/viewing-system-inventory-data.html
   - Confidence: high

3. JWT lifetime default is 900 seconds, set by `auth_token_exp_timeout`; it is changed with an authorised `PUT /security/config` (this endpoint is shown in the API spec, not on the cited configuration page), and changing the security config revokes all JWTs.
   - Quote: "Set how many seconds it takes for JWT tokens to expire." (default "900") / "For security reasons, changing the security configuration revokes all JWTs."
   - Source: https://documentation.wazuh.com/current/user-manual/api/configuration.html
   - Confidence: high

4. Default API credential is `wazuh:wazuh` and should be changed after installation (installation-script deployments store the generated password in `wazuh-install-files.tar`).
   - Quote: "The default Wazuh server API credential is `wazuh:wazuh`" ... "This should be changed after installation to avoid vulnerabilities."
   - Source: https://documentation.wazuh.com/current/user-manual/api/getting-started.html
   - Confidence: high

5. RBAC model: users, roles, rules and policies; roles are assigned to users, not policies.
   - Quote: "Specific permissions that define allowed actions on resources." (policies) / "You assign roles to users instead of individual policies."
   - Source: https://documentation.wazuh.com/current/user-manual/api/rbac/how-it-works.html
   - Confidence: high

6. Default `rbac_mode` is white (deny everything not allowed).
   - Quote: "By default, everything is allowed in black mode while everything is denied in white mode."
   - Source: https://documentation.wazuh.com/current/user-manual/api/configuration.html
   - Confidence: high

7. Built-in roles include administrator, agents_admin, agents_readonly, cluster_admin, cluster_readonly, readonly, users_admin. The `readonly` role reads everything and includes the policies agents_read, ciscat_read, cluster_read, decoders_read, lists_read, mitre_read, rootcheck_read, rules_read, sca_read, syscheck_read, syscollector_read.
   - Quote: "Read only role, this role can read all the information of the system."
   - Source: https://documentation.wazuh.com/current/user-manual/api/rbac/reference.html
   - Confidence: high

8. Default policy `syscollector_read` grants `syscollector:read` on `agent:id:*` (allow); `agents_read` grants `agent:read` on `agent:id:*` and `agent:group:*`, and `group:read` on `group:id:*` (the `agents_read` body was not confirmed by the verifier).
   - Quote: "Allow reading agents information." (syscollector_read description)
   - Source: https://documentation.wazuh.com/current/user-manual/api/rbac/reference.html
   - Confidence: medium (policy bodies read through a summarising fetch tool)

9. `agent:read` covers endpoints such as `GET /agents` and applies to `agent:id` or `agent:group` (the `GET /agents` example was not confirmed by the verifier).
   - Quote: "This endpoint applies the action `agent:read` on the resource `agent:id` or `agent:group`."
   - Source: https://documentation.wazuh.com/current/user-manual/api/rbac/reference.html
   - Confidence: high

10. Documented steps to create a least-privilege API user: `POST /security/policies` (actions, resources, effect), `POST /security/roles`, `POST /security/roles/{role_id}/policies?policy_ids=`, `POST /security/users` (username, password), `POST /security/users/{user_id}/roles?role_ids=`; optional rules via `POST /security/rules` and `POST /security/roles/{role_id}/rules?rule_ids=`. New users have `allow_run_as` false by default.
   - Quote: (steps read through a summarising fetch tool) "POST /security/users/{user_id}/roles?role_ids="
   - Source: https://documentation.wazuh.com/current/user-manual/api/rbac/configuration.html
   - Confidence: medium

11. Rate and login limits: 300 requests per minute by default (`max_request_per_minute`, 0 disables), 50 login attempts per 300-second period by default (`max_login_attempts`, `block_time`).
   - Quote: "The default limit is 300 requests per minute." / "By default, you're allowed 50 login attempts per 300-second period"
   - Source: https://documentation.wazuh.com/current/user-manual/api/securing-api.html
   - Confidence: high

12. The API listens on all interfaces by default (`host: ['0.0.0.0', '::']`, `port: 55000` in `/var/ossec/api/configuration/api.yaml`); the docs say to edit this file to restrict access.
   - Quote: "To restrict access, edit the Wazuh server API configuration in `/var/ossec/api/configuration/api.yaml`."
   - Source: https://documentation.wazuh.com/current/user-manual/api/securing-api.html
   - Confidence: high

13. HTTPS is on by default with a self-signed certificate; the docs recommend using your own certificate.
   - Quote: "The communication between the Wazuh dashboard and the Wazuh server API is encrypted with HTTPS by default."
   - Source: https://documentation.wazuh.com/current/user-manual/api/securing-api.html
   - Confidence: high

## Inference
- Inference: the built-in `readonly` role is broader than needed (rules, decoders, CDB lists, cluster info). A dedicated role with only `syscollector_read` and `agents_read` (or a custom policy on chosen `agent:group:<name>`) is the least-privilege option for inventory via the server API.
- Inference: none of these policies grants vulnerability data, because there is no vulnerability endpoint in 4.8+; the server API alone is not enough for the design.
- Inference: a 900 s JWT means the service re-authenticates with basic auth on a schedule; the service must store the API password (not only a token), so it should be a dedicated user that the customer can revoke.

## Open questions
- UNVERIFIED: whether the authorization-context (`run_as`) login is useful for a SaaS reader; not needed for basic least privilege.
- The securing-API page gives no explicit advice against internet exposure of port 55000 (it only documents host binding).

## Not read
- https://documentation.wazuh.com/current/user-manual/api/reference.html - ReDoc page did not render in the fetch tool.
- https://groups.google.com/g/wazuh/c/g3AjERT4yjg ("How to create a read-only user for the API") - seen in search results only; no claims made.
