# MCP Server Setup Guide — Product Discovery Workflow

This document describes all MCP server integrations available for the Product Discovery Harness, how to configure them, and which workflow phases they support.

---

## Overview

| Server | Status | Transport | Primary Use |
|--------|--------|-----------|-------------|
| Figma | Pre-connected | Remote (claude.ai) | Design context, screenshots, design system rules |
| Miro | Pre-connected | Remote (claude.ai) | Journey maps, diagrams, collaborative boards |
| Google Calendar | Pre-connected | Remote (claude.ai) | Scheduling interviews, stakeholder meetings |
| Atlassian | Needs setup | Local (uvx) | Confluence docs + Jira backlog (Phase 3) |
| Slack | Needs setup | Local (npx) | Team notifications, sharing outputs |
| Notion | Needs setup | Local (npx) | Alternative documentation platform |
| Google Workspace | Needs setup | Local (npx) | Interview transcripts in Google Docs/Sheets |
| GitHub | Needs setup | Remote HTTP | Issue tracking, PR context |

---

## Pre-Connected Servers (No Setup Required)

These are already available through the claude.ai environment. No configuration needed.

### Figma
- **What it does**: Fetches design context, screenshots, component metadata, design system rules, and code connect mappings.
- **Workflow phases**: Phase 2 (Solution Space) — reference existing designs when defining To-Be journeys and MVP specs.

### Miro
- **What it does**: Creates and reads boards, diagrams, tables, and documents in Miro.
- **Workflow phases**: Phase 1 (As-Is Journey visualization), Phase 2 (To-Be Journey diagrams, opportunity mapping).

### Google Calendar
- **What it does**: Lists, creates, updates calendar events; finds free time and meeting slots.
- **Workflow phases**: Pre-Phase 1 — scheduling customer interviews and stakeholder review sessions.

---

## Servers Requiring Setup

These are configured in `.claude/.mcp.json` and require environment variables to be set.

### Atlassian (Confluence + Jira)

**Purpose**: Phase 3 delivery — publish Confluence documentation and create Jira backlog items.

**Environment variables**:
```
CONFLUENCE_URL=https://your-domain.atlassian.net/wiki
CONFLUENCE_USERNAME=your-email@company.com
CONFLUENCE_API_TOKEN=your-confluence-api-token
JIRA_URL=https://your-domain.atlassian.net
JIRA_USERNAME=your-email@company.com
JIRA_API_TOKEN=your-jira-api-token
```

**How to get tokens**: Go to https://id.atlassian.com/manage-profile/security/api-tokens and create an API token.

**Workflow phases**:
- Phase 3 (Agent 11 — Confluence Publisher): Publishes strategic reports, journey maps, and MVP specs as Confluence pages.
- Phase 3 (Agent 12 — Jira Backlog Creator): Creates epics, stories, and tasks from the roadmap and MVP definition.

---

### Slack

**Purpose**: Send notifications to team channels when workflow phases complete or when outputs need review.

**Environment variables**:
```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_TEAM_ID=T00000000
```

**How to get tokens**: Create a Slack app at https://api.slack.com/apps, install it to your workspace, and copy the Bot User OAuth Token. The Team ID is visible in your workspace settings.

**Workflow phases**:
- All phases — notify stakeholders when outputs are ready for review.
- Phase 2 — share opportunity scores and prioritization results with the product team.

---

### Notion

**Purpose**: Alternative to Confluence for teams that use Notion as their documentation platform.

**Environment variables**:
```
NOTION_TOKEN=ntn_your-integration-token
```

**How to get tokens**: Create an internal integration at https://www.notion.so/my-integrations, then share the relevant Notion pages/databases with the integration.

**Workflow phases**:
- Phase 3 — publish deliverables to Notion instead of (or in addition to) Confluence.
- Phase 1 — store interview notes and pain point analyses.

---

### Google Workspace (Docs/Sheets)

**Purpose**: Read interview transcripts from Google Docs, manage data in Google Sheets.

**Environment variables**:
```
GOOGLE_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret
```

