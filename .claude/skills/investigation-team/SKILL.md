---
name: investigation-team
description: Spawns a team of 3-4 agents with competing hypotheses to investigate a problem. Each brings a different angle. Debate converges on root cause.
user-invocable: true
---

# Investigation Team — Hipóteses Concorrentes

## Propósito
Quando o PM tem um problema pra investigar (initiative tipo "investigation"), spawnar team de agentes com ângulos diferentes. Cada um investiga uma hipótese. O debate converge na causa raiz.

## Quando Usar
- PM cria initiative com --size investigation
- PM diz "preciso investigar por que X está acontecendo"
- /pair identifica problema complexo sem causa clara

## Fluxo

### 1. PM descreve o problema
"Usuários estão abandonando o checkout no step 3"

### 2. Copiloto gera 3-4 hipóteses
Baseado no contexto do produto + dados disponíveis:
- H1: "UX confusa — botão de pagamento não é visível"
- H2: "Performance — step 3 demora >3s pra carregar"
- H3: "Trust — falta selos de segurança antes do pagamento"
- H4: "Pricing — custo de frete revelado tarde demais"

### 3. Spawnar 3-4 investigators em paralelo
Cada um:
- Recebe SUA hipótese como premissa
- Pesquisa evidências a favor E contra
- Lê dados disponíveis (data-landscape, entrevistas, analytics)
- Se tiver web-research disponível, pesquisa benchmarks
- Escreve findings em `_explore/investigation/{hipotese}-findings.md`

### 4. Debate
Spawnar agent de debate que:
- Lê todos os findings
- Cada investigator responde aos findings dos outros
- Identifica: consenso, contradições, evidências cruzadas
- Converge: "A causa raiz mais provável é X, baseado em Y evidências"

### 5. Output
`_explore/investigation/report.md`:
- Problema investigado
- Hipóteses avaliadas (validada/invalidada/inconclusiva)
- Causa raiz mais provável + evidências
- Recomendação de ação
- Próximo passo sugerido (entrevista focada? A/B test? mais dados?)

## Integração
- /pair pode sugerir: "Problema complexo. Quer que eu spawne um investigation team?"
- Resultado alimenta o pipeline se PM decidir fazer discovery formal depois
- Domain _knowledge/ recebe os learnings via harvest
