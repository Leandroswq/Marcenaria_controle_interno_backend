"""custos_de_produtos

Revision ID: b43b40cc1c44
Revises: 4196cb3cd475
Create Date: 2023-07-27 14:29:50.644343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b43b40cc1c44"
down_revision = "4196cb3cd475"
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
        sa.Column("unidade", sa.String(50), nullable=False),
        sa.Column("quantidade", sa.Integer, nullable=False),
        sa.Column(
            "ordem_de_pedido_id",
            sa.Integer,
            sa.ForeignKey("ordens_de_pedido.id"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("custos_de_produto")
