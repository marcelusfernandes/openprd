# Skills no Claude Code — Guia Completo

> Documento de referência baseado na documentação oficial: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)

---

## 1. O que são Skills no Claude Code

**Skills** (ou "habilidades") estendem o que o Claude pode fazer. São arquivos `SKILL.md` com instruções que ampliam o conjunto de capacidades do assistente. O Claude pode carregá-las automaticamente quando forem relevantes, ou você pode invocá-las diretamente com `/nome-da-skill`.

### Características principais

- **Extensibilidade**: Crie instruções personalizadas e adicione-as ao toolkit do Claude
- **Invocações flexíveis**: Claude usa skills quando relevante, ou você chama com `/skill-name`
- **Padrão aberto**: Claude Code segue o padrão [Agent Skills](https://agentskills.io/), compatível com múltiplas ferramentas de IA
- **Extensões do Claude Code**: Inclui controle de invocação, execução em subagentes e injeção dinâmica de contexto

### Skills embutidas

Skills embutidas vêm com o Claude Code e estão disponíveis em toda sessão. Diferente de comandos built-in (que executam lógica fixa), skills embutidas são baseadas em prompt: dão ao Claude um playbook detalhado e deixam-no orquestrar o trabalho usando suas ferramentas.

| Skill | Descrição |
|-------|-----------|
| `/claude-api` | Carrega referência da API Claude para a linguagem do projeto |
| `/loop [intervalo]` | Executa um prompt repetidamente em intervalos (ex.: `/loop 5m check deploy`) |
| `/debug [descrição]` | Depura a sessão atual do Claude Code, lendo o log de debug |
| `/batch` | Orquestra mudanças em larga escala em paralelo (5–30 unidades, PRs por unidade) |
| `/simplify` | Revisa arquivos alterados quanto a reuso, qualidade e eficiência |

---

## 2. Como criar e estruturar Skills (SKILL.md)

### Estrutura básica

Todo skill precisa de um arquivo `SKILL.md` com duas partes:

1. **YAML frontmatter** (entre `---`): configura quando e como o Claude usa o skill
2. **Conteúdo em Markdown**: instruções que o Claude segue quando o skill é invocado

```markdown
---
name: meu-skill
description: O que este skill faz e quando usá-lo
---

Suas instruções aqui...
```

### Onde os Skills vivem

| Local | Caminho | Escopo |
|-------|---------|--------|
| Enterprise | Ver [managed settings](https://code.claude.com/en/settings#settings-files) | Toda a organização |
| Pessoal | `~/.claude/skills/<nome>/SKILL.md` | Todos os seus projetos |
| Projeto | `.claude/skills/<nome>/SKILL.md` | Apenas este projeto |
| Plugin | `/skills/<nome>/SKILL.md` | Onde o plugin está habilitado |

**Prioridade**: enterprise > pessoal > projeto. Skills de plugins usam namespace `plugin-name:skill-name` e não conflitam com outros níveis.

### Descoberta automática em diretórios aninhados

Em monorepos, o Claude Code descobre skills em `.claude/skills/` dentro de subdiretórios. Ao editar arquivos em `packages/frontend/`, ele também procura em `packages/frontend/.claude/skills/`.

### Estrutura de diretório recomendada

```
meu-skill/
├── SKILL.md           # Instruções principais (obrigatório)
├── template.md        # Template para o Claude preencher
├── examples/
│   └── sample.md      # Exemplo de output esperado
└── scripts/
    └── validate.sh    # Script que o Claude pode executar
```

- **SKILL.md**: obrigatório; contém as instruções principais
- **Outros arquivos**: opcionais; templates, exemplos, scripts, documentação de referência

---

## 3. Frontmatter — Campos disponíveis

Configuração via YAML no topo do `SKILL.md`:

```yaml
---
name: meu-skill
description: O que este skill faz
disable-model-invocation: true
allowed-tools: Read, Grep
---
```

### Tabela de campos

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Não | Nome exibido. Se omitido, usa o nome do diretório. Apenas letras minúsculas, números e hífens (máx. 64 caracteres) |
| `description` | Recomendado | O que o skill faz e quando usá-lo. O Claude usa isso para decidir quando carregá-lo. Se omitido, usa o primeiro parágrafo do markdown |
| `argument-hint` | Não | Dica no autocomplete ao digitar argumentos. Ex.: `[issue-number]` ou `[filename] [format]` |
| `disable-model-invocation` | Não | `true` impede o Claude de carregar o skill automaticamente. Use para workflows manuais com `/name`. Padrão: `false` |
| `user-invocable` | Não | `false` esconde do menu `/`. Use para conhecimento de fundo. Padrão: `true` |
| `allowed-tools` | Não | Ferramentas que o Claude pode usar sem pedir permissão quando o skill está ativo |
| `model` | Não | Modelo a usar quando o skill está ativo |
| `context` | Não | `fork` executa em contexto de subagente forkado |
| `agent` | Não | Tipo de subagente quando `context: fork` está definido |
| `hooks` | Não | Hooks vinculados ao ciclo de vida do skill |

### Substituição de strings (variáveis dinâmicas)

| Variável | Descrição |
|----------|-----------|
| `$ARGUMENTS` | Todos os argumentos passados na invocação |
| `$ARGUMENTS[N]` | Argumento específico (índice 0-based), ex.: `$ARGUMENTS[0]` |
| `$N` | Atalho para `$ARGUMENTS[N]`, ex.: `$0`, `$1` |
| `${CLAUDE_SESSION_ID}` | ID da sessão atual |
| `${CLAUDE_SKILL_DIR}` | Diretório contendo o `SKILL.md` do skill |

Se o conteúdo não incluir `$ARGUMENTS`, os argumentos são anexados como `ARGUMENTS: `.

---

## 4. Como Skills são invocadas (model-invoked vs user-invoked)

Por padrão, **você e o Claude** podem invocar qualquer skill. Dois campos controlam isso:

- **`user-invocable: false`**: apenas o Claude pode invocar. Use para conhecimento de fundo, não como comando acionável
- **`disable-model-invocation: true`**: apenas você pode invocar. Use para workflows com side effects ou que devem ser acionados manualmente (ex.: `/deploy`, `/commit`)

### Matriz de invocação e carregamento

| Frontmatter | Você pode invocar | Claude pode invocar | Quando carrega no contexto |
|-------------|-------------------|---------------------|----------------------------|
| (padrão) | Sim | Sim | Descrição sempre no contexto; skill completo ao ser invocado |
| `disable-model-invocation: true` | Sim | Não | Descrição fora do contexto; skill completo quando você invoca |
| `user-invocable: false` | Não | Sim | Descrição sempre no contexto; skill completo quando invocado |

### Controle de invocação pelo Claude

Três formas de limitar quais skills o Claude pode invocar:

1. **Desabilitar todos**: negar a ferramenta `Skill` em `/permissions`:
   ```
   Skill
   ```

2. **Permitir ou negar skills específicos**:
   ```
   # Permitir apenas alguns
   Skill(commit)
   Skill(review-pr *)
   
   # Negar específicos
   Skill(deploy *)
   ```

3. **Ocultar skills individuais**: `disable-model-invocation: true` remove o skill do contexto do Claude.

---

## 5. Progressive disclosure e boas práticas

### Tipos de conteúdo do skill

- **Conteúdo de referência**: conhecimento que o Claude aplica ao trabalho atual (convenções, padrões, guias de estilo). Executa inline.
- **Conteúdo de tarefa**: instruções passo a passo para uma ação específica. Use `disable-model-invocation: true` se quiser invocar manualmente.

### Boas práticas

1. **Manter SKILL.md enxuto**: preferir &lt; 500 linhas; mover referências detalhadas para arquivos separados
2. **Description clara**: incluir palavras-chave que os usuários usariam naturalmente
3. **Referenciar arquivos de suporte** no `SKILL.md` para que o Claude saiba o que carregar e quando
4. **Pensar na invocação**: manual (`/skill-name`), automática pelo Claude ou ambas
5. **Considerar contexto**: execução inline ou em subagente (`context: fork`)

---

## 6. Referências e templates dentro de Skills

Skills podem incluir vários arquivos na pasta do skill. Isso mantém o `SKILL.md` focado e permite carregar referências só quando necessário.

### Estrutura sugerida

```
meu-skill/
├── SKILL.md           # Visão geral e navegação
├── reference.md       # Documentação detalhada (carregada quando necessário)
├── examples.md        # Exemplos de uso
└── scripts/
    └── helper.py      # Script executável (não carregado como texto)
```

### Referência a arquivos de suporte

No `SKILL.md`:

```markdown
## Recursos adicionais

- Para detalhes completos da API, ver [reference.md](reference.md)
- Para exemplos de uso, ver [examples.md](examples.md)
```

Referenciar arquivos indica ao Claude o que cada arquivo contém e quando carregá-lo.

---

## 7. Interação entre Skills e subagentes

Skills e subagentes funcionam em duas direções:

| Abordagem | System prompt | Tarefa | Também carrega |
|-----------|---------------|--------|----------------|
| Skill com `context: fork` | Do tipo de agente (Explore, Plan, etc.) | Conteúdo do SKILL.md | CLAUDE.md |
| Subagente com campo `skills` | Markdown do subagente | Mensagem de delegação do Claude | Skills pré-carregados + CLAUDE.md |

### Executar skill em subagente

Use `context: fork` no frontmatter:

```yaml
---
name: deep-research
description: Pesquisa aprofundada sobre um tópico
context: fork
agent: Explore
---
```

O conteúdo do skill vira o prompt do subagente. O campo `agent` define o ambiente (modelo, ferramentas, permissões). Opções: `Explore`, `Plan`, `general-purpose` ou agentes customizados em `.claude/agents/`.

### Injeção dinâmica de contexto

Use `!` comando`` para executar comandos shell antes do envio do conteúdo ao Claude. O output substitui o placeholder:

```yaml
---
name: pr-summary
description: Resumir mudanças em um pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Contexto do PR
- Diff: !`gh pr diff`
- Comentários: !`gh pr view --comments`
- Arquivos alterados: !`gh pr diff --name-only`

## Sua tarefa
Resuma este pull request...
```

Isso é pré-processamento; o Claude recebe o resultado final, não o comando em si.

---

## 8. Exemplos práticos

### Exemplo 1: Skill de explicação de código

```yaml
---
name: explain-code
description: Explica código com diagramas visuais e analogias. Use quando explicar como código funciona ou ensinar sobre um codebase.
---

Ao explicar código, sempre inclua:

1. **Comece com uma analogia**: Compare o código a algo do cotidiano
2. **Desenhe um diagrama**: ASCII art para fluxo, estrutura ou relacionamentos
3. **Percorra o código**: Explique passo a passo o que acontece
4. **Destaque um gotcha**: Erro ou equívoco comum

Mantenha explicações conversacionais.
```

### Exemplo 2: Skill de deploy (só invocação manual)

```yaml
---
name: deploy
description: Faz deploy da aplicação em produção
disable-model-invocation: true
---

Faça deploy de $ARGUMENTS em produção:

1. Execute a suíte de testes
2. Build da aplicação
3. Push para o alvo de deploy
4. Verifique se o deploy foi concluído
```

### Exemplo 3: Skill com argumentos por posição

```yaml
---
name: migrate-component
description: Migra componente de um framework para outro
---

Migre o componente $0 de $1 para $2.
Preserve todo o comportamento existente e os testes.
```

Uso: `/migrate-component SearchBar React Vue`

### Exemplo 4: Skill read-only (ferramentas restritas)

```yaml
---
name: safe-reader
description: Lê arquivos sem fazer alterações
allowed-tools: Read, Grep, Glob
---

Explore o codebase em modo somente leitura.
```

### Exemplo 5: Skill de pesquisa com subagente

```yaml
---
name: deep-research
description: Pesquisa aprofundada sobre um tópico
context: fork
agent: Explore
---

Pesquise $ARGUMENTS de forma aprofundada:

1. Encontre arquivos relevantes com Glob e Grep
2. Leia e analise o código
3. Resuma os achados com referências específicas a arquivos
```

---

## Troubleshooting

### Skill não é acionada

1. Invocar diretamente com `/skill-name` se o skill for user-invocable
2. Reformular o pedido para aproximar da description
3. Verificar se o skill aparece em "Quais skills estão disponíveis?"
4. Conferir se a description inclui palavras-chave que os usuários usariam

### Skill acionada com frequência excessiva

1. Usar `disable-model-invocation: true` para invocação apenas manual
2. Tornar a description mais específica

### Claude não vê todos os skills

Descriptions são carregadas no contexto; com muitos skills, pode exceder o limite (2% da janela de contexto, fallback de 16.000 caracteres). Use `/context` para checar avisos. Para ajustar: variável `SLASH_COMMAND_TOOL_CHAR_BUDGET`.

---

## Recursos relacionados

- [Permissions](https://code.claude.com/en/permissions): controle de acesso a ferramentas e skills
- [Interactive mode](https://code.claude.com/en/interactive-mode): comandos built-in e atalhos
- [Memory](https://code.claude.com/en/memory): gerenciar arquivos CLAUDE.md
- [Hooks](https://code.claude.com/en/hooks): automação em torno de eventos de ferramentas
- [Plugins](https://code.claude.com/en/plugins): empacotar e distribuir skills
- [Subagents](https://code.claude.com/en/sub-agents): delegar tarefas a agentes especializados
