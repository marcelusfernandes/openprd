# Upstream Process - Agent Workflow System

## Overview

AI-driven qualitative research analysis system that transforms customer interviews into structured analysis, product opportunities, and executive deliverables. Dual-platform: Claude Code + Cursor.

## Two Modes of Operation

### `/pair` — Pair PMing (exploratório)
Copiloto AI que pensa junto com o PM. Conversa livre onde o AI questiona, sugere hipóteses, puxa dados das ferramentas configuradas, conecta pontos entre fontes, e ajuda a construir insights. **É aqui que as skills de integração (analytics, CRM, feedback, etc.) ganham vida** — o copiloto sabe o que o PM tem configurado e sugere análises relevantes no momento certo.

### `/start-workflow` — Pipeline (execução)
Pipeline estruturado de 3 fases com 15+ agentes que rodam em sequência. Transforma entrevistas em análise → soluções → entregáveis. Ideal quando o PM já tem material e quer processar tudo de uma vez.

O PM pode começar no modo exploratório (`/pair`) e quando tiver confiança suficiente, migrar para execução (`/start-workflow`). O copiloto sugere essa transição naturalmente.

> **Caminho Mínimo:** Tem entrevistas e quer analisar?
> Você precisa APENAS dos agentes 0-5 (Phase 1 básica).
> Nenhuma ferramenta externa é necessária — só as entrevistas.
> Digite `/start-workflow` e selecione "Pain Point Brief" pra começar rápido.
> Para data-first (sem entrevistas), selecione "Data-First Discovery".

## Architecture

| Component | Claude Code | Cursor |
|-----------|-------------|--------|
| **Rules** | `.claude/rules/` | `.cursor/rules/` |
| **Skills** | `.claude/skills/` | `.cursor/skills/` |
| **Agents** | `.claude/agents/` | `.cursor/agents/` |
| **Hooks** | `.claude/settings.json` | `.cursor/hooks.json` |
| **Templates** | `.claude/skills/*/references/` | `.cursor/skills/*/references/` |
| **MCP** | `.claude/.mcp.json` | N/A |
| **Commands** | `.claude/skills/` (user-invocable) | `.cursor/commands/` |

## Phases & Agents

### Data-First Discovery (opcional, antes do Phase 1)

| Agent | Skill | Propósito | Output |
|-------|-------|-----------|--------|
| Q1 | `agent-q1-data-scout` | Consulta analytics configurados, gera landscape de dados | `/1-problem/0-data-landscape/data-landscape.md` |
| Q2 | `agent-q2-hypothesis-generator` | Transforma anomalias em hipóteses testáveis | `/1-problem/0-data-landscape/hypotheses.md` |
| Script | `interview-script-generator` | Gera roteiro de entrevista baseado nas hipóteses | `/0-documentation/0a-projectdocs/interview-script.md` |

### Phase 1: Problem Analysis
| Agent | Skill | Purpose |
|-------|-------|---------|
| 0 | `agent-0-context-specialist` | Project context setup, broad-context.md |
| 1 | `agent-1-research-specialist` | Interview analysis, exhaustive pain point extraction |
| **Pain Point Analyst** | `.claude/agents/pain-point-analyst.md` | **Autonomous orchestrator for pain point sub-pipeline** |
| ↳ 2A | `agent-2a-granular-specialist` | Pain point decomposition into atomic issues |
| ↳ Review | `painpoint-reviewer` | Independent quality review of decomposition |
| ↳ 2B | `agent-2b-clustering-specialist` | Relationship-based pain point clustering |
| 2C | `agent-2c-jtbd-specialist` | Jobs to Be Done extraction from pain clusters |
| 3 | `agent-3-journey-mapper` | As-Is journey mapping per source |
| 4 | `agent-4-journey-consolidation` | Consolidated journey creation |
| 5 | `agent-5-report-generator` | Strategic reports (pain + problem) |
| 6 | `agent-6-visual-designer` | Figma Make journey visualization |

