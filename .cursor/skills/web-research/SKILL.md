---
name: web-research
description: Researches online content about the PM's product, market, competitors, and public benchmarks. Uses WebSearch and WebFetch to gather external context for discovery.
user-invocable: true
---

# Web Research — Pesquisa de Contexto Externo

## Propósito
Pesquisar online sobre o produto do PM, mercado, concorrentes e benchmarks públicos para enriquecer o discovery com dados externos reais.

## Triggers
- PM diz "pesquisa sobre meu produto", "benchmark do mercado", "o que os concorrentes fazem"
- `/pair` sugere pesquisa baseado no contexto da conversa
- Agent 0 enriquece broad-context com dados de mercado

## Capacidades

### 1. Product Research
- Buscar produto/empresa do PM online (reviews, percepção pública, menções)
- Output: `0-documentation/0a-projectdocs/product-research.md`

### 2. Competitor Analysis
- Buscar concorrentes mencionados pelo PM ou encontrados via pesquisa
- Comparar: features, posicionamento, pricing (dados públicos)
- Output: `0-documentation/0a-projectdocs/competitor-research.md`

### 3. Market Benchmarks
- Buscar benchmarks da indústria relevantes ao domínio do PM
- Ex: "SaaS B2B onboarding benchmark", "e-commerce conversion rates 2026"
- Output: `0-documentation/0a-projectdocs/market-benchmarks.md`

### 4. Public Research & Reports
- Buscar pesquisas, surveys, reports existentes sobre o tema
- Ex: Nielsen, Baymard, Forrester (findings públicos)
- Output: `0-documentation/0a-projectdocs/public-research.md`

## Workflow

```
1. PM descreve o que quer pesquisar (ou /pair sugere)
2. WebSearch com queries relevantes (3-5 queries)
3. WebFetch nos top 3-5 resultados por query
4. Extrair e organizar findings
5. Salvar em 0-documentation/0a-projectdocs/
6. Resumir: "Encontrei X sobre seu produto, Y benchmarks, Z concorrentes"
```

## Integração com Pipeline
- Agent 0 (Context Specialist) lê os arquivos de research ao criar broad-context.md
- `/pair` pode sugerir research durante a conversa
- `competitive-analyst` skill aprofunda análise competitiva estruturada

## Guardrails
- Citar fonte com URL: `[Source: url, accessed YYYY-MM-DD]`
- Marcar dados com data: `[Data from: YYYY]`
- Não apresentar dados pagos/privados como públicos
- Linguagem conservadora: "Benchmarks públicos sugerem..." não "O mercado tem..."
- Marcar estimativas: `[AI estimation based on X]`

## Output Format
```markdown
# {Tipo de Pesquisa} — {Produto/Tema}
**Data:** YYYY-MM-DD
**Queries utilizadas:** lista de queries

## Findings
### Finding 1
- Dado [Source: url, accessed YYYY-MM-DD]

## Resumo
- 3-5 insights principais

## Limitações
- Dados públicos apenas, possíveis vieses de fonte
```
