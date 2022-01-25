"""empty message

Revision ID: c36d15b1bb34
Revises: 72bd317ce1bd
Create Date: 2022-01-24 20:57:33.892627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c36d15b1bb34'
down_revision = '72bd317ce1bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('program', 'apitoken')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('program', sa.Column('apitoken', sa.VARCHAR(length=16), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
