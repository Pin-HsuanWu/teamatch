"""Add ScheduledJob table

Revision ID: d7a3d43d8524
Revises: 8b56fa18895b
Create Date: 2023-04-04 01:40:17.831985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7a3d43d8524'
down_revision = '8b56fa18895b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ScheduledJob',
    sa.Column('job_uuid', sa.UUID(), nullable=False),
    sa.Column('trigger_time', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('job_uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ScheduledJob')
    # ### end Alembic commands ###
