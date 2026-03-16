---
name: setup
description: Interactive onboarding wizard for Product Managers. Detects installed tools, guides through configuration of analytics, product, collaboration, and data platforms. Configures MCP servers, env vars, and CLIs automatically.
user-invocable: true
---

# Setup Wizard — Onboarding Interativo para PMs

## Propósito

Guiar Product Managers não-técnicos pela configuração completa do harness. O PM responde perguntas simples, e o harness faz toda a configuração nos bastidores. Deve parecer mágica.

## Tom de Voz

- Amigável, acessível, zero jargão técnico
- Celebrar cada ferramenta configurada ("Pronto! Jira conectado.")
- Nunca mostrar JSONs, configs ou comandos ao usuário
- Se algo der errado, explicar em linguagem simples e oferecer alternativa

## Fluxo Principal

### 1. Boas-vindas + Contexto do Produto

Primeiro, entender o PM e seu produto. Abordagem CONVERSACIONAL, não formulário.

```
Oi! Eu sou seu copiloto de product discovery.
Antes de configurar qualquer ferramenta, preciso entender seu produto.
Me conta: o que vocês fazem e pra quem?
```

Deixar o PM falar livremente. Depois de ouvir:

**Avaliar se tem contexto suficiente:**
- Sei o que o produto faz?
- Sei quem são os usuários?
- Sei qual o mercado/segmento?
- Sei qual problema o PM quer investigar?

**Se falta contexto**, oferecer pesquisa:
```
Entendi que vocês são [resumo]. Posso pesquisar online pra
entender melhor o mercado e o que existe por aí. Quer que eu faça
isso agora? Leva uns 30 segundos.
```

Se PM aceitar → rodar /web-research silenciosamente (produto + mercado + concorrentes).
Se PM recusar → seguir com o que tem.

**Salvar contexto** em `0-documentation/0a-projectdocs/product-context.md`:
```markdown
# Product Context
**Produto:** {o que o PM descreveu}
**Usuarios:** {quem usa}
**Segmento:** {B2B/B2C/B2B2C}
**Problema em investigacao:** {o que o PM quer descobrir}
**Pesquisa online:** {sim/nao} — {resumo se fez}
```

Esse arquivo sera lido pelo Agent 0 para gerar broad-context.md mais rico.

### 1b. Projeto (se ainda não existe)

Só depois de entender o produto, criar o projeto.
Verificar se existe um projeto ativo (`python3 _tools/project.py status`).

Se NÃO existir:
```
Beleza, entendi o contexto. Vou criar seu projeto de discovery.
Quer dar um nome ou posso chamar de "{nome sugerido baseado no problema}"?
```

Usar AskUserQuestion para nome e grupo:
```json
AskUserQuestion({
  questions: [
    {
      question: "Qual nome pro projeto?",
      header: "Projeto",
      multiSelect: false,
      options: [
        { label: "Vou digitar", description: "Escolher um nome personalizado" },
        { label: "{nome sugerido}", description: "Baseado no problema que você descreveu" },
        { label: "Decidir depois", description: "Criar com nome genérico e renomear depois" }
      ]
    },
    {
      question: "Você faz parte de alguma squad ou área?",
      header: "Squad",
      multiSelect: false,
      options: [
        { label: "Vou digitar", description: "Informar minha squad/área" },
        { label: "Sem squad", description: "Projeto independente" }
      ]
    }
  ]
})
```

Criar projeto via: `python3 _tools/project.py create "Nome" --group "Squad" --description "..."`

Se JÁ existir projeto ativo:
```
Projeto ativo: "Nome do Projeto" (Squad X)
Já tenho o contexto do produto. Vamos em frente!
```

### 1c. Detectar Perfil do PM

Baseado na conversa até aqui, classificar o PM:

