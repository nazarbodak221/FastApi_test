"""Add article table

Revision ID: 451e3b6a2675
Revises: 451e3b6a2674
Create Date: 2025-03-03 13:15:48.155963

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import VARCHAR

# revision identifiers, used by Alembic.
revision: str = '451e3b6a2675'
down_revision: str = '451e3b6a2674'  # This refers to the previous migration where the users table was created
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create the articles table and the foreign key to the users table"""
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),  # Foreign Key to users table
        sa.Column('text', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('ix_articles_user_id', 'user_id')
    )


def downgrade() -> None:
    """Drop the articles table"""
    op.drop_table('articles')