Flow: `0 → 1 → [Pain Point Analyst: 2A → review → 2B] → 2C → 3 → 4 → (5 ‖ 6)`

### Phase 2: Solution Ideation
| Agent | Skill | Purpose |
|-------|-------|---------|
| S6 | `solution-6-ideation` | Pain clusters → product opportunities |
| S7 | `solution-7-experience` | To-Be journey design |
| S8 | `solution-8-concept` | Solution concepts + feasibility |
| S9 | `solution-9-prioritization` | MVP scope + feature prioritization |
| S10 | `solution-10-communication` | Product brief, roadmap, executive materials |

Flow: `S6 → S7 → S8 → S9 → S10`

### Phase 3: Delivery
| Agent | Skill | Purpose |
|-------|-------|---------|
| 11 | `agent-11-confluence` | Confluence documentation structure |
| 12 | `agent-12-jira` | Jira Initiative/Epics/Stories |

### Publishing (post-Phase 3)
| Agent | Type | Purpose |
|-------|------|---------|
| `confluence-publisher` | `.claude/agents/` | Push Confluence docs via MCP |
| `jira-publisher` | `.claude/agents/` | Create Jira issues via MCP |
| `miro-publisher` | `.claude/agents/` | Create Miro boards with journey maps |
| `figma-publisher` | `.claude/agents/` | Create Figma visualizations |

### Data Exploration
| Component | Type | Purpose |
|-----------|------|---------|
| `data-explorer` | Skill | Query analytics platforms for quantitative evidence |
| `sql-analyst` | Skill | SQL queries against data warehouses |
| `databricks` | Skill | Databricks CLI, Unity Catalog, Genie, SQL |
| `analytics-explorer` | Agent | Cross-platform analytics exploration |

#### Dedicated Tool Skills
| Skill | Interface | Purpose |
|-------|-----------|---------|
| `bigquery` | CLI (bq) | BigQuery datasets, SQL queries, exports |
| `snowflake` | CLI (snowsql) | Snowflake warehouses, SQL queries, stages |
| `posthog` | CLI | Events, funnels, feature flags, session replays |
| `tableau` | CLI (tabcmd) | Workbooks, dashboards, data exports |
| `amplitude` | API | User behavior, funnels, cohorts, retention |
| `mixpanel` | API | Event analytics, funnels, segmentation |
| `metabase` | API | Dashboards, saved questions, SQL queries |
| `pendo` | API | Feature adoption, guides, NPS, user paths |
| `redash` | API | SQL queries, saved dashboards, visualizations |

### Product Tool Integrations
| Skill | Interface | Purpose |
|-------|-----------|---------|
| `linear` | MCP (official) | Issue tracking, backlog management, sprint cycles |
| `launchdarkly` | MCP (official) | Feature flags, targeting rules, gradual rollouts |
| `hotjar` | API | Survey responses, user feedback export |
| `zendesk` | MCP (community) | Support ticket analysis, pain point mining |
| `intercom` | MCP (official) | Customer conversations, feedback extraction |
| `segment` | API | CDP sources, destinations, tracking plans, user profiles |
| `salesforce` | MCP (official) | CRM data, deals, churn analysis, sales feedback |
| `sentry` | MCP (official) | Error tracking, product health, bug prioritization |
| `productboard` | MCP (community) | Feature management, customer feedback, roadmap alignment |
| `dovetail` | MCP (official) | Research repository, insights, interview management |
| `loom` | Community tools | Video transcripts, async demo analysis (no public API) |
| `palantir-foundry` | MCP (official) | Ontology, datasets, SQL queries, transforms |
| `palantir-gotham` | API + scripts | Graph analysis, entity search, geotemporal data |

