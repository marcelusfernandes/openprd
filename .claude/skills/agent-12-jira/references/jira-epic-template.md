# Jira Epic Template

## Purpose
Template para estruturar Jira Epics com contexto claro, valor definido e stories organizadas.

## Epic Structure

```markdown
# Epic: [Epic Name]

## Basic Information

**Epic Key:** [PROJ-E-XXX]
**Epic Name:** [Short, descriptive name]
**Initiative:** [PROJ-INIT] - [Initiative Name]
**Status:** Planning / In Progress / Done / Cancelled
**Priority:** Highest / High / Medium / Low
**Phase:** MVP / Stage 2 / Stage 3
**Target Sprint:** Sprint X-Y
**Owner:** [Product Manager or Tech Lead]

---

## Summary

[One sentence describing what this Epic delivers]

Example: 
"Unified Event Dashboard provides a single source of truth for all event information, eliminating tool fragmentation and reducing coordination time."

---

## Epic Description

### What This Is

[2-3 paragraphs describing:
- What this Epic builds
- Problem it solves
- Value it delivers
- How it fits in the larger product]

Example:
This Epic delivers a unified event dashboard that consolidates event information from multiple sources into a single, real-time view. Currently, HR teams managing Golden Thursdays events must manually check 5 different tools (email, calendar, spreadsheets, Slack, and form responses) to get a complete picture of event status, spending 2-3 hours per day on coordination alone.

The dashboard will automatically sync data from all sources, providing instant visibility into participant status, venue availability, budget tracking, and communication history. This eliminates manual data gathering and enables the team to focus on event experience rather than coordination logistics.

By centralizing event data, we reduce coordination time by 70% and eliminate the errors that occur when working with scattered, outdated information across multiple tools.

### Concept Origin

**Source Concept:** [Name of solution concept from Agent 8]
**Concept Description:** [Brief description]
**Related Journey Stage:** [Journey stage this improves]

---

## Problem Solved

### User Pain Points Addressed

1. **[Pain Point 1]**
   - Current: [How users struggle today]
   - After: [How this Epic solves it]
   
2. **[Pain Point 2]**
   - Current: [How users struggle today]
   - After: [How this Epic solves it]

3. **[Pain Point 3]**
   - Current: [How users struggle today]
   - After: [How this Epic solves it]

### Current vs Future State

| Aspect | Current State | With This Epic |
|--------|---------------|----------------|
| Time spent | 8-10 hours per event | 1-2 hours per event |
| Data accuracy | 75% (errors common) | 98% (automated sync) |
| Tool switching | 5 different tools | Single dashboard |
| Real-time visibility | None | Complete |
| User satisfaction | 4.2/10 | Target: 7.5/10 |

---

## Epic Goal

**Measurable Goal:**
[Specific, measurable outcome this Epic achieves]

Example:
"HR event coordinators can view complete event status, participant lists, and communication history in under 30 seconds, with 98%+ data accuracy, reducing event coordination time from 8 hours to 1.5 hours per event."

---

## Acceptance Criteria (Epic Level)

High-level criteria for Epic completion:

- [ ] **[Criteria 1]:** [Observable outcome]
  - Measured by: [How to verify]

- [ ] **[Criteria 2]:** [Observable outcome]
  - Measured by: [How to verify]

- [ ] **[Criteria 3]:** [Observable outcome]
  - Measured by: [How to verify]

- [ ] **[Criteria 4]:** [Observable outcome]
  - Measured by: [How to verify]

- [ ] **[Criteria 5]:** [Observable outcome]
  - Measured by: [How to verify]

Example:
- [ ] **Dashboard displays real-time event data** from all 5 integrated sources
  - Measured by: Data sync latency <1 minute, 98%+ accuracy
  
- [ ] **Users can complete core tasks within dashboard** without tool switching
  - Measured by: 80%+ of coordination tasks completable in-dashboard

- [ ] **Coordination time reduced significantly**
  - Measured by: User testing shows <2 hour average (vs 8 hours baseline)

- [ ] **User satisfaction improves**
  - Measured by: NPS >30, task success rate >85%

- [ ] **Dashboard is stable and performant**
  - Measured by: <2 sec load time, >99% uptime, <5 support tickets/month

---

## Stories

**Total Stories:** [X]
**Total Story Points:** [XX]
**Status:** [X Done / Y In Progress / Z To Do]

### P0 Stories (Critical)

- [ ] **[PROJ-001]:** [Story title] (5 points) - Sprint X
- [ ] **[PROJ-002]:** [Story title] (3 points) - Sprint X
- [ ] **[PROJ-003]:** [Story title] (8 points) - Sprint X+1

### P1 Stories (High)

- [ ] **[PROJ-004]:** [Story title] (5 points) - Sprint X+1
- [ ] **[PROJ-005]:** [Story title] (3 points) - Sprint X+1
- [ ] **[PROJ-006]:** [Story title] (2 points) - Sprint X+2

### P2 Stories (Medium - Optional)

- [ ] **[PROJ-007]:** [Story title] (3 points) - Sprint X+2
- [ ] **[PROJ-008]:** [Story title] (5 points) - Backlog

---

## Dependencies

### Blocks (This Epic blocks:)
- **[PROJ-E-XXX]:** [Epic Name]
  - Reason: [Why dependency exists]
  - Impact if delayed: [Consequence]

### Blocked By (This Epic is blocked by:)
- **[PROJ-E-XXX]:** [Epic Name]
  - Reason: [Why dependency exists]
  - Mitigation: [Plan if blocker delayed]

### Related (Related but not blocking:)
- **[PROJ-E-XXX]:** [Epic Name]
  - Relationship: [How they relate]

---

## Technical Considerations

### Technical Approach
[High-level technical strategy - 2-3 sentences]

### Key Technical Challenges
1. **[Challenge 1]:** [Description]
   - Solution: [Approach]
   
2. **[Challenge 2]:** [Description]
   - Solution: [Approach]

### Integration Points
- [System/API 1]: [What's needed]
- [System/API 2]: [What's needed]
- [System/API 3]: [What's needed]

### Performance Requirements
- Load time: [Target]
- Response time: [Target]
- Uptime: [Target]
- Concurrent users: [Target]

---

## User Experience

### Target Users
**Primary:** [User persona 1]
**Secondary:** [User persona 2]

### Key User Flows
1. **[Flow 1]:** [User does X to accomplish Y]
2. **[Flow 2]:** [User does X to accomplish Y]
3. **[Flow 3]:** [User does X to accomplish Y]

### UX Requirements
- [Requirement 1]: [Description]
- [Requirement 2]: [Description]
- [Requirement 3]: [Description]

---

## Success Metrics

### Quantitative Metrics

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| Time on task | 8 hours | 1.5 hours | Time tracking |
| Task success rate | 60% | 85% | User testing |
| Error rate | 25% | <5% | Analytics |
| User adoption | N/A | 70% | Analytics |

### Qualitative Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| User satisfaction | >7.5/10 | Survey |
| NPS | >30 | Survey |
| Task difficulty | "Easy" or "Very Easy" | User testing |

### Validation Approach
[How we'll validate this Epic delivers value - 1-2 sentences]

---

## Risks & Mitigation

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 3] | High/Med/Low | High/Med/Low | [Strategy] |

---

## Timeline & Milestones

### Sprint Allocation

| Sprint | Stories | Story Points | Status |
|--------|---------|--------------|--------|
| Sprint X | [Story IDs] | XX points | Planned |
| Sprint X+1 | [Story IDs] | XX points | Planned |
| Sprint X+2 | [Story IDs] | XX points | Planned |

### Key Milestones

- **[Date]:** Design complete, stories refined
- **[Date]:** Core functionality (P0 stories) complete
- **[Date]:** All features (P0+P1) complete  
- **[Date]:** Testing and validation complete
- **[Date]:** Epic complete, ready for release

---

## Related Resources

### Documentation
- [Design Mockups](link)
- [Technical Spec](link)
- [User Research](link)
- [Confluence Page](link)

### Related Jira Items
- Initiative: [PROJ-INIT]
- Related Epics: [Links]
- Dependent Stories: [Links]

---

## Notes & Updates

### Recent Updates
- [Date]: [Update]
- [Date]: [Update]

### Decisions Made
- [Date]: **[Decision]** - [Rationale]
- [Date]: **[Decision]** - [Rationale]

### Open Questions
- [ ] [Question] - Owner: [Name] - Due: [Date]
- [ ] [Question] - Owner: [Name] - Due: [Date]

---

## Labels

Epic labels for organization and filtering:

- Phase: `MVP` / `Stage2` / `Stage3`
- Priority: `P0` / `P1` / `P2` / `P3`
- Component: `Frontend` / `Backend` / `Integration` / `Design`
- Journey Stage: `[Stage name from journey map]`
- Feature Area: `[Dashboard/Communication/Analytics/etc]`

---

## Document Metadata

**Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]
**Version:** [1.0]
**Owner:** [Name]
**Status:** [Draft / Active / Complete]
```

