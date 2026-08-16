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
*Type: Multiple choice · Required*
- Building an AI product currently in production
- Building an AI feature internally
- Building/prototyping an AI product
- Planning to build one
- Just experimenting/learning
- Other

**Q2. How large is the team working on the AI product/feature?**
*Type: Multiple choice · Required*
- Just me
- 2–5
- 6–20
- 20+

**Q3. What industry/domain are you building for?**
*Type: Multiple choice · Required*
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
*Type: Paragraph · Required*
*(Description: "Which models, APIs, frameworks, databases, evaluation tools, monitoring tools, etc. do you currently use?")*
*High-value question — the gap between "OpenAI + Claude + Gemini + LangChain + RAG + custom evals" and "OpenAI API + nothing else" tells you a lot about sophistication and what's already solved.*

**Q5. How do you decide which model to use for a particular task?**
*Type: Paragraph · Required*
*Deliberately open — doesn't suggest "cost/latency/accuracy" as the framing, so you see their actual mental model instead of them reflecting your own options back at you. One of the highest-value questions in the form — this is the one to read closely, not skim.*

**Q6. Do you use one model for everything, or different models for different tasks?**
*Type: Multiple choice · Required*
- Mostly one model
- Different models for different tasks
- We experiment with multiple models but haven't standardized
- Not sure / depends

