<!-- EXEMPLO: Este é um output fictício para demonstração. -->

# Product Brief — Onboarding Redesign NovaTech SaaS

**Agent:** S10 — Communication Specialist
**Status:** Ready for stakeholder review
**Date:** 2026-03-05

---

## Problema

NovaTech perde 66% dos usuários no onboarding. O time-to-value médio é 14 dias — inaceitável para um mercado onde concorrentes entregam valor no primeiro dia. O onboarding responde por 42% dos tickets de suporte. [Source: broad-context.md]

**3 entrevistas revelaram:** ausência de guia no primeiro acesso, setup manual e demorado, e falta de transparência sobre features pagas são as maiores barreiras. [Source: pain-report.md]

## Solução Proposta

**Onboarding guiado em 5 passos** com template gallery, bulk import de membros e sinalização clara de pricing.

### O que muda para o usuário
| Hoje | Depois do MVP |
|------|---------------|
| Dashboard vazio, sem orientação | Wizard guiado de 5 passos |
| Criar projeto: 3 cliques em submenu | Template pronto em 1 clique |
| Convidar time: um por um, manual | Bulk import via Slack/Google |
| Paywall surpresa após 20min de config | Badge "Pro" visível antes de configurar |
| Time-to-value: 14 dias | Meta: redução substancial [AI estimation based on guided onboarding benchmarks] |

## Escopo MVP
5 features priorizadas por RICE Score (detalhes em mvp-scope.md):
1. Wizard de onboarding (RICE 9.2)
2. Template gallery — 5 templates (RICE 9.0)
3. Bulk import membros (RICE 7.5)
4. Bulk edit permissões (RICE 6.8)
5. Paywall transparency (RICE 6.5)

## O que fica de fora (e por quê)
- **GitHub integration** — requer partnership, Phase 2
- **Mobile onboarding** — app rewrite, Phase 3
- **API stability** — track paralelo com SRE

## Métricas de Sucesso
| Métrica | Baseline | Meta |
|---------|----------|------|
| Taxa conclusão onboarding | 34% | Melhoria substancial [AI estimation] |
| Time-to-value | 14 dias | Redução significativa [AI estimation] |
| Tickets suporte (onboarding) | 42% do total | Redução expressiva [AI estimation] |
| NPS | 32 | Elevação moderada [AI estimation] |

## Timeline
- **Design:** 2 semanas | **Dev:** 4 semanas | **QA + Launch:** 2 semanas
- **Total:** ~6 semanas [Assumption: requires validation]
- **Target:** Q3 2026 [Source: broad-context.md]

## Riscos e Dependências
- Capacidade limitada: 3 devs + 1 designer [Source: broad-context.md]
- Slack/Google OAuth requer aprovação de segurança [Assumption: requires validation]
- Templates precisam de validação com usuários reais antes do launch

---

**Brief Date:** 2026-03-05
**Author:** Agent S10 — Communication Specialist
**Sources:** pain-report.md, mvp-scope.md, cluster-onboarding-friction.md, broad-context.md
