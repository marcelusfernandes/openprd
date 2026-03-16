---
name: quick-ask
description: Quick question without making any modifications to the project
disable-model-invocation: true
---

# Quick Ask - Read-Only Question Answering

## Purpose
Answer the user's question directly and thoroughly without making any changes to the project. Extract genuinely useful information from the codebase, documentation, and outputs.

## Rules

1. **DO NOT** create, edit, or delete any files
2. **DO NOT** run any commands that modify state
3. **DO NOT** be complacent — provide honest, critical, and useful answers
4. **DO** read any files needed to answer the question accurately
5. **DO** provide specific references (file paths, line numbers) when citing project content
6. **DO** challenge assumptions if the question contains incorrect premises
7. **DO** say "I don't know" or "this information is not available in the project" when appropriate

## How to Answer

1. Understand the question fully before reading files
2. Read relevant project files to gather accurate information
3. Synthesize a clear, direct answer
4. Include file path references for any claims about project content
5. If the question requires analysis, provide structured reasoning
6. If the question is ambiguous, answer the most likely interpretation and note alternatives

## Scope
This skill can answer questions about:
- Project structure and architecture
- Agent workflow and sequencing
- Output contents and analysis results
- Template formats and conventions
- Guardrail rules and validation criteria
- Persona definitions and research methodology
- Any content within the project files
