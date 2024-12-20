"""update QuestionsImagesOrm 14

Revision ID: ca5ddb239d39
Revises: 6d2779d75a7f
Create Date: 2024-12-09 17:12:11.412172

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "ca5ddb239d39"
down_revision: Union[str, None] = "6d2779d75a7f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("photos")
    op.add_column("images", sa.Column("question", sa.UUID(), nullable=False))
    op.create_foreign_key(None, "images", "questions", ["question"], ["id"])


def downgrade() -> None:
    op.drop_constraint(None, "images", type_="foreignkey")
    op.drop_column("images", "question")
    op.create_table(
        "photos",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("filename", sa.VARCHAR(length=999), autoincrement=False, nullable=True),
        sa.Column("question_id", sa.UUID(), autoincrement=False, nullable=False),
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
        sa.ForeignKeyConstraint(["question_id"], ["questions.id"], name="photos_question_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="photos_pkey"),
    )
