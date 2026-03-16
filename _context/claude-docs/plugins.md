# Plugins no Claude Code — Guia Completo

> **Fonte:** [code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)  
> Documento de referência para criar e distribuir plugins no Claude Code.

---

## 1. O que são Plugins no Claude Code

**Plugins** são extensões que permitem adicionar funcionalidades customizadas ao Claude Code. Eles encapsulam uma ou mais destas capacidades:

- **Skills (ou comandos)** — comandos invocáveis como `/meu-plugin:hello`
- **Agents** — subagentes especializados para tarefas específicas
- **Hooks** — manipuladores de eventos que reagem a ações do Claude
- **MCP servers** — integração com ferramentas externas via Model Context Protocol
- **LSP servers** — inteligência de código em tempo real (navegação, definições, diagnósticos)

Plugins são **diretórios auto-contidos** com um manifesto (opcional) e seus componentes. Podem ser compartilhados entre projetos, times e comunidades, instalados via marketplace e versionados com controle de versão semântico.

---

## 2. Quando usar Plugins vs configuração standalone

O Claude Code suporta duas abordagens para skills, agents e hooks:

| Abordagem | Nome das skills | Melhor para |
|-----------|-----------------|-------------|
| **Standalone** (pasta `.claude/`) | `/hello`, `/deploy` | Workflows pessoais, experimentos rápidos, customizações por projeto |
| **Plugins** (diretório com `.claude-plugin/plugin.json`) | `/meu-plugin:hello` | Compartilhar com times, distribuir na comunidade, releases versionados, reusar em vários projetos |

### Use configuração standalone quando:

- Você quer nomes curtos de skills como `/hello` ou `/deploy`
- Está experimentando skills ou hooks antes de empacotá-los
- A configuração é pessoal e não precisa ser compartilhada
- Está customizando o Claude Code para um único projeto

### Use plugins quando:

- Você aceita nomes com namespace (ex.: `/meu-plugin:hello`) — evita conflitos entre plugins
- Vai distribuir via marketplace
- Quer controle de versão e atualizações fáceis para suas extensões
- Precisa das mesmas skills/agents em vários projetos
- Quer compartilhar funcionalidade com time ou comunidade

