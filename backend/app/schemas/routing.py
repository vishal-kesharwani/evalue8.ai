from pydantic import BaseModel, Field

from app.schemas.classification import Domain


class RouteRequest(BaseModel):
    task: str = Field(..., min_length=1)
    domain: Domain | None = None
    latency_sensitive: bool | None = None


class RouteResponse(BaseModel):
    recommended_model: str
    reasoning: str
    estimated_cost: float
