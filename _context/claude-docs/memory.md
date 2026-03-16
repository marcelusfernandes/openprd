# Como o Claude Lembra do Seu Projeto — Guia de Referência

> **Fonte:** [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)

Cada sessão do Claude Code começa com um contexto novo. Dois mecanismos mantêm conhecimento entre sessões:

- **Auto memory:** notas que o Claude escreve para si mesmo com base em correções e preferências do usuário
- **Arquivos CLAUDE.md:** instruções que você escreve para dar contexto persistente ao Claude

---

## 1. CLAUDE.md vs Auto Memory

O Claude Code usa dois sistemas de memória complementares. Ambos são carregados no início de cada conversa. O Claude os trata como **contexto**, não como configuração obrigatória. Quanto mais específicas e concisas forem suas instruções, mais consistente será o comportamento.

| Aspecto | CLAUDE.md | Auto memory |
|---------|-----------|-------------|
| **Quem escreve** | Você | Claude |
| **Conteúdo** | Instruções e regras | Aprendizados e padrões |
| **Escopo** | Projeto, usuário ou organização | Por árvore de trabalho (working tree) |
| **Carregamento** | A cada sessão | A cada sessão (primeiras 200 linhas) |
| **Uso típico** | Padrões de código, workflows, arquitetura do projeto | Comandos de build, insights de debug, preferências que o Claude descobre |

**Use CLAUDE.md** quando quiser guiar o comportamento do Claude. **Auto memory** permite que o Claude aprenda com suas correções sem esforço manual.

> Subagentes também podem manter sua própria auto memory. Consulte a documentação de subagentes para detalhes.

---

## 2. Locais e Escopos do CLAUDE.md

Arquivos CLAUDE.md podem ficar em vários locais. Locais mais específicos têm **precedência** sobre os mais amplos.

| Escopo | Local | Propósito | Exemplos de uso | Compartilhado com |
|--------|-------|-----------|-----------------|-------------------|
| **Managed policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br>Linux/WSL: `/etc/claude-code/CLAUDE.md`<br>Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Instruções organizacionais gerenciadas por TI/DevOps | Padrões de código da empresa, políticas de segurança, requisitos de compliance | Todos os usuários da organização |
| **Projeto** | `./CLAUDE.md` ou `./.claude/CLAUDE.md` | Instruções compartilhadas pela equipe | Arquitetura do projeto, padrões de código, workflows comuns | Membros da equipe via controle de versão |
| **Usuário** | `~/.claude/CLAUDE.md` | Preferências pessoais para todos os projetos | Estilo de código, atalhos de ferramentas | Apenas você (em todos os projetos) |
| **Local** | `./CLAUDE.local.md` | Preferências pessoais do projeto, **não versionadas** | URLs de sandbox, dados de teste preferidos | Apenas você (projeto atual) |

### Ordem de resolução

- CLAUDE.md na **hierarquia acima** do diretório de trabalho são carregados **integralmente** na inicialização
- CLAUDE.md em **subdiretórios** são carregados **sob demanda** quando o Claude lê arquivos nesses diretórios

### Configurar um CLAUDE.md de projeto

O CLAUDE.md do projeto pode ficar em `./CLAUDE.md` ou `./.claude/CLAUDE.md`. Inclua instruções que se apliquem a qualquer pessoa no projeto: comandos de build e teste, padrões de código, decisões arquiteturais, convenções de nomenclatura e workflows comuns.

**Dica:** execute `/init` para gerar um CLAUDE.md inicial. O Claude analisa o código e sugere comandos de build, instruções de teste e convenções que descobre.

---

## 3. Como Escrever Instruções Eficazes

Os arquivos CLAUDE.md entram na janela de contexto no início da sessão, consumindo tokens junto com a conversa. Como são **contexto** e não configuração forçada, a forma de escrever afeta o quanto o Claude segue as instruções.

### Tamanho

