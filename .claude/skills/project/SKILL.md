---
name: project
description: Multi-project workspace manager. Create, switch, list, archive, and manage discovery projects. Each project has isolated workspace dirs connected via symlinks so all skills work unchanged.
user-invocable: true
---

# Project Manager — Gerenciamento Multi-Projeto

## Propósito

Permitir que PMs trabalhem em múltiplos projetos de discovery sem misturar dados. Cada projeto tem seu próprio workspace isolado, e trocar entre eles é instantâneo.

## Como Funciona

Projetos vivem em `projects/{slug}/` com a estrutura completa de discovery dentro. Os diretórios na raiz (`0-documentation/`, `1-problem/`, `2-solution/`, `3-delivery/`) são **symlinks** que apontam para o projeto ativo. Isso significa que **todas as skills e agents funcionam sem nenhuma alteração** — eles continuam usando os mesmos paths de sempre.

```
projects/
  projeto-alpha/          ← projeto real
    0-documentation/
    1-problem/
    2-solution/
    3-delivery/
    project.md            ← metadata
  projeto-beta/           ← outro projeto
    ...

0-documentation/ → projects/projeto-alpha/0-documentation/  ← symlink
1-problem/       → projects/projeto-alpha/1-problem/         ← symlink
2-solution/      → projects/projeto-alpha/2-solution/        ← symlink
3-delivery/      → projects/projeto-alpha/3-delivery/        ← symlink
```

## Ferramenta

Script Python em `_tools/project.py`. Sem dependências externas.

## Comandos

### Criar projeto
```bash
python3 _tools/project.py create "Nome do Projeto" --group "Squad Checkout" --description "Breve descrição"
```
- Cria estrutura completa de diretórios
- Gera `project.md` com metadata e `broad-context.md` template
- `--group` opcional — agrupa projetos por squad/área
- Ativa automaticamente (atualiza symlinks)
- Se já existem diretórios reais na raiz, move o conteúdo para o projeto

### Listar projetos
```bash
python3 _tools/project.py list
```
- Mostra ativos e arquivados, agrupados por squad
- Indica qual é o projeto atual e quantos links tem

### Trocar projeto
```bash
python3 _tools/project.py switch "nome-ou-slug"
```
- Atualiza symlinks instantaneamente
- Aceita nome parcial ("alpha" encontra "Projeto Alpha")

### Status do projeto atual
```bash
python3 _tools/project.py status
```
- Mostra metadata, grupo, links e progresso por fase

### Grupo — ver projetos de uma squad
```bash
python3 _tools/project.py group "Squad Checkout"
```
- Lista projetos do grupo com tabela de progresso comparado

### Link — relacionar projetos
```bash
python3 _tools/project.py link "cupons" "cart-list" --note "Ambos afetam fluxo de checkout"
```
- Cria link bidirecional entre projetos
- Nota opcional explica a relação
- Aparece no `status` e no `list`

### Links — ver relações
```bash
python3 _tools/project.py links              # todos com links
python3 _tools/project.py links "cupons"     # links de um projeto
```

### Cross-reference — cruzar dados entre projetos
```bash
python3 _tools/project.py cross-ref "Squad Checkout"          # por grupo
python3 _tools/project.py cross-ref "cupons" "cart-list"      # por nome
```
- Gera relatório em `projects/_cross-references/`
- Compara pain points, JTBDs, jornadas, oportunidades lado a lado
- Peça ao Claude "analise o cross-ref" para insights cruzados automaticamente

### Arquivar projeto
```bash
python3 _tools/project.py archive "nome"
```
- Marca como arquivado (dados preservados)

### Deletar projeto
```bash
python3 _tools/project.py delete "nome" --confirm
```
- Remove permanentemente (requer --confirm)

### Renomear projeto
```bash
python3 _tools/project.py rename "nome-atual" "Novo Nome"
```

## Fluxo para o PM

### Primeiro uso
Quando o PM roda `/project` pela primeira vez ou `/setup`:

```
Parece que você ainda não tem nenhum projeto configurado!
Vamos criar o primeiro?

Como quer chamar esse projeto de discovery?
E você faz parte de alguma squad ou área? (opcional)
```

PM responde: "Cupons, sou da squad de checkout"

```
✓ Projeto "Cupons" criado! (Squad Checkout)

Tudo pronto — pode começar a jogar entrevistas em
0-documentation/0b-Interviews/ e rodar /start-workflow
quando quiser!
```

