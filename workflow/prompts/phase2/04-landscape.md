# Prompt 04 (R4): what already exists

- Date: 2026-11-10
- Agent: `researcher` (run in parallel with prompts 01–03)
- Plan step: Phase 2, Step 2 (`workflow/plans/01-phase2.md`)

## Prompt

> Research question: **What already exists to help Wazuh users, especially with AI?** The goal
> is to avoid choosing a need that Wazuh or a common tool already serves well.
>
> Find out:
> 1. **Wazuh's own AI/LLM work**: features, integrations, PoC guides or blog posts about using
>    LLMs or AI with Wazuh (for example alert enrichment, threat hunting assistants, chat over
>    Wazuh data). Say whether each is a shipped product feature, a documented integration, or a
>    blog/PoC example, and for which version.
> 2. **Wazuh's commercial offer**: Wazuh Cloud (what it includes, how it is sold), professional
>    services, and anything public about a "Wazuh Hub" or SaaS services that extend Wazuh. If
>    nothing public exists about the Hub, say so plainly.
> 3. **Built-in help for common pains**: what Wazuh offers out of the box for alert tuning and
>    noise reduction, rule testing (e.g. the rule test tool / logtest), vulnerability
>    prioritisation, compliance reporting and multi-tenancy.
> 4. **Third-party tools and competitors**: community or commercial projects that add AI or
>    automation on top of Wazuh (GitHub projects, integrations with SOAR tools such as Shuffle or
>    TheHive), and AI assistants in other SIEM/XDR products (for example Microsoft Security
>    Copilot, Google Security Operations Gemini, Elastic AI Assistant, Splunk AI Assistant),
>    only at the level of "what it does", from the vendor's own pages.
>
> Output: notes under `research/sources/` with the prefix `landscape-` (for example
> `landscape-wazuh-ai.md`, `landscape-wazuh-cloud.md`, `landscape-builtin-tuning.md`,
> `landscape-third-party.md`, `landscape-competitor-ai.md`). At most 7 notes. Topic notes may
> use `url: multiple, see claims`. Use the note template from your agent definition.
>
> Rules (from CLAUDE.md): every claim has the URL of a page you fetched in this session and a
> short quote; never invent features, versions or prices; vendor marketing claims are reported
> as "the vendor says"; mark confidence; keep inference apart from claims; no personal data;
> English only.
>
> When done, reply with at most 10 lines: files written and what is already covered vs. what
> looks like a gap.
