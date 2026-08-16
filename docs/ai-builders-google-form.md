# Google Form Copy — Round 1: Discovery Survey

Paste this directly into Google Forms. Each `— SECTION: Name —` below is one
Google Forms section break. Google Forms only supports branching *between
sections* (a question's "go to section based on answer" jumps to a whole
section, it can't conditionally hide a single question within the same
section) — so the section boundaries below are placed deliberately to make
every branch actually implementable.

**This is a pure discovery survey.** The objective is *not* "would people buy
our router + verifier" — it's **"what problems do AI builders actually have,
how often, and how do they solve them today?"** The product hypothesis gets
formed *after* reading these answers, not before.

**Nothing about the product is mentioned anywhere in this form** — no router,
no verification, no model optimization, no hallucination-prevention pitch, no
pricing. If a question would nudge someone toward describing *your* idea back
to you, it's wrong for this round. That reveal + pricing content still
exists — see `ai-builders-google-form-round2-concept-and-pricing.md` — it's
just not part of this survey.

---

## Form title

**AI Builders — 5-Minute Research Survey**

## Form description

> I'm researching how developers and teams are currently building and shipping
> products with AI/LLMs.
>
> I'm interested in your actual workflow, challenges, and how you solve
> problems today.
>
> This isn't a product pitch or sales survey. There are no right or wrong
> answers.
>
> Takes ~5 minutes. Feel free to skip anything that doesn't apply.

**Settings to turn on:** "Collect email addresses" → OFF (kept optional via
the dedicated field at the end instead). "Limit to 1 response" → your call.

---

## — SECTION: Who are you —

**Q1. What best describes your current work with AI/LLMs?**
*Type: Multiple choice*
- Building an AI product currently in production
- Building an AI feature internally
- Building/prototyping an AI product
- Planning to build one
- Just experimenting/learning
- Other

**Q2. How large is the team working on the AI product/feature?**
*Type: Multiple choice*
- Just me
- 2–5
- 6–20
- 20+

**Q3. What industry/domain are you building for?**
*Type: Multiple choice*
- Developer tools
- Fintech
- Healthcare
- Legal
- E-commerce
- SaaS
- Customer support
- Education
- General AI
- Other

*Why Q1–Q3: lets you later check whether pain is concentrated in a particular segment, team size, or maturity stage — without asking anyone to self-select into "your" segment.*

*Navigation: continue to Section: How they build*

---

## — SECTION: How they build —

**Q4. What does your current AI/LLM stack look like?**
*Type: Paragraph*
*(Description: "Which models, APIs, frameworks, databases, evaluation tools, monitoring tools, etc. do you currently use?")*
*High-value question — the gap between "OpenAI + Claude + Gemini + LangChain + RAG + custom evals" and "OpenAI API + nothing else" tells you a lot about sophistication and what's already solved.*

**Q5. How do you decide which model to use for a particular task?**
*Type: Paragraph*
*Deliberately open — doesn't suggest "cost/latency/accuracy" as the framing, so you see their actual mental model instead of them reflecting your own options back at you.*

**Q6. Do you use one model for everything, or different models for different tasks?**
*Type: Multiple choice*
- Mostly one model
- Different models for different tasks
- We experiment with multiple models but haven't standardized
- Not sure / depends

