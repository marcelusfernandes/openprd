---
name: palantir-foundry
description: Manages Palantir Foundry ontology, datasets, and SQL queries via official MCP server. Searches object types, runs transforms, queries data, and integrates ontology insights into discovery pipeline.
---

# Palantir Foundry — Ontology & Data Platform

## Purpose
Integrate Palantir Foundry into the discovery pipeline for ontology exploration, dataset querying, and data-driven product insights. Foundry's ontology provides a semantic layer over enterprise data.

## Integration Options
1. **MCP Server** (recommended): Official `palantir-mcp` npm package — configured in `.claude/.mcp.json`
2. **OSDK**: Ontology SDK for typed access (Python/TypeScript/Java)
3. **Python SDK**: `foundry-platform-sdk` for programmatic API access
4. **REST API**: OAuth2-authenticated endpoints

## MCP Capabilities (palantir-mcp)
- **Search ontology**: Find object types, action types, functions
- **Query datasets**: Run SQL queries against Foundry datasets
- **Modify ontology types**: Edit object type definitions (not data)
- **Create datasets**: Set up new datasets
- **Run transforms**: Execute Python transforms
- **Code context**: Inject OSDK/TypeScript/Python context for development

## Ontology MCP (Data Consumer)
Separate from palantir-mcp — exposes object types, actions, and query functions for reading/writing ontology **data** (not structure).

## Workflows

### Ontology Exploration for Discovery
1. Search ontology for object types related to product domain
2. Understand data relationships between entities
3. Query datasets for usage patterns, customer segments
4. Feed quantitative evidence into pain point analysis

### Data-Backed Pain Point Validation
1. Identify pain points from interviews (Phase 1)
2. Query Foundry datasets for quantitative evidence
3. Run SQL: user behavior patterns, error rates, drop-off funnels
4. Enrich pain reports with data from ontology objects

### Customer Segmentation via Ontology
1. Query customer/account object types
2. Analyze segments by behavior, revenue, tenure
3. Cross-reference with discovery personas
4. Identify underserved segments

### Metric Baseline Extraction
When `metric-definer` needs baselines:
1. Query relevant datasets for current metrics
2. Extract: conversion rates, retention, engagement
3. Provide baselines for KPI definition
4. Feed into success-metrics.md

## SQL Query Patterns
```sql
-- User behavior by segment
SELECT segment, COUNT(*) as users, AVG(sessions) as avg_sessions
FROM user_analytics
GROUP BY segment ORDER BY users DESC

-- Feature usage
SELECT feature_name, COUNT(DISTINCT user_id) as unique_users,
       COUNT(*) as total_events
FROM feature_events
WHERE event_date >= DATE_SUB(CURRENT_DATE, 30)
GROUP BY feature_name ORDER BY unique_users DESC

-- Funnel drop-off
SELECT step, COUNT(*) as users,
       ROUND(COUNT(*) * 100.0 / FIRST_VALUE(COUNT(*)) OVER (ORDER BY step), 1) as pct
FROM funnel_events
GROUP BY step ORDER BY step
```

## PM Query Patterns
- "What object types exist in our ontology related to customers?"
- "Query the user_analytics dataset for retention by cohort"
- "Show me feature usage data for the last 30 days"
- "What's our current conversion rate baseline?"
- "List all datasets related to onboarding"

## Output Format
Save to `/1-problem/1a-interview-analysis/foundry-data-{topic}.md`:
```
# Foundry Data Analysis — [Topic]
## Ontology Context
## SQL Queries Executed
## Key Findings
## Data Summary
## Cross-reference with Discovery
## Sources
```

## Rules
- ALWAYS cite: `[Source: Foundry dataset "{name}", query date={date}]`
- Tag data: `[Foundry data: N={row_count}, dataset={name}]`
- NEVER modify production ontology without confirmation
- Mark interpretations: `[AI analysis based on Foundry data]`
- Use read-only queries by default — write operations require explicit approval
