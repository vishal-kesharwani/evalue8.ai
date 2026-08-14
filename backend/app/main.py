from fastapi import FastAPI

from app.api.routing import router as routing_router
from app.api.traces import router as traces_router

app = FastAPI(title="LLM Router + Verification Platform")
app.include_router(routing_router)
app.include_router(traces_router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
