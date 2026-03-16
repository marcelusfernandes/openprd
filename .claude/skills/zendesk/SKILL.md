---
name: zendesk
description: Queries Zendesk tickets, conversations, and Help Center articles to extract customer pain points and support patterns. Uses MCP server or REST API for ticket analysis and trend identification.
---

# Zendesk — Support Ticket Analysis & Pain Point Mining

## Purpose
Mine Zendesk support tickets and conversations to identify recurring customer problems, supplement discovery research with real support data, and track issue resolution patterns.

## Integration Options
1. **MCP Server**: Community `zendesk-mcp-server` — configured in `.claude/.mcp.json`
2. **REST API**: `https://{subdomain}.zendesk.com/api/v2`
3. **Auth**: Email/token basic auth or OAuth bearer token

## Capabilities via MCP
- Search and retrieve tickets by status, tags, assignee, date range
- Read ticket comments and conversation threads
- Search Help Center articles
- List ticket fields and custom fields

## API Reference

### Authentication
```bash
# Basic auth with API token
curl -u "email@company.com/token:API_TOKEN" \
  https://yourcompany.zendesk.com/api/v2/tickets.json

# OAuth
curl -H "Authorization: Bearer OAUTH_TOKEN" \
  https://yourcompany.zendesk.com/api/v2/tickets.json
```

### Key Endpoints
```bash
# Search tickets
GET /api/v2/search.json?query=type:ticket status:open tags:bug

# Get ticket with comments
GET /api/v2/tickets/{id}.json?include=comments

# List tickets by view
GET /api/v2/views/{view_id}/tickets.json

# Ticket metrics (first reply time, resolution time)
GET /api/v2/tickets/{id}/metrics.json

# Help Center articles
GET /api/v2/help_center/articles.json
```

## Workflows

### Pain Point Mining from Tickets
1. Query tickets by category/tags relevant to the product area
2. Extract recurring themes from ticket descriptions and comments
3. Categorize by severity (urgent/high/normal/low)
4. Calculate frequency and impact metrics
5. Cross-reference with interview-based pain points
6. Output enriched pain point analysis

### Support Trend Analysis
1. Query tickets over time period (last 30/60/90 days)
2. Group by category, tag, or custom field
3. Identify trending issues (increasing volume)
4. Calculate: avg resolution time, first response time, reopens
5. Flag issues that correlate with churn signals

### Voice of Customer Report
1. Pull recent tickets with specific tags or product areas
2. Extract direct customer quotes from ticket descriptions
3. Categorize sentiment (frustrated/neutral/positive)
4. Generate VOC report with quantitative backing
5. Merge with survey data from Hotjar/other sources

### Feed Discovery Pipeline
After mining tickets:
1. Save findings to `/1-problem/1a-interview-analysis/zendesk-tickets-{topic}.md`
2. Format as supplementary evidence for Agent 1 (research specialist)
3. Tag all data: `[Source: Zendesk ticket #{id}, {date}]`

## PM Query Patterns
- "What are the top 10 recurring issues this month?"
- "Show me tickets tagged 'onboarding' from last 30 days"
- "What's the average resolution time for billing issues?"
- "Find tickets where customers mention competitor X"
- "How many tickets were reopened this week?"
- "Extract customer quotes about the checkout flow"

## Output Format
```
# Zendesk Analysis — [Topic]
## Summary Statistics
## Top Recurring Issues (by frequency)
## Severity Distribution
## Customer Quotes
## Trend Analysis
## Cross-reference with Discovery Pain Points
## Sources
```

## Rules
- ALWAYS cite ticket IDs: `[Source: Zendesk #12345, 2026-03-01]`
- NEVER expose customer PII (names, emails) in outputs
- Anonymize quotes: "Customer A said..." not "John Smith said..."
- Tag aggregated metrics: `[Zendesk data: N={ticket_count}, period={date_range}]`
- Mark trend interpretations: `[AI analysis based on ticket data]`
