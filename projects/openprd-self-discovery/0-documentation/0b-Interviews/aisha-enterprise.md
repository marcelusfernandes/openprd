# Interview: Aisha — Enterprise PM, Fortune 500

**Date:** 2026-03-15
**Context:** First-time OpenPRD user. Full tool stack: Jira, Confluence, Amplitude, Salesforce, Zendesk. Needs to present findings to VP in 2 weeks. Has done discovery many times with Notion/Miro.
**Format:** Moderated interview during first real session with OpenPRD.
**Interviewer:** Research team

---

**Interviewer:** Aisha, welcome. Give us the lay of the land — your role and what you're working on.

**Aisha:** I'm a Senior Product Manager at a Fortune 500 fintech. Our team owns the merchant onboarding flow — about 15 people between product, design, and engineering. I've been doing product discovery for 8 years. Currently using Miro for affinity mapping, Notion for documentation, Dovetail for interview tagging, and our standard stack: Jira, Confluence, Amplitude, Salesforce for account data, Zendesk for support tickets. I have a VP review in 2 weeks where I need to present findings from 8 merchant interviews about onboarding friction. I'm evaluating whether OpenPRD could accelerate that timeline.

**Interviewer:** What were your initial expectations coming in?

**Aisha:** I expected something between Dovetail and a consulting engagement — AI that does the grunt work of synthesis so I can focus on the "so what." I've tried EnjoyHQ, Dovetail, Condens. They all help with organizing and tagging but the actual synthesis — connecting themes, building narratives, drawing conclusions — is still manual. If OpenPRD could genuinely automate that synthesis layer, that's a step change.

**Interviewer:** First impressions of the tool?

**Aisha:** Mixed. Positive: the ambition is right. A pipeline that goes from raw interviews to Confluence pages and Jira stories? That's the dream. I spend 40% of my time reformatting insights into stakeholder-friendly docs. If this tool eliminated even half of that, it's worth it. Negative: it's a CLI tool. I opened it and my first thought was "I can't share this with my design lead." In enterprise, everything needs to be collaborative. A repo on my laptop is a non-starter for team workflows. I need my researcher, my designer, and my engineering lead to all see the same findings in real-time.

**Interviewer:** Let's talk about the actual workflow. What did you do?

**Aisha:** I loaded my 8 interview transcripts — we record everything in Gong, so I exported the transcripts as text files. Ran /start-workflow, picked the full pipeline. The Phase 1 analysis was... impressive. I'm not going to lie, it caught thematic connections across interviews that would have taken me a full day of affinity mapping. The pain point clustering was solid — maybe 80% aligned with what I'd have done manually. The 20% that was off was mostly about granularity: it split some things that should have been one cluster, and merged others that are actually distinct in our domain context. But 80% accuracy on auto-synthesis is remarkable.

**Interviewer:** How about the journey mapping?

**Aisha:** The as-is journey map was decent as a starting point. But it doesn't come close to what I'd build in Miro. No visual layout, no sticky notes, no color coding by severity, no ability for my designer to drag things around and add her perspective. It's a markdown document. For my personal analysis, fine. For a collaborative workshop artifact? Useless. This is where the "repo as product" model really breaks down. Product discovery is inherently collaborative. You need a canvas, not a file system.

**Interviewer:** You have Jira, Confluence, Salesforce, Amplitude, Zendesk. How did the integrations feel?

**Aisha:** I set up Amplitude and it worked — pulled event data relevant to the onboarding flow. But when I tried to connect Salesforce, there was a skill for it but it felt early-stage. I wanted to pull account data for the merchants I'd interviewed — ARR, account age, segment — so I could overlay "this pain point is felt most by our enterprise merchants who represent 70% of revenue." That data enrichment didn't happen smoothly. I had to manually provide account IDs and the output was raw JSON that I then had to interpret.

The Jira integration for Phase 3 was interesting conceptually but I'd never actually use it. At our company, Jira stories go through a specific workflow with our engineering leads. I can't have an AI auto-create stories — they need to go through technical review, estimation, dependency mapping. What I'd actually want is a draft that I can review, edit, and then push to Jira myself. The current flow felt too automated for enterprise governance.

