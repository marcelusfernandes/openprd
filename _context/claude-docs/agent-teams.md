# Agent Teams no Claude Code

> Documento de referência sobre orquestração de equipes de agentes Claude Code — baseado na documentação oficial e experimentos da comunidade.

---

## 1. O que são Agent Teams e como diferem de Subagents

### 1.1 Definição de Agent Teams

**Agent Teams** (Equipes de Agentes) permitem coordenar múltiplas instâncias do Claude Code trabalhando em paralelo. Uma sessão age como **team lead** (líder da equipe), coordenando o trabalho, atribuindo tarefas e sintetizando resultados. Os **teammates** (membros) trabalham de forma independente, cada um em sua própria janela de contexto, e se comunicam diretamente entre si.

Principais características:

- **Múltiplas sessões independentes** — cada teammate é uma instância completa do Claude Code
- **Comunicação peer-to-peer** — os teammates podem enviar mensagens uns aos outros, não só ao lead
- **Lista de tarefas compartilhada** — coordenação através de uma task list comum
- **Interação direta** — você pode interagir com qualquer teammate individualmente, sem passar pelo lead
- **Experimental** — funcionalidade desabilitada por padrão, requer habilitação explícita

### 1.2 Diferenças fundamentais: Agent Teams vs Subagents

| Aspecto | Subagents | Agent Teams |
|---------|-----------|-------------|
| **Contexto** | Janela de contexto própria; resultados retornam ao agente principal | Janela de contexto própria; sessões totalmente independentes |
| **Comunicação** | Relatam resultados apenas ao agente principal | Teammates trocam mensagens diretamente entre si |
| **Coordenação** | Agente principal gerencia todo o trabalho | Lista de tarefas compartilhada com autocoordenação |
| **Melhor para** | Tarefas focadas onde só o resultado importa | Trabalho complexo exigindo discussão e colaboração |
| **Custo de tokens** | Mais baixo: resultados resumidos no contexto principal | Mais alto: cada teammate é uma instância Claude separada (~2x) |
| **Persistência** | Tarefa executada, resultado retornado, agente encerrado | Sessões persistentes que ficam ociosas entre turnos |
| **Estado compartilhado** | Nenhum; subagents não se conhecem | Config, task queue e mailboxes compartilhados |

**Regra prática:** Use subagents quando precisar de workers focados que só reportam resultado. Use agent teams quando os membros precisarem compartilhar descobertas, desafiar uns aos outros e coordenar por conta própria.

---

## 2. Arquitetura e comunicação entre agents

### 2.1 Componentes da arquitetura

| Componente | Função |
|------------|--------|
| **Team Lead** | Sessão principal do Claude Code que cria a equipe, spawna teammates e coordena o trabalho |
| **Teammates** | Instâncias separadas do Claude Code que trabalham em tarefas atribuídas |
| **Task List** | Lista compartilhada de itens de trabalho que os teammates reivindicam e completam |
| **Mailbox** | Sistema de mensageria para comunicação entre agentes |

### 2.2 Estrutura em disco

Quando uma equipe é criada, o Claude Code cria duas árvores de diretórios:

```
~/.claude/teams/{nome-da-equipe}/
├── config.json                  # config da equipe: membros, lead, metadados
└── inboxes/
    ├── team-lead.json           # inbox do lead (criado na primeira mensagem)
    ├── frontend-engineer.json   # cada agente recebe um arquivo de inbox
    └── backend-engineer.json

~/.claude/tasks/{nome-da-equipe}/
├── .lock                        # arquivo vazio, usado para flock
├── 1.json                       # arquivos de tarefa (um por tarefa)
├── 2.json
├── 3.json
└── 4.json
```

**Observação:** Todo o sistema multiagente é baseado em **arquivos JSON em disco**. Não há banco de dados, message broker ou IPC. Os agentes se comunicam escrevendo nos arquivos de inbox uns dos outros.

### 2.3 Schema do config

O arquivo `config.json` rastreia quem está na equipe:

```json
{
  "name": "codebase-research",
  "description": "Equipe de pesquisa analisando o codebase",
  "createdAt": 1771441034855,
  "leadAgentId": "team-lead@codebase-research",
  "leadSessionId": "uuid-da-sessao",
  "members": [
    {
      "agentId": "team-lead@codebase-research",
      "name": "team-lead",
      "agentType": "team-lead",
      "model": "claude-opus-4-6",
      "joinedAt": 1771441034855,
      "cwd": "/caminho/do/projeto",
      "subscriptions": []
    },
    {
      "agentId": "frontend-engineer@codebase-research",
      "name": "frontend-engineer",
      "agentType": "general-purpose",
      "model": "claude-opus-4-6",
      "prompt": "Você é um engenheiro frontend sênior...",
      "color": "blue",
      "planModeRequired": false,
      "joinedAt": 1771441084084,
      "backendType": "in-process"
    }
  ]
}
```

O formato de `agentId` é sempre `{nome}@{nome-da-equipe}`.

### 2.4 Protocolo de mensagens

Toda comunicação passa por arquivos de inbox. Cada inbox é um array JSON de objetos de mensagem:

```json
[
  {
    "from": "worker",
    "text": "Todas as tarefas concluídas...",
    "summary": "As 2 tarefas foram concluídas com sucesso",
    "timestamp": "2026-02-18T18:39:39.925Z",
    "color": "blue",
    "read": false
  }
]
```

**Tipos de eventos de sistema** (campo `text` contém JSON stringificado):

| Tipo | Direção | Propósito |
|------|----------|------------|
| `idle_notification` | Agent → Lead | "Estou livre para trabalhar" (heartbeat) |
| `shutdown_request` | Lead → Agent | "Por favor, encerre" |
| `shutdown_approved` | Agent → Lead | "Encerrando agora" |
| `task_assignment` | Agent → Self | Agent reivindica uma tarefa (auto-notificação) |
| `plan_approval_request` | Agent → Lead | Plano pronto para revisão |
| `permission_request` | Agent → Lead | Agent precisa de permissão para ferramenta |

### 2.5 Dependências de tarefas

As dependências são **declarativas**. Quando a tarefa 1 termina, o sistema **não** atualiza o arquivo da tarefa 2 para dizer "você está desbloqueada". Em cada chamada a `TaskList`, o sistema lê todos os arquivos de tarefa, verifica quais estão completas e calcula o que está disponível.

O campo `blockedBy` em cada arquivo de tarefa **nunca muda** após a criação:

```json
{
  "id": "3",
  "subject": "Testes de integração",
  "status": "pending",
  "blockedBy": ["1", "2"]
}
```

### 2.6 Contexto e comunicação

- Cada teammate tem sua própria janela de contexto
- Ao serem spawnados, os teammates carregam o mesmo contexto de projeto: CLAUDE.md, servidores MCP e skills
- **O histórico de conversa do lead não é herdado**
- Os teammates recebem o spawn prompt do lead

**Como os teammates compartilham informações:**

- **Lista de tarefas compartilhada** — todos os agentes veem o status e podem reivindicar trabalho
- **Notificações de idle** — quando um teammate termina e para, notifica automaticamente o lead
- **Entrega automática** — mensagens entre teammates são entregues automaticamente aos destinatários

**Opções de mensageria entre teammates:**

- **broadcast** — enviar para todos os teammates simultaneamente (usar com moderação, custo escala com tamanho da equipe)
- **message** — enviar para um teammate específico

---

## 3. Como configurar Agent Teams

### 3.1 Habilitar Agent Teams

