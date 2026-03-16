---
name: guardrails-validator
description: Validates agent outputs for data integrity compliance. Checks for untagged financial claims, unsourced performance metrics, and missing attribution. Use when validating outputs, running guardrail checks, or the user says validacao.
---

# Guardrails Validator

## Purpose
On-demand validation of agent outputs for data integrity. Complements the deterministic hook in `.cursor/scripts/validate-guardrails.py`.

## When to Use
- User requests validation ("validacao", "validate", "check guardrails")
- Before finalizing any phase deliverables
- After manual edits to output files

## Validation Checklist

### Critical (Block Delivery)
- [ ] No untagged dollar amounts ($X without `[AI estimation]`)
- [ ] No specific ROI percentages without methodology
- [ ] No invented quotes or data
- [ ] No misattributed sources

### Warning (Require Fix)
- [ ] All `[AI estimation]` tags present where needed
- [ ] Source references specific (not vague)
- [ ] No overly confident language ("will", "guaranteed")
- [ ] Assumptions marked with `[Assumption: ...]`

### Advisory (Best Practice)
- [ ] Conservative language throughout
- [ ] Methodology detail in estimation tags
- [ ] Source attribution clarity

## How to Run
1. Specify target: a file, a folder (e.g., `/1-problem/`), or entire project
2. Read each file and check against the checklist above
3. Report violations with exact location and suggested fix
4. Use the script: `python3 .cursor/scripts/validate-guardrails.py` for automated checks

## Templates
- [references/conservative-estimation-guide.md](references/conservative-estimation-guide.md)
- [references/guardrail-validation-checklist.md](references/guardrail-validation-checklist.md)
- [references/template-quality-assessment.md](references/template-quality-assessment.md)

## Gate Automatico (pos-agente)

Apos cada agente do pipeline completar, rodar automaticamente estas verificacoes no output:

### Checks obrigatorios (falha = bloqueia pipeline)
1. Todo claim tem `[Source: filename.md]` → contar claims sem source
2. Nenhum valor financeiro sem `[AI estimation]` → regex scan
3. Nenhuma percentagem sem fonte → regex scan
4. Arquivo de output existe e tem >10 linhas

### Checks de qualidade (warning, nao bloqueia)
5. Pelo menos 3 fontes diferentes citadas
6. Pelo menos 1 quote de entrevista
7. Tags `[Assumption: requires validation]` presentes quando apropriado

### Output do gate
Se passa: "✓ Quality gate passed (7/7 checks)"
Se falha: "✗ Quality gate FAILED: [lista de checks que falharam]. Corrigir antes de prosseguir."

## Readiness Check (entre fases)

Rodar entre transições de fase para avaliar completude antes de avançar.

### Como executar
1. Identificar a fase atual e a próxima fase desejada
2. Rodar o checklist correspondente (ver CLAUDE.md → Modelo de Completude)
3. Para cada item, verificar existência e qualidade do artefato:
   - Arquivo existe? → `Glob` para localizar
   - Conteúdo mínimo? → `Read` e checar tamanho/conteúdo
   - Referências válidas? → Extrair `[Source: X]` e verificar se arquivo X existe
4. Reportar readiness score: "{fase}: {N}/{total} itens completos"

### Checklists por transição

**Pré-Discovery → Phase 1:**
- [ ] `product-context.md` existe e tem >50 palavras
- [ ] Pelo menos 1 fonte de dados disponível (entrevista, analytics, pesquisa)
- [ ] Projeto registrado em `projects/registry.json`

**Phase 1 → Phase 2:**
- [ ] `broad-context.md` existe e tem >100 palavras
- [ ] Pelo menos 3 entrevistas analisadas (checar `1-problem/`)
- [ ] Pain points clusterizados com evidências
- [ ] Todas as referências `[Source: X]` resolvem pra arquivos reais
- [ ] Revenue impact estimado (ou justificativa de por que não)

**Phase 2 → Phase 3 / Export:**
- [ ] Oportunidades linkadas a pain points específicos
- [ ] MVP scope definido com priorização
- [ ] Métricas de sucesso definidas
- [ ] TL;DR existe no pain report
- [ ] Sem claims financeiros sem tag `[AI estimation]`
- [ ] Revenue impact calculado (se dados disponíveis)

### Comportamento do readiness check
- NUNCA bloquear o avanço — apenas informar e sugerir
- Sugerir ações específicas para itens faltantes ("Quer que eu rode /revenue-impact?")
- Se readiness < 60%: alertar que outputs podem ficar incompletos
- Se readiness >= 80%: confirmar que está pronto pra avançar

## Approved Language Patterns
- Financial: "Substantial/High/Moderate investment", "Strong ROI potential"
- Performance: "Substantial improvement `[AI estimation based on X]`"
- Tags: `[Source: file.md]`, `[AI estimation based on X]`, `[Assumption: X]`, `[Uncertain: requires validation]`
