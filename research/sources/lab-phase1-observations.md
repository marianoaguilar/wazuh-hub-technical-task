---
title: Observations from my own Wazuh lab (Phase 1)
url: ../../PHASE1.md
publisher: Own lab (Mariano Aguilar Olmo)
source_type: own-lab
wazuh_version: 4.x (Docker deployment of server, indexer and dashboard; agent on Ubuntu host)
accessed: 2026-11-10
question: Which needs of Wazuh users can I see in my own first contact with Wazuh?
---

## Summary
First-hand experience from Phase 1, written by me without AI (in Spanish). It is the
experience of a single new user, so every need below is a **hypothesis** that the web research
(R1–R4) has to confirm or reject. Quotes are translated to English by the main agent; the
original Spanish text is in `PHASE1.md`.

## Claims
1. A noisy, repeating alert filled the dashboard: rule 40704 (systemd, level 5) fired over and
   over because a background service kept failing.
   - Quote (translated): "the 'low severity' alert counter kept rising periodically … all were
     identical and came from systemd rule 40704 (level 5)"
   - Source: `PHASE1.md`, section "Caso 1"; screenshot `screenshots/01_cups_alerts.png`
   - Confidence: high (own observation)
2. Understanding what the alert meant and what to do about it needed outside research, not
   Wazuh itself.
   - Quote (translated): "I started searching the internet about the 'cups-browsed' alert and
     read that it was advisable to disable it"
   - Source: `PHASE1.md`, section "What was hard, and how did you get past it?"
   - Confidence: high (own observation)
3. Interpreting the event data was hard for a new user.
   - Quote (translated): "It was hard to learn how to interpret all the information in the
     events that appeared and see what the real problem was"
   - Source: `PHASE1.md`, section "What was hard, and how did you get past it?"
   - Confidence: high (own observation)
4. After the first exploration, it was not clear what to do next in the dashboard.
   - Quote (translated): "after a while moving around the interface, I went a bit blank because
     I did not know how to continue"
   - Source: `PHASE1.md`, section "What was hard, and how did you get past it?"
   - Confidence: high (own observation)
5. Choosing an installation method was a first obstacle because of the amount of options and
   documentation.
   - Quote (translated): "with so much documentation and different ways to install Wazuh, I did
     not know which one would be the most correct for this lab"
   - Source: `PHASE1.md`, section "What was hard, and how did you get past it?"
   - Confidence: high (own observation)
6. Wazuh detected vulnerabilities on the Ubuntu endpoint, and reviewing which ones need
   attention was left as a next step.
   - Quote (translated): "Analyse in more detail the vulnerabilities that Wazuh detected on my
     Ubuntu endpoint, to see if any needs extra attention"
   - Source: `PHASE1.md`, section "If you had one more day with your lab…", item 3
   - Confidence: high (own observation)
7. Wazuh's alerts were also useful to confirm that a fix worked (an alert confirmed the service
   change).
   - Quote (translated): "Wazuh recorded a new alert confirming the change of state of the
     service on the host"
   - Source: `PHASE1.md`, section "Caso 1"; screenshot `screenshots/01_disable_service_alert.png`
   - Confidence: high (own observation)
8. Real-time FIM worked after a one-line configuration change and an agent restart, and it also
   recorded an unexpected change (`/root/.bash_history`).
   - Quote (translated): "a fourth and last event … was recorded when closing the root session
     … because `/root/.bash_history` was modified"
   - Source: `PHASE1.md`, section "Caso 2"; screenshot `screenshots/01_FIM_events.png`
   - Confidence: high (own observation)

## Inference
- Candidate needs (hypotheses to test with R2/R3):
  - **Alert noise and triage**: telling a repeating, harmless alert from a real problem (claims 1, 2).
  - **Explaining alerts**: what an alert means and what to do about it, without leaving Wazuh (claims 2, 3).
  - **Guided next steps / onboarding** for new users (claims 4, 5).
  - **Vulnerability prioritisation**: which detected vulnerabilities matter (claim 6).
  - **Unexpected events from monitoring** (claim 8): expected noise such as `.bash_history`
    changes looks the same as suspicious changes.
- Claim 7 suggests a positive use: alerts as confirmation of remediation. A service could close
  the loop (suggest a fix, then confirm it from the next alerts).

## Open questions
- Do experienced users and teams (not only beginners) report the same problems? (R2, R3)
- Does Wazuh already offer something for explaining alerts or reducing noise? (R4)

## Not read
- None (no web sources in this note).
