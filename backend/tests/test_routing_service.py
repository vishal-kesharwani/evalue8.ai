from types import SimpleNamespace

import pytest

from app.schemas.classification import Complexity, Domain, TaskClassification
from app.schemas.routing import RouteRequest
from app.services.classifier_service import ClassificationError
from app.services.routing_service import NoAvailableModelError, RoutingService


def make_orm_model(**overrides):
    base = dict(
        id="00000000-0000-0000-0000-000000000001",
        provider="anthropic",
        model_name="test-model",
        cost_per_token=0.000003,
        expected_latency=1.0,
        context_window=100_000,
        strengths=["general"],
        weaknesses=[],
        benchmark_scores={},
        tier="standard",
        active=True,
        created_at="2026-01-01T00:00:00Z",
        updated_at="2026-01-01T00:00:00Z",
    )
    base.update(overrides)
    return SimpleNamespace(**base)


class FakeRegistry:
    def __init__(self, models):
        self._models = models

    async def list_active(self):
        return self._models


class FakeClassifier:
    def __init__(self, result=None, error=None):
        self._result = result
        self._error = error

    async def classify(self, task):
        if self._error is not None:
            raise self._error
        return self._result


class FakeTraceService:
    def __init__(self):
        self.recorded = []

    async def record(self, **fields):
        self.recorded.append(fields)
        return SimpleNamespace(**fields)


@pytest.mark.asyncio
async def test_route_uses_classifier_result_when_no_caller_overrides():
    models = [make_orm_model(model_name="financial-premium", tier="premium", strengths=["financial"])]
    classifier = FakeClassifier(
        result=TaskClassification(complexity=Complexity.COMPLEX, domain=Domain.FINANCIAL, latency_sensitive=True)
    )
    service = RoutingService(FakeRegistry(models), classifier, FakeTraceService())

    response = await service.route(RouteRequest(task="Analyze this filing"))

    assert response.recommended_model == "financial-premium"
    assert "financial" in response.reasoning
    assert "fallback" not in response.reasoning.lower()


@pytest.mark.asyncio
async def test_route_caller_supplied_domain_and_latency_override_classifier():
    models = [
        make_orm_model(model_name="legal-cheap", tier="cheap", strengths=["legal"], cost_per_token=0.000001),
    ]
    classifier = FakeClassifier(
        result=TaskClassification(complexity=Complexity.SIMPLE, domain=Domain.GENERAL, latency_sensitive=False)
    )
    service = RoutingService(FakeRegistry(models), classifier, FakeTraceService())

    response = await service.route(RouteRequest(task="short task", domain=Domain.LEGAL, latency_sensitive=True))

    assert response.recommended_model == "legal-cheap"


@pytest.mark.asyncio
async def test_route_falls_back_to_heuristic_when_classifier_fails():
    models = [make_orm_model(model_name="generic-cheap", tier="cheap", strengths=["general"])]
    classifier = FakeClassifier(error=ClassificationError("no api key"))
    service = RoutingService(FakeRegistry(models), classifier, FakeTraceService())

    response = await service.route(RouteRequest(task="Fix typo"))

    assert response.recommended_model == "generic-cheap"
    assert "fallback" in response.reasoning.lower()


@pytest.mark.asyncio
async def test_route_raises_when_no_active_models():
    classifier = FakeClassifier(
        result=TaskClassification(complexity=Complexity.SIMPLE, domain=Domain.GENERAL, latency_sensitive=False)
    )
    service = RoutingService(FakeRegistry([]), classifier, FakeTraceService())

    with pytest.raises(NoAvailableModelError):
        await service.route(RouteRequest(task="anything"))


@pytest.mark.asyncio
async def test_route_records_a_trace_on_success():
    models = [make_orm_model(model_name="financial-premium", tier="premium", strengths=["financial"])]
    classifier = FakeClassifier(
        result=TaskClassification(complexity=Complexity.COMPLEX, domain=Domain.FINANCIAL, latency_sensitive=True)
    )
    trace_service = FakeTraceService()
    service = RoutingService(FakeRegistry(models), classifier, trace_service)

    await service.route(RouteRequest(task="Analyze this filing"))

    assert len(trace_service.recorded) == 1
    recorded = trace_service.recorded[0]
    assert recorded["selected_model"] == "financial-premium"
    assert recorded["task_domain"] == "financial"
    assert recorded["outcome"] == "routed"
    assert recorded["latency"] >= 0


@pytest.mark.asyncio
async def test_route_does_not_record_a_trace_when_no_model_available():
    classifier = FakeClassifier(
        result=TaskClassification(complexity=Complexity.SIMPLE, domain=Domain.GENERAL, latency_sensitive=False)
    )
    trace_service = FakeTraceService()
    service = RoutingService(FakeRegistry([]), classifier, trace_service)

    with pytest.raises(NoAvailableModelError):
        await service.route(RouteRequest(task="anything"))

    assert trace_service.recorded == []
