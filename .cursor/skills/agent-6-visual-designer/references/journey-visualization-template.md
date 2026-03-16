# Journey Visualization - Figma Make Specification

**Project:** [Project Name]  
**Date:** [YYYY-MM-DD]  
**Journey Type:** As-Is / To-Be  
**Total Stages:** [N]  
**Version:** 1.0

---

## ⚠️ CRITICAL: Figma Make Configuration

**THESE SPECIFICATIONS ARE CRITICAL FOR FIGMA MAKE AI TO GENERATE CORRECTLY**

```
LAYOUT DIRECTION: HORIZONTAL (left-to-right flow)
READING FLOW: Left → Right across stages
CANVAS ORIENTATION: Landscape (horizontal scrolling)

CANVAS DIMENSIONS:
- Width: [Number of Stages × 600px + 200px padding] = [X]px total
- Height: ~1100px minimum (auto-adjust based on content)
- Padding: 100px left + 100px right = 200px total

STAGE CONFIGURATION:
- Stage Width: 600px (FIXED - do not vary)
- Stage Height: Auto (based on lane content)
- Stage Spacing: 40px horizontal gap between stages
- Stage Arrangement: INLINE (not stacked)

SWIMLANE CONFIGURATION:
- Layout: VERTICAL stack within each 600px horizontal stage
- Swimlane Height: Auto (min 150px per lane, expands with content)
- Swimlane Spacing: 20px vertical gap between lanes
- Lane Order (top to bottom): Header → Context → JTBD → Emotion → Pains → Needs → Opportunities → Hypothesis

SPACING SYSTEM:
- Internal Padding (stage): 24px
- Element Spacing (vertical): 16px between elements
- Icon Spacing: 8px from text
- Badge Spacing: 8px between badges
```

---

## 🎨 Visual System

### Color Palette (Hex Codes)

**Pain Points (Red Scale by Severity):**
```
Critical (9-10): #DC2626 (red-600) 🔴
High (7-8):      #EA580C (orange-600) 🟠
Medium (5-6):    #F59E0B (amber-500) 🟡
Low (1-4):       #FCD34D (amber-300) 🟢
```

**Jobs to Be Done (Purple):**
```
Background: #EDE9FE (violet-100)
Border:     #7C3AED (violet-600)
Badge:      #8B5CF6 (violet-500)
Text:       #4C1D95 (violet-900)
```

**Needs (Yellow):**
```
Background: #FEF3C7 (amber-100)
Border:     #F59E0B (amber-500)
Text:       #78350F (amber-900)
```

**Opportunities (Green Scale by Impact):**
```
High Impact (9-10):   #059669 (green-600) 🟢
Medium Impact (5-8):  #10B981 (green-500) 🟢
Low Impact (1-4):     #6EE7B7 (green-300) 🟢
```

**Touchpoints (Blue):**
```
Background: #BFDBFE (blue-200)
Text:       #1E40AF (blue-800)
Border:     #3B82F6 (blue-500)
```

**Emotion Loadbar (Gradient):**
```
0-20%:   #DC2626 (red-600)
21-40%:  #EA580C (orange-600)
41-60%:  #F59E0B (amber-500)
61-80%:  #84CC16 (lime-500)
81-100%: #10B981 (green-500)
```

**Background & Neutrals:**
```
Canvas Background: #FFFFFF (white)
Stage Background:  #F9FAFB (gray-50)
Section Divider:   #E5E7EB (gray-200)
Text Primary:      #111827 (gray-900)
Text Secondary:    #6B7280 (gray-500)
```

### Badge System

**Pain Point Badge:**
```
┌─────────────┐
│ [9] 🔴      │ ← Score (1-10) + Emoji + Color
│ Pain Name   │ ← Short description
│ (UX)        │ ← Category (optional)
└─────────────┘

Styling:
- Background: Severity color (see Pain Points palette)
- Text: White (#FFFFFF)
- Font: 12px bold (score), 10px medium (name)
- Padding: 8px
- Border-radius: 6px
- Min-width: 120px
- Drop-shadow: 0 2px 4px rgba(0,0,0,0.1)
```

