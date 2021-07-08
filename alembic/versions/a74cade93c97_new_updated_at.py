"""new updated_at

Revision ID: a74cade93c97
Revises: d41251b4f99d
Create Date: 2021-07-08 09:36:59.163930

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from models.student import Student

# revision identifiers, used by Alembic.
revision = 'a74cade93c97'
down_revision = 'd41251b4f99d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('student', sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.text('now()')))
    conn = op.get_bind()

    all_users = conn.execute(sa.select([Student.id, Student.created_at])).fetchall()

    for id, created_at in all_users:
        op.execute(f"UPDATE student SET updated_at = '{created_at}' WHERE id = {id}")


def downgrade():
    op.drop_column('student', 'updated_at')
