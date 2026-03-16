# Pain Report — OpenPRD Self-Discovery

> **TL;DR:** OpenPRD's analytical engine is best-in-class, but its packaging fails every user segment differently — output formats don't match real-world delivery needs, quant-qual synthesis is broken, and the CLI-only architecture blocks both non-technical adoption and enterprise deals. Fix the output layer and data synthesis before adding features.

**[Agent5] Generated: 2026-03-15**

---

## Executive Summary

**32 atomic pain points** identified across 4 user interviews representing enterprise, mid-market, growth, and solo founder segments. Clustered into 5 problem areas, mapped to 5 Jobs to Be Done.

### Pain Point Statistics

| Type | Count | % of Total |
|------|-------|-----------|
| Feature | 10 | 31% |
| Architecture | 7 | 22% |
| UX | 6 | 19% |
| Business | 4 | 13% |
| Documentation | 3 | 9% |

**Note:** Type counts do not sum to 32 due to 2 PPs reclassified during atomic decomposition. [Source: all-painpoints-granular.md]

### Severity Distribution

| Severity | Count | Key Items |
|----------|-------|-----------|
| Critical | 4 | Shallow BigQuery (PP-08), No quant-qual synthesis (PP-11), No SOC 2 (PP-28), Negative founder ROI (PP-30) |
| High | 22 | 69% of all pain points — broad, systemic issues |
| Medium | 4 | Post-onboarding confusion, mixed language docs, enterprise tone, clustering accuracy |
| Low | 1 | Cloud recording import (PP-06) |

[Source: all-painpoints-granular.md]

### Key Finding

All 4 personas independently validated the **analytical engine as best-in-class** while identifying **packaging, collaboration, and integration depth** as the primary gaps. The convergence is strong: the "what" is right, the "how" needs work. [Source: cross-source-differentiation.md]

---

## Top Clusters Ranked by Severity + Frequency

### 1. Output Format & Delivery Mismatch (C2) — HIGHEST PRIORITY

**10 pain points** | 1 Critical, 7 High, 2 Medium | All 4 personas affected

The tool generates outputs that no user can use as-is. Every persona needs a different format, and none is served:
- **Founders** need a 1-page brief; get a 20-page report [Source: diego-analysis.md]
- **Mid-market PMs** need Google Slides/PDF; get HTML [Source: sarah-analysis.md]
- **Growth PMs** need experiment briefs; get Jira stories [Source: tom-analysis.md]
- **Enterprise PMs** need branded PowerPoint and Confluence in company templates; get generic HTML [Source: aisha-analysis.md]

Recommendations are described as "filler" (PP-16) and "platitudes" (PP-17). The system fights simplification instead of adapting to context (PP-20). [Source: sarah-analysis.md, diego-analysis.md]

**JTBD Link:** Job 2 (Deliver Outputs Stakeholders Use) — highest opportunity score. [Source: jtbd-mapping.md]

### 2. Integration Depth & Data Connectivity (C3) — CRITICAL GAP

**6 pain points** | 2 Critical, 3 High, 1 Low | 3 of 4 personas affected

The promise of quant-qual synthesis — OpenPRD's unique differentiator — is unfulfilled. Data integrations are shallow, and qualitative and quantitative data exist as "two separate tools that happen to live in the same repo" (PP-11). [Source: sarah-analysis.md]

- BigQuery runs "3 queries, not 30" — basic event counts only (PP-08, Critical) [Source: tom-analysis.md]
- Salesforce returns raw JSON without enrichment (PP-09) [Source: aisha-analysis.md]
- Intercom dumps tickets without correlating to interview findings (PP-10) [Source: sarah-analysis.md]
- Quant-qual synthesis confirmed as universal need by 3 of 4 sources (Convergence C3) [Source: cross-source-differentiation.md]

**JTBD Link:** Job 3 (Connect Quant+Qual) — tied for highest opportunity score. [Source: jtbd-mapping.md]

### 3. Collaboration, Security & Enterprise Readiness (C5) — ENTERPRISE BLOCKER

**5 pain points** | 1 Critical, 4 High | Aisha (primary), Sarah, Tom affected

The tool is "powerful but lonely" (PP-32). Discovery outputs die on the PM's laptop because there's no sharing, no collaboration, and no security compliance.

