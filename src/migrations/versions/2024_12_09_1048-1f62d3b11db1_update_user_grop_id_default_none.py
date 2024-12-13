"""update user grop_id default None

Revision ID: 1f62d3b11db1
Revises: 1b7392a4c704
Create Date: 2024-12-09 10:48:30.414337

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "1f62d3b11db1"
down_revision: Union[str, None] = "1b7392a4c704"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users", "group_id", existing_type=sa.UUID(), nullable=True)


def downgrade() -> None:
    op.alter_column("users", "group_id", existing_type=sa.UUID(), nullable=False)
