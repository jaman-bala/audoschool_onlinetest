"""add paymentsorm

Revision ID: 1b7392a4c704
Revises: ab38f6f31767
Create Date: 2024-12-09 10:26:19.244057

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "1b7392a4c704"
down_revision: Union[str, None] = "ab38f6f31767"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "payments",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("date_check", sa.Date(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=True),
        sa.Column(
            "created_date",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("updated_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("payments")
