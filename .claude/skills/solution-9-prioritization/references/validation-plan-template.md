---
template_name: "Validation Plan Template"
template_version: "1.0.0"
agent: "Agent 9 - Product Prioritization Specialist"
output_location: "/2-solution/2d-prioritization/2d1-mvp/mvp-validation-plan.md"
purpose: "Plan for validating MVP with hypotheses, metrics, and Go/No-Go criteria"
---

# MVP Validation Plan

## Document Metadata
- **Product:** [Name]
- **Created:** [YYYY-MM-DD]
- **Version:** [X.X]
- **Validation Period:** [Start - End Date]

---

## Validation Objectives

The MVP validation plan aims to answer 4 critical questions:

1. **Do users really have this problem?** (Problem validation)
2. **Does our solution solve the problem?** (Solution validation)
3. **Will users adopt and use it?** (Value validation)
4. **Can we build and maintain it?** (Feasibility validation)

---

## Critical Hypotheses

### Hypothesis 1: Problem Exists
**We believe that** [target users] struggle with [specific problem] and it causes [specific pain].

**How to validate:**
- **Method:** User interviews + analytics from MVP usage
- **What to observe:** [Specific behaviors or feedback]

**Success criteria:**
- ✅ 70%+ of users confirm they have this problem
- ✅ Problem occurs frequently (weekly or more)
- ✅ Current workarounds are unsatisfactory

**Failure criteria:**
- ❌ <50% of users recognize the problem
- ❌ Problem is rare (monthly or less)
- → **Action if fails:** Pivot to different problem

---

### Hypothesis 2: Solution Works
**We believe that** [our solution/feature] will reduce/eliminate [problem] for [target users].

**How to validate:**
- **Method:** Task success testing + before/after metrics
- **What to measure:** [Specific metrics]

**Success criteria:**
- ✅ Task success rate >= 80%
- ✅ Time to complete task reduced by 50%+
- ✅ User satisfaction score >= 7/10

**Failure criteria:**
- ❌ Task success rate < 60%
- ❌ No measurable improvement
- → **Action if fails:** Iterate on solution design

---

### Hypothesis 3: Users Will Adopt
**We believe that** [X%] of [target users] will actively use [solution] at least [frequency].

**How to validate:**
- **Method:** Adoption and retention analytics
- **What to measure:** [Specific metrics]

**Success criteria:**
- ✅ 30%+ of invited users try MVP within 2 weeks
- ✅ 50%+ of trial users return for 2nd use
- ✅ Average [X] uses per week per active user

**Failure criteria:**
- ❌ <15% trial rate
- ❌ <25% retention
- → **Action if fails:** Investigate onboarding and value prop

---

### Hypothesis 4: Technically Feasible
**We believe that** we can build and maintain [solution] with [constraints].

**How to validate:**
- **Method:** Technical spikes, prototype testing
- **What to measure:** Performance, stability, effort

**Success criteria:**
- ✅ Performance meets requirements (response time, load)
- ✅ Stable operation (>99% uptime)
- ✅ Maintainable by team (reasonable complexity)

**Failure criteria:**
- ❌ Can't meet performance requirements
- ❌ Too complex to maintain
- → **Action if fails:** Simplify solution or change approach

---

## Success Metrics

### Adoption Metrics
| Metric | Baseline | Week 2 | Week 4 | Week 6 | Target |
|--------|----------|--------|--------|--------|--------|
| Users invited | - | 50 | 100 | 200 | - |
| Trial rate (%) | - | 30% | 35% | 40% | >30% |
| Active users | - | 15 | 35 | 80 | >50 |
| Retention (%) | - | 60% | 55% | 50% | >50% |

### Experience Metrics
| Metric | Current | Week 2 | Week 4 | Week 6 | Target |
|--------|---------|--------|--------|--------|--------|
| User satisfaction | 4.2/10 | - | TBD | TBD | 7.5/10 |
| Task success rate | 60% | 70% | 75% | 80% | >80% |
| Time on task | 45min | 20min | 15min | 12min | <15min |

