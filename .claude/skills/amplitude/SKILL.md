---
name: amplitude
description: "Amplitude product analytics: query events, funnels, cohorts, dashboards via REST API. Use for user behavior analysis, feature adoption, and retention data."
---

# Amplitude — Product Analytics

Core skill for Amplitude via REST API (primary) or MCP server.

## Prerequisites

- **API Key + Secret Key**: Amplitude → Settings → Projects → API Keys
- Note: `ampli` CLI exists but is for instrumentation ONLY (not data queries)

## Claude Code — API Access

```bash
# Base URL
# US: https://amplitude.com/api/2
# EU: https://analytics.eu.amplitude.com/api/2

# Auth: Basic auth with api_key:secret_key
AMPLITUDE_AUTH=$(echo -n "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" | base64)
```

## Quick Reference

### Export Events (Raw Data)
```bash
# Export raw events for a date range (returns zipped JSON)
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/2/export?start=20250101T00&end=20250131T23"
```

### Get Chart Data
```bash
# Get any saved chart's data as JSON
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/3/chart/${CHART_ID}/query"

# Get chart data as CSV
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/3/chart/${CHART_ID}/csv"
```

### Dashboard Data
```bash
# List dashboards
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/3/dashboards"

# Get specific dashboard
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/3/dashboards/${DASHBOARD_ID}"
```

### User Activity
```bash
# User activity (last N events)
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/2/useractivity?user=USER_ID"

# User search
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/2/usersearch?user=email@example.com"
```

### Event Segmentation
```bash
# Event counts by day (last 30 days)
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/2/events/segmentation?e={\"event_type\":\"page_view\"}&start=20250201&end=20250301&m=uniques"
```

### Funnel Analysis
```bash
# Funnel query (requires funnel_id from Amplitude UI)
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/2/funnels?fs={\"events\":[{\"event_type\":\"step1\"},{\"event_type\":\"step2\"},{\"event_type\":\"step3\"}]}&start=20250201&end=20250301"
```

### Retention
```bash
# Retention analysis
curl -u "${AMPLITUDE_API_KEY}:${AMPLITUDE_SECRET_KEY}" \
  "https://amplitude.com/api/2/retention?re={\"event_type\":\"any_event\"}&se={\"event_type\":\"any_event\"}&start=20250201&end=20250301"
```

## Rate Limits
- 1000 cost units per 5 minutes
- 108,000 cost units per hour
- Export API: 100 requests/hour

## MCP Alternative
If Amplitude MCP is configured (`.claude/.mcp.json`), use for natural language queries. API is preferred for specific chart/dashboard data extraction.

## For Discovery Workflow
- Tag: `[Source: Amplitude API query, YYYY-MM-DD]`
- Use for: feature adoption rates, funnel conversion, retention curves, user segments
- Export chart data for quantitative evidence in pain-report.md
- Dashboard screenshots for executive presentations
