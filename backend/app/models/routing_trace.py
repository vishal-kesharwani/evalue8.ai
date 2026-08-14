import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RoutingTraceEntry(Base):
    __tablename__ = "routing_traces"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_input: Mapped[str] = mapped_column(String, nullable=False)
    task_complexity: Mapped[str] = mapped_column(String(32), nullable=False)
    task_domain: Mapped[str] = mapped_column(String(32), nullable=False)
    latency_sensitivity: Mapped[bool] = mapped_column(Boolean, nullable=False)
    selected_model: Mapped[str] = mapped_column(String(128), nullable=False)
    routing_reasoning: Mapped[str] = mapped_column(String, nullable=False)
    estimated_cost: Mapped[float] = mapped_column(Float, nullable=False)
    actual_cost: Mapped[float | None] = mapped_column(Float, nullable=True)
    latency: Mapped[float] = mapped_column(Float, nullable=False)
    outcome: Mapped[str] = mapped_column(String(32), nullable=False, default="routed")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
