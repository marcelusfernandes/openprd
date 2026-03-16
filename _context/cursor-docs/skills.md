# Cursor Agent Skills — Documentação Resumida

> Resumo da documentação oficial em [cursor.com/docs/skills](https://cursor.com/docs/skills). Referência para compreensão e uso de Agent Skills no Cursor.

---

## O que são Agent Skills

**Agent Skills** é um padrão aberto para estender agentes de IA com capacidades especializadas. Skills são pacotes que empacotam conhecimento e fluxos de trabalho específicos de um domínio, permitindo que agentes realizem tarefas pontuais.

### Características principais

| Característica | Descrição |
|----------------|-----------|
| **Portável** | Funcionam em qualquer agente que suporte o padrão Agent Skills |
| **Versionável** | Armazenados como arquivos; podem ser versionados no repositório ou instalados via links do GitHub |
| **Acionável** | Podem incluir scripts, templates e referências que o agente executa com suas ferramentas |
| **Progressivo** | Carregam recursos sob demanda, mantendo o uso de contexto eficiente |

---

## Como funcionam

### Descoberta automática

Ao iniciar, o Cursor descobre automaticamente skills nos diretórios configurados e os disponibiliza ao Agent.

### Invocação

1. **Automática**: o agente decide quando uma skill é relevante com base no contexto da conversa.
2. **Manual**: digite `/` no chat do Agent e busque pelo nome da skill para invocá-la diretamente.

---

## Diretórios de Skills

Skills são carregados automaticamente nestes locais:

| Localização | Escopo |
|-------------|--------|
| `.agents/skills/` | Projeto |
| `.cursor/skills/` | Projeto |
| `~/.cursor/skills/` | Usuário (global) |

### Diretórios compatíveis (Claude e Codex)

Para compatibilidade, o Cursor também carrega skills de:

- `.claude/skills/`
- `.codex/skills/`
- `~/.claude/skills/`
- `~/.codex/skills/`

### Estrutura mínima de um skill

Cada skill deve ser uma pasta contendo um arquivo `SKILL.md`:

```
.agents/
└── skills/
    └── my-skill/
        └── SKILL.md
```

---

## Formato do arquivo SKILL.md

Cada skill é definida em um `SKILL.md` com frontmatter YAML.

### Exemplo completo

```markdown
---
name: my-skill
description: Descrição curta do que este skill faz e quando usá-lo.
---

# My Skill

Instruções detalhadas para o agente.

## When to Use

- Use este skill quando...
- Este skill é útil para...

## Instructions

- Orientação passo a passo para o agente
- Convenções específicas do domínio
- Boas práticas e padrões
- Use a ferramenta de perguntas se precisar esclarecer requisitos com o usuário
```

### Campos do frontmatter

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Sim | Identificador do skill. Apenas letras minúsculas, números e hífens. Deve corresponder ao nome da pasta pai. |
| `description` | Sim | Descreve o que o skill faz e quando usá-lo. Usado pelo agente para determinar relevância. |
| `license` | Não | Nome da licença ou referência a arquivo de licença incluído. |
| `compatibility` | Não | Requisitos de ambiente (pacotes do sistema, acesso à rede, etc.). |
| `metadata` | Não | Mapeamento arbitrário de chave-valor para metadados adicionais. |
| `disable-model-invocation` | Não | Quando `true`, o skill só é incluído quando invocado explicitamente via `/skill-name`. O agente não o aplica automaticamente. |

---

## Diretórios opcionais

Skills podem incluir diretórios opcionais:

| Diretório | Propósito |
|-----------|-----------|
| `scripts/` | Código executável que o agente pode rodar |
| `references/` | Documentação adicional carregada sob demanda |
| `assets/` | Recursos estáticos (templates, imagens, arquivos de dados) |

### Estrutura com diretórios opcionais

```
.agents/
└── skills/
    └── deploy-app/
        ├── SKILL.md
        ├── scripts/
        │   ├── deploy.sh
        │   └── validate.py
        ├── references/
        │   └── REFERENCE.md
        └── assets/
            └── config-template.json
```

Mantenha o `SKILL.md` focado e mova material detalhado para arquivos separados. Isso otimiza o uso de contexto, pois os agentes carregam recursos de forma progressiva, somente quando necessário.

---

## Como incluir scripts em Skills

Skills podem ter um diretório `scripts/` com código executável. Referencie os scripts no `SKILL.md` usando caminhos relativos à raiz do skill.

### Exemplo

```markdown
---
name: deploy-app
description: Faz o deploy da aplicação em staging ou produção. Use quando o usuário mencionar deployment, releases ou ambientes.
---

# Deploy App

Faça o deploy da aplicação usando os scripts fornecidos.

## Uso

Execute o script de deploy: `scripts/deploy.sh <ambiente>`

Onde `<ambiente>` pode ser `staging` ou `production`.

## Validação pré-deploy

Antes de fazer o deploy, execute o script de validação: `python scripts/validate.py`
```

O agente lê as instruções e executa os scripts referenciados quando o skill é invocado. Scripts podem ser em Bash, Python, JavaScript ou qualquer outro formato executável suportado.

### Boas práticas para scripts

- Ser autocontidos
- Incluir mensagens de erro claras
- Tratar casos de borda adequadamente

---

## Como desabilitar invocação automática

Por padrão, skills são aplicados automaticamente quando o agente considera que são relevantes.

### Comportamento tipo slash command

Defina `disable-model-invocation: true` para que o skill funcione como um comando slash tradicional: ele só entra no contexto quando você digita `/skill-name` no chat.

```yaml
---
name: my-command-like-skill
description: Executa tarefa X quando invocado.
disable-model-invocation: true
---
```

---

## Como visualizar e instalar Skills

### Visualizar skills descobertos

1. Skills aparecem na seção **Agent Decides**
2. Acesse **Rules**
3. Abra **Cursor Settings** (`Cmd+Shift+J` no Mac, `Ctrl+Shift+J` no Windows/Linux)

### Instalar skills do GitHub

1. Informe a URL do repositório GitHub
2. Selecione **Remote Rule (Github)**
3. Em **Project Rules**, clique em **Add Rule**
4. Abra **Cursor Settings → Rules**

---

## Migração de rules e commands para skills

O Cursor inclui o skill `/migrate-to-skills` (desde 2.4) para converter dynamic rules e slash commands em skills.

### O que é convertido

| Tipo | Comportamento na migração |
|------|---------------------------|
| **Slash commands** | Comandos em nível de usuário e de workspace viram skills com `disable-model-invocation: true`, mantendo a invocação explícita. |
| **Dynamic rules** | Rules com "Apply Intelligently" (sem `alwaysApply: true` e sem `globs` definidos) viram skills padrão. |

### Como migrar

1. Digite `/migrate-to-skills` no chat do Agent
2. O agente identifica rules e commands elegíveis e os converte
3. Revise os skills gerados em `.cursor/skills/`

### O que não é migrado

- Rules com `alwaysApply: true` ou `globs` específicos (têm condições de disparo explícitas diferentes do comportamento de skills)
- User rules (não estão no sistema de arquivos)

---

## Boas práticas

1. **Foque no SKILL.md** — Instruções principais no arquivo principal; detalhes em `references/`.
2. **Description clara** — A descrição define quando o agente usa o skill automaticamente.
3. **Scripts autocontidos** — Incluam mensagens de erro e tratamento de casos de borda.
4. **Carregamento progressivo** — Use `references/` e `assets/` para reduzir uso de contexto.
5. **Nome consistente** — O `name` no frontmatter deve ser igual ao nome da pasta.
6. **Convenção de nomenclatura** — Use minúsculas, números e hífens em `name`.

---

## Saiba mais

Agent Skills é um padrão aberto. Mais informações em [agentskills.io](https://agentskills.io/).
