"""followers

Revision ID: 1269f4f0ee9b
Revises: 66d038569fbd
Create Date: 2018-10-14 18:25:22.647466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1269f4f0ee9b'
down_revision = '66d038569fbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
