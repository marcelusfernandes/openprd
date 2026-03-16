---
name: evidence-registry
description: Maintains a central registry of all evidence sources, insights, and connections. Foundation for cross-skill references and evidence traceability.
user-invocable: true
---

# Evidence Registry — Registro Central de Evidencias

## Proposito

Registro centralizado de TODAS as evidencias do discovery. Fundacao pra cross-references entre skills — qualquer agente consulta o registry pra encontrar fontes, conexoes e confianca. PM invoca `/evidence-registry` pra (re)gerar.

## Fluxo

### 1. Escanear Diretorios

Buscar **todos** os `.md` no projeto ativo:
- `0-documentation/**/*.md` — docs, entrevistas brutas, roteiros
- `1-problem/**/*.md` — analises, pain points, clusters, JTBDs, hipoteses
- `2-solution/**/*.md` — oportunidades, conceitos, priorizacao
- `_exports/**/*.md` — outputs de outras skills

### 2. Extrair Evidencias

Pra cada arquivo, extrair titulo, key insight (1 linha) e classificar tipo:
- `Interview` — em `1a-interview-analysis/` ou padrao de entrevista
- `Data Pull` — em `0-data-landscape/` ou com metricas
- `Pain Point` — em `1b-painpoints/`
- `Hypothesis` — com hipoteses identificadas
- `Opportunity` — em `2-solution/`
- `Decision` — com decisoes registradas
- `Quote` — citacoes diretas de entrevistas

**Confianca:** Alta (3+ fontes corroboram), Media (1-2), Baixa (fonte unica).

### 3. Detectar Conexoes

Escanear por tags `[Source: X]` e referencias cruzadas:
- Arquivo A cita `[Source: B.md]` → conexao A←B
- Multiplos citando mesma fonte → aumentar confianca dela

### 4. Gerar Tabela Registry

| Evidence ID | Type | Source File | Key Insight | Connected To | Confidence | Date |
|-------------|------|-------------|-------------|--------------|------------|------|
| EV-001 | Interview | `persona-x.md` | Processo manual gera retrabalho | EV-003, EV-007 | Alta | 2026-01-15 |
| EV-002 | Data Pull | `data-landscape.md` | Taxa de erro 23% no fluxo Y | EV-001 | Media | 2026-01-16 |

**IDs:** `EV-NNN` sequencial por data. **Date:** modificacao do arquivo fonte.

### 5. Salvar Output

Salvar em `_exports/evidence-registry.md`:
```markdown
# Evidence Registry — {Projeto}
**Gerado em:** {data} | **Evidencias:** {N} | **Conexoes:** {M}
## Registry
{tabela}
## Resumo por Tipo
- Interviews: X | Data Pulls: Y | Pain Points: Z | Hypotheses: W | Opportunities: V | Decisions: U | Quotes: T
## Evidencias Orfas (sem conexao)
{candidatas a investigacao}
## Evidencias Hub (mais conectadas)
{top 5 — pontos centrais do discovery}
```

### 6. OpenViking (opcional)

Se MCP `openviking` disponivel, chamar `ov_add_resource` pra cada evidencia com metadata. Se nao, pular silenciosamente.

## Guardrails

- Nunca inventar evidencias ou conexoes — so o que existe nos arquivos
- Manter `[Source: arquivo.md]` em cada linha
- Sem outputs → informar PM e sugerir `/start-workflow`
- Maximo 200 linhas na tabela — agrupar se necessario
