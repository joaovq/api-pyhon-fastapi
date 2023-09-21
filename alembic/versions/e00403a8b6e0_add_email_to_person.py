"""add email to person

Revision ID: e00403a8b6e0
Revises: 9fd7b37a6830
Create Date: 2023-09-20 22:50:57.348182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e00403a8b6e0'
down_revision: Union[str, None] = '9fd7b37a6830'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'person',
        sa.Column('email', sa.String, unique=True, nullable=True,default='')
    )


def downgrade() -> None:
    pass
