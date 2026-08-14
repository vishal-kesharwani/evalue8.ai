"""create model_registry table

Revision ID: 0001
Revises:
Create Date: 2026-08-14

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "model_registry",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("provider", sa.String(length=64), nullable=False),
        sa.Column("model_name", sa.String(length=128), nullable=False),
        sa.Column("cost_per_token", sa.Float(), nullable=False),
        sa.Column("expected_latency", sa.Float(), nullable=False),
        sa.Column("context_window", sa.Integer(), nullable=False),
        sa.Column("strengths", postgresql.ARRAY(sa.String()), server_default="{}", nullable=False),
        sa.Column("weaknesses", postgresql.ARRAY(sa.String()), server_default="{}", nullable=False),
        sa.Column("benchmark_scores", postgresql.JSONB(), server_default="{}", nullable=False),
        sa.Column("tier", sa.String(length=16), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("model_registry")
