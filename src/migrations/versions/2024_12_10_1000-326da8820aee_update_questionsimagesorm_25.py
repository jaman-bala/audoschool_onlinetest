"""update QuestionsImagesOrm 25

Revision ID: 326da8820aee
Revises: 94992fdcf9d7
Create Date: 2024-12-10 10:00:55.520065

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "326da8820aee"
down_revision: Union[str, None] = "94992fdcf9d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("questions", sa.Column("files", postgresql.ARRAY(sa.String()), nullable=True))
    op.drop_column("questions", "file")


def downgrade() -> None:
    op.add_column("questions", sa.Column("file", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column("questions", "files")