**Recomendação:** comece com configuração standalone em `.claude/` para iteração rápida e, quando estiver pronto para compartilhar, [converta para plugin](#10-migração-de-configurações-existentes-para-plugins).

---

## 3. Estrutura de diretórios de um plugin

### Estrutura padrão

```
meu-plugin/
├── .claude-plugin/           # Diretório de metadados (opcional)
│   └── plugin.json             # Manifesto do plugin
├── commands/                 # Local padrão para comandos (markdown)
│   ├── status.md
│   └── logs.md
├── agents/                   # Subagentes
│   ├── security-reviewer.md
│   └── performance-tester.md
├── skills/                   # Agent Skills com SKILL.md
│   ├── code-reviewer/
│   │   ├── SKILL.md
│   │   └── reference.md
│   └── pdf-processor/
│       ├── SKILL.md
│       └── scripts/
├── hooks/                    # Configuração de hooks
│   ├── hooks.json
│   └── security-hooks.json
├── settings.json             # Configurações padrão do plugin
├── .mcp.json                 # Definições de MCP servers
├── .lsp.json                 # Configurações de LSP servers
├── scripts/                  # Scripts utilitários
│   ├── format-code.sh
│   └── deploy.js
├── LICENSE
└── CHANGELOG.md
```

### Tabela de referência de localizações

| Componente | Localização padrão | Propósito |
|------------|--------------------|-----------|
| Manifesto | `.claude-plugin/plugin.json` | Metadados e configuração do plugin (opcional) |
| Commands | `commands/` | Arquivos Markdown de skills (legado; prefira `skills/` para novos) |
| Agents | `agents/` | Arquivos Markdown de subagentes |
| Skills | `skills/` | Skills com estrutura `/SKILL.md` |
| Hooks | `hooks/hooks.json` | Configuração de hooks |
| MCP servers | `.mcp.json` | Definições de servidores MCP |
| LSP servers | `.lsp.json` | Configurações de Language Server Protocol |
| Settings | `settings.json` | Configuração padrão aplicada quando o plugin está ativo |

### Erro comum

**Não coloque** `commands/`, `agents/`, `skills/` ou `hooks/` **dentro** de `.claude-plugin/`. Apenas `plugin.json` fica em `.claude-plugin/`. Os demais diretórios ficam na raiz do plugin.

---

## 4. Plugin manifest (plugin.json)

O arquivo `.claude-plugin/plugin.json` define a identidade e configuração do plugin.

### Schema completo

```json
{
  "name": "meu-plugin",
  "version": "1.2.0",
  "description": "Breve descrição do plugin",
  "author": {
    "name": "Nome do Autor",
    "email": "autor@exemplo.com",
    "url": "https://github.com/autor"
  },
  "homepage": "https://docs.exemplo.com/plugin",
  "repository": "https://github.com/autor/plugin",
  "license": "MIT",
  "keywords": ["palavra1", "palavra2"],
  "commands": ["./custom/commands/special.md"],
  "agents": "./custom/agents/",
  "skills": "./custom/skills/",
  "hooks": "./config/hooks.json",
  "mcpServers": "./mcp-config.json",
  "lspServers": "./.lsp.json",
  "outputStyles": "./styles/"
}
```

### Campos obrigatórios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `name` | string | Identificador único (kebab-case, sem espaços). Usado como namespace (ex.: `/meu-plugin:hello`). |

### Campos de metadados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `version` | string | Versão em [semantic versioning](https://semver.org/) (ex.: `"2.1.0"`). Se definido no marketplace, `plugin.json` tem prioridade. |
| `description` | string | Explicação breve do propósito do plugin |
| `author` | object | Informações do autor (`name`, `email`, `url`) |
| `homepage` | string | URL da documentação |
| `repository` | string | URL do repositório |
| `license` | string | Identificador SPDX (ex.: MIT, Apache-2.0) |
| `keywords` | array | Tags para descoberta |

### Campos de caminhos de componentes

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `commands` | string\|array | Caminhos para arquivos ou pastas de comandos |
| `agents` | string\|array | Caminhos para arquivos de agents |
| `skills` | string\|array | Caminhos para diretórios de skills |
| `hooks` | string\|array\|object | Caminhos ou config inline de hooks |
| `mcpServers` | string\|array\|object | Config de MCP ou caminho para arquivo |
| `lspServers` | string\|array\|object | Config de LSP ou caminho para arquivo |
| `outputStyles` | string\|array | Estilos de saída customizados |

### Regras de caminhos

- **Caminhos customizados complementam** os diretórios padrão; não os substituem.
- Use arrays para especificar múltiplos caminhos.
- Todos os caminhos devem ser relativos à raiz do plugin e começar com `./`.

### Variável de ambiente

- **`${CLAUDE_PLUGIN_ROOT}`** — Caminho absoluto do diretório do plugin. Use em hooks, MCP servers e scripts para garantir que os caminhos funcionem em qualquer local de instalação.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/process.sh"
          }
        ]
      }
    ]
  }
}
```

---

## 5. Como adicionar Skills, Agents, Hooks e MCP servers a plugins

### Skills

1. Crie `skills/` na raiz do plugin.
2. Cada skill é uma pasta com `SKILL.md`.
3. O nome da pasta vira o nome da skill com namespace: `skills/hello/` + plugin `meu-plugin` → `/meu-plugin:hello`.

Exemplo `skills/code-reviewer/SKILL.md`:

```markdown
---
name: code-reviewer
description: Revisa código para boas práticas e possíveis problemas. Use ao revisar código, analisar PRs ou checar qualidade.
---

Ao revisar código, verifique:
1. Organização e estrutura
2. Tratamento de erros
3. Segurança
4. Cobertura de testes
```

**Argumentos dinâmicos:** use `$ARGUMENTS` para capturar texto após o nome da skill:

```markdown
---
description: Cumprimenta o usuário com mensagem personalizada
---

Cumprimente o usuário "$ARGUMENTS" e pergunte como pode ajudar hoje.
```

### Agents

1. Crie `agents/` na raiz do plugin.
2. Cada agent é um arquivo Markdown com frontmatter e instruções.

Exemplo:

```markdown
---
name: security-reviewer
description: Especialista em revisão de segurança. Invoque ao analisar código para vulnerabilidades.
---

Você é um revisor de segurança. Analise o código em busca de:
- SQL injection
- XSS
- Exposição de credenciais
```

### Hooks

1. Crie `hooks/hooks.json` na raiz do plugin.
2. Ou defina hooks inline em `plugin.json`.
3. Formato: JSON com eventos e ações.

Exemplo:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

**Eventos disponíveis:** `PreCompact`, `TaskCompleted`, `TeammateIdle`, `SessionEnd`, `SessionStart`, `SubagentStop`, `SubagentStart`, `Stop`, `Notification`, `UserPromptSubmit`, `PermissionRequest`, `PostToolUseFailure`, `PostToolUse`, `PreToolUse`.

**Tipos de hooks:**
- `agent` — agente verificador com tools
- `prompt` — avaliar prompt com LLM (`$ARGUMENTS` para contexto)
- `command` — executar comandos shell ou scripts

### MCP servers

1. Crie `.mcp.json` na raiz do plugin.
2. Ou defina inline em `plugin.json`.

Exemplo:

```json
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

