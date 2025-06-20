"""Creación de tablas

Revision ID: c01fede9b171
Revises: 
Create Date: 2024-05-08 17:04:58.680601

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c01fede9b171'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('infoVideo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('texto', sa.Text(), nullable=False),
    sa.Column('embedding', sa.Text(), nullable=False),
    sa.Column('idVideo', sa.Integer(), nullable=False),
    sa.Column('idUsuario', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idUsuario'], ['user.id'], ),
    sa.ForeignKeyConstraint(['idVideo'], ['videos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=mysql.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=mysql.INTEGER(),
               nullable=False)

    op.drop_table('infoVideo')
    # ### end Alembic commands ###
