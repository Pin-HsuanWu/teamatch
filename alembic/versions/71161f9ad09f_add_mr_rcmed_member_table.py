"""Add MR_Rcmed_Member table

Revision ID: 71161f9ad09f
Revises: 84523463fe09
Create Date: 2023-04-04 01:55:36.943495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71161f9ad09f'
down_revision = '84523463fe09'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('MR_Rcmed_Member',
    sa.Column('member_uuid', sa.UUID(), nullable=False),
    sa.Column('rcmed_member_uuid', sa.UUID(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['member_uuid'], ['MR_Member.member_uuid'], ),
    sa.ForeignKeyConstraint(['rcmed_member_uuid'], ['MR_Member.member_uuid'], ),
    sa.PrimaryKeyConstraint('member_uuid', 'rcmed_member_uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('MR_Rcmed_Member')
    # ### end Alembic commands ###
