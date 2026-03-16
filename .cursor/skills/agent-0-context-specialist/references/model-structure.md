---
version: "2.4.0"
last_updated: "2025-10-16"
author: "Marcelus Fernandes"
template_type: "directory_structure_model"
used_by: ["agent-0-product-service-specialist.md", "agent-workflow-orchestrator.mdc"]
purpose: "Define AI agent workflow directory structure and output conventions for Cursor AI"
changelog:
  - "v2.4.0 (2025-10-16): Split Agent 2 into Agent 2A (Granularization) and Agent 2B (Clustering) with 2-phase pain point analysis structure (1b0-granular/ + 1b1-painpoints-breakdown/)"
  - "v2.3.0 (2025-10-16): Added note about critical template v2.0.0 updates for Agent 6 and Agent 10"
  - "v2.2.0 (2025-10-15): Updated Solution Space for 5-agent workflow (6-10) with product/experience focus, added breakdown folders for each phase, updated file naming conventions"
  - "v2.1.0 (2025-10-15): Updated directory structure to match actual agent implementation (1-problem/, 2-solution/)"
---

# AI Agent Workflow Directory Structure

```
project-root/
├── 0-documentation/
│   ├── 0a-projectdocs/
│   │   ├── context.md
│   │   └── annotations.md
│   ├── 0b-Interviews/
│   │   ├── interview-1.md
│   │   ├── interview-2.md
│   │   └── ...
│   └── broad-context.md
│
├── 1-problem/
│   ├── 1a-interview-analysis/
│   │   ├── {name-or-area}-analysis.md
│   │   └── ...
│   ├── 1b-painpoints/
│   │   ├── 1b0-granular/
│   │   │   └── all-painpoints-granular.md
│   │   ├── 1b1-painpoints-breakdown/
│   │   │   ├── {cluster-name}.md
│   │   │   └── ...
│   │   └── painpoint-mapping.md
│   ├── 1c-asis-journey/
│   │   ├── 1c2-asis-breakdown/
│   │   │   ├── {source-name}-journey.md
│   │   │   └── ...
│   │   └── asis-journey.md
│   └── 1d-problem-output/
│       ├── problem-report.md
│       ├── pain-report.md
│       └── journey-output.md
│
├── 2-solution/
│   ├── 2a-opportunities/
│   │   ├── opportunities-identification.md
│   │   ├── prioritization-matrix.md
│   │   ├── strategic-roadmap.md
│   │   └── 2a1-opportunities-breakdown/
│   │       ├── {opportunity-name}.md
│   │       └── ...
│   ├── 2b-tobe_journey/
│   │   ├── consolidated-future-journey.md
│   │   ├── experience-improvements.md
│   │   └── 2b1-journey-breakdown/
│   │       ├── {stage-name}-future.md
│   │       └── ...
│   ├── 2c-prioritization/
│   │   ├── solution-concepts.md
│   │   ├── feasibility-assessment.md
│   │   └── 2c1-concept-breakdown/
│   │       ├── {concept-name}.md
│   │       └── ...
│   ├── 2d-roadmap/
│   │   ├── mvp-scope.md
│   │   ├── feature-prioritization.md
│   │   ├── validation-plan.md
│   │   ├── 2d1-mvp/
│   │   │   ├── {feature-name}.md
│   │   │   └── ...
│   │   └── 2d2-stage2/
│   │       ├── {feature-name}.md
│   │       └── ...
│   └── 2e-solution-output/
│       ├── product-brief.md
│       ├── product-roadmap.md
│       ├── experience-evolution.md
│       ├── executive-presentation.md
│       ├── success-metrics-dashboard.md
│       └── stakeholder-communications/
│           ├── {audience-name}.md
│           └── ...
```

## Agent Output Mapping

