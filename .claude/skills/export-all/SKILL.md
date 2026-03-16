---
name: export-all
description: Export discovery outputs to all configured platforms at once (Confluence, Jira, Notion, Miro, Figma, Slack). One-click publish.
disable-model-invocation: true
---

# Export All — One-Click Publish

## Purpose
Publish all discovery outputs to every configured external platform in a single operation.

## Workflow

1. **Detect available integrations**
   Check which MCP servers are connected:
   - Atlassian (Confluence + Jira)
   - Notion
   - Miro
   - Figma
   - Slack

2. **For each available platform, spawn a subagent:**
   - `confluence-publisher` agent → Confluence pages
   - `jira-publisher` agent → Jira Initiative/Epics/Stories
   - `notion-exporter` skill → Notion workspace
   - `miro-publisher` agent → Miro boards
   - `figma-publisher` agent → Figma visualizations
   - `slack-notifier` skill → Notification of completion

3. **Run in parallel** where possible (Confluence + Jira can run together, Miro + Figma together)

4. **Consolidate report:**
   Show for each platform: ✅ Published / ⚠️ Partially / ❌ Not available
   Include URLs for each published resource

## Prerequisites
- At least one MCP integration configured
- Phase 3 outputs complete (/3-delivery/ populated)
- For partial export: relevant phase outputs must exist

## Error Handling
- Skip unavailable platforms silently
- Report at the end which platforms succeeded/failed
- Suggest manual alternatives for failed platforms
