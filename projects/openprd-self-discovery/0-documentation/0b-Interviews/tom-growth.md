# Interview: Tom — Growth PM, Data-Driven

**Date:** 2026-03-15
**Context:** First-time OpenPRD user. Lives in BigQuery and Amplitude. Wants data-first approach: funnels before interviews. Skeptical of qualitative-only tools.
**Format:** Moderated interview during first real session with OpenPRD.
**Interviewer:** Research team

---

**Interviewer:** Tom, give us the quick version of who you are and what you were hoping to get from OpenPRD.

**Tom:** Growth PM at a B2B marketplace. ~300 employees, Series D. My world is funnels, cohort analysis, experimentation. I own activation and retention. I live in BigQuery, Amplitude, and Looker. I run about 15 experiments a quarter. My CEO has been pushing us to "get closer to the customer" and do more qualitative work, which I intellectually agree with but practically resist because qualitative feels slow, unstructured, and hard to tie back to metrics. I was hoping OpenPRD could bridge that gap — give me a structured way to go from data anomalies to customer insights without losing the quantitative rigor I care about.

**Interviewer:** You specifically wanted the data-first approach. How was that experience?

**Tom:** It's the reason I tried this tool, actually. Most discovery tools start with "upload your interviews" and I'm like, I don't HAVE interviews yet. I want to start with my funnel data, find where users are struggling, and THEN interview people about those specific moments. OpenPRD has a "Data-First Discovery" path which is exactly that — Agent Q1 scans your analytics, Agent Q2 generates hypotheses, then it builds an interview script. Conceptually, this is the most interesting workflow I've seen in any PM tool.

**Interviewer:** And in practice?

**Tom:** In practice, it was about 60% there. I connected BigQuery and Amplitude. The data scout agent pulled some event data and identified a few anomalies — a 25% drop between "search performed" and "first listing click" for new users, which I already knew about. But it also caught something I hadn't focused on: returning users have a completely different navigation pattern that bypasses our main funnel, and we're not measuring that alternate path at all. That was genuinely useful. The hypothesis generator then created 6 hypotheses, 4 of which were interesting. It suggested that the search-to-click drop might be related to result relevance for specific verticals, which aligned with some Zendesk complaints I'd seen.

**Interviewer:** Where did the 60% break down?

**Tom:** Three areas. One: the BigQuery integration is shallow. It ran basic queries — event counts, funnel steps, simple cohort breakdowns. I wanted it to run segmented analysis: break the funnel by user acquisition channel, by company size, by industry vertical. I can write those queries myself, but the whole point of this tool is that I shouldn't have to. It should understand my schema deeply enough to explore dimensions autonomously. Instead, I had to hand-hold every query.

Two: there's no experimentation awareness. I've run 40+ experiments on the activation flow. The tool doesn't know any of that. It generated hypotheses that we've ALREADY TESTED and disproven. There should be a way to feed it my experiment history so it doesn't suggest "try simplifying the search filters" when I literally A/B tested that last quarter and it had no impact. Without experiment context, 30% of its hypotheses are wasted.

Three: the interview script it generated was generic. "Tell me about your experience with search." That's a Qualitative Research 101 question. I wanted it to generate POINTED questions tied to the specific data anomaly: "I noticed you searched for X three times and didn't click any results. Walk me through what you were looking for and what you saw." It needs to be anchored in the quantitative signal, not just loosely related.

**Interviewer:** Once you hypothetically had interviews, how did you test the qualitative analysis side?

**Tom:** I cheated a bit — I had 3 interviews that our UX researcher did last month, so I threw those in. The analysis was good. But what I really wanted was the SYNTHESIS between the quant data and the qual findings. Like, "Hypothesis 2 (search relevance by vertical) was confirmed by 2 out of 3 interviewees, and Amplitude data shows the drop-off is 3x worse for users in the healthcare vertical." That connected narrative didn't happen automatically. I had to manually ask the copilot to cross-reference, and even then it was more of a "here are the data points side by side" than a true integrated analysis.

**Interviewer:** You're clearly a metrics person. Did the tool produce anything metric-oriented?

