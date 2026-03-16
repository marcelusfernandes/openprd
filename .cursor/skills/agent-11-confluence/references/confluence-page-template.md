# Confluence Page Template

## Purpose
Template padrão para páginas Confluence, garantindo estrutura consistente e navegação eficiente.

## Basic Page Structure

```markdown
# [Page Title]

{info}
**Quick Summary:** [One-sentence description of what this page covers]
{info}

## Overview

[2-3 paragraph introduction explaining the context and purpose of this page]

## Navigation

**Parent:** [Link to parent page]
**Related Pages:**
- [Related page 1]
- [Related page 2]
- [Related page 3]

---

{toc:minLevel=2|maxLevel=3}

---

## [Main Section 1]

### [Subsection 1.1]

[Content here...]

### [Subsection 1.2]

[Content here...]

## [Main Section 2]

### [Subsection 2.1]

[Content here...]

{panel:title=Key Insight}
💡 [Important insight or highlight]
{panel}

## [Main Section 3]

### [Subsection 3.1]

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |

{expand:title=Additional Details}
[Detailed content that can be collapsed]
{expand}

## Key Takeaways

{success}
✅ **Key Takeaway 1:** [Summary point]
{success}

{success}
✅ **Key Takeaway 2:** [Summary point]
{success}

## Related Resources

- [Link to related document 1]
- [Link to related document 2]
- [Link to Confluence page]
- [Link to external resource]

## Next Steps

1. [Action item or next page to visit]
2. [Action item or next page to visit]
3. [Action item or next page to visit]

---

**Last Updated:** [Date]
**Owner:** [Name/Team]
**Status:** {status:colour=Green|title=Active}
```

## Confluence-Specific Formatting

### Panels
```
{panel:title=Panel Title}
Content inside panel
{panel}

{panel:title=Panel Title|borderColor=#ccc|titleBGColor=#F7D6C4|bgColor=#FFFFCE}
Custom styled panel
{panel}
```

### Info Macros
```
{info:title=Information}
💡 Informational content
{info}

{warning:title=Warning}
⚠️ Warning content
{warning}

{success:title=Success}
✅ Success or positive content
{success}

{note:title=Note}
📝 Additional note
{note}
```

### Table of Contents
```
{toc}                              # Basic TOC
{toc:minLevel=2|maxLevel=3}       # Limited levels
{toc:style=disc}                   # Bulleted style
{toc:printable=false}              # Hide in print
```

### Children Display
```
{children}                         # Show child pages
{children:all=true|sort=title}    # All descendants, sorted
{children:depth=2}                 # 2 levels deep
```

### Page Tree
```
{pagetree}                         # Show page tree
{pagetree:root=@self}             # From current page
{pagetree:startDepth=1}           # Start depth
```

### Expand Macro
```
{expand:title=Click to expand}
Hidden content here
{expand}
```

### Code Block
```
{code:language=javascript|title=Example Code}
function example() {
  return "Hello World";
}
{code}
```

### Status
```
{status:colour=Green|title=Active}
{status:colour=Yellow|title=In Progress}
{status:colour=Red|title=Blocked}
{status:colour=Blue|title=Complete}
{status:colour=Grey|title=Archived}
```

## Page Types

### Overview Page Template
```markdown
# [Topic] Overview

{info}
This page provides an overview of [topic] including [key areas covered].
{info}

## Quick Navigation

{children:all=false|sort=title}

## Summary

[Executive summary of the topic - 2-3 paragraphs]

## Key Topics

### [Topic 1]
[Brief description with link to detail page]
→ [Read more about Topic 1]

### [Topic 2]
[Brief description with link to detail page]
→ [Read more about Topic 2]

## Related Pages
- [Related page 1]
- [Related page 2]
```

### Detail Page Template
```markdown
# [Specific Item Name]

**Type:** [Document type]
**Status:** {status:colour=Green|title=Active}
**Last Updated:** [Date]

## Summary

[Brief summary - 1 paragraph]

## Details

### [Section 1]
[Detailed content]

### [Section 2]
[Detailed content]

## Related
- [Parent or overview page]
- [Related detail pages]
```

### Report/Analysis Page Template
```markdown
# [Report Name]

{panel:title=Executive Summary}
[Key findings and conclusions - 2-3 sentences]
{panel}

## Overview
[Context and purpose]

## Findings

### Finding 1: [Title]
{info}
**Key Insight:** [Main point]
{info}

[Details and evidence]

### Finding 2: [Title]
{info}
**Key Insight:** [Main point]
{info}

[Details and evidence]

## Recommendations

1. **[Recommendation 1]**
   - Rationale: [Why]
   - Impact: [Expected outcome]

2. **[Recommendation 2]**
   - Rationale: [Why]
   - Impact: [Expected outcome]

## Next Steps
[Action items]
```

## Formatting Best Practices

