# Cluster C5: Collaboration, Security & Enterprise Readiness

> Pain points that block team workflows, enterprise procurement, and organizational adoption.

---

## Cluster Summary

| Attribute | Value |
|-----------|-------|
| Pain Points | 5 (PP-24, PP-25, PP-26, PP-28, PP-32) |
| Severity Profile | 1 Critical, 4 High |
| Sources Affected | Aisha (primary), Sarah, Tom (partial) |
| Relationship Type | Contextual — all stem from the product being designed as a personal tool, not a team/organization tool |

---

## Member Pain Points

### PP-24: Jira integration too automated — no draft/review mode for enterprise governance
- **Type:** Feature | **Severity:** High
- **Source:** Aisha
- **Evidence:** "I can't have an AI auto-create stories — they need to go through technical review, estimation, dependency mapping. What I'd actually want is a draft" [Source: aisha-analysis.md]

### PP-25: No sharing or collaboration mechanism — outputs are local-only
- **Type:** Architecture | **Severity:** High
- **Sources:** Sarah, Aisha
- **Evidence:** "I can't share a link with my designer" [Source: sarah-analysis.md]. "A repo on my laptop is a non-starter for team workflows" [Source: aisha-analysis.md]. "The output of discovery isn't a document — it's shared understanding" [Source: aisha-analysis.md]
- **Cross-source convergence:** Convergence C6 [Source: cross-source-differentiation.md]

### PP-26: Journey map is markdown, not interactive canvas
- **Type:** UX | **Severity:** High
- **Source:** Aisha
- **Evidence:** "No visual layout, no sticky notes, no color coding by severity... For a collaborative workshop artifact? Useless" [Source: aisha-analysis.md]

### PP-28: No security compliance (SOC 2, data residency, SSO, access controls)
- **Type:** Business | **Severity:** Critical
- **Source:** Aisha
- **Evidence:** "My IT team would never approve a tool that stores customer interview data in a local git repo. We need SOC 2, data residency, access controls" [Source: aisha-analysis.md]

### PP-32: Product is "powerful but lonely" — limits organizational value
- **Type:** Business | **Severity:** High
- **Sources:** Sarah, Aisha
- **Evidence:** "powerful but lonely" [Source: sarah-analysis.md]. "OpenPRD produces a good document but doesn't create shared understanding" [Source: aisha-analysis.md]

---

## Cluster Relationship

This cluster represents the **personal→team transition gap**. The product excels as a personal analytical tool but has no mechanisms for:

1. **Sharing** — outputs live on one person's machine (PP-25, PP-32)
2. **Co-creation** — artifacts can't be collaboratively edited or workshopped (PP-26)
3. **Governance** — enterprise workflow controls don't exist (PP-24)
4. **Compliance** — enterprise security requirements unmet (PP-28)

The severity escalates with organizational scale:
- Solo founders (Diego): Not affected at all [Source: cross-source-differentiation.md — Divergence D2]
- Small teams (Sarah): "Would be nice" — can work around it
- Mid-size (Tom): "Moderate" — needs to feed experiment backlog to team
- Enterprise (Aisha): "Non-starter" — blocks adoption entirely

Aisha's framing is definitive: "The analysis engine is the best I've seen. Enterprise would pay $500-1000/seat/month for this if it were packaged correctly" [Source: aisha-analysis.md]. The gap isn't analytical quality — it's organizational packaging.

---

## Debate Notes (2A vs 2B)

**2A argued** PP-28 (security) should be a standalone cluster. **2B argued** security is one dimension of enterprise readiness alongside collaboration and governance — they share the same buyer (enterprise IT/procurement) and the same solution direction (SaaS platform with proper controls). **Resolution:** Kept in C5.

**2A argued** PP-26 (journey map canvas) belongs in C2 (Output Mismatch). **2B argued** the specific issue isn't output format but collaboration capability — the journey map needs to be a shared, interactive artifact for team workshops, which is a collaboration need. **Resolution:** PP-26 stays in C5.

---

**Analysis Date:** 2026-03-15