### PM Productivity Skills
| Skill | Type | Purpose |
|-------|------|---------|
| `competitive-analyst` | Research | Competitor analysis, feature matrices, gap identification |
| `metric-definer` | Strategy | KPIs, OKRs, tracking plans from MVP scope |
| `stakeholder-brief` | Communication | Audience-adapted briefs (exec, tech, design, commercial) |
| `user-story-writer` | Delivery | JTBD → user stories with acceptance criteria (Given/When/Then) |
| `ab-test-designer` | Experimentation | Hypothesis → A/B test plans with sample size and guardrails |
| `interview-script-generator` | Research | Gera roteiro de entrevista baseado em hipóteses data-backed |
| `discovery-reviewer` | Agent | Cross-phase peer review, gap analysis, quality scoring |

### Multimedia & Content Generation
| Skill | Type | Purpose |
|-------|------|---------|
| `notebooklm` | CLI + SDK | Audio podcasts, video overviews, slide decks, quizzes, mind maps from discovery outputs |

### Onboarding
| Skill | Type | Purpose |
|-------|------|---------|
| `setup` | Wizard (user-invocable) | Interactive onboarding — detects tools, guides credentials, configures everything |

### Utility Skills
| Skill | Type | Purpose |
|-------|------|---------|
| `guardrails-validator` | Validation | Data integrity checks |
| `researcher` | Research | Synthetic user interviews |
| `analyze-interview` | Analysis | Quick single-interview analysis |
| `google-importer` | Import | Pull docs from Google Workspace |
| `notion-exporter` | Export | Push outputs to Notion |
| `slack-notifier` | Notification | Team status updates |
| `export-all` | Export | One-click publish to all platforms |

### Commands (user-invocable)
| Command | Purpose |
|---------|---------|
| `/setup` | Interactive onboarding wizard — connect your tools |
| `/project` | Multi-project management — create, switch, list, archive |
| `/pair` | Pair PMing — AI thinking partner, explores with you, suggests analyses |
| `/start-workflow` | Launch the full discovery workflow |
| `/entrevista` | Conduct synthetic interview |
| `/quick-ask` | Quick question, no modifications |
| `/validacao` | Run guardrail validation |
| `/discovery-map` | Ver progresso do discovery |
| `/evidence-board` | Mapa visual de evidências (Mermaid) |
| `/export-presentation` | Exportar outputs pra HTML/PDF |

### Build System Agents
| Agent | Purpose |
|-------|---------|
| `builder` | Constructs skills, agents, rules |
| `validator` | Validates format and guardrails |
| `workflow-orchestrator` | Orchestrates full 3-phase pipeline |

## Workflow Triggers

- **Start workflow:** "start workflow", "begin analysis", "run agents", "comece"
- **Research:** "pesquisar", "research", "explorar", "investigar"
- **Validation:** "validacao", "validate guardrails"
- **Export:** "exportar", "publicar", "publish"

## Completion Checks

| Agent | Key Output |
|-------|------------|
| 0 | `/0-documentation/broad-context.md` |
| 1 | `/1-problem/1a-interview-analysis/*.md` |
| 2A | `/1-problem/1b-painpoints/1b0-granular/all-painpoints-granular.md` |
| Review | `/1-problem/1b-painpoints/1b0-granular/*-review.md` |
| 2B | `/1-problem/1b-painpoints/painpoint-mapping.md` |
| 2C | `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` |
| 3 | `/1-problem/1c-asis-journey/1c2-asis-breakdown/*.md` |
| 4 | `/1-problem/1c-asis-journey/asis-journey.md` |
| 5 | `/1-problem/1d-problem-output/pain-report.md` + `problem-report.md` |
| 6 | `/1-problem/1d-problem-output/journey-output.md` |
| S6 | `/2-solution/2a-opportunities/opportunities-identification.md` |
| S7 | `/2-solution/2b-tobe-journey/consolidated-future-journey.md` |
| S8 | `/2-solution/2c-solution-concepts/solution-concepts.md` |
| S9 | `/2-solution/2d-prioritization/mvp-scope.md` |
| S10 | `/2-solution/2f-solution-output/product-brief.md` |
| 11 | `/3-delivery/confluence/_structure-map.md` |
| 12 | `/3-delivery/jira/initiative.md` |

## Data Integrity

