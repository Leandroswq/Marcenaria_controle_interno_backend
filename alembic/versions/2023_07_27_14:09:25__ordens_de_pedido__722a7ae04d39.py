"""ordens_de_pedido

Revision ID: 722a7ae04d39
Revises: 4bed0f6d1585
Create Date: 2023-07-27 14:09:25.336193

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "722a7ae04d39"
down_revision = "4bed0f6d1585"
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "ordens_de_pedido",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "cliente_id",
            sa.Integer,
            sa.ForeignKey("clientes.id"),
            nullable=False,
        ),
        sa.Column("total", sa.Numeric(10, 2), nullable=False),
        sa.Column("inicio", sa.DateTime, nullable=False),
        sa.Column("data_prevista", sa.DateTime, nullable=False),
        sa.Column("Termino", sa.DateTime, nullable=True),
    )

    if create_seed:
        ordens_de_pedido = [
            {
                "cliente_id": 1,
                "total": 1500.00,
                "inicio": datetime(2023, 7, 27, 10, 0, 0),
                "data_prevista": datetime(2023, 8, 10, 18, 0, 0),
                "termino": None,
            },
            {
                "cliente_id": 2,
                "total": 2000.50,
                "inicio": datetime(2023, 7, 28, 9, 30, 0),
                "data_prevista": datetime(2023, 8, 15, 16, 30, 0),
                "termino": None,
            },
            {
                "cliente_id": 3,
                "total": 3000.75,
                "inicio": datetime(2023, 7, 30, 11, 15, 0),
                "data_prevista": datetime(2023, 8, 12, 20, 45, 0),
                "termino": None,
            },
        ]
        try:
            op.bulk_insert(tabela, ordens_de_pedido)
        except Exception as e:
            op.drop_table("ordens_de_pedido")
            raise e


def downgrade() -> None:
    op.drop_table("ordens_de_pedido")
