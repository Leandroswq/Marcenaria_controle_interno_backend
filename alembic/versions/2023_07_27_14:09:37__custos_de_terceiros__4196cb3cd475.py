"""custos_de_terceiros

Revision ID: 4196cb3cd475
Revises: 722a7ae04d39
Create Date: 2023-07-27 14:09:37.491108

"""
from alembic import op
import sqlalchemy as sa

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "4196cb3cd475"
down_revision = "722a7ae04d39"
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "custos_de_terceiros",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("descricao", sa.String(255), nullable=False),
        sa.Column("valor", sa.Numeric(10, 2), nullable=False),
        sa.Column(
            "parceiro",
            sa.Integer,
            sa.ForeignKey("parceiros.id"),
            nullable=False,
        ),
        sa.Column(
            "reponsavel_pelo_contato",
            sa.Integer,
            sa.ForeignKey("funcionarios.id"),
            nullable=False,
        ),
        sa.Column("quantidade", sa.Integer, nullable=False),
        sa.Column(
            "ordem_de_pedido_id",
            sa.Integer,
            sa.ForeignKey("ordens_de_pedido.id"),
            nullable=False,
        ),
    )

    if create_seed:
        custos_de_terceiros = [
            {
                "descricao": "Custo 1",
                "valor": 100.50,
                "parceiro": 1,
                "reponsavel_pelo_contato": 1,
                "quantidade": 3,
                "ordem_de_pedido_id": 1,
            },
            {
                "descricao": "Custo 2",
                "valor": 50.20,
                "parceiro": 2,
                "reponsavel_pelo_contato": 2,
                "quantidade": 2,
                "ordem_de_pedido_id": 2,
            },
            {
                "descricao": "Custo 3",
                "valor": 75.30,
                "parceiro": 3,
                "reponsavel_pelo_contato": 3,
                "quantidade": 1,
                "ordem_de_pedido_id": 3,
            },
            {
                "descricao": "Custo 4",
                "valor": 80.40,
                "parceiro": 1,
                "reponsavel_pelo_contato": 2,
                "quantidade": 4,
                "ordem_de_pedido_id": 1,
            },
            {
                "descricao": "Custo 5",
                "valor": 120.00,
                "parceiro": 2,
                "reponsavel_pelo_contato": 3,
                "quantidade": 2,
                "ordem_de_pedido_id": 2,
            },
            {
                "descricao": "Custo 6",
                "valor": 65.80,
                "parceiro": 3,
                "reponsavel_pelo_contato": 1,
                "quantidade": 3,
                "ordem_de_pedido_id": 3,
            },
            {
                "descricao": "Custo 7",
                "valor": 90.10,
                "parceiro": 1,
                "reponsavel_pelo_contato": 2,
                "quantidade": 1,
                "ordem_de_pedido_id": 1,
            },
            {
                "descricao": "Custo 8",
                "valor": 55.00,
                "parceiro": 2,
                "reponsavel_pelo_contato": 3,
                "quantidade": 5,
                "ordem_de_pedido_id": 2,
            },
            {
                "descricao": "Custo 9",
                "valor": 70.25,
                "parceiro": 3,
                "reponsavel_pelo_contato": 1,
                "quantidade": 2,
                "ordem_de_pedido_id": 3,
            },
        ]

        try:
            op.bulk_insert(tabela, custos_de_terceiros)
        except Exception as e:
            op.drop_table("custos_de_terceiros")
            raise e


def downgrade() -> None:
    op.drop_table("custos_de_terceiros")
