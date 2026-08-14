from enum import StrEnum

from pydantic import BaseModel


class Complexity(StrEnum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    PRODUCTION_CRITICAL = "production_critical"


class Domain(StrEnum):
    GENERAL = "general"
    CODING = "coding"
    LEGAL = "legal"
    FINANCIAL = "financial"
    TECHNICAL = "technical"
    RESEARCH = "research"


class TaskClassification(BaseModel):
    complexity: Complexity
    domain: Domain
    latency_sensitive: bool
