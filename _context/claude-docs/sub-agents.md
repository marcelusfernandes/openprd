# Subagents no Claude Code — Guia de Referência

> Documento baseado em [Claude Code - Sub-agents Documentation](https://code.claude.com/docs/en/sub-agents).

---

## 1. O que são Subagents no Claude Code

**Subagents** são assistentes de IA especializados que executam tipos específicos de tarefas. Cada subagent opera em sua própria janela de contexto, com um system prompt customizado, ferramentas específicas e permissões independentes.

### Características principais

- **Execução independente**: Quando Claude encontra uma tarefa que corresponde à descrição de um subagent, ele delega para esse subagent, que trabalha de forma autônoma e retorna os resultados.
- **Contexto isolado**: Cada subagent roda em seu próprio contexto — diferente de [agent teams](https://code.claude.com/en/agent-teams), que coordenam sessões separadas.
- **Decisão automática de delegação**: Claude usa a `description` de cada subagent para decidir **quando** delegar tarefas. Ao criar um subagent, escreva uma descrição clara.

### Benefícios

| Benefício | Descrição |
|-----------|-----------|
| Controle de custos | Rotear tarefas para modelos mais rápidos e baratos (ex: Haiku) |
| Especialização | Comportamento focado via system prompts para domínios específicos |
| Reuso | Configurações reutilizáveis entre projetos com subagents em nível de usuário |
| Restrições | Limitar quais ferramentas um subagent pode usar |
| Preservação de contexto | Manter exploração e implementação fora da conversa principal |

---

## 2. Subagents Built-in (Explore, Plan, General-purpose)

O Claude Code inclui subagents nativos que Claude usa automaticamente quando apropriado. Cada um herda as permissões da conversa pai com restrições adicionais de ferramentas.

### Explore

Agente rápido e somente leitura otimizado para busca e análise de codebase.

| Aspecto | Detalhe |
|---------|---------|
| **Propósito** | Descoberta de arquivos, busca de código, exploração de codebase |
| **Ferramentas** | Somente leitura (sem Write e Edit) |
| **Modelo** | Haiku (rápido, baixa latência) |
| **Uso** | Claude delega quando precisa buscar ou entender o codebase sem fazer alterações |

**Níveis de minuciosidade** ao invocar Explore: `quick` (buscas pontuais), `medium` (exploração balanceada), `very thorough` (análise abrangente).

### Plan

Agente de pesquisa usado durante o [plan mode](https://code.claude.com/en/common-workflows#use-plan-mode-for-safe-code-analysis) para reunir contexto antes de apresentar um plano.

| Aspecto | Detalhe |
|---------|---------|
| **Propósito** | Pesquisa no codebase para planejamento |
| **Ferramentas** | Somente leitura |
| **Modelo** | Herda da conversa principal |
| **Uso** | Previne nesting infinito (subagents não podem gerar outros subagents) |

### General-purpose

Agente capaz para tarefas complexas que exigem exploração e ação.

| Aspecto | Detalhe |
|---------|---------|
| **Propósito** | Pesquisa complexa, operações multi-etapa, modificações de código |
| **Ferramentas** | Todas as ferramentas |
| **Modelo** | Herda da conversa principal |
| **Uso** | Requer exploração + modificação, raciocínio complexo ou múltiplas etapas dependentes |

### Outros agentes built-in

| Agente | Modelo | Quando Claude usa |
|--------|--------|-------------------|
| Bash | Herda | Executar comandos de terminal em contexto separado |
| statusline-setup | Sonnet | Ao executar `/statusline` para configurar status line |
| Claude Code Guide | Haiku | Perguntas sobre recursos do Claude Code |

---

## 3. Como criar subagents customizados (Frontmatter YAML + system prompt)

Subagents são definidos em arquivos Markdown com **YAML frontmatter** para configuração, seguido do **system prompt** em Markdown.

### Estrutura básica

```markdown
---
name: code-reviewer
description: Revisa código para qualidade e melhores práticas
tools: Read, Glob, Grep
model: sonnet
---

Você é um revisor de código. Quando invocado, analise o código e forneça
feedback específico e acionável sobre qualidade, segurança e melhores práticas.
```

- **Frontmatter**: metadados e configuração do subagent
- **Corpo**: system prompt que guia o comportamento (o subagent recebe **apenas** isso + detalhes básicos de ambiente, não o prompt completo do Claude Code)

### Métodos de criação

| Método | Descrição |
|--------|-----------|
| **Comando `/agents`** | Interface interativa recomendada para criar e gerenciar subagents |
| **Arquivo manual** | Criar arquivos `.md` diretamente nos diretórios apropriados |
| **CLI `--agents`** | Passar JSON ao iniciar Claude Code para subagents efêmeros |
| **Plugins** | Subagents distribuídos via plugins |

### Quickstart via `/agents`

1. Execute `/agents`
2. Selecione **Create new agent** → **User-level** (salva em `~/.claude/agents/`)
3. Escolha **Generate with Claude** e descreva o subagent
4. Configure **tools**, **model** e **cor**
5. Salve — disponível imediatamente (sem restart)

---

## 4. Campos de configuração

### Tabela de campos suportados

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Sim | Identificador único (minúsculas e hífens) |
| `description` | Sim | Quando Claude deve delegar a este subagent |
| `tools` | Não | [Ferramentas](https://code.claude.com/docs/en/sub-agents#available-tools) disponíveis. Herda todas se omitido |
| `disallowedTools` | Não | Ferramentas negadas (removidas da lista herdada/especificada) |
| `model` | Não | `sonnet`, `opus`, `haiku` ou `inherit`. Padrão: `inherit` |
| `permissionMode` | Não | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | Não | Número máximo de turnos agentic antes de parar |
| `skills` | Não | [Skills](https://code.claude.com/en/skills) injetadas no contexto na inicialização |
| `mcpServers` | Não | Servidores MCP disponíveis ao subagent |
| `hooks` | Não | [Lifecycle hooks](https://code.claude.com/docs/en/sub-agents#define-hooks-for-subagents) escopados |
| `memory` | Não | `user`, `project` ou `local` para memória persistente |
| `background` | Não | `true` = execução em background. Padrão: `false` |
| `isolation` | Não | `worktree` = executar em [git worktree](https://code.claude.com/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) temporário e isolado |

### Escopo e prioridade

| Local | Escopo | Prioridade | Como criar |
|-------|--------|------------|------------|
| `--agents` (CLI) | Sessão atual | 1 (maior) | JSON ao lançar Claude Code |
| `.claude/agents/` | Projeto atual | 2 | Interativo ou manual |
| `~/.claude/agents/` | Todos projetos | 3 | Interativo ou manual |
| Plugin `agents/` | Onde plugin está habilitado | 4 (menor) | Instalado com [plugins](https://code.claude.com/en/plugins) |

### Exemplo via CLI

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Revisor de código especialista. Usar proativamente após mudanças.",
    "prompt": "Você é um revisor sênior. Foque em qualidade, segurança e melhores práticas.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

### Restringir quais subagents podem ser criados

Com `Agent(agent_type)` é possível limitar quais subagents um agente coordenador pode gerar:

```yaml
tools: Agent(worker, researcher), Read, Bash
```

- **Allowlist**: só `worker` e `researcher` podem ser criados
- `Agent` sem parênteses: permite qualquer subagent
- Omitir `Agent`: bloqueia criação de subagents

> **Nota**: Subagents **não podem** criar outros subagents. `Agent(agent_type)` só aplica ao agente principal (`claude --agent`).

---

## 5. Foreground vs Background execution

| Modo | Comportamento |
|------|---------------|
| **Foreground** | Bloqueia a conversa principal até terminar. Permissões e perguntas de esclarecimento (`AskUserQuestion`) passam para você |
| **Background** | Executa em paralelo enquanto você continua trabalhando. Claude Code pede permissões necessárias **antes** de iniciar; depois disso, auto-nega o que não foi pre-aprovado |

### Background — detalhes

- Permissões são solicitadas **antes** do lançamento
- Se um subagent em background precisar fazer perguntas, a chamada de tool falha, mas o subagent continua
- É possível **retomar** um subagent que falhou por permissões, executando-o em foreground

### Controles

- **Ctrl+B**: colocar tarefa atual em background
- Pedir a Claude: "run this in the background"
- **Desabilitar background globalmente**: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`

---

## 6. Padrões de uso

### 6.1 Isolamento de operações de alto volume

Um dos melhores usos é isolar operações que geram muita saída: testes, documentação, logs etc. O output fica no contexto do subagent; só o resumo relevante volta para a conversa principal.

```
Use um subagent para rodar a suite de testes e reportar apenas os testes
que falharam com suas mensagens de erro
```

### 6.2 Pesquisa paralela

Para investigações independentes, lance vários subagents em paralelo:

```
Pesquise os módulos de autenticação, banco de dados e API em paralelo
usando subagents separados
```

- Cada subagent explora sua área independentemente
- Claude sintetiza os resultados depois
- Funciona melhor quando os caminhos de pesquisa não dependem um do outro
- Para paralelismo prolongado ou além da janela de contexto, considere [agent teams](https://code.claude.com/en/agent-teams)

### 6.3 Encadeamento (chain)

Para fluxos multi-etapa, peça a Claude para usar subagents em sequência. Cada um completa sua tarefa e devolve o resultado; Claude passa o contexto relevante para o próximo.

```
Use o subagent code-reviewer para encontrar problemas de performance,
depois use o subagent optimizer para corrigi-los
```

---

## 7. Persistent memory para subagents

O campo `memory` dá ao subagent um diretório persistente que sobrevive entre conversas. O subagent pode acumular conhecimento ao longo do tempo.

```yaml
---
name: code-reviewer
description: Revisa código para qualidade e melhores práticas
memory: user
---

Você é um revisor de código. Conforme revisa, atualize sua memória de agente
com padrões, convenções e problemas recorrentes que descobrir.
```

### Escopos de memória

| Escopo | Localização | Quando usar |
|--------|-------------|-------------|
| `user` | `~/.claude/agent-memory/` | O subagent deve lembrar aprendizado em todos os projetos |
| `project` | `.claude/agent-memory/` | Conhecimento específico do projeto, versionável |
| `local` | `.claude/agent-memory-local/` | Específico do projeto, mas **não** versionado |

### Efeitos ao habilitar memória

- **Read**, **Write** e **Edit** são habilitados automaticamente
- As primeiras 200 linhas de `MEMORY.md` são incluídas no system prompt
- Instruções de leitura/escrita no diretório de memória são adicionadas ao prompt

### Dicas

- Inclua instruções de memória direto no arquivo do subagent
- Peça ao subagent para atualizar a memória ao concluir: *"Agora que terminou, salve o que aprendeu na sua memória"*
- Peça para consultar a memória antes de começar: *"Revise este PR e consulte sua memória para padrões que já viu"*
- `user` é o escopo recomendado por padrão

---

## 8. Hooks em subagents

Há duas formas de configurar hooks:

1. **`settings.json`**: hooks executados na sessão principal quando subagents iniciam ou terminam
2. **Frontmatter do subagent**: hooks que rodam **apenas** enquanto aquele subagent está ativo

### Hooks no frontmatter

| Evento | Matcher | Quando dispara |
|--------|---------|----------------|
| `PreToolUse` | Nome da tool | Antes do subagent usar uma tool |
| `PostToolUse` | Nome da tool | Depois do subagent usar uma tool |
| `Stop` | (nenhum) | Quando o subagent termina (convertido em `SubagentStop`) |

Exemplo — validação de Bash e linter após edits:

```yaml
---
name: code-reviewer
description: Revisar mudanças com linting automático
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-command.sh $TOOL_INPUT"
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "./scripts/run-linter.sh"
---
```

### Hooks em nível de projeto (settings.json)

| Evento | Matcher | Quando dispara |
|--------|---------|----------------|
| `SubagentStart` | Nome do agente | Quando um subagent começa |
| `SubagentStop` | Nome do agente | Quando um subagent termina |

```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "db-agent",
        "hooks": [
          { "type": "command", "command": "./scripts/setup-db-connection.sh" }
        ]
      }
    ],
    "SubagentStop": [
      {
        "hooks": [
          { "type": "command", "command": "./scripts/cleanup-db-connection.sh" }
        ]
      }
    ]
  }
}
```

### Validação condicional (PreToolUse)

Exemplo: subagent que só permite consultas read-only ao banco. O script recebe JSON via stdin, extrai o comando Bash e usa exit code 2 para bloquear escrita:

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty')
if echo "$COMMAND" | grep -iE '\b(INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE)\b' > /dev/null; then
  echo "Blocked: Only SELECT queries allowed" >&2
  exit 2
fi
exit 0
```

---

## 9. Exemplos práticos

### Code reviewer

Revisão somente leitura, sem modificação de código:

```markdown
---
name: code-reviewer
description: Especialista em code review. Revisa proativamente qualidade, segurança e manutenibilidade.
tools: Read, Grep, Glob, Bash
model: inherit
---

Você é um revisor sênior focado em qualidade e segurança.

Ao ser invocado:
1. Execute git diff para ver mudanças recentes
2. Foque em arquivos modificados
3. Comece a revisão imediatamente

Checklist: clareza, nomenclatura, duplicação, error handling, secrets, validação, testes, performance.

Forneça feedback por prioridade: Crítico | Avisos | Sugestões. Inclua exemplos de correção.
```

### Debugger

Permite análise e correção (inclui Edit):

```markdown
---
name: debugger
description: Especialista em debug para erros, falhas de teste e comportamento inesperado.
tools: Read, Edit, Bash, Grep, Glob
---

Você é um debugger especialista em root cause analysis.

Fluxo: capturar erro/stack → reprodução → localizar falha → aplicar correção mínima → verificar.

Para cada issue: causa raiz, evidências, correção de código, estratégia de teste, recomendações de prevenção.
```

### Data scientist

Domínio específico para análise de dados (usa Sonnet):

```markdown
---
name: data-scientist
description: Especialista em SQL, BigQuery e insights de dados.
tools: Bash, Read, Write
model: sonnet
---

Você é um cientista de dados focado em SQL e BigQuery.

Fluxo: entender requerimento → escrever SQL eficiente → usar bq quando apropriado → resumir e apresentar.

Boas práticas: SQL otimizado, joins adequados, comentários em lógica complexa, recomendações baseadas em dados.
```

### Database query validator

Bash permitido, mas apenas SELECT via PreToolUse hook:

```markdown
---
name: db-reader
description: Executar consultas read-only ao banco. Para análise e relatórios.
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

Você é um analista de dados com acesso read-only. Execute SELECT para responder perguntas.
Não pode modificar dados. Se pedirem INSERT/UPDATE/DELETE, explique que só tem acesso de leitura.
```

---

## 10. Quando usar subagents vs conversa principal

### Prefira a conversa principal quando

- **Latência importa**: subagents iniciam do zero e podem precisar de tempo para reunir contexto
- Mudança rápida e pontual
- Várias fases compartilham muito contexto (planejar → implementar → testar)
- A tarefa exige muito back-and-forth ou refinamento iterativo

### Prefira subagents quando

- O trabalho é **autocontido** e pode retornar um resumo
- Você quer impor restrições específicas de tools ou permissões
- A tarefa gera **output verboso** que não precisa estar no contexto principal

### Alternativas

- **[Skills](https://code.claude.com/en/skills)**: prompts/workflows reutilizáveis que rodam no contexto da conversa principal
- **Subagents encadeados**: quando há delegação sequencial (subagents não criam outros subagents)
- **Agent teams**: paralelismo prolongado ou além da janela de contexto

---

## Recursos adicionais

- [MCP servers](https://code.claude.com/en/mcp) — expor ferramentas externas aos subagents
- [Agent SDK (headless)](https://code.claude.com/en/headless) — rodar Claude Code de forma programática (CI/CD)
- [Plugins](https://code.claude.com/en/plugins) — distribuir subagents em equipe ou projetos

---

*Documentação criada em 09/03/2025. Fonte: [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents).*