**How to get credentials**: Create OAuth 2.0 credentials in the Google Cloud Console (https://console.cloud.google.com/apis/credentials). Enable the Google Docs and Google Sheets APIs.

**Workflow phases**:
- Pre-Phase 1 — pull interview transcripts directly from Google Docs into `0-documentation/0b-Interviews/`.
- Phase 1 — read supplementary data from Google Sheets (survey results, NPS scores).

---

### GitHub

**Purpose**: Richer repository context, issue tracking, and PR management beyond what `gh` CLI provides.

**Setup**: GitHub MCP uses remote HTTP transport, which is not configured via `.mcp.json`. Add it manually:

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
```

**Workflow phases**:
- Phase 3 — create GitHub issues from the roadmap if the team uses GitHub Projects instead of Jira.
- All phases — reference existing issues and PRs for technical context.

---

## Phase-to-Server Matrix

| Phase | Required | Optional |
|-------|----------|----------|
| **Pre-Phase 1** (Interviews) | — | Google Calendar, Google Workspace |
| **Phase 1** (Problem Space) | — | Miro, Notion, Google Workspace |
| **Phase 2** (Solution Space) | — | Figma, Miro |
| **Phase 3** (Delivery) | Atlassian OR Notion | Slack, GitHub |

---

## Configuration

All environment variables should be set in your shell profile (`~/.bashrc`, `~/.zshrc`) or in a `.env` file that your shell sources. Do not commit actual credentials to the repository.

Example `.env` file (add to `.gitignore`):

```bash
# Atlassian
export CONFLUENCE_URL=https://mycompany.atlassian.net/wiki
export CONFLUENCE_USERNAME=me@company.com
export CONFLUENCE_API_TOKEN=abc123
export JIRA_URL=https://mycompany.atlassian.net
export JIRA_USERNAME=me@company.com
export JIRA_API_TOKEN=abc123

# Slack
export SLACK_BOT_TOKEN=xoxb-xxx
export SLACK_TEAM_ID=T00000000

# Notion
export NOTION_TOKEN=ntn_xxx

# Google Workspace
export GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
export GOOGLE_CLIENT_SECRET=xxx
```

Then source it: `source .env`

---

## Analytics & Data Platforms

### Amplitude (Product Analytics)
- **Server:** `@amplitude/mcp-server`
- **Env vars:** `AMPLITUDE_API_KEY`, `AMPLITUDE_SECRET_KEY`
- **Get keys:** Amplitude → Settings → Projects → API Keys
- **Use for:** User behavior, funnels, cohorts, retention analysis

### Mixpanel (Event Analytics)
- **Server:** Remote MCP at `https://mcp.mixpanel.com/mcp`
- **Auth:** OAuth (browser sign-in on first use)
- **Use for:** Event analytics, funnels, session replays, retention

### PostHog (Product Analytics)
- **Server:** `posthog-mcp` (Python/uvx)
- **Env vars:** `POSTHOG_API_KEY`, `POSTHOG_PROJECT_ID`
- **Get keys:** PostHog → Settings → Personal API Keys
- **Use for:** Product analytics, feature flags, session replays, error tracking

### BigQuery (Data Warehouse)
- **Server:** `mcp-server-bigquery` (Python/uvx)
- **Env vars:** `BIGQUERY_PROJECT_ID`, `BIGQUERY_LOCATION`
- **Auth:** Google Cloud SDK (`gcloud auth application-default login`)
- **Use for:** SQL queries on large datasets, warehouse analytics

### Snowflake (Data Warehouse)
- **Server:** `mcp_snowflake_server` (Python/uvx)
- **Env vars:** `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_WAREHOUSE`, `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, `SNOWFLAKE_ROLE`, `SNOWFLAKE_DATABASE`, `SNOWFLAKE_SCHEMA`
- **Use for:** SQL queries, data warehouse exploration

### Metabase (BI / SQL)
- **Server:** `@cognitionai/metabase-mcp-server`
- **Env vars:** `METABASE_URL`, `METABASE_API_KEY`
- **Get key:** Metabase → Admin → API Keys
- **Use for:** SQL queries, dashboard data, database exploration

### Tableau (BI / Visualization)
- **Server:** `@tableau/mcp-server`
- **Env vars:** `TABLEAU_SERVER`, `TABLEAU_SITE_NAME`, `TABLEAU_PAT_NAME`, `TABLEAU_PAT_VALUE`
- **Get PAT:** Tableau → Account Settings → Personal Access Tokens
- **Use for:** Dashboard data, workbook exploration, data source downloads

### Redash (SQL / Dashboards)
- **Server:** `@suthio/redash-mcp`
- **Env vars:** `REDASH_URL`, `REDASH_API_KEY`
- **Get key:** Redash → Profile → API Key
- **Use for:** SQL queries, saved query execution, dashboard data

### Remote MCP Servers (add separately)
These use HTTP transport and must be added via CLI:
- **Databricks:** `claude mcp add --transport http databricks https://<workspace>.cloud.databricks.com/api/2.0/mcp/<catalog>/<schema>`
- **Pendo:** `claude mcp add --transport http pendo https://app.pendo.io/mcp/v0/shttp`
- **Looker:** Requires Google MCP Toolbox binary (see Google Cloud docs)

### Phase-to-Platform Matrix (updated)

| Platform | Phase 0 | Phase 1 | Phase 2 | Phase 3 |
|----------|---------|---------|---------|---------|
| Amplitude | Baseline metrics | Pain point validation | Opportunity sizing | Story metrics |
| Mixpanel | Usage overview | Funnel analysis | Feature prioritization | Acceptance criteria |
| PostHog | Feature flags | Session replays | A/B test planning | Feature rollout |
| BigQuery | Data overview | Usage queries | Impact estimation | KPI definitions |
| Snowflake | Data overview | Usage queries | Impact estimation | KPI definitions |
| Databricks | Catalog explore | AI analysis | Model insights | Data pipeline |
| Metabase | Dashboard review | Ad-hoc SQL | Dashboard creation | Monitoring setup |
| Tableau | Visual overview | Pain point data | Opportunity viz | Executive dashboards |
| Redash | Saved queries | Custom queries | Priority queries | Metric tracking |
| Pendo | In-app metrics | Feature usage | Guide planning | NPS tracking |
