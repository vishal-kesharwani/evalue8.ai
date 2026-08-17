# Google Form Copy — Round 1: Discovery Survey

**Status: finalized as built.** This mirrors the actual Google Form (6
sections, linear flow, no conditional branching) rather than the earlier
draft's branched structure — shortened for a guaranteed ~5-minute completion
time and a simpler respondent experience.

**This is a pure discovery survey.** The objective is *not* "would people buy
our router + verifier" — it's **"what problems do AI builders actually have,
how often, and how do they solve them today?"** The product hypothesis gets
formed *after* reading these answers, not before.

**Nothing about the product is mentioned anywhere in this form** — no router,
no verification, no model optimization, no hallucination-prevention pitch, no
pricing. That reveal + pricing content still exists — see
`ai-builders-google-form-round2-concept-and-pricing.md` — it's just not part
of this survey.

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

---

## Section 2 of 6 — About You

**Q1. What best describes your current work with AI/LLMs?** *Required*
- Building an AI product currently in production
- Building an AI feature internally
- Building/prototyping an AI product
- Planning to build one
- Just experimenting/learning
- Other

**Q2. How large is the team working on the AI product/feature?** *Required*
- Just me
- 2–5
- 6–20
- 20+

**Q3. What industry/domain are you building for?** *Required*
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

---

## Section 3 of 6 — How You Build

**Q4. What does your current AI/LLM stack look like?** *Required*
*Helper text: "Which models, APIs, frameworks, databases, evaluation/monitoring tools, etc. do you currently use?"*

**Q5. How do you decide which model to use for a particular task?** *Required*
*Helper text: "Describe what you actually do today. There are no right or wrong answers."*

**Q6. Do you use one model for everything, or different models for different tasks?** *Required*
- Mostly one model
- Different models for different tasks
- We experiment with multiple models but haven't standardized
- Not sure / depends

**Q6a. If you use different models, what makes you choose one over another?** *Optional*

---

## Section 4 of 6 — What's Painful?

**Q7. What is the biggest challenge you currently face when building with LLMs?** *Required*
*Helper text: "Please describe the problem in your own words."*

**Q8. Which of these problems have you personally experienced?** *Required (checkboxes — at least one)*
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

**Q9. How often do AI-related problems require you to intervene manually?** *Required*
- Never
- Rarely
- Sometimes
- Frequently
- Almost every day

**Q10. Have you ever had an AI-generated response cause a problem in development or production?** *Required*
- Yes
- No
- Not sure

*(No follow-up "what happened" question in this version — see the note at the top on what was traded for a shorter, linear form. Q7 and Q11 below are where narrative detail still surfaces.)*

---

## Section 5 of 6 — How You Deal With It

**Q11. How do you currently prevent, detect, or fix problems with your AI system?** *Required*
*Helper text: "For example: testing, human review, evaluation frameworks, monitoring, another AI model, prompt changes, changing models, custom rules, source checking, or doing nothing. Please describe what you actually do today."*
*This is the single most important question for gauging existing spend/effort now that the tools checklist has been cut — read it closely for named tools, team size doing the work, and cadence ("every week," "constantly," etc.).*

**Q12. What is frustrating about your current approach?** *Required*
*Helper text: "What is difficult, slow, expensive, unreliable, or annoying about how you solve these problems today?"*
*Likely the single best question in the form — "we have hallucinations" is weak signal, "3 engineers manually review outputs every week and it still misses edge cases" is a business opportunity.*

**Q13. If you could eliminate ONE recurring problem from your AI development workflow, what would it be?** *Required*
*Helper text: "Pick the one problem you'd most want gone."*

---

## Section 6 of 6 — Priorities & Optional Follow-Up

**Q14. Rank these based on what matters most when building/deploying AI features. 1 = most important, 8 = least important.** *Required*
*Rows: Accuracy / Reliability / Cost / Latency / Explainability / Developer experience / Privacy/security / Scalability*
*Columns: 1–8*
*Enable: "Limit to one response per column" AND "Require a response in each row."*

**Q15. Would you be open to a short 15-minute conversation about your experience building with AI?** *Required*
- Yes
- Maybe
- No

**Q16. Email** *Optional*
*Helper text: "Optional — only provide this if you'd like to participate in a follow-up conversation."*
*(Shown to everyone regardless of the Q15 answer, rather than conditionally — simpler to build, and low cost since it's optional either way.)*

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
up across Q7/Q8/Q9/Q11/Q12:

| Pain | % experiencing (Q8) | Frequency (Q9) | Current workaround (Q11) | Manual effort | Frustration level (Q12) |
|---|---:|---|---|---|---|
| Bad outputs | 65% | Frequent | Human review | High | High |
| Cost | 48% | Frequent | Model switching | Medium | Medium |
| Latency | 42% | Frequent | Caching | Medium | Low |
| Evaluation | 61% | Frequent | Custom tests | High | High |

*(The "Existing tool coverage" and "Money already spent" columns from the
earlier draft relied on Q13's tools checklist, which was cut — read Q11 for
named tools/services mentioned in free text instead; it's slower to tally
but the signal is still there.)*

Four patterns fall out of a matrix like this:

- **High frequency + high pain + expensive workaround** — worth pursuing
- **High frequency + low pain** — people don't actually care, skip it
- **High pain + already well-served by existing tools** — hard to displace
- **High pain + a genuinely terrible existing workaround** — this is the one
  you want.

Read Q7, Q12, and Q13 (the open-ended ones) before you look at the checkbox
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

If most of your Q7/Q11/Q12 answers read like the first example, the pain is
real but shallow — keep digging via the 10–15 follow-up interviews before
committing to a hypothesis. If they read like the second, you likely have
enough to move to Round 2.

### Optional deeper scoring, once you have a shortlist of pains

Don't rely on percentages alone. For each candidate pain theme, score 0–5 on:

| Factor | Question to ask of the data |
|---|---|
| Frequency | How often does this come up (Q9, and how often it appears across Q7/Q8)? |
| Severity | How damaging is it — infer from tone/detail in Q7 and Q12 (the incident narrative that used to be its own question is gone, so this one now leans on Q7/Q12's specifics)? |
| Manual effort | How much human work currently goes into it (Q11)? |
| Money | Is money already being spent on it — look for named paid tools/services in Q11's free text? |
| Existing solution strength | How good are the current tools/workarounds (quality described in Q11/Q12) — score this one *inverted*, since a strong existing solution works against you |
| Frustration | How frustrated are people, in their own words (Q12)? |
| Urgency | Do they talk about wanting to solve it now, or "someday" (Q12/Q13)? |

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
3. **10–15 follow-up interviews.** Recruit from Q15/Q16 responders plus anyone
   whose Q7/Q11/Q12 answers were strong-signal. Use
   `user-interview-guide.md` and `user-interview-tracker.xlsx`, adapted to
   probe the top 2–3 candidate pains specifically instead of the generic
   script — this is also where you recover the depth the cut "what happened"
   and "tools used" questions would have given you, by asking directly.
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
