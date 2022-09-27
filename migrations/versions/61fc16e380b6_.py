"""empty message

Revision ID: 61fc16e380b6
Revises: 34da2274f480
Create Date: 2022-09-27 19:58:20.678890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61fc16e380b6'
down_revision = '34da2274f480'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone_num', sa.String(length=120), nullable=True),
    sa.Column('path_face_id', sa.String(length=120), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('upper_bound', sa.Integer(), nullable=True),
    sa.Column('lower_bound', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path_face_id')
    )
    op.create_table('package',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_package', sa.Integer(), nullable=True),
    sa.Column('id_target', sa.Integer(), nullable=True),
    sa.Column('time_order', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('package')
    op.drop_table('customer')
    # ### end Alembic commands ###
