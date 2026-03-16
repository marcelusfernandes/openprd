---
name: loom
description: Extracts transcripts, captions, and metadata from Loom videos for analysis. Limited integration — no public API, uses community tools for transcript access. Best for async video content analysis.
---

# Loom — Video Transcript & Content Analysis

## Purpose
Extract and analyze Loom video content (transcripts, captions, AI summaries) to support the discovery pipeline with async video-based research data.

## Integration
- **No public API** — Loom does not offer an official REST API
- **Community MCP**: Available but relies on undocumented internal GraphQL (fragile)
- **Best approach**: Manual export or community transcript tools
- **Note**: Loom is now owned by Atlassian — public API may come in future

## Available Community Tools

### Transcript Extraction
For public/shared Loom videos:
- Extract auto-generated transcripts
- Pull captions and chapter markers
- Access AI-generated summaries (if available)

### What's NOT Available
- Programmatic video recording
- Batch video management
- Analytics/view data via API
- Private video access without auth

## Workflows

### Interview Transcript Import
When discovery interviews are recorded on Loom:
1. Get Loom video URL from user
2. Extract transcript using community tools or manual copy
3. Save to `/0-documentation/0b-Interviews/loom-{title}.md`
4. Format with speaker labels and timestamps
5. Feed into Agent 1 (research specialist) for analysis

### Async Demo Analysis
When stakeholders share Loom demos:
1. Extract transcript from demo video
2. Identify: key points, decisions made, action items
3. Generate structured summary
4. Save to project documentation

### Meeting Notes from Loom
1. Extract transcript from recorded meeting
2. Structure into: attendees, agenda items, decisions, action items
3. Cross-reference decisions with discovery outputs

## PM Query Patterns
- "Extract the transcript from this Loom video: [URL]"
- "Summarize this Loom recording"
- "Import this interview Loom as a transcript for analysis"
- "What action items were mentioned in this Loom?"

## Output Format
```
# Loom Transcript — [Video Title]
## Video Info
- URL: [loom_url]
- Duration: [duration]
- Date: [date]

## Transcript
[Timestamped transcript content]

## AI Summary
[Key points extracted]

## Action Items
[If applicable]
```

## Limitations
- No official API — integrations may break without notice
- Transcript quality depends on Loom's auto-transcription
- Private videos require manual transcript export
- No batch operations available

## Rules
- ALWAYS note source: `[Source: Loom video "{title}", {url}]`
- Mark transcript quality: `[Auto-transcribed — may contain errors]`
- NEVER claim transcript is verbatim unless manually verified
- Recommend manual review for critical research content
