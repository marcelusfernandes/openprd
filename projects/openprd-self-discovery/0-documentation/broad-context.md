# Broad Context — OpenPRD Self-Discovery

[Agent0] Generated: 2026-03-15

---

## 1. Project One-Liner

**OpenPRD is running product discovery on itself** — using its own pipeline to analyze real user interviews and identify what to build, fix, and prioritize for its next iteration.

### Scope Boundaries

- **In scope:** Analysis of 4 user interviews (enterprise PM, solo founder, Series B PM, growth PM), market research synthesis, identification of pain points and strategic opportunities across all user segments.
- **Out of scope:** Actual implementation of fixes, competitive reverse-engineering, pricing model decisions, go-to-market strategy execution.

---

## 2. Multi-Dimensional Objectives

### UX Objectives
- Identify UX friction across the onboarding, workflow execution, and output consumption phases.
- Understand where the CLI/IDE paradigm helps vs. hurts adoption across different PM personas.
- Map the gap between "power" and "accessibility" — the tool is analytically strong but operationally rough. [Source: product-context.md]

### Operational Objectives
- Determine which integrations (Amplitude, BigQuery, Salesforce, Jira, Intercom) deliver value vs. create friction.
- Evaluate whether the 3-phase pipeline (Problem → Solution → Delivery) fits all user types or needs modal workflows (full pipeline vs. quick analysis vs. data-first).
- Assess export/output format adequacy — HTML, Markdown, Confluence, Slides. [Source: product-context.md]

### Business Objectives
- Identify monetization signals: willingness to pay ranges from $50/mo (solo founder) to $500-1000/seat/mo (enterprise). [Source: aisha-enterprise.md] [Source: diego-founder.md]
- Determine segment prioritization: enterprise vs. mid-market vs. solo founders vs. growth PMs. [Source: product-context.md]
- Evaluate positioning within a market projected at $4.14B (2026) → $13.29B (2034) for AI in product/project management. [Source: market-research.md]

### Technical Objectives
- Assess integration depth — current integrations described as "shallow" (BigQuery) and "early-stage" (Salesforce). [Source: tom-growth.md] [Source: aisha-enterprise.md]
- Evaluate the copilot (/pair) vs. pipeline (/start-workflow) architecture and when each mode fits.
- Identify infrastructure needs: collaboration layer, SSO, SOC 2, export formats. [Source: aisha-enterprise.md]

### Strategic Objectives
- Validate OpenPRD's unique positioning: the only tool bridging quantitative analytics and qualitative discovery in an end-to-end pipeline. [Source: market-research.md]
- Assess competitive window — Notion Custom Agents, Productboard Spark, and open-source alternatives (cursor-pm-copilot, pm-workflow-copilot-ide) are emerging. [Source: market-research.md]
- Determine whether "open source + local-first + IDE-native" is a durable moat or a ceiling on adoption.

---

## 3. Stakeholders

### Internal (Product Team)
| Stakeholder | Priority | Concern |
|-------------|----------|---------|
| Core maintainers | Build the right thing next | Which pain points to fix first, which features to add |
| Community contributors | Clarity on architecture and contribution paths | Documentation, modularity, onboarding |

### External (Users — by Persona)
| Persona | Represented by | Priority | WTP |
|---------|---------------|----------|-----|
| Enterprise PM | Aisha | Collaboration, security, custom templates, governance | $500-1000/seat/mo |
| Mid-market PM | Sarah | Quant-qual synthesis, better exports, opinionated solutions | $200/mo |
| Growth PM | Tom | Deep data integration, experiment awareness, metric hooks | $300/mo |
| Solo Founder | Diego | Simplicity, speed, actionable top-3 list, low overhead | $50-100/mo |

### External (Market)
| Stakeholder | Relevance |
|-------------|-----------|
| Competing tools (Dovetail, Notion AI, Productboard) | Moving toward agentic AI; closing window of differentiation |
| Open-source PM community | No existing AI-powered discovery framework — OpenPRD is first mover |
| AI infrastructure providers (Anthropic, OpenAI) | Cost and quality of underlying LLMs directly affect product viability |

---

## 4. Data Inventory

### Qualitative Data
| Source | Count | Format | Coverage |
|--------|-------|--------|----------|
| User interviews | 4 | Markdown transcripts | 4 distinct personas: enterprise, mid-market, solo founder, growth PM |
| Interview: Aisha (Enterprise) | 1 | `0b-Interviews/aisha-enterprise.md` | Fortune 500 fintech, 8 merchant interviews loaded, full pipeline tested |
| Interview: Sarah (Series B) | 1 | `0b-Interviews/sarah-series-b.md` | 50-person SaaS, trial churn discovery, Amplitude + Intercom configured |
| Interview: Tom (Growth) | 1 | `0b-Interviews/tom-growth.md` | B2B marketplace, data-first workflow, BigQuery + Amplitude configured |
| Interview: Diego (Solo Founder) | 1 | `0b-Interviews/diego-founder.md` | Bootstrapped scheduling tool, 5 Zoom recordings, zero PM experience |

