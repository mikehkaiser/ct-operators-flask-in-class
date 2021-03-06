"""empty message

Revision ID: 109747cbd220
Revises: 78016cb3e43e
Create Date: 2021-08-05 10:45:39.560506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '109747cbd220'
down_revision = '78016cb3e43e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drone',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('camera_quality', sa.String(length=150), nullable=True),
    sa.Column('flight_time', sa.String(length=100), nullable=True),
    sa.Column('max_speed', sa.String(length=100), nullable=True),
    sa.Column('dimensions', sa.String(length=100), nullable=True),
    sa.Column('weight', sa.String(length=50), nullable=True),
    sa.Column('cost_of_prod', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('series', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('drone')
    # ### end Alembic commands ###