---

## 6. LSP servers em plugins

LSP (Language Server Protocol) oferece:
- **Inteligência de código** — tipos, documentação, símbolos
- **Navegação** — ir para definição, referências, hover
- **Diagnósticos** — erros e avisos em tempo quase real

### Quando criar um plugin LSP

Para TypeScript, Python, Rust etc., prefira plugins LSP do marketplace oficial. Só crie um LSP customizado se o idioma ainda não tiver suporte.

### Exemplo em `.lsp.json`

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

### Campos principais

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `command` | Sim | Binário do LSP (deve estar no PATH) |
| `extensionToLanguage` | Sim | Mapeamento de extensões para identificadores de linguagem |
| `args` | Não | Argumentos de linha de comando |
| `transport` | Não | `stdio` (padrão) ou `socket` |
| `env` | Não | Variáveis de ambiente |
| `initializationOptions` | Não | Opções passadas na inicialização |
| `restartOnCrash` | Não | Reiniciar automaticamente em caso de crash |

O binário do LSP deve ser instalado separadamente. O plugin apenas configura como o Claude Code se conecta a ele.

---

## 7. Settings padrão com plugins

O arquivo `settings.json` na raiz do plugin define configurações padrão aplicadas quando o plugin está ativo. Atualmente só o campo `agent` é suportado:

```json
{
  "agent": "security-reviewer"
}
```

Isso define o agent `security-reviewer` (do `agents/` do plugin) como thread principal. Settings em `settings.json` têm prioridade sobre `settings` em `plugin.json`. Chaves desconhecidas são ignoradas.

---

## 8. Teste local com --plugin-dir

Para desenvolver e testar sem instalação:

```bash
claude --plugin-dir ./meu-plugin
```

Ao iniciar, o Claude Code carrega o plugin e habilita seus componentes. Para testar a skill:

```shell
/meu-plugin:hello
```

**Carregar vários plugins:**

```bash
claude --plugin-dir ./plugin-um --plugin-dir ./plugin-dois
```

Reinicie o Claude Code após alterações para carregar as mudanças.

---

## 9. Distribuição e marketplaces

### Escopos de instalação

| Escopo | Arquivo de settings | Uso |
|--------|--------------------|-----|
| `user` | `~/.claude/settings.json` | Plugins pessoais em todos os projetos (padrão) |
| `project` | `.claude/settings.json` | Plugins compartilhados via versionamento |
| `local` | `.claude/settings.local.json` | Plugins locais do projeto (gitignored) |
| `managed` | Managed settings | Plugins gerenciados (somente leitura, só atualizações) |

### Criar um marketplace

1. Crie `.claude-plugin/marketplace.json` na raiz do repositório.
2. Liste os plugins e suas fontes (`source`).
3. Publique (GitHub, GitLab etc.).
4. Usuários adicionam com `/plugin marketplace add` e instalam com `/plugin install`.

**Exemplo de `marketplace.json`:**

```json
{
  "name": "meus-plugins",
  "owner": {
    "name": "Seu Nome",
    "email": "email@exemplo.com"
  },
  "plugins": [
    {
      "name": "quality-review-plugin",
      "source": "./plugins/quality-review-plugin",
      "description": "Skill /quality-review para revisões rápidas de código"
    }
  ]
}
```

### Fontes de plugins suportadas

| Fonte | Tipo | Campos |
|-------|------|--------|
| Caminho relativo | string | `"./meu-plugin"` |
| GitHub | object | `repo`, `ref?`, `sha?` |
| URL Git | object | `url`, `ref?`, `sha?` |
| Git subdiretório | object | `url`, `path`, `ref?`, `sha?` |
| npm | object | `package`, `version?`, `registry?` |
| pip | object | `package`, `version?`, `registry?` |

### Marketplace oficial (Anthropic)