**Q6a. If you use different models, what makes you choose one over another?**
*Type: Paragraph · Optional*
*(Self-skippable by anyone who answered "mostly one model" to Q6 — no branching needed, it just won't apply to them.)*

*Navigation: continue to Section: Pain discovery*

---

## — SECTION: Pain discovery —

*(The most important section in the survey.)*

**Q7. What is the biggest challenge you currently face when building with LLMs?**
*Type: Paragraph · Required*
*No options offered — listing "cost / latency / hallucination / reliability" here would suggest the answer instead of discovering it. This is qualitative; Q8 gets you the quantitative cut on the same topic. One of the six most important questions in the form.*

**Q8. Which of these problems have you personally experienced?**
*Type: Checkboxes · Required*
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
- Other

*No "None of these" option — Google Forms checkboxes can't easily be made
mutually exclusive against the rest of the list, so a "none" option can't be
enforced as exclusive and would just be noise. Q7 already captures "nothing
notable" implicitly (a short or empty-feeling answer there), so it's not lost
information, just not duplicated here.*

**Q9. How often do problems with AI output or AI system behavior require you to intervene manually?**
*Type: Multiple choice · Required*
- Never
- Rarely
- Sometimes
- Frequently
- Almost every day

*Navigation: continue to Section: Real-world impact*

---

## — SECTION: Real-world impact —

**Q10. Have you ever had an AI-generated response cause a problem in development or production?**
*Type: Multiple choice · Required*
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
*Type: Paragraph · Required*
*(Description: "What was the issue, how was it discovered, and what did you do afterward?")*
*Deliberately doesn't say "hallucination" — let them describe it in their own words. What they call it, and what they emphasize, is itself data. Required even though it's only reached via the "Yes" branch — Google Forms allows requiring a question on a conditionally-reached section, and this is too valuable to risk losing to a skip.*

*Navigation: continue to Section: Current workaround*

---

## — SECTION: Current workaround —

*(Everyone lands here regardless of their Q10 answer — this is the gold-mine
section. Purpose is not to map competitors; purpose is to find out whether
people are already spending real time/money solving this.)*

**Q12. How do you currently prevent, detect, or fix problems with your AI system?**
*Type: Paragraph · Required*
*(Description: "For example: testing, human review, evaluation frameworks, monitoring, another AI model, prompt changes, changing models, custom rules, source checking, or doing nothing. Please describe what you actually do today.")*
*One of the six most important questions in the form.*

**Q13. What tools or services do you currently use for this?**
*Type: Checkboxes · Required*
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
*Type: Paragraph · Required*
*Possibly the single best question in the form. "We have hallucinations" is weak signal. "We have 3 engineers manually reviewing outputs every week and it still misses edge cases" is a business opportunity. This question is what surfaces the second kind of answer. One of the six most important questions in the form.*

*Navigation: continue to Section: Priorities*

---

## — SECTION: Priorities —

**Q15. Rank these based on what matters most when building/deploying AI features (1 = most important).**
*Type: Multiple choice grid · Required*
*Rows: Accuracy / Reliability / Cost / Latency / Explainability / Developer experience / Privacy-security / Scalability*
*Columns: 1–8*
*Enable: "Limit to one response per column" AND "Require a response in each row" — together these force every respondent to give a genuine 1st-priority → 8th-priority ranking rather than leaving gaps or double-ranking.*

**Q16. If you could eliminate ONE recurring problem from your AI development workflow, what would it be?**
*Type: Paragraph · Required*
*The highest-leverage single question to highlight when you read results — Q8's checkboxes let someone select everything, this forces an actual choice. One of the six most important questions in the form.*

*Navigation: continue to Section: Optional interview*

---

## — SECTION: Optional interview —

**Q17. Would you be open to a short 15-minute conversation about your experience building with AI?**
*Type: Multiple choice · Required*
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
*Type: Short answer · Optional*
*(Left optional even though Q17 was "Yes"/"Maybe" — don't force it; someone who reconsiders at this point should still be able to submit the rest of their answers.)*

*Navigation: continue to Section: Thanks*

---

## — SECTION: Thanks —

> Thanks so much for the detailed answers — this genuinely helps shape what
> gets built next.

*(Form-ending section — no further navigation needed.)*

---

## How to distribute

Don't just drop the link with "guys fill this form." The framing matters as
much as the questions — it needs to read as research, not a pitch, or you'll
bias every answer that follows.

> Hey everyone! 👋
>
> I'm doing a short 5-minute research survey to understand how developers/teams
> are actually building and shipping AI/LLM features today.
>
> This isn't a product pitch or sales survey — I'm specifically trying to
> understand real workflows, problems, and how people currently solve them.
>
> If you're actively building with LLMs, would really appreciate your input.
>
> **5 mins:** [FORM LINK]
>
> Feel free to share it with another AI builder as well.

Don't say, anywhere in the post or in replies to it:
- "We're building an AI infrastructure startup…"
- "We're solving hallucinations…"
- "Help us validate our idea…"

Any of those immediately biases responses toward confirming what you said
rather than reporting what's actually true for them.

## Target response count

- **Minimum: 30** — enough to see obvious patterns, not enough for real segmentation.
- **Good: 50–75** — segmentation (production vs. prototype, solo vs. team, by industry) starts being meaningful.
- **Strong: 100+** — solid comparisons across every cut in Q1–Q3.

100 random responses are not better than 30 from people who actually build
and ship AI features — quality of respondent matters more than raw count.
Distributing in an AI builders community (rather than a general audience) is
what makes even 30–50 responses usable.

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
  you want.

Read Q7, Q14, and Q16 (the open-ended ones) before you look at the checkbox
percentages — a specific, detailed pain description is stronger signal than a
checked box, and it's where the real segmentation (by team size, industry,
maturity) tends to become visible.

### Weak signal vs. strong signal — read every open-ended answer against this

> "We sometimes get hallucinations." — **weak.** Pain, no depth.
>
> "We have two developers manually reviewing AI-generated reports every week
> because our automated evaluation misses edge cases." — **strong.** This one
> answer contains pain, frequency, human effort, an existing (inadequate)
> workaround, and a plausible buyer, all in one sentence.

If most of your Q11/Q12/Q14 answers read like the first example, the pain is
real but shallow — keep digging via the 10–15 follow-up interviews before
committing to a hypothesis. If they read like the second, you likely have
enough to move to Round 2.

### Optional deeper scoring, once you have a shortlist of pains

Don't rely on percentages alone. For each candidate pain theme, score 0–5 on:

| Factor | Question to ask of the data |
|---|---|
| Frequency | How often does this come up (Q9, and how often it appears across Q7/Q8)? |
| Severity | How damaging is it when it happens (Q11)? |
| Manual effort | How much human work currently goes into it (Q12)? |
| Money | Is money already being spent on it (Q13 — paid tools in use)? |
| Existing solution strength | How good are the current tools/workarounds (Q13, described quality in Q12/Q14) — score this one *inverted*, since a strong existing solution works against you |
| Frustration | How frustrated are people, in their own words (Q14)? |
| Urgency | Do they talk about wanting to solve it now, or "someday" (Q14/Q16)? |

`Opportunity score = Frequency + Severity + Effort + Money + Frustration + Urgency − Existing solution strength`

The exact formula matters less than the discipline it forces: don't let a
high percentage alone (e.g. "70% mentioned hallucinations") make the decision
— check it against effort, money already spent, and how bad the current
workarounds actually are.

## The recommended funnel

1. **Round 1 (this form): discovery.** No product mentioned. Target 50+
   quality responses from the AI builders community.
2. **Analyze.** Build the pain matrix + opportunity scores above. Identify the
   top 2–3 candidate pains — not a single winner yet.
3. **10–15 follow-up interviews.** Recruit from Q17/Q18 responders plus anyone
   whose Q11/Q12/Q14 answers were strong-signal. Use
   `user-interview-guide.md` and `user-interview-tracker.xlsx`, adapted to
   probe the top 2–3 candidate pains specifically instead of the generic
   script. This is where you get the *depth* the survey alone can't.
4. **Choose ONE problem.** If the data points somewhere other than
   routing/verification, follow the data — abandoning the original idea is
   the point of doing discovery first, not a failure of it.
5. **Round 2: concept validation.** Reveal only the chosen hypothesis and
   gauge reaction — see `ai-builders-google-form-round2-concept-and-pricing.md`.
6. **Round 3: pricing / willingness to pay.** Only after Round 2 confirms the
   concept lands.

Survey tells you the problem exists. Interviews tell you how deep it goes.
The product decision needs both, not the survey alone — don't skip straight
from Round 1 percentages to a product decision.
