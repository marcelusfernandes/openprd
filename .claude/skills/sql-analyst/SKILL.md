---
name: sql-analyst
description: "Writes and executes SQL queries against data warehouses (BigQuery, Snowflake, Databricks, Metabase, Redash) to extract product metrics and user behavior data. Use when quantitative data is needed."
---

# SQL Analyst — Data Warehouse Query Skill

## Purpose
Write and execute SQL queries against connected data warehouses to extract product metrics, user behavior data, and business KPIs.

## Supported Platforms

| Platform | MCP Server | Query Tool |
|----------|-----------|------------|
| BigQuery | bigquery | Execute SQL via MCP tools |
| Snowflake | snowflake | Execute SQL via MCP tools |
| Databricks | databricks | `databricks experimental aitools tools query` or MCP |
| Metabase | metabase | Execute SQL via MCP or API |
| Redash | redash | Execute saved queries or new SQL via MCP |

## Workflow

### 1. Understand the Question
Convert the PM's question to a data question:
- "Are users struggling with X?" → query event frequency, error rates, time-on-task
- "Which feature is most used?" → query feature usage events, DAU/MAU
- "Where do users drop off?" → funnel analysis query

### 2. Discover Schema
Before writing SQL, explore what data is available:
- For BigQuery: list datasets, tables, columns
- For Snowflake: browse catalogs/schemas/tables
- For Databricks: use `discover-schema` AI tool
- For Metabase: list databases and their schemas

### 3. Write & Execute Query
- Write clean, readable SQL with comments
- Use CTEs for complex queries
- Always include date filters (avoid full table scans)
- Limit results (TOP/LIMIT) for exploration
- Execute via the appropriate MCP tool

### 4. Interpret Results
- Summarize findings in plain language
- Tag with `[Source: {platform} SQL query, {date}]`
- Note caveats (sampling, date range, null handling)
- Connect findings to discovery context

## Common Query Patterns for Product Discovery

### Feature Usage
```sql
-- Daily active users by feature
SELECT feature_name, COUNT(DISTINCT user_id) as dau,
       DATE(event_time) as date
FROM events
WHERE event_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY feature_name, date
ORDER BY dau DESC
```

### Funnel Analysis
```sql
-- Step conversion rates
WITH funnel AS (
  SELECT user_id,
    MAX(CASE WHEN event = 'step_1' THEN 1 END) as step1,
    MAX(CASE WHEN event = 'step_2' THEN 1 END) as step2,
    MAX(CASE WHEN event = 'step_3' THEN 1 END) as step3
  FROM events WHERE event_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  GROUP BY user_id
)
SELECT COUNT(*) as total_users,
  SUM(step1) as reached_step1,
  SUM(step2) as reached_step2,
  SUM(step3) as reached_step3
FROM funnel
```

### Error/Friction Points
```sql
-- Most common errors by feature
SELECT feature, error_type, COUNT(*) as occurrences,
       COUNT(DISTINCT user_id) as affected_users
FROM error_events
WHERE event_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY feature, error_type
ORDER BY occurrences DESC
LIMIT 20
```

### Retention
```sql
-- Weekly retention cohorts
WITH cohort AS (
  SELECT user_id, DATE_TRUNC(MIN(event_time), WEEK) as cohort_week
  FROM events GROUP BY user_id
)
SELECT c.cohort_week,
  COUNT(DISTINCT c.user_id) as cohort_size,
  COUNT(DISTINCT CASE WHEN DATE_DIFF(e.event_time, c.cohort_week, WEEK) = 1 THEN e.user_id END) as week_1,
  COUNT(DISTINCT CASE WHEN DATE_DIFF(e.event_time, c.cohort_week, WEEK) = 2 THEN e.user_id END) as week_2
FROM cohort c LEFT JOIN events e ON c.user_id = e.user_id
GROUP BY c.cohort_week ORDER BY c.cohort_week
```

## Guardrails
- Never expose PII in query results
- Always use aggregated data (no individual user records unless explicitly asked)
- Tag all metrics: `[Source: {platform} SQL query, YYYY-MM-DD]`
- Note data freshness (when was the data last updated?)

## Prerequisites
- At least one data warehouse MCP configured
- See `_context/claude/mcp-setup.md` for setup