| Sinal | Perfil | Adaptação |
|-------|--------|-----------|
| Nunca fez discovery, inseguro, poucas ferramentas | **Junior** | Tutoria, explicar conceitos, sugerir /pair como mentor |
| Fala de stakeholders, VP, apresentações, Miro/Notion | **Senior** | Eficiência, /export-presentation, evidence board completo |
| Menciona funnels, cohorts, A/B tests, Amplitude | **Growth** | Data-first, Q1/Q2, métricas antes de narrativa |
| Solo, sem time de produto, "só eu e o código" | **Founder** | Founder Fast Track, simplicidade, /pair como PM mentor |

Salvar perfil em `product-context.md`:
```markdown
**Perfil PM:** {Junior/Senior/Growth/Founder}
**Adaptação:** {descrição curta de como o copiloto deve se comportar}
```

NÃO perguntar diretamente "qual seu nível?" — inferir da conversa. Se incerto, assumir Junior (mais seguro — tutoria excessiva incomoda menos que falta de orientação).

### 2. Ferramentas (quando o PM quiser)

Perguntar se quer configurar agora ou depois:
```
Agora que entendi seu produto, posso conectar suas ferramentas
(analytics, Jira, Slack...) pra ter mais dados durante o discovery.
Quer configurar agora ou prefere começar o /pair direto?
```

Se "agora" → segue o fluxo de ferramentas (Chamadas 1-5 abaixo)
Se "/pair" → pula setup de ferramentas, vai direto pro copiloto

### 3. Perguntas por Categoria (usando AskUserQuestion)

Usar a tool `AskUserQuestion` com `multiSelect: true` para que o PM apenas clique nas opções. Cada pergunta suporta 2-4 opções + "Other" automático, então quebrar categorias grandes em múltiplas perguntas enviadas juntas (até 4 perguntas por chamada).

**IMPORTANTE:** Nunca pedir pro PM digitar lista de ferramentas. Sempre usar AskUserQuestion com seleção clicável.

#### Chamada 1: Colaboração + Projeto
```json
AskUserQuestion({
  questions: [
    {
      question: "Quais ferramentas de colaboração você usa?",
      header: "Colaboração",
      multiSelect: true,
      options: [
        { label: "Jira + Confluence", description: "Atlassian — gestão de projetos e documentação" },
        { label: "Slack", description: "Comunicação do time" },
        { label: "Notion", description: "Documentação e wikis" },
        { label: "Google Docs", description: "Google Workspace — Docs, Drive, Sheets" }
      ]
    },
    {
      question: "Usa alguma ferramenta visual ou de design?",
      header: "Visual",
      multiSelect: true,
      options: [
        { label: "Miro", description: "Boards colaborativos e workshops" },
        { label: "Figma", description: "Design e prototipação" },
        { label: "Nenhuma", description: "Não uso ferramentas visuais" }
      ]
    }
  ]
})
```

#### Chamada 2: Analytics
```json
AskUserQuestion({
  questions: [
    {
      question: "Qual ferramenta de analytics de produto você usa?",
      header: "Analytics",
      multiSelect: true,
      options: [
        { label: "Amplitude", description: "Funnels, cohorts, comportamento de usuários" },
        { label: "Mixpanel", description: "Eventos, funnels, segmentação" },
        { label: "PostHog", description: "Analytics open-source + feature flags" },
        { label: "Nenhuma", description: "Não uso analytics de produto" }
      ]
    },
    {
      question: "Usa alguma ferramenta de BI ou data warehouse?",
      header: "BI / Data",
      multiSelect: true,
      options: [
        { label: "BigQuery", description: "Google Cloud — SQL data warehouse" },
        { label: "Metabase", description: "Dashboards e queries SQL" },
        { label: "Tableau", description: "Visualizações e dashboards" },
        { label: "Nenhuma", description: "Não uso BI / data warehouse" }
      ]
    }
  ]
})
```
Se o PM selecionar "Other", perguntar qual (pode ser Snowflake, Databricks, Redash, etc.).

