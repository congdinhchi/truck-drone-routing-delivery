"""empty message

Revision ID: effea3a4c5dd
Revises: 5936dc4504ac
Create Date: 2022-09-28 12:09:00.775363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'effea3a4c5dd'
down_revision = '5936dc4504ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('depot', sa.Column('phone_num', sa.String(length=10), nullable=True))
    op.drop_column('depot', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('depot', sa.Column('phone', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('depot', 'phone_num')
    # ### end Alembic commands ###
