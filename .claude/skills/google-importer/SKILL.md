---
name: google-importer
description: Imports interview transcripts and project documents from Google Docs/Sheets into the documentation folder. Use when the user wants to pull interviews from Google Drive.
disable-model-invocation: true
---

# Google Docs/Sheets Importer

## Purpose
Import interview transcripts and project documents from Google Workspace into the local documentation structure.

## Workflow

### Import Interviews
1. User provides Google Doc URL(s) or folder
2. Use Google Workspace MCP to read document content
3. Convert to markdown format
4. Save to `/0-documentation/0b-Interviews/{doc-name}.md`
5. Preserve original formatting as much as possible

### Import Project Docs
1. User provides Google Doc/Sheet URL(s)
2. Read content via MCP
3. Save to `/0-documentation/0a-projectdocs/{doc-name}.md`
4. For Sheets: convert to markdown tables

### Import Survey Data
1. User provides Google Sheets URL
2. Read via MCP
3. Convert to structured markdown
4. Save to `/0-documentation/0a-projectdocs/survey-data.md`

## Prerequisites
- Google Workspace MCP configured (see _context/claude/mcp-setup.md)
- User must provide document URLs or shared folder link

## Error Handling
- If MCP not configured: provide instructions for manual export
- If document not accessible: request sharing permissions
