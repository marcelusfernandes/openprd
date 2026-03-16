# Job: Get Started Quickly and Start Producing Insights

## Job Statement
> **"When** I first discover a product discovery tool, **I want to** get from zero to my first actionable insight without needing developer skills, **so I can** validate whether this tool is worth adopting before investing more time.

## Job Context
- **Who:** All PM personas — especially non-technical PMs and solo founders
- **When:** Initial tool evaluation, first 30 minutes of usage
- **Where:** Onboarding phase — setup, configuration, first run
- **Frequency:** Once per user (but determines retention)
- **Related Pain Clusters:** C1 — Onboarding & First-Use Barriers [Source: painpoint-mapping.md]
- **Pain Point IDs:** PP-01, PP-02, PP-03, PP-04, PP-05

## Job Dimensions

### Functional Jobs (What they DO)
- **F1:** Install/access the tool and complete initial configuration
  - Evidence: PP-02 — API key setup requires developer knowledge; PP-03 — Git repo/CLI excludes non-technical users [Source: all-painpoints-granular.md]
- **F2:** Load their first data (interviews, recordings, analytics credentials) and get an initial result
  - Evidence: PP-01 — "what do I do now" confusion after onboarding; PP-04 — documentation overwhelm [Source: all-painpoints-granular.md]
- **F3:** Understand what the tool can do without reading extensive documentation
  - Evidence: PP-04 — "15 agents, 3 phases... made me feel like bringing a knife to a gunfight"; PP-05 — mixed language docs [Source: diego-analysis.md]

### Emotional Jobs (How they want to FEEL)
- **E1:** Feel confident that this tool is for people like them (not just for expert PMs or developers)
  - Evidence: PP-03 — "90% of PMs would never clone a repo" [Source: sarah-analysis.md]; PP-04 — documentation signals enterprise-only [Source: diego-analysis.md]
- **E2:** Feel that their time investment will pay off quickly
  - Evidence: PP-01 — post-onboarding confusion creates doubt about ROI [Source: sarah-analysis.md]

### Social Jobs (How they want to be PERCEIVED)
- **S1:** Be seen as someone who adopts smart tools (not someone who wastes time on setup)
  - Evidence: PP-30 — "2 hours fighting with the pipeline I could have just re-listened to my recordings" — negative ROI undermines the decision to adopt [Source: diego-analysis.md]
- **S2:** Be able to recommend the tool to peers without caveats about technical requirements
  - Evidence: PP-03 — all 4 sources recognize CLI as barrier [Source: cross-source-differentiation.md]

## Desired Outcome Expectations

| # | Desired Outcome | Importance | Current Satisfaction | Gap | Pain Evidence |
|---|----------------|------------|---------------------|-----|---------------|
| 1 | Minimize technical prerequisites to start using the tool | High | Low | High | PP-02, PP-03 |
| 2 | Minimize time from first interaction to first insight | High | Low | High | PP-01, PP-30 |
| 3 | Reduce cognitive overload during initial exploration | High | Medium | Medium | PP-04, PP-05 |
| 4 | Increase clarity of what to do next at each step | High | Low | High | PP-01 |
| 5 | Maximize accessibility for non-developer PMs | High | Low | High | PP-03 |
| 6 | Reduce language barriers for international users | Medium | Low | Medium | PP-05 |

## Switching Triggers

### Functional Failures
- PM tries to set up API keys and can't figure it out in 10 minutes → abandons tool [PP-02]
- Non-technical PM encounters Git clone requirement → immediate bounce [PP-03]

### Emotional Failures
- User finishes onboarding and feels lost ("what do I do now?") → trust collapses [PP-01]
- Documentation signals "this is not for me" → feeling of exclusion [PP-04]

### Context Changes
- PM wants to share tool with non-technical colleague → CLI is non-sharable [PP-03]
- International user encounters Portuguese-only docs → "this wasn't built for me" [PP-05]

## Job Chain
- **Upstream job:** None (this is the entry point)
- **Downstream job:** Analyze Qualitative Data Deeply (Job 2), Connect Quantitative and Qualitative Insights (Job 3)
- **Competing jobs:** Re-listen to recordings manually, use Dovetail, hire a UX researcher

## Source References
- Pain Clusters: `1-problem/1b-painpoints/painpoint-mapping.md`
- Interview Analysis: `1-problem/1a-interview-analysis/sarah-analysis.md`, `diego-analysis.md`, `aisha-analysis.md`, `tom-analysis.md`
- Cross-Source: `1-problem/1a-interview-analysis/cross-source-differentiation.md` (Convergence C6)
