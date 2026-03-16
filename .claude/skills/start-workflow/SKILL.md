---
name: start-workflow
description: Launch the full discovery workflow with phase selection and mode choice
disable-model-invocation: true
---

# Start Workflow - Discovery Pipeline Orchestrator

## Overview
Orchestrates the full product discovery pipeline across three phases, invoking specialized agents sequentially via the Agent tool.

## Step 1: Ask User for Configuration

Use `AskUserQuestion` to collect configuration with clickable options:

```json
AskUserQuestion({
  questions: [
    {
      question: "O que você quer fazer?",
      header: "Modo",
      multiSelect: false,
      options: [
        { label: "Founder Fast Track (30min)", description: "Tenho 2-4 calls/notas — quero insights rapidos e proximo passo (Agents 0, 1, 5)" },
        { label: "Pain Point Brief (rápido)", description: "Só análise de problemas + resumo executivo — ideal pra 1ª apresentação (Agents 0,1,2A,2B,5)" },
        { label: "Fase 1: Problemas (completa)", description: "Análise completa: entrevistas, pain points, JTBDs, jornada as-is (Agents 0-6)" },
        { label: "Fase 2: Soluções", description: "Oportunidades, jornada to-be, conceitos, MVP (Agents S6-S10)" },
        { label: "Fase 3: Entregáveis", description: "Confluence + Jira (Agents 11-12)" },
        { label: "Pipeline Completo", description: "Tudo — da análise ao Jira, fase por fase" },
        { label: "Data-First Discovery", description: "Começa com dados quantitativos (Amplitude, BigQuery) → hipóteses → entrevistas focadas (Agents Q1, Q2, depois Phase 1)" },
        { label: "Stakeholder Prep (rápido)", description: "Tenho entrevistas + dados — gera resumo executivo e brief pra apresentação (Agents 0,1,2A,2B,5,S10)" },
        { label: "Retomar", description: "Continuar de um agente específico" }
      ]
    },
    {
      question: "Como quer acompanhar a execução?",
      header: "Modo",
      multiSelect: false,
      options: [
        { label: "Passo a passo (Recomendado)", description: "Revise e aprove após cada agente — ideal para primeira vez" },
        { label: "Automático", description: "Todos os agentes rodam em sequência sem pausas" }
      ]
    }
  ]
})
```

If user selects "Retomar", use a follow-up AskUserQuestion to ask which agent to resume from.

## Step 2: Verify Dependencies

Before starting any phase, verify required inputs exist:

### Phase 1 Dependencies
- `/0-documentation/0a-projectdocs/` contains project documentation
- `/0-documentation/0b-Interviews/` contains at least one interview file

If `/1-problem/0-data-landscape/data-landscape.md` exists but no interviews:
- Suggest: "Você tem dados analisados mas nenhuma entrevista. Quer gerar roteiro de entrevista baseado nas hipóteses do Agent Q2?"

### Phase 2 Dependencies
- `/1-problem/1b-painpoints/` contains pain point clusters
- `/1-problem/1b-painpoints/1b2-jtbd/` contains JTBD analysis
- `/1-problem/1c-asis-journey/` contains as-is journey maps
- `/0-documentation/broad-context.md` exists

### Phase 3 Dependencies
- `/2-solution/` contains completed solution outputs
- `/1-problem/1d-problem-output/` contains problem reports

If dependencies are missing, report which files are absent and use AskUserQuestion:
```json
AskUserQuestion({
  questions: [{
    question: "Faltam arquivos da fase anterior. O que quer fazer?",
    header: "Dependências",
    multiSelect: false,
    options: [
      { label: "Rodar fase anterior", description: "Executar a fase pré-requisito primeiro" },
      { label: "Continuar mesmo assim", description: "Prosseguir sem os arquivos (pode gerar resultados incompletos)" }
    ]
  }]
})
```

## Step 3: Execute Agents

### Investigation Guard
If the active initiative has size "investigation" (check via `python3 _tools/project.py status`):
- Do NOT run the pipeline. Inform: "Esta iniciativa e do tipo Investigacao — use /pair para explorar. Se precisar rodar o pipeline, converta para Quick com: python3 _tools/project.py resize {slug} quick"