### Problem Space (Agents 0-6)
| Agent | Output Directory | Files Created |
|-------|------------------|---------------|
| **Agent 0** | `0-documentation/` | `broad-context.md` - Project context and initialization |
| **Agent 1** | `1-problem/1a-interview-analysis/` | `{name-or-area}-analysis.md` - Individual interview analyses |
| **Agent 2A** | `1-problem/1b-painpoints/1b0-granular/` | `all-painpoints-granular.md` - Atomic pain points (30-50) with TYPE classification |
| **Agent 2B** | `1-problem/1b-painpoints/` | Pain point clusters (4-6) in `1b1-painpoints-breakdown/` and `painpoint-mapping.md` |
| **Agent 3** | `1-problem/1c-asis-journey/` | Individual journeys in `1c2-asis-breakdown/{source-name}-journey.md` |
| **Agent 4** | `1-problem/1c-asis-journey/` | `asis-journey.md` - Consolidated journey |
| **Agent 5** | `1-problem/1d-problem-output/` | `problem-report.md`, `pain-report.md` |
| **Agent 6** | `1-problem/1d-problem-output/` | `journey-output.md` - Figma Make-ready visualization |

### Solution Space (Solution Agents 6-10)
**Note:** Solution Space agents are numbered 6-10 but are distinct from Problem Space agents. For clarity, refer to them as "Solution Agent 6", "Solution Agent 7", etc.

| Agent | Output Directory | Files Created |
|-------|------------------|---------------|
| **Solution Agent 6** (Solution Ideation) | `2-solution/2a-opportunities/` | `opportunities-identification.md`, `prioritization-matrix.md`, `strategic-roadmap.md` + breakdown files in `2a1-opportunities-breakdown/` |
| **Solution Agent 7** (Experience Design) | `2-solution/2b-tobe_journey/` | `consolidated-future-journey.md`, `experience-improvements.md` + breakdown files in `2b1-journey-breakdown/` |
| **Solution Agent 8** (Solution Concept) | `2-solution/2c-prioritization/` | `solution-concepts.md`, `feasibility-assessment.md` + breakdown files in `2c1-concept-breakdown/` |
| **Solution Agent 9** (Prioritization) | `2-solution/2d-roadmap/` | `mvp-scope.md`, `feature-prioritization.md`, `validation-plan.md` + feature files in `2d1-mvp/` and `2d2-stage2/` |
| **Solution Agent 10** (Communication) | `2-solution/2e-solution-output/` | `product-brief.md`, `product-roadmap.md`, `experience-evolution.md`, `executive-presentation.md`, `success-metrics-dashboard.md` + stakeholder files in `stakeholder-communications/` |

## File Naming Conventions

### Problem Analysis (Phase 1)
- **Context file:** `broad-context.md` (created by Agent 0)
- **Interview analyses:** `{name-or-area}-analysis.md` (created by Agent 1)
- **Granular pain points:** `all-painpoints-granular.md` in `1b0-granular/` (created by Agent 2A - 30-50 atomic pain points)
- **Pain point clusters:** `{cluster-name}.md` in `1b1-painpoints-breakdown/` (created by Agent 2B - 4-6 clusters)
- **Pain point mapping:** `painpoint-mapping.md` (created by Agent 2B)
- **Individual journeys:** `{source-name}-journey.md` in `1c2-asis-breakdown/` (created by Agent 3)
- **Consolidated journey:** `asis-journey.md` (created by Agent 4)
- **Final reports:** `problem-report.md`, `pain-report.md` (Agent 5), `journey-output.md` (Agent 6)

### Solution Design (Phase 2)
- **Opportunities (Agent 6):**
  - Main: `opportunities-identification.md` (Template v2.0.0 - Product Thinking), `prioritization-matrix.md`, `strategic-roadmap.md`
  - Breakdown: `{opportunity-name}.md` in `2a1-opportunities-breakdown/`
  - **Key Features:** User Value Propositions, Journey Stage mappings, User Benefits, Success Hypotheses
- **Future Experience (Agent 7):**
  - Main: `consolidated-future-journey.md`, `experience-improvements.md`
  - Breakdown: `{stage-name}-future.md` in `2b1-journey-breakdown/`
- **Solution Concepts (Agent 8):**
  - Main: `solution-concepts.md`, `feasibility-assessment.md`
  - Breakdown: `{concept-name}.md` in `2c1-concept-breakdown/`
