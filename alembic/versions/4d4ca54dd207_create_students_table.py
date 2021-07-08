"""create students table

Revision ID: 4d4ca54dd207
Revises: 
Create Date: 2021-04-30 16:29:11.571425

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4d4ca54dd207'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'student',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('active', sa.Boolean, nullable=False),
    )


def downgrade():
    op.drop_table('student')
