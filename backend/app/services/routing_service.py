import time

from app.routing.rules import build_reasoning, complexity_to_tier, estimate_cost, fallback_classify, select_model
from app.schemas.classification import TaskClassification
from app.schemas.model import ModelRead
from app.schemas.routing import RouteRequest, RouteResponse
from app.services.classifier_service import ClassificationError, TaskClassifierService
from app.services.model_registry import ModelRegistryService
from app.services.trace_service import TraceService

_FALLBACK_NOTE = " (Task classifier unavailable — complexity/domain estimated with a fallback heuristic.)"


class NoAvailableModelError(Exception):
    pass


class RoutingService:
    def __init__(self, registry: ModelRegistryService, classifier: TaskClassifierService, trace_service: TraceService):
        self.registry = registry
        self.classifier = classifier
        self.trace_service = trace_service

    async def route(self, request: RouteRequest) -> RouteResponse:
        start = time.perf_counter()

        candidates_orm = await self.registry.list_active()
        candidates = [ModelRead.model_validate(c) for c in candidates_orm]

        if not candidates:
            raise NoAvailableModelError("No active models are registered.")

        classification, used_fallback = await self._classify(request)

        domain = request.domain or classification.domain
        latency_sensitive = (
            request.latency_sensitive if request.latency_sensitive is not None else classification.latency_sensitive
        )
        tier = complexity_to_tier(classification.complexity)

        model = select_model(candidates, tier, domain, latency_sensitive)
        if model is None:
            raise NoAvailableModelError("No active model available to serve this request.")

        reasoning = build_reasoning(classification.complexity, tier, domain, latency_sensitive, model)
        if used_fallback:
            reasoning += _FALLBACK_NOTE

        cost = estimate_cost(model, request.task)
        routing_latency = time.perf_counter() - start

        await self.trace_service.record(
            task_input=request.task,
            task_complexity=classification.complexity.value,
            task_domain=domain.value,
            latency_sensitivity=latency_sensitive,
            selected_model=model.model_name,
            routing_reasoning=reasoning,
            estimated_cost=cost,
            actual_cost=None,
            latency=routing_latency,
            outcome="routed",
        )

        return RouteResponse(
            recommended_model=model.model_name,
            reasoning=reasoning,
            estimated_cost=cost,
        )

    async def _classify(self, request: RouteRequest) -> tuple[TaskClassification, bool]:
        try:
            return await self.classifier.classify(request.task), False
        except ClassificationError:
            return fallback_classify(request.task, request.domain, request.latency_sensitive), True
