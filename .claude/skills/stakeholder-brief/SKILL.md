---
name: stakeholder-brief
description: Adapts discovery outputs for different stakeholder audiences (C-level, Engineering, Design, Sales). Generates tailored briefs with appropriate depth, language, and talking points.
---

# Stakeholder Brief Generator

## Purpose
Transform any discovery output into audience-appropriate communications. PMs spend significant time adapting the same information for different stakeholders — this skill automates that translation.

## Inputs
- Any output file(s) from the discovery pipeline (1-problem/, 2-solution/, 3-delivery/)
- Target audience — use AskUserQuestion if not specified:

```json
AskUserQuestion({
  questions: [{
    question: "Para qual audiência você quer gerar o brief?",
    header: "Audiência",
    multiSelect: true,
    options: [
      { label: "Executivos (C-level)", description: "Foco em impacto de negócio, ROI, decisão estratégica" },
      { label: "Engenharia", description: "Escopo técnico, arquitetura, complexidade, dependências" },
      { label: "Design", description: "Experiência do usuário, pain points, jornada, oportunidades" },
      { label: "Comercial / Vendas", description: "Proposta de valor, diferenciação, argumentos de venda" }
    ]
  }]
})
```

## Audiences & Templates

### Executive Brief (C-level / VP)
**Focus**: Business impact, strategic alignment, ROI
**Length**: 1 page max
**Structure**:
- Problem in 2 sentences (business impact with numbers)
- Proposed solution in 3 sentences
- Expected outcomes (revenue, retention, efficiency)
- Investment needed (team, time, cost range)
- Key risks and mitigations
- Decision needed / ask

**Tone**: Confident, data-driven, no jargon, focus on outcomes

### Technical Brief (Engineering / Architecture)
**Focus**: Implementation scope, technical constraints, dependencies
**Length**: 2-3 pages
**Structure**:
- Problem context (user behavior patterns)
- Proposed solution architecture (high-level)
- Scope: what's in MVP vs. future
- Technical constraints and dependencies
- API/data requirements
- Estimated complexity per component
- Open technical questions

**Tone**: Precise, technical vocabulary OK, focus on scope and constraints

### Design Brief (Product Design / UX)
**Focus**: User needs, journey pain points, experience goals
**Length**: 2 pages
**Structure**:
- User personas and contexts
- Current experience pain points (with quotes if available)
- Target experience description
- Key user flows to design
- Success criteria from user perspective
- Constraints (technical, business, accessibility)
- Inspiration / competitive references

**Tone**: Empathetic, user-centered, visual thinking

### Commercial Brief (Sales / CS / Marketing)
**Focus**: Value proposition, competitive positioning, customer impact
**Length**: 1-2 pages
**Structure**:
- Customer problem (in their language)
- What we're building and why
- Value proposition by segment
- Competitive differentiation
- Expected timeline
- Talking points for customer conversations
- FAQ (anticipated objections)

**Tone**: Customer-facing language, benefit-driven, no internal jargon

## Workflow

### Step 1: Analyze Source Material
1. Read provided output file(s)
2. Extract key facts, data points, quotes, and decisions
3. Identify which information maps to which audience

### Step 2: Generate Briefs
For each requested audience:
1. Filter and prioritize information for that audience
2. Adapt language and depth
3. Add audience-specific framing
4. Generate talking points (3-5 bullet points for verbal presentations)
5. Generate anticipated FAQ (3-5 questions per audience)

### Step 3: Output
Save to `/2-solution/2f-solution-output/stakeholder-briefs/`:
- `executive-brief.md`
- `technical-brief.md`
- `design-brief.md`
- `commercial-brief.md`

Or single file if only one audience requested.

## Rules
- ALWAYS maintain data integrity from source — never add claims not in the original
- Tag any inferences: `[Inferred from: source-file.md]`
- Keep executive briefs to 1 page equivalent (< 500 words)
- Include `[Source: filename.md]` for all factual claims
- Never use internal/technical language in commercial briefs
