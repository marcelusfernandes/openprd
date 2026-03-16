---
name: mixpanel
description: "Mixpanel event analytics: query events, funnels, retention, user profiles via MCP or API. Use for event-based analytics, conversion funnels, and user behavior."
---

# Mixpanel — Event Analytics

Core skill for Mixpanel via official MCP server (preferred) or REST API.

## Prerequisites

### MCP (Preferred)
- Configured in `.claude/.mcp.json` via `mcp-remote`
- Auth: OAuth flow (browser sign-in on first use)
- MCP handles natural language queries to events, funnels, session replays

### API Access
- **Service Account**: Mixpanel → Settings → Service Accounts
- **Project Token**: Mixpanel → Settings → Project Details

## REST API Quick Reference

### Query Events
```bash
# Insights query (event counts)
curl https://mixpanel.com/api/2.0/insights \
  -u SERVICE_ACCOUNT_USERNAME:SERVICE_ACCOUNT_SECRET \
  --data-urlencode 'project_id=PROJECT_ID' \
  --data-urlencode 'bookmark_id=INSIGHT_ID'

# Export raw events
curl "https://data.mixpanel.com/api/2.0/export?from_date=2025-01-01&to_date=2025-01-31&event=[\"page_view\"]" \
  -u SERVICE_ACCOUNT_USERNAME:SERVICE_ACCOUNT_SECRET \
  -H "Accept: application/json"
```

### Funnel Analysis
```bash
# Get funnel by ID
curl "https://mixpanel.com/api/2.0/funnels?funnel_id=FUNNEL_ID&from_date=2025-01-01&to_date=2025-01-31" \
  -u SERVICE_ACCOUNT_USERNAME:SERVICE_ACCOUNT_SECRET
```

### Retention
```bash
# Retention data
curl "https://mixpanel.com/api/2.0/retention?from_date=2025-01-01&to_date=2025-01-31&born_event=signup&event=any_event" \
  -u SERVICE_ACCOUNT_USERNAME:SERVICE_ACCOUNT_SECRET
```

### User Profiles
```bash
# Query user profiles (Engage)
curl "https://mixpanel.com/api/2.0/engage" \
  -u SERVICE_ACCOUNT_USERNAME:SERVICE_ACCOUNT_SECRET \
  --data-urlencode 'where=properties["plan"] == "pro"' \
  --data-urlencode 'output_properties=["$name","$email","plan","last_login"]'
```

## Rate Limits
- 60 queries per hour (Query API)
- Max 5 concurrent requests
- Export API: separate limits

## For Discovery Workflow
- Tag: `[Source: Mixpanel query, YYYY-MM-DD]`
- MCP for natural language exploration
- API for specific metric extraction
- Use for: event frequency, funnel drop-offs, retention by cohort