#### Chamada 3: Ferramentas de Produto
```json
AskUserQuestion({
  questions: [
    {
      question: "Quais ferramentas de gestão de produto você usa?",
      header: "Produto",
      multiSelect: true,
      options: [
        { label: "Linear", description: "Issue tracking e sprints" },
        { label: "Productboard", description: "Feature management e feedback" },
        { label: "LaunchDarkly", description: "Feature flags e rollouts" },
        { label: "Nenhuma", description: "Não uso nenhuma dessas" }
      ]
    },
    {
      question: "E ferramentas de feedback e suporte ao cliente?",
      header: "Feedback",
      multiSelect: true,
      options: [
        { label: "Hotjar", description: "Surveys, heatmaps, gravações" },
        { label: "Zendesk", description: "Tickets de suporte" },
        { label: "Intercom", description: "Chat e conversas com clientes" },
        { label: "Nenhuma", description: "Não uso nenhuma dessas" }
      ]
    }
  ]
})
```

#### Chamada 4: CRM + Dados + Extras
```json
AskUserQuestion({
  questions: [
    {
      question: "Usa CRM, monitoramento ou pesquisa?",
      header: "CRM / Ops",
      multiSelect: true,
      options: [
        { label: "Salesforce", description: "CRM — deals, clientes, churn" },
        { label: "Sentry", description: "Monitoramento de erros" },
        { label: "Dovetail", description: "Repositório de pesquisa UX" },
        { label: "Nenhuma", description: "Não uso nenhuma dessas" }
      ]
    },
    {
      question: "Quer habilitar geração de conteúdo multimídia?",
      header: "Conteúdo",
      multiSelect: true,
      options: [
        { label: "NotebookLM", description: "Gera podcasts, vídeos, slides dos seus docs" },
        { label: "Loom", description: "Transcrições de vídeos" },
        { label: "Agora não", description: "Posso configurar depois" }
      ]
    }
  ]
})
```

#### Chamada 5 (condicional): Plataformas avançadas
Só perguntar se o PM parecer técnico ou se respondeu "Other" antes:
```json
AskUserQuestion({
  questions: [
    {
      question: "Usa alguma plataforma de dados avançada?",
      header: "Dados",
      multiSelect: true,
      options: [
        { label: "Palantir Foundry", description: "Ontologia, datasets, transforms" },
        { label: "Palantir Gotham", description: "Grafos de inteligência" },
        { label: "Segment", description: "Customer Data Platform" },
        { label: "Não uso", description: "A maioria das equipes não usa — tudo bem!" }
      ]
    }
  ]
})
```

### 4. Configuração Automática

Para CADA ferramenta selecionada, seguir o fluxo:

1. **Verificar se já está configurada** — checar `.claude/.mcp.json` e env vars
2. **Se já configurada**: "✓ {Ferramenta} já está conectada!" → próxima
3. **Se NÃO configurada**: guiar o PM para obter credenciais (ver Guia de Credenciais abaixo)
4. **Configurar automaticamente** — editar `.mcp.json`, setar env vars, instalar pacotes
5. **Testar conexão** quando possível
6. **Confirmar**: "✓ {Ferramenta} configurada com sucesso!"

### 5. Resumo Final
```
Tudo pronto! Aqui está o que configuramos:

✓ Jira + Confluence — conectados
✓ Slack — conectado
✓ Amplitude — conectado
✓ Linear — conectado
○ Hotjar — configurar depois (precisa de conta Zapier)

Você está pronto para começar! Use /start-workflow para iniciar
sua primeira discovery, ou me pergunte qualquer coisa.
```

## Guia de Credenciais por Ferramenta

Para cada ferramenta, quando o PM precisar fornecer credenciais, explicar EXATAMENTE onde encontrar, passo a passo, em linguagem não-técnica.

