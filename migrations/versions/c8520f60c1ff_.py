"""empty message

Revision ID: c8520f60c1ff
Revises: 404e5319a3d9
Create Date: 2022-05-20 20:31:48.345754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8520f60c1ff'
down_revision = '404e5319a3d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'description_1',
               existing_type=sa.VARCHAR(length=2500),
               type_=sa.String(length=5000),
               existing_nullable=False)
    op.alter_column('products', 'description_2',
               existing_type=sa.VARCHAR(length=2500),
               type_=sa.String(length=5000),
               existing_nullable=False)
    op.alter_column('products', 'description_3',
               existing_type=sa.VARCHAR(length=2500),
               type_=sa.String(length=5000),
               existing_nullable=False)
    op.alter_column('products', 'description_4',
               existing_type=sa.VARCHAR(length=2500),
               type_=sa.String(length=5000),
               existing_nullable=False)
    op.alter_column('products', 'img',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.String(length=2500),
               existing_nullable=False)
    op.alter_column('products', 'thumbnail',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=5000),
               existing_nullable=False)
    op.alter_column('products', 'tittle_description_4',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=5000),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'tittle_description_4',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)
    op.alter_column('products', 'thumbnail',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=False)
    op.alter_column('products', 'img',
               existing_type=sa.String(length=2500),
               type_=sa.VARCHAR(length=250),
               existing_nullable=False)
    op.alter_column('products', 'description_4',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=2500),
               existing_nullable=False)
    op.alter_column('products', 'description_3',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=2500),
               existing_nullable=False)
    op.alter_column('products', 'description_2',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=2500),
               existing_nullable=False)
    op.alter_column('products', 'description_1',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=2500),
               existing_nullable=False)
    # ### end Alembic commands ###
