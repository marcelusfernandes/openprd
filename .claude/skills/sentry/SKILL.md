---
name: sentry
description: Queries Sentry error tracking data to understand product health, identify recurring bugs, and correlate errors with user experience issues. Uses official MCP server or CLI.
---

# Sentry — Error Tracking & Product Health

## Purpose
Integrate Sentry error data into the discovery pipeline to understand product health, identify quality pain points, and correlate technical issues with user experience problems.

## Integration Options
1. **MCP Server** (recommended): Official remote MCP at `https://mcp.sentry.dev/mcp` — configured in `.claude/.mcp.json`
2. **CLI**: `sentry-cli` for releases, source maps, event management
3. **REST API**: `https://sentry.io/api/0/`
4. **Auth**: OAuth (MCP remote) or `SENTRY_AUTH_TOKEN` (CLI/API)

## MCP Capabilities
- List and retrieve issues/errors
- Get event details with full stacktraces
- Access project and organization data
- View Seer AI analysis results
- Query performance/trace data

## CLI Reference (sentry-cli)

### Authentication
```bash
export SENTRY_AUTH_TOKEN=your_token
export SENTRY_ORG=your-org
export SENTRY_PROJECT=your-project
```

### Issue Investigation
```bash
sentry-cli issues list                  # List recent issues
sentry-cli issues list --status unresolved --sort-by events  # Top unresolved by frequency
```

### Release Management
```bash
sentry-cli releases list                # List releases
sentry-cli releases new v1.2.3          # Create release
sentry-cli releases set-commits v1.2.3 --auto  # Associate commits
```

### Event Monitoring
```bash
sentry-cli send-event -m "Test event"   # Send test event
```

## API Reference

### Key Endpoints
```bash
# List project issues (sorted by frequency)
GET /api/0/projects/{org}/{project}/issues/?sort=freq&statsPeriod=30d

# Get issue details
GET /api/0/organizations/{org}/issues/{issue_id}/

# Get issue events (with stacktraces)
GET /api/0/organizations/{org}/issues/{issue_id}/events/

# Get latest event for an issue
GET /api/0/organizations/{org}/issues/{issue_id}/events/latest/

# Resolve/ignore an issue
PUT /api/0/organizations/{org}/issues/{issue_id}/
{"status": "resolved"}
```

## Workflows

### Product Health Assessment
1. Query top issues by frequency and user impact
2. Group by: error type, component, user segment
3. Calculate: error rate trends, affected user count
4. Identify patterns: which features are most error-prone
5. Generate product health report

### Error-to-Pain-Point Correlation
1. Pull top errors from Sentry
2. Map errors to user-facing features/flows
3. Cross-reference with interview pain points
4. Identify: are reported pain points also error-prone?
5. Enrich pain point analysis with technical evidence

### Release Quality Tracking
1. Compare error rates before/after releases
2. Identify regressions introduced by recent deploys
3. Track: new issues per release, resolution time
4. Feed into experiment guardrail metrics

### Bug Prioritization for PM
1. List unresolved issues sorted by user impact
2. Enrich with: frequency, affected users, first seen, last seen
3. Categorize: critical (data loss/security), high (broken flow), medium (degraded), low (cosmetic)
4. Generate prioritized bug backlog for sprint planning

## PM Query Patterns
- "What are the top 10 errors affecting users this week?"
- "Show me errors in the checkout flow"
- "How many users are affected by issue PROJ-123?"
- "Did the latest release introduce new errors?"
- "What's our overall error rate trend for the last 30 days?"
- "Which pages/components have the highest error rates?"

## Output Format
Save to `/1-problem/1a-interview-analysis/sentry-health-{topic}.md`:
```
# Product Health Analysis — [Topic/Period]
## Summary
## Error Statistics
## Top Issues by Impact
## Feature/Component Breakdown
## Trend Analysis
## Correlation with Pain Points
## Recommended Actions
## Sources
```

## Rules
- ALWAYS cite: `[Source: Sentry, project={name}, period={range}]`
- Tag error metrics: `[Sentry data: {issue_count} issues, {event_count} events]`
- NEVER include sensitive data from stacktraces (secrets, tokens, PII)
- Mark trend analysis: `[AI analysis based on error data]`
- Include both frequency AND user impact in prioritization
