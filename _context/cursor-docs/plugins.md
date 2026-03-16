# Plugins no Cursor — Guia Completo

> **Fonte:** [cursor.com/docs/plugins](https://cursor.com/docs/plugins) e [Plugins reference](https://cursor.com/docs/reference/plugins)  
> Documento de referência para entender, criar e distribuir plugins no Cursor IDE.

---

## 1. O que são Plugins no Cursor

**Plugins** empacotam regras, skills, agents, comandos, servidores MCP e hooks em pacotes distribuíveis que funcionam no Cursor IDE. Eles permitem compartilhar configurações de IA, capacidades especializadas e integrações entre desenvolvedores e times.

### Limitações atuais

- O **Cursor CLI** ainda não suporta plugins.
- **Cloud Agents** suportam apenas servidores MCP vindos de plugins.

---

## 2. O que um plugin pode conter

Um plugin pode incluir qualquer combinação dos seguintes componentes:

| Componente | Descrição |
| --- | --- |
| **Rules** | Orientação persistente de IA e padrões de código (arquivos `.mdc`) |
| **Skills** | Capacidades especializadas para tarefas complexas |
| **Agents** | Configurações customizadas de agentes e prompts |
| **Commands** | Arquivos de comando executáveis pelo agente |
| **MCP Servers** | Integrações via Model Context Protocol |
| **Hooks** | Scripts de automação disparados por eventos |

---

## 3. O Marketplace

O [Cursor Marketplace](https://cursor.com/marketplace) é onde você descobre e instala plugins. Os plugins são distribuídos como repositórios Git e submetidos à equipe do Cursor. **Todos os plugins passam por revisão manual** antes de serem listados.

- Acesse em [cursor.com/marketplace](https://cursor.com/marketplace)
- Ou pesquise por palavra-chave no painel do marketplace no Cursor

---

## 4. Team Marketplaces

Disponíveis em planos **Teams** e **Enterprise**:

| Plano | Quantidade |
| --- | --- |
| Enterprise | Marketplaces de time ilimitados |
| Teams | Até 1 marketplace de time |

### Plugins obrigatórios vs opcionais

- **Opcional:** O plugin fica disponível para todos no grupo; cada desenvolvedor escolhe se instala.
- **Obrigatório:** Após salvar, o plugin é instalado automaticamente para todos no grupo.

### Como adicionar um Team Marketplace

1. Configure o nome e descrição do marketplace e salve.
2. Revise os plugins parsed e defina grupos de Team Access (opcional), então continue.
3. Cole o URL do repositório GitHub e continue.
4. Em Team Marketplaces, clique em Import.
5. Acesse Dashboard → Settings → Plugins.

**Exemplo de repositório:** [fieldsphere/cursor-team-marketplace-template](https://github.com/fieldsphere/cursor-team-marketplace-template)

### Integração com SCIM

Grupos de distribuição podem ser controlados por grupos de diretório sincronizados via [SCIM](https://cursor.com/docs/account/teams/scim). Gerencie a associação no seu provedor de identidade.

---

## 5. Instalação de plugins

- Instale a partir do marketplace.
- Escopo: **projeto** ou **nível do usuário**.

### Deeplinks para MCP Apps

Compartilhe configurações de servidores MCP via links de instalação:

```
cursor://anysphere.cursor-deeplink/mcp/install?name=$NAME&config=$BASE64_ENCODED_CONFIG
```

1. Substitua `$NAME` e `$BASE64_ENCODED_CONFIG` pelo nome e config em Base64.
2. Use `JSON.stringify` na configuração e codifique em Base64.
3. O usuário clica no link e o Cursor solicita a instalação.

Veja [MCP install links](https://cursor.com/docs/mcp/install-links) para detalhes.

---

## 6. Gerenciando plugins instalados

### MCP Servers

Ative/desative em Cursor Settings:

1. Alterne o toggle ao lado do servidor.
2. Acesse Features → Model Context Protocol.
3. Abra Settings (Cmd+Shift+J).

Servidores desativados não carregam nem aparecem no chat.

### Rules e Skills

Gerenciados em Cursor Settings → Rules:

- **Rules:** Always, Agent Decides ou Manual.
- **Skills:** Aparecem em Agent Decides e podem ser invocados com `/skill-name` no chat.

---

## 7. Como criar um plugin

### Estrutura básica

Um plugin é um diretório com um manifesto `.cursor-plugin/plugin.json` e seus componentes:

```
my-plugin/
├── .cursor-plugin/
│   └── plugin.json
├── rules/
│   └── coding-standards.mdc
├── skills/
│   └── code-reviewer/
│       └── SKILL.md
├── agents/
├── commands/
├── hooks/
├── .mcp.json
└── README.md
```

Use o [repositório template oficial](https://github.com/cursor/plugin-template) ou crie do zero.

### Manifesto mínimo (plugin.json)

O manifesto exige apenas o campo `name`:

```json
{
  "name": "my-plugin",
  "description": "Custom development tools",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

### Publicação

Quando estiver pronto, submeta em [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish). Para repositórios com múltiplos plugins, crie um manifesto em `.cursor-plugin/marketplace.json`.

---

## 8. Referência do manifest (plugin.json)

### Campos obrigatórios

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `name` | string | Identificador. Lowercase, kebab-case. Ex: `my-plugin`, `prompts.chat` |

### Campos opcionais

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `description` | string | Breve descrição |
| `version` | string | Semver (ex: `1.0.0`) |
| `author` | object | `name` (obrigatório), `email` (opcional) |
| `homepage` | string | URL da página do plugin |
| `repository` | string | URL do repositório |
| `license` | string | Ex: `MIT` |
| `keywords` | array | Tags para busca e categorização |
| `logo` | string | Caminho relativo ou URL absoluta para o logo |
| `rules` | string ou array | Caminho(s) para arquivos/diretórios de regras |
| `agents` | string ou array | Caminho(s) para agentes |
| `skills` | string ou array | Caminho(s) para skills |
| `commands` | string ou array | Caminho(s) para comandos |
| `hooks` | string ou object | Caminho ou config inline de hooks |
| `mcpServers` | string, object ou array | Config de MCP ou caminho para arquivo |

---

## 9. Descoberta automática de componentes

Se o manifest não especificar caminhos, a descoberta usa pastas padrão:

| Componente | Local padrão | Como é descoberto |
| --- | --- | --- |
| Skills | `skills/` | Subdiretórios com `SKILL.md` |
| Rules | `rules/` | Arquivos `.md`, `.mdc`, `.markdown` |
| Agents | `agents/` | Arquivos `.md`, `.mdc`, `.markdown` |
| Commands | `commands/` | Arquivos `.md`, `.mdc`, `.markdown`, `.txt` |
| Hooks | `hooks/hooks.json` | Parse por nomes de eventos |
| MCP Servers | `.mcp.json` | Parse por entradas de servidor |
| Root Skill | `SKILL.md` na raiz | Plugin single-skill (só se não houver `skills/`) |

Se um campo for especificado no manifest (ex: `"skills": "./my-skills/"`), ele substitui a descoberta por pasta para esse componente.

---

## 10. Formatos dos componentes

### Rules (rules/*.mdc)

Regras requerem YAML frontmatter:

```markdown
---
description: Prefer const over let for variables that are never reassigned
alwaysApply: true
globs: "**/*.ts"
---

prefer-const: Sempre use `const` para variáveis nunca reatribuídas.
```

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `description` | string | O que a regra faz |
| `alwaysApply` | boolean | `true` = aplica a todos os arquivos |
| `globs` | string/array | Padrões de arquivo (ex: `"**/*.ts"`) |

### Skills (skills/*/SKILL.md)

```markdown
---
name: api-designer
description: Projeta APIs RESTful seguindo OpenAPI 3.0.
  Use ao criar endpoints, revisar contratos ou gerar documentação.
---

# API Designer Skill

## Quando usar
- Criar novos endpoints
- Revisar contratos de API
```

### Agents (agents/*.md)

```markdown
---
name: security-reviewer
description: Revisor focado em segurança
---

Você é um revisor de segurança. Verifique:
1. Injeções (SQL, XSS)
2. Autenticação/autorização
3. Exposição de dados sensíveis
```

### Commands (commands/*.md)

```markdown
---
name: deploy-staging
description: Faz deploy do branch atual para staging
---

# Deploy para staging
1. Rodar testes
2. Build do projeto
3. Push para branch staging
```

### Hooks (hooks/hooks.json)

```json
{
  "hooks": {
    "afterFileEdit": [
      { "command": "./scripts/format-code.sh" }
    ],
    "beforeShellExecution": [
      {
        "command": "./scripts/validate-shell.sh",
        "matcher": "rm|curl|wget"
      }
    ],
    "sessionEnd": [
      { "command": "./scripts/audit.sh" }
    ]
  }
}
```

**Eventos disponíveis:** `beforeTabFileRead`, `afterTabFileEdit`, `sessionStart`, `sessionEnd`, `preToolUse`, `postToolUse`, `postToolUseFailure`, `subagentStart`, `subagentStop`, `beforeShellExecution`, `afterShellExecution`, `beforeMCPExecution`, `afterMCPExecution`, `beforeReadFile`, `afterFileEdit`, `beforeSubmitPrompt`, `preCompact`, `stop`, `afterAgentResponse`, `afterAgentThought`.

### MCP Servers (.mcp.json)

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${POSTGRES_URL}"
      }
    }
  }
}
```

---

## 11. Repositórios multi-plugin

Use um manifesto em `.cursor-plugin/marketplace.json` na raiz do repositório:

```json
{
  "name": "my-marketplace",
  "owner": {
    "name": "Your Org",
    "email": "plugins@yourorg.com"
  },
  "metadata": {
    "description": "Coleção de plugins para desenvolvedores"
  },
  "plugins": [
    {
      "name": "plugin-one",
      "source": "plugin-one",
      "description": "Primeiro plugin"
    },
    {
      "name": "plugin-two",
      "source": "plugin-two",
      "description": "Segundo plugin"
    }
  ]
}
```

Máximo de 500 plugins por marketplace.

---

## 12. Segurança do marketplace

- **Revisão manual:** Todos os plugins são revisados antes de serem listados.
- **Código aberto:** Plugins precisam ser open source.
- **Atualizações:** Cada atualização passa por revisão.
- **Risco:** Plugins são leves (principalmente markdown e scripts). Nenhum binário é distribuído.
- **MCP:** Plugins respeitam allowlist/blocklist de MCP. Servidores bloqueados não fazem chamadas.
- **Reportar problemas:** [security-reports@cursor.com](mailto:security-reports@cursor.com)

---

## 13. Checklist de submissão

- [ ] Para multi-plugin: `.cursor-plugin/marketplace.json` na raiz com nomes únicos
- [ ] Plugin testado localmente
- [ ] Caminhos relativos e válidos (sem `..`, sem caminhos absolutos)
- [ ] `README.md` descrevendo uso e configuração
- [ ] Logo no repositório e referenciado por caminho relativo (se fornecido)
- [ ] Rules, skills, agents e commands com frontmatter correto
- [ ] `description` clara
- [ ] `name` único, lowercase, kebab-case
- [ ] Manifest válido em `.cursor-plugin/plugin.json`

---

## 14. Boas práticas

1. **Use o template oficial** para começar: [github.com/cursor/plugin-template](https://github.com/cursor/plugin-template).
2. **Documente bem** no README o que o plugin faz e como configurá-lo.
3. **Frontmatter completo** em rules, skills e agents ajuda descoberta e documentação.
4. **Logos:** Prefira commitá-los no repo e usar caminho relativo em `logo`.
5. **Caminhos relativos** sempre; evite `..` e caminhos absolutos.
6. **Teste localmente** antes de submeter.
7. **MCP:** Respeite variáveis de ambiente e evite credenciais hardcoded.

---

## 15. Referências

- [Plugins overview](https://cursor.com/docs/plugins)
- [Plugins reference](https://cursor.com/docs/reference/plugins)
- [Plugin template](https://github.com/cursor/plugin-template)
- [Cursor Marketplace](https://cursor.com/marketplace)
- [Publish plugin](https://cursor.com/marketplace/publish)
- [MCP install links](https://cursor.com/docs/mcp/install-links)
- [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security)
