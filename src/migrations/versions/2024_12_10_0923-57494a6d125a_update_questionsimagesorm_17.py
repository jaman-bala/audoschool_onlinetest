"""update QuestionsImagesOrm 17

Revision ID: 57494a6d125a
Revises: ee0d42bca874
Create Date: 2024-12-10 09:23:22.677660

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "57494a6d125a"
down_revision: Union[str, None] = "ee0d42bca874"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("question_photos")
    op.add_column("questions", sa.Column("file", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("questions", "file")
    op.create_table(
        "question_photos",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("question_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("photo_path", sa.VARCHAR(), autoincrement=False, nullable=False),
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
        sa.ForeignKeyConstraint(
            ["question_id"], ["questions.id"], name="question_photos_question_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="question_photos_pkey"),
    )
