---
name: agent-5-report-generator
description: Generates strategic reports synthesizing problem analysis across all dimensions. Creates pain-report.md and problem-report.md. Use when creating executive reports, strategic summaries, or running Agent 5.
user-invocable: false
---

# Agent 5 - Strategic Report Generator

Tag responses with [Agent5].

## Inputs
- `/0-documentation/broad-context.md` (Agent 0)
- `/1-problem/1b-painpoints/painpoint-mapping.md` (Agent 2B)
- `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` (Agent 2C)
- `/1-problem/1c-asis-journey/asis-journey.md` (Agent 4)
- `/1-problem/0-data-landscape/data-landscape.md` (Agent 0) — **OPTIONAL**

## Outputs
1. `/1-problem/1d-problem-output/pain-report.md`
2. `/1-problem/1d-problem-output/problem-report.md`

Use template: [references/report-template.md](references/report-template.md)

**Note:** Journey visualization (journey-output.md) is handled by Agent 6 Visual Designer.

## TL;DR Obrigatório

Ambos os reports (pain-report.md e problem-report.md) DEVEM começar com um TL;DR de exatamente 1-2 frases no topo do documento, ANTES do executive summary. Formato:

```
> **TL;DR:** [1-2 sentence summary of the most critical finding and recommended action]
```

O TL;DR deve capturar o achado mais crítico e a ação recomendada — stakeholders querem o bottom line antes de ler qualquer coisa.

## Data Landscape Integration

Se `/1-problem/0-data-landscape/data-landscape.md` existir, incorporar baseline quantitativo nos reports. Usar métricas do data-landscape para contextualizar severidade dos pain points (ex: "Este cluster afeta o step com 45% drop-off no funil [Source: data-landscape.md]").

## Pain Report Structure
- TL;DR (1-2 sentences — see above)
- Executive summary with pain point statistics by type (UX/Ops/Business/Tech)
- Quantitative data summary (surveys, metrics)
- Detailed analysis BY DIMENSION: UX, Operational, Business, Technical
- **Jobs to Be Done synthesis:** Top underserved jobs and highest-gap outcomes (from Agent 2C)
- Multi-dimensional priority matrix
- Recommendations by dimension

## Problem Report Structure
- TL;DR (1-2 sentences — see above)
- Multi-dimensional problem statement
- **Jobs to Be Done framing:** Reframe the problem space through the lens of unmet jobs and underserved outcomes — executive-friendly language
- Objectives review by dimension (from Agent 0)
- Quantitative findings
- Key findings BY DIMENSION
- Strategic implications BY DIMENSION (impact, risk, opportunity cost)
- Recommendations and success metrics per dimension

## Key Rules
- Cover ALL 4 dimensions in both reports
- Include pain point statistics by type from Agent 2B
- Include JTBD outcome opportunity scores from Agent 2C
- Include quantitative data from Agents 0-2
- Source all claims to original files
- Cross-reference both reports for consistency

## Quality Gates
- Both reports follow template structure
- Both reports start with TL;DR before executive summary
- All 4 dimensions addressed in both reports
- Quantitative data included
- Data-landscape metrics incorporated when available
- Source references for all claims
