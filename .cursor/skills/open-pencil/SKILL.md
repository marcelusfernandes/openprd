---
name: open-pencil
description: Opens the Pencil design editor in a Cursor tab. Use when the user asks to open Pencil, start a design canvas, create a visual, or work with .pen files.
---

# Open Pencil Editor

## When to Use

Activate when the user says any of:
- "open pencil", "abrir pencil", "abra o pencil"
- "open canvas", "abrir canvas"
- "start design", "criar visual"
- "work with .pen", "novo .pen"

## How It Works

The Pencil MCP `open_document` tool doesn't open a visual tab in Cursor. The workaround is to create/locate a `.pen` file and open it via the `cursor` CLI, which triggers the Pencil custom editor.

## Steps

1. **Check for existing .pen files** in the workspace using Glob (`**/*.pen`)
2. **If a .pen file exists**, open it:
   ```bash
   cursor "<path-to-file>.pen"
   ```
3. **If no .pen file exists**, create one and open it:
   ```bash
   touch "<workspace>/canvas.pen" && cursor "<workspace>/canvas.pen"
   ```
4. **Confirm** the tab opened by checking `get_editor_state` from the Pencil MCP
5. The Pencil editor is now ready — proceed with any design tasks using `batch_design`, `batch_get`, and other Pencil MCP tools

## Notes

- The `.pen` file content is encrypted and managed entirely by the Pencil extension. An empty file created with `touch` is valid — Pencil initializes it on open.
- Always use the `cursor` CLI (not `code` or `open`) to ensure it opens in the current Cursor window.
- If the user wants a specific template (Welcome, Shadcn UI, Halo, etc.), they need to select it from the Pencil sidebar manually — templates are not accessible via MCP.
