---
name: ab-test-designer
description: Designs A/B test experiments from solution hypotheses. Generates test plans with hypothesis, variants, sample size, duration, and success criteria. Integrates with PostHog/Amplitude.
---

# A/B Test Designer

## Purpose
Transform product hypotheses from the solution space into rigorous A/B test designs, ready for implementation in analytics platforms (PostHog, Amplitude, or custom).

## Inputs
- `/2-solution/2c-solution-concepts/solution-concepts.md` — Hypotheses to test
- `/2-solution/2d-prioritization/mvp-scope.md` — Feature priorities
- `/2-solution/2e-roadmap/success-metrics.md` — KPIs and metrics (if exists)
- `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` — User jobs context

## Workflow

### Step 1: Extract Testable Hypotheses
From solution concepts, identify hypotheses in the format:
> **We believe that** [change] **for** [audience] **will result in** [outcome] **as measured by** [metric].

Prioritize hypotheses by:
1. Risk level (high uncertainty → test first)
2. Impact potential (high impact → test first)
3. Cost to test (low cost → test first)

### Step 2: Design Each Experiment

For each hypothesis:

```markdown
## Experiment: [Name]

### Hypothesis
We believe that [change] for [audience] will result in [outcome].

### Variants
- **Control (A)**: Current experience — [description]
- **Treatment (B)**: New experience — [description]
- **Treatment (C)**: [Optional alternative, if applicable]

### Primary Metric
- **Metric**: [e.g., conversion rate, time-to-complete, retention D7]
- **Current baseline**: [value or TBD]
- **Minimum Detectable Effect (MDE)**: [e.g., 5% relative improvement]
- **Direction**: [increase / decrease]

### Secondary Metrics
| Metric | Expected Direction | Purpose |
|--------|-------------------|---------|
| [metric] | [up/down/stable] | [why tracking] |

### Guardrail Metrics
| Metric | Threshold | Action if breached |
|--------|-----------|-------------------|
| [e.g., error rate] | [< 1%] | [Kill test] |
| [e.g., page load] | [< 3s] | [Investigate] |

### Audience
- **Segment**: [All users / New users / Specific cohort]
- **Allocation**: [50/50 or other split]
- **Exclusions**: [Any users to exclude]

### Sample Size & Duration
- **Statistical significance**: 95% confidence
- **Power**: 80%
- **Estimated sample size per variant**: [calculate based on baseline + MDE]
- **Estimated duration**: [days/weeks based on traffic]

### Implementation Notes
- **Platform**: [PostHog / Amplitude / Custom]
- **Feature flag name**: `exp_[experiment_slug]`
- **Events to track**: [list of analytics events]
- **Engineering effort**: [Low / Medium / High]

### Decision Framework
- **If significant positive**: Ship to 100%, update metrics
- **If inconclusive**: Extend duration or increase MDE tolerance
- **If significant negative**: Kill, investigate qualitative feedback
- **If guardrail breached**: Immediate rollback
```

### Step 3: Create Experiment Roadmap
Sequence experiments:
1. Pre-launch validation tests (before MVP ship)
2. Post-launch optimization tests
3. Growth experiments

### Step 4: Output
Save to `/2-solution/2e-roadmap/ab-tests/`:
- `experiment-[name].md` per experiment
- `experiment-roadmap.md` (sequenced plan)
- `tracking-requirements.md` (consolidated events/flags needed)

## Sample Size Quick Reference
| Baseline Rate | MDE 5% | MDE 10% | MDE 20% |
|--------------|--------|---------|---------|
| 1% | 300K/var | 80K/var | 20K/var |
| 5% | 60K/var | 15K/var | 4K/var |
| 10% | 30K/var | 8K/var | 2K/var |
| 25% | 10K/var | 3K/var | 800/var |
| 50% | 6K/var | 1.5K/var | 400/var |

## Rules
- ALWAYS specify guardrail metrics — never run a test without safety checks
- ALWAYS define the decision framework upfront — never decide post-hoc
- Tag baseline unknowns: `[Baseline TBD — measure before launch]`
- Tag sample estimates: `[AI estimation — validate with actual traffic data]`
- Mark assumptions: `[Assumption: requires validation with data/engineering]`
- Never recommend running multiple tests on the same user flow simultaneously without noting interaction risks
