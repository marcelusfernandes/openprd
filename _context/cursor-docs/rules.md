# Guia Completo: Rules no Cursor

Documento de referência sobre Rules (Regras) no Cursor. Baseado na [documentação oficial](https://cursor.com/docs/rules).

---

## O que são Rules no Cursor

**Rules** são instruções em nível de sistema fornecidas ao Agent do Cursor. Elas agrupam prompts, scripts e outros elementos em pacotes gerenciáveis, facilitando o compartilhamento de fluxos de trabalho entre equipes.

As Rules funcionam como **contexto persistente e reutilizável** no nível do prompt. Como modelos de linguagem não mantêm memória entre completions, as Rules garantem que a IA receba orientação consistente para:

- Gerar código
- Interpretar edições
- Ajudar com fluxos de trabalho específicos

Quando aplicadas, o conteúdo das Rules é incluído **no início do contexto do modelo**, oferecendo orientação consistente ao longo da sessão.

---

## Os 4 Tipos de Rules

| Tipo | Localização | Escopo |
|------|-------------|--------|
| **Project Rules** | `.cursor/rules/` | Limitadas ao projeto, versionáveis |
| **User Rules** | Configurações do Cursor | Global ao ambiente do usuário |
| **Team Rules** | Dashboard do Cursor | Toda a equipe (Planos Team e Enterprise) |
| **AGENTS.md** | Raiz do projeto ou subdiretórios | Alternativa simples às Project Rules |

---

## Project Rules

**Onde ficam:** `.cursor/rules/` como arquivos markdown (ou `.mdc`).

**Características:**
- Versionadas no Git
- Limitadas ao codebase do projeto
- Podem ser organizadas em subpastas
- Suportam glob patterns e frontmatter para controle fino de aplicação

**Quando usar:**
- Padronizar estilo ou decisões de arquitetura
- Automatizar fluxos de trabalho específicos do projeto
- Codificar conhecimento de domínio sobre o codebase

### Estrutura de pastas

```bash
.cursor/rules/
  react-patterns.mdc       # Rule com frontmatter (description, globs)
  api-guidelines.md       # Rule simples em markdown
  frontend/               # Organize rules em pastas
    components.md
```

### Tipos de aplicação (Rule Types)

| Tipo | Comportamento |
|------|---------------|
| **Always Apply** | Aplica em toda sessão de chat |
| **Apply Intelligently** | Quando o Agent decide que é relevante com base na description |
| **Apply to Specific Files** | Quando o arquivo combina com um padrão especificado |
| **Apply Manually** | Quando @-mencionada no chat (ex.: `@minha-regra`) |

---

## User Rules

**Onde ficam:** `Cursor Settings → Rules` (configurações do usuário).

**Características:**
- Globais ao ambiente do Cursor
- Usadas pelo Agent (Chat)
- Não se aplicam ao Inline Edit (Cmd/Ctrl+K)
- Não impactam Cursor Tab nem outras funcionalidades de IA

**Quando usar:**
- Definir estilo de comunicação preferido
- Convenções de código pessoais
- Preferências que devem valer em todos os projetos

**Exemplo:**

```md
Responda de forma concisa. Evite repetição desnecessária ou linguagem de preenchimento.
```

---

## Team Rules

**Onde ficam:** [Cursor Dashboard](https://cursor.com/dashboard?tab=team-content) (aba Team Content).

**Disponibilidade:** Planos Team e Enterprise.

**Características:**
- Gerenciadas por administradores
- Podem ser **obrigatórias** (enforced) — o usuário não pode desativar
- Suportam glob patterns para aplicação por tipo de arquivo
- Conteúdo em texto livre (não usam a estrutura de pastas das Project Rules)

**Quando usar:**
- Garantir padrões organizacionais em todos os projetos
- Compliance e workflows internos
- Padrões de código e práticas consistentes em toda a equipe

### Gerenciamento

- **Enforce this rule:** Se habilitado, a regra é obrigatória para todos; não pode ser desativada em configurações.
- **Enable this rule immediately:** Se marcado, a regra fica ativa ao ser criada; se desmarcado, fica como rascunho até ser habilitada.

---

## AGENTS.md

**Onde fica:** Raiz do projeto ou em subdiretórios (suporte aninhado).

**Características:**
- Arquivo markdown simples, sem metadata ou configurações complexas
- Alternativa leve a `.cursor/rules`
- Sem tipos de aplicação — conteúdo é lido diretamente
- Suporta hierarquia: `AGENTS.md` em subpastas aplica instruções locais

**Quando usar:**
- Projetos que precisam de instruções simples e legíveis
- Casos em que não se quer o overhead de várias rules estruturadas

**Estrutura com subpastas:**

```bash
project/
  AGENTS.md              # Instruções globais
  frontend/
    AGENTS.md            # Instruções específicas do frontend
    components/
      AGENTS.md          # Instruções específicas de componentes
  backend/
    AGENTS.md            # Instruções específicas do backend
```

Instruções de `AGENTS.md` aninhados são combinadas com as dos diretórios pai; instruções mais específicas têm precedência.

**Exemplo de conteúdo:**

```markdown
# Instruções do Projeto

## Estilo de Código

- Use TypeScript para todos os novos arquivos
- Prefira componentes funcionais em React
- Use snake_case para colunas de banco de dados

## Arquitetura

- Siga o padrão repository
- Mantenha lógica de negócio em camadas de serviço
```

---

## Estrutura dos Arquivos de Rules

Cada rule é um arquivo markdown com **frontmatter** (metadados) e **conteúdo**. O frontmatter controla como a regra é aplicada.

### Extensões suportadas

- `.md` — markdown simples
- `.mdc` — markdown com frontmatter (recomendado para controle de aplicação)

### Exemplo de frontmatter

```markdown
---
description: "Esta regra define padrões para componentes frontend e validação de API"
alwaysApply: false
globs: ["**/*.tsx", "**/components/**"]
---

...conteúdo da regra
```

### Campos do frontmatter

| Campo | Descrição |
|-------|-----------|
| `description` | Usado pelo Agent para decidir aplicação (Apply Intelligently) |
| `alwaysApply` | Se `true`, aplica em toda sessão |
| `globs` | Padrões de arquivo para Apply to Specific Files |

### Anatomia de uma rule

```markdown
---
globs:
alwaysApply: false
---

- Use nosso padrão RPC interno ao definir serviços
- Sempre use snake_case para nomes de serviços

@service-template.ts
```

O uso de `@arquivo.ts` inclui o arquivo no contexto da regra.

---

## Como Criar Rules

### Via Settings

1. Abra **Cursor Settings → Rules, Commands**
2. Clique em **+ Add Rule**
3. O Cursor cria um novo arquivo em `.cursor/rules`
4. Em Settings você vê todas as rules e seu status

### Via Chat

1. Digite `/create-rule` no Agent
2. Descreva o que deseja
3. O Agent gera o arquivo com frontmatter apropriado e salva em `.cursor/rules`

---

## Boas Práticas

Rules eficazes são **focadas**, **acionáveis** e **bem escopadas**.

### O que fazer

- **Referenciar arquivos** em vez de copiar conteúdo — mantém rules curtas e evita desatualização
- **Reutilizar rules** quando repetir prompts no chat
- **Evitar orientações vagas** — escreva como documentação interna clara
- **Incluir exemplos concretos** ou arquivos referenciados
- **Dividir rules grandes** em múltiplas rules menores e composáveis
- **Manter rules com até 500 linhas**

### O que evitar

| Anti-padrão | Recomendação |
|-------------|--------------|
| Duplicar o que já está no codebase | Aponte para exemplos canônicos |
| Instruções para casos raros | Mantenha foco em padrões usados frequentemente |
| Documentar cada comando possível | O Agent já conhece ferramentas como npm, git, pytest |
| Copiar guias de estilo inteiros | Use um linter; o Agent já segue convenções comuns |

**Conselho:** Comece simples. Adicione rules apenas quando o Agent repetir o mesmo erro. Não otimize demais antes de entender seus padrões.

**Dica:** Faça commit das rules no Git para que toda a equipe se beneficie. Ao ver o Agent errar, atualize a rule. Você pode até marcar `@cursor` em issues ou PRs no GitHub para o Agent atualizar a rule.

---

## Importação de Rules Remotas

É possível importar rules de repositórios externos para reaproveitar configurações ou trazer rules de outras ferramentas.

### Rules remotas via GitHub

1. Abra **Cursor Settings → Rules, Commands**
2. Clique em **+ Add Rule** ao lado de Project Rules
3. Selecione **Remote Rule (Github)**
4. Cole a URL do repositório GitHub que contém a rule

**Comportamento:**
- O Cursor baixa e sincroniza a rule no seu projeto
- Rules importadas permanecem sincronizadas com o repositório de origem
- Atualizações no repositório remoto são refletidas automaticamente no projeto

---

## Precedência Entre Tipos de Rules

A ordem de aplicação e precedência é:

1. **Team Rules** (maior precedência)
2. **Project Rules**
3. **User Rules** (menor precedência)

Todas as rules aplicáveis são **mescladas**. Em caso de conflito de orientação, a fonte que aparece primeiro na ordem acima tem precedência.

---

## FAQ

### Por que minha rule não está sendo aplicada?

Verifique o tipo da rule:
- Para **Apply Intelligently**, certifique-se de que há uma `description` definida
- Para **Apply to Specific Files**, verifique se o padrão de arquivo corresponde aos arquivos referenciados

### Rules podem referenciar outras rules ou arquivos?

Sim. Use `@arquivo.ts` para incluir arquivos no contexto da rule. Você também pode @mencionar rules no chat para aplicá-las manualmente.

### Posso criar uma rule pelo chat?

Sim. Basta pedir ao Agent para criar uma nova rule para você.

### Rules impactam Cursor Tab ou outras funcionalidades de IA?

Não. Rules não afetam Cursor Tab nem outras funcionalidades de IA.

### User Rules se aplicam ao Inline Edit (Cmd/Ctrl+K)?

Não. User Rules são usadas apenas pelo Agent (Chat).

---

## Referências

- [Documentação oficial: Rules](https://cursor.com/docs/rules)
- [Documentação oficial: Enterprise](https://cursor.com/docs/enterprise)
- [Cursor Dashboard (Team Content)](https://cursor.com/dashboard?tab=team-content)
