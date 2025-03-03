"""Initial commit

Revision ID: 451e3b6a2674
Revises: 
Create Date: 2025-03-03 13:07:48.155963

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import VARCHAR

# revision identifiers, used by Alembic.
revision: str = '451e3b6a2674'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the users table in the database"""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.Index('ix_users_email', 'email')
    )


def downgrade() -> None:
    """Drop the users table"""
    op.drop_table('users')