### Atlassian (Jira + Confluence)
**Precisa:** URL do workspace, email, API token
**Guia para o PM:**
```
Para conectar o Jira e Confluence, vou precisar de 3 coisas:

1. A URL do seu workspace — é o endereço que você usa pra acessar.
   Exemplo: https://suaempresa.atlassian.net

2. Seu email — o mesmo que você usa pra fazer login no Jira

3. Um API Token — é como uma "senha especial" só pra essa conexão:
   a) Abra: https://id.atlassian.com/manage-profile/security/api-tokens
   b) Clique em "Create API token"
   c) Dê um nome tipo "Product Discovery"
   d) Copie o token que aparecer e me envie aqui

Pode ir lá que eu espero!
```
**Configuração automática:**
- Setar env vars: `CONFLUENCE_URL`, `CONFLUENCE_USERNAME`, `CONFLUENCE_API_TOKEN`, `JIRA_URL`, `JIRA_USERNAME`, `JIRA_API_TOKEN`
- A URL e username são os mesmos para ambos
- O MCP server `atlassian` já está pré-configurado no `.mcp.json`

### Slack
**Precisa:** Bot token, Team ID
**Guia para o PM:**
```
Para conectar o Slack, preciso que alguém com permissão de admin
no workspace crie um "Bot" (é tipo um app automático). Se você
for admin, é rapidinho:

1. Acesse: https://api.slack.com/apps
2. Clique em "Create New App" → "From scratch"
3. Dê o nome "Product Discovery" e escolha seu workspace
4. No menu lateral, vá em "OAuth & Permissions"
5. Em "Bot Token Scopes", adicione:
   - channels:read
   - chat:write
   - users:read
6. Clique em "Install to Workspace" e autorize
7. Copie o "Bot User OAuth Token" (começa com xoxb-)
8. Para o Team ID: abra o Slack no navegador, o ID está na URL
   (parece com T01ABCDEF)

Se não for admin, peça pro admin da equipe seguir esses passos!
```
**Configuração automática:**
- Setar env vars: `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID`

### Notion
**Precisa:** Integration token
**Guia para o PM:**
```
Para conectar o Notion:

1. Acesse: https://www.notion.so/my-integrations
2. Clique em "New integration"
3. Dê o nome "Product Discovery"
4. Selecione o workspace certo
5. Clique em "Submit" e copie o token (começa com ntn_)
6. IMPORTANTE: No Notion, vá nas páginas que quer acessar,
   clique em "..." → "Connections" → adicione "Product Discovery"

Me envie o token quando tiver!
```
**Configuração automática:**
- Setar env var: `NOTION_TOKEN`

### Google Workspace (Docs/Drive)
**Precisa:** OAuth Client ID e Secret
**Guia para o PM:**
```
Essa é um pouquinho mais chatinha de configurar, mas te guio:

1. Acesse: https://console.cloud.google.com
2. Crie um projeto (ou use um existente)
3. Vá em "APIs & Services" → "Credentials"
4. Clique "Create Credentials" → "OAuth 2.0 Client ID"
5. Tipo: "Desktop application"
6. Copie o Client ID e o Client Secret

Se isso parecer complicado demais, sem problema!
Você pode importar documentos manualmente quando precisar.
```
**Configuração automática:**
- Setar env vars: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`

### Amplitude
**Precisa:** API Key, Secret Key
**Guia para o PM:**
```
Para conectar o Amplitude:

1. No Amplitude, vá em Settings (ícone de engrenagem)
2. Clique em "Projects" e selecione seu projeto
3. Na aba "General", copie:
   - API Key (é público, sem problema)
   - Secret Key (esse é privado, não compartilhe)

Me envie os dois!
```
**Configuração automática:**
- Setar env vars: `AMPLITUDE_API_KEY`, `AMPLITUDE_SECRET_KEY`

### Mixpanel
**Precisa:** Nada! Usa OAuth no navegador
**Guia para o PM:**
```
Mixpanel é fácil! Na primeira vez que eu precisar acessar,
vai abrir uma janela no navegador pedindo pra você fazer login
no Mixpanel. Só autorizar e pronto!
```
**Configuração automática:**
- MCP remoto, sem env vars necessárias

### PostHog
**Precisa:** API Key, Project ID
**Guia para o PM:**
```
Para conectar o PostHog:

1. No PostHog, clique no seu avatar → "Settings"
2. Vá em "Personal API Keys"
3. Clique "Create personal API key"
4. Copie a chave
5. O Project ID está na URL quando você está no projeto
   (parece com um número: 12345)

