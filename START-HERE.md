# Product Discovery Harness — Guia de Início Rápido

## O que é isso?

Um copiloto de product discovery. Você conversa com ele, e ele te ajuda a pensar — analisar entrevistas, identificar padrões, priorizar problemas, desenhar soluções. Quando você quer estrutura, ele roda um pipeline que gera documentação completa: relatórios, roadmap, MVP, stories pro Jira.

## O que eu recebo no final?

- Análise detalhada de cada entrevista
- Mapa de problemas agrupados por tema
- Jornada do usuário (atual e futura)
- Relatório executivo pronto pra apresentar
- Priorização de oportunidades e escopo de MVP
- Roadmap de produto com justificativas
- Documentação formatada pra Confluence
- Épicos e stories prontos pra importar no Jira

Para descrições detalhadas de cada entregável, veja [`entregaveis.md`](entregaveis.md).

## Pré-requisitos

- **Claude Code** instalado ([instalar aqui](https://docs.anthropic.com/en/docs/claude-code))
- Abrir este projeto no Claude Code (terminal na pasta do projeto)
- Pronto. Nenhuma outra ferramenta é obrigatória — analytics, Jira, Slack são opcionais.

## O mínimo que preciso pra começar

- **Entrevistas:** pelo menos 3 (ideal: 5-8). Com 2 funciona, mas os padrões são mais fracos.
- **Formato:** transcricao, notas de call, bullet points, ou qualquer texto — `.md`, `.txt` ou `.docx`
- **Onde colocar:** na pasta `0-documentation/0b-Interviews/`
- **Sem entrevistas?** Tudo bem — use `/pair` pra começar com dados quantitativos (Amplitude, BigQuery) ou até pra planejar suas primeiras entrevistas.

## Como começo?

**Só conversa.** Abre o projeto no Claude Code e diz o que tá precisando — "tenho 5 entrevistas e quero entender os padrões", "preciso priorizar features pro Q3", "quero montar um roadmap". O copiloto se adapta.

Na prática, isso é o `/pair` — seu copiloto de discovery. Ele te guia, sugere análises, puxa dados das suas ferramentas, e pensa junto com você. Pode começar com entrevistas, dados quantitativos (Amplitude, BigQuery), ou até do zero planejando suas primeiras entrevistas.

**Quer o pipeline completo de uma vez?** Use `/start-workflow`. Roda o processo estruturado: analisa todas as entrevistas, mapeia problemas, prioriza soluções, gera documentação. Você valida cada fase, o sistema faz o trabalho pesado.

**Resumindo:**
- `/pair` — modo padrão. Explorar, pensar junto, qualquer ordem.
- `/start-workflow` — modo estruturado. Todas as entrevistas de uma vez, output completo.

## Quanto tempo leva?

| Fase | O que faz | Tempo estimado |
|------|-----------|----------------|
| Fase 1 | Analisa problemas e mapeia jornada | 2-4 horas |
| Fase 2 | Cria soluções, MVP e roadmap | 1-2 horas |
| Fase 3 | Gera docs pro Confluence e Jira | 30-60 min |

Pode rodar uma fase por vez — não precisa fazer tudo de uma.

## Quer ver um exemplo antes de rodar?

Veja o [projeto demo](demo/) com outputs fictícios mostrando exatamente o que cada fase produz.

## Seus Dados

- Tudo roda local na sua máquina — nenhum dado é enviado a servidores externos
- Entrevistas, análises e outputs ficam no filesystem do projeto (versionável com git)
- Credenciais (.env) nunca são commitadas (já estão no .gitignore)
- Transcrições de entrevistas não são compartilhadas — ficam em 0-documentation/
- Se usar analytics (Amplitude, BigQuery), as queries rodam via API com suas próprias credenciais
- Pesquisa online (/web-research) só roda com sua autorização explícita

## Termos desconhecidos?

Consulte o [`glossario.md`](glossario.md) — explica todos os termos de discovery em linguagem simples.

## Todos os comandos

- `/pair` — Copiloto de pensamento (recomendado pra começar)
- `/start-workflow` — Pipeline de discovery (Pain Point Brief, Data-First, completo)
- `/setup` — Configuração inicial das ferramentas
- `/project` — Criar, trocar ou listar projetos de discovery
- `/discovery-map` — Ver seu progresso no discovery
- `/evidence-board` — Mapa visual de evidências (entrevistas + dados + insights)
- `/export-presentation` — Exportar findings pra HTML/PDF (pra apresentar pro VP)
- `/entrevista` — Conduzir entrevista sintética com persona
- `/quick-ask` — Pergunta rápida sem rodar o pipeline
- `/validacao` — Verificar qualidade dos outputs gerados
