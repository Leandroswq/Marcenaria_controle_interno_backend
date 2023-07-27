"""custos_de_terceiros

Revision ID: a08fa91e79df
Revises: 15f9b0ba2955
Create Date: 2023-07-26 17:26:29.885363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a08fa91e79df"
down_revision = "15f9b0ba2955"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "custos_de_terceiros",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("descricao", sa.String(255), nullable=False),
        sa.Column("valor", sa.Numeric(10, 2), nullable=False),
        sa.Column(
            "responsavel_contato",
            sa.Integer,
            sa.ForeignKey("parceiros.id"),
            nullable=False,
        ),
        sa.Column("quantidade", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("custos_de_terceiros")
