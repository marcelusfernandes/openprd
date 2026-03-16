---
name: metric-definer
description: Defines success metrics, KPIs, OKRs, and tracking plans based on MVP scope and solution concepts. Bridges solution design to measurable outcomes.
---

# Metric Definer — Success Metrics & KPI Generator

## Purpose
Transform solution concepts and MVP scope into measurable success frameworks with KPIs, OKRs, and analytics tracking plans.

## Inputs
- `/2-solution/2d-prioritization/mvp-scope.md` — MVP features and priorities
- `/2-solution/2c-solution-concepts/solution-concepts.md` — Solution designs
- `/2-solution/2b-tobe-journey/consolidated-future-journey.md` — Target experience
- `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` — Jobs to be done
- `/0-documentation/broad-context.md` — Product context

## Workflow

### Step 1: Extract Measurable Outcomes
For each MVP feature and JTBD:
1. Identify the behavioral change expected
2. Define what "success" looks like quantitatively
3. Map to user journey stages (acquisition → activation → retention → revenue → referral)

### Step 2: Define KPIs
For each feature/capability in MVP:

| Feature | Primary KPI | Secondary KPI | Baseline | Target | Timeline |
|---------|------------|---------------|----------|--------|----------|
| Feature A | Metric 1 | Metric 2 | Current | Goal | Weeks |

Categories:
- **North Star Metric**: Single metric that best captures value delivered
- **Input Metrics**: Leading indicators that drive the North Star
- **Health Metrics**: Guardrails to ensure we don't break existing experience
- **Counter Metrics**: What could go wrong / unintended consequences

### Step 3: Generate OKRs
Structure quarterly OKRs:

```
Objective: [Qualitative goal]
  KR1: [Metric] from [baseline] to [target] by [date]
  KR2: [Metric] from [baseline] to [target] by [date]
  KR3: [Metric] from [baseline] to [target] by [date]
```

Generate for:
- Launch quarter (Q1): Focus on shipping + early adoption
- Growth quarter (Q2): Focus on retention + engagement
- Scale quarter (Q3): Focus on efficiency + expansion

### Step 4: Tracking Plan
For each KPI, define:

| Event Name | Trigger | Properties | Platform | Owner |
|-----------|---------|------------|----------|-------|
| `feature_used` | User clicks X | user_id, plan, variant | Amplitude/PostHog | PM |

### Step 5: Output
Save to `/2-solution/2e-roadmap/success-metrics.md`:

## Output Format
```
# Success Metrics — [Product Name]
## North Star Metric
## KPI Dashboard
### Input Metrics
### Health Metrics
### Counter Metrics
## OKRs
### Q1 — Launch
### Q2 — Growth
### Q3 — Scale
## Tracking Plan
## Measurement Cadence
## Sources & Assumptions
```

## Rules
- Tag baselines without data: `[Baseline TBD — requires current analytics]`
- Tag target estimates: `[AI estimation based on industry benchmarks]`
- Always include counter-metrics to avoid Goodhart's Law
- Mark assumptions: `[Assumption: requires validation with data team]`
- Cite industry benchmarks: `[Source: benchmark-source]`