### Headers
- **H1 (#):** Page title only (once per page)
- **H2 (##):** Main sections
- **H3 (###):** Subsections
- **H4 (####):** Rarely used, for deep hierarchy

### Lists
```
Unordered:
- Item 1
- Item 2
  - Nested item
  - Nested item

Ordered:
1. First item
2. Second item
   a. Sub-item
   b. Sub-item
```

### Links
```
Internal page: [Page Name]
External: [Link Text|https://example.com]
Anchor: [Section Name|#anchor-name]
```

### Tables
```
|| Header 1 || Header 2 || Header 3 ||
| Cell 1 | Cell 2 | Cell 3 |
| Cell 4 | Cell 5 | Cell 6 |
```

### Text Formatting
```
*italic*
**bold**
***bold italic***
~~strikethrough~~
{{monospace}}
```

## Navigation Elements

### Breadcrumbs
Add at top of each page:
```
**Navigation:** [Home] > [Section] > [Subsection] > [Current Page]
```

### Related Pages Section
Add at bottom or sidebar:
```
## Related Pages
- [Link 1] - Brief description
- [Link 2] - Brief description
- [Link 3] - Brief description
```

### Quick Links Panel
For landing/overview pages:
```
{panel:title=Quick Links}
🎯 [Most Important Page]
📊 [Key Report]
📋 [Action Items]
🗺️ [Roadmap]
{panel}
```

## Common Page Patterns

### Home/Landing Page
- Hero section with project title
- Quick navigation panel
- Overview section
- Page tree or children display
- Key insights highlight
- Next steps

### Section Overview
- Summary of section
- Children pages display
- Navigation to related sections
- Key highlights

### Detail Page
- Clear title and metadata
- Structured content with TOC
- Related pages
- Breadcrumbs

### Report/Analysis
- Executive summary panel
- Structured findings
- Visual elements (tables, charts descriptions)
- Recommendations
- Next steps

## Metadata Footer

Add to bottom of important pages:
```
---

**Document Information**
- **Owner:** [Name/Team]
- **Last Updated:** [Date]
- **Status:** {status:colour=Green|title=Current}
- **Version:** [Version number]
- **Review Date:** [Next review date]
```

## Tips for Confluence Conversion

1. **Preserve Content:** Don't lose any information from source
2. **Add Navigation:** Links, breadcrumbs, TOC
3. **Format for Scanning:** Use panels, bullets, tables
4. **Highlight Key Info:** Use info/warning/success macros
5. **Collapse Details:** Use expand macros for lengthy content
6. **Link Extensively:** Connect related pages
7. **Use Metadata:** Status, dates, ownership
8. **Test Links:** Verify all links work after import

## Example Complete Page

```markdown
# Product Brief: Stella Golden Thursdays

**Navigation:** [Home] > [Solution Space] > Product Brief

{info}
**Quick Summary:** Comprehensive product brief for the Stella Golden Thursdays event management transformation initiative.
{info}

{panel:title=Executive Summary}
This initiative transforms the Golden Thursdays event planning experience from a manual, fragmented process into an automated, integrated platform. We're solving critical pain points in event coordination, participant management, and cross-team collaboration to enable HR teams to deliver better events with less effort.
{panel}

{toc:minLevel=2|maxLevel=3}

---

## 1. Problem Context

### Pain Points Identified

{warning:title=Critical Pain Point}
⚠️ **Manual Participant Management:** HR teams spend 8-10 hours per event manually managing participant lists across 5 different tools, leading to errors and frustration.
{warning}

1. **Fragmented Tools** - Data scattered across email, spreadsheets, Slack, calendar
   - Affects: 100% of HR event organizers
   - Current impact: 8-10 hours manual work per event

2. **Communication Complexity** - Manual coordination with multiple stakeholders
   - Affects: All cross-functional events
   - Current impact: Delays, miscommunication, duplicated effort

[Additional pain points...]

### Why Now?
- Golden Thursdays is strategic initiative for 2025
- Current process doesn't scale with growth
- Competitive advantage in employee experience

---

## 2. Product Vision

### What We're Building

**Concept 1: Unified Event Dashboard**
- **Type:** Digital Platform
- **Purpose:** Single source of truth for all event information
- **Value:** Reduces coordination time from 8 hours to 1 hour
- **Phase:** MVP

{expand:title=Full Concept Details}
[Detailed breakdown of the concept...]
{expand}

### How It Transforms Experience

|| Current State || MVP State || Stage 2 State ||
| Manual, 8-10 hrs | Automated, 1-2 hrs | AI-powered, <30 min |
| Scattered tools | Unified platform | Predictive insights |
| Error-prone | Accurate | Proactive |
| Satisfaction: 4.2/10 | Target: 7.5/10 | Target: 8.5/10 |

---

## 3. MVP Scope & Features

{success:title=MVP Objective}
✅ Validate that unified event management reduces coordination time by 70%+ while improving participant satisfaction
{success}

### In-Scope (MVP)

**Core Features (P0 - Critical):**
1. F-001: Unified Event Dashboard - Central hub for all event data
2. F-002: Automated Participant Sync - Integration with HR systems
3. F-003: Communication Templates - Pre-built event communications
4. F-004: Calendar Integration - Sync with team calendars

**Total MVP Features:** 10

[See complete feature list|MVP Features]

---

## 4. Success Metrics

|| Metric || Current || MVP Target || Stage 2 Target ||
| User Satisfaction | 4.2/10 | 7.5/10 | 8.5/10 |
| Coordination Time | 8 hours | 1.5 hours | 30 min |
| Task Success Rate | 60% | 85% | 95% |
| User Adoption | N/A | 40% | 70% |

---

## Related Resources

- [MVP Scope Details]
- [Product Roadmap]
- [Problem Report]
- [Solution Concepts]

## Next Steps

1. Review and approve MVP scope
2. Allocate team resources
3. Begin Sprint 1 planning
4. Schedule stakeholder kickoff

---

**Document Information**
- **Owner:** Product Team
- **Last Updated:** 2025-10-27
- **Status:** {status:colour=Yellow|title=Pending Approval}
- **Next Review:** 2025-11-03
```

---

This template ensures consistent, professional, and navigable Confluence documentation.

