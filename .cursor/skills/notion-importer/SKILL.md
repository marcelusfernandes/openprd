---
name: notion-importer
description: Imports pages from Notion workspace into the project's documentation directory. Converts Notion blocks to markdown.
user-invocable: true
---

# Notion Importer

Imports Notion pages/databases into the project as markdown files.

## Step 1: Check API Key

Read `.env` and check if `NOTION_API_KEY` is set.

If NOT set, guide the user:
```
Para conectar o Notion:
1. Abra notion.so/my-integrations
2. Clique "New integration" → dê um nome (ex: "Discovery Harness")
3. Copie o "Internal Integration Secret"
4. Compartilhe as páginas desejadas com a integração (Share → Invite)
5. Cole a chave aqui que eu configuro o .env
```

Use `AskUserQuestion` to collect the key. Append `NOTION_API_KEY=<key>` to `.env`.

## Step 2: Accept Input

Use `AskUserQuestion`:
```json
AskUserQuestion({
  questions: [{
    question: "Cole a URL da página ou database ID do Notion:",
    header: "Notion Import"
  }]
})
```

Extract the page/database ID from the URL. Notion URLs follow:
- `notion.so/{workspace}/{title}-{id}` — page
- `notion.so/{workspace}/{id}?v=...` — database

The ID is the 32-char hex string (with or without dashes).

## Step 3: Fetch and Convert

Use `Bash` to call the Notion API:

```bash
curl -s "https://api.notion.com/v1/blocks/${PAGE_ID}/children?page_size=100" \
  -H "Authorization: Bearer ${NOTION_API_KEY}" \
  -H "Notion-Version: 2022-06-28" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for block in data.get('results', []):
    bt = block['type']
    if bt in ('paragraph','heading_1','heading_2','heading_3','bulleted_list_item','numbered_list_item','quote','callout','toggle'):
        rich = block[bt].get('rich_text', [])
        text = ''.join(t.get('plain_text','') for t in rich)
        prefix = {'heading_1':'# ','heading_2':'## ','heading_3':'### ','bulleted_list_item':'- ','numbered_list_item':'1. ','quote':'> ','callout':'> '}.get(bt,'')
        if text: print(f'{prefix}{text}')
        else: print()
    elif bt == 'divider': print('---')
    elif bt == 'code':
        lang = block[bt].get('language','')
        text = ''.join(t.get('plain_text','') for t in block[bt].get('rich_text',[]))
        print(f'\`\`\`{lang}\n{text}\n\`\`\`')
"
```

Also fetch page title via `https://api.notion.com/v1/pages/${PAGE_ID}` for the filename.

## Step 4: Save

Use `AskUserQuestion` to ask where to save:
```json
AskUserQuestion({
  questions: [{
    question: "Onde salvar?",
    header: "Destino",
    multiSelect: false,
    options: [
      { label: "Documentação do projeto", description: "0-documentation/0a-projectdocs/" },
      { label: "Entrevistas", description: "0-documentation/0b-Interviews/" }
    ]
  }]
})
```

Save the markdown file with a slugified title: `{destination}/{slug}.md`.

## Step 5: Confirm

Report: file path, page title, block count, and word count.
