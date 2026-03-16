---
name: cross-phase-validator
description: Spawns a validation team of 3 agents with different perspectives to debate output quality between pipeline phases. More thorough than single-agent guardrails check.
---

# Cross-Phase Validator — Validação por Debate

## Propósito
Validação profunda entre fases do pipeline. Em vez de 1 validator checando guardrails, 3 agentes com perspectivas diferentes debatem a qualidade.

## Quando Usar
- Entre Phase 1 → Phase 2 (pain points robustos o suficiente pra idear?)
- Entre Phase 2 → Phase 3 (soluções prontas pra virar Jira stories?)
- Antes de /export-presentation (output confiável pra stakeholder?)
- O PM pode chamar /cross-phase-validator a qualquer momento

## Os 3 Validadores

### Guardrails Enforcer
- Checa: todas as tags [Source:], [AI estimation], [Assumption:] presentes?
- Checa: referências internas resolvem pra arquivos reais?
- Checa: linguagem conservadora, sem claims absolutos?
- Foco: COMPLIANCE

### Consistency Checker
- Checa: pain points de Phase 1 aparecem nas oportunidades de Phase 2?
- Checa: JTBDs linkados aos clusters corretos?
- Checa: métricas do data-landscape refletidas nos reports?
- Foco: COERÊNCIA entre fases

### Stakeholder Fit Reviewer
- Checa: output é apresentável pra VP sem edição?
- Checa: TL;DR existe e é claro?
- Checa: revenue impact calculado (se dados disponíveis)?
- Checa: nível de detalhe adequado ao público?
- Foco: USABILIDADE do output

## Fluxo
1. Spawnar 3 subagents em paralelo (um por validador)
2. Cada um escreve findings em `_exports/validation/{validator}-findings.md`
3. Spawnar agent de síntese que lê os 3 e gera consenso
4. Output: `_exports/validation/cross-phase-report.md` com:
   - Compliance: PASS/FAIL (lista de violações)
   - Coerência: X/10 (gaps entre fases)
   - Stakeholder fit: X/10 (readiness pra apresentar)
   - Recomendação: "Pronto pra avançar" ou "Corrigir X antes de prosseguir"

## Integração com Pipeline
O /start-workflow pode invocar este skill entre fases no modo step-by-step:
"Quer validação profunda antes de avançar? (leva ~2 min extra)"
