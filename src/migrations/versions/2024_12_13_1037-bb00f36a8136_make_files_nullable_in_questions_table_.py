"""Make files nullable in questions table up:01

Revision ID: bb00f36a8136
Revises: c1f327b1ba9d
Create Date: 2024-12-13 10:37:50.434623

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "bb00f36a8136"
down_revision: Union[str, None] = "c1f327b1ba9d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("questions", "files", existing_type=sa.ARRAY(sa.String()), nullable=True)


def downgrade() -> None:
    op.alter_column("questions", "files", existing_type=sa.ARRAY(sa.String()), nullable=False)
