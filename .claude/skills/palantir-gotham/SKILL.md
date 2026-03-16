---
name: palantir-gotham
description: Queries Palantir Gotham objects, graphs, and geotemporal data via REST API and Python SDK. No MCP available — uses custom scripts with gotham-platform-sdk for data extraction and analysis.
---

# Palantir Gotham — Intelligence & Graph Analysis

## Purpose
Integrate Palantir Gotham into the discovery pipeline for entity analysis, graph exploration, and geotemporal data. Gotham specializes in intelligence-grade data integration and relationship analysis.

## Integration
- **No MCP server available** — custom scripts required
- **Python SDK**: `gotham-platform-sdk` (official, on PyPI)
- **TypeScript SDK**: `@osdk/gotham` (official, on npm)
- **REST API**: OAuth2-authenticated at `https://{instance}/gotham/api/`
- **Custom scripts**: `_tools/gotham/` directory

## Setup

### Install SDK
```bash
# Project-scoped installation
pip install gotham-platform-sdk --target=./_tools/gotham/lib
# or
pip install gotham-platform-sdk
```

### Authentication
```python
from gotham.client import GothamClient

client = GothamClient(
    auth=ConfidentialClientAuth(
        client_id=os.environ["GOTHAM_CLIENT_ID"],
        client_secret=os.environ["GOTHAM_CLIENT_SECRET"],
        hostname=os.environ["GOTHAM_HOSTNAME"],
    ),
    hostname=os.environ["GOTHAM_HOSTNAME"],
)
```

Environment variables:
- `GOTHAM_HOSTNAME` — Gotham instance URL
- `GOTHAM_CLIENT_ID` — OAuth2 client ID
- `GOTHAM_CLIENT_SECRET` — OAuth2 client secret

## Custom Scripts

### `_tools/gotham/query_objects.py`
Query Gotham objects by type and filters.

### `_tools/gotham/search_graph.py`
Explore entity relationships in the graph.

### `_tools/gotham/export_data.py`
Export object data for analysis in the discovery pipeline.

## API Reference

### Authentication (OAuth2)
```bash
# Client Credentials grant
curl -X POST https://{hostname}/multipass/api/oauth2/token \
  -d "grant_type=client_credentials" \
  -d "client_id=${GOTHAM_CLIENT_ID}" \
  -d "client_secret=${GOTHAM_CLIENT_SECRET}"
```

### Key Endpoints
```bash
# Search objects
POST /gotham/api/graph/v1/objects/search
{"query": "...", "objectTypes": ["customer"], "limit": 100}

# Get object by RID
GET /gotham/api/graph/v1/objects/{rid}

# Get object relationships
GET /gotham/api/graph/v1/objects/{rid}/links

# Geotemporal query
POST /gotham/api/geotemporal/v1/query
{"bounds": {...}, "timeRange": {...}, "objectTypes": [...]}
```

## Workflows

### Entity Analysis for Discovery
1. Search Gotham for customer/user entities
2. Explore relationship graphs between entities
3. Identify patterns: customer segments, interaction networks
4. Extract entity attributes for persona enrichment

### Graph-Based Pain Point Mining
1. Query entity relationships around problem domains
2. Map interaction flows between systems/users
3. Identify bottlenecks in process graphs
4. Quantify relationship density (strong vs weak connections)

### Geotemporal Analysis
For location-based products:
1. Query geotemporal data for user activity patterns
2. Analyze geographic distribution of issues/usage
3. Identify regional variations in behavior
4. Feed into journey mapping with location context

### Data Export for Discovery
1. Export relevant object data from Gotham
2. Transform into discovery-compatible format
3. Save to `/1-problem/1a-interview-analysis/gotham-{topic}.md`
4. Cross-reference with interview findings

## PM Query Patterns
- "Search Gotham for customer entities in the healthcare segment"
- "Show me the relationship graph for entity X"
- "Export user interaction data for the last quarter"
- "What entities are connected to the onboarding process?"
- "Query geotemporal activity data for the São Paulo region"

## Output Format
```
# Gotham Analysis — [Topic]
## Entity Summary
## Relationship Graph (text representation)
## Key Patterns
## Data Extracts
## Cross-reference with Discovery
## Sources
```

## Rules
- ALWAYS cite: `[Source: Gotham, object_type={type}, query_date={date}]`
- NEVER expose classified or sensitive entity data in outputs
- Anonymize entity identifiers in all discovery documents
- Tag data: `[Gotham data: N={object_count}, types={list}]`
- Mark graph interpretations: `[AI analysis based on graph data]`
- All Gotham API calls require valid OAuth2 tokens — never hardcode credentials
