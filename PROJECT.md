# PROJECT.md — Current State

**Last updated:** 2026-08-14

## Where we are

Repo skeleton scaffolded per `PRD.md` §37. Phase 1 routing engine (Weeks 1–2 sprint) is complete and verified end-to-end against a live `docker-compose` stack.

## Current phase

**Phase 1 — Routing Engine.** Weeks 1–2, 3–4, and 5–6 all done — Phase 1 is functionally complete per `PRD.md` §41 Definition of Done (routing half; verification is Phase 3). Next up: Weeks 7–8 product validation (user interviews), which isn't a coding task — see `TODO.md`.

## What's built

- FastAPI app (`backend/app/main.py`) with `GET /health` and `POST /api/v1/route`
- SQLAlchemy async setup (`app/database.py`, `app/config.py` via pydantic-settings)
- `model_registry` table (`app/models/model_registry.py`) + Alembic migration (`migrations/versions/0001_create_model_registry.py`)
- `ModelRegistryService` (CRUD) and `RoutingService` (classify → tier → select → cost/reasoning)
- Rule-based routing logic in `app/routing/rules.py` — pure functions, no DB dependency, fully unit-tested (12 tests passing)
- Provider abstraction (`app/providers/`: `base.py`, `openai_provider.py`, `anthropic_provider.py`, `opensource_provider.py`) — not yet called by anything; will be used by the task classifier in Weeks 3–4
- Seed script (`backend/scripts/seed_models.py`) with 4 candidate models across cheap/standard/premium tiers

Verified end-to-end against a live `docker-compose` stack (2026-08-15):
- `pytest` passes (12/12)
- `app.main:app` imports cleanly, exposes `/health` and `/api/v1/route` in the OpenAPI schema
- Alembic migration applied against the containerized Postgres, creating `model_registry`
- Seed script populated 4 models (Anthropic Haiku/Sonnet/Opus + OpenAI gpt-4o-mini)
- `POST /api/v1/route` tested live: a short task routes to the cheap tier; a long, latency-sensitive financial task correctly escalates to premium tier and picks the lower-latency premium model (Sonnet over Opus)

**Environment note:** this machine already has a native Postgres install bound to port 5432, so `docker-compose.yml`'s db service is published on host port **5433** instead of the default 5432. See `DECISIONS.md`.

### Weeks 3–4 (2026-08-15)

- Real LLM-based task classifier: `app/services/classifier_service.py` (`TaskClassifierService`), prompts an `LLMProvider` (Anthropic by default) for `{complexity, domain, latency_sensitive}` as JSON, handles markdown-fenced responses
- `app/schemas/classification.py`: `Complexity` (now includes `production_critical`), `Domain` (6 values per `PRD.md` §7.2), `TaskClassification`
- `RoutingService` now classifies first, falls back to the old word-count heuristic only if the classifier call fails (missing key, network error, bad response) — always flagged explicitly in `reasoning`, never silent (see `DECISIONS.md`)
- `RouteRequest.domain` / `.latency_sensitive` are now optional caller overrides — omit them to let the classifier decide
- Verified live: with the current empty `ANTHROPIC_API_KEY`, `/route` correctly falls back and labels the response as such. The real (non-fallback) LLM classification path is implemented but **not yet tested against a live model** — needs a real API key.

### Weeks 5–6 (2026-08-15)

- `routing_traces` table (`app/models/routing_trace.py`, migration `0002`) — one row per successful routing decision, matching `PRD.md` §25's `RoutingTrace` fields
- `TraceService` (`app/services/trace_service.py`): `record()`, `list_traces()` (filterable by model/domain/outcome), `analytics_summary()` (total requests, cost/count by model, cost by domain)
- `RoutingService` now records a trace as part of every successful `route()` call; failed routing (no available model) is intentionally *not* traced — only completed decisions are, for now
- New read-only endpoints: `GET /api/v1/traces`, `GET /api/v1/analytics`
- Streamlit dashboard rebuilt to call those endpoints (not direct DB access — keeps the dashboard container free of DB drivers/model duplication). Verified live in a real browser: metrics, 3 charts, and the filterable historical-decisions table all render correctly against real seeded data

**Phase 1 (Routing Engine) is now functionally complete.**

### Weeks 7–8 prep (2026-08-15)

Interview materials ready in `docs/`: `user-interview-guide.md` (script + probes), `interview-outreach-templates.md` (recruiting messages), `user-interview-tracker.xlsx` (log + auto-computing summary — segment mix, willingness-to-pay, pricing preference, design-partner candidates). Formulas verified error-free via LibreOffice recalculation.

## What's next

Conduct the actual 5–10 interviews (needs you — see `docs/user-interview-guide.md`). Once ~5 are logged in the tracker, its Summary sheet informs the beachhead market, pricing, and verification-domain decisions (`PRD.md` §33-34). Engineering-wise, the next thing on the roadmap after that is Phase 3's verification MVP (Weeks 9–12), but per `PRD.md` §31 that shouldn't start until validation picks a domain.

Also still open: if a real Anthropic/OpenAI key becomes available, worth a quick pass to confirm the live classifier path (not just its fallback) actually works end-to-end — untested so far.

## Open questions

- Which open-source model provider to integrate first for Phase 1 (Together AI vs. Groq vs. self-hosted Llama/Mistral) — deferred until routing logic is in place, see `DECISIONS.md`.
- Beachhead market (small AI teams vs. legal-tech vs. fintech) — deferred to Week 7–8 user interviews per `PRD.md` §33.
- Verification domain (legal vs. financial) — deferred to same validation window.

## How to update this file

Update after every meaningful work session: what changed, what's now true that wasn't before, what's blocked. Keep it short — this is a status snapshot, not a changelog. Detailed history lives in git commits.
