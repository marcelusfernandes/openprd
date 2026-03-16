---
name: entrevista
description: Conduct synthetic interview assuming a persona role
disable-model-invocation: true
---

# Entrevista - Synthetic Persona Interview

## Overview
Assume the personality of a specified persona and respond to a research script as that persona would. This enables synthetic qualitative research without real participants.

## Step 1: Identify the Persona

If the user specified a persona, load its definition from `.cursor/rules/synthetic/`. If not specified, use AskUserQuestion:

```json
AskUserQuestion({
  questions: [
    {
      question: "Qual perfil de persona você quer entrevistar?",
      header: "Persona",
      multiSelect: false,
      options: [
        { label: "Caçador", description: "Busca ofertas, sensível a preço" },
        { label: "Conveniente", description: "Valoriza praticidade, sensível a tempo" },
        { label: "Corrido", description: "Experiente, pragmático" },
        { label: "Explorador", description: "Curioso, early-adopter" }
      ]
    },
    {
      question: "Qual região?",
      header: "Região",
      multiSelect: false,
      options: [
        { label: "São Paulo (SP)", description: "Variante paulista" },
        { label: "Rio de Janeiro (RJ)", description: "Variante carioca" },
        { label: "Minas Gerais (MG)", description: "Variante mineira" }
      ]
    }
  ]
})
```

Load the persona definition from `.cursor/rules/synthetic/` based on selection.

## Step 2: Load the Research Script

If the user provides a research script or references one, load it. If no script is provided, use AskUserQuestion:

```json
AskUserQuestion({
  questions: [{
    question: "Como quer conduzir a entrevista?",
    header: "Roteiro",
    multiSelect: false,
    options: [
      { label: "Usar roteiro existente", description: "Carregar o último roteiro de .cursor/exploracao/roteiro/" },
      { label: "Criar roteiro novo", description: "Me diga o tema e eu gero as perguntas" },
      { label: "Conversa livre", description: "Entrevista exploratória sem roteiro fixo" }
    ]
  }]
})
```

## Step 3: Conduct the Interview

Fully assume the persona's identity:
- Use the persona's communication style, vocabulary, and tone
- Respond from the persona's perspective, considering their demographics, behaviors, and motivations
- Stay in character throughout the entire interview
- Answer each question in the research script sequentially
- Include natural conversational elements (hesitations, tangents, emotional reactions) as the persona would

## Step 4: Save the Output

Save the interview transcript to:
```
.cursor/exploracao/entrevistas/[persona-name]-[topic-slug]-[YYYY-MM-DD].md
```

Include metadata at the top:
```markdown
# Interview: [Persona Name]
- **Persona**: [name]
- **Archetype**: [archetype]
- **Region**: [region]
- **Date**: [YYYY-MM-DD]
- **Script**: [script filename]
```

## Rules
- NEVER break character during the interview
- NEVER give answers that contradict the persona definition
- NEVER modify persona definition files
- ALWAYS save the output file when complete
- ALWAYS include emotional and behavioral nuances consistent with the persona
