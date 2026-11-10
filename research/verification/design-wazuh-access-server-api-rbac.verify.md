---
note: research/sources/design-wazuh-access-server-api-rbac.md
verified: 2026-11-10
result: NEEDS FIXES
---

## Claims
| # | Verdict | Explanation |
|---|---------|-------------|
| 1 | SUPPORTED | spec.yaml (read only the first 100k of ~732k characters): "Perform a call with `basicAuth` to `POST /security/user/authenticate` and obtain a JWT token to run any endpoint." Getting-started page also shows POST with basic auth. |
| 2 | SUPPORTED | Viewing-inventory page: `TOKEN=$(curl -u <USER> -k -X GET "https://<WAZUH_SERVER_IP>:55000/security/user/authenticate?raw=true")`. |
| 3 | PARTIAL | The cited configuration page confirms `auth_token_exp_timeout` default 900, "Set how many seconds it takes for JWT tokens to expire", and "changing the security configuration revokes all JWTs". `PUT /security/config` is stated only in spec.yaml, which is not the URL cited for this claim. |
| 4 | SUPPORTED | Getting-started: default credential `wazuh:wazuh`, "This should be changed after installation to avoid vulnerabilities."; password retrievable from `wazuh-install-files.tar`. |
| 5 | SUPPORTED | RBAC how-it-works: policies = "Specific permissions that define allowed actions on resources"; "You assign roles to users instead of individual policies." |
| 6 | SUPPORTED | Configuration page: `rbac_mode` default white; "By default, everything is allowed in black mode while everything is denied in white mode." |
| 7 | SUPPORTED | RBAC reference lists the roles administrator, agents_admin, agents_readonly, cluster_admin, cluster_readonly, readonly, users_admin. `readonly`: "Read only role, this role can read all the information of the system." with the 11 listed policies (agents_read ... syscollector_read). |
| 8 | PARTIAL | `syscollector_read`: description "Allow reading agents information.", action `syscollector:read` on `agent:id:*`, effect allow: confirmed. The `agents_read` body (`agent:read` on `agent:id:*` and `agent:group:*`, `group:read` on `group:id:*`) was not seen in the tool output. |
| 9 | PARTIAL | The exact sentence "This endpoint applies the action `agent:read` on the resource `agent:id` or `agent:group`." is on the page. The example `GET /agents` was not confirmed in the tool output. |
| 10 | SUPPORTED | RBAC configuration page: POST /security/policies, /roles, /users, `/roles/{role_id}/policies?policy_ids=`, `/users/{user_id}/roles?role_ids=`, optional `/security/rules` and `/roles/{role_id}/rules?rule_ids=`; `allow_run_as` false by default. |
| 11 | SUPPORTED | Securing-API page: "The default limit is 300 requests per minute." (`max_request_per_minute`, 0 disables); "By default, you're allowed 50 login attempts per 300-second period" (`max_login_attempts`, `block_time`). |
| 12 | SUPPORTED | Securing-API page: `host` default `['0.0.0.0', '::']`, `port: 55000`, "edit the Wazuh server API configuration in `/var/ossec/api/configuration/api.yaml`". |
| 13 | SUPPORTED | HTTPS enabled by default, self-signed certificate generated, own certificate recommended. The exact quote about the dashboard-to-API channel was not seen verbatim, but the claim itself holds. |

## Note-level problems
- Claim 3 mixes two sources under one URL.
- Open questions: "The securing-API page gives no explicit advice against internet exposure of port 55000" is a statement of absence; the fetch tool summary of that page did not mention such advice, but I could not verify absence over the whole page.
- Front matter complete; confidence levels fit. Inferences are labelled. No personal data. English.

## Recommended fixes
- Claim 3: cite spec.yaml (or getting-started) for `PUT /security/config`, or drop it.
- Claim 8: keep `medium`; mark the `agents_read` body UNVERIFIED or re-read it.
- Claim 9: remove "such as `GET /agents`" or re-check it.
