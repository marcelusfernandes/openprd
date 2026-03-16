# Interview: Sarah — PM at Series B SaaS (50 employees)

**Date:** 2026-03-15
**Context:** First-time OpenPRD user. Has Amplitude and Intercom configured. Wants to run discovery on "why users churn after trial."
**Format:** Moderated interview during first real session with OpenPRD.
**Interviewer:** Research team

---

**Interviewer:** Sarah, thanks for joining. Can you give us a quick background on what you do and what brought you to try OpenPRD?

**Sarah:** Sure. I'm the PM at a Series B SaaS — we do workflow automation for mid-market ops teams. About 50 people, growing fast, but our trial-to-paid conversion is terrible. Like 8%. We have Amplitude set up pretty well, we use Intercom for support and onboarding flows, and I've done maybe 12 customer interviews in the last quarter. I heard about OpenPRD from a PM community on Slack and figured I'd give it a shot. My current process is just me in a Google Doc trying to make sense of things.

**Interviewer:** Walk me through your very first experience opening the project. What happened?

**Sarah:** OK so I cloned the repo, opened it in Claude Code, and immediately got a wall of text. The START-HERE.md was actually pretty good — clear, told me what I'd get. But when I actually started the conversation, the system asked me about my product, which was nice. I described what we do and it created a product-context file. That felt smooth. But then I wasn't sure — do I upload my interviews first? Do I run /setup? Do I just talk? There was a moment of "OK what do I actually DO now."

**Interviewer:** What did you end up doing?

**Sarah:** I ran /setup because the docs mentioned it. It asked me about my tools — I said Amplitude and Intercom. It walked me through putting API keys in an .env file. That part was... fine, but honestly a bit intimidating. I'm a PM, not a developer. I had to go to our Amplitude settings, figure out which API key, which secret — it took me like 20 minutes just for that. Intercom was similar. I wish there was an OAuth flow or something. Copy-pasting API keys feels very 2019.

**Interviewer:** Once you had tools connected, what did you try?

**Sarah:** I threw my 5 best interview transcripts into the 0-documentation/0b-Interviews/ folder. They were Google Doc exports, so .docx files. Then I said "I have 5 interviews about trial churn, can you help me find patterns?" The system immediately started analyzing them. That part was genuinely impressive — it pulled out pain points I hadn't connected before. Like, three different users mentioned confusion around our permissions model during setup, and I'd read all those interviews but never connected them as the same root issue.

**Interviewer:** What about the Amplitude integration? Did you use it?

**Sarah:** I tried /pair and mentioned I wanted to see our trial funnel data. The copilot offered to pull Amplitude data, which was great. But when it actually ran the query, it pulled a generic "funnel analysis" that wasn't quite what I needed. I wanted specifically the drop-off between "workspace created" and "first automation built" segmented by company size. I had to go back and forth three times to get the right query. It felt like I was debugging SQL through a chatbot, which is not what I signed up for. Eventually it got there, and the data was good, but the iteration loop was painful.

**Interviewer:** You ran /start-workflow after that?

**Sarah:** Yeah. I picked "Pain Point Brief" since I had interviews. It took maybe 2 hours to run through Phase 1. The output was... honestly? Way better than I expected. The pain report was structured, had citations back to specific interviews, grouped things into clusters. The journey map was solid. But here's the thing — I already had intuitions about most of these problems. What I really wanted was the "so what" — which problem should I fix FIRST? The prioritization felt weak. It said things like "substantial improvement potential" which is just filler. I wanted it to connect to my Amplitude data and say "this pain point affects the step where you lose 40% of trial users."

**Interviewer:** That connection between qualitative and quantitative — did it happen at all?

**Sarah:** Not automatically. I had to manually say "hey, can you map these pain points to the funnel data we pulled earlier?" And even then, it was me doing the connecting, not the system. The qualitative analysis was A-tier. The quantitative integration felt bolted on. Like two separate tools that happen to live in the same repo. What I want is: "Users 3, 5, and 7 all complained about permissions setup. In Amplitude, this is step 4 of the trial funnel, where 38% of users drop off. This pain point has the highest churn impact." That synthesis just didn't happen organically.

**Interviewer:** What about the Intercom integration?

**Sarah:** Honestly, I didn't even get to use it meaningfully. I asked if it could pull recent support tickets about trial issues, and it said it could, but the output was just a dump of ticket summaries. No connection to the interview pain points. No "hey, 47 tickets last month were about the same permissions issue your interviewees mentioned." That triangulation is what would make this a killer product for me.

**Interviewer:** How did the outputs compare to what you'd normally produce?

**Sarah:** The Phase 1 outputs — the pain report, the journey map — those were better than what I'd produce solo. Genuinely. It would have taken me a week to write something that polished. The fact that it cites every claim back to an interview is great for stakeholder buy-in. But Phase 2, the solutions... felt generic. "Consider simplifying the permissions model." Yeah, I know. Tell me HOW. Give me three concrete approaches with trade-offs. That's where a PM copilot should shine and it just gave me platitudes.

**Interviewer:** Let's talk about the export. You need to present to your leadership team.

**Sarah:** I ran /export-presentation and it generated an HTML file. The formatting was clean, I'll give it that. But I can't present an HTML file in a leadership meeting. I need a Google Slides deck or a PDF with our brand colors. I ended up copy-pasting sections into our company Slides template, which defeated the purpose. If it exported to Google Slides or even a clean PDF with configurable styling, that would save me 2 hours of reformatting.

**Interviewer:** Would you use OpenPRD again? Would you pay for it?

**Sarah:** I'd use it again for the interview analysis piece — that's the strongest part. But in its current form it's a "sometimes tool" not a "daily driver." For it to be my primary discovery tool, I need three things: one, the quant-qual synthesis to be automatic and deep, not just side by side. Two, better exports — Slides, Notion, something I can actually present. Three, the solution phase needs to be way more concrete and opinionated. If those three things existed, I'd pay $200/month easy. Right now, it's a nice interview analyzer that happens to have some integrations.

**Interviewer:** How does it compare to your current tools?

**Sarah:** My current stack is Google Docs, Amplitude dashboards, and my brain. OpenPRD is better for the structured analysis part — no question. But Dovetail, which I've tried, has a smoother UX for tagging and connecting quotes, even though its AI analysis is weaker. The ideal tool would have OpenPRD's analytical depth with Dovetail's UX and Notion's collaboration features. Right now OpenPRD is powerful but lonely — I can't share a link with my designer and say "look at finding #3." It's a repo on my machine.

**Interviewer:** Anything else you'd want to share?

**Sarah:** Two things. First, the whole thing being a git repo is both a strength and a weakness. As a PM who's comfortable with code, I find it kind of cool — version-controlled discovery is a great concept. But I know 90% of PMs would never clone a repo. You're going to hit a hard ceiling on adoption if the entry point is "install Claude Code and clone this repo." Second, the /pair mode is underrated. When it's working well, it genuinely feels like having a senior PM next to you asking good questions. The moment where it said "have you considered that the permissions issue might be downstream of a deeper onboarding problem?" — that was worth the whole setup time. More of that proactive thinking, less of the mechanical pipeline stuff.

**Interviewer:** Thanks Sarah, this was incredibly helpful.

**Sarah:** Happy to help. I'll keep using it — I'm curious to see where it goes.
