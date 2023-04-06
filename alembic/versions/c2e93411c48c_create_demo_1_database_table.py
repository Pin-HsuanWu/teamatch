"""Create Demo 1 database table

Revision ID: c2e93411c48c
Revises: 
Create Date: 2023-04-04 07:34:46.880138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2e93411c48c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('MatchingRoom',
    sa.Column('room_uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('room_id', sa.String(), nullable=False),
    sa.Column('due_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('min_member_num', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_forced_matching', sa.Boolean(), nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_closed', sa.Boolean(), nullable=False),
    sa.Column('finish_time', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('room_uuid'),
    sa.UniqueConstraint('room_id')
    )
    op.create_table('NotificationTemplate',
    sa.Column('template_uuid', sa.UUID(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('template_uuid')
    )
    op.create_table('ScheduledJob',
    sa.Column('job_uuid', sa.UUID(), nullable=False),
    sa.Column('trigger_time', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('job_uuid')
    )
    op.create_table('User',
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('line_id', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('user_uuid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('line_id')
    )
    op.create_table('BindUser',
    sa.Column('bind_uuid', sa.UUID(), nullable=False),
    sa.Column('bind_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('room_uuid', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['room_uuid'], ['MatchingRoom.room_uuid'], ),
    sa.PrimaryKeyConstraint('bind_uuid')
    )
    op.create_table('Group',
    sa.Column('group_uuid', sa.UUID(), nullable=False),
    sa.Column('room_uuid', sa.UUID(), nullable=False),
    sa.Column('create_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('group_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['room_uuid'], ['MatchingRoom.room_uuid'], ),
    sa.PrimaryKeyConstraint('group_uuid')
    )
    op.create_table('MatchingEvent',
    sa.Column('matching_event_uuid', sa.UUID(), nullable=False),
    sa.Column('maching_algo', sa.String(), nullable=False),
    sa.Column('room_uuid', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['room_uuid'], ['MatchingRoom.room_uuid'], ),
    sa.PrimaryKeyConstraint('matching_event_uuid')
    )
    op.create_table('Notification',
    sa.Column('notification_uuid', sa.UUID(), nullable=False),
    sa.Column('receiver_uuid', sa.UUID(), nullable=False),
    sa.Column('sender_uuid', sa.UUID(), nullable=True),
    sa.Column('send_time', sa.DateTime(timezone=True), nullable=False),
    sa.Column('template_uuid', sa.String(), nullable=False),
    sa.Column('f_string', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_uuid'], ['User.user_uuid'], ),
    sa.ForeignKeyConstraint(['sender_uuid'], ['User.user_uuid'], ),
    sa.PrimaryKeyConstraint('notification_uuid')
    )
    op.create_table('Tag',
    sa.Column('tag_uuid', sa.UUID(), nullable=False),
    sa.Column('tag_text', sa.String(), nullable=False),
    sa.Column('room_uuid', sa.UUID(), nullable=False),
    sa.Column('mentioned_num', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room_uuid'], ['MatchingRoom.room_uuid'], ),
    sa.PrimaryKeyConstraint('tag_uuid', 'room_uuid'),
    sa.UniqueConstraint('tag_text')
    )
    op.create_table('GR_Member',
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('group_uuid', sa.UUID(), nullable=False),
    sa.Column('join_time', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['group_uuid'], ['Group.group_uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['User.user_uuid'], ),
    sa.PrimaryKeyConstraint('user_uuid', 'group_uuid')
    )
    op.create_table('MR_Member',
    sa.Column('user_uuid', sa.UUID(), nullable=False),
    sa.Column('room_uuid', sa.UUID(), nullable=False),
    sa.Column('member_uuid', sa.UUID(), nullable=False),
    sa.Column('join_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('leave_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_left', sa.Boolean(), nullable=False),
    sa.Column('is_bound', sa.Boolean(), nullable=False),
    sa.Column('bind_uuid', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['bind_uuid'], ['BindUser.bind_uuid'], ),
    sa.ForeignKeyConstraint(['room_uuid'], ['MatchingRoom.room_uuid'], ),
    sa.ForeignKeyConstraint(['user_uuid'], ['User.user_uuid'], ),
    sa.PrimaryKeyConstraint('user_uuid', 'room_uuid', 'member_uuid'),
    sa.UniqueConstraint('member_uuid')
    )
    op.create_table('MR_Liked_Hated_Member',
    sa.Column('member_uuid', sa.UUID(), nullable=False),
    sa.Column('target_member_uuid', sa.UUID(), nullable=False),
    sa.Column('is_liked', sa.Boolean(), nullable=False),
    sa.Column('is_hated', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['member_uuid'], ['MR_Member.member_uuid'], ),
    sa.ForeignKeyConstraint(['target_member_uuid'], ['MR_Member.member_uuid'], ),
    sa.PrimaryKeyConstraint('member_uuid', 'target_member_uuid')
    )
    op.create_table('MR_Member_Tag',
    sa.Column('member_uuid', sa.UUID(), nullable=False),
    sa.Column('tag_text', sa.String(), nullable=False),
    sa.Column('is_self_tag', sa.Boolean(), nullable=False),
    sa.Column('is_find_tag', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['member_uuid'], ['MR_Member.member_uuid'], ),
    sa.PrimaryKeyConstraint('member_uuid')
    )
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
    op.drop_table('MR_Member_Tag')
    op.drop_table('MR_Liked_Hated_Member')
    op.drop_table('MR_Member')
    op.drop_table('GR_Member')
    op.drop_table('Tag')
    op.drop_table('Notification')
    op.drop_table('MatchingEvent')
    op.drop_table('Group')
    op.drop_table('BindUser')
    op.drop_table('User')
    op.drop_table('ScheduledJob')
    op.drop_table('NotificationTemplate')
    op.drop_table('MatchingRoom')
    # ### end Alembic commands ###