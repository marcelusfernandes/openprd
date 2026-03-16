# Job: Connect Quantitative Data and Qualitative Insights Automatically

## Job Statement
> **"When** I have both analytics data and interview findings, **I want to** see them synthesized into a single coherent narrative automatically, **so I can** make evidence-backed decisions without manually cross-referencing spreadsheets and transcripts.

## Job Context
- **Who:** PMs with access to both quantitative and qualitative data — Sarah, Tom, Aisha
- **When:** After loading both data types; during analysis phase
- **Where:** Integration and synthesis phases of the discovery workflow
- **Frequency:** Every discovery cycle where both data types are available
- **Related Pain Clusters:** C3 — Integration Depth & Data Connectivity [Source: painpoint-mapping.md]
- **Pain Point IDs:** PP-06, PP-07, PP-08, PP-09, PP-10, PP-11

## Job Dimensions

### Functional Jobs (What they DO)
- **F1:** Run deep, autonomous queries against analytics platforms (not just basic event counts)
  - Evidence: PP-08 — BigQuery integration is shallow: "Not 3 queries — 30 queries" [Source: tom-analysis.md]
- **F2:** Automatically overlay quantitative metrics onto qualitative findings
  - Evidence: PP-11 — "two separate tools that happen to live in the same repo" [Source: sarah-analysis.md]; PP-09 — Salesforce returns raw JSON, no enrichment [Source: aisha-analysis.md]
- **F3:** Triangulate support/CRM data with interview pain points
  - Evidence: PP-10 — "No 'hey, 47 tickets about the same permissions issue your interviewees mentioned'" [Source: sarah-analysis.md]
- **F4:** Import data from cloud sources without manual download
  - Evidence: PP-06 — Zoom recordings in cloud, not local files [Source: diego-analysis.md]
- **F5:** Iterate on queries without friction
  - Evidence: PP-07 — Amplitude query requires "three round-trips... like debugging SQL through a chatbot" [Source: sarah-analysis.md]

### Emotional Jobs (How they want to FEEL)
- **E1:** Feel that the tool understands their data deeply, not superficially
  - Evidence: PP-08 — shallow queries feel like "a junior analyst" doing the work [Source: tom-analysis.md]
- **E2:** Feel confident that synthesis is comprehensive, not cherry-picked
  - Evidence: PP-11 — "data points side by side" not "true integrated analysis" [Source: tom-analysis.md]

### Social Jobs (How they want to be PERCEIVED)
- **S1:** Be perceived as having rigorous, data-backed findings (not just anecdotes)
  - Evidence: PP-11, PP-14 — lack of metric hooks makes findings look qualitative-only [Source: tom-analysis.md]
- **S2:** Present insights that combine the "why" (interviews) with the "what" (metrics)
  - Evidence: Convergence C3 — universally desired capability [Source: cross-source-differentiation.md]

## Desired Outcome Expectations

| # | Desired Outcome | Importance | Current Satisfaction | Gap | Pain Evidence |
|---|----------------|------------|---------------------|-----|---------------|
| 1 | Maximize depth of autonomous data exploration (segmented, multi-dimensional) | High | Low | High | PP-08 |
| 2 | Maximize automatic triangulation between qualitative and quantitative data | High | Low | High | PP-11 |
| 3 | Reduce manual steps in cross-referencing support data with interview themes | High | Low | High | PP-10 |
| 4 | Increase richness of CRM/support data integration (enrichment, not raw JSON) | High | Low | High | PP-09 |
| 5 | Minimize friction in iterating analytics queries | Medium | Low | Medium | PP-07 |
| 6 | Reduce manual data import steps (cloud-native ingestion) | Low | Low | Low | PP-06 |

## Switching Triggers

### Functional Failures
- Growth PM asks for segmented cohort analysis → tool returns basic event counts → has to do it manually in BigQuery [PP-08]
- PM loads Intercom data → gets ticket dump without correlation to interview findings → does manual mapping [PP-10]

### Emotional Failures
- PM sees analytics and interviews as "separate tools" → feels synthesis promise is broken [PP-11]
- PM receives raw Salesforce JSON → feels tool is an extra step, not a time-saver [PP-09]

### Context Changes
- PM discovers a data anomaly → wants to immediately ask "did any interviewee mention this?" → no automated path [PP-11]
- Scaling from 3 to 30 analytical queries overwhelms the current shallow integration [PP-08]

## Job Chain
- **Upstream job:** Get Started Quickly (Job 1)
- **Downstream job:** Deliver Outputs to Stakeholders (Job 2)
- **Competing jobs:** Manual cross-referencing in spreadsheets, Dovetail + separate BI tool, hire data analyst

## Source References
- Pain Clusters: `1-problem/1b-painpoints/painpoint-mapping.md`
- Interview Analysis: `sarah-analysis.md`, `tom-analysis.md`, `aisha-analysis.md`
- Cross-Source: `cross-source-differentiation.md` (Convergence C3, Divergence D3)
