# OpenPRD — Product Discovery Copilot

Copiloto AI de product discovery. Conversa com você, entende seu produto, pesquisa seu mercado, analisa dados e entrevistas — e quando você quer estrutura, gera documentação completa até stories no Jira.

> Primeira vez? Comece pelo [START-HERE.md](START-HERE.md).
> Termos desconhecidos? Consulte o [glossario.md](glossario.md).

## Como usar

**Só abre o projeto no Claude Code e conversa.** Não precisa de nenhum comando. O copiloto detecta seu contexto, pergunta sobre seu produto, e se adapta ao que você precisa.

Se preferir atalhos:
- `/pair` — modo copiloto explícito (pensar junto, explorar, qualquer ordem)
- `/start-workflow` — pipeline estruturado (Pain Point Brief, Data-First, Founder Fast Track, completo)
- `/quick-ask` — pergunta rápida sem rodar processo

## O que você recebe

- Análise detalhada de cada entrevista
- Mapa de problemas agrupados por tema (pain points, clusters, JTBDs)
- Jornada do usuário (atual e futura)
- Relatório executivo com TL;DR + revenue impact
- Priorização de oportunidades e escopo de MVP
- Roadmap de produto com justificativas
- Documentação formatada pro Confluence
- Épicos e stories prontos pro Jira
- Export HTML/PDF pronto pra apresentar pro VP

Descrições completas: [entregaveis.md](entregaveis.md) | Exemplo real: [demo/](demo/)

## Formatos aceitos

Mande o que tiver — o copiloto sabe lidar:

| Formato | Suporte |
|---------|---------|
| Markdown (.md), texto (.txt) | Nativo |
| CSV, TSV | Nativo |
| Excel (.xlsx, .xlsm) | Via skill Anthropic |
| Word (.docx) | Via skill Anthropic |
| PowerPoint (.pptx) | Via skill Anthropic |
| PDF | Via skill Anthropic |
| Áudio/vídeo (Zoom, Loom) | Via /transcribe (Whisper local ou Otter.ai) |
| Notas de call, bullet points | Aceito como entrevista |

## Modos de discovery

| Modo | Quando usar | Tempo |
|------|------------|-------|
| **Founder Fast Track** | 2-4 calls, resultado rápido | ~30 min |
| **Pain Point Brief** | Resumo executivo focado | 1-2h |
| **Data-First** | Começar com Amplitude/BigQuery | 1-2h |
| **Stakeholder Prep** | Preparar pra reunião com VP | 2-3h |
| **Pipeline Completo** | Discovery de ponta a ponta | 4-7h |

## Integrações suportadas

Todas opcionais — o sistema funciona só com entrevistas ou até sem elas.

| Categoria | Ferramentas |
|-----------|-------------|
| **Analytics** | Amplitude, Mixpanel, PostHog, Pendo |
| **BI / Data** | BigQuery, Metabase, Tableau, Databricks, Snowflake, Redash |
| **Produto** | Jira, Linear, Productboard, LaunchDarkly |
| **Feedback** | Hotjar, Zendesk, Intercom, Dovetail |
| **CRM** | Salesforce, Segment |
| **Colaboração** | Confluence, Slack, Notion, Miro, Figma, Loom |
| **Research** | Pesquisa online (WebSearch), Synthetic Users, NotebookLM |

## Todos os comandos

| Comando | O que faz |
|---------|-----------|
| `/pair` | Copiloto de pensamento (modo padrão) |
| `/start-workflow` | Pipeline estruturado (5 modos) |
| `/setup` | Configurar ferramentas |
| `/project` | Gerenciar projetos e domínios |
| `/discovery-map` | Ver progresso do discovery |
| `/evidence-board` | Mapa visual de evidências |
| `/export-presentation` | Exportar pra HTML/PDF |
| `/revenue-impact` | Calcular impacto financeiro |
| `/evidence-registry` | Registro central de evidências |
| `/web-research` | Pesquisar produto, mercado, concorrentes online |
| `/transcribe` | Transcrever áudio/vídeo de entrevistas |
| `/entrevista` | Entrevista sintética com persona |
| `/cross-phase-validator` | Validação cruzada entre fases |
| `/investigation-team` | Investigar problema com hipóteses concorrentes |
| `/quick-ask` | Pergunta rápida |
| `/validacao` | Verificar qualidade dos outputs |

## Pré-requisitos

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) instalado
- Abrir este projeto no terminal
- Pronto. Nenhuma outra ferramenta é obrigatória.

## Seus dados

Tudo roda local. Nada é enviado a servidores externos. Detalhes em [START-HERE.md](START-HERE.md#seus-dados).

## Glossário

Todos os termos explicados em linguagem simples: [glossario.md](glossario.md)
