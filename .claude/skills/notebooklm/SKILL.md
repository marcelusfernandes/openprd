---
name: notebooklm
description: Creates research notebooks, generates audio podcasts, video overviews, slide decks, quizzes, mind maps, and infographics from discovery outputs using Google NotebookLM CLI. Transforms discovery documents into shareable multimedia content.
---

# NotebookLM — Multimedia Content Generation & Research

## Purpose
Transform discovery pipeline outputs into multimedia deliverables — audio podcasts, video overviews, slide decks, quizzes, mind maps, and infographics. Essential for PMs who need to communicate findings in diverse formats to different stakeholders.

## Integration
- **CLI**: `notebooklm` (Python package `notebooklm-py`)
- **Python SDK**: Async client `NotebookLMClient`
- **Auth**: Google OAuth via browser login
- **Install**: `pip install "notebooklm-py[browser]" && playwright install chromium`
- **Claude Code skill**: `notebooklm skill install` for natural language commands

## Setup
```bash
# Install
pip install "notebooklm-py[browser]"
playwright install chromium

# Login (one-time)
notebooklm login

# Verify
notebooklm auth check --test

# Install Claude Code skill (optional)
notebooklm skill install
```

## CLI Reference

### Notebook Management
```bash
notebooklm create "Product Discovery — Q1 2026"
notebooklm use NOTEBOOK_ID
notebooklm metadata --json
```

### Source Management
```bash
# Add discovery outputs as sources
notebooklm source add "/1-problem/1d-problem-output/pain-report.md"
notebooklm source add "/2-solution/2f-solution-output/product-brief.md"
notebooklm source add "https://docs.google.com/document/d/..."
notebooklm source add-research "competitor analysis SaaS onboarding"
```

### Content Generation
```bash
# Audio podcast (stakeholder-friendly)
notebooklm generate audio "Create a podcast discussing key findings from our product discovery" --wait

# Video overview
notebooklm generate video --style whiteboard
notebooklm generate cinematic-video "Explain the customer journey pain points" --wait

# Slide deck (for presentations)
notebooklm generate slide-deck

# Quiz (for team alignment)
notebooklm generate quiz --difficulty medium

# Flashcards (for onboarding new team members)
notebooklm generate flashcards --quantity more

# Visual artifacts
notebooklm generate infographic --orientation landscape
notebooklm generate mind-map
notebooklm generate data-table "Pain points by severity and frequency"
```

### Download & Export
```bash
notebooklm download audio ./exports/discovery-podcast.mp3
notebooklm download video ./exports/discovery-video.mp4
notebooklm download slide-deck ./exports/discovery-deck.pptx
notebooklm download quiz --format json ./exports/quiz.json
notebooklm download flashcards --format markdown ./exports/flashcards.md
notebooklm download infographic ./exports/infographic.png
notebooklm download mind-map ./exports/mindmap.json
notebooklm download data-table ./exports/data-table.csv
```

### Chat & Research
```bash
notebooklm ask "What are the top 3 pain points across all sources?"
notebooklm ask "Summarize the competitive landscape"
notebooklm ask "Generate action items from the discovery findings"
```

## Workflows

### Discovery → Podcast for Stakeholders
Perfect for busy executives who prefer audio:
1. Create notebook for the discovery cycle
2. Add key outputs: pain-report, product-brief, journey maps
3. Generate audio overview with executive framing
4. Download and share via Slack/email
```bash
notebooklm create "Discovery Podcast — Sprint 12"
notebooklm source add "1-problem/1d-problem-output/pain-report.md"
notebooklm source add "2-solution/2f-solution-output/product-brief.md"
notebooklm generate audio "Executive summary of product discovery findings, focusing on business impact and recommended next steps" --wait
notebooklm download audio ./exports/discovery-podcast.mp3
```

### Discovery → Presentation Deck
For sprint reviews or leadership presentations:
1. Add solution outputs as sources
2. Generate slide deck
3. Download as PPTX for customization
```bash
notebooklm source add "2-solution/2d-prioritization/mvp-scope.md"
notebooklm source add "2-solution/2e-roadmap/success-metrics.md"
notebooklm generate slide-deck
notebooklm download slide-deck ./exports/discovery-deck.pptx
```

### Discovery → Team Knowledge Base
For onboarding or team alignment:
1. Add all discovery outputs
2. Generate quizzes and flashcards
3. Export for team distribution
```bash
notebooklm source add "1-problem/1b-painpoints/painpoint-mapping.md"
notebooklm source add "1-problem/1b-painpoints/1b2-jtbd/jtbd-mapping.md"
notebooklm generate quiz --difficulty medium
notebooklm generate flashcards --quantity more
notebooklm download quiz --format markdown ./exports/discovery-quiz.md
notebooklm download flashcards --format markdown ./exports/discovery-flashcards.md
```

### Discovery → Visual Summary
For design reviews or workshop materials:
1. Add journey maps and pain reports
2. Generate mind maps and infographics
3. Use in Miro/Figma workshops
```bash
notebooklm source add "1-problem/1c-asis-journey/asis-journey.md"
notebooklm generate mind-map
notebooklm generate infographic --orientation landscape
notebooklm download mind-map ./exports/journey-mindmap.json
notebooklm download infographic ./exports/journey-infographic.png
```

### Research Augmentation
Use NotebookLM's research agent to supplement discovery:
```bash
notebooklm source add-research "user onboarding best practices SaaS 2026"
notebooklm source add-research "competitive analysis [industry] market trends"
notebooklm ask "Based on all sources, what are the industry benchmarks for our key pain points?"
```

## Python SDK (for automation)
```python
from notebooklm import NotebookLMClient

async with await NotebookLMClient.from_storage() as client:
    # Create notebook with discovery sources
    nb = await client.notebooks.create("Discovery Q1")
    await client.sources.add_file(nb.id, "pain-report.md", wait=True)

    # Generate multiple formats
    audio = await client.artifacts.generate_audio(nb.id, instructions="Executive summary")
    await client.artifacts.wait_for_completion(nb.id, audio.task_id)
    await client.artifacts.download_audio(nb.id, "podcast.mp3")

    # Chat for insights
    result = await client.chat.ask(nb.id, "Top 3 actionable recommendations")
```

## PM Query Patterns
- "Create a podcast from our discovery findings"
- "Generate a slide deck from the product brief"
- "Make flashcards from the JTBD mapping for team onboarding"
- "Create a mind map of our pain point clusters"
- "Generate a quiz to test team alignment on discovery insights"
- "Research competitor onboarding flows and add to our notebook"

## Output Formats
| Artifact | Formats | Best For |
|----------|---------|----------|
| Audio | MP3, MP4 | Exec stakeholders, async updates |
| Video | MP4 (whiteboard, cinematic) | All-hands, demos |
| Slides | PPTX, PDF | Sprint reviews, leadership |
| Quiz | JSON, Markdown, HTML | Team alignment checks |
| Flashcards | JSON, Markdown, HTML | Onboarding, training |
| Infographic | PNG | Workshop materials, social |
| Mind Map | JSON | Design reviews, brainstorming |
| Data Table | CSV | Analysis, spreadsheets |

## Rules
- ALWAYS cite source documents in generated content instructions
- Tag generated content: `[Generated by: NotebookLM from discovery outputs]`
- Review generated audio/video before sharing — verify accuracy
- Use specific instructions for better output quality
- Keep notebooks organized: one per discovery cycle
- Export structured formats (JSON) for integration with other tools
