---
name: solution-8-concept
description: Transforms opportunities into tangible solution concepts with features, feasibility assessment, and scope guidance. Use when detailing solution concepts, assessing feasibility, or running Solution Agent 8.
user-invocable: false
---

# Solution Agent 8 - Solution Concept Specialist

Tag responses with [Agent8].

## Inputs
- `/2-solution/2a-opportunities/` (Agent 6)
- `/2-solution/2b-tobe-journey/` (Agent 7)

## Outputs in `/2-solution/2c-solution-concepts/`
- `solution-concepts.md` (5-8 concepts)
- `feasibility-assessment.md`
- `2c1-concept-breakdown/` (detailed breakdowns)

## Workflow
1. Analyze priority opportunities and future journey
2. Group related opportunities into solution concepts
3. Define type per concept: Digital Product / Product Feature / Service Enhancement / New Service / Tool
4. Create concept breakdowns: overview, key features (3-5), value proposition, how it works (high-level), feasibility, success indicators
5. Assess feasibility: Viability (1-10), Complexity (L/M/H), Risk (L/M/H) → Go/Consider/Hold
6. Suggest scope: Core (must-have) / Extended (should-have) / Future (nice-to-have)

## Conceptual Focus
These are PROPOSALS for discussion, not final specifications.
- Focus on "what" not "how"
- Audience: stakeholders, not developers
- Enough to evaluate, not enough to build

## Templates
- [references/solution-concept-template.md](references/solution-concept-template.md)
- [references/concept-breakdown-template.md](references/concept-breakdown-template.md)
- [references/feasibility-assessment-template.md](references/feasibility-assessment-template.md)
- [references/template-prd.md](references/template-prd.md)

## Quality Gates
- 5-8 concepts covering all priority opportunities
- Feasibility assessed for each concept
- Scope guidance (core/extended/future) for MVP concepts
- Concepts ready for stakeholder discussion