- **Product Prioritization (Agent 9):**
  - Main: `mvp-scope.md`, `feature-prioritization.md`, `validation-plan.md`
  - MVP Features: `{feature-name}.md` in `2d1-mvp/`
  - Stage 2 Features: `{feature-name}.md` in `2d2-stage2/`
- **Product Communications (Agent 10):**
  - Main: `product-brief.md`, `product-roadmap.md`, `experience-evolution.md`, `executive-presentation.md`, `success-metrics-dashboard.md`
  - Stakeholders: `stakeholder-communications.md` (Template v2.0.0 - ADKAR Framework)
  - **Key Features:** Stakeholder Matrix, 5+ detailed groups, ADKAR Timeline, Messaging Strategy, Feedback Mechanisms

### General Rules
1. **Directories:** Use numeric prefix (0, 1, 2) followed by hyphen-case (e.g., `1-problem/`, `2a-opportunities/`)
2. **Files:** Use hyphen-case with .md extension
3. **Variables:** Use `{variable-name}` format for dynamic naming
4. **Consistency:** Follow template naming patterns from each skill's `references/` directory
5. **Subdirectories:** Use numeric/alphabetic codes (e.g., `1a`, `1b1`, `1c2`, `2a`, `2b`)

## Cursor AI Workflow Support

This structure enables:
1. **Agent Orchestration:** Clear input/output paths for each agent with numeric progression
2. **Template Integration:** Templates embedded in each skill's `references/` directory
3. **Sequential Processing:** 
   - Problem Space: Agents 0→1→2A→2B→3→4→(5+6 parallel)
   - Solution Space: Solution Agents 6→7→8→9→10
4. **Two-Phase Pain Point Analysis:**
   - Phase 1 (Agent 2A): Granularization - explode into 30-50 atomic pain points
   - Phase 2 (Agent 2B): Clustering - organize into 4-6 thematic clusters
5. **File Discovery:** Predictable locations for agent file consumption
6. **Output Organization:** Phase-based separation (`1-problem/` vs `2-solution/`)
7. **Local Efficiency:** Optimized for Cursor AI local file operations
8. **Numeric Convention:** Follows workflow rules with 0→1→2 phase progression and a→b→c→d→e sub-phase progression

## Directory Creation Rules

- **Auto-create:** Agents create directories as needed during execution
- **No pre-scaffolding:** Directories emerge from agent workflow execution
- **Template-driven:** Use templates from each skill's `references/` directory for file formats
- **Dynamic naming:** File names adapt based on actual content being processed
- **Numeric sequence:** Follow `workflow-rules.md` progression (0→1→2 for phases, a→b→c→d→e for sub-phases)
- **Subfolder codes:** Use alphanumeric codes (e.g., `1a`, `1b1`, `1c2`) for nested organization

## Key Structure Points

### Problem Space (Phase 1)
- **Main directory:** `1-problem/`
- **Sub-phases:** `1a` (interviews) → `1b` (pain points) → `1c` (journey) → `1d` (outputs)
- **Two-phase pain analysis:** `1b0-granular/` (Agent 2A atomic pain points) → `1b1-painpoints-breakdown/` (Agent 2B clusters)
- **Nested levels:** Some phases have breakdown folders (e.g., `1b0-granular/`, `1b1-painpoints-breakdown/`, `1c2-asis-breakdown/`)

### Solution Space (Phase 2)
- **Main directory:** `2-solution/`
- **Sub-phases:** `2a` (opportunities) → `2b` (future journey) → `2c` (solution concepts) → `2d` (roadmap & MVP) → `2e` (communications)
- **Breakdown folders:** Each phase has breakdown folders (e.g., `2a1-opportunities-breakdown/`, `2b1-journey-breakdown/`, `2c1-concept-breakdown/`)
- **MVP stages:** Roadmap phase has MVP stages (e.g., `2d1-mvp/`, `2d2-stage2/`)
- **Stakeholder comms:** Output phase has stakeholder subfolder (`stakeholder-communications/`)

### Documentation (Phase 0)
- **Main directory:** `0-documentation/`
- **Project docs:** `0a-projectdocs/` - Context and annotations
- **Source data:** `0b-Interviews/` - Raw interview files
- **Context file:** `broad-context.md` - Generated by Agent 0
