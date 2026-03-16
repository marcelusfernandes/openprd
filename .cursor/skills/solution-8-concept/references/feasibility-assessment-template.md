---
template_name: "Feasibility Assessment Template"
template_version: "1.0.0"
agent: "Agent 8 - Solution Concept Specialist"
output_location: "/2-solution/2c-solution-concepts/feasibility-assessment.md"
purpose: "High-level feasibility assessment of all solution concepts for prioritization"
---

# Feasibility Assessment: Solution Concepts

## Document Metadata
- **Created:** [YYYY-MM-DD]
- **Version:** [X.X]
- **Status:** [Draft / In Review / Approved]
- **Total Concepts Assessed:** [X]

---

## Executive Summary

### Assessment Overview
**Purpose:**
Evaluate the feasibility of each solution concept to inform prioritization and identify risks early.

**Approach:**
High-level assessment across three dimensions:
- **Viability** (1-10): Is it viable technically, for business, and for users?
- **Complexity** (L/M/H): How complex to implement?
- **Risk** (L/M/H): What are the main risks?

**Key Findings:**
- **Go (Recommended):** [X] concepts - High viability, manageable complexity
- **Consider (Conditional):** [X] concepts - Good viability but higher complexity
- **Hold (Defer):** [X] concepts - Lower viability or very high complexity/risk

---

## Assessment Framework

### Viability Score (1-10)

**Components:**
1. **Technical Viability (1-10)**
   - Is the technology available/accessible?
   - Can we realistically build this?
   - Do we have or can get the expertise?

2. **Business Viability (1-10)**
   - Does it align with business strategy?
   - Are resources available or attainable?
   - Does value justify investment?

3. **User Desirability (1-10)**
   - Do users want/need this?
   - Is there evidence of demand from Phase 1?
   - Will users adopt it?

**Overall Viability = Average of 3 scores**

### Complexity (Low / Medium / High)
- **Low:** Simple implementation, few integrations, proven patterns
- **Medium:** Standard complexity, some integrations, established approaches
- **High:** Complex implementation, many dependencies, novel solutions

### Risk (Low / Medium / High)
- **Low:** Few unknowns, low impact if fails, easy to validate
- **Medium:** Some unknowns, moderate impact, standard validation
- **High:** Many unknowns, high impact if fails, difficult to validate

### Recommendation
- **Go:** Viability 7+, Complexity Low-Medium, Risk Low-Medium
- **Consider:** Viability 5-7 OR Complexity High OR Risk High
- **Hold:** Viability <5 OR (Complexity High AND Risk High)

---

## Concept Assessments

### Concept SC-01: [Concept Name]

#### Viability Assessment

**Technical Viability: [X]/10**
- **Assessment:** [Is technology available? Can we build it?]
- **Justification:**
  - ✅ [Factor supporting viability]
  - ✅ [Factor supporting viability]
  - ⚠️ [Factor of concern if any]

**Business Viability: [X]/10**
- **Assessment:** [Does it fit strategy? Resources available?]
- **Justification:**
  - ✅ [Factor supporting viability]
  - ✅ [Factor supporting viability]
  - ⚠️ [Factor of concern if any]

**User Desirability: [X]/10**
- **Assessment:** [Do users want it? Evidence of demand?]
- **Justification:**
  - ✅ [Evidence from Phase 1]
  - ✅ [User pain point connection]
  - ⚠️ [Factor of concern if any]

**Overall Viability: [X]/10**
*(Average of Technical, Business, User scores)*

---

#### Complexity Assessment

**Overall Complexity: [Low / Medium / High]**

**Complexity Factors:**

**Implementation Complexity:**
- [Factor 1: e.g., "5 main features, standard patterns"]
- [Factor 2: e.g., "Proven technology stack"]
- [Factor 3: if applicable]
- **Assessment:** [Low/Med/High]

**Integration Complexity:**
- [Number of integrations needed]
- [Complexity of each integration]
- [Dependency on external systems]
- **Assessment:** [Low/Med/High]

**Novelty/Uncertainty:**
- [How novel is this solution?]
- [Have we done something similar before?]
- [Industry precedents?]
- **Assessment:** [Low/Med/High]

**Justification:**
[Overall explanation of why this complexity level]

---

#### Risk Assessment

**Overall Risk Level: [Low / Medium / High]**

**Main Risks:**

