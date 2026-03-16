---
version: "1.0.0"
last_updated: "2025-03-09"
author: "Marcelus Fernandes"
template_type: "jtbd_analysis"
used_by: ["agent-2c-jtbd-specialist"]
purpose: "Structure Jobs to Be Done analysis with functional, emotional, and social dimensions plus outcome expectations"
---

# Job: [Job Title — verb-oriented, e.g., "Monitor Campaign Performance Across Brands"]

## Job Statement
> **"When** [situation/trigger], **I want to** [motivation/action], **so I can** [expected outcome]."

## Job Context
- **Who:** [Primary user role(s) performing this job]
- **When:** [Situations/triggers that activate this job]
- **Where:** [Process stages where this job occurs]
- **Frequency:** [How often this job is performed]
- **Related Pain Clusters:** [Cluster names from Agent 2B + file references]
- **Pain Point IDs:** [PP IDs mapped to this job]

## Job Dimensions

### Functional Jobs (What they DO)
- **F1:** [Practical task the user performs]
  - Evidence: [PP IDs and brief description]
- **F2:** [Next functional sub-job]
  - Evidence: [PP IDs and brief description]

### Emotional Jobs (How they want to FEEL)
- **E1:** [Emotional need — e.g., "Feel confident that data is accurate"]
  - Evidence: [PP IDs — what pain causes the opposite emotion]
- **E2:** [Next emotional sub-job]
  - Evidence: [PP IDs]

### Social Jobs (How they want to be PERCEIVED)
- **S1:** [Social need — e.g., "Be seen as data-driven by leadership"]
  - Evidence: [PP IDs or inference from context]
- **S2:** [Next social sub-job]
  - Evidence: [PP IDs or inference]

## Desired Outcome Expectations

> Ranked by importance (derived from pain severity). Format: [Direction] + [Metric] + [Object of control]

| # | Desired Outcome | Importance | Current Satisfaction | Gap | Pain Evidence |
|---|----------------|------------|---------------------|-----|---------------|
| 1 | [e.g., Minimize time spent extracting campaign data] | High | Low | High | PP1, PP2 |
| 2 | [e.g., Maximize accuracy of cross-brand comparisons] | High | Low | High | PP5, PP12 |
| 3 | [e.g., Reduce manual steps in report generation] | High | Medium | Medium | PP3, PP9 |
| 4 | [e.g., Increase confidence in data-driven decisions] | Medium | Low | Medium | PP15 |
| 5 | [Continue...] | | | | |

### Importance Scale
- **High:** Derived from Critical/High severity pain points; frequent occurrence
- **Medium:** Derived from Medium severity or moderate frequency
- **Low:** Derived from Low severity or rare occurrence

### Satisfaction Gap
- **High gap:** Current workaround barely works; high frustration
- **Medium gap:** Workaround exists but is painful
- **Low gap:** Mostly addressed, minor friction

## Switching Triggers
What causes the user's current approach to break down:

### Functional Failures
- [Current tool/process limitation that blocks the job — with PP reference]

### Emotional Failures
- [Point where frustration/anxiety exceeds tolerance — with PP reference]

### Context Changes
- [New scenario where scale/urgency/complexity breaks the workaround — with PP reference]

## Job Chain
How this job connects to adjacent jobs:
- **Upstream job:** [What job must be done BEFORE this one]
- **Downstream job:** [What job depends on THIS one being done well]
- **Competing jobs:** [Alternative approaches the user currently uses]

## Process Stage Mapping
| Process Stage | Functional Jobs Active | Key Outcomes at Stake | Pain Point Count |
|---------------|----------------------|----------------------|-----------------|
| [Stage 1] | F1, F2 | Outcome 1, 3 | [X] |
| [Stage 2] | F3 | Outcome 2, 4 | [X] |

## Source References
- Pain Clusters: `[paths to cluster files]`
- Interview Analysis: `[paths to Agent 1 outputs]`
- Pain Point Mapping: `[path to painpoint-mapping.md]`
