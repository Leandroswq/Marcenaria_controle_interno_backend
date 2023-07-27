"""ordens_de_pedido

Revision ID: e470351833fa
Revises: fe04d9ecc88b
Create Date: 2023-07-27 11:18:47.520181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e470351833fa"
down_revision = "fe04d9ecc88b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "ordem_de_pedido",
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
    op.drop_table("ordem_de_pedido")
