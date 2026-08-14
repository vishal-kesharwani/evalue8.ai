# CONVENTIONS.md — Coding Rules

## Python / Backend

- Follow PEP 8; format with `black`, lint with `ruff`.
- Type-hint everything. Pydantic models for all request/response schemas — never raw dicts across a service boundary.
- Async all the way down: FastAPI route handlers, SQLAlchemy calls, and provider HTTP calls are all `async def`. Don't mix sync DB calls into async routes.
- One responsibility per module. Routing logic lives in `app/routing/`, verification logic in `app/verification/`, provider clients in `app/providers/` — don't reach across these boundaries directly from `app/api/`.
- Business logic belongs in `app/services/`, not in route handlers. Route handlers parse input, call a service, return output.

## API conventions

- All endpoints under `/api/v1/` (even though the PRD examples show bare `/route`, `/verify` — version from day one).
- Every response that represents a decision (routing, verification) must include the reasoning/evidence behind it — never return a bare recommendation. This is a product requirement (`PRD.md` §27), not just a nice-to-have.
- Errors return structured JSON (`{"error": "...", "detail": "..."}`), never a bare 500 with a stack trace.
- Never silently treat a failed verification as a passed one (`PRD.md` §30) — an incomplete verification must be explicitly flagged as such in the response.

## Database

- All schema changes go through Alembic migrations — never hand-edit the schema or use `create_all()` outside of tests.
- Every table gets `created_at` / `updated_at`. Routing traces and verification results are append-only — never update or delete a persisted trace.
- Model registry rows are soft-deleted (`active = false`), never hard-deleted, so historical traces still resolve to the model metadata that was true at the time.

## LLM calls

- All provider calls go through the `app/providers/` abstraction — no direct OpenAI/Anthropic SDK calls from routing or verification code. This is what makes provider swaps and fallback handling possible.
- Every LLM call that feeds a user-facing decision (classification, verification) must log its prompt/response pair for auditability, with secrets/PII scrubbed before persisting.
- Prefer a well-prompted general model over a fine-tuned/custom model until the simpler approach is proven insufficient (`PRD.md` §4, §7.2) — don't reach for fine-tuning by default.

## Testing

- New service-layer logic needs a test in `backend/tests/` before it's considered done.
- Routing and verification decisions should have fixture-based tests (fixed input → expected model/verdict) so routing-rule regressions are caught.

## Git / commits

- Small, scoped commits. Update `PROJECT.md` and check off `TODO.md` items in the same commit as the work they describe, not a batch cleanup later.
