"""categorias_produto

Revision ID: c3bacdd0d252
Revises: 26a2c5adbc2b
Create Date: 2023-07-26 21:38:09.976885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c3bacdd0d252"
down_revision = "d8ddfc52c0fa"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "categorias",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("categoria", sa.String(50), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("categorias")
