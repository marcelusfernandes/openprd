---
name: validacao
description: Run guardrail validation on project outputs
disable-model-invocation: true
---

# Validacao - Guardrail Validation Runner

## Overview
Executes data integrity validations on project outputs using both the `guardrails-validator` skill and the automated validation script.

## Step 1: Determine Target

If the user specified a target (file or folder), use that. Otherwise, use AskUserQuestion:

```json
AskUserQuestion({
  questions: [{
    question: "O que você quer validar?",
    header: "Alvo",
    multiSelect: false,
    options: [
      { label: "Projeto inteiro (Recomendado)", description: "Validar todos os outputs (1-problem, 2-solution, 3-delivery)" },
      { label: "Fase 1: Problemas", description: "Validar apenas /1-problem/" },
      { label: "Fase 2: Soluções", description: "Validar apenas /2-solution/" },
      { label: "Fase 3: Entregáveis", description: "Validar apenas /3-delivery/" }
    ]
  }]
})
```

## Step 2: Run Automated Script

Execute the deterministic validation script:
```bash
python3 .cursor/scripts/validate-guardrails.py [target-path]
```

If the script is not available or fails, proceed with manual validation only and inform the user.

## Step 3: Run Manual Validation

Apply the `guardrails-validator` skill (from `.claude/skills/guardrails-validator/SKILL.md`) to perform the deeper semantic checks:

- Read each target file
- Check against the validation checklist (Critical / Warning / Advisory levels)
- Identify violations with exact line references and suggested fixes

## Step 4: Report Results

Present a structured report:

```
## Validation Report: [target]

### Critical Issues (Block Delivery)
- [file:line] Description of violation → Suggested fix

### Warnings (Require Fix)
- [file:line] Description → Suggested fix

### Advisory (Best Practice)
- [file:line] Description → Suggestion

### Summary
- Files scanned: N
- Critical: N | Warnings: N | Advisory: N
- Status: PASS / FAIL
```

## Step 5: Offer Next Actions

Use AskUserQuestion:
```json
AskUserQuestion({
  questions: [{
    question: "Validação concluída. O que quer fazer?",
    header: "Ação",
    multiSelect: false,
    options: [
      { label: "Corrigir problemas", description: "Corrigir warnings e advisories automaticamente" },
      { label: "Validar de novo", description: "Rodar validação novamente após correções" },
      { label: "Tá bom, continuar", description: "Prosseguir com o workflow" }
    ]
  }]
})
```
