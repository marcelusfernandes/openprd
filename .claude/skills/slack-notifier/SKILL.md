---
name: slack-notifier
description: Sends workflow status updates and deliverable notifications to Slack channels. Use after completing phases or when sharing results with the team.
user-invocable: false
---

# Slack Notifier

## Purpose
Send structured notifications to Slack when workflow milestones are reached.

## When to Use
- After completing any phase (1, 2, or 3)
- When sharing a specific deliverable with stakeholders
- When the workflow encounters a blocking error

## Notification Templates

### Phase Complete
Channel: project channel
Message format:
📊 **Discovery Workflow — Phase {N} Complete**
> {phase_name}: {summary}
> 📄 Key deliverables: {list}
> ⏭️ Next: {what_comes_next}

### Deliverable Ready
Channel: project channel
Message format:
📋 **{deliverable_name}** is ready for review
> {one_line_summary}
> Files: {file_list}

### Error/Block
Channel: project channel
Message format:
⚠️ **Workflow Blocked** at Agent {N}
> Reason: {error}
> Action needed: {what_to_do}

## Prerequisites
- Slack MCP server configured (see _context/claude/mcp-setup.md)
- If not available, skip silently (notifications are optional)

## Execution
1. Determine notification type based on context
2. Format the message using templates above
3. Send via Slack MCP tools
4. Log the notification in the build log
