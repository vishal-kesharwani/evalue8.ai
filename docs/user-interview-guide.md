# User Interview Guide — Weeks 7–8 Product Validation

**Goal:** Before investing further in Phase 3 (verification), validate three open decisions (`PROJECT.md` → Open questions):
1. **Beachhead market** — small AI dev teams vs. legal-tech vs. fintech (`PRD.md` §33)
2. **Pricing model** — usage-based vs. seat-based, and what tier structure (`PRD.md` §34)
3. **Verification domain** — which narrow domain to build first (`PRD.md` §31, §88)

**Target:** 5–10 interviews (`PRD.md` §31). Target profile: developer friends, small AI teams, AI startups, teams shipping LLM features (`PRD.md` §31).

**Format:** 20–25 min call (video preferred so you can share your screen if useful). Ask permission to take notes; recording is fine if the person consents, but don't rely on it — log answers into the tracker within an hour of each call while it's fresh.

---

## Before the call

- Confirm the person's role and whether they currently build with LLMs in production (if not, they're not the right interviewee — reschedule the ask for someone else).
- Have the tracker spreadsheet open, one row pre-filled with name/company/date.
- Do NOT pitch the product before asking questions 1–4. You want their unprompted current behavior, not a reaction to your idea.

## Opening (2 min)

> "Thanks for making time. I'm exploring a tool for routing tasks across different LLMs and catching AI errors before they ship — but I want to understand your actual experience first before I describe anything. Mind if I ask a few questions and take notes?"

## Core questions (verbatim from PRD.md §32 — ask in order)

1. **How do you currently decide which model to use for a given task?**
   - Probe if vague: "Walk me through the last time you had to pick a model for something new."
2. **Do you track why you made that model choice, or is it ad hoc?**
   - Probe: "If I asked you next month why you used GPT-4 instead of Haiku on some feature, could you tell me?"
3. **Have you ever shipped a hallucinated or incorrect AI output to a customer?**
   - If yes, go deep — this is the highest-signal question in the whole interview.
4. **What happened when that occurred?**
   - Probe: severity, who noticed (user vs. internal), whether it changed their process afterward.
5. **Would you pay for a tool that automatically selects models?**
   - Don't accept a bare "yes" — probe: "What would that need to do for you to actually switch?"
6. **Would you pay for a tool that catches AI errors before they reach customers?**
   - Same probe as above. Note if this lands harder than Q5 — that's a signal verification may matter more than routing to this segment.
7. **What matters more to you: Cost / Latency / Accuracy / Reliability / Explainability?**
   - Ask them to rank, don't just pick one. Write down the order.
8. **How would you prefer to pay: per API call / per developer / monthly SaaS subscription?**

## Follow-up questions (not in PRD, but useful — ask if time allows)

- "What do you currently use for this — anything, even a spreadsheet or a Slack channel?" (reveals the real competitor: usually "nothing" or "manual judgment")
- "If this existed today, who else on your team would need to sign off before you adopted it?" (reveals sales cycle length — relevant to `PRD.md` §39 Risk 3)
- "Would you be open to being a design partner — early access in exchange for feedback?" (identifies design-partner candidates for `PRD.md` §35 Week 13+)

## Closing (2 min)

- Thank them.
- If they showed strong signal on Q3/Q4/Q6 (hallucination pain) or named legal/fintech as their domain, flag them in the tracker's "Follow up" column — they're a candidate for the verification-domain decision.
- Ask: "Anyone else you know who'd be worth talking to for this?" (referrals are the cheapest way to hit 5–10 interviews)

## After the call

1. Log answers into the tracker (`docs/user-interview-tracker.xlsx`) within the hour.
2. Update `PROJECT.md`'s open questions section with any early signal, once you have 3+ interviews to triangulate from.
3. Do not make the beachhead/pricing/domain decision after 1–2 interviews — wait for the full batch (`PRD.md` §33: "final market should be selected based on user interviews and willingness to pay").
