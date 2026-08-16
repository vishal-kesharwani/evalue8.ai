# Google Form Copy — Round 2/3: Concept Validation & Pricing

**Do not send this yet.** This is the concept-reveal + willingness-to-pay
material originally drafted for the first survey, held back per the decision
to keep Round 1 (`ai-builders-google-form.md`) pure discovery with zero
product mentions. Use this once Round 1's pain matrix has pointed at a
specific hypothesis — router, verification, or something else that actually
showed up in Round 1's Q7/Q14/Q16 answers.

**Before using this:** rewrite the "Quick concept" reveal below to match
whichever hypothesis Round 1 actually validated. If Round 1 shows
verification pain dominates and routing barely registers, don't reveal both —
lead with verification alone, and vice versa. Sending the full bundled pitch
regardless of what Round 1 found defeats the point of running Round 1 first.

---

## Round 2 — Concept validation (send this first, no pricing)

Recruit from Round 1's Q17/Q18 (people who agreed to further contact) plus
anyone who showed strong signal in Round 1's free-text answers on the
hypothesis you're validating.

### — SECTION: Quick concept —

*(Adapt this to whichever hypothesis Round 1 pointed at — this version
assumes both, edit down to one if Round 1's data says one dominates.)*

> **A quick concept, then a few more questions:**
>
> I'm exploring a tool that automatically picks the right LLM for each task
> (so you're not overpaying with an expensive model on simple stuff, or
> underpowering something that needed more capability) — and separately,
> checks the AI's output against real sources before it reaches a user, to
> surface evidence supporting (or contradicting) the answer before it ships.
>
> In short: **the right model, every time — with a clear record of why, and
> evidence behind the answer.**

*(Deliberately not claiming "proof it's correct" — source-checking provides
evidence, not a correctness guarantee, and overclaiming here would undermine
credibility with a technical audience.)*

### — SECTION: Reaction —

**Q5. Would this address the problem(s) you described in the earlier survey / your own workflow?**
*Type: Multiple choice*
- Yes, directly
- Partially
- No, not really

**Q5a. What would it need to do for you to actually adopt it — and would it replace something you already use or pay for?**
*Type: Paragraph*

*(If validating both router and verification separately, split into two
pairs of questions like this — one for each — so you can cross-tabulate
interest independently. See "Cross-tabulate" note below.)*

**Q6. [If validating both] Same question for the [other half of the concept]:**
*Type: Multiple choice*
- Yes, directly
- Partially
- No, not really

**Q6a. What would it need to do for you to actually adopt it — and would it replace something you already use or pay for?**
*Type: Paragraph*

### Cross-tabulate Q5 × Q6 if both were asked

Your concept may be two products bundled together — router and verification.
Don't average interest into one number; cross-tabulate:

- High interest in verification, low in router → verification is the real
  pain, router is a nice-to-have
- High interest in router, low in verification → the opposite; lead with
  router
- High on both → bundle is validated, build both per the roadmap sequencing
- Low on both → the concept itself needs rethinking, don't proceed to Round 3
  pricing yet

---

## Round 3 — Pricing / willingness to pay (only after Round 2 confirms the concept lands)

### — SECTION: Pricing —

**Q8. How would you prefer to pay for a tool like this?**
*Type: Multiple choice*
- Per API call / usage-based
- Per million tokens / compute usage processed
- Per developer seat
- Monthly flat SaaS subscription
- I wouldn't pay for this

**Q9. What best describes where you'd use this?**
*Type: Multiple choice*
- General AI product / dev team
- Developer tools
- Customer support
- Healthcare
- Fintech / financial services
- Legal-tech
- E-commerce
- Other (write in)

*(Q9 may already be redundant if you're recruiting Round 3 from people who
already answered Round 1's Q3 — cross-reference by email instead of
re-asking, if you tracked emails.)*

---

## Why this is split into three rounds instead of one form

Bundling concept-reveal and pricing into the same form as discovery
questions — the original draft's mistake — anchors every answer to a product
idea the respondent hasn't had a chance to react to on its own merits, and
optimizes the data for "did people say yes" rather than "what's actually
worth building." Keeping the rounds separate, and only advancing to the next
round once the previous one's data supports it, is what makes each round's
signal trustworthy on its own terms.
