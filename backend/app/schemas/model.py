from datetime import datetime
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ModelTier(StrEnum):
    CHEAP = "cheap"
    STANDARD = "standard"
    PREMIUM = "premium"


class ModelBase(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    provider: str
    model_name: str
    cost_per_token: float
    expected_latency: float
    context_window: int
    strengths: list[str] = []
    weaknesses: list[str] = []
    benchmark_scores: dict[str, float] = {}
    tier: ModelTier


class ModelCreate(ModelBase):
    pass


class ModelRead(ModelBase):
    model_config = ConfigDict(from_attributes=True, protected_namespaces=())

    id: UUID
    active: bool
    created_at: datetime
    updated_at: datetime