- **Meta:** menos de 200 linhas por arquivo CLAUDE.md
- Arquivos maiores consomem mais contexto e reduzem a aderência
- Se as instruções crescerem muito, divida com [imports](#4-imports-com-sintaxe-path) ou [`.claude/rules/`](#6-clauderules---regras-organizadas-por-tópico)

### Estrutura

- Use **cabeçalhos e listas** em markdown para agrupar instruções relacionadas
- O Claude lê a estrutura como um leitor humano: seções organizadas são mais fáceis de seguir que parágrafos densos

### Especificidade

Escreva instruções **concretas o suficiente** para verificar. Exemplos:

| Ruim | Bom |
|------|-----|
| "Mantenha os arquivos organizados" | "Handlers de API ficam em `src/api/handlers/`" |
| "Teste suas alterações" | "Execute `npm test` antes de commitar" |
| "Formate o código corretamente" | "Use indentação de 2 espaços" |

### Consistência

- Se duas regras se contradizem, o Claude pode escolher uma arbitrariamente
- Revise CLAUDE.md, CLAUDE.md em subdiretórios e `.claude/rules/` periodicamente para remover instruções obsoletas ou conflitantes
- Em monorepos, use `claudeMdExcludes` para ignorar CLAUDE.md de outras equipes que não se aplicam ao seu trabalho

---

## 4. Imports com Sintaxe @path

Arquivos CLAUDE.md podem importar outros arquivos usando a sintaxe `@caminho/para/arquivo`:

```text
Veja @README para visão geral do projeto e @package.json para comandos npm disponíveis.

# Instruções Adicionais
- fluxo de git @docs/git-instructions.md
```

### Regras de importação

- **Caminhos relativos e absolutos** são permitidos
- **Caminhos relativos** são resolvidos em relação ao arquivo que contém o import, **não** ao diretório de trabalho
- Arquivos importados podem importar outros recursivamente, com **profundidade máxima de 5 níveis**

### Preferências privadas (não versionadas)

Use `CLAUDE.local.md`: ele é carregado automaticamente e deve ser colocado em `.gitignore`.

### Múltiplos worktrees

Para compartilhar instruções entre worktrees do mesmo projeto, use um import do diretório home:

```text
# Preferências Individuais
- @~/.claude/my-project-instructions.md
```

### Diálogo de aprovação

Na primeira vez que o Claude Code encontrar imports externos em um projeto, mostra um diálogo listando os arquivos. Se você recusar, os imports permanecem desabilitados e o diálogo não aparece novamente.

---

## 5. Como os Arquivos CLAUDE.md são Carregados

O Claude Code lê CLAUDE.md **subindo** a árvore de diretórios a partir do diretório de trabalho, verificando cada diretório em busca de `CLAUDE.md` e `CLAUDE.local.md`.

- Se você executar o Claude Code em `foo/bar/`, ele carrega instruções de `foo/bar/CLAUDE.md` **e** `foo/CLAUDE.md`
- O Claude também descobre CLAUDE.md em **subdiretórios** abaixo do diretório atual
- Esses arquivos **não** são carregados na inicialização; são incluídos quando o Claude lê arquivos nesses subdiretórios

### Carregar de diretórios adicionais

A flag `--add-dir` dá ao Claude acesso a diretórios fora do working directory principal. Por padrão, CLAUDE.md desses diretórios **não** são carregados.

Para carregá-los, defina a variável de ambiente:

```bash
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
```

Isso inclui `CLAUDE.md`, `.claude/CLAUDE.md` e `.claude/rules/*.md` dos diretórios adicionais.

---

## 6. `.claude/rules/` — Regras Organizadas por Tópico

Em projetos maiores, você pode organizar instruções em vários arquivos na pasta `.claude/rules/`. Isso mantém as instruções modulares e mais fáceis de manter. Regras também podem ter [escopo por caminho de arquivo](#7-path-specific-rules-com-frontmatter).

### Estrutura sugerida

```text
seu-projeto/
├── .claude/
│   ├── CLAUDE.md           # Instruções principais do projeto
│   └── rules/
│       ├── code-style.md   # Estilo de código
│       ├── testing.md      # Convenções de teste
│       └── security.md     # Requisitos de segurança
```

- Arquivos em `.claude/rules/` cobrem **um tópico** por arquivo, com nomes descritivos
- Arquivos `.md` são descobertos **recursivamente**, permitindo subdiretórios como `frontend/` ou `backend/`
- Regras **sem** frontmatter `paths` são carregadas no início da sessão com a mesma prioridade de `.claude/CLAUDE.md`

### Regras em nível de usuário

Regras pessoais em `~/.claude/rules/` se aplicam a **todos os projetos** na sua máquina. São carregadas **antes** das regras do projeto, então as regras do projeto têm prioridade maior.

---

## 7. Path-Specific Rules com Frontmatter

Regras podem ser limitadas a **arquivos específicos** usando YAML frontmatter com o campo `paths`. Essas regras condicionais só carregam quando o Claude trabalha com arquivos que batem com os padrões.

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# Regras de Desenvolvimento de API

- Todos os endpoints de API devem incluir validação de entrada
- Use o formato padrão de resposta de erro
- Inclua comentários de documentação OpenAPI
```

- Regras **sem** o campo `paths` são carregadas incondicionalmente
- Regras com `paths` são acionadas quando o Claude **lê** arquivos que batem com o padrão, não em toda chamada de ferramenta

### Padrões glob suportados

| Padrão | Correspondência |
|--------|-----------------|
| `**/*.ts` | Todos os arquivos TypeScript em qualquer diretório |
| `src/**/*` | Todos os arquivos sob `src/` |
| `*.md` | Arquivos markdown na raiz do projeto |
| `src/components/*.tsx` | Componentes React em um diretório específico |

Você pode especificar **vários padrões** e usar **brace expansion** para múltiplas extensões:

```markdown
---
paths:
  - "src/**/*.{ts,tsx}"
  - "lib/**/*.ts"
  - "tests/**/*.test.ts"
---
```

### Symlinks para regras compartilhadas

`.claude/rules/` suporta **symlinks**, permitindo manter um conjunto de regras compartilhadas e vinculá-las em vários projetos:

```bash
ln -s ~/shared-claude-rules .claude/rules/shared
ln -s ~/company-standards/security.md .claude/rules/security.md
```

---

## 8. Auto Memory — Funcionamento

Auto memory permite que o Claude **acumule conhecimento** entre sessões sem que você escreva nada. O Claude salva notas para si mesmo durante o trabalho: comandos de build, insights de debug, notas de arquitetura, preferências de estilo de código e hábitos de workflow.

O Claude **não** salva algo em toda sessão. Ele decide o que vale a pena lembrar com base na utilidade em conversas futuras.

### Habilitar ou desabilitar

- **Padrão:** ligado
- No diálogo: use o comando `/memory` e o toggle de auto memory
- No projeto: defina em `settings`:

```json
{
  "autoMemoryEnabled": false
}
```

Via variável de ambiente:

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

### Local de armazenamento

Cada projeto tem seu próprio diretório de memória em:

```
~/.claude/projects/<projeto>/memory/
```

O `<projeto>` é derivado do **repositório git**; todos os worktrees e subdiretórios do mesmo repo compartilham o mesmo diretório. Fora de um repo git, a raiz do projeto é usada.

Estrutura típica:

```text
~/.claude/projects/<projeto>/memory/
├── MEMORY.md          # Índice conciso, carregado em toda sessão
├── debugging.md       # Notas detalhadas sobre padrões de debug
├── api-conventions.md # Decisões de design de API
└── ...                # Outros arquivos de tópico que o Claude cria
```

- **`MEMORY.md`** funciona como índice do diretório
- A memória é **local à máquina**; não é compartilhada entre máquinas ou ambientes cloud

### Limite de 200 linhas

- As **primeiras 200 linhas** de `MEMORY.md` são carregadas no início de cada conversa
- Conteúdo **além da linha 200** **não** é carregado no início da sessão
- O Claude mantém `MEMORY.md` conciso movendo notas detalhadas para arquivos de tópico separados
- Arquivos de tópico (`debugging.md`, `patterns.md`, etc.) **não** são carregados no startup; o Claude os lê sob demanda quando precisa

> O limite de 200 linhas vale apenas para `MEMORY.md`. CLAUDE.md é carregado inteiro, mas arquivos menores tendem a ter melhor aderência.

---

## 9. Comando /memory

O comando `/memory` permite:

1. **Listar** todos os arquivos CLAUDE.md e rules carregados na sessão atual
2. **Alternar** auto memory ligado/desligado
3. **Abrir** o link para a pasta de auto memory
4. **Selecionar** qualquer arquivo para abrir no editor

### Quando pedir ao Claude para lembrar

- Frases como *"sempre use pnpm, não npm"* ou *"lembre que os testes de API exigem Redis local"* → o Claude salva na **auto memory**
- Para gravar instruções em **CLAUDE.md**, peça explicitamente: *"adicione isso ao CLAUDE.md"* ou edite o arquivo via `/memory`

---

## 10. Troubleshooting de Problemas Comuns

### O Claude não está seguindo meu CLAUDE.md

CLAUDE.md é **contexto**, não imposição. O Claude lê e tenta seguir, mas não há garantia de conformidade estrita, sobretudo com instruções vagas ou conflitantes.

**Para debugar:**

- Procure **instruções conflitantes** entre arquivos CLAUDE.md
- Torne as instruções **mais específicas** (ex.: "Use indentação de 2 espaços" em vez de "formate o código")
- Confira se o CLAUDE.md relevante está em um **local que será carregado** na sessão
- Execute `/memory` para verificar quais arquivos estão carregados; se um arquivo não aparece, o Claude não o enxerga
- Use o hook `InstructionsLoaded` para registrar exatamente quais arquivos de instrução foram carregados e quando

### Não sei o que a auto memory salvou

Execute `/memory` e escolha a pasta de auto memory para explorar o conteúdo. Tudo é markdown simples que você pode ler, editar ou apagar.

### Meu CLAUDE.md está muito grande

Arquivos com mais de 200 linhas consomem mais contexto e podem reduzir aderência. Movimente conteúdo detalhado para:

- Arquivos separados referenciados com imports `@path`
- Arquivos em `.claude/rules/`

### Instruções parecem perdidas depois de /compact

CLAUDE.md **não é afetado** pelo compaction. Depois de `/compact`, o Claude relê o CLAUDE.md do disco e o injeta de novo na sessão. Se uma instrução sumiu após compaction, ela foi dada **apenas na conversa**, não foi salva no CLAUDE.md. Adicione-a ao CLAUDE.md para persistência entre sessões.

---

## 11. Boas Práticas para Times Grandes

Para organizações que usam Claude Code em várias equipes, é possível centralizar instruções e controlar quais CLAUDE.md são carregados.

### Implantar CLAUDE.md organizacional

Crie e implante um CLAUDE.md gerenciado centralmente que se aplique a todos os usuários da máquina. **Esse arquivo não pode ser excluído** por configurações individuais.

**Local do arquivo:**

- Windows: `C:\Program Files\ClaudeCode\CLAUDE.md`
- Linux e WSL: `/etc/claude-code/CLAUDE.md`
- macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`

**Implantação:** use MDM, Group Policy, Ansible ou ferramentas similares para distribuir o arquivo.

### Excluir CLAUDE.md específicos

Em monorepos grandes, CLAUDE.md de diretórios ancestrais podem conter instruções irrelevantes. A configuração `claudeMdExcludes` permite ignorar arquivos por caminho ou padrão glob.

Exemplo em `.claude/settings.local.json` (para manter local e fora do git):

```json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```

- Padrões são aplicados contra **caminhos absolutos**
- Pode ser configurado em qualquer camada de settings: usuário, projeto, local ou managed policy
- Arrays são **mesclados** entre camadas
- **Managed policy CLAUDE.md não pode ser excluído** — instruções organizacionais sempre se aplicam

---

## Recursos Relacionados

- [Subagent memory](https://code.claude.com/en/sub-agents#enable-persistent-memory): auto memory para subagentes
- [Manage sessions](https://code.claude.com/en/sessions): gerenciar contexto, retomar conversas e rodar sessões paralelas
- [Settings](https://code.claude.com/en/settings): configurar comportamento do Claude Code
- [Skills](https://code.claude.com/en/skills): workflows repetíveis carregados sob demanda
