"""Rename set_number to training_set_number

Revision ID: 3437c12adbcf
Revises: 7556d18e0c52
Create Date: 2026-11-03 20:05:28.108580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3437c12adbcf'
down_revision: Union[str, Sequence[str], None] = '7556d18e0c52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'completed_set',
        'set_number',
        new_column_name='training_set_number'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'completed_set',
        'training_set_number',
        new_column_name='set_number'
    )
