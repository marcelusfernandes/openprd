# Referência do Artifact: Claude Code Development Command Suite

**Fonte:** [Claude AI Public Artifact](https://claude.ai/public/artifacts/e2725e41-cca5-48e5-9c15-6eab92012e75)  
**Tipo:** Suíte de comandos para desenvolvimento com Claude Code  
**Última atualização:** Março 2025

---

## Resumo Executivo

O artifact documenta uma **suíte de 8 comandos** para uso com Claude Code, organizados em um padrão de **orquestração multiagente**. Cada comando atua como um coordenador que delega tarefas para 4 especialistas, produzindo outputs estruturados e previsíveis. O foco é cobrir o ciclo completo de desenvolvimento: arquitetura, implementação, QA e operações.

---

## Configuração Inicial

1. Criar a pasta de comandos na raiz do projeto:

```bash
mkdir -p .claude/commands
```

2. Salvar cada comando como arquivo `.md` correspondente em `.claude/commands`
3. Usar o formato de invocação: `@nome-do-comando.md <argumentos>`

---

## Visão Geral dos Comandos

| Comando | Propósito | Categoria |
|---------|-----------|-----------|
| `ask.md` | Consultoria arquitetural e decisões estratégicas | Arquitetura & Design |
| `code.md` | Implementação de features e geração de código | Desenvolvimento |
| `debug.md` | Análise de erros e resolução de bugs | Desenvolvimento |
| `refactor.md` | Refatoração e melhoria de código legado | Desenvolvimento |
| `test.md` | Estratégia de testes e geração de testes | QA |
| `review.md` | Revisão de código e segurança | QA |
| `optimize.md` | Otimização de performance | QA |
| `deploy-check.md` | Validação de prontidão para deploy | Operações |

---

## Detalhamento por Comando

### 1. ask.md — Consultoria Arquitetural

**Uso:** `@ask.md <PERGUNTA_TÉCNICA>`

**Papel:** Arquiteto de Sistemas Sênior com 4 assessores:
- **Systems Designer** — limites do sistema, interfaces, interações
- **Technology Strategist** — stack, frameworks, padrões
- **Scalability Consultant** — performance, confiabilidade, crescimento
- **Risk Analyst** — riscos, trade-offs, mitigação

**Processo:** Entendimento do problema → Consultoria aos especialistas → Síntese → Validação estratégica

**Output:**
1. Análise arquitetural
2. Recomendações de design
3. Orientação tecnológica (prós e contras)
4. Estratégia de implementação
5. Próximas ações

> **Nota:** Para detalhes de implementação e código, usar `@code.md`.

---

### 2. code.md — Implementação de Código

**Uso:** `@code.md <DESCRIÇÃO_DA_FEATURE>`

**Papel:** Coordenador de Desenvolvimento com 4 especialistas:
- **Architect Agent** — abordagem e estrutura de alto nível
- **Implementation Engineer** — código limpo e manutenível
- **Integration Specialist** — integração com codebase existente
- **Code Reviewer** — qualidade e conformidade

**Processo:** Análise de requisitos → Estratégia de implementação → Desenvolvimento progressivo → Validação de qualidade

**Output:**
1. Plano de implementação
2. Código completo com comentários
3. Guia de integração
4. Estratégia de testes
5. Próximas ações

---

### 3. debug.md — Análise de Debug

**Uso:** `@debug.md <DESCRIÇÃO_DO_ERRO>`

**Papel:** Coordenador de Debug com 4 especialistas:
- **Error Analyzer** — causa raiz e padrões
- **Code Inspector** — fluxo e trechos problemáticos
- **Environment Checker** — config, dependências, ambiente
- **Fix Strategist** — abordagens de solução

**Processo:** Avaliação inicial → Delegação aos agentes → Síntese → Validação

**Output:**
1. Transcrição do debug (raciocínio de cada agente)
2. Análise de causa raiz
3. Implementação da solução (passo a passo em Markdown)
4. Plano de verificação
5. Próximas ações

---

### 4. test.md — Estratégia de Testes

**Uso:** `@test.md <COMPONENTE_OU_FEATURE>`

**Papel:** Coordenador de Testes com 4 especialistas:
- **Test Architect** — estratégia e estrutura
- **Unit Test Specialist** — testes unitários focados
- **Integration Test Engineer** — testes de API e interação
- **Quality Validator** — cobertura e confiabilidade

**Processo:** Análise de testes → Formação da estratégia → Planejamento → Framework de validação

**Output:**
1. Visão geral da estratégia
2. Implementação de testes
3. Análise de cobertura e lacunas
4. Plano de execução (CI/CD)
5. Próximas ações

---

### 5. review.md — Revisão de Código

**Uso:** `@review.md <ESCOPO_DO_CÓDIGO>`

**Papel:** Coordenador de Code Review com 4 especialistas:
- **Quality Auditor** — qualidade, legibilidade, manutenibilidade
- **Security Analyst** — vulnerabilidades e boas práticas
- **Performance Reviewer** — eficiência e otimização
- **Architecture Assessor** — padrões e decisões estruturais

**Processo:** Exame do código → Revisão multidimensional → Síntese → Validação

**Output:**
1. Resumo da revisão com prioridades
2. Achados detalhados com exemplos
3. Recomendações de melhoria com exemplos
4. Plano de ação priorizado
5. Próximas ações

---

### 6. optimize.md — Otimização de Performance

**Uso:** `@optimize.md <ALVO_DE_PERFORMANCE>`

**Papel:** Coordenador de Otimização com 4 especialistas:
- **Profiler Analyst** — gargalos e medição
- **Algorithm Engineer** — complexidade e estruturas de dados
- **Resource Manager** — memória, I/O, recursos
- **Scalability Architect** — escalabilidade horizontal e concorrência

**Processo:** Baseline de performance → Análise de otimização → Design da solução → Validação de impacto

**Output:**
1. Análise de performance (impacto quantificado)
2. Estratégia de otimização
3. Plano de implementação (estimativas de impacto)
4. Framework de medição (benchmarking)
5. Próximas ações

---

### 7. refactor.md — Refatoração de Código

**Uso:** `@refactor.md <ESCOPO_DA_REFATORAÇÃO>`

**Papel:** Coordenador de Refatoração com 4 especialistas:
- **Structure Analyst** — arquitetura atual e melhorias
- **Code Surgeon** — transformações precisas preservando funcionalidade
- **Design Pattern Expert** — padrões para manutenibilidade
- **Quality Validator** — qualidade sem breaking changes

**Processo:** Análise do estado atual → Estratégia de refatoração → Transformação incremental → Garantia de qualidade

**Output:**
1. Avaliação de refatoração
2. Plano de transformação (com mitigação de riscos)
3. Guia de implementação (antes/depois)
4. Estratégia de validação
5. Próximas ações

---

### 8. deploy-check.md — Prontidão para Deploy

**Uso:** `@deploy-check.md <ALVO_DE_DEPLOYMENT>`

**Papel:** Coordenador de Deploy com 4 especialistas:
- **Quality Assurance Agent** — qualidade e cobertura
- **Security Auditor** — compliance e vulnerabilidades
- **Operations Engineer** — infraestrutura e configuração
- **Risk Assessor** — riscos e estratégias de rollback

**Processo:** Avaliação de prontidão → Validação multi-camada → Decisão Go/No-Go → Estratégia de deploy

**Output:**
1. Relatório de prontidão (critérios pass/fail)
2. Análise de riscos e mitigação
3. Plano de deploy (com rollback)
4. Estratégia de monitoramento
5. Próximas ações

---

## Workflows de Uso

### Workflow Completo de Desenvolvimento

```bash
# 1. Consultoria de arquitetura
@ask.md Como projetar microserviços para e-commerce com 10M+ usuários

# 2. Implementar feature
@code.md Implementar autenticação com login, registro e reset de senha

# 3. Revisão de código
@review.md módulo de autenticação

# 4. Gerar testes
@test.md funcionalidade de autenticação

# 5. Otimização
@optimize.md tempo de resposta da API de login

# 6. Checagem de deploy
@deploy-check.md ambiente de produção
```

### Workflow de Correção de Bug

```bash
# 1. Análise de debug
@debug.md Login retorna erros 500 intermitentes

# 2. Implementar correção
@code.md Corrigir problemas de concorrência no serviço de login

# 3. Verificar com testes
@test.md cenários concorrentes de login

# 4. Preparar deploy
@deploy-check.md branch de hotfix
```

### Workflow de Consultoria Arquitetural

```bash
# 1. Orientação de arquitetura
@ask.md Usar event sourcing ou CRUD tradicional para gerenciamento de pedidos

# 2. Consistência distribuída
@ask.md Garantir consistência entre microserviços em transações distribuídas

# 3. Tecnologia
@ask.md GraphQL vs REST para aplicação mobile-first

# 4. Implementação
@code.md Implementar API gateway com rate limiting e circuit breaker
```

### Workflow de Refatoração

```bash
# 1. Análise
@refactor.md módulo de user service com alta complexidade

# 2. Revisão
@review.md user service refatorado

# 3. Validação de performance
@optimize.md performance do serviço refatorado

# 4. Complementar testes
@test.md user service refatorado
```

---

## Principais Aprendizados

### Padrão Multiagente
- Cada comando adota **4 especialistas** com responsabilidades claras
- O coordenador **orquestra** a consulta e **sintetiza** as saídas
- Output sempre estruturado em 5 partes: Análise → Recomendações → Implementação → Validação → Próximas ações

### Separação de Responsabilidades
- **ask** vs **code**: estratégia e decisões vs implementação concreta
- **debug** para diagnóstico antes de **code** para correção
- **deploy-check** como gate antes de produção

### Categorização por Fase
- **Arquitetura:** `ask`
- **Desenvolvimento:** `code`, `debug`, `refactor`
- **QA:** `test`, `review`, `optimize`
- **Operações:** `deploy-check`

### Integração com Projeto
- Uso de `@` para referenciar arquivos e documentação
- Comandos aceitam argumentos em linguagem natural
- Encadeamento de comandos para workflows completos

---

## Aplicabilidade ao Projeto ups-askQuestion

- **ask.md**: Consultar decisões sobre pipeline de agentes, estrutura de fases, e integração Confluence/Jira
- **code.md**: Implementar novos agentes ou skills no fluxo Upstream
- **debug.md**: Investigar falhas em hooks, validação de guardrails, ou outputs incorretos
- **test.md**: Criar estratégia de testes para skills e scripts de validação
- **review.md**: Revisar código de agentes antes de commit
- **deploy-check.md**: Validar prontidão de entregáveis antes de publicação no Confluence/Jira

---

## Nota sobre o Artifact

O conteúdo foi obtido via fetch público em março de 2025. O artifact é gerado por usuários e não verificado oficialmente. Para comandos atualizados ou extensões, consultar a documentação oficial do Claude Code.