## Epic Writing Best Practices

### Characteristics of Good Epics

✅ **Clear Value:** Obvious why this matters to users
✅ **Right Size:** 3-15 stories, completable in 2-6 sprints
✅ **Focused:** Single concept or feature area
✅ **Measurable:** Clear success criteria
✅ **Independent:** Minimal dependencies on other Epics

### Common Epic Mistakes

❌ **Too Large:** >20 stories, spans quarters (break into multiple Epics)
❌ **Too Small:** 1-2 stories (just make them stories)
❌ **Vague:** Unclear what "done" means
❌ **Technical focus:** Describes implementation not user value
❌ **No success metrics:** Can't validate if it worked

### Epic vs Story

| Epic | Story |
|------|-------|
| Feature set | Single feature |
| Weeks/months | Days |
| Multiple stories | Atomic work |
| Product/user value | Technical task |
| High-level acceptance | Detailed acceptance |

## Example Filled Template

```markdown
# Epic: Unified Event Dashboard

## Basic Information

**Epic Key:** PROJ-E-001
**Epic Name:** Unified Event Dashboard
**Initiative:** PROJ-INIT - Stella Golden Thursdays Platform
**Status:** In Progress
**Priority:** Highest
**Phase:** MVP
**Target Sprint:** Sprint 1-3
**Owner:** Maria Silva (PM)

---

## Summary

Unified Event Dashboard provides a single source of truth for all Golden Thursdays event information, eliminating tool fragmentation and reducing coordination time by 70%.

---

## Epic Description

### What This Is

This Epic delivers a unified event dashboard that consolidates event information from multiple sources into a single, real-time view. Currently, HR teams managing Golden Thursdays events must manually check 5 different tools (email, calendar, Google Sheets, Slack, and Google Forms) to get a complete picture of event status, spending 8-10 hours per event on coordination alone.

The dashboard will automatically sync data from all sources, providing instant visibility into participant status, venue availability, budget tracking, and communication history. This eliminates manual data gathering and enables the team to focus on event experience rather than coordination logistics.

By centralizing event data, we reduce coordination time from 8 hours to 1.5 hours per event and eliminate the 25% error rate that occurs when working with scattered, outdated information.

### Concept Origin

**Source Concept:** Integrated Event Management Platform
**Concept Description:** Digital platform that unifies all event planning tools
**Related Journey Stage:** Stage 2 - Strategic Planning & Stage 3 - Pre-Event Coordination

---

## Problem Solved

### User Pain Points Addressed

1. **Tool Fragmentation**
   - Current: Check 5 different tools to get complete event picture
   - After: Single dashboard with all information unified

2. **Manual Data Sync**
   - Current: Copy-paste between tools, high error rate (25%)
   - After: Automatic sync, 98%+ accuracy

3. **No Real-Time Visibility**
   - Current: Information outdated as soon as compiled
   - After: Real-time updates, always current

### Current vs Future State

| Aspect | Current State | With This Epic |
|--------|---------------|----------------|
| Time spent | 8-10 hours per event | 1.5 hours per event |
| Data accuracy | 75% | 98% |
| Tool switching | 5 different tools | Single dashboard |
| Real-time visibility | None | Complete |
| User satisfaction | 4.2/10 | Target: 7.5/10 |

---

## Epic Goal

HR event coordinators can view complete event status, participant lists, venue information, budget, and communication history in under 30 seconds with 98%+ data accuracy, reducing event coordination time from 8 hours to 1.5 hours per event.

---

## Acceptance Criteria (Epic Level)

- [ ] **Dashboard displays real-time event data** from all 5 integrated sources
  - Measured by: Data sync latency <1 minute, 98%+ accuracy verified in testing

- [ ] **Users can complete 80%+ of coordination tasks within dashboard**
  - Measured by: User testing shows 8 of 10 common tasks completable without leaving dashboard

- [ ] **Coordination time reduced to <2 hours per event**
  - Measured by: Time tracking with 5 beta users over 3 events each

- [ ] **User satisfaction score >7.5/10**
  - Measured by: Post-event surveys, NPS >30

- [ ] **Dashboard is stable and performant**
  - Measured by: <2 sec load time, >99% uptime, <5 support tickets per month

---

## Stories

**Total Stories:** 8
**Total Story Points:** 34
**Status:** 3 Done / 2 In Progress / 3 To Do

### P0 Stories (Critical)

- [x] **PROJ-001:** Create event dashboard UI framework (5 points) - Sprint 1 ✅
- [x] **PROJ-002:** Integrate Google Calendar API (3 points) - Sprint 1 ✅
- [ ] **PROJ-003:** Integrate participant data from Forms (5 points) - Sprint 2 🔄

### P1 Stories (High)

- [ ] **PROJ-004:** Add real-time sync engine (8 points) - Sprint 2
- [ ] **PROJ-005:** Build event overview cards (3 points) - Sprint 2
- [ ] **PROJ-006:** Add participant list view (5 points) - Sprint 3
- [ ] **PROJ-007:** Implement communication history (3 points) - Sprint 3

### P2 Stories (Medium - Nice to Have)

- [ ] **PROJ-008:** Add data export functionality (2 points) - Sprint 3 or defer

---

## Dependencies

### Blocks (This Epic blocks:)
- **PROJ-E-002:** Smart Participant Management
  - Reason: Dashboard data model needed for participant features
  - Impact if delayed: Stage 2 timeline at risk

### Blocked By (This Epic is blocked by:)
- None - Critical path Epic

### Related (Related but not blocking:)
- **PROJ-E-003:** Automated Communication Engine
  - Relationship: Uses same event data model

---

## Technical Considerations

### Technical Approach
React-based dashboard with real-time WebSocket updates, REST API integration layer for external services, PostgreSQL for unified data model.

### Key Technical Challenges

1. **Real-time data sync across 5 sources**
   - Solution: Event-driven architecture with sync queue

2. **Handling API rate limits**
   - Solution: Intelligent caching, batch updates where possible

3. **Data consistency across sources**
   - Solution: Single source of truth in our DB, conflict resolution rules

### Integration Points
- Google Calendar API: Read events, availability
- Google Forms API: Read participant responses
- Slack API: Read/write messages, notifications
- Internal HR System: Read employee data
- Email API: Read/send event communications

### Performance Requirements
- Load time: <2 seconds initial load
- Response time: <500ms for interactions
- Uptime: >99%
- Concurrent users: Support 50 simultaneous users

---

## Success Metrics

### Quantitative Metrics

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| Coordination time | 8 hours | 1.5 hours | Time tracking (5 users, 3 events) |
| Task success rate | 60% | 85% | User testing (10 tasks, 5 users) |
| Data accuracy | 75% | 98% | Comparison with source systems |
| Dashboard adoption | 0% | 70% | Analytics (MAU / Target Users) |

### Qualitative Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| User satisfaction | >7.5/10 | Post-event survey |
| NPS | >30 | In-app NPS survey |
| Task difficulty | "Easy" rating | User testing feedback |

---

## Timeline & Milestones

### Sprint Allocation

| Sprint | Stories | Story Points | Status |
|--------|---------|--------------|--------|
| Sprint 1 | PROJ-001, 002 | 8 points | ✅ Complete |
| Sprint 2 | PROJ-003, 004, 005 | 16 points | 🔄 In Progress |
| Sprint 3 | PROJ-006, 007, 008 | 10 points | ⚪ Planned |

### Key Milestones

- **2025-11-05:** Design complete, all stories refined ✅
- **2025-11-15:** Core UI and first integration complete ✅
- **2025-11-25:** All integrations complete (target)
- **2025-12-02:** Testing and validation complete (target)
- **2025-12-06:** Epic complete, ready for beta (target)

---

**Created:** 2025-10-27
**Last Updated:** 2025-11-14
**Owner:** Maria Silva (PM)
**Status:** Active
```

---

This template ensures Epics provide complete context for implementation teams while maintaining focus on user value.

