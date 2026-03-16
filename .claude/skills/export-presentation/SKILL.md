---
name: export-presentation
description: Exports discovery outputs to presentation-ready HTML format. Generates stakeholder-friendly single-page documents with styling, charts (Mermaid), and print-to-PDF support.
user-invocable: true
---

# Export Presentation — Output Formatado pra Stakeholders

## Propósito

PMs precisam apresentar findings pra VPs, diretores e stakeholders que não leem markdown. Esta skill converte qualquer output do discovery em HTML formatado, pronto pra compartilhar ou imprimir como PDF.

## Como Usar

O PM pode invocar de duas formas:
1. `/export-presentation` — o sistema pergunta o que exportar
2. Dentro do `/pair`: "exporta isso pra apresentação" ou "formata pra meu VP"

## Fluxo

### 1. Selecionar o que exportar

```json
AskUserQuestion({
  questions: [{
    question: "O que você quer exportar?",
    header: "Conteúdo",
    multiSelect: false,
    options: [
      { label: "Pain Report (resumo executivo)", description: "Top pain points + evidências + recomendação" },
      { label: "Stakeholder Brief", description: "Brief adaptado pra audiência específica" },
      { label: "MVP Scope", description: "Escopo do MVP com priorização e roadmap" },
      { label: "Discovery Completo", description: "Documento completo com todas as fases" },
      { label: "Data Summary (tabular)", description: "Metricas, hipoteses e evidencias em formato tabela — ideal pra Growth PMs" },
      { label: "Custom", description: "Escolher arquivos específicos pra exportar" }
    ]
  }]
})
```

### 2. Gerar HTML Formatado

Para cada tipo de export, ler os arquivos-fonte e gerar um HTML single-file com:

**Estrutura do HTML:**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{Título do Projeto} — {Tipo de Export}</title>
  <style>
    /* Estilo profissional, print-friendly */
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; color: #1a1a1a; line-height: 1.6; }
    h1 { border-bottom: 3px solid #2563eb; padding-bottom: 12px; }
    h2 { color: #2563eb; margin-top: 2em; }
    .metric { font-size: 2em; font-weight: bold; color: #2563eb; }
    .quote { border-left: 4px solid #e5e7eb; padding-left: 16px; font-style: italic; color: #4b5563; margin: 16px 0; }
    .evidence { background: #f0f9ff; border-radius: 8px; padding: 16px; margin: 12px 0; }
    .priority-high { border-left: 4px solid #ef4444; }
    .priority-medium { border-left: 4px solid #f59e0b; }
    table { width: 100%; border-collapse: collapse; margin: 16px 0; }
    th, td { border: 1px solid #e5e7eb; padding: 10px; text-align: left; }
    th { background: #f8fafc; font-weight: 600; }
    @media print { body { padding: 20px; } h1 { page-break-before: avoid; } }
  </style>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
  <!-- Conteúdo convertido de markdown para HTML -->
  <script>mermaid.initialize({startOnLoad:true});</script>
</body>
</html>
```

**Regras de conversão:**
- Headings → `<h1>`, `<h2>`, `<h3>` com estilos
- Quotes de entrevista → `<blockquote class="quote">`
- Métricas-chave → `<span class="metric">`
- Tabelas → `<table>` formatada
- Listas de evidência → `<div class="evidence">`
- Pain points High → `<div class="priority-high">`
- Diagramas Mermaid → `<div class="mermaid">` (renderiza no browser)
- Tags `[Source: ...]` → footnotes discretos
- Tags `[AI estimation]` → tooltip ou nota de rodapé

### 3. Salvar e Instruir

Salvar o HTML em: `_exports/{slug}-{tipo}-{data}.html`

Informar ao PM:
```
Pronto! Arquivo salvo em _exports/{nome}.html

Para visualizar: abra no navegador
Para PDF: abra no navegador → Ctrl+P → "Salvar como PDF"
Para compartilhar: envie o arquivo HTML (funciona standalone, sem internet)
```

## Tipos de Export

### Pain Report
Fonte: `/1-problem/1d-problem-output/pain-report.md`
Estrutura HTML:
1. Título + data + projeto
2. Resumo executivo (3-4 frases)
3. Top 3 pain points com evidências
4. Quotes mais impactantes
5. Diagrama Mermaid: clusters de problemas
6. Recomendação + próximo passo

### Stakeholder Brief
Fonte: output do skill `stakeholder-brief`
Estrutura: adaptada por audiência (executivo = 1 página, engenharia = detalhado)

### MVP Scope
Fonte: `/2-solution/2d-prioritization/*.md`
Estrutura:
1. Escopo resumido
2. Tabela de priorização (Impact x Effort)
3. Diagrama Mermaid: roadmap em timeline
4. Riscos e trade-offs
5. Métricas de sucesso

### Data Summary (tabular)
Fonte: `/1-problem/0-data-landscape/data-landscape.md` + `hypotheses.md` + pain-report
Estrutura HTML:
1. Metricas-chave em stat cards (grandes, visuais)
2. Tabela de hipoteses: ID | Statement | Evidence | Confidence | Status
3. Tabela de pain points: Cluster | Severity | Frequency | Revenue Impact
4. Sem prosa — apenas dados estruturados com headers claros

### Discovery Completo
Fonte: todos os outputs de Phase 1 + 2
Estrutura: documento navegável com sidebar de índice (CSS-only)

## Batch Export

Se PM pedir "exporta tudo pra reuniao" ou "prepara material pra stakeholder meeting":
1. Gerar Pain Report HTML
2. Gerar Evidence Board (se outputs existem)
3. Gerar Revenue Impact (se /revenue-impact foi rodado)
4. Salvar todos em `_exports/` com prefixo do projeto
5. Listar: "3 arquivos gerados em _exports/. Abra no browser pra visualizar."

## Branding

Se PM fornecer cores e logo:
- Substituir cor primaria (#2563eb) pela cor da marca
- Adicionar logo no header do HTML
- Se nao fornecido, usar estilo padrao
- Perguntar na primeira vez: "Quer personalizar com as cores da sua empresa? Pode me dar o hex code e um link pro logo."

## Guardrails
- Manter todas as tags `[Source:]` como footnotes
- Manter `[AI estimation]` visíveis (não esconder)
- Não adicionar dados que não existam nos arquivos-fonte
- O HTML funciona offline para texto e tabelas. Diagramas Mermaid precisam de internet (CDN) — avisar o PM se incluir charts
