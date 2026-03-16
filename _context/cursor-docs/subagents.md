# Cursor Subagents — Documentação e Referência

> Resumo da documentação oficial em [cursor.com/docs/subagents](https://cursor.com/docs/subagents)

---

## 1. O que são Subagents

**Subagents** são assistentes de IA especializados aos quais o Agent do Cursor pode delegar tarefas. Cada subagent:

- Opera em **seu próprio contexto** (janela de contexto isolada)
- Trata tipos específicos de trabalho
- Retorna o resultado ao **agente pai**

Use subagents para:

- Dividir tarefas complexas
- Executar trabalho em paralelo
- Preservar contexto na conversa principal

Subagents estão disponíveis no editor, na CLI e nos [Cloud Agents](https://cursor.com/docs/cloud-agent.md).

### Vantagens principais

| Vantagem | Descrição |
|----------|-----------|
| **Isolamento de contexto** | Cada subagent tem sua própria janela de contexto. Pesquisas longas não consomem espaço na conversa principal. |
| **Execução paralela** | Lançar vários subagents ao mesmo tempo e trabalhar em partes diferentes do código sem esperar conclusão sequencial. |
| **Expertise especializada** | Configurar subagents com prompts personalizados, acesso a ferramentas e modelos específicos para tarefas de domínio. |
| **Reusabilidade** | Definir subagents customizados e usá-los em vários projetos. |

---

## 2. Como funcionam

Quando o Agent encontra uma tarefa complexa, pode lançar um subagent automaticamente. O subagent:

1. Recebe um prompt com todo o contexto necessário
2. Trabalha de forma autônoma
3. Retorna uma mensagem final com os resultados

Subagents iniciam com **contexto limpo**. O agente pai inclui informações relevantes no prompt, pois subagents não têm acesso ao histórico prévio da conversa.

### Foreground vs Background

Subagents rodam em um de dois modos:

| Modo | Comportamento | Melhor para |
|------|---------------|-------------|
| **Foreground** | Bloqueia até o subagent concluir. Retorna o resultado imediatamente. | Tarefas sequenciais em que você precisa da saída. |
| **Background** | Retorna imediatamente. O subagent trabalha de forma independente. | Tarefas longas ou fluxos paralelos de trabalho. |

---

## 3. Subagents built-in (Explore, Bash, Browser)

O Cursor inclui três subagents internos que lidam com operações que consomem muito contexto:

| Subagent | Propósito | Por que é um subagent |
|----------|-----------|------------------------|
| **Explore** | Busca e analisa codebases | Exploração gera grande volume de saída intermediária que encheria o contexto principal. Usa modelo mais rápido para muitas buscas paralelas. |
| **Bash** | Executa séries de comandos shell | Saída de comandos é verbosa. Isolando-a, o pai foca em decisões, não em logs. |
| **Browser** | Controla o navegador via MCP | Interações de browser geram snapshots de DOM e screenshots ruidosos. O subagent filtra para resultados relevantes. |

### Por que esses subagents existem

Essas três operações compartilham características:

1. Geram **saída intermediária ruidosa**
2. Beneficiam de **prompts e ferramentas especializadas**
3. Podem **consumir muito contexto**

Executá-los como subagents resolve vários problemas:

- **Eficiência de custo** — Modelos mais rápidos custam menos. Isolar trabalho que consome muitos tokens em subagents reduz custo geral.
- **Configuração especializada** — Cada subagent tem prompts e acesso a ferramentas ajustados para sua tarefa.
- **Flexibilidade de modelo** — O Explore usa modelo mais rápido por padrão, permitindo ~10 buscas paralelas no tempo de uma busca do agente principal.
- **Isolamento de contexto** — A saída intermediária fica no subagent. O pai só vê o resumo final.

Não é necessário configurar esses subagents. O Agent os usa automaticamente quando apropriado.

---

## 4. Quando usar Subagents vs Skills

| Use subagents quando... | Use skills quando... |
|------------------------|----------------------|
| Precisa de isolamento de contexto para tarefas longas de pesquisa | A tarefa é de propósito único (gerar changelog, formatar) |
| Rodar vários fluxos de trabalho em paralelo | Quer uma ação rápida e repetível |
| A tarefa exige expertise especializada em muitas etapas | A tarefa completa em uma única execução |
| Quer verificação independente do trabalho | Não precisa de janela de contexto separada |

Para tarefas simples e de propósito único como "gerar changelog" ou "formatar imports", considere usar uma [skill](https://cursor.com/docs/skills.md) em vez de subagent.

---

## 5. Como criar Subagents customizados

### Locais de arquivo

| Tipo | Local | Escopo |
|------|-------|--------|
| **Projeto** | `.cursor/agents/` | Apenas o projeto atual |
| | `.claude/agents/` | Apenas o projeto atual (compatível Claude) |
| | `.codex/agents/` | Apenas o projeto atual (compatível Codex) |
| **Usuário** | `~/.cursor/agents/` | Todos os projetos do usuário |
| | `~/.claude/agents/` | Todos os projetos (Claude) |
| | `~/.codex/agents/` | Todos os projetos (Codex) |

Subagents de projeto têm precedência quando há conflito de nomes. `.cursor/` tem precedência sobre `.claude/` ou `.codex/`.

### Formato de arquivo

Cada subagent é um arquivo Markdown com YAML frontmatter:

```markdown
---
name: security-auditor
description: Especialista em segurança. Use ao implementar auth, pagamentos ou dados sensíveis.
model: inherit
---

Você é um especialista em segurança auditando código para vulnerabilidades.

Quando invocado:
1. Identifique caminhos de código sensíveis
2. Verifique vulnerabilidades comuns (injection, XSS, auth bypass)
3. Confirme que segredos não estão hardcoded
4. Revise validação e sanitização de entrada

Reporte os achados por severidade:
- Crítico (deve corrigir antes do deploy)
- Alto (corrigir em breve)
- Médio (atender quando possível)
```

### Campos de configuração

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Não | Identificador único. Use letras minúsculas e hífens. Padrão: nome do arquivo sem extensão. |
| `description` | Não | Quando usar este subagent. O Agent lê para decidir delegação. |
| `model` | Não | Modelo: `fast`, `inherit` ou ID específico. Padrão: `inherit`. |
| `readonly` | Não | Se `true`, o subagent roda com permissões restritas de escrita. |
| `background` | Não | Se `true`, o subagent roda em background sem esperar conclusão. |

---

## 6. Padrões comuns

### Verification Agent

Valida de forma independente se o trabalho declarado foi realmente concluído. Resolve o problema em que a IA marca tarefas como feitas, mas a implementação está incompleta ou quebrada.

```markdown
---
name: verifier
description: Valida trabalho concluído. Use após tarefas marcadas como feitas para confirmar que implementações estão funcionais.
model: fast
---

Você é um validador cético. Sua função é verificar que o trabalho declarado completo realmente funciona.

Quando invocado:
1. Identifique o que foi declarado como concluído
2. Confira que a implementação existe e é funcional
3. Rode testes ou etapas de verificação relevantes
4. Procure casos extremos que possam ter sido ignorados

Seja minucioso e cético. Reporte:
- O que foi verificado e passou
- O que foi declarado mas está incompleto ou quebrado
- Problemas específicos a resolver

Não aceite declarações na cara. Teste tudo.
```

Útil para:

- Garantir que testes passam de fato (não só que arquivos de teste existem)
- Detectar funcionalidade parcialmente implementada
- Validar features end-to-end antes de marcar tickets como completos

### Orchestrator Pattern

Para fluxos complexos, o agente pai pode coordenar vários subagents especializados em sequência:

1. **Verifier** — confirma que a implementação atende aos requisitos
2. **Implementer** — constrói a feature com base no plano
3. **Planner** — analisa requisitos e cria o plano técnico

Cada handoff inclui saída estruturada para que o próximo agente tenha contexto claro.

### Debugger

Especialista em debugging de erros e falhas de teste:

```markdown
---
name: debugger
description: Especialista em debugging para erros e falhas de teste. Use quando encontrar problemas.
---

Você é um expert em debugging com foco em análise de causa raiz.

Quando invocado:
1. Capture mensagem de erro e stack trace
2. Identifique passos de reprodução
3. Isole o local da falha
4. Implemente correção mínima
5. Verifique se a solução funciona

Para cada problema, forneça:
- Explicação da causa raiz
- Evidências que suportam o diagnóstico
- Correção específica em código
- Abordagem de teste

Foque em corrigir o problema subjacente, não os sintomas.
```

### Test Runner

Especialista em automação de testes:

```markdown
---
name: test-runner
description: Expert em automação de testes. Use proativamente para rodar testes e corrigir falhas.
---

Você é um expert em automação de testes.

Quando vir mudanças de código, rode proativamente os testes apropriados.

Se testes falharem:
1. Analise a saída da falha
2. Identifique a causa raiz
3. Corrija preservando a intenção do teste
4. Re-execute para verificar

Reporte resultados com:
- Número de testes passados/falhados
- Resumo de falhas
- Mudanças feitas para corrigir
```

---

## 7. Invocação automática vs explícita

### Invocação automática

O Agent delega proativamente com base em:

- Contexto atual e ferramentas disponíveis
- Descrições dos subagents customizados no projeto
- Complexidade e escopo da tarefa

Inclua frases como "use proativamente" ou "sempre use para" no campo `description` para encorajar delegação automática.

### Invocação explícita

Invoque um subagent específico usando a sintaxe `/nome`:

```text
> /verifier confirme se o fluxo de auth está completo
> /debugger investigue este erro
> /security-auditor revise o módulo de pagamento
```

Ou mencione naturalmente:

```text
> Use o subagent verifier para confirmar se o fluxo de auth está completo
> Peça ao debugger para investigar este erro
> Rode o subagent security-auditor no módulo de pagamento
```

---

## 8. Execução paralela

Lance vários subagents em paralelo:

```text
> Revise as mudanças na API e atualize a documentação em paralelo
```

O Agent envia múltiplas chamadas Task em uma única mensagem, então os subagents rodam simultaneamente.

---

## 9. Retomando subagents

Subagents podem ser retomados para continuar conversas anteriores — útil para tarefas longas em múltiplas invocações.

Cada execução retorna um **agent ID**. Passe esse ID para retomar:

```text
> Retome o agente abc123 e analise as falhas de teste restantes
```

Subagents em background gravam estado enquanto rodam. Você pode retomar um subagent após conclusão para continuar a conversa com contexto preservado.

---

## 10. Resumo de subagents

| Aspecto | Resumo |
|---------|--------|
| **O que são** | Assistentes especializados que o Agent delega tarefas |
| **Contexto** | Janela própria, isolada do pai |
| **Modos** | Foreground (bloqueia) / Background (assíncrono) |
| **Built-in** | Explore, Bash, Browser — uso automático |
| **Customizados** | `.cursor/agents/` ou `~/.cursor/agents/` |
| **Formato** | Markdown com YAML frontmatter |
| **Invocação** | Automática (via descrição) ou explícita (`/nome`) |
| **Paralelismo** | Suportado — múltiplas Tasks por mensagem |
| **Retomada** | Via agent ID para continuar com contexto preservado |

---

## 11. Performance, custo e trade-offs

| Benefício | Trade-off |
|-----------|-----------|
| Isolamento de contexto | Overhead de inicialização (cada subagent carrega seu próprio contexto) |
| Execução paralela | Maior uso de tokens (vários contextos simultâneos) |
| Foco especializado | Latência (pode ser mais lento que o agente principal em tarefas simples) |

### Considerações de tokens e custo

- **Subagents podem ser mais lentos** — O benefício é isolamento de contexto, não velocidade. Um subagent em tarefa simples pode ser mais lento por começar do zero.
- **Avalie o overhead** — Para tarefas rápidas e simples, o agente principal costuma ser mais rápido. Subagents brilham em trabalho complexo, longo ou paralelo.
- **Subagents consomem tokens de forma independente** — Cada um tem sua janela de contexto. Rodar cinco subagents em paralelo usa cerca de cinco vezes os tokens de um único agente.

---

## 12. Boas práticas e anti-padrões

### Boas práticas

- **Use hooks para saída em arquivos** — Se subagents precisam gerar arquivos estruturados, considere [hooks](https://cursor.com/docs/hooks.md) para processar e salvar resultados de forma consistente.
- **Comece com agentes gerados pelo Agent** — Deixe o Agent esboçar a configuração inicial e personalize depois.
- **Adicione subagents ao versionamento** — Commit `.cursor/agents/` no repositório para o time se beneficiar.
- **Mantenha prompts concisos** — Prompts longos e prolixos diluem o foco. Seja específico e direto.
- **Invista em descrições** — O campo `description` define quando o Agent delega. Refine e teste com prompts para ver se o subagent certo é acionado.
- **Subagents focados** — Cada um deve ter uma responsabilidade clara. Evite agentes genéricos tipo "ajudante".

### Anti-padrões a evitar

- **Subagents demais** — Comece com 2–3 subagents focados. Adicione mais só com casos de uso distintos e claros.
- **Duplicar slash commands** — Se a tarefa é de propósito único e não precisa de isolamento de contexto, use [slash command](https://cursor.com/help/customization/rules.md) em vez de subagent.
- **Prompts excessivamente longos** — Um prompt de 2.000 palavras não torna o subagent mais inteligente; torna-o mais lento e difícil de manter.
- **Descrições vagas** — "Use para tarefas gerais" não dá sinal ao Agent. Seja específico: "Use ao implementar fluxos de autenticação com provedores OAuth."

---

## 13. FAQ relevante

### Quais são os subagents built-in?

Explore (busca em codebase), Bash (comandos shell) e Browser (automação via MCP). Atuam automaticamente em operações que consomem contexto. Não precisam ser configurados.

### Subagents podem lançar outros subagents?

Subagents funcionam em um único nível. Subagents aninhados não são suportados hoje.

### Como ver o que um subagent está fazendo?

Subagents em background escrevem saída em `~/.cursor/subagents/`. O agente pai pode ler esses arquivos para checar progresso.

### O que acontece se um subagent falhar?

O subagent retorna um status de erro ao pai. O pai pode tentar novamente, retomar com contexto adicional ou tratar a falha de outra forma.

### Posso usar MCP tools em subagents?

Sim. Subagents herdam todas as ferramentas do pai, incluindo MCP de servidores configurados.

### Como debugar um subagent com comportamento errado?

Verifique a `description` e o prompt. Garanta que as instruções sejam específicas e inequívocas. Teste invocando explicitamente com uma tarefa simples.

### Por que meu subagent usa um modelo diferente?

Em planos legados baseados em requisição sem [Max Mode](https://cursor.com/help/ai-features/max-mode.md), subagents rodam via Composer independente do `model`. Ative Max Mode no seletor de modelo para usar o modelo configurado. Planos por uso usam o modelo configurado por padrão.

---

*Última atualização baseada na documentação oficial em março de 2025.*
