# Job: Run Data-First Growth Discovery That Feeds Experiments

## Job Statement
> **"When** I see a metric anomaly or conversion drop, **I want to** run a discovery cycle that starts from data, generates data-anchored hypotheses, and outputs experiment briefs, **so I can** rapidly test solutions with statistical rigor instead of guessing.

## Job Context
- **Who:** Growth PMs (primarily Tom's persona)
- **When:** After identifying a metric anomaly, conversion drop, or underperforming funnel step
- **Where:** Growth experiment cycle — from anomaly detection through hypothesis generation to test design
- **Frequency:** Continuous (weekly experiment cadence)
- **Related Pain Clusters:** C4 — Growth PM Workflow Fit [Source: painpoint-mapping.md]
- **Pain Point IDs:** PP-12, PP-13, PP-14, PP-15, PP-23, PP-27

## Job Dimensions

### Functional Jobs (What they DO)
- **F1:** Generate hypotheses filtered by experiment history (don't suggest already-tested ideas)
  - Evidence: PP-12 — "30% of its hypotheses are wasted" on already-tested-and-disproven ideas [Source: tom-analysis.md]
- **F2:** Create interview scripts anchored to specific data anomalies (not generic)
  - Evidence: PP-13 — "That's a Qualitative Research 101 question" — wants pointed questions tied to conversion drops [Source: tom-analysis.md]
- **F3:** Attach quantitative metrics to every pain point for OKR/experiment integration
  - Evidence: PP-14 — "Every pain point should have a metric attached" with current value and benchmark [Source: tom-analysis.md]
- **F4:** Build bottom-up revenue impact models from actual conversion data
  - Evidence: PP-15 — top-down estimates have "confidence intervals too wide to be useful" [Source: tom-analysis.md]
- **F5:** Output experiment briefs (hypothesis, metric, MDE, test design) instead of Jira stories
  - Evidence: PP-23 — "Growth Discovery workflow that outputs experiment briefs instead of Jira stories" [Source: tom-analysis.md]
- **F6:** Overlay conversion rates and timing data on journey maps
  - Evidence: PP-27 — "Show me the conversion rate at each step... p50 and p95 time" [Source: tom-analysis.md]

### Emotional Jobs (How they want to FEEL)
- **E1:** Feel confident that hypotheses are novel and worth testing
  - Evidence: PP-12 — wasting experiment cycles on already-tested ideas creates frustration [Source: tom-analysis.md]
- **E2:** Feel that the tool understands the growth PM's specific workflow
  - Evidence: PP-23 — current output format signals "this wasn't built for growth PMs" [Source: tom-analysis.md]

### Social Jobs (How they want to be PERCEIVED)
- **S1:** Be seen as running a rigorous experiment program by CEO
  - Evidence: PP-14, PP-15 — metric hooks and bottom-up models demonstrate analytical rigor [Source: tom-analysis.md]
- **S2:** Be perceived as leveraging cutting-edge tools (first-mover in "Growth Discovery")
  - Evidence: Divergence D5 — "Growth Discovery is a distinct niche product opportunity" [Source: cross-source-differentiation.md]

## Desired Outcome Expectations

| # | Desired Outcome | Importance | Current Satisfaction | Gap | Pain Evidence |
|---|----------------|------------|---------------------|-----|---------------|
| 1 | Eliminate hypothesis waste from suggesting already-tested ideas | High | Low | High | PP-12 |
| 2 | Maximize data-anchoring of interview scripts to specific anomalies | High | Low | High | PP-13 |
| 3 | Increase metric attachment to every pain point (current + benchmark) | High | Low | High | PP-14 |
| 4 | Maximize accuracy of revenue impact estimates (bottom-up, not top-down) | High | Low | High | PP-15 |
| 5 | Increase output format fit for experiment workflows (briefs, not stories) | High | Low | High | PP-23 |
| 6 | Maximize quantitative overlay on journey maps | High | Low | High | PP-27 |

## Switching Triggers

### Functional Failures
- Tool suggests 10 hypotheses → 3 already tested and disproven → PM loses trust in recommendations [PP-12]
- PM needs experiment brief → tool outputs Jira story → has to rewrite entirely [PP-23]
- Revenue model is top-down → CFO rejects estimate → PM looks unprepared [PP-15]

### Emotional Failures
- Generic interview questions feel like "Research 101" → PM feels the tool doesn't understand their job [PP-13]
- Pain report has no metrics → PM can't connect findings to OKRs → feels like qualitative fluff [PP-14]

### Context Changes
- Team scales from 1 experiment/month to 4/week → manual hypothesis filtering becomes impossible [PP-12]
- PM switches from traditional discovery to data-first → tool's pipeline doesn't support the workflow [PP-23]

## Job Chain
- **Upstream job:** Connect Quant+Qual Insights (Job 3) — needs deep data integration as prerequisite
- **Downstream job:** Deliver Outputs to Stakeholders (Job 2) — experiment briefs as delivery format
- **Competing jobs:** Manual hypothesis spreadsheets, Statsig/Amplitude built-in tools, custom internal tools

## Source References
- Pain Clusters: `1-problem/1b-painpoints/painpoint-mapping.md`
- Interview Analysis: `tom-analysis.md`
- Cross-Source: `cross-source-differentiation.md` (Divergence D5)
