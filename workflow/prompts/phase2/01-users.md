# Prompt 01 (R1): who uses Wazuh, and for what

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with prompts 02–04)
- Plan step: Phase 2, Step 2 (`workflow/plans/01-phase2.md`)

## Prompt

> Research question: **Who uses Wazuh, and for what?**
>
> Find out:
> 1. Which kinds of organisations use Wazuh (size, sector, region if stated) and which roles
>    operate it day to day (SOC analysts, sysadmins, MSSPs, consultants, students…).
> 2. The main use cases Wazuh is used for (e.g. threat detection, FIM, vulnerability detection,
>    compliance such as PCI DSS / HIPAA / GDPR / NIST, cloud security, container security).
> 3. How it is deployed and offered: self-hosted vs. Wazuh Cloud, typical deployment sizes, any
>    public numbers on adoption (downloads, users, protected endpoints). Quote numbers exactly
>    and say where they come from; vendor-stated numbers are marked as such.
> 4. MSSPs and multi-tenant use: does Wazuh document it, and how.
>
> Start from documentation.wazuh.com, wazuh.com (use cases, customer stories / case studies,
> Wazuh Cloud pages) and the Wazuh blog. Then independent sources if they add something
> (analyst or comparison articles), clearly marked as such.
>
> Output: notes under `research/sources/` with the prefix `users-` (for example
> `users-use-cases.md`, `users-customer-stories.md`, `users-wazuh-cloud.md`). At most 6 notes.
> Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent sources or numbers; mark confidence; keep inference apart from
> claims; no personal data (no names of individuals from case studies unless they are the
> company's public spokesperson, and even then prefer the company name); English only.
> Prefer recent content about the latest Wazuh 4.x.
>
> When done, reply with at most 10 lines: files written and the main findings.
