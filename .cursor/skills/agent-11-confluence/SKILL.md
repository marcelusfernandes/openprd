---
name: agent-11-confluence
description: Structures and formats all project documentation for Confluence with navigable hierarchy, macros, and import guide. Use when creating Confluence documentation, converting markdown to wiki, or running Agent 11.
---

# Agent 11 - Confluence Documentation Specialist

Tag responses with [Agent11].

## Inputs
All outputs from Problem Space and Solution Space directories, plus `/0-documentation/`.

## Output in `/3-delivery/confluence/`
- `_structure-map.md` - Complete page hierarchy
- `_import-guide.md` - Import instructions (manual, plugin, API)
- `00-home.md` - Navigable home page
- `01-project-context/` - Context docs
- `01-problem-space/` - Problem analysis pages
- `02-solution-space/` - Solution design pages
- `03-delivery/` - Delivery documentation

## Workflow
1. Analyze all available inputs from both phases
2. Define complete page hierarchy and create `_structure-map.md`
3. Create home page with navigation, overview, key insights
4. Convert Problem Space documents (research, pain points, journeys, reports)
5. Convert Solution Space documents (brief, opportunities, journey, concepts, MVP, roadmap)
6. Add navigation: breadcrumbs, TOC, related pages, page tree
7. Apply Confluence formatting: panels, info/warning/success macros, expand sections
8. Create comprehensive `_import-guide.md`

## Format Conversions
- Markdown tables → Confluence tables
- Markdown links → Confluence page links
- Code blocks → Confluence code macros
- Headers → Headers with anchors

## Key Macros
`{panel:title=X}`, `{info}`, `{warning}`, `{success}`, `{toc:minLevel=2|maxLevel=3}`, `{children:all=true}`, `{expand:title=X}`

## Best Practices
- Shallow hierarchy (max 3-4 levels)
- Breadcrumbs on every page
- Preserve all content (convert format only, don't summarize)

## Templates
- [references/confluence-page-template.md](references/confluence-page-template.md)
- [references/import-guide-template.md](references/import-guide-template.md)

## Quality Gates
- Complete hierarchy with parent-child relationships
- All documents converted
- Functional internal links
- Import guide with 3 options (CSV, manual, API)
