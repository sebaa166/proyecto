"""añade imagen al modelo post

Revision ID: a6200f4e68c8
Revises: 6b6e2391aa93
Create Date: 2023-10-02 17:26:15.139873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6200f4e68c8'
down_revision = '6b6e2391aa93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image_name')

    # ### end Alembic commands ###
