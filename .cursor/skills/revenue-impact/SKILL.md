---
name: revenue-impact
description: Calculates estimated revenue impact of pain points and opportunities. Bridges discovery insights to business decisions with conservative financial framing.
---

# Revenue Impact Calculator

## Propósito

Transforma pain points e oportunidades de discovery em estimativas de impacto financeiro. Sem revenue impact, output é exercício acadêmico que não move decisão. Esta skill fecha essa lacuna com framing conservador e rastreável.

## Inputs

1. **Pain report e/ou clusters** de `1-problem/` (arquivos de Agent 2B, Agent 5, ou pain-report)
2. **Oportunidades** de `2-solution/` (arquivos de Solution Agents 6-9, se disponíveis)
3. **Dados de contexto** — perguntar ao PM se não disponíveis:
   - Qual a base de usuários afetados (total ou por segmento)?
   - Qual a receita média por usuário (ARPU) mensal?
   - Quais métricas de conversão/retenção atuais? (se não tiver, usar estimativas conservadoras)

## Workflow

### Passo 1: Coletar Inputs
1. Ler arquivos de `1-problem/` — identificar pain point clusters com severidade
2. Ler arquivos de `2-solution/` — identificar oportunidades priorizadas (se existirem)
3. Se dados de usuários/receita não foram fornecidos, perguntar ao PM

### Passo 2: Mapear Impacto por Cluster/Oportunidade
Para cada pain point cluster ou oportunidade:
1. **Usuários afetados** — extrair de analytics ou input do PM; se ausente, tagar `[AI estimation based on severity distribution]`
2. **Taxa atual** — conversão, retenção ou eficiência relevante ao cluster
3. **Potencial de melhoria** — estimativa CONSERVADORA (usar faixa baixa-alta)
4. **Receita por usuário** — ARPU fornecido ou `[AI estimation based on segment]`
5. **Confiança** — Alta (dados reais), Média (dados parciais + estimativa), Baixa (estimativa pura)

### Passo 3: Calcular e Gerar Tabela

| Oportunidade | Usuários Afetados | Taxa Atual | Potencial | Est. Impacto Anual | Confiança |
|---|---|---|---|---|---|
| [nome do cluster] | X.XXX | Y% | Y+Z% | R$ faixa-baixa — faixa-alta | Alta/Média/Baixa |

**Fórmula:** `Impacto Anual = Usuários Afetados × ARPU × 12 × (Taxa Potencial - Taxa Atual)`

Sempre apresentar como **faixa** (conservador — otimista), nunca valor único.

### Passo 4: Gerar Output

Salvar em `_exports/revenue-impact.md` com seções:
1. **Header** — Projeto, Data, Status: `[AI estimation — requires PM validation]`
2. **Disclaimer** — projeções conservadoras, valores [AI estimation] requerem validação
3. **Resumo Executivo** — 2-3 frases: maior oportunidade, impacto total, confiança geral
4. **Tabela de Impacto** — tabela do Passo 3
5. **Premissas e Fontes** — tabela: Premissa | Valor | Fonte | Tag
6. **Detalhamento por Oportunidade** — 3-5 linhas por item explicando racional
7. **Limitações** — custos não inclusos, efeitos compostos não modelados, assume execução completa

## Regras — EXTRA CONSERVADOR

1. **NUNCA** valor único — sempre faixa (conservador — otimista)
2. **TODA** estimativa DEVE ter tag: `[AI estimation based on X]` ou `[Source: arquivo.md]`
3. **TODA** premissa na seção Premissas e Fontes
4. **Usar**: "Potencial estimado de", "Faixa projetada entre", "Sugere impacto na ordem de"
5. **PROIBIDO**: "vai gerar", "economia garantida", "retorno comprovado", "ROI de X%"
6. **Confiança Baixa** = `⚠️ Estimativa com dados insuficientes — validar antes de usar`
7. **Sem dados = sem número** — escrever "Dados insuficientes para estimar"
8. Seguir `rules/guardrails.md` integralmente

## Linguagem

**Aprovada:** "Potencial estimado na faixa de R$50k — R$120k anuais `[AI estimation based on ARPU de R$80 e 2.000 usuários]`"
**Rejeitada:** "Vai gerar R$500k", "ROI de 340%", "Economia garantida de R$1.2M"
