"""update QuestionsImagesOrm 16

Revision ID: ee0d42bca874
Revises: 1a12a2dc3206
Create Date: 2024-12-09 17:53:02.233173

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "ee0d42bca874"
down_revision: Union[str, None] = "1a12a2dc3206"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "question_photos",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("question_id", sa.UUID(), nullable=False),
        sa.Column("photo_path", sa.String(), nullable=False),
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


def downgrade() -> None:
    op.drop_table("question_photos")
