"""rename set_id to training_set_id

Revision ID: 7556d18e0c52
Revises: c42858b5d043
Create Date: 2026-11-01 23:59:28.844246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7556d18e0c52'
down_revision: Union[str, Sequence[str], None] = 'c42858b5d043'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands written manually: autogenerate cannot detect renames ###
    # The foreign key completed_set -> training_set is left untouched,
    # PostgreSQL updates it automatically when the column is renamed.
    op.alter_column('completed_set', 'set_id', new_column_name='training_set_id')
    op.alter_column('training_set', 'set_id', new_column_name='training_set_id')
    # ### end manual commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands written manually: reverse of upgrade() ###
    op.alter_column('training_set', 'training_set_id', new_column_name='set_id')
    op.alter_column('completed_set', 'training_set_id', new_column_name='set_id')
    # ### end manual commands ###