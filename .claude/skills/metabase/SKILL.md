---
name: metabase
description: "Metabase operations: execute SQL queries, browse dashboards, explore database schemas via REST API or MCP. Use for BI queries and dashboard data."
---

# Metabase — BI & SQL

Core skill for Metabase via REST API or MCP server (if configured).

## Prerequisites

- **API Key**: Metabase → Admin → API Keys
- **Instance URL**: Your Metabase domain (e.g., `https://metabase.company.com`)

## Claude Code — API Access

```bash
# All requests use API key header
METABASE_URL="https://metabase.company.com"
METABASE_KEY="your-api-key"

# Or session-based auth
SESSION=$(curl -s -X POST "$METABASE_URL/api/session" \
  -H "Content-Type: application/json" \
  -d '{"username":"user@email.com","password":"pass"}' | jq -r '.id')
```

## Quick Reference

### Explore Schema
```bash
# List databases
curl "$METABASE_URL/api/database" -H "x-api-key: $METABASE_KEY"

# Get database metadata (tables, columns)
curl "$METABASE_URL/api/database/1/metadata" -H "x-api-key: $METABASE_KEY"

# List tables in a database
curl "$METABASE_URL/api/table" -H "x-api-key: $METABASE_KEY"

# Get table metadata
curl "$METABASE_URL/api/table/42/query_metadata" -H "x-api-key: $METABASE_KEY"
```

### Run SQL Queries
```bash
# Execute native SQL query
curl -X POST "$METABASE_URL/api/dataset" \
  -H "x-api-key: $METABASE_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "database": 1,
    "type": "native",
    "native": {"query": "SELECT * FROM events LIMIT 20"}
  }'

# Export query results as CSV
curl -X POST "$METABASE_URL/api/dataset/csv" \
  -H "x-api-key: $METABASE_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "database": 1,
    "type": "native",
    "native": {"query": "SELECT * FROM events LIMIT 1000"}
  }' > results.csv
```

### Saved Questions (Cards)
```bash
# List saved questions
curl "$METABASE_URL/api/card" -H "x-api-key: $METABASE_KEY" | jq '.[].name'

# Execute a saved question
curl -X POST "$METABASE_URL/api/card/42/query" -H "x-api-key: $METABASE_KEY"

# Export saved question as CSV
curl -X POST "$METABASE_URL/api/card/42/query/csv" -H "x-api-key: $METABASE_KEY" > results.csv
```

### Dashboards
```bash
# List dashboards
curl "$METABASE_URL/api/dashboard" -H "x-api-key: $METABASE_KEY" | jq '.[].name'

# Get dashboard details
curl "$METABASE_URL/api/dashboard/7" -H "x-api-key: $METABASE_KEY"
```

## MCP Alternative
If Metabase MCP is configured (`@cognitionai/metabase-mcp-server`), use for schema browsing and natural language queries. API is preferred for batch exports and saved question execution.

## For Discovery Workflow
- Tag: `[Source: Metabase query/dashboard "Name", YYYY-MM-DD]`
- Use for: ad-hoc SQL analysis, dashboard data, schema exploration
- Export CSVs for quantitative evidence
- Reference saved dashboards in reports
