---
name: pendo
description: "Pendo product analytics: query visitor data, feature usage, page analytics, guides via REST API. Use for in-app analytics, NPS, and feature adoption."
---

# Pendo — Product Analytics & In-App Guides

Core skill for Pendo via REST API. No CLI available.

## Prerequisites

- **Integration Key**: Pendo → Settings → Integrations → Integration Keys
- **Base URL**: `https://app.pendo.io` (US) or `https://eu.pendo.io` (EU)

## Quick Reference

### Feature Usage
```bash
# List features
curl "https://app.pendo.io/api/v1/feature" \
  -H "X-Pendo-Integration-Key: YOUR_KEY" \
  -H "Content-Type: application/json"

# Feature usage aggregation
curl -X POST "https://app.pendo.io/api/v1/aggregation" \
  -H "X-Pendo-Integration-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "response": {"mimeType": "application/json"},
    "request": {
      "pipeline": [
        {"source": {"featureEvents": {"featureId": "FEATURE_ID"}}},
        {"identified": "visitorId"},
        {"dateRange": {"first": "1709251200000", "count": 30, "unit": "day"}},
        {"group": {"group": ["visitorId"]}},
        {"count": {}}
      ]
    }
  }'
```

### Page Analytics
```bash
# List pages
curl "https://app.pendo.io/api/v1/page" \
  -H "X-Pendo-Integration-Key: YOUR_KEY"

# Page views aggregation
curl -X POST "https://app.pendo.io/api/v1/aggregation" \
  -H "X-Pendo-Integration-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "response": {"mimeType": "application/json"},
    "request": {
      "pipeline": [
        {"source": {"pageEvents": {"pageId": "PAGE_ID"}}},
        {"dateRange": {"first": "-30d"}},
        {"group": {"group": ["day"]}},
        {"count": {}}
      ]
    }
  }'
```

### Visitor Data
```bash
# Get visitor profile
curl "https://app.pendo.io/api/v1/visitor/VISITOR_ID" \
  -H "X-Pendo-Integration-Key: YOUR_KEY"

# List guides
curl "https://app.pendo.io/api/v1/guide" \
  -H "X-Pendo-Integration-Key: YOUR_KEY"

# Guide analytics
curl "https://app.pendo.io/api/v1/guide/GUIDE_ID/analytics" \
  -H "X-Pendo-Integration-Key: YOUR_KEY"
```

### NPS Data
```bash
# NPS responses via aggregation
curl -X POST "https://app.pendo.io/api/v1/aggregation" \
  -H "X-Pendo-Integration-Key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "response": {"mimeType": "application/json"},
    "request": {
      "pipeline": [
        {"source": {"pollEvents": null}},
        {"dateRange": {"first": "-90d"}},
        {"group": {"group": ["pollResponse"]}},
        {"count": {}}
      ]
    }
  }'
```

## For Discovery Workflow
- Tag: `[Source: Pendo API query, YYYY-MM-DD]`
- Use for: feature adoption rates, page analytics, NPS scores, guide engagement
- Feature usage data validates pain points from interviews
- NPS data enriches problem-report.md