**Opportunity Badge:**
```
┌─────────────┐
│ [9] 🟢      │ ← Impact score + Emoji + Color
│ Opp Name    │ ← Short description
│ (High)      │ ← Impact level
└─────────────┘

Styling:
- Background: Impact color (see Opportunities palette)
- Text: White (#FFFFFF)
- Font: 12px bold (score), 10px medium (name)
- Padding: 8px
- Border-radius: 6px
- Min-width: 120px
- Drop-shadow: 0 2px 4px rgba(0,0,0,0.1)
```

**Touchpoint Badge:**
```
┌──────────┐
│ 🔵 Tool A │ ← Emoji + Name
└──────────┘

Styling:
- Background: #BFDBFE (blue-200)
- Text: #1E40AF (blue-800)
- Font: 10px semibold
- Padding: 6px 12px
- Border-radius: 12px (pill shape)
- Border: 1px solid #3B82F6 (blue-500)
```

**JTBD Card:**
```
┌─────────────────────────────────┐
│ [J1] 🟣 Job Statement Core     │ ← Badge + short statement
│ Outcome: [Top desired outcome]  │ ← Most underserved outcome
│ Gap: [Crítico/Alto/Médio]       │ ← Opportunity gap level
└─────────────────────────────────┘

Styling:
- Background: #EDE9FE (violet-100)
- Border: 2px solid #7C3AED (violet-600)
- Badge Background: #8B5CF6 (violet-500)
- Badge Text: #FFFFFF (white)
- Body Text: #4C1D95 (violet-900)
- Font: 12px medium (statement), 10px regular (outcome/gap)
- Padding: 12px
- Border-radius: 6px
- Min-width: 200px
```

**Need Card:**
```
┌─────────────┐
│ Need Name   │ ← Description
│ (from Pain) │ ← Source reference
└─────────────┘

Styling:
- Background: #FEF3C7 (amber-100)
- Border: 2px solid #F59E0B (amber-500)
- Text: #78350F (amber-900)
- Font: 12px medium
- Padding: 12px
- Border-radius: 6px
- Min-width: 120px
```

### Typography Hierarchy

```
Stage Title:      24px, Bold, #111827 (gray-900)
Section Headers:  18px, Semibold, #374151 (gray-700)
Body Text:        14px, Regular, #1F2937 (gray-800)
Pain Point Label: 12px, Medium, #FFFFFF (white on colored background)
Badge Text:       10px, Bold, varies by badge type
Quote Text:       14px, Italic, #6B7280 (gray-500)

Font Family: System default (Inter, SF Pro, or Roboto)
Line Height: 1.5
```

### Spacing Scale

```
Stage Internal Padding:    24px
Section Vertical Spacing:  20px (between sections)
Element Vertical Spacing:  16px (between elements)
Badge Horizontal Spacing:  8px (between badges)
Icon Text Spacing:         8px (icon to text)
Lane Vertical Margin:      20px (between lanes)
```

---

## 🗺️ Journey Stage Structure

**REPEAT THIS STRUCTURE FOR EACH STAGE**

### Stage [N]: [Stage Name]

#### 1.1 Stage Header

**Stage [N]: [Stage Name]**

**Description:**  
[1-2 sentence overview of what happens in this stage]

**Duration:** [Average time spent: e.g., "2-3 hours" or "2-5 days"]

**Key Context:**
- [Key fact or insight about this stage]

---

#### 1.2 Context Section

**What Happens / What's Done:**

[Detailed description of activities, decisions, and workflows in this stage. Include insights and observations from interviews. 2-3 paragraphs.]

Key activities:
- [Activity 1]
- [Activity 2]
- [Activity 3]