| Risk | Impact | Mitigation Strategy |
|------|--------|-------------------|
| [Technical risk] | H/M/L | [How to address] |
| [Business risk] | H/M/L | [How to address] |
| [User adoption risk] | H/M/L | [How to address] |

**Key Uncertainties:**
- [Uncertainty 1 that needs validation]
- [Uncertainty 2 that needs validation]

---

#### Dependencies & Constraints

**Critical Dependencies:**
- [What must exist before this can be built]
- [What this depends on]

**Resource Constraints:**
- [Team expertise needed]
- [Timeline considerations]
- [Budget considerations if applicable]

**External Dependencies:**
- [Third-party services or APIs]
- [External data sources]

---

#### Recommendation

**Overall Assessment: [Go / Consider / Hold]**

**Rationale:**
[Clear explanation of recommendation based on viability, complexity, and risk]

**If Go:**
- **Timing:** [MVP / Stage 2]
- **Priority:** [High / Medium]
- **Next Steps:** [What to do next]

**If Consider:**
- **Condition:** [What needs to happen for this to be Go]
- **Validation Needed:** [What to validate first]
- **Decision Point:** [When to re-assess]

**If Hold:**
- **Reason:** [Why holding]
- **Reconsider When:** [Conditions for re-evaluation]

---

### Concept SC-02: [Concept Name]

[Same structure as SC-01...]

#### Viability Assessment
[Same structure...]

#### Complexity Assessment
[Same structure...]

#### Risk Assessment
[Same structure...]

#### Dependencies & Constraints
[Same structure...]

#### Recommendation
[Same structure...]

---

### Concept SC-03: [Concept Name]

[Continue same structure for all concepts...]

---

[Continue for all concepts...]

---

## Summary & Prioritization

### Concept Classification

#### GO Concepts (Recommended for Development)

| ID | Concept | Viability | Complexity | Risk | Phase |
|----|---------|-----------|-----------|------|-------|
| SC-01 | [Name] | [X/10] | [L/M/H] | [L/M/H] | MVP |
| SC-02 | [Name] | [X/10] | [L/M/H] | [L/M/H] | MVP |
| SC-XX | [Name] | [X/10] | [L/M/H] | [L/M/H] | Stage 2 |

**Total GO Concepts:** [X]

**Why These:**
[Brief explanation of why these concepts are recommended]

**Combined Value if All GO Concepts Implemented:**
- [Key benefit 1]
- [Key benefit 2]
- [Key benefit 3]

---

#### CONSIDER Concepts (Conditional Recommendation)

