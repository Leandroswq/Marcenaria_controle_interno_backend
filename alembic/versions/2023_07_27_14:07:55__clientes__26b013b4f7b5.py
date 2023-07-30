"""clientes

Revision ID: 26b013b4f7b5
Revises:
Create Date: 2023-07-27 14:07:55.456422

"""
from alembic import op
import sqlalchemy as sa

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "26b013b4f7b5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "clientes",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_Nome", sa.String(100)),
        sa.Column("telefone", sa.VARCHAR(11), nullable=False),
        sa.Column("empresa", sa.String(50), nullable=True),
        sa.Column("e_empresa", sa.Boolean, nullable=False, default=False),
        sa.CheckConstraint("LENGTH(telefone) = 11", name="ck_cliente_telefone_length"),
    )

    if create_seed:
        clientes = [
            {
                "nome": "Cliente 1",
                "telefone": "62999999999",
                "empresa": "Empresa 1",
                "e_empresa": True,
            },
            {
                "nome": "Cliente 2",
                "telefone": "62988888888",
                "empresa": "Empresa 2",
                "e_empresa": True,
            },
            {
                "nome": "Cliente 3",
                "telefone": "62977777777",
                "empresa": "Empresa 3",
                "e_empresa": True,
            },
            {
                "nome": "Cliente 4",
                "telefone": "62966666666",
                "empresa": None,
                "e_empresa": False,
            },
            {
                "nome": "Cliente 5",
                "telefone": "62955555555",
                "empresa": None,
                "e_empresa": False,
            },
        ]

        try:
            op.bulk_insert(tabela, clientes)
        except Exception as e:
            op.drop_table("clientes")
            raise e


def downgrade() -> None:
    op.drop_table("clientes")
