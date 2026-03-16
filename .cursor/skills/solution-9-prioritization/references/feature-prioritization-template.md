---
template_name: "Feature Prioritization Template"
template_version: "1.0.0"
agent: "Agent 9 - Product Prioritization Specialist"
output_location: "/2-solution/2d-prioritization/2d1-mvp/mvp-features.md"
purpose: "Prioritized list of features with Impact/Effort scores and acceptance criteria"
---

# MVP Features - Prioritized List

## Document Metadata
- **Product:** [Name]
- **Created:** [YYYY-MM-DD]
- **Version:** [X.X]
- **Status:** [Draft / Approved]

---

## Overview

**Total Features Evaluated:** [X]
**MVP Features (P0/P1):** [X]
**Deferred Features (P2/P3):** [X]

---

## Prioritization Method

### Impact (User Value): 1-5
- **5 = Critical:** Resolves main pain point, MVP doesn't work without it
- **4 = High:** Significant experience improvement
- **3 = Medium:** Noticeable improvement but not essential
- **2 = Low:** Nice-to-have, marginal value
- **1 = Minimal:** Little impact on experience

### Effort (Implementation): 1-5
- **1 = Very Low:** Hours to 1-2 days
- **2 = Low:** 3-5 days
- **3 = Medium:** 1-2 weeks
- **4 = High:** 2-4 weeks
- **5 = Very High:** 1+ month

### Priority Score
```
Priority Score = Impact / Effort

- Score > 2.0 + Impact >= 4 = P0 (Critical)
- Score > 1.5 OR Impact = 5 = P1 (High)
- Score > 1.0 = P2 (Medium)
- Score <= 1.0 = P3 (Low)
```

---

## P0 Features (Critical - Must Have)

### F-001: [Feature Name]
**Concept:** [SC-XX: Concept Name]

**Description:**
[What this feature does - 1-2 sentences]

**User Value:**
[Why this matters to users - specific benefit]

**Acceptance Criteria:**
- [ ] [Criterion 1 - specific, measurable]
- [ ] [Criterion 2 - specific, measurable]
- [ ] [Criterion 3 - specific, measurable]

**Scores:**
- **Impact:** 5/5 (Critical - [justification])
- **Effort:** 2/5 (Low - [justification])
- **Priority Score:** 2.5 → **P0**

**Dependencies:**
- [Dependency 1 if any]

**Related Journey Stage:** [Stage name from Agent 7]

**Experience Improvement:** [ID from Agent 7]

---

### F-002: [Feature Name]
[Same structure...]

---

[Continue for all P0 features...]

---

## P1 Features (High Priority - Should Have)

### F-005: [Feature Name]
**Concept:** [SC-XX: Concept Name]

**Description:**
[What it does]

**User Value:**
[Why it matters]

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Scores:**
- **Impact:** 4/5 (High - [justification])
- **Effort:** 2/5 (Low - [justification])
- **Priority Score:** 2.0 → **P1**

**Dependencies:**
- [Dependency if any]

---

[Continue for all P1 features...]

---

## P2 Features (Medium - Consider for MVP)

| ID | Feature | Concept | Impact | Effort | Score | Decision |
|----|---------|---------|--------|--------|-------|----------|
| F-012 | [Name] | SC-XX | 4 | 3 | 1.33 | **Defer to Stage 2** |
| F-013 | [Name] | SC-XX | 3 | 2 | 1.50 | **Include in MVP** |
| F-015 | [Name] | SC-XX | 3 | 3 | 1.00 | **Defer to Stage 2** |

**Rationale for Decisions:**
- **F-012:** High impact but medium effort. Deferred to keep MVP lean and validate core first.
- **F-013:** Good score and enables key experience improvement. Included.
- **F-015:** Borderline score. Not critical for minimum value. Deferred.

---

## P3 Features (Low - Defer to Later Phases)

| ID | Feature | Concept | Impact | Effort | Score | Phase |
|----|---------|---------|--------|--------|-------|-------|
| F-018 | [Name] | SC-XX | 2 | 4 | 0.50 | Stage 2 |
| F-022 | [Name] | SC-XX | 2 | 5 | 0.40 | Stage 3 |
| F-025 | [Name] | SC-XX | 1 | 3 | 0.33 | Backlog |

---

## Feature Dependencies

### Dependency Graph
```
F-001 (foundation) → F-003, F-005
F-002 → F-006
F-004 (independent)
F-007 → F-009
```

**Critical Path:**
F-001 must be done first as it's a dependency for F-003 and F-005.

**Parallel Tracks:**
- Track A: F-001 → F-003 → F-005
- Track B: F-002 → F-006 (can run parallel)
- Track C: F-004, F-007 (independent)

---

## Summary

### MVP Includes (12 features)
**P0 (Critical):** F-001, F-002, F-003, F-004
**P1 (High):** F-005, F-006, F-007, F-008, F-009, F-010, F-011, F-013

### Deferred to Stage 2 (18 features)
- P2 features with good scores but not critical
- Some P1 features that depend on MVP validation

### Deferred to Stage 3 or Backlog (15 features)
- P3 features with low scores
- Exploratory or optimization features

---

## Document Information
- **Created By:** Agent 9
- **Date:** [YYYY-MM-DD]
- **Version:** [X.X]
- **Status:** [Draft / Approved]

