<!-- EXEMPLO: Este é um output fictício para demonstração. -->

# Pain Point Analysis: Fricção no Onboarding

## Introduction
- **Context:** Cluster agrupa dores relacionadas à experiência de primeiro uso da plataforma
- **Cluster Type:** UX-led
- **Relationship:** Todos compartilham causa-raiz — ausência de guia estruturado no primeiro acesso
- **Sources:** maria-pm-analysis.md, joao-dev-analysis.md, lucas-founder-analysis.md
- **Pain Point Breakdown:** 4 UX + 2 Operational + 1 Business = 7 total

## Pain Points in This Cluster

### PP-01: Ausência de orientação no primeiro acesso
**Type:** User Experience
> "Não sabia por onde começar. Tinha um monte de menu e nenhum guia."
> — Source: maria-pm-analysis.md
- **Frequency:** Every time | **Severity:** Critical

### PP-02: Configuração de workspace não-intuitiva
**Type:** User Experience
> "Demorei 3 dias pra configurar o workspace."
> — Source: maria-pm-analysis.md
- **Frequency:** Every time | **Severity:** High

### PP-03: Convite de equipe manual
**Type:** Operational
> "Tive que mandar convite um por um."
> — Source: maria-pm-analysis.md
- **Frequency:** Every time | **Severity:** High

### PP-04: Falta de templates pré-configurados
**Type:** User Experience
> "Tive que montar tudo do zero. Nenhum template de sprint ou roadmap."
> — Source: joao-dev-analysis.md
- **Frequency:** Often | **Severity:** Medium

## Cluster Analysis

### Severity Distribution
- **Critical:** 1 | **High:** 2 | **Medium:** 4

### Multi-Dimensional Impact
**UX Impact:** Confusão, frustração e abandono nos primeiros 30 minutos
**Operational Impact:** 3-14 dias de atraso até primeiro valor [Source: maria-pm-analysis.md]
**Business Impact:** Taxa de conclusão de onboarding em 34% [Source: broad-context.md] — potencial de melhoria substancial [AI estimation based on SaaS benchmarks]

## Mapping to Process Stages
| Estágio | Pain Points | Severity | Priority |
|---------|-------------|----------|----------|
| Primeiro acesso | PP-01 | Critical | 1 |
| Config workspace | PP-02, PP-04 | High | 2 |
| Convite equipe | PP-03 | High | 3 |

## Recommendations
- **R1:** Implementar wizard de onboarding guiado — endereça PP-01, PP-02
- **R2:** Adicionar import de membros via Slack/Google — endereça PP-03
- **R3:** Oferecer templates por caso de uso — endereça PP-04