All outputs enforced by:
1. `.claude/rules/guardrails-core.md` / `.cursor/rules/guardrails-core.mdc` (always-on)
2. `.cursor/scripts/validate-guardrails.py` (deterministic hook)
3. `guardrails-validator` skill (on-demand validation)

Rules: No untagged dollar amounts, no unsourced percentages, all claims need `[Source: file.md]` or `[AI estimation based on X]` tags.

## MCP Integrations

### Collaboration & Delivery
| Server | Purpose | Phase |
|--------|---------|-------|
| **Figma** | Journey visualization, design handoff | Phase 1 (Agent 6) |
| **Miro** | Collaborative boards, journey maps | Phase 1-2 |
| **Google Calendar** | Team scheduling | All |
| **Atlassian** | Confluence pages + Jira issues | Phase 3 |
| **Slack** | Team notifications | All |
| **Notion** | Alternative documentation | Phase 3 |
| **Google Workspace** | Interview transcript import | Phase 0 |

### Analytics & Data
| Server | Purpose | Phase |
|--------|---------|-------|
| **Amplitude** | User behavior, funnels, cohorts | Phase 0-2 |
| **Mixpanel** | Event analytics, funnels, retention | Phase 0-2 |
| **PostHog** | Product analytics, feature flags, replays | Phase 0-2 |
| **BigQuery** | SQL data warehouse queries | Phase 0-3 |
| **Snowflake** | SQL data warehouse queries | Phase 0-3 |
| **Databricks** | Unity Catalog, SQL, Genie AI | Phase 0-3 |
| **Metabase** | BI dashboards, SQL queries | Phase 0-3 |
| **Tableau** | BI visualizations, data exploration | Phase 0-3 |
| **Redash** | SQL queries, saved dashboards | Phase 0-3 |

### Product Tools
| Server | Purpose | Phase |
|--------|---------|-------|
| **Linear** | Issue tracking, backlog, sprints | Phase 3 |
| **LaunchDarkly** | Feature flags, rollouts, experiments | Post-launch |
| **Zendesk** | Support ticket mining, VOC | Phase 0-1 |
| **Intercom** | Customer conversations, feedback | Phase 0-1 |
| **Salesforce** | CRM data, deals, customer intelligence | Phase 0-2 |
| **Sentry** | Error tracking, product health | Phase 0-2 |
| **Productboard** | Feature management, customer feedback | Phase 0-3 |
| **Dovetail** | Research repository, insights | Phase 0-2 |
| **Palantir Foundry** | Ontology, datasets, SQL, transforms | Phase 0-3 |

Config: `.claude/.mcp.json` + `_context/claude/mcp-setup.md`

## Directory Structure

```
.claude/                      # Claude Code configuration
  skills/                     # 62 skills (SKILL.md + references/)
  agents/                     # 10 subagents
  rules/                      # 3 rule files
  settings.json               # Hooks + permissions
  .mcp.json                   # MCP server config
.cursor/                      # Cursor configuration (mirror)
  skills/                     # 21 skills
  agents/                     # 1 agent
  rules/                      # 2 rules
  commands/                   # 3 commands
  hooks.json                  # Hooks
  scripts/                    # Validation scripts
0-documentation/              # Inputs
  0a-projectdocs/
  0b-Interviews/
  broad-context.md
1-problem/                    # Phase 1 outputs
  1a-interview-analysis/
  1b-painpoints/
    1b0-granular/
    1b1-painpoints-breakdown/
    1b2-jtbd/
  1c-asis-journey/
  1d-problem-output/
2-solution/                   # Phase 2 outputs
  2a-opportunities/
  2b-tobe-journey/
  2c-solution-concepts/
  2d-prioritization/
  2e-roadmap/
  2f-solution-output/
3-delivery/                   # Phase 3 outputs
  confluence/
  jira/
_context/                     # Reference documentation
  claude-docs/                # Claude Code reference
  cursor-docs/                # Cursor reference
  claude/logs/                # Build logs
_exports/                     # Exported presentations (HTML/PDF)
```
