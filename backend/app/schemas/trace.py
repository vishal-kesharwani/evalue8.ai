from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TraceRead(BaseModel):
    model_config = ConfigDict(from_attributes=True, protected_namespaces=())

    id: UUID
    task_input: str
    task_complexity: str
    task_domain: str
    latency_sensitivity: bool
    selected_model: str
    routing_reasoning: str
    estimated_cost: float
    actual_cost: float | None
    latency: float
    outcome: str
    timestamp: datetime