**Touchpoints:**

🔵 [Tool/System 1]  🔵 [Tool/System 2]  🔵 [Tool/System 3]  🔵 [Tool/System 4]

[List all tools, systems, platforms, or services used in this stage as blue pill badges]

**Actors/Roles Involved:**
- [Role 1]: [What they do]
- [Role 2]: [What they do]

---

#### 1.3 Jobs to Be Done (JTBD) 🟣

**Active Jobs at This Stage:**

| Job | Statement Core | Top Outcome | Gap |
|-----|---------------|-------------|-----|
| [J#] | [Short job statement from asis-journey.md "Jobs Being Done" section] | [Most underserved desired outcome at this stage] | [Crítico/Alto/Médio] |
| [J#] | [Short job statement] | [Top outcome] | [Gap level] |

**Causal Chain:** [How jobs connect at this stage — e.g., "Fragmentação (J5) → Sobrecarga (J3) → Modo executor"]

[Source: jtbd-mapping.md]

[Take content directly from asis-journey.md "Jobs Being Done (unified from JTBD)" sections. Format as table with job badge, statement core, top outcome, and gap. Add causal chain showing how jobs interact at this stage.]

---

#### 1.4 Emotion & Satisfaction

**Satisfaction Level:**

**Option 1: Loadbar (Preferred)**
```
████████░░ 75% satisfaction
```
[Use block characters to show percentage: 0-100%]
[Color according to percentage: 0-20% red, 21-40% orange, 41-60% yellow, 61-80% lime, 81-100% green]

**Option 2: Emoji Scale (Alternative)**
```
😫 😟 😐 🙂 😊  →  🙂 selected
```
[Show emoji scale with one highlighted]

**Emotional State:** [Frustrated / Anxious / Neutral / Satisfied / Delighted]

**Representative Quote:**

> "[Direct quote from interview that captures the emotion/experience in this stage. Should be authentic user voice that represents the stage sentiment.]"
> 
> — [Source: Interview with Persona/Role if available]

**Emotion Drivers:**
- [What causes positive emotions]
- [What causes negative emotions]

---

#### 1.5 Pain Points Lane 🔴

**Pain Points in This Stage:**

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ [9] 🔴           │  │ [7] 🟠           │  │ [5] 🟡           │
│ Pain Point 1     │  │ Pain Point 2     │  │ Pain Point 3     │
│ (UX/Ops/Business)│  │ (Type)           │  │ (Type)           │
└──────────────────┘  └──────────────────┘  └──────────────────┘

**Pain Point Details:**

**🔴 [Score: 9] Pain Point 1 Name (Critical)**
- **Description:** [What the pain point is - specific description]
- **Category:** UX / Operational / Business / Technical
- **Impact:** [How it affects users/business]
- **Frequency:** [How often it occurs: Always / Often / Sometimes / Rarely]
- **Quote:** "[Supporting quote from interview]"

**🟠 [Score: 7] Pain Point 2 Name (High)**
- **Description:** [What the pain point is]
- **Category:** [Type]
- **Impact:** [Effect]
- **Frequency:** [Occurrence]
- **Quote:** "[Quote]"

**🟡 [Score: 5] Pain Point 3 Name (Medium)**
- **Description:** [What the pain point is]
- **Category:** [Type]
- **Impact:** [Effect]
- **Frequency:** [Occurrence]
- **Quote:** "[Quote]"

[Continue for all pain points in this stage, sorted by severity score descending]

---

#### 1.6 Needs Lane 🟡

**Needs Derived from Pain Points:**

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ Need 1           │  │ Need 2           │  │ Need 3           │
│ (from Pain 1, 2) │  │ (from Pain 3)    │  │ (from Pain 4)    │
└──────────────────┘  └──────────────────┘  └──────────────────┘

**Need Details:**

**🟡 Need 1: [Need Name]**
- **Description:** [What users need - framed positively as requirement]
- **Derived From:** Pain Point 1, Pain Point 2
- **User Story:** "As a [persona], I need [capability] so that [benefit]"
- **Success Criteria:** [How we know this need is met]

**🟡 Need 2: [Need Name]**
- **Description:** [What users need]
- **Derived From:** Pain Point 3
- **User Story:** "[Story]"
- **Success Criteria:** [Criteria]

**🟡 Need 3: [Need Name]**
- **Description:** [What users need]
- **Derived From:** Pain Point 4
- **User Story:** "[Story]"
- **Success Criteria:** [Criteria]

[Continue for all needs - typically 2-5 needs per stage]

---

#### 1.7 Opportunities Lane 🟢

**Improvement Opportunities:**

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ [9] 🟢           │  │ [6] 🟢           │  │ [4] 🟢           │
│ Opportunity 1    │  │ Opportunity 2    │  │ Opportunity 3    │
│ (High Impact)    │  │ (Medium Impact)  │  │ (Low Impact)     │
└──────────────────┘  └──────────────────┘  └──────────────────┘

**Opportunity Details:**

**🟢 [Impact: 9] Opportunity 1 Name (High Impact)**
- **Description:** [What the opportunity is - specific improvement or solution direction]
- **Addresses:** Pain Points 1, 2 | Needs 1
- **Potential Value:** [Expected benefit if implemented]
- **Effort Estimate:** Low / Medium / High
- **Type:** Quick Win / Strategic Initiative / Long-term Investment

**🟢 [Impact: 6] Opportunity 2 Name (Medium Impact)**
- **Description:** [What the opportunity is]
- **Addresses:** Pain Point 3 | Need 2
- **Potential Value:** [Benefit]
- **Effort Estimate:** [Level]
- **Type:** [Type]

**🟢 [Impact: 4] Opportunity 3 Name (Low Impact)**
- **Description:** [What the opportunity is]
- **Addresses:** Pain Point 4 | Need 3
- **Potential Value:** [Benefit]
- **Effort Estimate:** [Level]
- **Type:** [Type]

[Continue for all opportunities, sorted by impact score descending]

---

#### 1.8 Hypothesis Section 💡

**Stage Hypothesis:**

**💡 Hypothesis Statement:**

"If we implement [solution/improvement], we expect [outcome/benefit] because [reasoning based on pain points and user needs]."

**Example:**
"If we implement an automated notification system with clear status updates, we expect user anxiety to decrease by 50% and support tickets related to status inquiries to drop by 70%, because the primary pain point is lack of visibility into process status."

**Validation Approach:**
- **Pre-implementation:** [How to test hypothesis before building - e.g., prototype, user interview]
- **Success Metrics:** [How to measure if hypothesis is true after implementation]
- **Timeline:** [When to measure results]

**Assumptions:**
- [Key assumption 1]
- [Key assumption 2]
- [Key assumption 3]

**Risks if Wrong:**
- [What happens if hypothesis doesn't hold]
- [Mitigation strategy]

---

**[END OF STAGE [N] - REPEAT STRUCTURE FOR NEXT STAGE]**

---

---

## 📊 Journey-Level Metrics & Insights

**After detailing all stages, include journey-level summary:**

### Overall Journey Statistics

**Total Journey:**
- **Number of Stages:** [N]
- **Total Duration:** [Average time from start to end]
- **Total Pain Points:** [Count across all stages]
- **Total Needs:** [Count across all stages]
- **Total Opportunities:** [Count across all stages]

**Pain Point Distribution:**
| Severity | Count | Percentage |
|----------|-------|------------|
| Critical (9-10) | [N] | [%] |
| High (7-8) | [N] | [%] |
| Medium (5-6) | [N] | [%] |
| Low (1-4) | [N] | [%] |

**Pain Point by Category:**
| Category | Count | Avg Severity |
|----------|-------|--------------|
| UX | [N] | [Score] |
| Operational | [N] | [Score] |
| Business | [N] | [Score] |
| Technical | [N] | [Score] |

**Opportunity Distribution:**
| Impact Level | Count | Percentage |
|--------------|-------|------------|
| High (9-10) | [N] | [%] |
| Medium (5-8) | [N] | [%] |
| Low (1-4) | [N] | [%] |

### Critical Insight Summary

**Top 5 Critical Pain Points (Journey-Wide):**
1. [9-10] [Pain Point Name] - Stage [N]
2. [9-10] [Pain Point Name] - Stage [N]
3. [9-10] [Pain Point Name] - Stage [N]
4. [9-10] [Pain Point Name] - Stage [N]
5. [9-10] [Pain Point Name] - Stage [N]

**Top 5 High-Impact Opportunities (Journey-Wide):**
1. [9-10] [Opportunity Name] - Stage [N]
2. [9-10] [Opportunity Name] - Stage [N]
3. [9-10] [Opportunity Name] - Stage [N]
4. [9-10] [Opportunity Name] - Stage [N]
5. [9-10] [Opportunity Name] - Stage [N]

**Most Critical Stages (by pain severity):**
1. Stage [N]: [Name] - Avg severity [Score]
2. Stage [N]: [Name] - Avg severity [Score]
3. Stage [N]: [Name] - Avg severity [Score]

**Emotional Journey Pattern:**
```
Stage 1: 😐 (50%) → Stage 2: 😟 (35%) → Stage 3: 😫 (20%) → Stage 4: 🙂 (65%) → Stage 5: 😊 (80%)
```
[Show emotional progression across journey]

---

## 📐 Implementation Notes for Figma Make

### Canvas Setup Instructions

1. **Create New Figma File:**
   - Orientation: Landscape
   - Canvas size: [Calculated Width]px × ~1100px
   - Background: #FFFFFF

2. **Configure Frame:**
   - Name: "Journey Map - [Project Name]"
   - Layout: Auto layout HORIZONTAL
   - Direction: Left to right
   - Gap: 40px (between stages)
   - Padding: 100px left/right, 50px top/bottom

3. **Create Stage Columns:**
   - For each stage, create frame:
     - Width: 600px (FIXED)
     - Height: Auto (hug contents)
     - Layout: Auto layout VERTICAL
     - Gap: 20px (between lanes)
     - Padding: 24px
     - Background: #F9FAFB (gray-50)
     - Corner radius: 8px

4. **Create Swimlanes (within each stage):**
   - Stack vertically in order: Header → Context → JTBD → Emotion → Pains → Needs → Opps → Hypothesis
   - Each lane is a separate frame:
     - Width: 552px (600px - 24px padding × 2)
     - Height: Auto (hug contents)
     - Layout: Auto layout VERTICAL
     - Padding: 16px
     - Gap: 8px between elements

### Component Creation Guide

**Pain Point Component:**
```
Frame (Auto layout VERTICAL)
├─ Badge background (colored rectangle with border-radius: 6px)
│  ├─ Score + Emoji (12px bold, white)
│  ├─ Name (10px medium, white)
│  └─ Category (10px regular, white)
└─ Drop shadow (0 2px 4px rgba(0,0,0,0.1))
```

**Touchpoint Component:**
```
Frame (Auto layout HORIZONTAL)
├─ Emoji (16px)
├─ Spacer (8px)
└─ Text (10px semibold, blue-800)
Background: blue-200, Border-radius: 12px (pill)
```

**JTBD Card Component:**
```
Frame (Auto layout VERTICAL)
├─ Job Badge (pill: #8B5CF6 bg, white text, 10px bold) — e.g. "J1"
├─ Statement Core (12px medium, #4C1D95)
├─ Outcome + Gap (10px regular, #4C1D95)
Background: #EDE9FE, Border: 2px solid #7C3AED
Border-radius: 6px, Padding: 12px
```

**Emotion Loadbar Component:**
```
Frame (width: 200px, height: 20px)
├─ Background bar (gray-200)
└─ Fill bar (gradient based on percentage, width: [%])
```

### Export Settings

**For Presentation:**
- Format: PDF
- Scale: 2x
- Include: All stages in one horizontal layout
- Pages: Single page (wide)

**For Sharing:**
- Format: PNG
- Scale: 2x or 3x (high DPI)
- Background: Include (white)

**For Prototype:**
- Enable horizontal scroll
- Prototype link with "Present" mode
- Allow: Zoom in/out

---

## 🔗 Source References

**Journey Source:**
- File: `1-problem/1c-asis-journey/asis-journey.md`
- Created by: Agent 4 (Journey Consolidation Specialist)

**JTBD Source:**
- File: `1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md`
- Created by: Agent 2C (JTBD Specialist)

**Pain Points Source:**
- File: `1-problem/1b-painpoints/painpoint-mapping.md`
- Created by: Agent 2 (Pain Point Analysis Specialist)

**Interviews Source:**
- Directory: `1-problem/1a-interview-analysis/`
- Created by: Agent 1 (Qualitative Research Specialist)

**Context Source:**
- File: `0-documentation/broad-context.md`
- Created by: Agent 0 (Product & Service Specialist)

---

## ✅ Quality Checklist

Before finalizing this journey visualization, verify:

- [ ] All stages have complete 8-section structure (incl. JTBD)
- [ ] Pain points have severity scores (1-10) and correct color codes
- [ ] Opportunities have impact scores (1-10) and correct color codes
- [ ] Touchpoints formatted as blue badges (🔵)
- [ ] Emotion indicators present (loadbar or emoji) for all stages
- [ ] Representative quotes included for each stage
- [ ] Needs mapped to source pain points
- [ ] JTBD lane present in every stage with active jobs, outcomes, gaps, and causal chains
- [ ] JTBD coverage summary included in journey-level metrics
- [ ] Hypothesis generated for each stage (positioned AFTER opportunities)
- [ ] Canvas dimensions calculated correctly
- [ ] All hex color codes documented
- [ ] Typography hierarchy specified (24px/18px/14px/12px/10px)
- [ ] Spacing system documented (24px/16px/8px)
- [ ] Horizontal layout explicitly specified (600px stages, left-to-right)
- [ ] Journey-level metrics calculated
- [ ] Top pain points and opportunities summarized
- [ ] Source references complete
- [ ] Ready to copy-paste into Figma Make

---

## 📝 Usage Notes

**For Agent 6 (Visual Journey Designer):**

This template provides the complete structure for generating Figma Make-ready journey visualizations. Follow these guidelines:

1. **Be Explicit:** Figma Make AI needs precise specifications - don't assume it will infer layout or colors
2. **Use Hex Codes:** Always include hex color codes, never generic color names
3. **Fixed Measurements:** Use px values for all spacing and sizing
4. **Horizontal Priority:** Emphasize horizontal layout multiple times - it's critical
5. **Badge Format:** Always include score + emoji + color for pain/opportunity badges
6. **Quote Authenticity:** Use real quotes from interviews when available
7. **Hypothesis Quality:** Generate meaningful hypotheses based on data, not generic statements
8. **Completeness:** Fill ALL sections for ALL stages - no placeholders

**For Stakeholders Using This Output:**

This document is designed to be:
- **Copy-paste ready** for Figma Make AI
- **Complete specification** requiring no additional formatting
- **Professional quality** suitable for executive presentation
- **Evidence-based** with clear source references
- **Actionable** with clear opportunities and hypotheses

---

**Template Version:** 1.0  
**Last Updated:** 2025-10-16  
**Created By:** Agent 6 (Visual Journey Designer)  
**Template File:** `journey-visualization-template.md`

