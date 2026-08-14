# TODO.md — Single Source of Truth for Next Work

## Current Sprint — Weeks 1–2: Model Registry + Basic Routing

(`PRD.md` §35, no UI required for this sprint)

- [x] Initialize FastAPI project structure (`backend/app/main.py`)
- [x] Configure PostgreSQL connection + SQLAlchemy async engine
- [x] Set up Alembic migrations (`alembic.ini`, `migrations/`, initial `model_registry` revision — verified wiring against a live Postgres, connection reached auth stage)
- [x] Create model registry schema (`PRD.md` §25 — Model table)
- [x] Implement `ModelRegistry` service (CRUD over registered models)
- [x] Seed registry with initial models — 4 models seeded (Anthropic Haiku/Sonnet/Opus + OpenAI gpt-4o-mini) against the live containerized Postgres
- [x] Implement provider abstraction (`app/providers/`) — base + OpenAI/Anthropic/open-source clients, not yet wired into routing (routing is rule-based only until the classifier lands in Weeks 3-4)
- [x] Implement basic routing rules (complexity/domain/latency → model tier) — word-count heuristic for complexity, placeholder until real classifier
- [x] Implement `POST /api/v1/route` endpoint returning `recommended_model`, `reasoning`, `estimated_cost`
- [x] Write service-layer tests for routing rules (fixture-based) — 12 tests, all passing (`backend/tests/test_routing_rules.py`)

**Sprint complete.** Verified end-to-end against a live `docker-compose` stack: migration applied, registry seeded, `/route` correctly escalates cheap → premium tier by task length and picks the lower-latency premium model when `latency_sensitive: true`. Note: db's host port is `5433` (not the default `5432`) — a native Postgres install on this machine already owns 5432, see `DECISIONS.md`.

## Weeks 3–4: Task Classification — done

- [x] Task classifier (prompted LLM — `app/services/classifier_service.py`, Anthropic by default via `app/providers/anthropic_provider.py`)
- [x] Complexity classification (simple/moderate/complex/production_critical — `app/schemas/classification.py`)
- [x] Domain classification (general/coding/legal/financial/technical/research)
- [x] Latency classification (boolean `latency_sensitive`, classifier-inferred with caller override)
- [x] Wire classifier output into routing rules — `RoutingService` now calls the classifier first, falls back to the old word-count heuristic (explicitly flagged in `reasoning`) only if the classifier call fails; see `DECISIONS.md`

Verified: 24/24 tests passing (12 routing-rules, 5 classifier-service, 4 routing-service, plus prior), and live end-to-end against `docker-compose` — confirmed the fallback path actually engages when `ANTHROPIC_API_KEY` is empty (current `.env` state), with the reasoning field correctly flagging it.

**Not yet done:** no real `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` has been tested — the classifier's live LLM path (as opposed to the fallback path) is implemented but unverified against a real model. Add a key to `.env` and re-test when one is available.

## Weeks 5–6: Trace & Audit — done

- [x] Routing trace persistence (`PRD.md` §25 — `routing_traces` table, `app/models/routing_trace.py`; `RoutingService` records one trace per successful routing decision)
- [x] Basic analytics queries (requests by model, cost by model, cost by domain — `app/services/trace_service.py::analytics_summary`, exposed via `GET /api/v1/analytics`)
- [x] Streamlit trace dashboard (`dashboard/streamlit_app.py`) — total requests, 3 charts, filterable historical-decisions table; calls the backend's `GET /api/v1/traces` and `GET /api/v1/analytics` rather than reading Postgres directly, so the dashboard container stays simple (no DB driver/model duplication)

Verified live: migrated `routing_traces`, generated 5 varied `/route` calls, confirmed `/api/v1/analytics` and `/api/v1/traces` return correct aggregates, and loaded the dashboard in a real browser — data, charts, and the historical-decisions table all rendered correctly.

**Not built (intentionally out of scope for this sprint):** cost/time-range filters on the dashboard (only model/domain/outcome text filters — PRD §15 lists cost/time as filter dimensions but exact range-filter UX wasn't specified, deferred), and "routing patterns" / "model usage distribution" as separate metrics (redundant with requests-by-model as currently scoped). Revisit if real usage surfaces a concrete need.

## Later — Weeks 7–8: Product Validation

- [ ] 5–10 user interviews (`PRD.md` §32 questions)
- [ ] Pricing discussion
- [ ] Beachhead market decision (see open question in `PROJECT.md`)
- [ ] Verification domain decision (see open question in `PROJECT.md`)

## Later — Weeks 9–12: Verification MVP

- [ ] Claim extraction
- [ ] FAISS retrieval + trusted source ingestion for chosen domain
- [ ] Verification model (SUPPORTED/UNSUPPORTED/CONTRADICTED/UNCERTAIN)
- [ ] Confidence/risk scoring
- [ ] `POST /api/v1/verify` endpoint

## Later — Week 13+: Productionization

- [ ] React dashboard (replaces Streamlit)
- [ ] Improved analytics
- [ ] Model metadata refresh process
- [ ] Production deployment
- [ ] Design partner onboarding

---

## How to use this file

Standard AI-session prompt:

> Read `PROJECT.md`, `STACK.md`, `CONVENTIONS.md`, `DECISIONS.md`, `TODO.md`, and `PRD.md`. Understand the current architecture and constraints. Pick the highest-priority unchecked item in `TODO.md`. Before changing code, inspect the existing implementation and follow the documented conventions and architectural decisions.

Check items off as they're completed, in the same commit as the work. Move to "Current Sprint" only what's actually being worked on next — don't front-load the whole roadmap into one active section.
