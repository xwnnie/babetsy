"""review-content-length

Revision ID: e817a36b9259
Revises: 4b15111725b4
Create Date: 2022-06-14 14:53:48.497885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e817a36b9259'
down_revision = '4b15111725b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reviews', 'content',
               existing_type=sa.TEXT(),
               type_=sa.String(length=250),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reviews', 'content',
               existing_type=sa.String(length=250),
               type_=sa.TEXT(),
               existing_nullable=False)
    # ### end Alembic commands ###
