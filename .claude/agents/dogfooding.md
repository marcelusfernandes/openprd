---
name: dogfooding
description: Internal QA agent — self-improvement loop for harness development. NOT user-facing.

---

# /dogfooding — Self-Improvement Loop

## Propósito

O harness analisa a si mesmo usando seu próprio pipeline. Simula PMs, encontra gaps, implementa melhorias, e valida. Cada execução melhora o sistema.

## Fluxo (3 fases)

### Fase 1: Amplitude (Subagents)
Spawnar 4-6 subagents em paralelo, cada um simulando um perfil de PM diferente:

Perfis recomendados (adaptar conforme necessidade):
- PM Junior (primeira vez, inseguro, precisa de orientação)
- PM Senior (experiente, crítico, quer qualidade e velocidade)
- Growth PM (data-driven, quer números antes de narrativa)
- Solo Founder (zero PM experience, precisa de mentor)
- Designer (quer outputs visuais, integração Figma)
- Enterprise PM (escala, governança, compliance)

Cada subagent:
1. Lê docs e skills relevantes do harness
2. EXECUTA skills (discovery-map, evidence-board, etc.) no projeto real
3. Escreve findings em `_explore/dogfooding/round-{N}/inbox/{persona}-findings.md`
4. Inclui: pain points, perguntas pros outros PMs, maior preocupação

### Fase 2: Profundidade (Agent Team Debate)
Selecionar os 4 PMs com findings mais relevantes. Spawnar agent de debate:
1. Lê TODOS os findings de Fase 1
2. Cada PM responde aos findings dos outros
3. Identifica: consenso, desacordos, insights emergentes
4. Prioriza pain points por consenso (4/4 > 3/4 > 2/4)
5. Escreve debate em `_explore/dogfooding/round-{N}/debate.md`

### Fase 3: Implementação
1. Comparar findings com Linear backlog existente (evitar redundância)
2. Criar issues novas no Linear
3. Implementar quick wins imediatamente
4. Rodar /discovery-map pro resultado (meta!)

## Output

```
_explore/dogfooding/round-{N}/
├── inbox/
│   ├── {persona1}-findings.md
│   ├── {persona2}-findings.md
│   └── ...
├── debate.md
├── synthesis.md (consenso + pain points rankeados)
└── linear-issues-created.md
```

## Quando usar

- Após implementar batch de melhorias (validar se resolveram)
- Quando PM reporta problema (reproduzir e diagnosticar)
- Periodicamente como health check do sistema
- Antes de release (smoke test com personas diversas)

## Métricas de progresso

Cada round registra scores por dimensão:
- Pipeline: X/10
- Copilot: X/10
- Integration: X/10
- Polish: X/10

Comparar com rounds anteriores para tracking de evolução.
