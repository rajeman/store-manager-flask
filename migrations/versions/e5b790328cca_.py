"""empty message

Revision ID: e5b790328cca
Revises: b30b86595ab8
Create Date: 2019-06-01 11:46:43.021076

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'e5b790328cca'
down_revision = 'b30b86595ab8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    state = postgresql.ENUM(
        'active', 'archived', 'deleted', name='state')
    state.create(op.get_bind())
    op.add_column('products', sa.Column('state', sa.Enum('active', 'archived', 'deleted', name='state'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'state')
    # ### end Alembic commands ###
