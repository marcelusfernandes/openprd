---
name: notion-exporter
description: Exports discovery workflow outputs to Notion as structured pages. Alternative to Confluence for teams using Notion.
disable-model-invocation: true
---

# Notion Exporter

## Purpose
Export the complete discovery output to Notion as an organized workspace, as an alternative to Confluence delivery.

## Workflow

### Setup
1. Verify Notion MCP is configured
2. Ask user for target Notion workspace/database
3. Plan the page hierarchy (mirror /3-delivery/confluence/ structure)

### Export Structure
Create in Notion:
- 📁 Discovery Home (database page)
  - 📊 Problem Space
    - Interview Analyses
    - Pain Point Clusters
    - As-Is Journey
    - Strategic Reports
  - 💡 Solution Space
    - Opportunities
    - To-Be Journey
    - Solution Concepts
    - MVP Scope & Roadmap
    - Product Brief
  - 📋 Delivery
    - Jira Backlog Summary
    - Implementation Guide

### Content Conversion
- Markdown → Notion blocks
- Tables → Notion tables
- Headers → Notion headings with toggles for long sections
- Links → Notion page links (internal) or URLs (external)
- Tags ([Source:], [AI estimation]) → Notion callout blocks

### Execution
1. Read all output files from 1-problem/, 2-solution/, 3-delivery/
2. For each file, convert content and create Notion page
3. Establish parent-child relationships
4. Add navigation links between pages
5. Report: pages created, workspace URL

## Prerequisites
- Notion MCP configured (see _context/claude/mcp-setup.md)
- If not available: suggest manual import of markdown files
