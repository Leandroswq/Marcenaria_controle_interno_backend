"""funcionarios

Revision ID: 2d700beed168
Revises: 26b013b4f7b5
Create Date: 2023-07-27 14:08:07.269639

"""
from alembic import op
import sqlalchemy as sa

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "2d700beed168"
down_revision = "26b013b4f7b5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "funcionarios",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_nome", sa.String(100)),
        sa.Column("funcao", sa.String(50), nullable=False),
        sa.Column("telefone", sa.VARCHAR(11), nullable=False),
        sa.CheckConstraint(
            "LENGTH(telefone) = 11", name="ck_funcionarios_telefone_length"
        ),
    )

    if create_seed:
        funcionarios = [
            {
                "nome": "João",
                "sobre_nome": "Silva",
                "funcao": "Analista",
                "telefone": "91122334455",
            },
            {
                "nome": "Maria",
                "sobre_nome": "Santos",
                "funcao": "Gerente",
                "telefone": "95566778899",
            },
            {
                "nome": "Pedro",
                "sobre_nome": None,
                "funcao": "Desenvolvedor",
                "telefone": "99988776655",
            },
        ]
        try:
            op.bulk_insert(tabela, funcionarios)
        except Exception as e:
            op.drop_table("funcionarios")
            raise e


def downgrade() -> None:
    op.drop_table("funcionarios")
