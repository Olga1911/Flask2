"""Add surname

Revision ID: 90921b74c966
Revises: f6eda7049057
Create Date: 2022-09-17 21:45:19.332091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90921b74c966'
down_revision = 'f6eda7049057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author_model', sa.Column('surname', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('author_model', 'surname')
    # ### end Alembic commands ###