### Quantitative Data
- No direct quantitative data from user analytics (product telemetry, usage metrics, etc.).
- Market sizing data available from market-research.md (industry projections, competitor pricing).
- Willingness-to-pay signals captured qualitatively from interviews.

### Other Artifacts
| Artifact | Location | Status |
|----------|----------|--------|
| Product context | `0a-projectdocs/product-context.md` | Complete (v1) |
| Market research | `0a-projectdocs/market-research.md` | Complete (v1), 28 sources cited |
| Domain context | `/_domain-context/` | Not available |
| Domain knowledge | `/_domain-knowledge/` | Not available |

---

## 5. Analysis Scope Brief

### Directive to Downstream Agents

**Capture ALL pain point types exhaustively.** The 4 interviews represent fundamentally different user segments with divergent needs. Agents must:

1. **Extract every atomic pain point** — even seemingly small frictions (e.g., "Portuguese docs confused me" from Diego) matter for adoption.
2. **Preserve segment context** — a pain point from Aisha (enterprise) has different weight and implications than the same pain point from Diego (solo founder). Tag by persona.
3. **Include quantitative signals** — willingness-to-pay, time estimates ("40% of my time reformatting," "2 hours fighting the pipeline," "20 minutes for API key setup"), and satisfaction ratings ("80% accuracy," "60% of content reusable").
4. **Capture positive signals too** — what works well is as important as what's broken. The copilot /pair mode, source attribution, and analytical depth were praised across all 4 interviews.
5. **Cross-reference with market research** — pain points that align with market gaps (e.g., "no tool bridges quant and qual") have strategic significance beyond individual user frustration.
6. **Watch for convergent themes** — all 4 users independently mentioned: (a) collaboration/sharing gap, (b) export format limitations, (c) quant-qual synthesis weakness, (d) /pair mode as the strongest feature. These convergences signal high-confidence findings.

### Pain Point Categories to Watch
- **Onboarding & Setup:** API keys, repo cloning, language confusion, complexity overload
- **Workflow Fit:** Pipeline overkill for small users, insufficient depth for data-heavy users
- **Integration Depth:** Shallow data queries, no experiment awareness, raw JSON outputs
- **Output & Export:** HTML-only export, no brand templates, no Google Slides/PowerPoint
- **Collaboration:** No sharing, no URLs, no team access, "lonely tool"
- **Solution Quality:** Generic Phase 2 outputs, weak prioritization, platitudes instead of concrete approaches
- **Copilot Intelligence:** When /pair works, it's the best part; but pipeline mode doesn't leverage the same intelligence
- **Segment Mismatch:** Tool assumes enterprise PM workflow; doesn't adapt to founders or growth PMs

---

## 6. Market Landscape Summary

### Market Size
- AI in project management: $4.14B (2026) → $13.29B (2034), CAGR 15.70% [Source: market-research.md]
- 94% of product professionals use AI frequently; ~50% deeply integrated in workflows [Source: market-research.md]
- 80% of UX researchers use AI tools, +24% YoY [Source: market-research.md]

### Key Trends
1. **Copilot → Agentic AI transition** (2026-2030): Market shifting from prompt-response to autonomous multi-step execution. OpenPRD's 15-agent pipeline is architecturally ahead but execution needs maturation. [Source: market-research.md]
2. **AI-native entrantes disrupting incumbents**: ChatPRD (100K+ PMs), BuildBetter, Zeda.io iterating faster than Productboard/Dovetail on AI features. [Source: market-research.md]
3. **Custom Agents era**: Notion launched Custom Agents (Feb 2026) — autonomous 24/7 agents across Slack, Figma, Linear, etc. This raises the competitive bar. [Source: market-research.md]

### Competitive Positioning
OpenPRD occupies a **unique but undefended position**: high discovery depth + high pipeline breadth. No competitor currently covers interview-to-Jira end-to-end with agentic AI. However:
- **Dovetail** dominates UX for qualitative research (better tagging, collaboration, visual outputs)
- **Productboard Spark** has enterprise traction with credit-based AI copilot
- **Notion AI Custom Agents** offers generalizable agentic workflows with superior UX
- **cursor-pm-copilot** and **pm-workflow-copilot-ide** are open-source competitors attempting similar IDE-native PM workflows [Source: market-research.md]

### Unserved Market Gaps (Opportunities)
1. **End-to-end discovery pipeline** — no tool covers the full loop [Source: market-research.md]
2. **Quant-qual bridge** — every user interviewed wants this; no tool delivers it [Source: tom-growth.md] [Source: sarah-series-b.md]
3. **Open-source AI discovery** — completely empty space in open-source ecosystem [Source: market-research.md]
4. **Compliance-grade traceability** — source attribution as enterprise differentiator [Source: aisha-enterprise.md]

