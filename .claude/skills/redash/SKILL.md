---
name: redash
description: "Redash operations: execute SQL queries, run saved queries, browse dashboards via REST API. Use for ad-hoc SQL and saved dashboard data."
---

# Redash — SQL Queries & Dashboards

Core skill for Redash via REST API or MCP server (if configured).

## Prerequisites

- **API Key**: Redash → Profile → API Key
- **Instance URL**: Your Redash domain

## Quick Reference

### Explore
```bash
REDASH_URL="https://redash.company.com"
REDASH_KEY="your-api-key"

# List data sources
curl "$REDASH_URL/api/data_sources" -H "Authorization: Key $REDASH_KEY"

# List queries
curl "$REDASH_URL/api/queries" -H "Authorization: Key $REDASH_KEY" | jq '.[].name'

# List dashboards
curl "$REDASH_URL/api/dashboards" -H "Authorization: Key $REDASH_KEY" | jq '.[].name'
```

### Execute Queries
```bash
# Execute a saved query
curl -X POST "$REDASH_URL/api/queries/42/results" \
  -H "Authorization: Key $REDASH_KEY" \
  -H "Content-Type: application/json"

# Get results as CSV
curl "$REDASH_URL/api/queries/42/results.csv" \
  -H "Authorization: Key $REDASH_KEY" > results.csv

# Execute new query against a data source
curl -X POST "$REDASH_URL/api/query_results" \
  -H "Authorization: Key $REDASH_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data_source_id": 1, "query": "SELECT * FROM events LIMIT 100", "max_age": 0}'
```

### Dashboards
```bash
# Get dashboard with all widgets
curl "$REDASH_URL/api/dashboards/my-dashboard-slug" \
  -H "Authorization: Key $REDASH_KEY"
```

## For Discovery Workflow
- Tag: `[Source: Redash query #ID, YYYY-MM-DD]`
- Reference saved queries by ID for reproducibility
- Use for: ad-hoc SQL, saved team queries, dashboard data
