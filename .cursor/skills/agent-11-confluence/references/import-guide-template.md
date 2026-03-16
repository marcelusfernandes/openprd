# Import Guide Template

## Purpose
Template para criar guias de importação de documentação para Confluence e estruturas de projeto para Jira.

## Confluence Import Guide Structure

```markdown
# Confluence Import Guide

## Overview

This guide provides instructions for importing the complete project documentation structure into Confluence.

**What You're Importing:**
- [X] total pages organized in hierarchical structure
- Problem Space documentation
- Solution Space documentation  
- Delivery documentation
- Complete internal linking and navigation

**Estimated Time:** [X] minutes for automated import, [Y] hours for manual

---

## Prerequisites

### Required Permissions
- [ ] Confluence Space Admin rights
- [ ] Ability to create pages in target space
- [ ] Ability to configure page permissions

### Required Tools

**For Automated Import:**
- Markdown Importer plugin for Confluence (recommended)
- OR Confluence CLI tools
- OR API access + import scripts

**For Manual Import:**
- Access to Confluence web interface
- Copy-paste capability

### Preparation Steps

1. **Choose or Create Confluence Space**
   - Recommended: Create new space for this project
   - Space Key suggestion: `[PROJECT]`
   - Space Name: `[Project Name]`

2. **Review Structure Map**
   - Open `/3-delivery/confluence/_structure-map.md`
   - Understand page hierarchy
   - Identify key/anchor pages

3. **Backup (if importing to existing space)**
   - Export current space content
   - Save backup before import

---

## Import Methods

### Method 1: Markdown Importer Plugin (Recommended)

**Best For:** Quick import with preserved formatting

**Steps:**

1. **Install Plugin** (if not already installed)
   - Go to Confluence Admin > Find new apps
   - Search for "Markdown Importer" or similar
   - Install and enable

2. **Prepare Files**
   - All markdown files are in `/3-delivery/confluence/`
   - Files use relative links that need conversion

3. **Import Process**
   - Navigate to target Confluence space
   - Go to Space Tools > Content Tools > Import
   - Select "Markdown" as format
   - Upload files or paste content

4. **Import Order** (Important!)
   - Start with `00-home.md` (creates root)
   - Import parent pages before children
   - Follow structure map hierarchy

5. **Post-Import Tasks**
   - [ ] Verify all pages imported
   - [ ] Check page hierarchy
   - [ ] Fix internal links
   - [ ] Apply Confluence macros
   - [ ] Test navigation

**Pros:** 
- Fast for large volumes
- Preserves most formatting
- Handles images and attachments

**Cons:**
- May require link fixes
- Macros need manual addition
- Plugin-dependent

---

### Method 2: Manual Copy-Paste

**Best For:** Small volumes, precise control

**Steps:**

1. **Create Page Structure First**
   - Create home page: `00-home.md` content
   - Create major sections as child pages
   - Build hierarchy top-down

2. **For Each Page:**
   
   **a. Create Page**
   - Navigate to parent page
   - Click "Create" > "Blank Page"
   - Set page title
   
   **b. Convert Content**
   - Open markdown file
   - Copy content
   - Paste into Confluence editor
   - Confluence auto-converts basic markdown
   
   **c. Add Confluence Elements**
   - Add table of contents: `/toc` macro
   - Add info panels: `/panel` or `/info` macro
   - Add status macros: `/status` macro
   - Format tables properly
   
   **d. Fix Links**
   - Convert markdown links to Confluence links
   - `[Text](../file.md)` → Search and link to page
   - Test all links work

3. **Import Order**
   ```
   1. Home page (00-home.md)
   2. Project Context pages
   3. Problem Space overview
   4. Problem Space detail pages
   5. Solution Space overview
   6. Solution Space detail pages
   7. Delivery pages
   ```

4. **Verify Each Section**
   - Check hierarchy correct
   - Verify links work
   - Test navigation
   - Review formatting

**Pros:**
- Complete control
- Best formatting quality
- No dependencies

**Cons:**
- Time-consuming
- Manual link conversion
- Tedious for large volumes

---

### Method 3: Confluence REST API (Advanced)

**Best For:** Automation, scripting, large-scale imports

**Prerequisites:**
- API token or credentials
- Python/Node.js environment
- Technical knowledge

**High-Level Process:**

1. **Setup**
   ```bash
   # Install dependencies
   pip install atlassian-python-api markdown2
   # or
   npm install confluence-api markdown-it
   ```

2. **API Authentication**
   ```python
   from atlassian import Confluence
   
   confluence = Confluence(
       url='https://your-domain.atlassian.net/wiki',
       username='your-email@company.com',
       password='your-api-token'
   )
   ```

3. **Create Pages Programmatically**
   - Read markdown files
   - Convert to Confluence storage format
   - Create pages via API
   - Maintain hierarchy with parent_id

4. **Handle Links**
   - Map file paths to page IDs
   - Replace markdown links with Confluence links
   - Verify all links after import

**Resources:**
- Confluence REST API docs
- Confluence storage format docs
- Example scripts (can be provided)

**Pros:**
- Fully automated
- Repeatable
- Handles large volumes
- Can customize transformation

**Cons:**
- Requires technical skills
- Setup time
- API rate limits

---

## Page Import Order

**Critical:** Import in this order to maintain relationships:

### Phase 1: Foundation
1. `00-home.md` - Home page (root)
2. `01-project-context/*.md` - Context pages

### Phase 2: Problem Space
3. `01-problem-space/problem-overview.md`
4. `01-problem-space/research/*.md`
5. `01-problem-space/pain-points/*.md`
6. `01-problem-space/journeys/*.md`
7. `01-problem-space/reports/*.md`

### Phase 3: Solution Space
8. `02-solution-space/solution-overview.md`
9. `02-solution-space/product-brief.md` ⭐
10. `02-solution-space/opportunities/*.md`
11. `02-solution-space/future-experience/*.md`
12. `02-solution-space/concepts/*.md`
13. `02-solution-space/mvp/*.md`
14. `02-solution-space/roadmap/*.md`

### Phase 4: Delivery
15. `03-delivery/*.md`

**Why Order Matters:**
- Parent pages must exist before children
- Links reference pages by title/ID
- Hierarchy builds correctly

---

## Post-Import Tasks

### 1. Verify Page Structure

- [ ] All pages imported successfully
- [ ] Page hierarchy matches structure map
- [ ] No orphaned pages
- [ ] Breadcrumbs work correctly

**How to Check:**
- View page tree (Space Tools > Content Tools > Page Tree)
- Compare with `_structure-map.md`

### 2. Fix Internal Links

- [ ] All page links work
- [ ] No broken links (404s)
- [ ] Anchor links work
- [ ] External links preserved

**How to Check:**
- Click through all links
- Use link checker tool if available
- Search for markdown syntax (`](../` or `.md)`)

### 3. Apply Confluence Macros

- [ ] Table of Contents added where needed
- [ ] Info/Warning/Success panels applied
- [ ] Status macros configured
- [ ] Children display added to overview pages
- [ ] Page tree added to home

**Common Macros:**
```
{toc:minLevel=2|maxLevel=3}
{info}..{info}
{warning}..{warning}
{success}..{success}
{status:colour=Green|title=Active}
{children:all=true|sort=title}
{pagetree:root=@self}
```

### 4. Format Tables

- [ ] Tables render correctly
- [ ] Header rows styled
- [ ] Sortable where appropriate
- [ ] Mobile-friendly

**Check:**
- View each table
- Test sorting if enabled
- Check on mobile/tablet

### 5. Configure Permissions

- [ ] Space permissions set
- [ ] Page-level permissions (if needed)
- [ ] Restrict sensitive content
- [ ] Grant appropriate access

**Recommended Permissions:**
- Read: All authenticated users
- Write: Project team members
- Admin: Project leads only

### 6. Set Up Navigation

- [ ] Home page has quick links
- [ ] Overview pages have children display
- [ ] Related pages linked
- [ ] Breadcrumbs visible

### 7. Add Metadata

- [ ] Page labels applied
- [ ] Owners assigned
- [ ] Last updated dates set
- [ ] Status indicators added

**Useful Labels:**
- `problem-space`
- `solution-space`
- `mvp`
- `stage-2`
- `priority-p0`

### 8. Test User Experience

- [ ] Navigation intuitive
- [ ] Search finds pages
- [ ] Mobile view works
- [ ] Print view acceptable

**Test As:**
- New team member (fresh eyes)
- Stakeholder (quick access to key info)
- Developer (find technical details)

---

## Troubleshooting

### Issue: Markdown Syntax Still Visible

**Symptoms:** Content shows `##` or `**text**` literally

**Solution:**
- Markdown wasn't converted
- Re-paste content
- Use "Preview" mode to check
- Manually format if needed

### Issue: Broken Internal Links

**Symptoms:** Links show as text or 404

**Solution:**
- Confluence uses page titles for links
- Search for target page
- Replace with Confluence link
- Format: `[Page Title]` or full link

### Issue: Images Not Showing

**Symptoms:** Broken image icons

**Solution:**
- Upload images to Confluence
- Attach to relevant page
- Update image references
- Use Confluence image syntax

### Issue: Tables Malformed

**Symptoms:** Tables show as plain text or broken

**Solution:**
- Use Confluence table editor
- Copy-paste table data
- Reformat headers
- Set column widths

### Issue: Hierarchy Wrong

**Symptoms:** Pages at wrong level

**Solution:**
- Move pages to correct parent
- Page Tools > Move
- Update breadcrumbs
- Check structure map

### Issue: Macros Not Working

**Symptoms:** `{toc}` or `{info}` shows literally

**Solution:**
- Ensure in Wiki Markup mode
- Or use macro browser (type `/` in editor)
- Insert macro properly
- Save and verify

---

## Validation Checklist

Before considering import complete:

### Content Completeness
- [ ] All [X] expected pages exist
- [ ] No content missing
- [ ] All sections present
- [ ] Text accurate and complete

### Structure & Navigation
- [ ] Hierarchy matches structure map
- [ ] Home page accessible
- [ ] All sections navigable
- [ ] Breadcrumbs work
- [ ] Page tree displays correctly

### Links & References
- [ ] All internal links work
- [ ] External links preserved
- [ ] Anchor links functional
- [ ] No 404 errors

### Formatting & Style
- [ ] Headers formatted correctly
- [ ] Tables render properly
- [ ] Lists formatted
- [ ] Code blocks styled
- [ ] Panels/macros work

### Confluence Features
- [ ] Table of contents added
- [ ] Info/warning panels applied
- [ ] Status macros configured
- [ ] Children displays work
- [ ] Page metadata set

### Access & Permissions
- [ ] Space accessible by team
- [ ] Permissions configured
- [ ] Sensitive content protected
- [ ] Watchers added

### User Experience
- [ ] Search finds pages
- [ ] Navigation intuitive
- [ ] Mobile view acceptable
- [ ] Print view readable

---

## Maintenance

### Regular Updates

**Weekly:**
- Update changed pages
- Fix broken links
- Address feedback

**Monthly:**
- Review outdated content
- Update status indicators
- Archive completed items

**Quarterly:**
- Reorganize if needed
- Clean up unused pages
- Update structure

### Version Control

**Track Changes:**
- Confluence tracks page history
- Use page versions
- Add change comments

**Major Updates:**
- Create new version
- Archive old version
- Update links

---

## Support Resources

### Documentation
- [Confluence User Guide](https://confluence.atlassian.com/doc/)
- [Markdown to Confluence Guide]
- [Confluence API Documentation]

### Internal Contacts
- Confluence Admin: [Name/Email]
- Project Owner: [Name/Email]
- Technical Support: [Name/Email]

### Training
- [Confluence basics training]
- [Markdown syntax guide]
- [Macro usage examples]

---

## Quick Reference

### Common Confluence Macros

| Macro | Usage | Purpose |
|-------|-------|---------|
| `{toc}` | Table of Contents | Auto-generate page outline |
| `{info}` | Info panel | Highlight information |
| `{warning}` | Warning panel | Show warnings |
| `{success}` | Success panel | Positive messages |
| `{note}` | Note panel | Additional notes |
| `{children}` | Child pages | List child pages |
| `{pagetree}` | Page tree | Show page hierarchy |
| `{expand}` | Expandable section | Collapse/expand content |
| `{code}` | Code block | Format code |
| `{status}` | Status label | Show status |

### Markdown to Confluence Conversion

| Markdown | Confluence | Notes |
|----------|-----------|--------|
| `# Header` | `h1. Header` | Usually auto-converts |
| `**bold**` | `*bold*` | Usually auto-converts |
| `*italic*` | `_italic_` | Usually auto-converts |
| `[Link](url)` | `[Link|url]` | May need manual fix |
| `` `code` `` | `{{code}}` | Usually auto-converts |

---

**Document Version:** 1.0
**Last Updated:** [Date]
**Owner:** [Name]
```

---

## Jira Import Guide Structure

```markdown
# Jira Import Guide

## Overview

This guide provides instructions for importing the complete project structure (Initiative, Epics, Stories) into Jira.

**What You're Importing:**
- 1 Initiative with strategic context
- [X] Epics organized by theme/concept
- [Y] Stories with complete acceptance criteria
- All relationships and dependencies

**Estimated Time:** [X] minutes via CSV, [Y] hours manually

---

## Prerequisites

### Required Permissions
- [ ] Jira Project Admin rights
- [ ] Ability to create Issues
- [ ] Ability to configure project settings

### Project Setup
- [ ] Jira Project created
- [ ] Project Key assigned (e.g., `PROJ`)
- [ ] Issue types enabled (Initiative, Epic, Story)
- [ ] Custom fields created (if needed)

### Required Files
- `/3-delivery/jira/initiative.md`
- `/3-delivery/jira/epics/*.md`
- `/3-delivery/jira/stories/*.md`
- `/3-delivery/jira/import-template.csv`

---

## Import Methods

### Method 1: CSV Import (Recommended)

**Best For:** Bulk import with relationships

**Steps:**

1. **Prepare CSV File**
   - Use provided template: `import-template.csv`
   - Verify all required columns present
   - Check data formatting

2. **Import to Jira**
   - Go to Jira Project
   - Settings > System > External System Import > CSV
   - Upload CSV file
   - Map columns to Jira fields

3. **Column Mapping**
   ```
   Issue Type → Issue Type
   Summary → Summary
   Description → Description
   Priority → Priority
   Story Points → Story Points
   Epic Link → Epic Link
   Sprint → Sprint
   Labels → Labels
   ```

4. **Import Order**
   - First: Import Initiative
   - Second: Import all Epics
   - Third: Import all Stories

5. **Post-Import**
   - [ ] Verify counts match
   - [ ] Check Epic Links
   - [ ] Configure Dependencies
   - [ ] Set up Board

**Pros:**
- Fast for large volumes
- Preserves relationships
- Repeatable

**Cons:**
- Field mapping required
- Limited to CSV capabilities
- May lose formatting

---

### Method 2: Manual Creation

**Best For:** Small projects, maximum control

**Steps:**

1. **Create Initiative**
   - In Jira, click Create
   - Select "Initiative" type
   - Copy content from `initiative.md`
   - Fill all fields
   - Save

2. **Create Epics**
   - For each epic in `/epics/` folder:
   - Click Create > Epic
   - Copy content from epic file
   - Link to Initiative
   - Save

3. **Create Stories**
   - For each story in `/stories/` folder:
   - Click Create > Story
   - Use Story template format
   - Link to Epic
   - Add acceptance criteria
   - Set story points
   - Save

4. **Configure Relationships**
   - Add Epic Links (Story → Epic)
   - Add Dependencies (Blocks/Blocked By)
   - Set Priority
   - Apply Labels

**Pros:**
- Maximum control
- Perfect formatting
- Immediate validation

**Cons:**
- Time-consuming
- Error-prone for large volumes
- Manual relationship setup

---

### Method 3: Jira REST API (Advanced)

**Best For:** Automation, programmatic import

**Prerequisites:**
- API credentials
- Programming knowledge
- Jira API familiarity

**Process:**
1. Authenticate with Jira API
2. Create Initiative via POST request
3. Create Epics with Initiative link
4. Create Stories with Epic links
5. Add issue links for dependencies

**Resources:**
- Jira REST API documentation
- Example scripts available
- Python/Node.js libraries

**Pros:**
- Fully automated
- Repeatable
- Custom transformations

**Cons:**
- Technical knowledge required
- Setup time
- API rate limits

---

## Post-Import Tasks

### 1. Verify Import

- [ ] Initiative created correctly
- [ ] All [X] Epics present
- [ ] All [Y] Stories present
- [ ] Issue counts match expected

### 2. Configure Relationships

- [ ] Epic Links set (Story → Epic → Initiative)
- [ ] Dependencies configured (Blocks, Blocked By)
- [ ] Related issues linked
- [ ] Sprint allocation set

### 3. Validate Data

- [ ] Priorities correct (P0 → Highest, etc)
- [ ] Story points assigned
- [ ] Labels applied
- [ ] Descriptions complete
- [ ] Acceptance criteria present

### 4. Set Up Board

- [ ] Create/configure Scrum or Kanban board
- [ ] Add sprints (if Scrum)
- [ ] Configure swimlanes (by Epic or Priority)
- [ ] Set up quick filters
- [ ] Configure columns (To Do, In Progress, Done, etc)

### 5. Configure Workflow

- [ ] Workflow appropriate for project
- [ ] Transitions configured
- [ ] Required fields set
- [ ] Validators added if needed

### 6. Team Setup

- [ ] Team members added to project
- [ ] Roles assigned
- [ ] Permissions configured
- [ ] Notifications set up

---

## Troubleshooting

### Issue: CSV Import Fails

**Solution:**
- Check CSV format (UTF-8 encoding)
- Verify required fields present
- Check for special characters
- Try smaller batches

### Issue: Epic Links Not Working

**Solution:**
- Ensure Epics created before Stories
- Use Epic Key (not name) for linking
- Verify Epic Link field enabled

### Issue: Story Points Not Importing

**Solution:**
- Ensure Story Points field exists
- Check field type (number)
- Verify values are numeric
- Import as custom field if needed

### Issue: Dependencies Not Set

**Solution:**
- Import all issues first
- Then configure links manually
- Or use API for automated linking

---

## Validation Checklist

- [ ] All issues imported ([X] total)
- [ ] Hierarchy correct (Initiative > Epic > Story)
- [ ] Priorities mapped correctly
- [ ] Story points assigned
- [ ] Epic links functional
- [ ] Dependencies configured
- [ ] Labels applied
- [ ] Board configured
- [ ] Team has access
- [ ] Ready for sprint planning

---

**Document Version:** 1.0
**Last Updated:** [Date]
**Owner:** [Name]
```

---

This template provides complete import guidance for both Confluence and Jira, ensuring successful deployment of all project documentation and execution structure.

