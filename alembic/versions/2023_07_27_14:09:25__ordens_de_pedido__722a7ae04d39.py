"""ordens_de_pedido

Revision ID: 722a7ae04d39
Revises: 4bed0f6d1585
Create Date: 2023-07-27 14:09:25.336193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "722a7ae04d39"
down_revision = "4bed0f6d1585"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
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
        sa.Column("Data prevista", sa.DateTime, nullable=False),
        sa.Column("Termino", sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("ordens_de_pedido")
