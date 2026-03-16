# Interview: Diego — Solo Founder, Bootstrapped

**Date:** 2026-03-15
**Context:** First-time OpenPRD user. No analytics tools — only Zoom recordings from 5 customer calls. Wants to understand "what feature to build next." Zero PM experience.
**Format:** Moderated interview during first real session with OpenPRD.
**Interviewer:** Research team

---

**Interviewer:** Diego, tell us a bit about yourself and why you're here.

**Diego:** Yeah, so I'm a solo founder. I built a scheduling tool for freelance personal trainers — basically helps them manage clients, bookings, payments. I've been running it for about 14 months, bootstrapped, no employees. I have around 200 paying users. I've been doing customer calls every week, and I have 5 recent Zoom recordings from trainers who are paying customers. They keep asking me for stuff and I have no idea what to prioritize. A friend who works in product told me to "do discovery" and pointed me at this tool.

**Interviewer:** What's your first reaction when you looked at the OpenPRD documentation?

**Diego:** Honestly? Overwhelmed. I read the START-HERE and it mentions 15 agents, 3 phases, Jira integration, Confluence output — I don't use any of that stuff. I don't have a Jira. I don't have Confluence. I barely have a Trello board. The document says "you don't need any tools" but then there are like 70 integrations listed and it made me feel like I was bringing a knife to a gunfight. Also, all the docs are in Portuguese? I'm in Austin, Texas. I had to figure out that the interface actually works in English, but some internal docs are in Portuguese. Confusing.

**Interviewer:** Once you got past the docs, what happened?

**Diego:** I opened it in Claude Code and just typed "I have 5 customer call recordings and I need to figure out what to build next." The system asked me about my product, which was nice — conversational, not a form. I described it and it created a product context file. Cool. Then it asked about my interviews. I said I have Zoom recordings. It told me to use /transcribe to get transcripts. OK, makes sense. But when I tried /transcribe, it asked me to put the video files in a folder. My Zoom recordings are in the cloud, not downloaded. I had to go download them one by one, which took 15 minutes. Not a big deal, but I wish it could just connect to Zoom and pull them.

**Interviewer:** Did the transcription work?

**Diego:** It did. Took a while, but the transcripts came out clean. Then the system immediately started analyzing them without me asking, which was kind of cool — it pulled out pain points and organized them. But here's where I got confused. It generated like 35 "atomic pain points" and clustered them into 8 groups. For a solo founder with 200 users, that's WAY too much. I don't need an exhaustive taxonomy of problems. I need a top-3 list with "build this first, this second, this third" and a rough idea of effort. The output felt like it was designed for a PM at a big company writing a strategy doc, not for me trying to decide what to code this weekend.

**Interviewer:** Did you try /pair mode?

**Diego:** Yes! And that was actually the best part. When I said "look, I just need to know what to build next," the copilot dropped the formal analysis and just... talked to me like a smart advisor. It said things like "Your users keep mentioning group class scheduling — 4 out of 5 brought it up. But the pain around payment tracking seems more acute based on the language they used. If you could only build one thing this month, payment tracking would reduce the most friction." THAT is what I needed. Direct, opinionated, actionable. Why couldn't the whole tool be like that?

**Interviewer:** So the pipeline felt like overkill but /pair felt right?

**Diego:** Exactly. The pipeline generated a 20-page pain report. I will never read a 20-page pain report. I'm one person. I need a 1-page brief. The /pair mode, when I pushed it, gave me something close to that. But I had to actively fight the system's instinct to be comprehensive. It kept wanting to generate more documents, run more agents, create journey maps. I don't need a journey map! I need to know if I should build group scheduling or payment tracking first.

**Interviewer:** What about the output format? Was it useful?

**Diego:** The markdown files in the repo are fine for me — I'm technical, I can read markdown. But the reports are written for stakeholders I don't have. Phrases like "strategic alignment with business objectives" and "cross-functional implications." Bro, I AM the cross-function. I'm engineering, product, sales, support. The tone needs a "solo founder" mode where it speaks plainly: "Build X because your users care about it the most and it's medium effort."

**Interviewer:** If OpenPRD had a mode specifically for founders like you, what would it look like?

**Diego:** One command. Something like /decide or /what-next. I paste my call recordings or notes, and in 10 minutes I get: here are the top 3 things your users want, here's what I'd build first and why, here's a rough scope estimate, and here are 2 questions you should ask in your next calls. Done. No phases, no pipeline, no Jira stories. I don't need Jira stories — I track work with Post-it notes and a GitHub project board.

**Interviewer:** Would you pay for this?

**Diego:** In its current form? Probably not, because I'd have to also pay for Claude Code's API costs and the value-to-effort ratio for a solo founder is off. The 2 hours I spent fighting with the pipeline I could have just re-listened to my recordings. BUT — if there was a streamlined founder mode that did what I described? Yeah, I'd pay $50/month. $100 tops. The interview analysis piece genuinely surfaced things I'd missed. One user mentioned they were about to switch to a competitor because we don't support Apple Pay. I heard that in the call but didn't register how important it was. The AI caught that it was tied to a deeper trust issue about payment reliability. That insight alone was valuable.

**Interviewer:** How does this compare to how you currently make decisions?

**Diego:** Currently I just listen to calls, write messy notes in Notion, and go with my gut. OpenPRD's analysis is objectively better than my gut — it catches patterns across interviews that I miss. But the overhead is too high. It's like buying a professional kitchen when you just need a microwave. If it met me where I am — solo, scrappy, speed over completeness — it could become essential. Right now it's built for the PM at Sarah's company, not for me.

**Interviewer:** Any other feedback?

**Diego:** Three things. One: the setup assumes you know what a .env file is, what an API key is, how to clone a repo. I happen to know because I'm a developer, but if I were a non-technical founder, I'd bounce in 5 minutes. Two: the system should detect that I'm a solo operation and auto-simplify. When I told it my situation, it should have said "cool, let's skip the formal pipeline and just do a quick analysis — here's what to focus on." Instead it tried to sell me on the full workflow. Three: the language thing. If you want global founders, everything needs to be in English. Having Portuguese docs mixed in is a friction point that signals "this wasn't built for me."

**Interviewer:** Thanks Diego, really valuable perspective.

**Diego:** Sure thing. Like I said, the core insight is there — the AI analysis is legit. Just package it for people like me.
