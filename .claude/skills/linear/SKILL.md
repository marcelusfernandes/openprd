---
name: linear
description: Manages Linear issues, projects, and cycles. Creates issues, updates status, queries backlogs, and syncs with product discovery outputs. Uses Linear MCP server or GraphQL API.
---

# Linear — Issue Tracking & Project Management

## Purpose
Integrate Linear into the product discovery pipeline for issue tracking, backlog management, and sprint planning. Alternative/complement to Jira for modern product teams.

## Integration Options
1. **MCP Server** (recommended): Official Linear remote MCP at `https://mcp.linear.app/sse` — configured in `.claude/.mcp.json`
2. **GraphQL API**: Via `@linear/sdk` npm package
3. **CLI**: `@linear/cli` for basic operations (create issue, checkout branch)

## Capabilities via MCP
- Find issues by ID, title, assignee, status, label
- Create new issues with title, description, priority, labels
- Update issue status, assignee, priority
- List projects and their issues
- Add comments to issues

## Workflows

### Query Backlog
```
Find all issues in project "Discovery" with label "pain-point"
List issues assigned to me in current cycle
Show all high-priority bugs in "Product" team
```

### Create Issues from Discovery
After running the discovery pipeline, create Linear issues from:
- Pain point clusters → Epics
- JTBD → Features/Stories
- MVP scope items → Tasks with priority

### Sync with User Stories
When `user-story-writer` skill generates stories:
1. Read stories from `/3-delivery/jira/user-stories/`
2. Create corresponding Linear issues
3. Set labels: `discovery`, `mvp`, priority level
4. Link related issues

### Sprint Planning Support
- Query current cycle issues and progress
- Create new cycle with selected issues
- Move issues between cycles
- Generate sprint status reports

## PM Query Patterns

### Status Checks
- "What's the status of the discovery epic?"
- "Show me all blocked issues"
- "How many story points are in the current cycle?"

### Triage
- "Create a bug for [description] with high priority"
- "Move issue LIN-123 to In Progress"
- "Assign all unassigned design tasks to @designer"

### Reporting
- "Summarize cycle velocity for last 3 cycles"
- "List all issues completed this week"
- "Show dependency graph for the MVP epic"

## Output Integration
- Issues created are logged in `/3-delivery/linear/` (if used instead of Jira)
- Cross-reference format: `[Linear: TEAM-123]`

## Rules
- ALWAYS verify issue doesn't exist before creating duplicates
- Tag AI-created issues with label `ai-generated`
- Include `[Source: discovery-file.md]` in issue descriptions
- Never delete or close issues without confirmation
