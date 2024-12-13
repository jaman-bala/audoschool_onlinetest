"""update QuestionsImagesOrm 02

Revision ID: c8b736e7c81e
Revises: 7e486b870146
Create Date: 2024-12-09 15:17:52.689243

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "c8b736e7c81e"
down_revision: Union[str, None] = "7e486b870146"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("questions_images")


def downgrade() -> None:
    op.create_table(
        "questions_images",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("question_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("image_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["image_id"], ["images.id"], name="questions_images_image_id_fkey"),
        sa.ForeignKeyConstraint(
            ["question_id"], ["questions.id"], name="questions_images_question_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="questions_images_pkey"),
    )
