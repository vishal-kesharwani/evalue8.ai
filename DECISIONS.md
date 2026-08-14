# DECISIONS.md — Architectural Memory

Log of consciously-made decisions and the alternatives they rejected. The point of this file is to stop an AI coding agent (or a future contributor) from re-litigating a choice that was already made deliberately. When re-proposing something listed here as "rejected for now," check the trigger condition first — it may already be met.

Format: **Decision** — what we chose. **Rejected (for now)** — what we didn't. **Why.** **Revisit when.**

---

## Database: PostgreSQL first, ClickHouse later

**Decision:** PostgreSQL is the only datastore for model registry, routing traces, and verification results.
**Rejected (for now):** ClickHouse for trace analytics.
**Why:** Premature infra complexity — Postgres handles MVP-scale trace volume fine, and running two datastores adds ops burden with no current benefit (`PRD.md` §14).
**Revisit when:** Trace volume or analytics query patterns actually strain Postgres — not before.

---

## Vector store: FAISS first, managed vector DB later

**Decision:** FAISS (local, in-process) for retrieval in the verification layer.
**Rejected (for now):** Pinecone, Weaviate.
**Why:** No need to pay for or operate a managed vector service before the verification domain and document volume are known (`PRD.md` §20).
**Revisit when:** Document corpus size or multi-instance retrieval needs outgrow a local index.

---

## Dashboard: Streamlit first, React later

**Decision:** Streamlit for the MVP dashboard.
**Rejected (for now):** React + Tailwind dashboard.
**Why:** Fast to implement, avoids frontend build-out before the API is validated (`PRD.md` §16, §36).
**Revisit when:** Product-market validation is done and dashboard UX becomes a differentiator (Week 13+, `PRD.md` §35).

---

## Task classifier: prompted LLM first, fine-tuned classifier later

**Decision:** Use a well-prompted LLM (Claude/GPT) for task classification.
**Rejected (for now):** A fine-tuned classifier.
**Why:** Unproven need — a prompted LLM is faster to ship and iterate on; fine-tuning adds training/data-collection overhead that isn't justified yet (`PRD.md` §4, §7.2).
**Revisit when:** Classification accuracy or latency from the prompted approach is measured and found insufficient.

---

## Verification scope: one domain first, general-purpose later

**Decision:** Verification layer targets a single narrow domain initially (legal or financial — final choice deferred to user interviews, `PRD.md` §31–§33).
**Rejected (for now):** General-purpose fact-checking across all domains.
**Why:** Verification is flagged as the hardest technical component (`PRD.md` §39, Risk 1); narrowing scope is the stated mitigation.
**Revisit when:** The chosen domain's verification pipeline is validated end-to-end.

---

## Orchestration: LangGraph

**Decision:** LangGraph for routing and verification workflow orchestration.
**Why:** Matches the multi-step, stateful nature of both pipelines (classify → route → generate; extract → retrieve → verify → score) as specified in `PRD.md` §11, §36.

---

## Backend framework: FastAPI + PostgreSQL

**Decision:** FastAPI for the API layer, PostgreSQL for persistence.
**Why:** Async-native, strong typing via Pydantic, and the team's stated stack (`PRD.md` §11, §36).

---

## Local dev: Postgres container published on host port 5433, not 5432

**Decision:** `docker-compose.yml`'s `db` service maps `5433:5432` instead of the default `5432:5432`.
**Why:** This development machine already has a native Postgres install listening on `localhost:5432`. Publishing the container on the same port silently routed host connections to the native instance instead of the container (surfaced as a confusing `InvalidPasswordError` even though the container's credentials were correct).
**How to apply:** Any host-side tool connecting to the containerized DB (Alembic, seed scripts, a local psql) must target port `5433`, e.g. `postgresql+asyncpg://postgres:postgres@localhost:5433/llm_router`. The `backend` container itself is unaffected — it talks to `db:5432` over the internal Docker network. `.env`'s `DATABASE_URL` intentionally still says `db:5432` for that reason; override `DATABASE_URL` on the command line for host-side scripts instead of editing `.env`.
**Revisit when:** Never, unless this specific machine's native Postgres install is removed — this is a local-environment workaround, not a portable convention. A teammate on a clean machine may not need it.

---

## Task classifier: fall back to the heuristic on failure, don't hard-fail `/route`

**Decision:** If the LLM classifier call fails (missing API key, network error, malformed response), `RoutingService` falls back to the old word-count heuristic (`app/routing/rules.py::fallback_classify`) instead of returning an error. The response's `reasoning` field explicitly flags when this happened.
**Why:** A missing/invalid provider API key is the actual current state of this environment (`.env` ships with empty keys), not a hypothetical edge case — hard-failing `/route` whenever no key is configured would make local dev and CI unusable. `CONVENTIONS.md` already establishes the pattern of never *silently* treating a degraded result as a normal one (see the verification-failure rule) — this applies the same idea to routing: degrade honestly, don't hide it.
**Revisit when:** Once `/verify`-style explicit "not successfully classified" signaling exists (Phase 3 precedent), consider whether `/route` should also expose a structured `classifier_used: bool` field instead of a text note in `reasoning`.

---

## How to add a new entry

Add one whenever a real alternative was considered and consciously rejected — not for the default/obvious choice. Include the trigger condition for revisiting so this file stays a decision log, not dead weight.
