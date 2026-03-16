---
name: transcribe
description: Transcribes audio/video interview recordings to markdown text. Supports local files via Whisper and cloud recordings via Otter.ai/Rev integration.
user-invocable: true
---

# Transcrever Entrevistas

Transcreve gravacoes de audio/video de entrevistas para markdown estruturado.

## Input

Arquivo de audio/video (caminho local) ou URL de gravacao cloud.
Argumento: `$ARGUMENTS` (caminho do arquivo ou URL).

## Deteccao de Metodo

Verificar na ordem:

1. **Whisper (local)** — Executar `which whisper`. Se disponivel, usar localmente (gratis, privado, sem upload).
2. **Otter.ai (cloud)** — Verificar se `OTTER_API_KEY` existe em `.env`. Se sim, usar API.
3. **Paste manual** — Se nenhum disponivel, instruir o PM a transcrever externamente e colar o conteudo.

## Fluxo — Whisper (local)

```bash
whisper "$ARGUMENTS" --model medium --language pt --output_format txt --output_dir 0-documentation/0b-Interviews/
```

Apos execucao:
1. Ler o arquivo `.txt` gerado
2. Converter para markdown com labels de speaker (se detectavel)
3. Adicionar header de metadados
4. Salvar como `0-documentation/0b-Interviews/{nome-do-arquivo}.md`

## Fluxo — Otter.ai

1. Carregar `OTTER_API_KEY` do `.env`
2. Enviar arquivo/URL via API
3. Aguardar processamento e baixar transcricao
4. Converter para markdown com speakers e timestamps
5. Salvar em `0-documentation/0b-Interviews/{nome}.md`

## Fluxo — Paste Manual

Informar ao PM:
> Nenhum metodo de transcricao automatica encontrado.
> Opcoes: (1) Instalar Whisper, (2) Configurar OTTER_API_KEY no .env, (3) Colar transcricao manualmente.

## Header de Metadados

```markdown
---
entrevista: {nome}
data: {YYYY-MM-DD}
duracao: {estimada ou extraida}
participantes: {se identificados}
metodo: whisper | otter | manual
---
```

## Pos-Transcricao

Ao finalizar, sugerir:
> Transcricao pronta! Quer analisar com /start-workflow ou explorar com /pair?

## Instalacao do Whisper

Se Whisper nao estiver instalado e o PM quiser usar:
```bash
pip install openai-whisper
# ou via brew:
brew install whisper
```

Requisitos: Python 3.8+, ffmpeg (`sudo apt install ffmpeg` ou `brew install ffmpeg`).

## Regras

- Nunca inventar conteudo de transcricao
- Preservar pausas e hesitacoes como `[pausa]`, `[inaudivel]`
- Manter citacoes originais sem edicao
- Seguir guardrails de dados do projeto
