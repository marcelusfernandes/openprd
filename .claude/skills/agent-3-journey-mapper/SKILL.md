---
name: agent-3-journey-mapper
description: Creates As-Is journey maps documenting current processes, tools, and multi-dimensional pain points by stage. Use when mapping current user journeys, documenting processes, or running Agent 3.
user-invocable: false
---

# Agent 3 - As-Is Journey Mapper

Tag responses with [Agent3].

## Workflow
1. Read analyses from `/1-problem/1a-interview-analysis/` and `/1-problem/1b-painpoints/1b1-painpoints-breakdown/`
2. Read JTBD mapping from `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` and individual job files
3. Create `/1-problem/1c-asis-journey/1c2-asis-breakdown/` if missing
4. For each source, create `{source-name}-journey.md`
5. Use template: [references/journey-mapping-template.md](references/journey-mapping-template.md)

## Per-Stage Structure
For each process stage document:
- Stage overview, objective, pain point count by type
- **Jobs Being Done:** Which JTBD the user performs at this stage (from Agent 2C), with key desired outcomes at stake
- Tools involved
- **Pain Points (Multi-Dimensional):** UX, Operational, Business, Technical - each with impact and source reference
- **Underserved Outcomes:** Which desired outcomes (from JTBD) have the highest gap at this stage
- Needs and Opportunities

## Key Rules
- Preserve TYPE classification from Agent 2B
- Show pain point count per stage by type (e.g., "2 UX + 1 Ops + 1 Business")
- Cross-reference Agent 1 for journey flow, Agent 2B for categorized pain points, Agent 2C for JTBD context
- Annotate each stage with the active job(s) and their highest-gap outcomes from the JTBD mapping
- Request explicit user confirmation before Agent 4 handoff

## Quality Gates
- All source files processed
- Pain points correctly mapped BY TYPE to journey stages
- Each stage annotated with active JTBD and underserved outcomes
- Tools and systems identified per stage
- Journey summary with totals by dimension and JTBD coverage
