"""up:17 update models and add new models 

Revision ID: b90e56ca8d67
Revises: 7c74df69df23
Create Date: 2024-12-06 10:30:56.051714

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "b90e56ca8d67"
down_revision: Union[str, None] = "7c74df69df23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "questions_images",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("question_id", sa.UUID(), nullable=False),
        sa.Column("image_id", sa.UUID(), nullable=False),
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
            ["image_id"],
            ["images.id"],
        ),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["questions.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_constraint("questions_image_id_fkey", "questions", type_="foreignkey")
    op.drop_column("questions", "image_id")


def downgrade() -> None:
    op.add_column(
        "questions",
        sa.Column("image_id", sa.UUID(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "questions_image_id_fkey", "questions", "images", ["image_id"], ["id"]
    )
    op.drop_table("questions_images")

