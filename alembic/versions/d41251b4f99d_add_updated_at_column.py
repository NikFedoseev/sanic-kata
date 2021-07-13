"""add updated_at column

Revision ID: d41251b4f99d
Revises: e12fe1f2bcef
Create Date: 2021-06-18 09:09:53.466322

"""
from alembic import op
import sqlalchemy as sa
from models.student import Student
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'd41251b4f99d'
down_revision = 'e12fe1f2bcef'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_column('student', 'updated_at')
