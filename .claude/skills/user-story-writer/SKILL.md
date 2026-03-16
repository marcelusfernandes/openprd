---
name: user-story-writer
description: Transforms JTBD and solution concepts into detailed user stories with acceptance criteria (Given/When/Then), story points, and sprint-ready formatting for Jira.
---

# User Story Writer

## Purpose
Bridge the gap between solution design and sprint execution by generating detailed, implementation-ready user stories from JTBD mappings and solution concepts.

## Inputs
- `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` — Jobs to be done
- `/2-solution/2c-solution-concepts/solution-concepts.md` — Solution designs
- `/2-solution/2d-prioritization/mvp-scope.md` — MVP scope and priorities
- `/3-delivery/jira/initiative.md` — Jira structure (if exists)

## Workflow

### Step 1: Map JTBD → Epics → Stories
1. Read JTBD mapping and solution concepts
2. Group related JTBDs into Epics
3. Decompose each Epic into user stories (aim for 1-3 day stories)
4. Prioritize: MVP-critical → MVP-nice-to-have → Future

### Step 2: Write User Stories

For each story, generate:

```markdown
## [EPIC-ID] Story Title

**As a** [persona from discovery],
**I want to** [specific action],
**So that** [outcome linked to JTBD].

### Acceptance Criteria

**Scenario 1: [Happy path]**
- **Given** [precondition]
- **When** [action]
- **Then** [expected result]

**Scenario 2: [Edge case]**
- **Given** [precondition]
- **When** [action]
- **Then** [expected result]

**Scenario 3: [Error state]**
- **Given** [precondition]
- **When** [action]
- **Then** [expected result]

### Technical Notes
- [Implementation hints from solution concepts]
- [API dependencies]
- [Design dependencies]

### Story Points: [1/2/3/5/8]
### Priority: [Must/Should/Could]
### Labels: [mvp, backend, frontend, design, etc.]
### Dependencies: [Other story IDs]
### JTBD Reference: [Source JTBD ID]
```

### Step 3: Generate Sprint Suggestions
Group stories into suggested sprints:
- Sprint 1: Foundation + critical path
- Sprint 2: Core experience
- Sprint 3: Polish + edge cases

### Step 4: Output
Save to `/3-delivery/jira/user-stories/`:
- `epic-{name}.md` per epic (contains all stories for that epic)
- `sprint-plan.md` (suggested sprint groupings)
- `story-index.md` (quick reference of all stories with status)

## Story Sizing Guide
- **1 point**: Config change, copy update, simple UI tweak
- **2 points**: Single component, straightforward CRUD
- **3 points**: Multiple components, some logic, API integration
- **5 points**: Complex logic, multiple integrations, new patterns
- **8 points**: Should probably be split — flag for review

## Rules
- ALWAYS link stories back to JTBDs: `[JTBD: job-id]`
- ALWAYS include at least 2 acceptance criteria per story
- NEVER estimate above 8 points — split the story instead
- Tag assumptions: `[Assumption: needs refinement with engineering]`
- Include error/edge case scenarios, not just happy paths
- Mark design dependencies: `[Needs: design mockup for X]`