**Q6a. If you use different models, what makes you choose one over another?**
*Type: Paragraph (optional)*
*(Self-skippable by anyone who answered "mostly one model" to Q6 — no branching needed, it just won't apply to them.)*

*Navigation: continue to Section: Pain discovery*

---

## — SECTION: Pain discovery —

*(The most important section in the survey.)*

**Q7. What is the biggest challenge you currently face when building with LLMs?**
*Type: Paragraph*
*No options offered — listing "cost / latency / hallucination / reliability" here would suggest the answer instead of discovering it. This is qualitative; Q8 gets you the quantitative cut on the same topic.*

**Q8. Which of these problems have you personally experienced?**
*Type: Checkboxes*
- Unexpected/inaccurate outputs
- Hallucinations
- High API/model costs
- Slow response times
- Model inconsistency
- Difficult evaluation/testing
- Difficult debugging
- Production reliability issues
- Context/token limitations
- Prompt maintenance
- Data/privacy concerns
- Monitoring/observability
- None of these
- Other

**Q9. How often do problems with AI output or AI system behavior require you to intervene manually?**
*Type: Multiple choice*
- Never
- Rarely
- Sometimes
- Frequently
- Almost every day

*Navigation: continue to Section: Real-world impact*

---

## — SECTION: Real-world impact —

**Q10. Have you ever had an AI-generated response cause a problem in development or production?**
*Type: Multiple choice*
- Yes
- No
- Not sure

*Navigation (set per answer choice):*
- *"Yes" → go to Section: What happened*
- *"No" → go to Section: Current workaround*
- *"Not sure" → go to Section: Current workaround*

---

## — SECTION: What happened —

*(Only reached if Q10 = "Yes")*

**Q11. What happened?**
*Type: Paragraph*
*(Description: "What was the issue, how was it discovered, and what did you do afterward?")*
*Deliberately doesn't say "hallucination" — let them describe it in their own words. What they call it, and what they emphasize, is itself data.*

*Navigation: continue to Section: Current workaround*

---

## — SECTION: Current workaround —

*(Everyone lands here regardless of their Q10 answer — this is the gold-mine
section. Purpose is not to map competitors; purpose is to find out whether
people are already spending real time/money solving this.)*

**Q12. How do you currently prevent, detect, or fix problems with your AI system?**
*Type: Paragraph*
*(Description: "For example: testing, human review, evaluation frameworks, monitoring, another AI model, prompt changes, changing models, custom rules, source checking, or doing nothing. Please describe what you actually do today.")*

**Q13. What tools or services do you currently use for this?**
*Type: Checkboxes*
- Custom/internal tooling
- OpenAI tools
- Anthropic tools
- Google tools
- LangSmith
- Langfuse
- Arize/Phoenix
- Weights & Biases
- Human review
- Automated tests/evals
- Monitoring/observability tools
- Nothing specific
- Other

**Q14. What is frustrating about your current approach?**
*Type: Paragraph*
*Possibly the single best question in the form. "We have hallucinations" is weak signal. "We have 3 engineers manually reviewing outputs every week and it still misses edge cases" is a business opportunity. This question is what surfaces the second kind of answer.*

*Navigation: continue to Section: Priorities*

---

## — SECTION: Priorities —

**Q15. Rank these based on what matters most when building/deploying AI features (1 = most important).**
*Type: Multiple choice grid*
*Rows: Accuracy / Reliability / Cost / Latency / Explainability / Developer experience / Privacy-security / Scalability*
*Columns: 1–8*
*Enable: "Limit to one response per column" and "Require a response in each row"*

**Q16. If you could eliminate ONE recurring problem from your AI development workflow, what would it be?**
*Type: Paragraph*
*Personally the highest-leverage single question to highlight when you read results — it forces a prioritization the checkbox list (Q8) can't.*

*Navigation: continue to Section: Optional interview*

---

## — SECTION: Optional interview —

**Q17. Would you be open to a short 15-minute conversation about your experience building with AI?**
*Type: Multiple choice*
- Yes
- Maybe
- No

*Navigation (set per answer choice):*
- *"Yes" → go to Section: Email*
- *"Maybe" → go to Section: Email*
- *"No" → go to Section: Thanks*

*Why this matters: the form gives you "AI builders say X is a problem" — an interview gives you "tell me about the last time X happened." That's where the actual product gets discovered, not from the aggregate stats alone.*

---

## — SECTION: Email —

*(Only reached if Q17 = "Yes" or "Maybe")*

**Q18. Email**
*Type: Short answer*

*Navigation: continue to Section: Thanks*

---

## — SECTION: Thanks —

> Thanks so much for the detailed answers — this genuinely helps shape what
> gets built next.

*(Form-ending section — no further navigation needed.)*

---

## How to analyze responses

Don't stop at single-question percentages ("72% said hallucinations are a
problem"). Build a pain matrix instead, one row per problem theme that shows
up across Q7/Q8/Q9/Q12/Q13/Q14:

| Pain | % experiencing (Q8) | Frequency (Q9) | Current workaround (Q12/Q13) | Manual effort | Existing tool coverage |
|---|---:|---|---|---|---|
| Bad outputs | 65% | Frequent | Human review | High | Some |
| Cost | 48% | Frequent | Model switching | Medium | Some |
| Latency | 42% | Frequent | Caching | Medium | Yes |
| Evaluation | 61% | Frequent | Custom tests | High | Some |

Four patterns fall out of a matrix like this:

- **High frequency + high pain + expensive workaround** — worth pursuing
- **High frequency + low pain** — people don't actually care, skip it
- **High pain + already well-served by existing tools** — hard to displace
- **High pain + a genuinely terrible existing workaround** — this is the one
  you want. It's the gap between "we have hallucinations" and "3 engineers
  manually review outputs weekly and still miss edge cases" — the second
  tells you there's a business opportunity, the first alone doesn't.

Read Q7, Q14, and Q16 (the open-ended ones) before you look at the checkbox
percentages — a specific, detailed pain description is stronger signal than a
checked box, and it's where the real segmentation (by team size, industry,
maturity) tends to become visible.

## The three-round plan

1. **Round 1 (this form): discovery.** No product mentioned. Answers this
   survey's own real question — what's actually painful and how much.
2. **Round 2: concept validation.** Once the pain matrix points at a specific
   hypothesis (routing, verification, or something else entirely that showed
   up in Q7/Q16), reveal *that* concept specifically and gauge reaction — see
   `ai-builders-google-form-round2-concept-and-pricing.md` for the
   already-drafted reveal copy and reaction questions (Q5/Q6-style
   "would this help" questions, still no pricing yet).
3. **Round 3: pricing / willingness to pay.** Only after Round 2 confirms the
   concept lands — the pricing questions from the earlier draft live in the
   same Round 2 file, ready to split out once you get there.

Don't skip straight to Round 3 material with Round 1 data — that's the
mistake this rewrite is specifically avoiding: asking people to validate an
idea you've already decided on, instead of letting the data pick the idea.
