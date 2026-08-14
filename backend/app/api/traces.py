from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.analytics import AnalyticsSummary
from app.schemas.trace import TraceRead
from app.services.trace_service import TraceService

router = APIRouter(prefix="/api/v1", tags=["traces"])


@router.get("/traces", response_model=list[TraceRead])
async def list_traces(
    model: str | None = None,
    domain: str | None = None,
    outcome: str | None = None,
    limit: int = Query(default=100, le=1000),
    db: AsyncSession = Depends(get_db),
) -> list[TraceRead]:
    service = TraceService(db)
    traces = await service.list_traces(model=model, domain=domain, outcome=outcome, limit=limit)
    return [TraceRead.model_validate(t) for t in traces]


@router.get("/analytics", response_model=AnalyticsSummary)
async def get_analytics(db: AsyncSession = Depends(get_db)) -> AnalyticsSummary:
    service = TraceService(db)
    return await service.analytics_summary()
