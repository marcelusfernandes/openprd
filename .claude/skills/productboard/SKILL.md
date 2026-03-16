---
name: productboard
description: Manages Productboard features, notes, and components. Imports customer feedback, prioritizes features, and syncs with discovery outputs. Uses MCP server or REST API v2.
---

# Productboard — Feature Management & Customer Feedback

## Purpose
Integrate Productboard into the discovery pipeline to manage feature requests, import customer feedback, and align discovery outputs with product roadmap priorities.

## Integration Options
1. **MCP Server**: Community `productboard-mcp` (49+ tools) — configured in `.claude/.mcp.json`
2. **REST API**: v1 and v2 at `https://api.productboard.com`
3. **Auth**: API token (Bearer) from Productboard settings, or OAuth2

## MCP Capabilities
- CRUD operations on features, notes, components, products
- Custom field management
- Feature ranking and prioritization
- Note/feedback import

## API Reference

### Authentication
```bash
curl -H "Authorization: Bearer PB_API_TOKEN" \
  -H "Content-Type: application/json" \
  https://api.productboard.com/features
```

### Key Endpoints
```bash
# List features
GET /features?status=planned

# Create feature
POST /features
{"name": "New Onboarding", "description": "...", "status": {"id": "planned"}}

# List notes (customer feedback)
GET /notes

# Create note (import feedback)
POST /notes
{"title": "Customer feedback", "content": "...", "tags": ["discovery"]}

# List components
GET /components

# List products
GET /products
```

## Workflows

### Import Discovery Pain Points
After pain point analysis (Agent 2A/2B):
1. Read pain point clusters from `/1-problem/1b-painpoints/`
2. Create Productboard notes for each validated pain point
3. Tag with: `discovery`, severity, source interview
4. Link to relevant features or components

### Feature Request Aggregation
1. Pull all notes/feedback from Productboard
2. Cluster by theme using discovery pain point categories
3. Quantify demand: how many customers requested each feature
4. Cross-reference with JTBD mapping
5. Feed into prioritization (Agent S9)

### Roadmap Alignment
1. Pull current features and their status
2. Compare with MVP scope from `/2-solution/2d-prioritization/mvp-scope.md`
3. Identify: features in discovery not in Productboard (gaps)
4. Identify: features in Productboard not validated by discovery
5. Generate alignment report

### Feedback Loop
After shipping:
1. Import new customer feedback notes
2. Track feature adoption sentiment
3. Inform next discovery cycle

## PM Query Patterns
- "What are the most requested features in Productboard?"
- "Import our pain point clusters as Productboard notes"
- "Show me planned features for the 'Onboarding' component"
- "How many customer notes mention 'pricing'?"
- "Compare our MVP scope with what's already in the roadmap"

## Output Format
```
# Productboard Analysis — [Topic]
## Feature Summary
## Customer Demand by Theme
## Alignment with Discovery
## Gaps Identified
## Recommendations
## Sources
```

## Rules
- ALWAYS cite: `[Source: Productboard, feature/note ID={id}]`
- Tag imported data: `[Productboard data: N={count} features/notes]`
- NEVER delete or modify existing Productboard features without confirmation
- Mark AI suggestions: `[AI recommendation based on discovery data]`
