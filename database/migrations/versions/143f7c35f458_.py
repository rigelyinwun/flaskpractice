"""empty message

Revision ID: 143f7c35f458
Revises: ab661286786c
Create Date: 2024-10-05 10:21:57.896360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '143f7c35f458'
down_revision = 'ab661286786c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###