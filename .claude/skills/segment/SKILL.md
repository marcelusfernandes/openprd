---
name: segment
description: Manages Twilio Segment CDP sources, destinations, tracking plans, and user profiles. Uses Public API and Profile API for customer data platform operations.
---

# Segment — Customer Data Platform

## Purpose
Integrate Twilio Segment CDP into the discovery pipeline to understand data flows, user tracking, and profile data. Essential for PMs who need to know what data is being collected and how users are tracked across platforms.

## Integration
- **Public API**: Manage sources, destinations, warehouses, tracking plans
- **Profile API**: Read user profiles, traits, events (requires Unify add-on)
- **Auth**: Bearer token from Segment workspace settings
- **SDKs**: Official SDKs in TypeScript, Python, Go
- **No MCP server available** — use API directly via Bash/scripts

## Public API Reference

### Authentication
```bash
curl -H "Authorization: Bearer SEGMENT_API_TOKEN" \
  https://api.segmentapis.com
```

### Sources
```bash
# List all sources
GET https://api.segmentapis.com/sources

# Get source by ID
GET https://api.segmentapis.com/sources/{sourceId}

# Create source
POST https://api.segmentapis.com/sources
{"name": "My App", "catalogId": "catalog_id", "settings": {}}
```

### Destinations
```bash
# List destinations for a source
GET https://api.segmentapis.com/destinations?sourceId={sourceId}

# Create destination
POST https://api.segmentapis.com/destinations
```

### Tracking Plans
```bash
# List tracking plans
GET https://api.segmentapis.com/tracking-plans

# Get tracking plan rules
GET https://api.segmentapis.com/tracking-plans/{trackingPlanId}/rules
```

### Warehouses
```bash
# List warehouses
GET https://api.segmentapis.com/warehouses
```

## Profile API Reference (Unify)

### User Profiles
```bash
# Get user traits
GET https://profiles.segment.com/v1/spaces/{spaceId}/collections/users/profiles/email:{email}/traits

# Get user events
GET https://profiles.segment.com/v1/spaces/{spaceId}/collections/users/profiles/email:{email}/events

# Get external IDs
GET https://profiles.segment.com/v1/spaces/{spaceId}/collections/users/profiles/email:{email}/external_ids
```

Auth: HTTP Basic with API token as username, empty password.

## Workflows

### Audit Data Collection
1. List all sources to understand what data flows exist
2. For each source, list connected destinations
3. Map the data flow: Source → Segment → Destinations
4. Identify gaps: what's tracked vs. what metrics need
5. Compare with tracking plan from `metric-definer` skill

### Tracking Plan Validation
After `metric-definer` generates KPIs and tracking plans:
1. Read existing tracking plans from Segment
2. Compare with required events from `/2-solution/2e-roadmap/success-metrics.md`
3. Identify missing events that need implementation
4. Generate tracking plan diff report

### User Profile Enrichment
For discovery research:
1. Query user profiles for specific segments
2. Extract behavioral traits (plan type, usage frequency, tenure)
3. Enrich persona definitions with real data
4. Feed into broad-context.md

### Data Flow Documentation
1. Map all sources → destinations
2. Document what events each source tracks
3. Identify data warehouse connections
4. Generate data architecture diagram (text-based)

## PM Query Patterns
- "What sources are connected to our Segment workspace?"
- "Show me all events in our tracking plan"
- "Which destinations receive our 'Purchase Completed' event?"
- "What traits do we have for user X?"
- "Are we tracking the events needed for our new KPIs?"
- "Map our data flow from app → analytics tools"

## Output Format
```
# Segment Data Architecture — [Workspace]
## Sources
## Destinations by Source
## Tracking Plan Coverage
## Data Flow Map
## Gap Analysis (vs. required metrics)
## Recommendations
## Sources & API References
```

## Rules
- ALWAYS cite: `[Source: Segment API, workspace={name}]`
- NEVER expose user PII from Profile API — anonymize in outputs
- Tag data flow findings: `[Segment data: {source_count} sources, {destination_count} destinations]`
- Mark assumptions: `[Assumption: requires Segment workspace access]`
- Note tier requirements: Public API needs Team/Business plan, Profile API needs Unify add-on
