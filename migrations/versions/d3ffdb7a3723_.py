"""empty message

Revision ID: d3ffdb7a3723
Revises: 
Create Date: 2024-07-10 01:26:36.562073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3ffdb7a3723'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dialogs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dialogs')
    # ### end Alembic commands ###