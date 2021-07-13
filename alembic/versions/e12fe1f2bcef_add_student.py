"""add student

Revision ID: e12fe1f2bcef
Revises: 4d4ca54dd207
Create Date: 2021-04-30 16:45:06.910653

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from models.student import Student

# revision identifiers, used by Alembic.
revision = 'e12fe1f2bcef'
down_revision = '4d4ca54dd207'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()

    stmt = f"""
    INSERT INTO student (id, name, created_at, active)  
    VALUES
    (DEFAULT, 'Marcus Aurelius', '{datetime.utcnow()}', {True}),
    (DEFAULT, 'Abraham Lincoln', '{datetime.utcnow()}', {True});
    """

    conn.execute(stmt)


def downgrade():
    pass
