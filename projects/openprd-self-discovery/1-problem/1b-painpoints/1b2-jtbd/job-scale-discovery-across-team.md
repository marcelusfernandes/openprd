# Job: Scale Discovery Across the Team With Enterprise Governance

## Job Statement
> **"When** I've completed a discovery cycle, **I want to** share findings with my team, collaborate in real-time, and meet security/compliance requirements, **so I can** create shared understanding across product, design, and engineering — not just a document on my laptop.

## Job Context
- **Who:** Enterprise PMs (primarily Aisha), mid-market PMs with team collaboration needs (Sarah, Tom)
- **When:** After analysis, during team alignment, and continuously for organizational adoption
- **Where:** Collaboration, sharing, governance, and security layers
- **Frequency:** Ongoing — every discovery cycle and every stakeholder interaction
- **Related Pain Clusters:** C5 — Collaboration, Security & Enterprise Readiness [Source: painpoint-mapping.md]
- **Pain Point IDs:** PP-24, PP-25, PP-26, PP-27, PP-28, PP-32

## Job Dimensions

### Functional Jobs (What they DO)
- **F1:** Share discovery findings via URL or collaboration platform with teammates
  - Evidence: PP-25 — "I can't share a link with my designer" [Source: sarah-analysis.md]; "A repo on my laptop is a non-starter" [Source: aisha-analysis.md]
- **F2:** Review AI-generated outputs in draft mode before publishing (governance)
  - Evidence: PP-24 — "I can't have an AI auto-create stories — they need technical review, estimation, dependency mapping" [Source: aisha-analysis.md]
- **F3:** Use interactive, visual artifacts for workshops (not static markdown)
  - Evidence: PP-26 — "No visual layout, no sticky notes, no color coding... For a collaborative workshop artifact? Useless" [Source: aisha-analysis.md]
- **F4:** Meet enterprise security and compliance requirements
  - Evidence: PP-28 — "My IT team would never approve a tool that stores customer interview data in a local git repo. We need SOC 2, data residency, access controls" [Source: aisha-analysis.md]

### Emotional Jobs (How they want to FEEL)
- **E1:** Feel that discovery creates shared understanding, not just a personal document
  - Evidence: PP-32 — "Depth without collaboration is limited value... The output of discovery isn't a document — it's shared understanding" [Source: aisha-analysis.md]
- **E2:** Feel confident that the tool meets organizational security standards
  - Evidence: PP-28 — IT approval is a hard gate for enterprise adoption [Source: aisha-analysis.md]

### Social Jobs (How they want to be PERCEIVED)
- **S1:** Be seen as facilitating team-wide product thinking (not gatekeeping insights)
  - Evidence: PP-25 — inability to share makes PM the bottleneck [Source: sarah-analysis.md, aisha-analysis.md]
- **S2:** Be perceived as using tools that meet enterprise standards (not "scrappy hacks")
  - Evidence: PP-28 — SOC 2 and SSO are table stakes for enterprise credibility [Source: aisha-analysis.md]

## Desired Outcome Expectations

| # | Desired Outcome | Importance | Current Satisfaction | Gap | Pain Evidence |
|---|----------------|------------|---------------------|-----|---------------|
| 1 | Maximize shareability of discovery outputs (URLs, real-time access) | High | Low | High | PP-25, PP-32 |
| 2 | Increase governance controls (draft mode, review workflows) | High | Low | High | PP-24 |
| 3 | Maximize visual interactivity of journey maps and artifacts | High | Low | High | PP-26 |
| 4 | Increase security compliance (SOC 2, SSO, data residency) | High (enterprise) | Low | High | PP-28 |
| 5 | Reduce isolation of discovery insights ("lonely tool" problem) | High | Low | High | PP-32 |

## Switching Triggers

### Functional Failures
- PM completes discovery → can't share with design lead → insights stay siloed [PP-25]
- Enterprise PM proposes tool → IT blocks due to local git storage of customer data [PP-28]
- PM wants to run journey mapping workshop → markdown map is useless for collaboration [PP-26]

### Emotional Failures
- PM produces excellent analysis → "powerful but lonely" — value dies on their laptop [PP-32]
- PM uses auto-generated Jira stories → team rejects without review process [PP-24]

### Context Changes
- PM team grows from 1 to 5 → local-first model can't scale [PP-25]
- Company achieves SOC 2 → all tools must comply → OpenPRD doesn't qualify [PP-28]

## Job Chain
- **Upstream job:** All analysis jobs (1, 2, 3, 4) — collaboration only matters if analysis is valuable
- **Downstream job:** Deliver Outputs to Stakeholders (Job 2) — collaborative review feeds into better outputs
- **Competing jobs:** Dovetail (built-in collaboration), Miro (visual workshops), Notion (team knowledge base)

## Source References
- Pain Clusters: `1-problem/1b-painpoints/painpoint-mapping.md`
- Interview Analysis: `aisha-analysis.md`, `sarah-analysis.md`
- Cross-Source: `cross-source-differentiation.md` (Divergence D2, D4)