Me envie a chave e o ID!
```
**Configuração automática:**
- Setar env vars: `POSTHOG_API_KEY`, `POSTHOG_PROJECT_ID`

### BigQuery
**Precisa:** Project ID, gcloud auth
**Guia para o PM:**
```
Para conectar o BigQuery:

1. Me diga o ID do projeto no Google Cloud
   (fica no topo do console: https://console.cloud.google.com)
2. Eu vou rodar um comando que abre o navegador
   pra você fazer login com sua conta Google
3. Autorize o acesso e pronto!

Qual é o Project ID?
```
**Configuração automática:**
- Rodar: `gcloud auth application-default login` (abre navegador)
- Setar env vars: `BIGQUERY_PROJECT_ID`, `BIGQUERY_LOCATION`
- Instalar gcloud SDK se não tiver

### Snowflake
**Precisa:** Account, Warehouse, User, Password, Role, Database, Schema
**Guia para o PM:**
```
O Snowflake precisa de mais informações. Pode ser mais fácil
pedir pro time de dados/engenharia te fornecer:

- Account (ex: xy12345.us-east-1)
- Warehouse (ex: COMPUTE_WH)
- Usuário e senha
- Role (ex: ANALYST)
- Database e Schema

Se tiver um admin de Snowflake na equipe, peça essas infos!
```
**Configuração automática:**
- Setar env vars: `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_WAREHOUSE`, `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, `SNOWFLAKE_ROLE`, `SNOWFLAKE_DATABASE`, `SNOWFLAKE_SCHEMA`

### Databricks
**Precisa:** Host, Token
**Guia para o PM:**
```
Para conectar o Databricks:

1. No Databricks, vá em "User Settings" → "Developer"
2. Em "Access tokens", clique "Generate new token"
3. Me envie o token e a URL do seu workspace
   (ex: https://adb-123456789.azuredatabricks.net)
```
**Configuração automática:**
- Setar env vars: `DATABRICKS_HOST`, `DATABRICKS_TOKEN`

### Metabase
**Precisa:** URL da instância, API key
**Guia para o PM:**
```
Para conectar o Metabase:

1. Me diga a URL do seu Metabase (ex: https://metabase.suaempresa.com)
2. No Metabase, vá em Admin → Settings → Authentication → API Keys
3. Crie uma nova chave e copie

Se não for admin, peça a chave pro responsável!
```
**Configuração automática:**
- Setar env vars: `METABASE_URL`, `METABASE_API_KEY`

### Tableau
**Precisa:** Server URL, Site name, Personal Access Token
**Guia para o PM:**
```
Para conectar o Tableau:

1. No Tableau Server/Online, clique no seu avatar → "My Account Settings"
2. Em "Personal Access Tokens", crie um novo:
   - Dê um nome (ex: "Discovery")
   - Copie o nome e o valor do token
3. Me diga também:
   - URL do servidor (ex: https://10az.online.tableau.com)
   - Nome do site (está na URL após /site/)
```
**Configuração automática:**
- Setar env vars: `TABLEAU_SERVER`, `TABLEAU_SITE_NAME`, `TABLEAU_PAT_NAME`, `TABLEAU_PAT_VALUE`

### Redash
**Precisa:** URL, API Key
**Guia para o PM:**
```
Para conectar o Redash:

1. Me diga a URL do seu Redash (ex: https://redash.suaempresa.com)
2. No Redash, clique no seu perfil → "API Key"
3. Copie a chave

Simples assim!
```
**Configuração automática:**
- Setar env vars: `REDASH_URL`, `REDASH_API_KEY`

### Linear
**Precisa:** Nada! Usa OAuth no navegador
**Guia para o PM:**
```
Linear é super fácil! Na primeira vez que eu acessar,
abre uma tela no navegador pra você autorizar. Só clicar
em "Allow" e tá feito!
```
**Configuração automática:**
- MCP remoto com OAuth, sem env vars

### LaunchDarkly
**Precisa:** API Key
**Guia para o PM:**
```
Para conectar o LaunchDarkly:

1. No LaunchDarkly, vá em Account Settings → Authorization
2. Clique em "Create token"
3. Dê um nome e selecione role "Reader" (suficiente pra discovery)
4. Copie o token

Me envie quando tiver!
```
**Configuração automática:**
- Setar env var: `LAUNCHDARKLY_API_KEY`

### Hotjar
**Precisa:** Client ID, Client Secret (ou Zapier)
**Guia para o PM:**
```
Hotjar tem duas formas de conectar:

Opção 1 (mais fácil) — Via Zapier:
Se você usa Zapier, posso conectar por lá. Me diga e eu explico!

Opção 2 (direto) — Via API:
1. No Hotjar, vá em "Integrations" → "API"
2. Crie um novo aplicativo OAuth
3. Copie Client ID e Client Secret
Nota: precisa do plano Ask Scale.

Qual prefere?
```
**Configuração automática (Opção 1 - Zapier):**
- Setar env vars: `ZAPIER_MCP_SERVER_ID`, `ZAPIER_API_KEY`
- Instalar: `pip install mcp2cli`
**Configuração automática (Opção 2 - Direto):**
- Setar env vars: `HOTJAR_CLIENT_ID`, `HOTJAR_CLIENT_SECRET`

### Zendesk
**Precisa:** Subdomain, Email, API Token
**Guia para o PM:**
```
Para conectar o Zendesk:

1. Me diga o subdomínio do seu Zendesk
   (é o "suaempresa" em suaempresa.zendesk.com)
2. Me diga o email que você usa pra logar
3. Para o API Token:
   a) No Zendesk, vá em Admin → Channels → API
   b) Ative o acesso por token se não estiver ativo
   c) Clique "Add API Token"
   d) Copie o token
```
**Configuração automática:**
- Setar env vars: `ZENDESK_SUBDOMAIN`, `ZENDESK_EMAIL`, `ZENDESK_API_TOKEN`

### Intercom
**Precisa:** Access Token
**Guia para o PM:**
```
Para conectar o Intercom:

1. Acesse: https://app.intercom.com/a/apps/_/developer-hub
2. Crie um novo app ou selecione existente
3. Vá em "Authentication" e copie o Access Token

Se não tiver acesso ao Developer Hub, peça pro admin!
```
**Configuração automática:**
- Setar env var: `INTERCOM_TOKEN`

### Salesforce
**Precisa:** Login via navegador (Salesforce CLI)
**Guia para o PM:**
```
Para conectar o Salesforce, vou abrir uma tela de login
no navegador. Faça login com sua conta Salesforce normalmente
e autorize o acesso. Eu cuido do resto!

Posso abrir agora?
```
**Configuração automática:**
- Rodar: `sf org login web --alias discovery`
- Setar env var: `SALESFORCE_ORG_ALIAS=discovery`
- Instalar Salesforce CLI se não tiver

### Sentry
**Precisa:** Nada para MCP remoto
**Guia para o PM:**
```
Sentry já vem pré-configurado! Na primeira vez que eu
acessar, pode pedir uma autorização no navegador.
Não precisa fazer nada agora.
```
**Configuração automática:**
- MCP remoto HTTP, sem env vars para funcionar

### Productboard
**Precisa:** API Token
**Guia para o PM:**
```
Para conectar o Productboard:

1. No Productboard, vá em Settings → Integrations → API
2. Gere um novo token de acesso
3. Copie e me envie!
```
**Configuração automática:**
- Setar env var: `PRODUCTBOARD_API_TOKEN`

### Dovetail
**Precisa:** API Token
**Guia para o PM:**
```
Para conectar o Dovetail:

1. No Dovetail, vá em Settings → API
2. Crie um Personal API Token
3. Copie e me envie!
```
**Configuração automática:**
- Setar env var: `DOVETAIL_API_TOKEN`

### Segment
**Precisa:** API Token
**Guia para o PM:**
```
Para conectar o Segment:

1. No Segment, vá em Settings → Access Management → Tokens
2. Crie um novo token com permissão de leitura
3. Copie e me envie!
```
**Configuração automática:**
- Setar env var: `SEGMENT_API_TOKEN`

### Palantir Foundry
**Precisa:** API URL, Token
**Guia para o PM:**
```
Para conectar o Palantir Foundry:

1. Me diga a URL da sua instância Foundry
   (ex: https://suaempresa.palantirfoundry.com)
2. No Foundry, gere um token de serviço:
   a) Vá em "Control Panel" → "Tokens"
   b) Crie um novo token com escopo de leitura
   c) Copie o token

Se não souber como, o admin do Foundry pode ajudar!
```
**Configuração automática:**
- Setar env vars: `FOUNDRY_API_URL`, `FOUNDRY_TOKEN`

### Palantir Gotham
**Precisa:** Hostname, Client ID, Client Secret
**Guia para o PM:**
```
Para conectar o Palantir Gotham:

1. Me diga o hostname da instância (ex: https://gotham.suaempresa.com)
2. Credenciais OAuth2 (Client ID e Client Secret)
   — essas geralmente vêm do admin do Gotham

É uma plataforma mais especializada, então provavelmente
o admin já tem essas credenciais prontas.
```
**Configuração automática:**
- Setar env vars: `GOTHAM_HOSTNAME`, `GOTHAM_CLIENT_ID`, `GOTHAM_CLIENT_SECRET`
- Instalar: `pip install gotham-platform-sdk`

### NotebookLM
**Precisa:** Login com conta Google (navegador)
**Guia para o PM:**
```
O NotebookLM é uma ferramenta incrível do Google que
transforma seus documentos em podcasts, vídeos e apresentações!

Vou instalar o necessário e abrir uma tela de login do Google
no navegador. Depois é só fazer login normalmente.

Posso instalar agora?
```
**Configuração automática:**
- Instalar: `pip install "notebooklm-py[browser]" && playwright install chromium`
- Rodar: `notebooklm login` (abre navegador)

## Como Configurar Env Vars

Ao receber credenciais do PM:

1. **Criar/atualizar `.env`** na raiz do projeto com as variáveis
2. **Garantir que `.env` está no `.gitignore`** — NUNCA commitar credenciais
3. **Exportar vars** para a sessão atual via `export VAR=value`
4. **Verificar `.mcp.json`** — confirmar que o server referencia as env vars corretas

```bash
# Exemplo de configuração automática
echo 'AMPLITUDE_API_KEY=abc123' >> .env
echo 'AMPLITUDE_SECRET_KEY=xyz789' >> .env

# Adicionar .env ao .gitignore se não estiver
grep -q '.env' .gitignore 2>/dev/null || echo '.env' >> .gitignore
```

## Como Configurar MCP Servers

O arquivo `.claude/.mcp.json` já tem todos os servers pré-configurados.
As env vars são referenciadas como `${VAR_NAME}`. Ao setar as env vars
no `.env`, os servers automaticamente pegam os valores.

Se um server NÃO estiver no `.mcp.json`, adicionar automaticamente
usando o formato correto do catálogo de referência.

## Testes de Conexão

Após configurar, tentar validar quando possível:
- MCP servers: verificar se o server inicia sem erro
- CLI tools: rodar comando de teste (ex: `notebooklm auth check --test`)
- APIs: fazer request simples de healthcheck

Se falhar, explicar o erro em linguagem simples e sugerir solução.

## Regras

- NUNCA mostrar JSON, configs ou comandos raw ao PM
- NUNCA pedir que o PM edite arquivos manualmente
- SEMPRE confirmar antes de instalar pacotes
- SEMPRE adicionar `.env` ao `.gitignore`
- NUNCA commitar credenciais
- Se o PM não souber onde encontrar algo, oferecer alternativa ou pular
- Permitir configurar depois: "Sem problema! Pode configurar quando quiser"
- Celebrar cada configuração concluída
- No final, mostrar resumo visual com ✓ e ○
