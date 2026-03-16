---
name: intercom
description: Searches Intercom conversations and contacts to extract customer feedback, support patterns, and user sentiment. Uses official MCP server or REST API for conversation analysis.
---

# Intercom — Customer Conversations & Feedback Mining

## Purpose
Extract insights from Intercom conversations, contacts, and tickets to enrich the discovery pipeline with real customer communication data. Complements Zendesk for teams using Intercom as their primary support/messaging platform.

## Integration Options
1. **MCP Server** (recommended): Official Intercom MCP at `https://mcp.intercom.com/mcp` — configured in `.claude/.mcp.json`
2. **REST API**: `https://api.intercom.io` (v2.15)
3. **Node SDK**: `intercom-client` npm package
4. **Auth**: Bearer token from Intercom Developer Hub

## Capabilities via MCP
- Search conversations by keyword, status, date
- Search contacts by email, name, company
- Retrieve conversation details with full message history
- List conversation parts (messages, notes, actions)

## API Reference

### Authentication
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  https://api.intercom.io/conversations
```

### Key Endpoints
```bash
# Search conversations
POST /conversations/search
{
  "query": {
    "operator": "AND",
    "value": [
      {"field": "open", "operator": "=", "value": true},
      {"field": "updated_at", "operator": ">", "value": 1709251200}
    ]
  }
}

# Get conversation with messages
GET /conversations/{id}

# Search contacts
POST /contacts/search
{
  "query": {"field": "email", "operator": "=", "value": "user@example.com"}
}

# List companies
GET /companies

# Get contact's conversations
GET /contacts/{id}/conversations

# Tickets
GET /tickets
POST /tickets/search
```

## Workflows

### Customer Feedback Mining
1. Search conversations by topic keywords or tags
2. Extract customer messages (filter out bot/agent responses)
3. Categorize feedback themes
4. Identify sentiment patterns
5. Generate feedback report with direct quotes

### Conversation Pattern Analysis
1. Query conversations over time period
2. Analyze: first response time, resolution time, handoffs
3. Identify common conversation flows
4. Flag escalation patterns
5. Calculate customer effort score indicators

### User Journey Evidence
1. Pull conversations for specific user/company
2. Map conversation history to journey touchpoints
3. Identify friction points where users seek help
4. Cross-reference with as-is journey maps (Agent 3/4)

### Product Feedback Extraction
1. Search conversations mentioning specific features
2. Categorize: feature request, bug report, confusion, praise
3. Quantify demand signals per feature
4. Feed into opportunity identification (Agent S6)

### Feed Discovery Pipeline
1. Save findings to `/1-problem/1a-interview-analysis/intercom-conversations-{topic}.md`
2. Format as supplementary evidence
3. Cross-reference with interview pain points and Zendesk tickets

## PM Query Patterns
- "What are customers saying about the new dashboard?"
- "Show me conversations tagged 'feature-request' this month"
- "Find conversations where users mention pricing concerns"
- "What's the most common first message from users?"
- "How many conversations mention competitor features?"
- "Extract feedback about the onboarding experience"

## Output Format
```
# Intercom Analysis — [Topic]
## Summary
## Conversation Statistics
## Key Themes
## Customer Quotes (anonymized)
## Feature Request Frequency
## Sentiment Distribution
## Cross-reference with Pain Points
## Sources
```

## Rules
- ALWAYS cite: `[Source: Intercom conversation #{id}, {date}]`
- NEVER expose customer PII in outputs — anonymize all references
- Tag data: `[Intercom data: N={conversation_count}, period={date_range}]`
- Mark interpretations: `[AI analysis based on conversation data]`
- Note: MCP server currently US workspaces only