- No URL sharing or collaboration mechanism (PP-25) — 2 sources [Source: sarah-analysis.md, aisha-analysis.md]
- No SOC 2, SSO, data residency (PP-28, Critical) — binary enterprise blocker [Source: aisha-analysis.md]
- Jira integration too automated, no draft/review mode (PP-24) [Source: aisha-analysis.md]
- Journey map is static markdown, not interactive workshop artifact (PP-26) [Source: aisha-analysis.md]

**JTBD Link:** Job 5 (Scale Across Team) — unlocks highest-WTP segment. [Source: jtbd-mapping.md]

### 4. Onboarding & First-Use Barriers (C1) — ADOPTION GATE

**5 pain points** | 2 High, 2 Medium, 1 Low | All 4 personas affected

CLI/repo entry point is the #1 cross-source convergence (4 of 4 sources). "90% of PMs would never clone a repo" (PP-03). API key setup requires developer knowledge (PP-02, 2 sources). Documentation overwhelms non-enterprise users (PP-04). [Source: sarah-analysis.md, diego-analysis.md, aisha-analysis.md, tom-analysis.md]

**JTBD Link:** Job 1 (Get Started Quickly) — binary gate. [Source: jtbd-mapping.md]

### 5. Growth PM Workflow Fit (C4) — NICHE OPPORTUNITY

**6 pain points** | 6 High | Tom (primary)

A distinct workflow that no competitor serves: data-first discovery feeding experiment cycles. The tool suggests already-tested hypotheses (PP-12), generates generic interview scripts (PP-13), lacks metric hooks (PP-14), and uses wide-interval top-down revenue estimates (PP-15). [Source: tom-analysis.md]

"If OpenPRD built a 'Growth Discovery' workflow that outputs experiment briefs instead of Jira stories, you'd own a niche that nobody else is serving." [Source: tom-analysis.md]

**JTBD Link:** Job 4 (Run Growth Discovery) — high-value differentiation wedge. [Source: jtbd-mapping.md]

---

## Cross-Persona Patterns

### Universal Pain (All 4 Sources)
- **CLI is an adoption barrier** — Convergence C6: all 4 sources recognize this [Source: cross-source-differentiation.md]
- **Output format mismatch** — Convergence C4: every user needs a different format, none is served [Source: cross-source-differentiation.md]

### Strong Signal (3 Sources)
- **Quant-qual synthesis broken** — Convergence C3: all sources with data describe this gap [Source: cross-source-differentiation.md]

### Segment-Specific Pain
- **Enterprise governance** (Aisha only): SOC 2, SSO, draft mode — Divergence D4 [Source: cross-source-differentiation.md]
- **Growth workflow** (Tom only): experiment briefs, metric hooks — Divergence D5 [Source: cross-source-differentiation.md]
- **Founder simplicity** (Diego only): negative ROI, needs 10-minute workflow — Divergence D1 [Source: cross-source-differentiation.md]
- **Language/localization** (Diego only): Portuguese docs block international adoption — Divergence D6 [Source: cross-source-differentiation.md]

---

## Key Quotes by Persona

**Sarah (Series B PM):**
> "Two separate tools that happen to live in the same repo." — on quant-qual synthesis [Source: sarah-analysis.md]
> "I can't present an HTML file in a leadership meeting." — on export formats [Source: sarah-analysis.md]

**Diego (Solo Founder):**
> "The 2 hours I spent fighting with the pipeline I could have just re-listened to my recordings." — on negative ROI [Source: diego-analysis.md]
> "I need a top-3 list... One command. /decide or /what-next." — on output simplicity [Source: diego-analysis.md]

**Aisha (Enterprise PM):**
> "Depth without collaboration is limited value. The output of discovery isn't a document — it's shared understanding." — on collaboration [Source: aisha-analysis.md]
> "My IT team would never approve a tool that stores customer interview data in a local git repo." — on security [Source: aisha-analysis.md]

**Tom (Growth PM):**
> "Not 3 queries — 30 queries." — on integration depth [Source: tom-analysis.md]
> "You'd own a niche that nobody else is serving." — on Growth Discovery [Source: tom-analysis.md]

---

## Revenue Impact Estimate