### Projetos da mesma squad
```
PM: "cria um projeto Cart List, também da squad checkout"

✓ Projeto "Cart List" criado! (Squad Checkout)

Quer linkar com o projeto "Cupons"? Os dois são da mesma squad.
```

PM: "sim, os dois mexem no fluxo de checkout"

```
✓ Projetos linkados: Cupons ↔ Cart List
  Nota: Ambos afetam fluxo de checkout
```

### Listar projetos
```
PM: "quais projetos eu tenho?"

PROJETOS ATIVOS
──────────────────────────────────────
  [Squad Checkout]
  ● Cupons — sistema de descontos [2026-03-13] [1 links] ◀ atual
  ○ Cart List — redesign carrinho [2026-03-13] [1 links]

  [Sem grupo]
  ○ Dashboard Analytics — nova versão [2026-03-05]

Total: 3 ativos, 0 arquivados
```

### Cruzar dados entre projetos
```
PM: "quero comparar os pain points dos projetos de checkout"

✓ Cross-reference gerado!
  Projetos: Cupons, Cart List
  Arquivo: projects/_cross-references/2026-03-13-cupons-cart-list.md

Analisando o relatório...

Padrões encontrados entre os dois projetos:
- 3 pain points em comum: [...]
- JTBDs complementares: [...]
- Oportunidade de solução unificada: [...]
```

### Ver progresso da squad
```
PM: "como tá o andamento da squad checkout?"

GRUPO: Squad Checkout
  ● Cupons — descontos [2026-03-13] ◀ atual
  ○ Cart List — carrinho [2026-03-13]

PROGRESSO COMPARADO
  Projeto                   Docs  Problema  Solução  Entrega
  Cupons                       3        12        8        0
  Cart List                    2         5        0        0
```

## Integração com /setup

O wizard `/setup` deve verificar se existe um projeto ativo. Se não:
1. Perguntar o nome do primeiro projeto
2. Criar via `python _tools/project.py create "Nome"`
3. Continuar com o setup de ferramentas

## Integração com /start-workflow

O workflow deve verificar se existe um projeto ativo antes de iniciar.
Se não houver, pedir para criar um via `/project`.

## Regras

- NUNCA rodar workflow sem projeto ativo — vai gerar arquivos soltos
- Credentials (.env, MCP configs) são COMPARTILHADAS entre projetos
- Cada projeto é isolado — dados de um não vazam para outro
- Symlinks são relativos (portabilidade entre máquinas)
- Ao criar o primeiro projeto, migrar dados existentes das pastas raiz
- O registry (`projects/registry.json`) é a fonte de verdade
- Mostrar progresso por fase ao trocar de projeto (ajuda o PM a lembrar onde parou)
- Ao criar projeto na mesma squad, sugerir link com projetos existentes do grupo
- Cross-ref gera relatório estático — peça ao Claude analisar para insights
- Links são bidirecionais — linkar A↔B automaticamente cria nos dois

## Dominios e Iniciativas

### Criar dominio
PM diz "cria um dominio pra Checkout" ou "novo dominio Growth":
```bash
python3 _tools/project.py domain create "Checkout" --owner "Squad Checkout" --description "Fluxo de compra"
```

### Listar dominios
```bash
python3 _tools/project.py domain list
```

### Criar iniciativa
PM diz "abre uma investigacao sobre timeout na API" ou "novo discovery de cupom no Checkout":
```bash
python3 _tools/project.py initiative create "Add Cupom" --domain checkout --size quick
python3 _tools/project.py initiative create "Investigar Timeout" --domain checkout --size investigation
```

Tamanhos:
- `investigation` — so /pair + notas. Sem pipeline.
- `quick` — Pain Point Brief, Founder Fast Track. Pipeline simplificado.
- `full` — Pipeline completo de discovery.

### Trocar entre iniciativas
```bash
python3 _tools/project.py switch checkout/add-cupom
```

### Harvest — salvar aprendizados no dominio
```bash
python3 _tools/project.py harvest
```
Extrai learnings da iniciativa ativa e salva no `_knowledge/` do dominio.

### Heranca de contexto
Toda iniciativa herda automaticamente o contexto do dominio (`_context/`). Isso inclui:
- Conhecimento acumulado do dominio
- Pain points de iniciativas anteriores
- Baseline de metricas