### Business Metrics
| Metric | Current | Week 2 | Week 4 | Week 6 | Target |
|--------|---------|--------|--------|--------|--------|
| [Key metric] | [Value] | TBD | TBD | TBD | [Target] |
| [Impact metric] | [Value] | TBD | TBD | TBD | [Target] |

---

## Validation Phases

### Phase 1: Alpha Testing (Week 1-2)
**Participants:** 5-10 internal users or early adopters

**Goals:**
- Validate core functionality works
- Identify major usability issues
- Test hypothesis 2 (solution works)

**Activities:**
- Guided task testing
- Think-aloud sessions
- Bug identification

**Success criteria:**
- All P0 features functional
- Task success rate >60%
- No critical bugs

---

### Phase 2: Beta Testing (Week 3-4)
**Participants:** 50-100 target users

**Goals:**
- Test hypothesis 1 (problem exists) and 3 (will adopt)
- Collect quantitative usage data
- Gather qualitative feedback

**Activities:**
- Open access to MVP
- Analytics tracking
- User surveys and interviews

**Success criteria:**
- 30%+ trial rate
- 50%+ retention
- NPS >20

---

### Phase 3: Validation & Iteration (Week 5-6)
**Participants:** Expanded user base (100-200)

**Goals:**
- Validate all hypotheses with larger sample
- Test scalability (hypothesis 4)
- Refine based on feedback

**Activities:**
- Broader rollout
- A/B testing of variations
- Performance monitoring

**Success criteria:**
- All success metrics hit targets
- No major technical issues
- Clear path to Stage 2

---

## Go/No-Go Decision (End of Week 6)

### GO Criteria (Proceed to Stage 2)
- ✅ Problem validation: >70% confirm problem
- ✅ Solution validation: Task success >80%
- ✅ Adoption validation: >30% trial, >50% retention
- ✅ Feasibility validation: Stable, performant
- ✅ User satisfaction: NPS >30

### NO-GO Criteria (Pivot or Stop)
- ❌ Any critical hypothesis failed
- ❌ <50% of success metrics achieved
- ❌ Major technical blockers discovered
- ❌ User feedback overwhelmingly negative

### ITERATE Criteria (Middle Ground)
- ⚠️ Some hypotheses validated, others not
- ⚠️ 50-70% of success metrics achieved
- → **Action:** Run extended validation (2-4 more weeks) with iterations

---

## Iteration Plan

**If metrics below target:**

1. **Low trial rate (<30%):**
   - Action: Improve onboarding, clarify value prop
   - Retest: Week 7-8

2. **Low retention (<50%):**
   - Action: Interview churned users, improve core value delivery
   - Retest: Week 7-8

3. **Low task success (<80%):**
   - Action: Simplify UI, improve UX, add guidance
   - Retest: Week 7-8

4. **Low satisfaction (NPS <30):**
   - Action: Identify and fix top complaints
   - Retest: Week 7-8

---

## Feedback Collection

### Quantitative
- **Analytics:** User behavior, feature usage, conversion funnels
- **Performance:** Load times, error rates, completion rates
- **Surveys:** NPS, CSAT, feature ratings

### Qualitative
- **Interviews:** 10-15 users (mix of active and churned)
- **Support tickets:** Track issues and requests
- **Session recordings:** Observe usage patterns

### Continuous
- **In-app feedback:** Simple feedback widget
- **Feature requests:** Capture and prioritize
- **Bug reports:** Track and fix

---

## Next Steps After Validation

### If GO Decision:
1. Celebrate! 🎉
2. Document learnings
3. Plan Stage 2 features
4. Handoff to Agent 10 for communication

### If NO-GO Decision:
1. Analyze what went wrong
2. Decide: Pivot, Persevere, or Pause
3. Document learnings
4. If pivot: Return to problem space
5. If stop: Communicate decision and rationale

### If ITERATE Decision:
1. Prioritize iterations based on data
2. Run focused experiments
3. Revalidate in 2-4 weeks
4. Make final GO/NO-GO decision

---

## Document Information
- **Created By:** Agent 9
- **Date:** [YYYY-MM-DD]
- **Version:** [X.X]
- **Status:** [Draft / Approved]

