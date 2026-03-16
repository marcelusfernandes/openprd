<!-- EXEMPLO: Este é um output fictício para demonstração. -->

# MVP Scope — Onboarding Redesign NovaTech

**Agent:** S9 — Prioritization Specialist
**Input:** solution-concepts.md, cluster-onboarding-friction.md, pain-report.md

---

## Prioritization Framework: RICE + Strategic Fit

| Feature | Reach | Impact | Confidence | Effort | RICE Score | MVP? |
|---------|-------|--------|------------|--------|------------|------|
| Wizard de onboarding 5 passos | High | High | High | Medium | 9.2 | Yes |
| Templates por caso de uso (5 templates) | High | High | High | Low | 9.0 | Yes |
| Bulk import membros (Slack/Google) | Medium | High | High | Medium | 7.5 | Yes |
| Bulk edit permissões | Medium | Medium | High | Low | 6.8 | Yes |
| Sinalização clara de features pagas | High | Medium | Medium | Low | 6.5 | Yes |
| Integração GitHub (PRs no board) | Medium | Medium | Medium | High | 4.2 | No — Phase 2 |
| App mobile onboarding | Low | Medium | Low | High | 2.1 | No — Phase 3 |
| API stability + docs update | Low | High | High | High | 3.8 | No — Parallel track |

## MVP Definition

### Included (Sprint 1-3)
1. **Wizard de onboarding** — 5 passos: perfil → workspace → template → convite → primeiro projeto
   - Endereça: PP-01, PP-02, PP-07 [Source: all-painpoints-granular.md]
2. **Template gallery** — 5 templates: Sprint Dev, Kanban, Roadmap, Startup Basics, Marketing
   - Endereça: PP-04 [Source: joao-dev-analysis.md]
3. **Bulk import de membros** — via Slack OAuth e Google Workspace
   - Endereça: PP-03 [Source: maria-pm-analysis.md]
4. **Bulk edit permissões** — seleção múltipla + assign role em batch
   - Endereça: PP-06 [Source: joao-dev-analysis.md]
5. **Paywall transparency** — badges "Pro" visíveis antes de configurar
   - Endereça: PP-08 [Source: lucas-founder-analysis.md]

### Deferred
- GitHub integration → Phase 2 (alta complexidade, requer partnership)
- Mobile onboarding → Phase 3 (app rewrite necessário) [Assumption: requires validation]
- API stabilization → Track paralelo com SRE team

## Expected Impact
- **Taxa de conclusão onboarding:** potencial de melhoria substancial [AI estimation based on SaaS benchmarks]
- **Time-to-value:** redução significativa esperada — de 14 dias para patamar competitivo [AI estimation based on guided onboarding benchmarks]
- **Tickets de suporte:** redução expressiva no volume relacionado a onboarding [AI estimation based on self-service adoption rates]

## Effort Estimate
- **Design:** 1 sprint (2 semanas) [AI estimation based on feature complexity]
- **Dev:** 2 sprints (4 semanas) com equipe de 3 devs [Source: broad-context.md]
- **QA + Launch:** 1 sprint
- **Total:** ~6 semanas até production [Assumption: requires validation]

---

**Prioritization Date:** 2026-03-01
**Analyst:** Agent S9 — Prioritization Specialist
**Next:** Agent S10 — Product Brief
