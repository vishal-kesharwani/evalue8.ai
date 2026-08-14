import pytest

from app.routing.rules import (
    build_reasoning,
    complexity_to_tier,
    estimate_complexity,
    estimate_cost,
    fallback_classify,
    select_model,
)
from app.schemas.classification import Complexity, Domain
from app.schemas.model import ModelRead, ModelTier


def make_model(**overrides) -> ModelRead:
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
        tier=ModelTier.STANDARD,
        active=True,
        created_at="2026-01-01T00:00:00Z",
        updated_at="2026-01-01T00:00:00Z",
    )
    base.update(overrides)
    return ModelRead.model_validate(base)


@pytest.mark.parametrize(
    "task,expected",
    [
        ("Fix typo", Complexity.SIMPLE),
        (
            "Summarize this document in a few paragraphs covering the main points and "
            "providing enough context for someone unfamiliar with the topic to follow along.",
            Complexity.MODERATE,
        ),
        (
            "Analyze this financial report in extreme depth, cross-referencing every disclosed "
            "metric against prior quarters, identifying anomalies, footnote-level risks, and "
            "producing a multi-section risk memo with citations for each claim made throughout "
            "the entire analysis.",
            Complexity.COMPLEX,
        ),
    ],
)
def test_estimate_complexity(task, expected):
    assert estimate_complexity(task) == expected


def test_complexity_to_tier_mapping():
    assert complexity_to_tier(Complexity.SIMPLE) == ModelTier.CHEAP
    assert complexity_to_tier(Complexity.MODERATE) == ModelTier.STANDARD
    assert complexity_to_tier(Complexity.COMPLEX) == ModelTier.PREMIUM
    assert complexity_to_tier(Complexity.PRODUCTION_CRITICAL) == ModelTier.PREMIUM


def test_fallback_classify_uses_heuristic_and_defaults():
    result = fallback_classify("Fix typo", domain=None, latency_sensitive=None)
    assert result.complexity == Complexity.SIMPLE
    assert result.domain == Domain.GENERAL
    assert result.latency_sensitive is False


def test_fallback_classify_respects_provided_domain_and_latency():
    result = fallback_classify("Fix typo", domain=Domain.FINANCIAL, latency_sensitive=True)
    assert result.domain == Domain.FINANCIAL
    assert result.latency_sensitive is True


def test_build_reasoning_flags_production_critical_for_verification():
    model = make_model(model_name="premium-one", tier=ModelTier.PREMIUM)
    reasoning = build_reasoning(Complexity.PRODUCTION_CRITICAL, ModelTier.PREMIUM, "legal", False, model)
    assert "verification" in reasoning.lower()


def test_select_model_prefers_domain_match_within_tier():
    generic = make_model(
        model_name="generic-standard", tier=ModelTier.STANDARD, strengths=["general"], cost_per_token=0.000001
    )
    financial = make_model(
        model_name="financial-standard", tier=ModelTier.STANDARD, strengths=["financial"], cost_per_token=0.000005
    )

    chosen = select_model([generic, financial], ModelTier.STANDARD, "financial", latency_sensitive=False)

    assert chosen.model_name == "financial-standard"


def test_select_model_falls_back_to_tier_when_no_domain_match():
    generic = make_model(model_name="generic-standard", tier=ModelTier.STANDARD, strengths=["general"])

    chosen = select_model([generic], ModelTier.STANDARD, "legal", latency_sensitive=False)

    assert chosen.model_name == "generic-standard"


def test_select_model_prefers_cheapest_when_no_latency_requirement():
    cheap = make_model(model_name="cheap-one", cost_per_token=0.000001, expected_latency=2.0)
    pricier = make_model(model_name="pricier-one", cost_per_token=0.000009, expected_latency=0.2)

    chosen = select_model([cheap, pricier], ModelTier.STANDARD, "general", latency_sensitive=False)

    assert chosen.model_name == "cheap-one"


def test_select_model_prefers_lowest_latency_when_latency_sensitive():
    cheap = make_model(model_name="cheap-one", cost_per_token=0.000001, expected_latency=2.0)
    fast = make_model(model_name="fast-one", cost_per_token=0.000009, expected_latency=0.2)

    chosen = select_model([cheap, fast], ModelTier.STANDARD, "general", latency_sensitive=True)

    assert chosen.model_name == "fast-one"


def test_select_model_returns_none_when_no_candidates():
    assert select_model([], ModelTier.STANDARD, "general", latency_sensitive=False) is None


def test_select_model_ignores_inactive_models():
    inactive = make_model(model_name="inactive-one", active=False, cost_per_token=0.0000001)
    active = make_model(model_name="active-one", active=True, cost_per_token=0.000005)

    chosen = select_model([inactive, active], ModelTier.STANDARD, "general", latency_sensitive=False)

    assert chosen.model_name == "active-one"


def test_estimate_cost_is_positive_and_scales_with_task_length():
    model = make_model(cost_per_token=0.00001)
    short_cost = estimate_cost(model, "hi")
    long_cost = estimate_cost(model, "x" * 400)
    assert 0 < short_cost < long_cost


def test_build_reasoning_mentions_key_factors():
    model = make_model(model_name="financial-standard", tier=ModelTier.STANDARD, provider="anthropic")
    reasoning = build_reasoning(Complexity.MODERATE, ModelTier.STANDARD, "financial", True, model)
    assert "financial" in reasoning
    assert "financial-standard" in reasoning
    assert "low-latency" in reasoning