### Founder Fast Track
If user selected "Founder Fast Track (30min)":
Run: `0 → 1 → 5`
Skip ALL intermediate agents (2A, 2B, 2C, 3, 4, 6).
Produces: broad context + interview analysis + executive pain summary.
Estimated time: 30-45 minutes for 2-4 interviews.
Post-completion: suggest /pair for deeper exploration or Pain Point Brief for structured analysis.

### Fast-Track: Pain Point Brief
If user selected "Pain Point Brief (rápido)", run ONLY these agents in order:
`0 → 1 → [2A → review → 2B] → 5`
Skip agents 2C, 3, 4, 6. This produces: interview analysis + pain point clusters + executive report.
Estimated time: 1-2 hours for 5 interviews.

### Data-First Discovery
If user selected "Data-First Discovery":
1. Check if analytics tools are configured (Amplitude, PostHog, BigQuery in .env)
2. If not configured, suggest running /setup first
3. Run: `Q1 (agent-q1-data-scout) → Q2 (agent-q2-hypothesis-generator)`
4. Verify outputs: `/1-problem/0-data-landscape/data-landscape.md` and `/1-problem/0-data-landscape/hypotheses.md`
5. Present hypotheses and ask: "Quer gerar roteiro de entrevista baseado nessas hipóteses?"
6. If yes, invoke the `interview-script-generator` skill. Verify output at `/0-documentation/0a-projectdocs/interview-script.md`
7. After interviews are done, user can run Phase 1 normally — agents will have data-landscape context available

### Stakeholder Prep
If user selected "Stakeholder Prep":
Run: `0 → 1 → [2A → review → 2B] → 5 → S10`
Produces: interview analysis + pain points + executive report + stakeholder brief.
Estimated time: 2-3 hours for 5 interviews.

### Fast-Track: Pipeline Completo
If user selected "Pipeline Completo", run Phase 1 → Phase 2 → Phase 3 sequentially, asking for approval between phases.

### Orchestration Flow

**Phase 1:** `0 → 1 → [2A → review → 2B] → 2C → 3 → 4 → (5 ‖ 6)`
**Phase 2:** `S6 → S7 → S8 → S9 → S10`
**Phase 3:** `11 → 12`

### Agent Invocation Protocol

For each agent:

1. **Guardrails reminder**: Before invoking, remind the subagent of core guardrails:
   - Never invent data — tag estimates as `[AI estimation based on X]`
   - Always cite sources — `[Source: filename.md]` for every claim
   - Mark assumptions — `[Assumption: requires validation]`
   - Conservative language — no absolute claims

2. **Invoke via Agent tool** (subagent_type: general-purpose):
   - Instruct the subagent to read its skill from `.claude/skills/{agent-name}/SKILL.md`
   - Provide the agent with the list of input files it needs to read
   - Provide the guardrails reminder above

3. **Completion check**: After the agent finishes, verify its output exists per the table below

3b. **Quality gate**: Run `guardrails-validator` automated checks on the output. If critical checks fail, report and offer to re-run the agent.

3c. **Dual-write (OpenViking)**: If OpenViking MCP is available (ov_health succeeds), index the agent's output:
    - Call `ov_add_resource` with the absolute path of each output file
    - This ensures outputs are searchable via semantic search while remaining in git via filesystem
    - If OpenViking is not available, skip silently — filesystem is the primary store

4. **Step-by-step mode**: If in step-by-step mode, present the agent's output summary and use AskUserQuestion:
   ```json
   AskUserQuestion({
     questions: [{
       question: "Agente {name} concluído. Como quer prosseguir?",
       header: "Próximo passo",
       multiSelect: false,
       options: [
         { label: "Aprovar e continuar", description: "Avançar para o próximo agente" },
         { label: "Revisar output", description: "Me mostre o que foi gerado antes de continuar" },
         { label: "Parar aqui", description: "Interromper o workflow neste ponto" }
       ]
     }]
   })
   ```

### Special Cases

