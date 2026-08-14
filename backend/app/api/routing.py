from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.providers.anthropic_provider import AnthropicProvider
from app.schemas.routing import RouteRequest, RouteResponse
from app.services.classifier_service import TaskClassifierService
from app.services.model_registry import ModelRegistryService
from app.services.routing_service import NoAvailableModelError, RoutingService
from app.services.trace_service import TraceService

router = APIRouter(prefix="/api/v1", tags=["routing"])


@router.post("/route", response_model=RouteResponse)
async def route_task(request: RouteRequest, db: AsyncSession = Depends(get_db)) -> RouteResponse:
    classifier = TaskClassifierService(AnthropicProvider())
    service = RoutingService(ModelRegistryService(db), classifier, TraceService(db))
    try:
        return await service.route(request)
    except NoAvailableModelError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
