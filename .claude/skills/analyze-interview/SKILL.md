---
name: analyze-interview
description: Quick analysis of a single interview file without running the full workflow. Extracts pain points, needs, and bright spots. Use when adding a new interview mid-workflow.
disable-model-invocation: true
---

# Quick Interview Analyzer

## Purpose
Analyze a single interview without running the full Agent 1 pipeline. Useful for:
- Quick preview before starting the workflow
- Adding a new interview after Phase 1 is complete
- Standalone analysis for stakeholder review

## Workflow
1. User specifies the interview file (in /0-documentation/0b-Interviews/)
2. Read the file completely
3. Extract:
   - User context (role, environment, usage patterns)
   - Pain points (with quotes, severity, frequency)
   - Bright spots (what works well)
   - Emotional journey highlights
   - Explicit and implicit needs
4. Output to /1-problem/1a-interview-analysis/{name}-analysis.md
5. Use the Agent 1 template from .claude/skills/agent-1-research-specialist/references/

## Key Rules
- EXHAUSTIVE extraction (include everything, don't filter)
- Always quote the source
- Mark inferences with [INFERRED] tag
- Follow guardrails (no invented data)
