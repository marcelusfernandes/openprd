---
name: Move Templates Into Skills
overview: Move all 35 templates from the centralized `_output-structure/` directory into each skill's `references/` subdirectory, update all path references across SKILL.md files and other documents, then remove `_output-structure/`.
todos:
  - id: move-problem-templates
    content: Move 8 problem-space templates into their respective skill references/ directories
    status: completed
  - id: move-solution-templates
    content: Move 18 solution-space templates into their respective skill references/ directories
    status: completed
  - id: move-delivery-templates
    content: Move 5 delivery-space templates into agent-11 and agent-12 skill references/ + update their SKILL.md
    status: completed
  - id: move-utility-templates
    content: Move 4 orphan utility templates into guardrails-validator and solution-8 references/
    status: completed
  - id: update-skill-paths
    content: Update all 12+ SKILL.md files to use relative references/ paths instead of _output-structure/
    status: completed
  - id: update-project-refs
    content: Update broad-context.md, README.md, AGENTS.md, and workflow-rules.md references
    status: completed
  - id: cleanup
    content: Delete _output-structure/ directory and empty scripts/ dir in guardrails-validator
    status: completed
isProject: false
---

# Move Templates Into Skills references/

## Context

The analysis revealed that **zero templates are shared** between skills -- every template has a strict 1:1 relationship with one skill. This makes full encapsulation into skills the cleanest architecture. Currently all `references/` directories are empty and all template paths use absolute project-root format (`_output-structure/...`).

## Template Move Map

### Problem Space Skills (8 templates)

- `_output-structure/problem-space/model-structure.md` --> `.cursor/skills/agent-0-context-specialist/references/model-structure.md`
- `_output-structure/workflow-rules.md` --> `.cursor/skills/agent-0-context-specialist/references/workflow-rules.md`
- `_output-structure/problem-space/interview-analysis-template.md` --> `.cursor/skills/agent-1-research-specialist/references/interview-analysis-template.md`
- `_output-structure/problem-space/granular-painpoint-template.md` --> `.cursor/skills/agent-2a-granular-specialist/references/granular-painpoint-template.md`
- `_output-structure/problem-space/pain-point-analysis-template.md` --> `.cursor/skills/agent-2b-clustering-specialist/references/pain-point-analysis-template.md`
- `_output-structure/problem-space/journey-mapping-template.md` --> `.cursor/skills/agent-3-journey-mapper/references/journey-mapping-template.md`
- `_output-structure/problem-space/report-template.md` --> `.cursor/skills/agent-5-report-generator/references/report-template.md`
- `_output-structure/problem-space/journey-visualization-template.md` --> `.cursor/skills/agent-6-visual-designer/references/journey-visualization-template.md`

### Solution Space Skills (18 templates)

- `solution-6-ideation`: opportunity-identification-template, opportunity-breakdown-template, prioritization-matrix-template, strategic-roadmap-template (4 files)
- `solution-7-experience`: future-journey-template, future-journey-breakdown-template, experience-improvements-template (3 files)
- `solution-8-concept`: solution-concept-template, concept-breakdown-template, feasibility-assessment-template (3 files)
- `solution-9-prioritization`: mvp-scope-template, feature-prioritization-template, validation-plan-template (3 files)
- `solution-10-communication`: product-brief-template, product-roadmap-template, stakeholder-communication-template, executive-presentation-template, experience-evolution-template (5 files)

### Delivery Space Skills (5 unreferenced templates -- need adding)

- `delivery-space/confluence-page-template.md` --> `.cursor/skills/agent-11-confluence/references/confluence-page-template.md`
- `delivery-space/import-guide-template.md` --> `.cursor/skills/agent-11-confluence/references/import-guide-template.md`
- `delivery-space/jira-initiative-template.md` --> `.cursor/skills/agent-12-jira/references/jira-initiative-template.md`
- `delivery-space/jira-epic-template.md` --> `.cursor/skills/agent-12-jira/references/jira-epic-template.md`
- `delivery-space/jira-story-template.md` --> `.cursor/skills/agent-12-jira/references/jira-story-template.md`

Agent 11 and 12 SKILL.md files will be updated to reference these templates.

### Utility Templates (4 orphans)

- `solution-space/template-prd.md` --> `.cursor/skills/solution-8-concept/references/template-prd.md` (closest match)
- `solution-space/conservative-estimation-guide.md` --> `.cursor/skills/guardrails-validator/references/conservative-estimation-guide.md`
- `solution-space/guardrail-validation-checklist.md` --> `.cursor/skills/guardrails-validator/references/guardrail-validation-checklist.md`
- `template-quality-assessment.md` --> `.cursor/skills/guardrails-validator/references/template-quality-assessment.md`

## Path Updates Required

### SKILL.md files (12 files)

Update all `_output-structure/...` references to relative `references/...` paths. Example:

```
# Before
Use template: `_output-structure/problem-space/interview-analysis-template.md`

# After
Use template: [references/interview-analysis-template.md](references/interview-analysis-template.md)
```

### Non-skill files (4 files)

- [broad-context.md](0-documentation/broad-context.md) -- lines 86, 151-152: update references to point to skills or remove `_output-structure` mention
- [README.md](README.md) -- update architecture description (remove `_output-structure/` from directory tree, mention templates live inside skills)
- [AGENTS.md](AGENTS.md) -- update "Templates" reference
- [model-structure.md](_output-structure/problem-space/model-structure.md) -- self-references (will move to skill, internal refs updated)

### Files to leave as-is

- `.cursor/rules/problem-space/README.md`, `.cursor/rules/solution-space/README.md`, `.cursor/rules/delivery-space/README.md` -- legacy informational files, not part of active system
- `.cursor/plans/modernize_agent_system_cc6fbfe3.plan.md` -- never edit

## Cleanup

After all moves and updates:

- Delete the entire `_output-structure/` directory
- Remove the empty `.cursor/skills/guardrails-validator/scripts/` directory (script lives at `.cursor/scripts/`)