[AI estimation based on willingness-to-pay data from interviews]

| Segment | Current WTP | WTP With Fixes | Key Conditions | Potential Impact |
|---------|------------|----------------|----------------|-----------------|
| Enterprise | $0 | $500-1000/seat/mo | Collaboration, SOC 2, templates | Highest per-deal value; blocked by C5 |
| Mid-market | "sometimes tool" | $200/mo | Quant-qual synthesis, exports | Conversion from trial to paid |
| Growth PM | $50 max | $300/mo ($1000 dream) | Deep data, experiment briefs | Niche premium positioning |
| Solo Founder | $0 | $50-100/mo | 10-min workflow, /decide command | High volume, low price |

[Source: cross-source-differentiation.md — Willingness to Pay Summary]

Addressing C2 (output format) and C3 (quant-qual synthesis) would likely unlock the mid-market segment ($200/mo) and improve Growth PM conversion. Addressing C5 (collaboration + security) is required to unlock enterprise ($500-1000/seat/mo). [AI estimation based on interview data]

---

## Recommended Actions (Prioritized)

### Tier 1 — Do Now (Highest impact, unblocks most users)

1. **Fix output format system** — Context-adaptive outputs: 1-page brief for founders, branded PDF/Slides for mid-market, Confluence templates for enterprise, experiment briefs for growth PMs. Addresses C2 (10 PPs), impacts all 4 segments. [Source: painpoint-mapping.md]

2. **Deepen quant-qual synthesis** — Make analytics and qualitative data genuinely integrated, not side-by-side. This is the core differentiator and it's currently broken. Addresses C3 (6 PPs, 2 Critical). [Source: cross-source-differentiation.md]

3. **Reduce onboarding friction** — Consider web-based entry point or hosted tier alongside CLI. At minimum: guided setup wizard, no-code API key configuration. Addresses C1 (5 PPs, 4-source convergence). [Source: painpoint-mapping.md]

### Tier 2 — Do Next (Segment unlocks)

4. **Build collaboration layer** — URL sharing, team access, draft/review mode. Required for enterprise adoption ($500-1000/seat). Addresses C5 (5 PPs). [Source: aisha-analysis.md]

5. **Build "Growth Discovery" workflow** — Experiment briefs, hypothesis filtering, metric hooks. Differentiation wedge in unserved niche. Addresses C4 (6 PPs). [Source: tom-analysis.md]

### Tier 3 — Do Later (Important but not blocking)

6. **Enterprise security** — SOC 2, SSO, data residency. Required for enterprise deals but meaningless without collaboration layer (Tier 2). [Source: aisha-analysis.md]

7. **Documentation and localization** — English-first docs, persona-adaptive documentation. Reduces international friction. [Source: diego-analysis.md]

---

## Bright Spots to Preserve

These capabilities are working well and must not be degraded during any redesign:

| Bright Spot | Validation | Preserve Because |
|-------------|-----------|-----------------|
| **Qualitative analysis depth** | "Best I've seen" — all 4 sources [Source: cross-source-differentiation.md] | Core differentiator; foundation for everything else |
| **/pair mode intelligence** | "Worth the whole setup time" — Sarah, Diego, Tom [Source: cross-source-differentiation.md] | Most valued interaction pattern; users prefer this over pipeline |
| **Source attribution** | "Compliance-grade traceability" — Aisha [Source: aisha-analysis.md] | Enterprise differentiator; trust-builder |
| **Product context onboarding** | Smooth, conversational — Sarah, Diego [Source: cross-source-differentiation.md] | Good first-touch experience; extend pattern to other flows |
| **Data-first workflow concept** | "Most interesting workflow in any PM tool" — Tom [Source: tom-analysis.md] | Unique positioning; foundation for Growth Discovery niche |
| **Anomaly detection** | Found unseen navigation pattern — Tom [Source: tom-analysis.md] | Differentiator when integrations are deep enough |

---

---

*[Agent5] Sources: 4 interviews (sarah, diego, aisha, tom), cross-source-differentiation.md, all-painpoints-granular.md, painpoint-mapping.md, jtbd-mapping.md, broad-context.md. Pipeline: Agent 0→1→2A+2B→2C→5. Guardrails: all claims sourced, estimates tagged [AI estimation].*
