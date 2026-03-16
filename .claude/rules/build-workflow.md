# Build Workflow — Regras de Construção Autônoma

## Ciclo de Construção

Toda construção segue o ciclo: **Build → Test → Log → Commit**

1. **Build**: Criar/modificar artefatos usando subagents quando apropriado
2. **Test**: Validar formato, conteúdo e guardrails
3. **Log**: Registrar em `_context/claude/logs/YYYY-MM-DD-{desc}.md`
4. **Commit**: Commitar apenas arquivos da construção (nunca `git add .`)

## Dual-Platform

Ao criar skills, agents ou rules:
1. Primeiro criar para Claude Code (`.claude/`)
2. Depois criar espelho para Cursor (`.cursor/`)
3. Testar apenas Claude Code (ambiente atual)
4. Registrar ambos no log

## Delegação

- Pesquisa de referência → subagent Explore (background se não bloqueia)
- Construção de artefato → subagent general-purpose (foreground)
- Validação → subagent com tools restritas (Read, Grep, Glob)
- Logging → pode ser feito inline (é rápido)

## Proteção de Contexto

- NUNCA ler arquivos grandes inteiros na conversa principal
- Delegar leitura de referências longas para subagents Explore
- Manter janela principal para orquestração e decisões
- Usar `context: fork` em skills que precisam de pesquisa profunda
