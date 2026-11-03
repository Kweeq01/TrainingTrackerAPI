"""Rename training_set_number to completed_set_number

Revision ID: 4cd550177268
Revises: 3437c12adbcf
Create Date: 2026-11-03 20:56:09.108664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cd550177268'
down_revision: Union[str, Sequence[str], None] = '3437c12adbcf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "completed_set",
        "training_set_number",
        new_column_name="completed_set_number"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "completed_set",
        "completed_set_number",
        new_column_name="training_set_number"
    )
