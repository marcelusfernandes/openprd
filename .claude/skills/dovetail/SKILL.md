---
name: dovetail
description: Manages Dovetail research repository — projects, notes, insights, and highlights. Imports interview analysis, creates insights, and maintains a centralized research knowledge base. Uses official MCP server.
---

# Dovetail — Research Repository & Insights

## Purpose
Integrate Dovetail as the centralized research repository for the discovery pipeline. Push interview analyses, pain points, and insights from the discovery workflow into Dovetail for team-wide access and long-term knowledge management.

## Integration Options
1. **MCP Server** (recommended): Official `@dovetail/mcp` — configured in `.claude/.mcp.json`
2. **REST API**: Documented at developers.dovetail.com
3. **Auth**: Personal API token from Dovetail settings
4. **Requirement**: Node.js 22+

## MCP Capabilities
- Find, create, and update projects
- Manage notes within projects
- Create and update insights
- Search across research data

## API Reference

### Authentication
```bash
curl -H "Authorization: Bearer DOVETAIL_API_TOKEN" \
  -H "Content-Type: application/json" \
  https://dovetail.com/api/v1/projects
```

### Key Operations
```bash
# List projects
GET /api/v1/projects

# Create project
POST /api/v1/projects
{"title": "Product Discovery — Q1 2026"}

# Create note in project
POST /api/v1/projects/{projectId}/notes
{"title": "Interview Analysis — User A", "content": "..."}

# Create insight
POST /api/v1/insights
{"title": "Key Finding", "description": "..."}
```

## Workflows

### Push Discovery to Dovetail
After each discovery phase:
1. Create a Dovetail project for the discovery cycle
2. Import interview analyses from `/1-problem/1a-interview-analysis/`
3. Create highlights from key quotes
4. Create insights from pain point clusters
5. Tag everything with phase, source, severity

### Research Repository Sync
1. Read existing Dovetail projects and insights
2. Cross-reference with current discovery outputs
3. Identify: prior research that validates/contradicts current findings
4. Build cumulative knowledge base across discovery cycles

### Insight Extraction
1. Pull existing notes and highlights from Dovetail
2. Cluster by theme
3. Generate insight summaries
4. Push back synthesized insights to Dovetail

### Team Collaboration
1. Create project with all discovery outputs
2. Structure: one note per interview, one insight per pain cluster
3. Enable team members to add their own highlights and tags
4. Maintain living research repository

## PM Query Patterns
- "Push all interview analyses to Dovetail"
- "Create a Dovetail project for this discovery cycle"
- "What existing research do we have about onboarding?"
- "Create insights from our pain point clusters"
- "Show me all insights tagged 'churn'"

## Output Format
```
# Dovetail Sync Report — [Discovery Cycle]
## Project Created
## Notes Imported
## Insights Created
## Tags Applied
## Cross-references Found
```

## Rules
- ALWAYS cite origin: `[Imported from: filename.md]` in Dovetail notes
- Tag all imported content: `discovery`, `ai-generated`, cycle name
- NEVER overwrite existing Dovetail insights — create new versions
- Mark AI-generated insights: prefix with "[AI Insight]"
