---
name: tableau
description: "Tableau operations: export dashboards, download data, manage workbooks via tabcmd CLI. Use for all Tableau BI tasks."
---

# Tableau — BI & Visualization

Core skill for Tableau via `tabcmd` CLI (for exports) or MCP server (for exploration).

## Prerequisites

1. **tabcmd installed**: `tabcmd --version`
   - Install: `pip install tabcmd`
   - Requires Python 3.7+
2. **Logged in**: `tabcmd login -s SERVER -t SITE -u USER -p PASS`

## Claude Code — IMPORTANT

tabcmd requires a login session. Chain login with commands:

```bash
# WORKS: chained
tabcmd login -s https://tableau.company.com -t mysite -u user -p pass && \
  tabcmd export "Project/Workbook/View" --csv -f output.csv

# WORKS: session token file persists between runs
tabcmd login -s https://tableau.company.com -t mysite --token-name pat --token-value TOKEN
```

## Quick Reference

### Authentication
```bash
# Login with Personal Access Token (recommended)
tabcmd login -s https://server -t site --token-name PAT_NAME --token-value PAT_VALUE

# Login with username/password
tabcmd login -s https://server -t site -u username -p password
```

### Export Data
```bash
# Export view as CSV (data)
tabcmd export "Project/Workbook/ViewName" --csv -f data.csv

# Export view as PDF
tabcmd export "Project/Workbook/ViewName" --pdf -f report.pdf

# Export view as PNG image
tabcmd export "Project/Workbook/ViewName" --png -f dashboard.png

# Export full workbook as PDF
tabcmd export "Project/Workbook" --fullpdf --pagesize tabloid -f workbook.pdf

# Export with filter
tabcmd export "Project/Workbook/View?Region=West" --csv -f west_data.csv
```

### Download
```bash
# Download view data
tabcmd get "/views/workbook/view.csv" -f data.csv

# Download workbook
tabcmd get "/workbooks/workbook.twbx" -f workbook.twbx
```

### List Content
```bash
# List sites
tabcmd listsites

# Get URL for any view (use in browser or export)
# Format: /views/WorkbookName/ViewName
```

## MCP Capabilities (when configured)
Via MCP, Tableau also provides:
- Explore workbooks, views, data sources interactively
- Get data as structured JSON
- Download images of dashboards
- Search content
- Admin: list users, audit access, manage groups

## For Discovery Workflow
- Export dashboard data as CSV for quantitative analysis
- Export dashboard images for reports and presentations
- Tag: `[Source: Tableau dashboard "Name", YYYY-MM-DD]`
- Use for: baseline metrics, executive visualizations, KPI tracking
