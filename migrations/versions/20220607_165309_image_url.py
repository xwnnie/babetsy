"""image-url

Revision ID: 919bf369090e
Revises: 9be750603905
Create Date: 2022-06-07 16:53:09.379094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919bf369090e'
down_revision = '9be750603905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'image_url', type_=sa.String(length=500))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'image_url', type_=sa.String(length=255))
    # ### end Alembic commands ###
