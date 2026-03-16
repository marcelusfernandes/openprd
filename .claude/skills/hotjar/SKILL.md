---
name: hotjar
description: Queries Hotjar survey responses, feedback, recordings, and heatmaps. Uses Zapier MCP via mcp2cli for full access, or REST API for direct survey data. Enriches discovery with quantitative user sentiment.
---

# Hotjar — Survey Responses & User Feedback

## Purpose
Extract survey and feedback data from Hotjar to enrich the discovery pipeline with quantitative user sentiment. Complements interview-based qualitative research.

## Integration Options

### Option 1: Zapier MCP → mcp2cli (recommended for full access)
Zapier MCP exposes Hotjar actions (surveys, recordings, feedback, heatmaps) as MCP tools.
`mcp2cli` converts those tools into CLI commands — no AI client required.

**Setup:**
```bash
# Install mcp2cli
pip install mcp2cli

# Option A: Remote Zapier MCP (requires setup at mcp.zapier.com)
mcp2cli --mcp-sse "https://mcp.zapier.com/${ZAPIER_MCP_SERVER_ID}" --list

# Option B: Local Zapier SDK MCP (stdio)
mcp2cli --mcp-stdio "npx @zapier/zapier-sdk-mcp" --list

# Example: get survey responses
mcp2cli --mcp-sse "https://mcp.zapier.com/${ZAPIER_MCP_SERVER_ID}" hotjar-list-survey-responses --survey-id 12345
```

**Zapier MCP Setup (one-time):**
1. Go to [mcp.zapier.com](https://mcp.zapier.com)
2. Create MCP Server → Add Hotjar actions
3. Available triggers: New Survey Response, New Feedback, New Recording, New Heatmap
4. Get server URL + API key
5. Set env: `ZAPIER_MCP_SERVER_ID`, `ZAPIER_API_KEY`

### Option 2: Hotjar REST API (direct, limited)
- **API**: Hotjar REST API v1
- **Auth**: OAuth client credentials (client_id + client_secret from Hotjar app settings)
- **Plan requirement**: Ask Scale plan for Responses API
- **Limitation**: Only surveys and user lookup — no heatmaps/recordings

## API Capabilities

### Available
- **Survey Responses API**: Export survey/feedback responses with pagination
- **User Lookup API**: Find user data by identifier (GDPR compliance)
- **Webhooks**: Automated notifications on new responses

### NOT Available via REST API (use Zapier MCP instead)
- Heatmap data → available via Zapier MCP
- Session recordings → available via Zapier MCP
- Funnel analysis
- Form analytics

## API Reference

### Authentication
```bash
# Get access token
curl -X POST https://api.hotjar.com/v1/oauth/token \
  -d "grant_type=client_credentials" \
  -d "client_id=${HOTJAR_CLIENT_ID}" \
  -d "client_secret=${HOTJAR_CLIENT_SECRET}"
```

### Survey Responses
```bash
# List surveys
curl -H "Authorization: Bearer TOKEN" \
  https://api.hotjar.com/v1/sites/{site_id}/surveys

# Get responses (paginated)
curl -H "Authorization: Bearer TOKEN" \
  "https://api.hotjar.com/v1/sites/{site_id}/surveys/{survey_id}/responses?limit=100&cursor=CURSOR"
```

### User Lookup
```bash
# Find user by identifier
curl -H "Authorization: Bearer TOKEN" \
  "https://api.hotjar.com/v1/sites/{site_id}/users?identifier=user@email.com"
```

## Workflows

### Feed Discovery with Survey Data
1. Export survey responses for relevant surveys
2. Aggregate sentiment scores and common themes
3. Enrich pain point analysis with quantitative backing
4. Add to `/1-problem/` as supplementary evidence

### Survey Response Analysis
1. Pull all responses for a survey
2. Categorize open-text responses by theme
3. Calculate NPS/CSAT scores
4. Generate summary report with key insights
5. Cross-reference with interview pain points

### User Sentiment Tracking
1. Query responses over time periods
2. Track sentiment trends
3. Identify response spikes (positive or negative)
4. Correlate with product changes

## PM Query Patterns
- "Export all responses from our onboarding survey"
- "What's the average NPS score from last month?"
- "Show me negative feedback themes from the checkout survey"
- "How many survey responses did we get this week?"

## Output Format
Save analysis to `/1-problem/1a-interview-analysis/hotjar-survey-{name}.md`:
```
# Hotjar Survey Analysis — [Survey Name]
## Summary
## Response Statistics
## Key Themes
## Sentiment Distribution
## Notable Quotes
## Cross-reference with Pain Points
## Sources
```

## Rules
- ALWAYS cite: `[Source: Hotjar survey "{name}", {date_range}]`
- Tag aggregated metrics: `[Hotjar data: N={sample_size}]`
- Note API limitations: heatmaps/recordings via Zapier MCP or manual Hotjar dashboard
- Mark trend interpretations: `[AI interpretation based on response data]`

## mcp2cli Reference
`mcp2cli` converts any MCP server into CLI commands at runtime (zero codegen).
- **Install**: `pip install mcp2cli`
- **GitHub**: [knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli)
- **Usage**: `mcp2cli --mcp-sse "URL" --list` to discover tools, then call by name
- **Benefit**: 96-99% fewer tokens than native MCP tool injection
- **Can be used with ANY MCP server**, not just Hotjar/Zapier
