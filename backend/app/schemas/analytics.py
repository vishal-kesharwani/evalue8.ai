from pydantic import BaseModel, ConfigDict


class ModelCount(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    model: str
    count: int


class ModelCost(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    model: str
    total_cost: float


class DomainCost(BaseModel):
    domain: str
    total_cost: float


class AnalyticsSummary(BaseModel):
    total_requests: int
    requests_by_model: list[ModelCount]
    cost_by_model: list[ModelCost]
    cost_by_domain: list[DomainCost]
