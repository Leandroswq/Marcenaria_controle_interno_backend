"""custos_de_produto

Revision ID: 26a2c5adbc2b
Revises: a08fa91e79df
Create Date: 2023-07-26 19:04:57.215067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "26a2c5adbc2b"
down_revision = "c3bacdd0d252"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "custos_de_produto",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "produto", sa.Integer, sa.ForeignKey("produtos.id"), nullable=False
        ),
        sa.Column("valor", sa.Numeric(10, 2), nullable=False),
        sa.Column("valor_unitario", sa.Numeric(10, 2), nullable=False),
        sa.Column(
            "categoria",
            sa.Integer,
            sa.ForeignKey("categorias_de_produto.id"),
            nullable=False,
        ),
        sa.Column("unidade", sa.String(50), nullable=False),
        sa.Column("quantidade", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("custos_de_produto")
