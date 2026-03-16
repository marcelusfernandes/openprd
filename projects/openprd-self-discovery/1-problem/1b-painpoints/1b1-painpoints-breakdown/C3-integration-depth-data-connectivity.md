# Cluster C3: Integration Depth & Data Connectivity

> Pain points where integrations exist but are too shallow, disconnected, or manual to deliver on the product's core promise of connected discovery.

---

## Cluster Summary

| Attribute | Value |
|-----------|-------|
| Pain Points | 6 (PP-06 to PP-11) |
| Severity Profile | 2 Critical, 3 High, 1 Low |
| Sources Affected | Sarah, Diego, Aisha, Tom |
| Relationship Type | Causal — shallow individual integrations (PP-06 to PP-10) prevent the synthesis layer (PP-11) from working |

---

## Member Pain Points

### PP-06: No direct cloud recording integration (Zoom, Gong)
- **Type:** Feature | **Severity:** Low
- **Sources:** Diego, Aisha (inferred)
- **Evidence:** "My Zoom recordings are in the cloud, not downloaded... 15 minutes" [Source: diego-analysis.md]. Aisha manually exported Gong transcripts [Source: aisha-analysis.md]

### PP-07: Amplitude query iteration requires multiple round-trips
- **Type:** Feature | **Severity:** High
- **Source:** Sarah
- **Evidence:** "I had to go back and forth three times to get the right query. It felt like I was debugging SQL through a chatbot" [Source: sarah-analysis.md]

### PP-08: BigQuery integration is shallow — basic queries only
- **Type:** Feature | **Severity:** Critical
- **Source:** Tom
- **Evidence:** "event counts, funnel steps, simple cohort breakdowns" — wants segmented analysis by channel, company size, vertical [Source: tom-analysis.md]. "Not 3 queries — 30 queries" [Source: tom-analysis.md]

### PP-09: Salesforce integration returns raw JSON, no enrichment
- **Type:** Feature | **Severity:** High
- **Source:** Aisha
- **Evidence:** "raw JSON that I then had to interpret" — wanted automatic overlay of ARR, account age, segment [Source: aisha-analysis.md]

### PP-10: Intercom integration lacks cross-reference with interview findings
- **Type:** Feature | **Severity:** High
- **Source:** Sarah
- **Evidence:** "No 'hey, 47 tickets last month were about the same permissions issue your interviewees mentioned'" — output was "just a dump of ticket summaries" [Source: sarah-analysis.md]

### PP-11: No automatic quant-qual synthesis
- **Type:** Architecture | **Severity:** Critical
- **Sources:** Sarah, Tom, Aisha (via Salesforce enrichment need)
- **Evidence:** "two separate tools that happen to live in the same repo" [Source: sarah-analysis.md]. "data points side by side" not "true integrated analysis" [Source: tom-analysis.md]
- **Cross-source convergence:** Convergence C3 — universal desire across all sources with data [Source: cross-source-differentiation.md]

---

## Cluster Relationship

This cluster has a **causal hierarchy**:

```
Layer 1 (Input): PP-06 — Recording import friction
Layer 2 (Individual integrations): PP-07, PP-08, PP-09, PP-10 — Each integration is shallow
Layer 3 (Synthesis): PP-11 — Cross-integration synthesis doesn't happen automatically
```

PP-11 is the crown jewel pain point — it's what makes OpenPRD's promise unique ("BigQuery AND Amplitude AND interview analysis in the same system" [Source: tom-analysis.md]). But it can't work well until the Layer 2 integrations are deep enough to produce rich, structured data.

The gap between "architecture is right" and "execution needs to go 3x deeper" [Source: tom-analysis.md] lives entirely in this cluster.

---

## Debate Notes (2A vs 2B)

**2A proposed** PP-11 should be its own cluster ("Quant-Qual Synthesis"). **2B argued** synthesis is the emergent property of integration depth — it belongs with the integrations because fixing PP-07 through PP-10 is prerequisite to fixing PP-11. **Resolution:** Kept together as causal hierarchy within C3.

**2A argued** PP-07 (Amplitude iteration) and PP-08 (BigQuery shallow) should merge as "analytics integration depth." **2B argued** they're different tools with different users and different solutions. **Resolution:** Kept separate.

---

**Analysis Date:** 2026-03-15
