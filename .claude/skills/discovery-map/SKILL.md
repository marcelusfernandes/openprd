---
name: discovery-map
description: Shows PM where they are in the discovery process. Visual progress indicator based on completed outputs.
user-invocable: true
---

# Discovery Map — Indicador de Progresso

## Proposito

Mostrar ao PM onde ele esta no processo de discovery. Escaneia os diretorios do projeto ativo e exibe um mapa visual de progresso com sugestoes contextuais do proximo passo.

## Instrucoes

### 1. Resolver path do projeto ativo

**IMPORTANTE:** Os diretorios do projeto (`0-documentation/`, `1-problem/`, `2-solution/`, `3-delivery/`) sao symlinks. Glob pode nao segui-los. Use este fluxo:

1. Ler `projects/registry.json` para obter o slug do projeto ativo
2. Usar o path real: `projects/{slug}/` como base para todos os scans
3. Se `registry.json` nao existir, usar os paths relativos diretamente (projeto sem /project)
4. Mostrar nome do projeto ativo no output

Se o ativo for uma initiative (`active.type == "initiative"`):
- Mostrar nome do dominio + nome da initiative
- Mostrar tamanho: Investigation / Quick / Full
- Se Investigation: mostrar apenas checkpoints relevantes (notas, dados, hipoteses — sem pipeline)
- Se `_domain-context/` existir: mostrar "Contexto do dominio: disponivel (X pain points conhecidos)"

### 2. Escanear outputs

Para cada checkpoint, usar Glob ou Bash (`ls`) no path REAL do projeto:

| Checkpoint | Path (relativo ao projeto) | Criterio |
|-----------|---------------------------|----------|
| Contexto | `0-documentation/broad-context.md` | arquivo existe |
| Dados | `1-problem/0-data-landscape/data-landscape.md` | arquivo existe |
| Hipoteses | `1-problem/0-data-landscape/hypotheses.md` | arquivo existe |
| Entrevistas | `0-documentation/0b-Interviews/*` | contar arquivos (.md, .csv, .txt, .docx) |
| Analise | `1-problem/1a-interview-analysis/*.md` | contar arquivos .md |
| Pain Points | `1-problem/1b-painpoints/1b0-granular/*.md` E `1-problem/1b-painpoints/1b1-painpoints-breakdown/*.md` | ambos tem arquivos |
| JTBDs | `1-problem/1b-painpoints/1b2-jtbd/*.md` | tem arquivos |
| Jornada | `1-problem/1c-asis-journey/*.md` | tem arquivos |
| Oportunidades | `2-solution/2a-opportunities/*.md` | tem arquivos |
| MVP | `2-solution/2d-prioritization/*.md` | tem arquivos |
| Entregaveis | `3-delivery/confluence/*.md` OU `3-delivery/jira/*.md` | tem arquivos em subdirs |

### 3. Exibir mapa visual

Formato (usar `[x]` para completo, `[ ]` para pendente, contagens onde aplicavel):

```
=== Discovery Map === (Projeto: {nome})

[x] Contexto       [ ] Dados          [ ] Hipoteses
[ ] Entrevistas (0) [ ] Analise (0)    [ ] Pain Points
[ ] JTBDs          [ ] Jornada        [ ] Oportunidades
[ ] MVP            [ ] Entregaveis

Progresso: X/11 etapas concluidas
```

Nota: Dados e Hipoteses sao opcionais (fluxo data-first). Se ambos estao vazios, nao contar como pendentes — ajustar denominador para 9.

### 4. Gerar sugestao contextual

| Estado | Sugestao |
|--------|----------|
| Nenhum output | "Comece definindo o contexto do projeto com /start-workflow ou crie broad-context.md" |
| So contexto | "Configure analytics via /setup e rode 'Data-First Discovery' no /start-workflow — ou adicione entrevistas em 0-documentation/0b-Interviews/" |
| Contexto + dados | "Faca 3-5 entrevistas focadas nas hipoteses. Use /entrevista para entrevista sintetica" |
| Entrevistas sem analise | "Rode /start-workflow para analisar as entrevistas automaticamente" |
| Analise sem pain points | "Decomponha os pain points — rode /start-workflow e selecione 'Pain Point Brief'" |
| Pain points sem JTBDs | "Defina os Jobs-to-be-Done a partir dos pain points identificados" |
| JTBDs sem jornada | "Mapeie a jornada as-is para entender o contexto dos problemas" |
| Jornada sem oportunidades | "Identifique oportunidades — rode /start-workflow Fase 2" |
| Oportunidades sem MVP | "Priorize as oportunidades e defina o escopo do MVP" |
| MVP sem entregaveis | "Gere os entregaveis finais (Confluence/Jira) com /start-workflow Fase 3" |
| Tudo completo | "Discovery completo! Use /export-presentation pra gerar um PDF pro stakeholder" |

## Regras

- Apenas leitura — nao criar nem modificar arquivos
- Se nenhum projeto ativo, informar e sugerir `/project` para criar um
- Manter output conciso — mapa + sugestao + nome do projeto, nada mais
- Contar arquivos de qualquer formato relevante (.md, .csv, .txt, .docx) para entrevistas
- Para analise e demais, contar apenas .md
