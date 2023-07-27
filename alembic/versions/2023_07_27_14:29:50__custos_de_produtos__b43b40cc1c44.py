"""custos_de_produtos

Revision ID: b43b40cc1c44
Revises: 2a1d2b765e11
Create Date: 2023-07-27 14:29:50.644343

"""
from alembic import op
import sqlalchemy as sa

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "b43b40cc1c44"
down_revision = "4196cb3cd475"
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "custos_de_produto",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "produto", sa.Integer, sa.ForeignKey("produtos.id"), nullable=False
        ),
        sa.Column("valor", sa.Numeric(10, 2), nullable=False),
        sa.Column("valor_unitario", sa.Numeric(10, 2), nullable=False),
        sa.Column("quantidade", sa.Integer, nullable=False),
        sa.Column(
            "ordem_de_pedido_id",
            sa.Integer,
            sa.ForeignKey("ordens_de_pedido.id"),
            nullable=False,
        ),
    )

    if create_seed:
        custos = [
            {
                "produto": 1,
                "valor": 100.50,
                "valor_unitario": 50.25,
                "quantidade": 10,
                "ordem_de_pedido_id": 1,
            },
            {
                "produto": 2,
                "valor": 75.25,
                "valor_unitario": 25.08,
                "quantidade": 5,
                "ordem_de_pedido_id": 1,
            },
            {
                "produto": 1,
                "valor": 300.00,
                "valor_unitario": 150.00,
                "quantidade": 2,
                "ordem_de_pedido_id": 2,
            },
            {
                "produto": 2,
                "valor": 45.80,
                "valor_unitario": 22.90,
                "quantidade": 8,
                "ordem_de_pedido_id": 2,
            },
            {
                "produto": 3,
                "valor": 180.00,
                "valor_unitario": 60.00,
                "quantidade": 3,
                "ordem_de_pedido_id": 3,
            },
            {
                "produto": 3,
                "valor": 120.75,
                "valor_unitario": 40.25,
                "quantidade": 4,
                "ordem_de_pedido_id": 3,
            },
        ]
        try:
            op.bulk_insert(tabela, custos)
        except Exception as e:
            op.drop_table("custos_de_produto")
            raise e


def downgrade() -> None:
    op.drop_table("custos_de_produto")