| ID | Concept | Viability | Complexity | Risk | Condition |
|----|---------|-----------|-----------|------|-----------|
| SC-XX | [Name] | [X/10] | [L/M/H] | [L/M/H] | [What's needed] |
| SC-XX | [Name] | [X/10] | [L/M/H] | [L/M/H] | [What's needed] |

**Total CONSIDER Concepts:** [X]

**Conditions for Proceeding:**
- [Concept X]: [What needs to be validated/resolved]
- [Concept Y]: [What needs to be validated/resolved]

---

#### HOLD Concepts (Defer to Later)

| ID | Concept | Viability | Complexity | Risk | Reason |
|----|---------|-----------|-----------|------|--------|
| SC-XX | [Name] | [X/10] | [L/M/H] | [L/M/H] | [Why holding] |

**Total HOLD Concepts:** [X]

**Why Holding:**
[Explanation of reasons for deferring these concepts]

**Reconsideration Criteria:**
[Under what conditions these might be reconsidered]

---

## Risk Summary

### Critical Risks Across All Concepts

**High-Priority Risks:**

| Risk | Affects Concepts | Overall Impact | Mitigation |
|------|-----------------|---------------|------------|
| [Risk 1] | SC-01, SC-03 | High | [Strategy] |
| [Risk 2] | SC-02, SC-04 | Medium | [Strategy] |

### Risk Mitigation Priorities

**Immediate Actions:**
1. [ ] [Action to address critical risk 1]
2. [ ] [Action to address critical risk 2]
3. [ ] [Action to address critical risk 3]

**Validation Needed:**
- [What to validate before committing to concept X]
- [What to test before committing to concept Y]

---

## Dependency Map

### Concept Dependencies

```
SC-01 (Foundation)
  ↓
SC-03 (Depends on SC-01)
  ↓
SC-05 (Depends on SC-01 & SC-03)

SC-02 (Independent)

SC-04 (Depends on SC-02)
```

**Critical Path:**
[Identify the sequence of concepts that must be built in order]

**Parallel Opportunities:**
[Concepts that can be developed simultaneously]

---

## Resource Implications

### Overall Resource Assessment

**Team Composition Needed:**
- [Role 1]: [X people, Y% dedication]
- [Role 2]: [X people, Y% dedication]
- [Role 3]: [X people, Y% dedication]

**Timeline Implications:**
- **MVP Concepts:** [Estimated total time]
- **Stage 2 Concepts:** [Estimated total time]
- **Full Vision:** [Estimated total time]

**Expertise Gaps:**
- [Skill/expertise we need but don't have]
- [How to address: hire, train, partner]

---

## Validation Priorities

### What to Validate First

**Before MVP Commitment:**
1. **[Validation 1]** - For concepts: [SC-XX, SC-XX]
   - **Method:** [How to validate]
   - **Timeline:** [When]
   - **Decision:** [Go/No-Go criteria]

2. **[Validation 2]** - For concepts: [SC-XX]
   - **Method:** [How to validate]
   - **Timeline:** [When]
   - **Decision:** [Go/No-Go criteria]

**During MVP Development:**
- [Continuous validation approach]
- [Metrics to monitor]

---

## Recommendations for Agent 9

### MVP Scope Recommendations

**Strongly Recommend for MVP:**
- **SC-01:** [Name] - [Why critical]
- **SC-02:** [Name] - [Why critical]

**Rationale:**
[Why this set forms minimum viable product]

**Expected MVP Value:**
- [Key benefit 1]
- [Key benefit 2]
- [Key benefit 3]

---

### Stage 2 Recommendations

**Recommend for Stage 2:**
- **SC-03:** [Name] - [Why Stage 2]
- **SC-04:** [Name] - [Why Stage 2]

**Trigger for Stage 2:**
[What needs to be validated in MVP before proceeding]

---

### Deferred Concepts

**Hold Until Later:**
- **SC-XX:** [Name] - [Why defer]

**Reconsider When:**
[Conditions for reconsidering]

---

## Success Criteria

### How to Know Feasibility Assessment Was Effective

**Short-term (Week 1-6):**
- [ ] No major feasibility blockers discovered during MVP development
- [ ] Concepts proceed as assessed (no major scope changes)
- [ ] Risks anticipated and mitigated

**Medium-term (Week 7-12):**
- [ ] GO concepts successfully implemented
- [ ] CONSIDER concepts resolved (Go or No-Go decisions made)
- [ ] Risk mitigation strategies effective

**Long-term (Week 13+):**
- [ ] Feasibility predictions accurate (viability, complexity, risk)
- [ ] Resource estimates reasonably accurate
- [ ] Recommendations led to successful product

---

## Document Information
- **Created By:** Agent 8 - Solution Concept Specialist
- **Date:** [YYYY-MM-DD]
- **Version:** [X.X]
- **Status:** [Draft / In Review / Approved]
- **Last Updated:** [Date]
- **Related Documents:**
  - Solution Concepts: `/2-solution/2c-solution-concepts/solution-concepts.md`
  - Concept Breakdowns: `/2-solution/2c-solution-concepts/2c1-concept-breakdown/`
  - Next Step: `/2-solution/2d-prioritization/mvp-scope.md` (Agent 9)

---

## Template Notes for Agent 8

**When filling this template:**
- Be honest and realistic - better to identify risks now than during development
- This is HIGH-LEVEL feasibility, not detailed technical assessment
- Use evidence from Phase 1 to support viability assessments
- Consider the team's capabilities and constraints
- Think about risk mitigation, not just risk identification
- Viability scores should be justified, not arbitrary
- Complexity and risk should be based on concrete factors
- Recommendations should be clear and actionable for Agent 9

**Remember:**
- This assessment informs MVP scoping (Agent 9)
- Be conservative on risk - easier to scale up than down
- "Consider" is okay - not everything needs to be clear Go/No-Go
- Dependencies matter - can't build everything in parallel
- Resource constraints are real - factor them in
- This is a PROPOSAL assessment for discussion, not final verdict

**Key Questions to Answer:**
1. Can we realistically build this?
2. Is it worth building?
3. Will users actually use it?
4. What are the main risks?
5. What should we build first?

**Output Should Enable Agent 9 to:**
- Prioritize concepts confidently
- Make informed MVP scoping decisions
- Understand risks and how to mitigate them
- Plan phased approach based on dependencies

