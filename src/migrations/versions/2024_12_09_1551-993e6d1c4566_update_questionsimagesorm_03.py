"""update QuestionsImagesOrm 03

Revision ID: 993e6d1c4566
Revises: c8b736e7c81e
Create Date: 2024-12-09 15:51:53.782315

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "993e6d1c4566"
down_revision: Union[str, None] = "c8b736e7c81e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "photos",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("filename", sa.String(length=999), nullable=True),
        sa.Column("question_id", sa.UUID(), nullable=False),
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
            ["question_id"],
            ["questions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_column("questions", "created_date")
    op.drop_column("questions", "updated_date")
    op.drop_column("questions", "photo")


def downgrade() -> None:
    op.add_column(
        "questions",
        sa.Column("photo", sa.VARCHAR(length=999), autoincrement=False, nullable=True),
    )
    op.add_column(
        "questions",
        sa.Column(
            "updated_date",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "questions",
        sa.Column(
            "created_date",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_table("photos")
