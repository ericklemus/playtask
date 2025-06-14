"""add foreign key to Task -> TaskList

Revision ID: 784f9cfc33b9
Revises: 593752c3094d
Create Date: 2025-06-12 04:18:46.205748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '784f9cfc33b9'
down_revision: Union[str, None] = '593752c3094d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasklists',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_tasklists_uuid'), 'tasklists', ['uuid'], unique=False)
    op.add_column('tasks', sa.Column('completed', sa.Boolean(), nullable=False))
    op.add_column('tasks', sa.Column('tasklist_id', sa.Uuid(), nullable=False))
    op.create_foreign_key(None, 'tasks', 'tasklists', ['tasklist_id'], ['uuid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'tasklist_id')
    op.drop_column('tasks', 'completed')
    op.drop_index(op.f('ix_tasklists_uuid'), table_name='tasklists')
    op.drop_table('tasklists')
    # ### end Alembic commands ###