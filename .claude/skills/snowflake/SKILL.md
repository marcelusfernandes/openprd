---
name: snowflake
description: "Snowflake CLI operations: SQL queries, schema exploration, data export via SnowSQL. Use for all Snowflake data warehouse tasks."
---

# Snowflake — Data Warehouse

Core skill for Snowflake via `snowsql` CLI (preferred) or MCP server.

## Prerequisites

1. **SnowSQL installed**: `snowsql --version`
   - macOS: `brew install --cask snowflake-snowsql`
   - Linux: Download from Snowflake docs
2. **Config file**: `~/.snowsql/config` with connection parameters
3. **Or use CLI args**: `snowsql -a ACCOUNT -u USER`

## Claude Code — IMPORTANT

Each Bash command runs in a **separate shell session**. Always pass connection inline.

```bash
# WORKS: all args inline
snowsql -a myaccount -u myuser -d mydb -s myschema -w mywarehouse -q "SELECT 1"

# WORKS: named connection from config
snowsql -c my_connection -q "SELECT 1"

# DOES NOT WORK: interactive session state
snowsql  # Opens interactive, can't type commands
```

## Quick Reference

### Explore Data
```bash
# List databases
snowsql -a ACCOUNT -u USER -q "SHOW DATABASES"

# List schemas
snowsql -a ACCOUNT -u USER -d DB -q "SHOW SCHEMAS"

# List tables
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -q "SHOW TABLES"

# Describe table
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -q "DESCRIBE TABLE tablename"

# Preview data
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -q "SELECT * FROM tablename LIMIT 20"
```

### Run Queries
```bash
# Inline query
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -w WH -q "SELECT count(*) FROM events"

# Query from file
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -w WH -f query.sql

# CSV output
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -w WH \
  -o output_format=csv -o header=true -o timing=false \
  -q "SELECT * FROM events LIMIT 100" > output.csv

# JSON output
snowsql -a ACCOUNT -u USER -d DB -s SCHEMA -w WH \
  -o output_format=json -q "SELECT * FROM events LIMIT 100"
```

### Common PM Queries
```bash
# Active users
snowsql -c prod -q "
SELECT DATE_TRUNC('day', event_time) as date, COUNT(DISTINCT user_id) as dau
FROM events
WHERE event_time >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY date ORDER BY date"

# Feature adoption
snowsql -c prod -q "
SELECT feature_name, COUNT(*) as uses, COUNT(DISTINCT user_id) as users
FROM feature_events
WHERE event_time >= DATEADD('day', -7, CURRENT_DATE())
GROUP BY feature_name ORDER BY uses DESC LIMIT 20"
```

## MCP Alternative
If Snowflake MCP is configured, use for natural language queries. CLI preferred for complex SQL, exports, and when MCP auth is not configured.

## For Discovery Workflow
- Tag: `[Source: Snowflake query, YYYY-MM-DD]`
- Aggregate only (no PII)
- Note warehouse, date range, filters
- Include SQL for reproducibility
