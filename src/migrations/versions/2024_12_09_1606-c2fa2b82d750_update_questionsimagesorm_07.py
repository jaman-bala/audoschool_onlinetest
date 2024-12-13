"""update QuestionsImagesOrm 07

Revision ID: c2fa2b82d750
Revises: 59bc4ab21476
Create Date: 2024-12-09 16:06:13.541665

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "c2fa2b82d750"
down_revision: Union[str, None] = "59bc4ab21476"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("avatars", "updated_date")
    op.drop_column("avatars", "created_date")
    op.drop_column("images", "updated_date")
    op.drop_column("images", "created_date")


def downgrade() -> None:
    op.add_column(
        "images",
        sa.Column(
            "created_date",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "images",
        sa.Column(
            "updated_date",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "avatars",
        sa.Column(
            "created_date",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "avatars",
        sa.Column(
            "updated_date",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
    )
