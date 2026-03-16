# Jira Story Template

## Purpose
Template para estruturar Jira Stories com user story format, acceptance criteria claros e todos os campos necessários para desenvolvimento.

## Story Structure

```markdown
# Story: [Story ID] - [Short Title]

## Basic Information

**Story ID:** [PROJ-XXX]
**Story Type:** Story / Task / Bug / Technical Debt
**Status:** To Do / In Progress / In Review / Done
**Priority:** Highest / High / Medium / Low
**Story Points:** [1/2/3/5/8/13]
**Sprint:** Sprint X
**Assignee:** [Developer Name]
**Reporter:** [Product Manager Name]
**Created:** [YYYY-MM-DD]
**Updated:** [YYYY-MM-DD]

---

## Epic Link

**Epic:** [PROJ-E-XXX] - [Epic Name]
**Initiative:** [PROJ-INIT] - [Initiative Name]

---

## User Story

```
As a [specific user persona],
I want [specific, actionable goal],
So that [clear benefit/value].
```

### Example - Good Story:
```
As a HR Manager organizing Golden Thursdays events,
I want to view all participant registrations in a single dashboard,
So that I can quickly understand attendance without checking multiple tools.
```

### Example - Bad Story:
```
As a user,
I want a dashboard,
So that I can see data.
```

---

## Description

### Context

[1-2 paragraphs providing context:
- What is the current situation
- Why this story is needed now
- How it fits into the larger feature/epic]

Example:
Currently, HR managers must check Google Forms responses, cross-reference with employee database, check calendar availability, and verify in Slack channels to understand who has registered for an event. This manual process takes 30-45 minutes and is error-prone, leading to inaccurate participant counts and missed registrations.

This story delivers a unified participant view that automatically syncs all registration sources into a single list, showing real-time status, dietary restrictions, and confirmation status. This is the first core feature of the Unified Event Dashboard and unblocks other participant management features.

### What We're Building

[Specific description of what this story delivers - 2-3 sentences]

Example:
A participant list view that displays all registered attendees for an event, including:
- Name, department, and contact info (from HR system)
- Registration timestamp and source (Google Forms)
- Confirmation status (confirmed/pending/declined)
- Dietary restrictions and accessibility needs
- Real-time sync with data updates every 60 seconds

### User Value

[Why this matters to the user - 1-2 sentences]

Example:
Eliminates 30-45 minutes of manual data gathering per event and ensures 100% accurate participant counts for planning purposes.

---

## Acceptance Criteria

Specific, testable criteria that define "done":

### Functional Criteria

- [ ] **[Criteria 1]:** [Specific, observable outcome]
  - Given [precondition]
  - When [action]
  - Then [expected result]

- [ ] **[Criteria 2]:** [Specific, observable outcome]
  - Given [precondition]
  - When [action]
  - Then [expected result]

- [ ] **[Criteria 3]:** [Specific, observable outcome]
  - Given [precondition]
  - When [action]
  - Then [expected result]

### Non-Functional Criteria

- [ ] **Performance:** [Specific requirement]
- [ ] **Accessibility:** [Specific requirement]
- [ ] **Error Handling:** [Specific requirement]
- [ ] **Testing:** [Specific requirement]

### Example - Complete Acceptance Criteria:

- [ ] **Participant list displays all registered attendees**
  - Given: An event has 50 registered participants
  - When: Manager opens the event dashboard
  - Then: All 50 participants are visible in the list with complete information

- [ ] **List shows real-time registration status**
  - Given: A new participant registers
  - When: Registration completes in Google Forms
  - Then: Participant appears in dashboard within 60 seconds

- [ ] **Manager can filter participants**
  - Given: List has 50 participants with various statuses
  - When: Manager applies "Confirmed only" filter
  - Then: Only confirmed participants are shown

- [ ] **Performance: List loads quickly**
  - Load time <1 second for up to 200 participants

- [ ] **Accessibility: List is keyboard navigable**
  - All interactions possible via keyboard only

- [ ] **Error Handling: Sync failures are visible**
  - If sync fails, user sees clear error message and retry option

- [ ] **Testing: Unit tests cover core logic**
  - >80% code coverage, all happy and error paths tested

---

## Technical Details

### Implementation Notes

[Technical approach or considerations - 3-5 bullets]

Example:
- Use React Table component for list rendering
- WebSocket connection for real-time updates
- REST API endpoint: GET /api/events/{eventId}/participants
- Cache participant data in Redux store
- Implement virtual scrolling for >100 participants

### API/Data Requirements

**Endpoints:**
- `GET /api/events/{eventId}/participants` - Fetch participant list
- `WS /ws/events/{eventId}` - Real-time updates

**Data Model:**
```
Participant {
  id: string
  eventId: string
  name: string
  email: string
  department: string
  registeredAt: timestamp
  status: "confirmed" | "pending" | "declined"
  dietaryRestrictions: string[]
  accessibilityNeeds: string
  source: "google_forms" | "hr_system" | "manual"
}
```

### Dependencies (Technical)

- Requires: Participant API endpoint (PROJ-002)
- Blocks: Participant filtering feature (PROJ-007)
- Related: Real-time sync engine (PROJ-004)

---

## Design/UX

### Design Assets
- [Link to Figma mockup]
- [Link to design spec]

### User Flow
1. User navigates to event dashboard
2. User clicks on "Participants" tab
3. System loads and displays participant list
4. User can scroll, filter, and export data

### UI Components
- ParticipantList component
- ParticipantCard component
- FilterBar component
- ExportButton component

### Edge Cases to Handle
- Empty state (no participants yet)
- Loading state (data fetching)
- Error state (sync failure)
- Large list (>200 participants)

---

## Test Scenarios

### Happy Path
1. **View participant list**
   - Open event with participants
   - Verify all expected participants shown
   - Verify data accuracy

2. **Real-time update**
   - Have participant register while viewing list
   - Verify new participant appears within 60 sec

### Edge Cases
3. **Empty participant list**
   - View event with no participants
   - Verify helpful empty state message

4. **Large participant list**
   - View event with 200+ participants
   - Verify list renders smoothly, scrolling works

### Error Cases
5. **Sync failure**
   - Simulate API failure
   - Verify error message shown
   - Verify retry mechanism works

6. **Network offline**
   - Go offline while viewing list
   - Verify cached data still visible
   - Verify sync resumes when online

---

## Definition of Done Checklist

- [ ] Code written and peer reviewed
- [ ] All acceptance criteria met
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests passing
- [ ] Manual testing completed
- [ ] No critical or high bugs
- [ ] Design review approved (if UI changes)
- [ ] Accessibility requirements met (WCAG AA)
- [ ] Performance requirements met
- [ ] Documentation updated (if needed)
- [ ] Deployed to staging environment
- [ ] Product Owner acceptance

---

## Dependencies & Relationships

### Depends On (Blocked By):
- **[PROJ-002]:** Integrate participant data from Forms (5 points)
  - Reason: Need API endpoint for participant data
  - Status: In Progress
  - ETA: Sprint 2

### Blocks:
- **[PROJ-007]:** Implement participant filtering (3 points)
  - Reason: Needs base list component

### Related Stories:
- **[PROJ-005]:** Build event overview cards
  - Relationship: Uses same data model

---

## Estimation

### Story Points: 5

**Breakdown:**
- Frontend component: 2 points
- API integration: 1 point
- Real-time sync: 1 point
- Testing & edge cases: 1 point

**Assumptions:**
- API endpoint available
- Design mockups complete
- No major technical unknowns

**Risks:**
- Real-time sync complexity may increase scope
- Large list performance may need optimization

---

## Labels & Tags

**Labels:**
- `MVP` - Part of MVP scope
- `Frontend` - Frontend work
- `P0` - Critical priority
- `Stage2-Strategic-Planning` - Improves this journey stage
- `Dashboard` - Feature area

**Component:** Dashboard
**Journey Stage:** Stage 2 - Strategic Planning
**Feature Area:** Participant Management

---

## Source Information

**Original Feature:** F-006 from MVP Features (Agent 9)
**Feature ID:** F-006
**Impact Score:** 5/5 (Critical)
**Effort Score:** 3/5 (Medium)
**Priority Score:** 1.67 → P0

**From Product Brief:**
"Participant management is one of the top 3 pain points, affecting 100% of event organizers and consuming 30-45 minutes per event in manual coordination."

---

## Comments & Discussion

### Questions:
- [ ] Do we need to show participants who declined registration?
  - **Answer:** Yes, for tracking purposes. Add filter to hide if needed.
  
- [ ] What happens if HR system API is down?
  - **Answer:** Show cached data with warning banner. Log error for monitoring.

### Decisions:
- **2025-11-10:** Decided to implement virtual scrolling for performance
  - Rationale: Some events have 200+ participants
  - Alternative considered: Pagination (rejected - worse UX)

### Notes:
- Consider adding bulk actions (select all, export) in future story
- Real-time sync may benefit from WebSocket connection reuse

---

## Timeline

**Created:** 2025-10-27
**Started:** 2025-11-15
**In Review:** [Date]
**Completed:** [Date]

**Time Spent:** [Hours]
**Original Estimate:** [Hours]

---

## Document Metadata

**Created By:** Maria Silva (PM)
**Assigned To:** João Santos (Frontend Dev)
**Reviewed By:** [Tech Lead Name]
**Sprint:** Sprint 3
**Status:** In Progress
**Last Updated:** 2025-11-16
```

