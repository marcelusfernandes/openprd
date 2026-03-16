# Cluster C1: Onboarding & First-Use Barriers

> Pain points that prevent or delay new users from reaching first value.

---

## Cluster Summary

| Attribute | Value |
|-----------|-------|
| Pain Points | 5 (PP-01 to PP-05) |
| Severity Profile | 2 High, 2 Medium, 1 Low |
| Sources Affected | Sarah, Diego, Aisha, Tom |
| Relationship Type | Sequential — each barrier appears at a different stage of first-use onboarding |

---

## Member Pain Points

### PP-01: Post-onboarding "what do I do now" confusion
- **Type:** UX | **Severity:** Medium
- **Source:** Sarah
- **Evidence:** "OK what do I actually DO now" — product-context is created but next step is unclear [Source: sarah-analysis.md]
- **Atomic because:** Distinct from PP-02 (API setup friction) — this is about wayfinding, not technical difficulty

### PP-02: API key setup requires developer-level knowledge
- **Type:** UX | **Severity:** High
- **Sources:** Sarah, Diego
- **Evidence:** "I'm a PM, not a developer" — 20+ minutes per integration [Source: sarah-analysis.md]. "The setup assumes you know what a .env file is" [Source: diego-analysis.md]
- **Atomic because:** Specific to credentials and tool connection (not repo/CLI barrier which is PP-03)

### PP-03: Git repo / CLI entry point excludes non-technical users
- **Type:** Architecture | **Severity:** High
- **Sources:** Sarah, Diego, Aisha, Tom (all 4)
- **Evidence:** "90% of PMs would never clone a repo" [Source: sarah-analysis.md]. "I can't share this with my design lead" [Source: aisha-analysis.md]. "a UI that isn't a terminal" [Source: tom-analysis.md]
- **Atomic because:** Fundamental architecture decision, separate from API key friction (PP-02) and documentation issues (PP-04)
- **Cross-source convergence:** Convergence C6 [Source: cross-source-differentiation.md]

### PP-04: Documentation overwhelms non-enterprise users
- **Type:** Documentation | **Severity:** High
- **Source:** Diego
- **Evidence:** "15 agents, 3 phases, Jira integration, Confluence output — I don't use any of that stuff... made me feel like I was bringing a knife to a gunfight" [Source: diego-analysis.md]
- **Atomic because:** About documentation content/tone, not about technical prerequisites (PP-03) or language (PP-05)

### PP-05: Mixed Portuguese/English documentation
- **Type:** Documentation | **Severity:** Medium
- **Source:** Diego
- **Evidence:** "all the docs are in Portuguese? I'm in Austin, Texas" [Source: diego-analysis.md]
- **Atomic because:** Language-specific issue, separate from documentation complexity (PP-04)

---

## Cluster Relationship

These 5 pain points form a **sequential barrier chain** during first use:

```
[Discover tool] → PP-05 (language confusion) → PP-04 (doc overwhelm) → PP-03 (repo/CLI barrier)
→ PP-02 (API key friction) → PP-01 (what now? confusion) → [First value]
```

Each barrier reduces the percentage of users who reach the next step. The cumulative effect is a substantial adoption funnel drop-off. [Assumption: requires validation with quantitative onboarding data]

---

## Debate Notes (2A vs 2B)

**2A argued** PP-03 should be split into "CLI barrier" (architecture) and "non-technical exclusion" (business). **2B argued** they share the same root cause (git repo as entry point) and splitting would create redundancy. **Resolution:** Kept as single PP-03 typed as Architecture (the root cause), with the business impact noted in the evidence.

**2A argued** PP-04 and PP-05 should be merged (both documentation issues). **2B argued** they have different solutions — PP-04 needs content restructuring (progressive disclosure), PP-05 needs i18n. **Resolution:** Kept separate.

---

**Analysis Date:** 2026-03-15