**Tom:** There's a /revenue-impact skill which tries to estimate financial impact of pain points. I ran it. It was... brave? It estimated that the search relevance issue could be costing us $2M-4M ARR in lost conversions. The methodology was visible and tagged as AI estimation, which I appreciated. But the confidence interval was too wide to be useful and the underlying assumptions were things I'd want to tune. What would be better is if it connected to my actual conversion rates and ASP data from BigQuery to build a bottoms-up impact model, not a top-down estimate. I know my conversion rates. I know my average deal size. Build the model with MY data, not with guesses.

**Interviewer:** How about the pipeline output? The reports, journey maps, etc.?

**Tom:** The pain report was well-structured. I'd give it a B+. But it's missing something critical for a growth PM: metric hooks. Every pain point should have a metric attached to it. "Pain point: search relevance" should immediately connect to "Primary metric: search-to-click rate (currently 12%, benchmark 25-35%). Secondary metric: time to first meaningful action (currently 4.2 min, target <2 min)." Without those metric connections, the pain report is just a qualitative document that I can't plug into my OKR framework or my experiment backlog.

The journey map was similarly good but metric-free. Show me the conversion rate at each step. Show me the p50 and p95 time at each step. Then overlay the qualitative pain points on top. That's the visualization I need — not a text-based journey in markdown.

**Interviewer:** If you could redesign the data-first workflow, what would it look like?

**Tom:** Stage 1: Deep automated exploration of my analytics. Not 3 queries — 30 queries. Segment by every dimension. Find the anomalies I haven't seen. Stage 2: Hypotheses ranked by estimated revenue impact, with experiment history filtered out. Stage 3: Generate interview scripts that are surgically tied to specific data anomalies, with the data points embedded in the script as interviewer notes. Stage 4: After interviews, produce a synthesis document that maps every qualitative finding to a quantitative signal, with a recommended metric to track for each one. Stage 5: Generate an experiment brief for each validated hypothesis — not a Jira story, an experiment brief with hypothesis, metric, minimum detectable effect, and suggested test design.

**Interviewer:** That's a very specific vision. Does any tool do that today?

**Tom:** No. That's why I was excited about OpenPRD — it's the only thing I've seen that even attempts the quant-to-qual loop. Amplitude has AI features but they're all within the quant world. Dovetail is all qual. Nobody bridges them. OpenPRD is the only tool I've seen that has BigQuery AND Amplitude AND interview analysis in the same system. The architecture is right. The execution needs to go 3x deeper on the data side.

**Interviewer:** Would you use it? Would you pay?

**Tom:** I'll keep experimenting with it because the data-first concept is unique. But today it's maybe 20% of what I need on the data side. I'd pay $300/month if it could do what I described — genuine quant-qual synthesis with metric hooks and experiment awareness. Right now I'd pay $50 tops, and only for the interview analysis piece, which frankly isn't my primary need. The growth PM market is underserved and OpenPRD is pointing in the right direction but hasn't arrived yet.

**Interviewer:** Compared to your current tools?

**Tom:** Amplitude's AI is better at pure analytics exploration. Statsig is better at experiment management. Dovetail is better at interview tagging UX. But none of them do the BRIDGE between quant and qual. OpenPRD is the only one attempting the bridge, and that's why it's interesting despite being rough. My dream tool takes OpenPRD's pipeline concept, gives it Amplitude's data exploration depth, adds Statsig's experiment awareness, and wraps it in a UI that isn't a terminal. That tool would be worth $1000/month to me.

**Interviewer:** Any final thoughts?

**Tom:** Two things. First: the /pair mode was surprisingly good for ad-hoc data questions. I asked it "what metrics should I track for onboarding health?" and it gave a thoughtful framework specific to our marketplace model — not generic SaaS metrics. That kind of contextual intelligence is valuable. Second: growth PMs are a specific audience with specific needs. We don't just want insights — we want testable hypotheses with measurable outcomes. If OpenPRD built a "Growth Discovery" workflow that outputs experiment briefs instead of Jira stories, you'd own a niche that nobody else is serving. I'd champion that internally in a heartbeat.

**Interviewer:** Great feedback, Tom. Thanks for your time.

**Tom:** For sure. Ping me when you ship the deeper BigQuery integration — I'll be your first beta tester.