- Console: [platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit)
- Claude.ai: [claude.ai/settings/plugins/submit](https://claude.ai/settings/plugins/submit)

---

## 10. Migração de configurações existentes para plugins

### Passos básicos

1. **Criar a estrutura do plugin:**

```bash
mkdir -p meu-plugin/.claude-plugin
```

2. **Criar o manifesto:**

```json
{
  "name": "meu-plugin",
  "description": "Migrado da configuração standalone",
  "version": "1.0.0"
}
```

3. **Copiar arquivos existentes:**

```bash
cp -r .claude/commands meu-plugin/
cp -r .claude/agents meu-plugin/
cp -r .claude/skills meu-plugin/
```

4. **Migrar hooks:** se tiver hooks em `settings.json`, crie `meu-plugin/hooks/hooks.json` e copie o objeto `hooks` do arquivo de settings. O comando recebe o input no stdin (JSON); use `jq` para extrair o caminho do arquivo:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "jq -r '.tool_input.file_path' | xargs npm run lint:fix" }]
      }
    ]
  }
}
```

5. **Testar:**

```bash
claude --plugin-dir ./meu-plugin
```

### O que muda na migração

| Standalone (`.claude/`) | Plugin |
|-------------------------|--------|
| Disponível em um projeto | Compartilhável via marketplaces |
| Arquivos em `.claude/commands/` | Arquivos em `plugin-name/commands/` |
| Hooks em `settings.json` | Hooks em `hooks/hooks.json` |
| Compartilhar por cópia manual | Instalação com `/plugin install` |

Depois da migração, pode remover os arquivos originais em `.claude/` para evitar duplicação.

---

## 11. Exemplos práticos

### Exemplo 1: Plugin mínimo com uma skill

```bash
mkdir -p meu-plugin/.claude-plugin
mkdir -p meu-plugin/skills/cumprimentar
```

`meu-plugin/.claude-plugin/plugin.json`:

```json
{
  "name": "meu-plugin",
  "description": "Plugin de exemplo com cumprimento",
  "version": "1.0.0"
}
```

`meu-plugin/skills/cumprimentar/SKILL.md`:

```markdown
---
description: Cumprimenta o usuário de forma amigável
disable-model-invocation: true
---

Cumprimente o usuário calorosamente e pergunte como pode ajudar hoje.
```

Teste: `claude --plugin-dir ./meu-plugin` e execute `/meu-plugin:cumprimentar`.

### Exemplo 2: Plugin com skill com argumentos

`meu-plugin/skills/cumprimentar/SKILL.md`:

```markdown
---
description: Cumprimenta o usuário com mensagem personalizada
---

Cumprimente o usuário chamado "$ARGUMENTS" e pergunte como pode ajudar.
```

Uso: `/meu-plugin:cumprimentar Maria`

### Exemplo 3: Plugin com hook de formatação

`meu-plugin/hooks/hooks.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs --no-run-if-empty prettier --write"
          }
        ]
      }
    ]
  }
}
```

### Exemplo 4: Plugin com agent como padrão

`meu-plugin/agents/revisor.md`:

```markdown
---
name: revisor
description: Revisor de código focado em qualidade e boas práticas
---

Ao revisar código, analise: estrutura, tratamentos de erro, seguranças e testes.
```

`meu-plugin/settings.json`:

```json
{
  "agent": "revisor"
}
```

### Comandos CLI úteis

```bash
claude plugin install meu-plugin@marketplace
claude plugin uninstall meu-plugin
claude plugin enable meu-plugin
claude plugin disable meu-plugin
claude plugin update meu-plugin
claude --debug   # Debug de carregamento de plugins
```

### Dicas de troubleshooting

| Problema | Causa provável | Solução |
|----------|----------------|---------|
| Plugin não carrega | `plugin.json` inválido | Verificar JSON com `claude plugin validate` |
| Commands não aparecem | Estrutura errada | Manter `commands/` na raiz, fora de `.claude-plugin/` |
| Hooks não disparam | Script não executável | `chmod +x script.sh` |
| MCP falha | Caminho errado | Usar `${CLAUDE_PLUGIN_ROOT}` para caminhos |
| LSP "Executable not found" | Binário ausente | Instalar o LSP (ex.: `npm install -g typescript-language-server typescript`) |

---

## Referências

- [Create plugins](https://code.claude.com/docs/en/plugins) — Tutorial de criação
- [Plugins reference](https://code.claude.com/docs/en/plugins-reference) — Spec técnica completa
- [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) — Criar e distribuir marketplaces
- [Discover and install plugins](https://code.claude.com/en/discover-plugins) — Instalar plugins existentes
- [Skills](https://code.claude.com/en/skills) — Desenvolvimento de skills
- [Hooks](https://code.claude.com/en/hooks) — Eventos e automação
- [Subagents](https://code.claude.com/en/sub-agents) — Configuração de agents
- [MCP](https://code.claude.com/en/mcp) — Integração com ferramentas externas
