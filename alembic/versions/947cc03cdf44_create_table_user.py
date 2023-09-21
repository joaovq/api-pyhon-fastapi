"""create table user

Revision ID: 947cc03cdf44
Revises: a26a2dce6d78
Create Date: 2023-09-20 23:45:51.143522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '947cc03cdf44'
down_revision: Union[str, None] = 'a26a2dce6d78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
         sa.Column('id',sa.Integer,primary_key=True),
     sa.Column('name',sa.String),
     sa.Column('username',sa.String, unique=True),
     sa.Column('password',sa.String),
     sa.Column('email',sa.String, unique=True),
     sa.Column('is_active',sa.Boolean, default=False),
    )


def downgrade() -> None:
    pass
