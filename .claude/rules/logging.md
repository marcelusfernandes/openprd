# Logging — Regras de Registro

## Quando Logar
- Após cada construção bem-sucedida (skill, agent, rule, command)
- Após correções significativas (fix de bugs, refactors)
- Após mudanças arquiteturais

## Formato
- Arquivo: `_context/claude/logs/YYYY-MM-DD-{descricao-kebab}.md`
- Máximo 50 linhas
- Foco em: o que, por que, arquivos, decisões, próximos passos

## Não Logar
- Explorações sem resultado
- Mudanças triviais (typos, formatação)
- Informação já presente nos arquivos criados
