"""esp

Revision ID: ffa0bce948be
Revises: 79a419a3b9cd
Create Date: 2023-11-22 17:12:00.288904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa0bce948be'
down_revision = '79a419a3b9cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('especialidad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('familia', sa.String(length=20), nullable=True),
    sa.Column('codigo', sa.String(length=5), nullable=True),
    sa.Column('nombre', sa.String(length=256), nullable=False),
    sa.Column('nivel', sa.String(length=20), nullable=True),
    sa.Column('cert', sa.String(length=256), nullable=False),
    sa.Column('resolucion', sa.String(length=20), nullable=True),
    sa.Column('hcat', sa.String(length=4), nullable=True),
    sa.Column('hreloj', sa.String(length=4), nullable=True),
    sa.Column('requisitos', sa.String(length=128), nullable=True),
    sa.Column('diseno', sa.String(length=20), nullable=True),
    sa.Column('reemplaza', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modulo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=10), nullable=True),
    sa.Column('nombre', sa.String(length=256), nullable=False),
    sa.Column('hcat', sa.String(length=4), nullable=True),
    sa.Column('hreloj', sa.String(length=4), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('especialidad_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['especialidad_id'], ['especialidad.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('turno', sa.String(length=15), nullable=True))
        batch_op.alter_column('especialidad',
               existing_type=sa.VARCHAR(length=256),
               type_=sa.Integer(),
               nullable=True)
        batch_op.create_foreign_key(None, 'especialidad', ['especialidad'], ['id'])
        batch_op.drop_column('icon')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('icon', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('especialidad',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.drop_column('turno')

    op.drop_table('modulo')
    op.drop_table('especialidad')
    # ### end Alembic commands ###
