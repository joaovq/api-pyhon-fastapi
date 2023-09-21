"""add email

Revision ID: a26a2dce6d78
Revises: e00403a8b6e0
Create Date: 2023-09-20 22:55:35.853762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a26a2dce6d78'
down_revision: Union[str, None] = 'e00403a8b6e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('person')
    op.create_table(
        'person_1',
        sa.Column('id', sa.Integer,primary_key=True,  unique=True, nullable=True,default=''),
        sa.Column('name', sa.String, unique=True, nullable=True,default=''),
        sa.Column('email', sa.String, unique=True, nullable=True,default=''),
        sa.Column('age', sa.String, unique=True, nullable=True,default=''),
    )
    


def downgrade() -> None:
    pass
