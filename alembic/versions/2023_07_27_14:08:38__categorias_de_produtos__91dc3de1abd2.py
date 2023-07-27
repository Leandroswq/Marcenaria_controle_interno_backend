"""categorias_de_produtos

Revision ID: 91dc3de1abd2
Revises: b88192b3344d
Create Date: 2023-07-27 14:08:38.951160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "91dc3de1abd2"
down_revision = "b88192b3344d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "categorias_de_produto",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("categoria", sa.String(50), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("categorias_de_produto")
