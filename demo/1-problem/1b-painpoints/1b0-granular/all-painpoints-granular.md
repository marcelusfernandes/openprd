<!-- EXEMPLO: Este é um output fictício para demonstração. -->

# Granular Pain Point Decomposition

**Sources:** maria-pm-analysis.md, joao-dev-analysis.md, lucas-founder-analysis.md
**Total Atomic Pain Points:** 10
**Agent:** 2A — Granular Specialist

---

## Atomic Pain Points

### PP-01: Ausência de guia no primeiro acesso
- **Sources:** Maria (Critical), Lucas (Critical) | **Frequency:** Every time | **Severity:** Critical
- **Atomic Issue:** Nenhum wizard, tooltip ou checklist no primeiro login
- **Evidence:** "Não sabia por onde começar" [Source: maria-pm.md], "Tentando entender a diferença entre workspace, projeto e board" [Source: lucas-founder.md]

### PP-02: Botão de criar projeto escondido em submenu
- **Sources:** Maria (High) | **Frequency:** Every time | **Severity:** High
- **Atomic Issue:** Ação primária (criar projeto) está a 3 cliques de profundidade

### PP-03: Convite de membros sem bulk import
- **Sources:** Maria (High), João (High) | **Frequency:** Every time | **Severity:** High
- **Atomic Issue:** Sem integração Slack/Google; manual um-por-um

### PP-04: Zero templates pré-configurados
- **Sources:** João (High), Lucas (High) | **Frequency:** Every time | **Severity:** High
- **Atomic Issue:** Workspace vazio no primeiro acesso; sem Sprint, Kanban, Roadmap templates

### PP-05: API instável (500 errors) e docs desatualizadas
- **Sources:** João (Critical) | **Frequency:** Often | **Severity:** Critical
- **Atomic Issue:** Endpoints de criação de projeto retornam 500; docs não refletem API atual

### PP-06: Permissões sem bulk edit
- **Sources:** João (High) | **Frequency:** Every time | **Severity:** High
- **Atomic Issue:** Config de roles exige ir usuário por usuário

### PP-07: Hierarquia conceitual confusa (workspace/projeto/board)
- **Sources:** Lucas (Critical) | **Frequency:** Every time | **Severity:** Critical
- **Atomic Issue:** Modelo mental não é explicado; 3 níveis sem onboarding contextual

### PP-08: Features pagas sem sinalização clara
- **Sources:** Lucas (High) | **Frequency:** Often | **Severity:** High
- **Atomic Issue:** Paywall aparece depois que o usuário já investiu tempo configurando

### PP-09: App mobile read-only
- **Sources:** Lucas (Medium) | **Frequency:** Always | **Severity:** Medium
- **Atomic Issue:** App não suporta ações de setup; times remote-first ficam bloqueados

### PP-10: Falta de integração com GitHub
- **Sources:** João (Medium) | **Frequency:** Always | **Severity:** Medium
- **Atomic Issue:** Devs não veem PRs/commits no board; adoção reduzida entre engenheiros

---

## Severity Summary
| Severity | Count | IDs |
|----------|-------|-----|
| Critical | 3 | PP-01, PP-05, PP-07 |
| High | 5 | PP-02, PP-03, PP-04, PP-06, PP-08 |
| Medium | 2 | PP-09, PP-10 |

**Decomposition Date:** 2026-02-17
**Analyst:** Agent 2A — Granular Specialist
