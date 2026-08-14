# STACK.md — Technical Truth

Exact versions and tools in use. Update this file the moment a version changes — it is the single source of truth for what's actually installed, not what's aspirational.

## Backend

| Component | Choice | Version | Notes |
|---|---|---|---|
| Language | Python | 3.12+ | |
| Web framework | FastAPI | latest stable | async endpoints |
| ASGI server | Uvicorn | latest stable | |
| ORM | SQLAlchemy | 2.x | async engine |
| Migrations | Alembic | latest stable | |
| Validation | Pydantic | v2 | |
| Orchestration | LangGraph | latest stable | routing + verification workflows |

## Database

| Component | Choice | Notes |
|---|---|---|
| Primary datastore | PostgreSQL | 16+. Model registry, routing traces, verification results. |
| Future analytics store | ClickHouse | Not adopted yet — only if trace volume outgrows Postgres. See `DECISIONS.md`. |
| Vector store | FAISS | Local, in-process. Retrieval for verification layer. |
| Future managed vector store | Pinecone / Weaviate | Not adopted yet — only after retrieval needs outgrow FAISS. See `DECISIONS.md`. |

## LLM Providers

| Provider | Role |
|---|---|
| OpenAI API | Candidate model in registry; also usable for task classification |
| Anthropic API | Candidate model in registry; also usable for task classification |
| Open-source (Llama / Mistral via Together AI or Groq) | Cheap-tier candidate model — exact provider TBD |

## Dashboard

| Phase | Choice |
|---|---|
| MVP | Streamlit |
| Production | React + Vite + Tailwind |

## Infra / Dev

| Component | Choice |
|---|---|
| Containerization | Docker + docker-compose (app + Postgres) |
| Testing | pytest |
| Env config | `.env` (see `.env.example`), never committed |

## How to update this file

When you add, remove, or upgrade a dependency, update the table in the same commit. Do not let this file drift from `requirements.txt` / `package.json`.
