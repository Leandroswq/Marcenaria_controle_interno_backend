"""produtos

Revision ID: 4bed0f6d1585
Revises: 91dc3de1abd2
Create Date: 2023-07-27 14:08:50.555601

"""
from alembic import op
import sqlalchemy as sa

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "4bed0f6d1585"
down_revision = "91dc3de1abd2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "produtos",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("produto", sa.String(50), nullable=False, unique=True),
        sa.Column(
            "categoria",
            sa.Integer,
            sa.ForeignKey("categorias_de_produto.id"),
            nullable=False,
        ),
    )

    if create_seed:
        produtos = [
            {"produto": "pinus", "categoria": 1},
            {"produto": "furadeira", "categoria": 2},
            {"produto": "broca 8", "categoria": 3},
        ]
        try:
            op.bulk_insert(tabela, produtos)
        except Exception as e:
            op.drop_table("produtos")
            raise e


def downgrade() -> None:
    op.drop_table("produtos")
