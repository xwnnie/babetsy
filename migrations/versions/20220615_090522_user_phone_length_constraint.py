"""user-phone-length-constraint

Revision ID: 836a7b471d63
Revises: b48199c35571
Create Date: 2022-06-15 09:05:22.934216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836a7b471d63'
down_revision = 'b48199c35571'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=10),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
    # ### end Alembic commands ###
