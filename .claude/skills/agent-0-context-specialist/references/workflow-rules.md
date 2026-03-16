---
version: "2.2.0"
last_updated: "2025-10-16"
author: "Marcelus Fernandes"
template_type: "workflow_rules"
used_by: ["all agents"]
purpose: "Define workflow progression rules and file operation guidelines"
changelog:
  - "v2.2.0 (2025-10-16): Split Agent 2 into Agent 2A (Granularization) and Agent 2B (Clustering) with 2-phase pain point analysis structure"
  - "v2.1.0 (2025-10-16): Added note about critical template v2.0.0 updates (opportunity-identification and stakeholder-communication)"
  - "v2.0.0 (2025-10-15): Updated Solution Space structure for product/experience focus, updated sub-phase descriptions, added breakdown folder guidance"
  - "v1.0.0 (2025-09-02): Initial version"
---

# Product Development Workflow Rules

## 1. CONTEXT FIRST
- Always check `/0-documentation/broad-context.md` first
- All new concepts must be documented in `/0-documentation/`
- Reference materials go in `/0-documentation/0a-projectdocs/`

## 2. SEQUENTIAL PROGRESSION
### Main Phases
- Problem (1) → Solution (2) → Development (3)
- Never skip steps in the numerical sequence
- Higher numbers can reference lower, but not vice-versa

### Sub-Phase Progression
Each main phase follows an alphabetical progression (a→b→c→d→e) representing specific steps:

#### 0-documentation/
- 0a-projectdocs/: Project documentation and references

#### 1-problem/
- 1a-interview-analysis/: User interview analysis with experience focus
- 1b-painpoints/: Pain point analysis (2-phase process)
  - 1b0-granular/: Atomic pain point decomposition (Agent 2A output)
  - 1b1-painpoints-breakdown/: Clustered pain point analysis (Agent 2B output)
  - painpoint-mapping.md: Consolidated mapping (Agent 2B final output)
- 1c-asis-journey/: Current state journey mapping (with 1c2-asis-breakdown/)
- 1d-problem-output/: Final problem documentation (reports)

#### 2-solution/
- 2a-opportunities/: Product/service/experience opportunity identification (with 2a1-opportunities-breakdown/)
- 2b-tobe_journey/: Future experience journey design and improvements (with 2b1-journey-breakdown/)
- 2c-prioritization/: Solution concepts and feasibility assessment (with 2c1-concept-breakdown/)
- 2d-roadmap/: MVP scope, feature prioritization, and validation plan (with 2d1-mvp/ and 2d2-stage2/)
- 2e-solution-output/: Product communications and executive materials (with stakeholder-communications/)

#### 3-development/
- 3a-planning/: Development planning
- 3b-technical-specs/: Technical specifications
- 3c-implementation/: Implementation details
- 3d-development-output/: Development documentation

## 3. OUTPUT HANDLING
- Each major phase has an output folder (ends with `-output`)
- Outputs are immutable once finalized
- New iterations create new files, don't modify outputs
- **Breakdown folders:** Many sub-phases have breakdown folders (e.g., `1b1-`, `1c2-`, `2a1-`, `2b1-`, `2c1-`) for detailed individual analyses

## 4. DOCUMENT TYPES
- `*-template.md`: Base structure for new documents
- `*-list.md`: Enumeration of items
- `*-report.md`: Analysis and conclusions
- `*-export.md`: External system format (e.g., Jira)

## 5. TASK HIERARCHY
- Epics → User Stories → Tasks
- Always maintain this order
- Each level must reference its parent

## 6. FILE OPERATIONS
- New files follow existing naming patterns in their directory
- Templates must be used when available
- Related files stay in the same subfolder
- **Breakdown files:** Individual items go in breakdown folders (e.g., `{cluster-name}.md`, `{opportunity-name}.md`, `{concept-name}.md`)
- **Dynamic naming:** Use descriptive names with hyphens for multi-word names (e.g., `communication-gaps.md`, `dashboard-redesign.md`)

## 7. CROSS-REFERENCES
- Use relative paths for references
- Always reference the most recent output document
- Link to specific sections when possible

