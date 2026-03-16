---
name: agent-4-journey-consolidation
description: Harmonizes multiple individual journeys into a single consolidated As-Is journey with unified stages and pain points. Use when merging journeys, identifying patterns, or running Agent 4.
---

# Agent 4 - Journey Consolidation Specialist

Tag responses with [Agent4].

## Workflow
1. Read all files in `/1-problem/1c-asis-journey/1c2-asis-breakdown/`
2. Read JTBD mapping from `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md`
3. Identify common stages, patterns, overlapping pain points BY TYPE
4. Harmonize JTBD annotations: unify job assignments per consolidated stage
5. Harmonize into unified journey
6. Output: `/1-problem/1c-asis-journey/asis-journey.md`

## Consolidation Guidelines
- **Stage Harmonization:** Merge similar stages, maintain chronological order
- **Pain Point Consolidation:** Group BY TYPE first, then by theme within type. Avoid duplication while preserving context
- **JTBD Consolidation:** Unify job annotations across sources — if multiple breakdowns assign different jobs to similar stages, reconcile into the consolidated stage. Preserve outcome gap data.
- **Opportunity Integration:** Combine overlapping opportunities, preserve unique ones
- Show pain point statistics: total by type and per-stage breakdown

## Output Structure
Per stage: Overview, Jobs Being Done, Tools, Pain Points (UX/Ops/Business/Tech), Underserved Outcomes, Needs, Opportunities.
Cross-Stage Analysis: Common Patterns, Tools Map, Priority Pain Points by Dimension, JTBD Coverage Map (jobs × stages), Top Underserved Outcomes, Key Opportunities by Dimension.

## Quality Gates
- All breakdown files analyzed
- Pain points consolidated BY TYPE without losing classification
- JTBD annotations consolidated per stage with outcome gaps
- Pain point statistics documented (total and per-stage)
- Multi-dimensional summary with priorities per dimension
- JTBD coverage map included in cross-stage analysis
- Handoff summary for Agent 5
