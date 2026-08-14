from app.schemas.classification import Complexity, Domain, TaskClassification
from app.schemas.model import ModelRead, ModelTier


def estimate_complexity(task: str) -> Complexity:
    """Word-count heuristic. Used only as the fallback_classify() path when the
    real LLM-based classifier (app/services/classifier_service.py) is unavailable."""
    word_count = len(task.split())
    if word_count <= 8:
        return Complexity.SIMPLE
    if word_count <= 25:
        return Complexity.MODERATE
    return Complexity.COMPLEX


def fallback_classify(task: str, domain: Domain | None, latency_sensitive: bool | None) -> TaskClassification:
    """Used when the LLM classifier call fails (no API key, network error, bad
    response) so routing can still complete instead of hard-failing the request."""
    return TaskClassification(
        complexity=estimate_complexity(task),
        domain=domain or Domain.GENERAL,
        latency_sensitive=bool(latency_sensitive),
    )


def complexity_to_tier(complexity: Complexity) -> ModelTier:
    return {
        Complexity.SIMPLE: ModelTier.CHEAP,
        Complexity.MODERATE: ModelTier.STANDARD,
        Complexity.COMPLEX: ModelTier.PREMIUM,
        Complexity.PRODUCTION_CRITICAL: ModelTier.PREMIUM,
    }[complexity]


def select_model(
    candidates: list[ModelRead],
    tier: ModelTier,
    domain: str,
    latency_sensitive: bool,
) -> ModelRead | None:
    """Pick a model from active candidates: prefer domain + tier match, then
    tier-only, then domain-only, then any active model. Ranks the surviving
    pool by latency (if latency_sensitive) or cost (otherwise)."""
    active = [c for c in candidates if c.active]
    if not active:
        return None

    def domain_matches(m: ModelRead) -> bool:
        return domain == "general" or domain in m.strengths

    def rank(pool: list[ModelRead]) -> ModelRead:
        key = (lambda m: m.expected_latency) if latency_sensitive else (lambda m: m.cost_per_token)
        return min(pool, key=key)

    tier_matches = [c for c in active if c.tier == tier]
    domain_and_tier = [c for c in tier_matches if domain_matches(c)]
    if domain_and_tier:
        return rank(domain_and_tier)
    if tier_matches:
        return rank(tier_matches)

    domain_only = [c for c in active if domain_matches(c)]
    if domain_only:
        return rank(domain_only)

    return rank(active)


def estimate_cost(model: ModelRead, task: str) -> float:
    """Rough token estimate (~4 chars/token) times the model's per-token cost."""
    estimated_tokens = max(len(task) // 4, 1)
    return round(model.cost_per_token * estimated_tokens, 6)


def build_reasoning(
    complexity: Complexity,
    tier: ModelTier,
    domain: str,
    latency_sensitive: bool,
    model: ModelRead,
) -> str:
    latency_clause = " with a low-latency requirement" if latency_sensitive else ""
    reasoning = (
        f"Task classified as {complexity.value} complexity in the '{domain}' domain{latency_clause}; "
        f"routed to {tier.value}-tier model '{model.model_name}' ({model.provider})."
    )
    if complexity == Complexity.PRODUCTION_CRITICAL:
        reasoning += " Production-critical tasks should also pass through verification once that layer ships (see PRD.md Phase 3)."
    return reasoning