## 8. VERSION CONTROL
- Don't modify completed phase documents
- Create new versions in the next phase
- Keep change history in annotations.md

## 9. SEARCH PRIORITY
1. Check phase-specific output folder
2. Look in current phase main folder
3. Reference previous phase outputs
4. Consult documentation if needed

## 10. AUTOMATION RULES
- Templates guide document structure
- Follow folder letter sequence (a→b→c→d→e)
- Respect phase boundaries (0→1→2→3)
- **Agent sequence:** Phase 1 (Agents 0-6) → Phase 2 (Solution Agents 6-10)
- **Breakdown folders:** Create when multiple items need individual analysis
- **Naming consistency:** Use hyphen-case for all files and folders

## 11. PHASE FOCUS AREAS

### Phase 0: Documentation Setup
- **Purpose:** Project context and interview collection
- **Agents:** Agent 0
- **Output:** Broad context, project structure

### Phase 1: Problem Space (User Experience Assessment)
- **Purpose:** Understand current state, pain points, and user experience
- **Agents:** Agents 0-6 (where Agent 6 = Visual Journey Designer)
  - Agent 0: Product Service Specialist
  - Agent 1: Qualitative Research Specialist
  - Agent 2A: Pain Point Granularization Specialist (decomposition)
  - Agent 2B: Pain Point Clustering Specialist (pattern recognition)
  - Agent 3: As-Is Journey Mapper
  - Agent 4: Journey Consolidation Specialist
  - Agent 5: Strategic Report Generator
  - Agent 6: Visual Journey Designer
- **Focus:** User interviews, atomic pain point decomposition, relational clustering, As-Is journey, experience assessment, visual journey specs
- **Key Outputs:** Granular pain point catalog, clustered pain analyses, pain point mapping, journey documentation, problem reports, Figma Make-ready visualization

### Phase 2: Solution Space (Product & Experience Design)
- **Purpose:** Design future products/services and experience improvements
- **Agents:** Solution Agents 6-10 (distinct from Problem Space agents)
  - Solution Agent 6: Solution Ideation Specialist
  - Solution Agent 7: Experience Design Specialist
  - Solution Agent 8: Solution Concept Specialist
  - Solution Agent 9: Product Prioritization Specialist
  - Solution Agent 10: Product Communication Specialist
- **Focus:** Opportunities, future journey (To-Be), solution concepts, MVP prioritization, communications
- **Key Outputs:** Product concepts, MVP scope, roadmap, executive materials
- **NOT focused on:** Process automation or AI implementation (focus is product/experience)
- **Template Versions:** Critical templates updated to v2.0.0 (2025-10-16):
  - `opportunity-identification-template.md` v2.0.0 (product thinking, user value propositions)
  - `stakeholder-communication-template.md` v2.0.0 (ADKAR framework, comprehensive)

## 12. SPECIAL FOLDER STRUCTURES

### Breakdown Folders (for detailed analysis)
- **Pattern:** Parent folder has main consolidated file + breakdown subfolder(s)
- **Examples:**
  - `1b-painpoints/` has 2-phase structure:
    - `1b0-granular/` - Atomic pain point decomposition (Agent 2A)
    - `1b1-painpoints-breakdown/` - Clustered analyses (Agent 2B)
    - `painpoint-mapping.md` - Final consolidated mapping (Agent 2B)
  - `1c-asis-journey/` contains `asis-journey.md` + `1c2-asis-breakdown/`
  - `2a-opportunities/` contains main files + `2a1-opportunities-breakdown/`
  - `2b-tobe_journey/` contains main files + `2b1-journey-breakdown/`
  - `2c-prioritization/` contains main files + `2c1-concept-breakdown/`

### Stage Folders (for phased implementation)
- **Pattern:** Roadmap phase has MVP stages
- **Examples:**
  - `2d-roadmap/2d1-mvp/` - Core MVP features
  - `2d-roadmap/2d2-stage2/` - Post-MVP features

### Communication Folders (for different audiences)
- **Pattern:** Output phase has audience-specific subfolders
- **Examples:**
  - `2e-solution-output/stakeholder-communications/` - Multiple audience files