- **Agents 5 and 6** run in parallel (both depend on Agent 4 output, neither depends on the other)
- **Pain Point sub-pipeline (2A → review → 2B)**: Agent 2A produces granular decomposition, the painpoint-reviewer validates it, then Agent 2B clusters the reviewed output. Run these three sequentially within the pipeline.
- **Se CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS habilitado**: Em vez de rodar 2A → review → 2B sequencialmente, spawnar os 3 como agent team. Cada um traz sua perspectiva e debatem a decomposição/validação/clustering simultaneamente. Resultado mais robusto, ~2x tempo.

## Completion Checks

| Agent | Skill Name | Check | Key Output |
|-------|-----------|-------|------------|
| Q1 | `agent-q1-data-scout` | File exists | `/1-problem/0-data-landscape/data-landscape.md` |
| Q2 | `agent-q2-hypothesis-generator` | File exists | `/1-problem/0-data-landscape/hypotheses.md` |
| Script | `interview-script-generator` | File exists | `/0-documentation/0a-projectdocs/interview-script.md` |
| 0 | `agent-0-context-specialist` | File exists | `/0-documentation/broad-context.md` |
| 1 | `agent-1-research-specialist` | All interviews processed | `/1-problem/1a-interview-analysis/*.md` |
| 2A | `agent-2a-granular-specialist` | Decomposition complete | `/1-problem/1b-painpoints/1b0-granular/all-painpoints-granular.md` |
| Review | `painpoint-reviewer` | Review complete | `/1-problem/1b-painpoints/1b0-granular/*-review.md` |
| 2B | `agent-2b-clustering-specialist` | Clusters formed | `/1-problem/1b-painpoints/painpoint-mapping.md` |
| 2C | `agent-2c-jtbd-specialist` | JTBD extracted | `/1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md` |
| 3 | `agent-3-journey-mapper` | Journey maps created | `/1-problem/1c-asis-journey/1c2-asis-breakdown/*.md` |
| 4 | `agent-4-journey-consolidation` | Consolidated journey | `/1-problem/1c-asis-journey/asis-journey.md` |
| 5 | `agent-5-report-generator` | Reports generated | `/1-problem/1d-problem-output/pain-report.md` + `problem-report.md` |
| 6 | `agent-6-visual-designer` | Visuals created | `/1-problem/1d-problem-output/journey-output.md` |
| S6 | `solution-6-ideation` | Opportunities identified | `/2-solution/2a-opportunities/*.md` |
| S7 | `solution-7-experience` | To-Be journey designed | `/2-solution/2b-tobe-journey/*.md` |
| S8 | `solution-8-concept` | Concepts documented | `/2-solution/2c-solution-concepts/*.md` |
| S9 | `solution-9-prioritization` | Prioritization complete | `/2-solution/2d-prioritization/*.md` |
| S10 | `solution-10-communication` | Communication materials | `/2-solution/2e-roadmap/*.md` and `/2-solution/2f-solution-output/*.md` |
| 11 | `agent-11-confluence` | Confluence pages | `/3-delivery/confluence/*.md` |
| 12 | `agent-12-jira` | Jira backlog | `/3-delivery/jira/*.md` |

## Error Handling

- **Missing skill file**: If `.claude/skills/{agent-name}/SKILL.md` does not exist, check `.cursor/skills/{agent-name}/SKILL.md` as fallback. If neither exists, report the error and skip the agent.
- **Agent failure**: If an agent produces no output or errors, report the failure, ask the user whether to retry, skip, or abort.
- **Missing dependencies mid-pipeline**: If an agent's expected input from a previous agent is missing, halt and report which upstream agent may have failed.

## Post-Phase Actions

After completing a phase:
1. Run the `guardrails-validator` skill on all outputs from that phase
2. Present a summary of all files created
3. Suggest: "Quer exportar pra apresentação? Use `/export-presentation` pra gerar HTML/PDF pro stakeholder."
4. Suggest: "Use `/evidence-board` pra ver o mapa de evidências ou `/discovery-map` pra seu progresso."
5. Ask the user whether to proceed to the next phase (if applicable)
6. If active is a domain initiative, suggest: "Quer salvar os aprendizados no dominio? Rode `python3 _tools/project.py harvest`"
