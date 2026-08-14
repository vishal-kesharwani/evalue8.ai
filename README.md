# LLM Router + Verification Platform

Intelligent routing layer that selects the optimal LLM for each incoming task and verifies generated output before it reaches the end user.

**"Right model, every time — with proof of why, and proof it's correct."**

## Docs

Start every session by reading these, in order:

1. [`PRD.md`](PRD.md) — product spec (what and why)
2. [`PROJECT.md`](PROJECT.md) — current state
3. [`STACK.md`](STACK.md) — exact tech stack/versions
4. [`CONVENTIONS.md`](CONVENTIONS.md) — coding rules
5. [`DECISIONS.md`](DECISIONS.md) — architectural decisions and why
6. [`TODO.md`](TODO.md) — what's next

## Repo layout

```text
backend/       FastAPI app (routing, verification, provider abstraction)
dashboard/     Streamlit MVP dashboard
migrations/    Alembic migrations
docs/          Additional docs
```

## Getting started

```bash
cp .env.example .env
docker-compose up --build
```

API will be available at `http://localhost:8000`. Dashboard at `http://localhost:8501`.

## Status

MVP / Phase 1 (Routing Engine) — not yet started. See [`TODO.md`](TODO.md) for the active sprint.
