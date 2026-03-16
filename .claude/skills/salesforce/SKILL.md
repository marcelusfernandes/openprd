---
name: salesforce
description: Queries Salesforce CRM data via MCP server, CLI (sf), or SOQL API. Extracts customer insights, deal data, churn signals, and sales feedback to enrich product discovery.
---

# Salesforce — CRM Data & Customer Intelligence

## Purpose
Extract CRM data from Salesforce to enrich the discovery pipeline with customer intelligence: deal insights, churn reasons, customer segments, and sales team feedback.

## Integration Options
1. **MCP Server** (recommended): Official `@salesforce/mcp` — configured in `.claude/.mcp.json`
2. **CLI**: `sf` (Salesforce CLI v2) — SOQL queries, data operations, Apex execution
3. **REST API**: `https://{instance}.my.salesforce.com/services/data/v62.0/`
4. **Auth**: OAuth via `sf org login web` (CLI), then MCP uses same auth

## MCP Capabilities
- **orgs**: List and manage authorized orgs
- **data**: SOQL queries, record CRUD, bulk operations
- **metadata**: Deploy, retrieve, describe objects
- **users**: Manage users, permission sets

## CLI Reference (sf)

### Authentication
```bash
sf org login web --alias my-org        # Browser OAuth login
sf org list                             # List authorized orgs
sf org display --target-org my-org      # Show org details
```

### SOQL Queries
```bash
# Query accounts
sf data query -q "SELECT Id, Name, Industry, AnnualRevenue FROM Account WHERE Industry = 'Technology'" --json

# Query opportunities (deals)
sf data query -q "SELECT Name, StageName, Amount, CloseDate, Account.Name FROM Opportunity WHERE StageName = 'Closed Lost' AND CloseDate > LAST_N_MONTHS:3" --json

# Query cases (support tickets)
sf data query -q "SELECT Subject, Status, Priority, Reason FROM Case WHERE CreatedDate > LAST_N_MONTHS:1" --json

# Query contacts by account
sf data query -q "SELECT Name, Email, Title FROM Contact WHERE Account.Name = 'Acme Corp'" --json
```

### Data Operations
```bash
sf data get record -s Account -i 001XXXXXXXXXXXX --json     # Get single record
sf data create record -s Account -v "Name='New Corp'"       # Create record
sf data export tree -q "SELECT Name FROM Account" -d ./     # Export to JSON
```

## Workflows

### Customer Segmentation Analysis
1. Query Account data: industry, size, revenue, region
2. Query Opportunity data: win/loss rates by segment
3. Cross-reference with discovery personas
4. Identify underserved segments with high potential

### Churn Analysis
1. Query Closed Lost opportunities with loss reasons
2. Query churned accounts (custom fields)
3. Extract common churn themes
4. Cross-reference with pain points from interviews
5. Generate churn insight report

### Sales Feedback Mining
1. Query Opportunity notes and descriptions
2. Query Case/Support data for product-related issues
3. Extract feature requests mentioned in deals
4. Identify competitive displacement patterns
5. Feed insights into competitive-analyst skill

### Customer Health Dashboard
1. Query Account health scores (if available)
2. Aggregate: NPS, support tickets, renewal dates
3. Identify at-risk accounts
4. Generate customer health report

## PM Query Patterns
- "What are the top reasons for lost deals this quarter?"
- "Show me enterprise accounts in the Technology sector"
- "How many support cases are tagged 'product-bug' this month?"
- "What features do prospects most commonly ask about?"
- "Which accounts are up for renewal in the next 90 days?"
- "Compare win rates by industry segment"

## Output Format
Save to `/1-problem/1a-interview-analysis/salesforce-{topic}.md`:
```
# Salesforce Analysis — [Topic]
## Summary
## Data Overview (N records, period)
## Key Findings
## Segment Breakdown
## Cross-reference with Discovery
## Sources
```

## Rules
- ALWAYS cite: `[Source: Salesforce SOQL, {object}, N={count}, period={range}]`
- NEVER expose customer PII — anonymize account/contact names in outputs
- Tag aggregated metrics: `[Salesforce data: N={record_count}]`
- Mark interpretations: `[AI analysis based on CRM data]`
- Respect data access — only query objects the authenticated user can access
