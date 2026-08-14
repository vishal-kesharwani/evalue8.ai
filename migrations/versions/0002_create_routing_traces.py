"""create routing_traces table

Revision ID: 0002
Revises: 0001
Create Date: 2026-08-15

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "0002"
down_revision: Union[str, None] = "0001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "routing_traces",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("task_input", sa.String(), nullable=False),
        sa.Column("task_complexity", sa.String(length=32), nullable=False),
        sa.Column("task_domain", sa.String(length=32), nullable=False),
        sa.Column("latency_sensitivity", sa.Boolean(), nullable=False),
        sa.Column("selected_model", sa.String(length=128), nullable=False),
        sa.Column("routing_reasoning", sa.String(), nullable=False),
        sa.Column("estimated_cost", sa.Float(), nullable=False),
        sa.Column("actual_cost", sa.Float(), nullable=True),
        sa.Column("latency", sa.Float(), nullable=False),
        sa.Column("outcome", sa.String(length=32), server_default="routed", nullable=False),
        sa.Column("timestamp", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_routing_traces_selected_model", "routing_traces", ["selected_model"])
    op.create_index("ix_routing_traces_task_domain", "routing_traces", ["task_domain"])
    op.create_index("ix_routing_traces_timestamp", "routing_traces", ["timestamp"])


def downgrade() -> None:
    op.drop_index("ix_routing_traces_timestamp", table_name="routing_traces")
    op.drop_index("ix_routing_traces_task_domain", table_name="routing_traces")
    op.drop_index("ix_routing_traces_selected_model", table_name="routing_traces")
    op.drop_table("routing_traces")