**Interviewer:** What about Confluence output?

**Aisha:** Similar story. It generated Confluence-formatted markdown which is a good start. But our Confluence has specific templates, specific page hierarchies, specific review workflows. I can't just dump a generated page into our space. I need it to match our template — we have a "Discovery Summary" template with specific sections our VP expects. The tool should let me define my output template and fill it in, not impose its own structure.

**Interviewer:** You mentioned needing to present to your VP in 2 weeks. Did OpenPRD help with that?

**Aisha:** Partially. The pain report had good content that I'll reuse. The executive summary was actually well-written — concise, clear, backed by evidence. I'll probably copy 60% of it into my VP deck. But the /export-presentation output was an HTML page. My VP needs a PowerPoint or a PDF in our brand template. I ended up spending 3 hours reformatting the content into our internal deck template. The analysis saved me time; the formatting ate some of that back.

**Interviewer:** How does the depth of analysis compare to your manual process with Miro and Dovetail?

**Aisha:** The AI analysis goes deeper and wider than I typically go manually. It catches connections I'd miss because I'm cognitively limited — after reading 8 transcripts, I'm saturated. The AI isn't. The JTBD extraction was particularly good. It found a job-to-be-done that I wouldn't have articulated: "When a merchant is migrating from a legacy system, they want to validate that their historical data transferred correctly before going live, so they can maintain trust with their customers." That's a real insight that connects to three different pain points. Manually, I might have logged those as separate issues.

But — and this is important — depth without collaboration is limited value. In my process, the Miro board IS the analysis. My researcher adds tags, my designer groups patterns differently, my eng lead flags technical constraints on sticky notes. The output of discovery isn't a document — it's shared understanding. OpenPRD produces a good document but doesn't create shared understanding.

**Interviewer:** What would need to change for OpenPRD to fit your enterprise workflow?

**Aisha:** Five things, in priority order. First: collaboration. Even if it's read-only sharing — give me a URL I can send to my team. Second: custom templates for outputs. Let me define what my Confluence page looks like, what my VP deck contains. Third: Salesforce enrichment that actually works — overlay account data automatically onto qualitative findings. Fourth: governance controls on Jira output. Draft mode, review before push, respect our workflow. Fifth: SSO and security compliance. My IT team would never approve a tool that stores customer interview data in a local git repo. We need SOC 2, data residency, access controls.

**Interviewer:** Would you pay for it?

**Aisha:** In its current form, no — not for enterprise use. It's a personal productivity tool right now, and enterprise PMs need team tools. But if it had collaboration, security compliance, and custom templates? Yes, absolutely. The analysis engine is the best I've seen. Enterprise would pay $500-1000/seat/month for this if it were packaged correctly. The value is there in the synthesis — I've just never seen an AI do thematic analysis this well across 8+ interviews. The packaging needs to catch up to the engine.

**Interviewer:** Compared to Dovetail and your current stack?

**Aisha:** Dovetail is better at: UX, collaboration, tagging workflow, team access, visual outputs. OpenPRD is better at: depth of analysis, automated synthesis, the pipeline concept, connecting problems to solutions to delivery artifacts. If Dovetail had OpenPRD's analytical engine, or if OpenPRD had Dovetail's UX, either one would dominate the market. Right now they're strong in opposite areas. I'll probably use OpenPRD privately for my own synthesis and then put the outputs into Dovetail/Miro for team collaboration. Which is absurd, but that's where we are.

**Interviewer:** Last thoughts?

**Aisha:** One more thing: the system is remarkably good at maintaining source attribution. Every claim traced back to a specific interview, with the actual quote. That's compliance-grade traceability. In regulated fintech, being able to say "this product decision was based on these specific customer inputs" is not just nice — it's sometimes required. If you lean into that traceability as a feature for regulated industries, you'd have a very compelling enterprise pitch. Right now it's buried as a quality-of-life feature when it could be a headline differentiator.

**Interviewer:** That's a great insight. Thanks Aisha.

**Aisha:** Thanks. Send me the next version — I'll test it again.