---

## 7. Assumptions and Open Questions

### Assumptions (Require Validation)
1. [Assumption: requires validation] CLI/IDE-native approach serves early adopters while a future web layer could unlock broader adoption.
2. [Assumption: requires validation] The 4 interviewed personas (enterprise, mid-market, growth, founder) represent the primary segments worth pursuing.
3. [Assumption: requires validation] Open-source + local-first is a durable competitive moat, not just a phase before SaaS competitors catch up.
4. [Assumption: requires validation] PM copilot (/pair mode) is more valuable than automated pipeline — interviews suggest users prefer guided intelligence over automated document generation.
5. [Assumption: requires validation] 80% accuracy on auto-synthesis (Aisha's assessment) is sufficient for early adoption, with iteration improving over time.

### Open Questions
1. **Monetization:** Open-source core + premium features? Hosted SaaS tier? Enterprise licenses? All 4 users expressed willingness to pay different amounts — what model captures the most value? [Source: product-context.md]
2. **Segment priority:** Enterprise (high WTP, complex needs) vs. mid-market (moderate WTP, faster iteration) vs. founders (low WTP, high volume)? [Source: product-context.md]
3. **Collaboration layer:** Build native collaboration or integrate with existing tools (Notion, Miro, Google Docs)? Aisha and Sarah both flagged this as critical. [Source: aisha-enterprise.md] [Source: sarah-series-b.md]
4. **Data integration depth:** How deep should BigQuery/Amplitude/Salesforce integrations go? Tom wants 30-query autonomous exploration; current state is 3 basic queries. [Source: tom-growth.md]
5. **Adaptation by persona:** Should the tool auto-detect user type and simplify (Diego's request) or offer explicit mode selection? [Source: diego-founder.md]
6. **Language:** Should all documentation be English-first for global adoption? Diego flagged Portuguese docs as a friction point. [Source: diego-founder.md]
7. **Export format:** How to support PowerPoint/Google Slides/branded PDFs without building a rendering engine? [Source: aisha-enterprise.md] [Source: sarah-series-b.md]

---

## 8. Risks and Constraints

### Risks
| Risk | Severity | Mitigation |
|------|----------|------------|
| Competitive window closing — Notion Agents, Productboard Spark accelerating | High | Ship faster on core differentiators (quant-qual bridge, traceability) |
| IDE-native limits addressable market to technical PMs | High | Consider web/hosted layer for non-technical users |
| LLM API cost makes tool expensive for individual users | Medium | Optimize token usage; explore cheaper models for routine tasks |
| Open-source competitors (cursor-pm-copilot) could iterate faster | Medium | Build community, establish brand as the reference framework |
| Enterprise security requirements (SOC 2, SSO) create high barrier | Medium | Prioritize only if enterprise is target segment |

### Constraints
- **Technical:** Dependent on Anthropic/OpenAI APIs; no proprietary model.
- **Resource:** Appears to be small team or solo maintainer — limits parallelization of improvements.
- **Architecture:** Local-first repo model inherently conflicts with collaboration needs.
- **Data:** No product telemetry on OpenPRD itself — user insights come only from qualitative interviews.

---

## 9. Handoff Checklist for Agent 1

- [x] `broad-context.md` created with source references
- [x] All files in `0-documentation/0a-projectdocs/` read and synthesized (2 files: product-context.md, market-research.md)
- [x] Interview files listed with summaries (4 interviews in `0b-Interviews/`)
- [x] Open questions and assumptions documented
- [x] Data inventory complete
- [x] `1-problem/` directory structure exists (1a through 1d)
- [ ] Domain context: Not available (`/_domain-context/` and `/_domain-knowledge/` do not exist)

### Interview Files for Agent 1 Processing
1. `0-documentation/0b-Interviews/aisha-enterprise.md` — Enterprise PM, Fortune 500 fintech, collaboration/security/templates focus
2. `0-documentation/0b-Interviews/sarah-series-b.md` — Series B PM, quant-qual synthesis/exports/opinionated solutions focus
3. `0-documentation/0b-Interviews/tom-growth.md` — Growth PM, data-first workflow/metric hooks/experiment awareness focus
4. `0-documentation/0b-Interviews/diego-founder.md` — Solo founder, simplicity/speed/actionability focus

### Key Signal for Downstream Analysis
All 4 users independently validated the **analytical engine** as best-in-class while identifying **packaging, collaboration, and integration depth** as the primary gaps. The convergence is strong: the "what" is right, the "how" needs work.

---

*[Agent0] Sources: product-context.md, market-research.md, aisha-enterprise.md, sarah-series-b.md, tom-growth.md, diego-founder.md*
