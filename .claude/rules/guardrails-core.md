# Guardrails Core — Data Integrity

Regras SEMPRE ativas para todo output gerado em `1-problem/`, `2-solution/`, `3-delivery/`.

## Afirmações Financeiras
- Nunca usar valores em dólar/real sem tag: `[AI estimation based on X]`
- Linguagem conservadora: "Melhoria substancial", "Potencial de redução significativo"

## Atribuição de Fontes
- Toda afirmação deve ter `[Source: filename.md]` ou `[AI estimation based on X]`
- Sem fonte = não incluir

## Marcação de Suposições
- Suposições devem ser tagadas: `[Assumption: requires validation]`
- Nunca apresentar suposições como fatos

## Linguagem
- Proibido: "vai reduzir 50%", "economia de R$X", "garantia de melhoria"
- Permitido: "Potencial de melhoria substancial", "Estimativa sugere redução significativa"

## Imutabilidade
- Outputs de fases completas NÃO são modificados
- Novas iterações criam novos arquivos com sufixo v2, v3, etc.
