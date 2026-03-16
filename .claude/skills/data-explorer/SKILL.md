---
name: data-explorer
description: "Explores product data across analytics platforms (Amplitude, Mixpanel, PostHog, BigQuery, Metabase, etc.) to support discovery decisions with quantitative evidence. Use when PMs need to validate hypotheses, find usage patterns, or gather metrics."
---

# Data Explorer — Product Analytics Skill

## Purpose
Help Product Managers explore quantitative data from analytics platforms to:
- Validate qualitative findings from interviews with data
- Find usage patterns, funnels, and retention metrics
- Gather baseline metrics before solution design
- Support prioritization with actual numbers

## Available Platforms (via MCP)

### Tier 1: Full MCP Integration
These have dedicated MCP servers configured in `.claude/.mcp.json`:

| Platform | What you can do |
|----------|----------------|
| **Amplitude** | Query events, funnels, cohorts, dashboards, user segments |
| **Mixpanel** | Query events, funnels, retention, session replays |
| **PostHog** | Query insights, feature flags, session replays, annotations |
| **BigQuery** | Execute SQL, explore schemas, aggregate data |
| **Snowflake** | Execute SQL, browse catalogs, query tables |
| **Databricks** | Unity Catalog, SQL queries, AI tools, Genie |
| **Metabase** | Execute SQL, browse dashboards, create queries |
| **Tableau** | Browse workbooks, download data, explore dashboards |
| **Looker** | Semantic layer queries, dashboard exploration |

### Tier 2: API-based (via Bash)
| Platform | Access method |
|----------|--------------|
| **Redash** | MCP server or REST API via curl |
| **Pendo** | Remote MCP (beta) for visitor analytics |
| **Segment** | REST API via curl for event data |
| **Heap** | REST API via curl / Pipedream MCP bridge |

## Workflow

### 1. Identify the Question
What does the PM need to know? Examples:
- "How many users complete the campaign creation funnel?"
- "What's the retention rate for feature X?"
- "What are the most common drop-off points?"

### 2. Choose the Right Platform
- **User behavior/funnels** → Amplitude, Mixpanel, PostHog
- **SQL/warehouse queries** → BigQuery, Snowflake, Databricks
- **Dashboard data** → Metabase, Tableau, Looker
- **Product usage metrics** → Pendo, Heap

### 3. Query and Analyze
- Use MCP tools to query the platform
- Extract relevant metrics
- Format results clearly with tables and summaries

### 4. Connect to Discovery
Tag all data findings for use in the discovery workflow:
- `[Source: {platform} query on YYYY-MM-DD]` for verifiable claims
- Include the actual query or dashboard reference
- Note any caveats (date range, filters, sampling)

## Integration with Discovery Workflow

### Phase 0 (Context)
- Pull baseline metrics to enrich broad-context.md
- Example: "Current NPS: X, monthly active users: Y, key funnel conversion: Z%"

### Phase 1 (Problem Analysis)
- Validate pain points with usage data
- Enrich Agent 1 analysis with quantitative evidence
- Support Agent 2A granularity with frequency data
- Add metrics to Agent 4 consolidated journey

### Phase 2 (Solution Ideation)
- Provide baseline metrics for Agent S6 opportunity sizing
- Support Agent S9 prioritization with usage data
- Feed Agent S10 with metrics for executive materials

### Phase 3 (Delivery)
- Include metrics in Confluence documentation
- Add acceptance criteria based on current metrics to Jira stories

## Output Format
Always structure data findings as:

**Metric:** {name}
**Value:** {value} `[Source: {platform} query, {date}]`
**Context:** {what this means for the discovery}
**Query:** {the actual query or dashboard reference}

## Prerequisites
- At least one analytics platform MCP configured
- See `_context/claude/mcp-setup.md` for setup instructions
- If no MCP available, guide user to export data manually