## Story Writing Best Practices

### INVEST Principles

A good story is:
- **I**ndependent: Can be developed separately
- **N**egotiable: Details can be discussed
- **V**aluable: Delivers user value
- **E**stimable: Team can estimate effort
- **S**mall: Completable in one sprint
- **T**estable: Clear acceptance criteria

### User Story Format

✅ **Good Format:**
```
As a [specific persona with context],
I want [specific, actionable goal],
So that [clear, measurable benefit].
```

❌ **Bad Format:**
```
As a user,
I want features,
So that it's better.
```

### Acceptance Criteria

✅ **Good Criteria:**
- Specific and measurable
- Testable (can verify pass/fail)
- Includes edge cases
- Covers non-functional requirements
- Uses Given-When-Then format when helpful

❌ **Bad Criteria:**
- Vague ("works well", "user-friendly")
- Not testable
- Missing edge cases
- Only happy path

### Story Sizing

**1-2 Points (Simple):**
- Clear requirements
- Well-understood technology
- Minimal dependencies
- 1-2 days work

**3 Points (Standard):**
- Moderate complexity
- Some unknowns
- Few dependencies
- 3-4 days work

**5 Points (Complex):**
- Significant complexity
- Multiple components
- Several dependencies
- 5-8 days work

**8 Points (Very Complex):**
- High complexity
- Many unknowns
- Complex dependencies
- 8-10 days work
- Consider splitting

