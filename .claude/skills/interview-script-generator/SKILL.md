---
name: interview-script-generator
description: Generates targeted interview scripts from data-backed hypotheses. Bridges quantitative findings to qualitative investigation.
---

# Gerador de Roteiro de Entrevista

Transforma hipoteses do Agent Q2 em roteiros de entrevista estruturados e prontos para uso.

## Input

Ler o output do Agent Q2:
- `/1-problem/0-data-landscape/hypotheses.md`

Se o arquivo nao existir, abortar: "Input obrigatorio ausente: hypotheses.md. Execute o Agent Q2 (Hypothesis Generator) primeiro."

## Workflow

1. Ler `/1-problem/0-data-landscape/hypotheses.md`
2. Extrair todas as hipoteses (HYP-1, HYP-2, etc.) e suas classificacoes
3. Gerar roteiro estruturado com 4 blocos: abertura, core, aprofundamento, fechamento
4. Para cada hipotese, gerar 3-5 perguntas abertas de validacao
5. Adicionar dicas para o entrevistador
6. Salvar output em `/0-documentation/0a-projectdocs/interview-script.md`

## Estrutura do Output

```markdown
# Roteiro de Entrevista — Discovery

**Gerado por:** Interview Script Generator
**Data:** {YYYY-MM-DD}
**Baseado em:** hypotheses.md ({N} hipoteses)
**Duracao estimada:** {30-60} minutos

---

## Dicas para o Entrevistador

- Nunca induza respostas — pergunte "como voce faz X?" nao "voce acha X dificil?"
- Peca exemplos concretos — observe emocoes — anote citacoes literais
- Silencios sao aliados — espere 5s antes de reformular

---

## Bloco 1: Abertura (5 min)

1. Me conta sobre seu papel e o que voce faz no dia a dia?
2. Ha quanto tempo voce trabalha com {dominio}?
3. Como e um dia tipico quando lida com {processo relevante}?

---

## Bloco 2: Investigacao por Hipotese

### HYP-{N}: {Titulo}
**Objetivo:** Validar/invalidar — "{declaracao resumida}"

1. {Pergunta aberta comportamental}
2. {Pergunta sobre frequencia/impacto}
3. {Pergunta sobre alternativas/workarounds}
4. {Pergunta situacional — "Me conta a ultima vez que..."}
5. {Pergunta sobre consequencias}

> Dica: {orientacao especifica para esta hipotese}

{Repetir para cada hipotese}

---

## Bloco 3: Aprofundamento (10 min)

Probing para usar a qualquer momento:
- "Pode me dar um exemplo concreto?" / "Me conta mais..."
- "Como isso afeta seu trabalho?" / "O que acontece quando da errado?"
- "Como resolve isso hoje?" / "Se pudesse mudar uma coisa, qual seria?"

---

## Bloco 4: Fechamento (5 min)

1. Tem algo que eu nao perguntei e voce acha importante?
2. Quem mais voce recomendaria que eu conversasse?
3. Se pudesse resolver um unico problema dos que falamos, qual seria?

---

## Mapa Hipotese-Perguntas

| Hipotese | Perguntas (Bloco 2) | Classificacao |
|----------|---------------------|---------------|
| HYP-{N}  | Q1, Q2, Q3...       | {tipo}        |

## Notas Metodologicas

- Roteiro baseado em hypotheses.md [Source: hypotheses.md]
- Perguntas desenhadas como abertas e nao-indutivas
- Ordem sugerida; adaptar conforme fluxo da conversa
```

## Regras de Perguntas

**Fazer:** perguntas abertas ("como", "me conta", "o que"); pedir comportamentos passados, nao opinioes; explorar frequencia, impacto e workarounds atuais.

**Nao fazer:** perguntas fechadas (sim/nao); perguntas indutivas; multiplas perguntas em uma so; jargao tecnico; sugerir respostas.

## Guardrails

- Toda pergunta rastreavel a pelo menos uma hipotese
- Citar fonte: `[Source: hypotheses.md]` | Suposicoes: `[Assumption: requires validation]`
- Nunca inventar dados — usar apenas informacoes do input
- Adaptar linguagem ao dominio identificado nas hipoteses

## Checklist Final

1. hypotheses.md lido integralmente
2. Toda hipotese tem 3-5 perguntas dedicadas
3. 4 blocos presentes: abertura, core, aprofundamento, fechamento
4. Zero perguntas fechadas ou indutivas
5. Mapa hipotese-perguntas completo e fontes citadas
