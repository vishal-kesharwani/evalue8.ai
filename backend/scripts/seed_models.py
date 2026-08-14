import asyncio

from app.database import async_session_factory
from app.schemas.model import ModelCreate, ModelTier
from app.services.model_registry import ModelRegistryService

SEED_MODELS = [
    ModelCreate(
        provider="anthropic",
        model_name="claude-haiku-4-5-20251001",
        cost_per_token=0.000001,
        expected_latency=0.8,
        context_window=200_000,
        strengths=["general", "coding"],
        weaknesses=["deep research"],
        benchmark_scores={"mmlu": 0.75},
        tier=ModelTier.CHEAP,
    ),
    ModelCreate(
        provider="openai",
        model_name="gpt-4o-mini",
        cost_per_token=0.0000015,
        expected_latency=1.0,
        context_window=128_000,
        strengths=["general", "coding"],
        weaknesses=["long-context reasoning"],
        benchmark_scores={"mmlu": 0.78},
        tier=ModelTier.STANDARD,
    ),
    ModelCreate(
        provider="anthropic",
        model_name="claude-sonnet-5",
        cost_per_token=0.000003,
        expected_latency=1.5,
        context_window=200_000,
        strengths=["general", "coding", "financial", "legal", "research"],
        weaknesses=[],
        benchmark_scores={"mmlu": 0.9},
        tier=ModelTier.PREMIUM,
    ),
    ModelCreate(
        provider="anthropic",
        model_name="claude-opus-5",
        cost_per_token=0.000015,
        expected_latency=2.5,
        context_window=200_000,
        strengths=["general", "coding", "financial", "legal", "research", "production-critical"],
        weaknesses=[],
        benchmark_scores={"mmlu": 0.93},
        tier=ModelTier.PREMIUM,
    ),
]


async def seed() -> None:
    async with async_session_factory() as session:
        service = ModelRegistryService(session)
        existing = await service.list_all()
        if existing:
            print(f"Registry already has {len(existing)} models — skipping seed.")
            return
        for model in SEED_MODELS:
            await service.create(model)
        print(f"Seeded {len(SEED_MODELS)} models.")


if __name__ == "__main__":
    asyncio.run(seed())