**13 Points (Too Large):**
- Should be split into smaller stories
- Or promoted to Epic

### Common Mistakes

❌ **Technical Jargon in User Story:**
"As a user, I want RESTful API integration..."
✅ Better: "As a user, I want to see real-time data..."

❌ **No Clear Value:**
"As a user, I want a button..."
✅ Better: "As a user, I want to save my work so I don't lose progress..."

❌ **Too Large:**
Story with 13+ points, touches 5+ files
✅ Better: Split into 2-3 smaller, focused stories

❌ **Missing Acceptance Criteria:**
Only has "Implement feature X"
✅ Better: 5-7 specific, testable criteria

❌ **Vague Requirements:**
"Make it user-friendly"
✅ Better: "Task completion time <2 minutes, 0 errors in testing"

## Story vs Task vs Bug

### Story
- Delivers user value
- Written from user perspective
- Has user story format
- Part of Epic

### Task
- Technical work with no direct user value
- Written from team perspective
- Examples: Setup CI/CD, Refactor code, Write docs
- Often standalone

### Bug
- Fixes broken functionality
- Describes what's wrong and expected behavior
- Has steps to reproduce
- Priority based on severity

## Example: Complete Filled Story

```markdown
# Story: PROJ-006 - Add Participant List View

## Basic Information

**Story ID:** PROJ-006
**Story Type:** Story
**Status:** In Progress
**Priority:** Highest
**Story Points:** 5
**Sprint:** Sprint 3
**Assignee:** João Santos
**Reporter:** Maria Silva
**Created:** 2025-10-27
**Updated:** 2025-11-16

---

## Epic Link

**Epic:** PROJ-E-001 - Unified Event Dashboard
**Initiative:** PROJ-INIT - Stella Golden Thursdays Platform

---

## User Story

```
As a HR Manager organizing Golden Thursdays events,
I want to view all participant registrations in a single dashboard list,
So that I can quickly understand attendance status without checking multiple tools.
```

---

## Description

### Context

Currently, HR managers must check Google Forms responses, cross-reference with the employee database, verify calendar availability, and check Slack channels to understand who has registered for an event. This manual process takes 30-45 minutes per event and is error-prone, leading to inaccurate participant counts (25% error rate) and missed registrations.

This story delivers a unified participant view that automatically syncs all registration sources into a single, real-time list. This is the first core feature of the Unified Event Dashboard and unblocks participant management features in PROJ-007.

### What We're Building

A participant list view that displays all registered attendees for an event with:
- Complete participant info (name, department, contact from HR system)
- Registration details (timestamp, source, confirmation status)
- Special needs (dietary restrictions, accessibility requirements)
- Real-time sync with 60-second refresh

### User Value

Eliminates 30-45 minutes of manual coordination per event and ensures 100% accurate participant tracking for better event planning.

---

## Acceptance Criteria

### Functional Criteria

- [ ] **Participant list displays all registered attendees**
  - Given: An event has 50 registered participants
  - When: Manager opens the event dashboard
  - Then: All 50 participants visible with name, dept, status, registration date

- [ ] **List shows real-time registration updates**
  - Given: A new participant registers via Google Forms
  - When: Registration completes
  - Then: New participant appears in list within 60 seconds

- [ ] **List displays participant status**
  - Given: Participants have different statuses (confirmed/pending/declined)
  - When: Manager views list
  - Then: Status clearly indicated with color coding (green/yellow/red)

- [ ] **Manager can search participants**
  - Given: List has 50+ participants
  - When: Manager types name in search box
  - Then: List filters to matching participants in real-time

- [ ] **Empty state handled gracefully**
  - Given: Event has no participants yet
  - When: Manager opens participant list
  - Then: Helpful message shown: "No registrations yet. Share the event link to get started."

### Non-Functional Criteria

- [ ] **Performance: List loads in <1 second** for up to 200 participants
- [ ] **Accessibility: Keyboard navigation works** - can navigate entire list via keyboard
- [ ] **Error Handling: Sync failures shown** - clear error message if data sync fails
- [ ] **Testing: >80% code coverage** - unit tests for all components and logic

---

## Technical Details

### Implementation Notes

- Use React Table v8 for list rendering (supports virtual scrolling)
- WebSocket connection for real-time updates (reuse existing WS from PROJ-004)
- REST API: GET /api/events/{eventId}/participants
- Redux store for client-side caching
- Implement virtual scrolling for lists >100 participants

### API/Data Requirements

**Endpoints:**
- `GET /api/events/{eventId}/participants` - Fetch participants
- `WS /ws/events/{eventId}` - Subscribe to real-time updates

**Data Model:**
```typescript
interface Participant {
  id: string;
  eventId: string;
  name: string;
  email: string;
  department: string;
  registeredAt: Date;
  status: 'confirmed' | 'pending' | 'declined';
  dietaryRestrictions: string[];
  accessibilityNeeds: string;
  source: 'google_forms' | 'hr_system' | 'manual';
}
```

### Dependencies (Technical)

- Requires: Participant API (PROJ-003) - In Progress, ETA Sprint 2
- Requires: Real-time sync engine (PROJ-004) - Sprint 2
- Blocks: Participant filtering (PROJ-007)

---

## Design/UX

### Design Assets
- [Figma: Participant List View](https://figma.com/file/...)
- [Design Spec Document](https://confluence.company.com/...)

### User Flow
1. User opens event dashboard
2. Clicks "Participants" tab (default view)
3. System loads participant list (loading state shown)
4. List displays with all participants
5. User can scroll, search, view details

### UI Components
- `ParticipantList.tsx` - Main list container
- `ParticipantRow.tsx` - Individual participant row
- `SearchBar.tsx` - Search/filter component
- `EmptyState.tsx` - No participants message

### Edge Cases
- Empty state (no participants)
- Loading state (fetching data)
- Error state (API failure)
- Large list (200+ participants)
- Offline mode (no network)

---

## Test Scenarios

### Happy Path Tests

1. **View populated participant list**
   - Setup: Event with 25 participants
   - Action: Open participant list
   - Expected: All 25 participants shown with correct data

2. **Real-time participant addition**
   - Setup: Viewing participant list
   - Action: New participant registers
   - Expected: New participant appears within 60 seconds

### Edge Cases

3. **Empty participant list**
   - Setup: Event with 0 participants
   - Action: Open participant list
   - Expected: Empty state message shown

4. **Large participant list (200+)**
   - Setup: Event with 250 participants
   - Action: Open and scroll list
   - Expected: Smooth scrolling, <1sec load

### Error Cases

5. **API failure**
   - Setup: Simulate API timeout
   - Action: Open participant list
   - Expected: Error message + retry button shown

6. **Offline mode**
   - Setup: Go offline after loading list
   - Action: View list
   - Expected: Cached data shown + offline indicator

---

## Definition of Done

- [ ] Code written and follows style guide
- [ ] Peer review completed and approved
- [ ] All 8 acceptance criteria verified
- [ ] Unit tests written (>80% coverage achieved: 87%)
- [ ] Integration tests passing
- [ ] Manual testing completed (checklist above)
- [ ] No critical or high bugs remaining
- [ ] Design review approved ✅ 2025-11-12
- [ ] Accessibility tested (keyboard nav, screen reader)
- [ ] Performance verified (<1sec load for 200 participants)
- [ ] Documentation updated in Confluence
- [ ] Deployed to staging
- [ ] Product Owner acceptance pending

---

## Dependencies & Relationships

### Depends On (Blocked By):
- ✅ **PROJ-003:** Integrate participant data (Done 2025-11-14)
- 🔄 **PROJ-004:** Real-time sync engine (In Progress, Sprint 2)

### Blocks:
- **PROJ-007:** Participant filtering (Waiting on this)
- **PROJ-009:** Participant export (Planned for Sprint 4)

---

## Estimation

**Story Points:** 5

**Breakdown:**
- React Table setup + styling: 1.5 points
- API integration + state management: 1 point  
- Real-time WebSocket integration: 1 point
- Search functionality: 0.5 points
- Testing (unit + integration): 1 point

**Time Estimate:** 5-6 days

---

## Labels

`MVP` `Frontend` `P0` `Stage2-Strategic-Planning` `Dashboard` `React`

---

## Timeline

**Created:** 2025-10-27
**Started:** 2025-11-15
**In Review:** [Pending]
**Completed:** [Pending]

**Time Spent:** 2.5 days so far
**Remaining:** ~2.5 days

---

**Last Updated:** 2025-11-16
**Status:** In Progress (60% complete)
```

---

This template ensures Stories are clear, actionable, and ready for development with all context needed for successful implementation.

