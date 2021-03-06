"""initial migration2

Revision ID: 790032e435d0
Revises: 
Create Date: 2018-08-29 16:22:41.399482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790032e435d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('code', sa.String(length=16), nullable=True),
    sa.Column('fair_price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stocks_code'), 'stocks', ['code'], unique=True)
    op.create_index(op.f('ix_stocks_name'), 'stocks', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_stocks_name'), table_name='stocks')
    op.drop_index(op.f('ix_stocks_code'), table_name='stocks')
    op.drop_table('stocks')
    # ### end Alembic commands ###
