"""custos_de_terceiros

Revision ID: 4196cb3cd475
Revises: 722a7ae04d39
Create Date: 2023-07-27 14:09:37.491108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4196cb3cd475"
down_revision = "722a7ae04d39"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
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


def downgrade() -> None:
    op.drop_table("custos_de_terceiros")
