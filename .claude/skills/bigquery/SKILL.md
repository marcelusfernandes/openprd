---
name: bigquery
description: "BigQuery CLI operations: SQL queries, schema exploration, data export, dataset management. Use for all BigQuery and Google data warehouse tasks."
---

# BigQuery — Google Data Warehouse

Core skill for BigQuery via `bq` CLI (preferred) or MCP server.

## Prerequisites

1. **gcloud SDK installed**: `gcloud --version`
   - If not: `curl https://sdk.cloud.google.com | bash`
2. **Authenticated**: `gcloud auth application-default login`
3. **Project set**: `gcloud config set project YOUR_PROJECT_ID`

## Claude Code — IMPORTANT

Each Bash command runs in a **separate shell session**.

```bash
# WORKS: inline project flag
bq query --project_id=myproject --use_legacy_sql=false 'SELECT 1'

# WORKS: chained with &&
export CLOUDSDK_CORE_PROJECT=myproject && bq query --use_legacy_sql=false 'SELECT 1'

# DOES NOT WORK: separate commands
export CLOUDSDK_CORE_PROJECT=myproject
bq query --use_legacy_sql=false 'SELECT 1'  # project not set!
```

## Quick Reference

### Explore Data
```bash
# List datasets
bq ls --project_id=PROJECT

# List tables in a dataset
bq ls PROJECT:DATASET

# Show table schema
bq show --schema --format=prettyjson PROJECT:DATASET.TABLE

# Preview rows
bq head -n 20 PROJECT:DATASET.TABLE

# Get table info (size, rows, last modified)
bq show --format=prettyjson PROJECT:DATASET.TABLE
```

### Run Queries
```bash
# Simple query
bq query --use_legacy_sql=false 'SELECT column FROM dataset.table LIMIT 100'

# Query with format
bq query --use_legacy_sql=false --format=csv 'SELECT * FROM dataset.table LIMIT 50'

# Query to file (via redirect)
bq query --use_legacy_sql=false --format=csv 'SELECT ...' > output.csv

# Dry run (estimate bytes scanned)
bq query --use_legacy_sql=false --dry_run 'SELECT * FROM dataset.table'

# Query from file
bq query --use_legacy_sql=false < query.sql
```

### Common PM Queries
```bash
# Daily active users
bq query --use_legacy_sql=false '
SELECT DATE(event_timestamp) as date, COUNT(DISTINCT user_id) as dau
FROM `project.dataset.events`
WHERE event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY date ORDER BY date'

# Feature usage
bq query --use_legacy_sql=false '
SELECT event_name, COUNT(*) as total, COUNT(DISTINCT user_id) as unique_users
FROM `project.dataset.events`
WHERE event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
GROUP BY event_name ORDER BY total DESC LIMIT 20'

# Funnel conversion
bq query --use_legacy_sql=false '
WITH funnel AS (
  SELECT user_id,
    MAX(IF(event_name="step_1",1,0)) as s1,
    MAX(IF(event_name="step_2",1,0)) as s2,
    MAX(IF(event_name="step_3",1,0)) as s3
  FROM `project.dataset.events`
  WHERE event_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
  GROUP BY user_id
)
SELECT COUNT(*) as users, SUM(s1) as step1, SUM(s2) as step2, SUM(s3) as step3
FROM funnel'
```

### Export Data
```bash
# Export table to GCS as CSV
bq extract --destination_format=CSV PROJECT:DATASET.TABLE gs://bucket/export.csv

# Export query results to GCS
bq query --use_legacy_sql=false --destination_table=PROJECT:DATASET.temp_export 'SELECT ...'
bq extract PROJECT:DATASET.temp_export gs://bucket/results.csv
bq rm -f PROJECT:DATASET.temp_export
```

## MCP Alternative
If BigQuery MCP is configured (see `.claude/.mcp.json`), use MCP tools for schema browsing and natural language queries. CLI is preferred for complex SQL and exports.

## For Discovery Workflow
- Tag all findings: `[Source: BigQuery query, YYYY-MM-DD]`
- Always aggregate (no PII in results)
- Note date range and filters used
- Include the SQL query for reproducibility
