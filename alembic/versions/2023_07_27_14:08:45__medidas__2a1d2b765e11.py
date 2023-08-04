"""medidas

Revision ID: 2a1d2b765e11
Revises: 91dc3de1abd2
Create Date: 2023-07-27 14:08:45.804039

"""
from alembic import op
import sqlalchemy as sa

import os

create_seed = True if os.getenv("ALEMBIC_CREATE_SEEDS") == "True" else False

# revision identifiers, used by Alembic.
revision = "2a1d2b765e11"
down_revision = "91dc3de1abd2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    tabela = op.create_table(
        "medidas",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("medida", sa.String(50), nullable=False, unique=True),
        sa.Column(
            "unidade",
            sa.Enum(
                "distancia",
                "volume",
                "tempo",
                "peso",
                "temperatura",
                "unidade",
                name="unidade_enum",
            ),
            nullable=False,
        ),
    )

    if create_seed:
        medidas = [
            {"medida": "metro", "unidade": "distancia"},
            {"medida": "unidade", "unidade": "unidade"},
            {"medida": "litro", "unidade": "volume"},
        ]
        try:
            op.bulk_insert(tabela, medidas)
        except Exception as e:
            op.drop_table("medidas")
            raise e


def downgrade() -> None:
    op.drop_table("medidas")