Agent Teams são **desabilitados por padrão**. Habilite definindo a variável de ambiente `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` como `1`, no seu ambiente de shell ou através do `settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 3.2 Iniciar sua primeira equipe

Após habilitar, peça ao Claude para criar uma equipe descrevendo a tarefa e a estrutura desejada em linguagem natural:

```
Estou projetando uma ferramenta CLI que ajuda desenvolvedores a rastrear
comentários TODO no codebase. Crie uma equipe de agentes para explorar isso
de diferentes ângulos: um teammate em UX, um em arquitetura técnica,
um como advogado do diabo.
```

O Claude cria a equipe com a lista de tarefas compartilhada, spawna os teammates, faz com que explorem o problema e sintetiza os achados. Ao final, tenta fazer a limpeza da equipe.

### 3.3 Modos de exibição (teammateMode)

| Modo | Descrição |
|------|-----------|
| **Split panes** | Cada teammate em seu próprio painel. Requer tmux ou iTerm2. |
| **In-process** | Todos rodam dentro do terminal principal. Use Shift+Down para alternar entre teammates. Funciona em qualquer terminal. |
| **auto** (padrão) | Usa split panes se já estiver em sessão tmux, caso contrário in-process. |

Para forçar o modo in-process:

```json
{
  "teammateMode": "in-process"
}
```

Ou via linha de comando:

```bash
claude --teammate-mode in-process
```

**Requisitos para split-pane:**

- **tmux:** instalar via gerenciador de pacotes do sistema. `tmux -CC` no iTerm2 é o ponto de entrada sugerido.
- **iTerm2:** instalar o CLI [`it2`](https://github.com/mkusaka/it2), depois habilitar a Python API em iTerm2 → Settings → General → Magic → Enable Python API.

### 3.4 Especificar teammates e modelos

Você pode especificar exatamente o que quer:

```
Crie uma equipe com 4 teammates para refatorar esses módulos em paralelo.
Use Sonnet para cada teammate.
```

### 3.5 Exigir aprovação de plano

Para tarefas complexas ou arriscadas:

```
Spawne um teammate arquiteto para refatorar o módulo de autenticação.
Exija aprovação do plano antes de fazer qualquer alteração.
```

O fluxo:

1. Teammate trabalha em modo read-only (Plano) até o lead aprovar
2. Teammate envia `plan_approval_request` ao lead
3. Lead aprova ou rejeita com feedback
4. Se rejeitado, o teammate revisa e reenvia
5. Aprovado → teammate sai do modo plano e começa a implementação

Para influenciar as decisões do lead: "só aprove planos que incluam cobertura de testes" ou "rejeite planos que modifiquem o schema do banco".

---

## 4. Padrões de coordenação

### 4.1 Fan-out (trabalho paralelo independente)

Cada teammate recebe um pedaço de trabalho independente. Ideal quando as tarefas não têm dependências entre si.

**Exemplo:** Revisão de código com três revisores — um focado em segurança, outro em performance, outro em cobertura de testes.

### 4.2 Pipeline (fluxo sequencial)

Tarefas com dependências explícitas (`blockedBy`). O sistema desbloqueia automaticamente tarefas dependentes quando as predecessoras são concluídas.

```
Tarefa 1 (Análise) → Tarefa 2 (Design) → Tarefa 3 (Implementação)
```

### 4.3 Auto-claim vs atribuição pelo lead

- **Self-claim:** Após concluir uma tarefa, o teammate pega a próxima tarefa não atribuída e desbloqueada
- **Lead atribui:** Você diz ao lead qual tarefa dar a qual teammate

O sistema usa **file locking** para evitar condições de corrida quando múltiplos teammates tentam reivindicar a mesma tarefa.

### 4.4 Tamanho recomendado da equipe

- **3-5 teammates** para a maioria dos workflows
- **5-6 tarefas por teammate** mantém todos produtivos sem excesso de context switching
- Para 15 tarefas independentes, 3 teammates é um bom ponto de partida

**Motivos:** Retornos decrescentes, overhead de coordenação cresce, custo de tokens escala linearmente.

---

## 5. Casos de uso e exemplos

### 5.1 Casos de uso mais fortes

- **Coordenação cross-layer:** Mudanças que abrangem frontend, backend e testes, cada um de um teammate diferente
- **Debug com hipóteses concorrentes:** Teammates testam teorias diferentes em paralelo e convergem mais rápido
- **Novos módulos ou features:** Cada teammate pode possuir um pedaço separado sem pisar nos outros
- **Pesquisa e revisão:** Múltiplos teammates investigam aspectos diferentes simultaneamente e compartilham/contestam achados

### 5.2 Revisão de código paralela

```
Crie uma equipe de agentes para revisar o PR #142. Spawne três revisores:
- Um focado em implicações de segurança
- Um verificando impacto em performance
- Um validando cobertura de testes
Peça que cada um revise e reporte achados.
```

### 5.3 Investigação com hipóteses concorrentes

```
Usuários relatam que o app encerra após uma mensagem em vez de manter a conexão.
Spawne 5 agentes teammates para investigar hipóteses diferentes. Faça-os conversar
entre si para tentar refutar as teorias uns dos outros, como um debate científico.
Atualize o doc de achados com o consenso que emergir.
```

A estrutura de debate é o mecanismo chave — investigação sequencial sofre de ancoragem; com investigadores independentes tentando se refutar mutuamente, a teoria que sobrevive tem maior probabilidade de ser a causa raiz real.

### 5.4 Quando NÃO usar Agent Teams

- Tarefas sequenciais
- Edições no mesmo arquivo (risco de conflitos)
- Trabalho com muitas dependências
- Tarefas rotineiras (custo extra de tokens não compensa)

Para esses cenários: sessão única ou subagents são mais eficazes.

---

## 6. Limitações e boas práticas

### 6.1 Limitações conhecidas

| Limitação | Detalhes |
|-----------|----------|
| **Split panes** | Requer tmux ou iTerm2. Não suportado em VS Code integrado, Windows Terminal ou Ghostty |
| **Permissões no spawn** | Todos os teammates começam com o modo de permissão do lead. Não é possível definir modos por teammate no spawn |
| **Lead fixo** | A sessão que cria a equipe é o lead pela vida inteira. Não é possível promover teammate a lead |
| **Sem equipes aninhadas** | Teammates não podem spawnar suas próprias equipes. Só o lead gerencia |
| **Uma equipe por sessão** | O lead só gerencia uma equipe por vez. Limpe a atual antes de começar outra |
| **Shutdown pode ser lento** | Teammates terminam a requisição/chamada de tool atual antes de encerrar |
| **Status de tarefa pode atrasar** | Teammates às vezes falham em marcar tarefas como concluídas, bloqueando dependentes |
| **Resumo de sessão** | `/resume` e `/rewind` não restauram teammates in-process. O lead pode tentar mensagear teammates que não existem mais |

### 6.2 Boas práticas

#### Dar contexto suficiente aos teammates

O spawn prompt deve incluir detalhes da tarefa — teammates não herdam o histórico do lead:

```
Spawne um teammate revisor de segurança com o prompt: "Revise o módulo de
autenticação em src/auth/ em busca de vulnerabilidades. Foque em tratamento
de tokens, gerenciamento de sessão e validação de input. A app usa JWT em
cookies httpOnly. Reporte issues com severidade."
```

#### Dimensionar tarefas adequadamente

- **Adequado:** Unidades autocontidas com deliverable claro (função, arquivo de teste, revisão)
- **Grande demais:** Teammates trabalham muito tempo sem check-ins, aumento de risco
- **Pequenas demais:** Overhead de coordenação excede o benefício

#### Esperar teammates terminarem

Se o lead começar a implementar em vez de delegar:

```
Espere seus teammates completarem as tarefas antes de prosseguir
```

#### Começar com pesquisa e revisão

Se é sua primeira vez: comece com tarefas de limites claros que não exigem código — revisar PR, pesquisar biblioteca, investigar bug. Mostra o valor do paralelismo sem os desafios de coordenação.

#### Evitar conflitos de arquivo

Dois teammates editando o mesmo arquivo = sobrescritas. Divida o trabalho para cada teammate possuir um conjunto de arquivos diferente.

#### Monitorar e redirecionar

Verifique o progresso dos teammates, redirecione abordagens que não funcionam e sintetize achados conforme chegam. Deixar a equipe rodando sem supervisão aumenta o risco de esforço desperdiçado.

### 6.3 Hooks para gates de qualidade

| Hook | Quando roda | Uso |
|------|-------------|-----|
| `TaskCompleted` | Ao marcar tarefa como completa | Exit code 2 impede conclusão e envia feedback |
| `TeammateIdle` | Quando teammate está prestes a ficar ocioso | Exit code 2 envia feedback e mantém o teammate trabalhando |

---

## 7. Quando usar Agent Teams vs Subagents

### 7.1 Decisão rápida

```
┌─────────────────────────────────────────────────────────┐
│                     SUBAGENTS                            │
│                                                          │
│  Parent ──spawn──▶ Agent ──result──▶ Parent              │
│                    (contexto próprio, sem estado shared)  │
│                                                          │
│  Custo: mais baixo (sem contexto persistente)             │
├─────────────────────────────────────────────────────────┤
│                     AGENT TEAMS                          │
│                                                          │
│  Lead ──spawn──▶ Agent A ◀──inbox──▶ Agent B             │
│    │                ▲                    ▲               │
│    │                └────task queue──────┘               │
│    └──────────config.json + inboxes/─────                │
│                                                          │
│  Custo: ~2x (contexto persistente + overhead heartbeat)   │
└─────────────────────────────────────────────────────────┘
```

### 7.2 Tabela de decisão

| Precisa de... | Use |
|---------------|-----|
| Múltiplos agentes em paralelo que **não** precisam conversar | **Subagents** |
| Múltiplos agentes que precisam compartilhar achados e coordenar | **Agent Teams** |
| Tarefas focadas, resultado único importa | **Subagents** |
| Discussão entre agentes, debate, consenso | **Agent Teams** |
| Menor custo de tokens | **Subagents** |
| Fila de tarefas compartilhada e mensagens peer-to-peer | **Agent Teams** |

### 7.3 Alternativas

- **Sessões paralelas manuais:** [Git worktrees](https://code.claude.com/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) para rodar múltiplas sessões Claude Code manualmente sem coordenação automatizada
- **Delegação leve:** Subagents para spawn de agentes auxiliares de pesquisa ou verificação dentro da sua sessão

---

## 8. Troubleshooting

### Teammates não aparecem

- Se pediu split panes: verifique se tmux está instalado (`which tmux`)
- A tarefa era complexa o suficiente? Claude decide se spawna baseado na tarefa
- Em modo in-process: pressione Shift+Down para alternar entre teammates ativos
- Para iTerm2: verifique CLI `it2` e Python API habilitada nas preferências

### Muitos prompts de permissão

Pré-aprove operações comuns nas [configurações de permissão](https://code.claude.com/en/permissions) antes de spawnar teammates.

### Teammates param em erros

Verifique a saída com Shift+Down (in-process) ou clicando no painel (split). Opções:

- Spawnar um teammate substituto para continuar
- Dar instruções adicionais diretamente

### Lead encerra antes do trabalho terminar

Diga ao lead para continuar ou: "espere seus teammates terminarem antes de prosseguir".

### Sessões tmux órfãs

Se uma sessão tmux persistir após o fim da equipe:

```bash
tmux ls
tmux kill-session -t <nome-da-sessao>
```

### Debug de equipe travada

```bash
# Ver config e membros atuais
cat ~/.claude/teams/*/config.json | python3 -m json.tool

# Ver tarefas criadas e reivindicadas
watch -n 1 'ls -la ~/.claude/tasks/*/'

# Ler inbox do lead
cat ~/.claude/teams/*/inboxes/team-lead.json | python3 -m json.tool
```

---

## 9. Referências

- [Documentação oficial: Agent Teams](https://code.claude.com/docs/en/agent-teams)
- [Documentação oficial: Subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Agent Teams: How They Work Under the Hood](https://www.claudecodecamp.com/p/claude-code-agent-teams-how-they-work-under-the-hood) — Análise detalhada do protocolo baseado em arquivos
- [Compare: subagent vs agent team](https://code.claude.com/en/features-overview#compare-similar-features)
