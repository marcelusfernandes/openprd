---
name: posthog
description: "PostHog operations: product analytics, HogQL queries, feature flags, session replays, annotations. CLI and MCP available. Use for all PostHog tasks."
---

# PostHog — Product Analytics

Core skill for PostHog via CLI (for SQL/HogQL) or MCP server (for full capabilities).

## Prerequisites

1. **CLI installed**: `posthog-cli --version`
   - Install: `npm install -g @posthog/cli`
2. **Authenticated**: `posthog-cli login`
   - Or env vars: `POSTHOG_CLI_HOST`, `POSTHOG_CLI_API_KEY`, `POSTHOG_CLI_PROJECT_ID`

## Claude Code — IMPORTANT

```bash
# WORKS: env vars inline
POSTHOG_CLI_HOST=https://app.posthog.com POSTHOG_CLI_API_KEY=phx_xxx POSTHOG_CLI_PROJECT_ID=12345 \
  posthog-cli query "SELECT count() FROM events"

# WORKS: if already logged in
posthog-cli query "SELECT count() FROM events WHERE event = 'pageview'"
```

## CLI Quick Reference

### HogQL Queries (SQL-like)
```bash
# Count events
posthog-cli query "SELECT count() FROM events WHERE timestamp >= now() - INTERVAL 7 DAY"

# Feature usage
posthog-cli query "
SELECT event, count() as total, uniq(distinct_id) as unique_users
FROM events
WHERE timestamp >= now() - INTERVAL 30 DAY
GROUP BY event ORDER BY total DESC LIMIT 20"

# Funnel
posthog-cli query "
SELECT
  countIf(event = 'step_1') as step1,
  countIf(event = 'step_2') as step2,
  countIf(event = 'step_3') as step3,
  round(countIf(event = 'step_3') / countIf(event = 'step_1') * 100, 2) as conversion_pct
FROM events
WHERE timestamp >= now() - INTERVAL 30 DAY"

# Retention (weekly cohorts)
posthog-cli query "
SELECT
  toStartOfWeek(first_seen) as cohort_week,
  count(DISTINCT user_id) as cohort_size
FROM (
  SELECT distinct_id as user_id, min(timestamp) as first_seen
  FROM events GROUP BY distinct_id
)
GROUP BY cohort_week ORDER BY cohort_week"

# User paths
posthog-cli query "
SELECT event, count() as freq FROM events
WHERE distinct_id = 'user-id-here'
AND timestamp >= now() - INTERVAL 7 DAY
ORDER BY timestamp"
```

## MCP Capabilities (when configured)
Via MCP, PostHog also provides:
- Create annotations
- Manage feature flags
- Error tracking queries
- Session replay metadata
- Project management

## REST API (for advanced use)
```bash
# Query via API
curl -X POST https://app.posthog.com/api/projects/PROJECT_ID/query/ \
  -H "Authorization: Bearer phx_xxx" \
  -H "Content-Type: application/json" \
  -d '{"query": {"kind": "HogQLQuery", "query": "SELECT count() FROM events"}}'

# List feature flags
curl https://app.posthog.com/api/projects/PROJECT_ID/feature_flags/ \
  -H "Authorization: Bearer phx_xxx"
```

## For Discovery Workflow
- Tag: `[Source: PostHog HogQL query, YYYY-MM-DD]`
- Use for: pain point validation, feature usage data, funnel analysis
- Session replays: reference by ID for qualitative evidence
- Feature flags: useful for Phase 2 experimentation planning
