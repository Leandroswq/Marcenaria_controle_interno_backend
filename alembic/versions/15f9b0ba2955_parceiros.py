"""parceiros

Revision ID: 15f9b0ba2955
Revises: ab682dc1abe2
Create Date: 2023-07-26 17:26:16.935232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "15f9b0ba2955"
down_revision = "ab682dc1abe2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "parceiros",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_Nome", sa.String(100)),
        sa.Column("empresa", sa.String(50), nullable=True),
        sa.Column("e_empresa", sa.Boolean, nullable=False, default=False),
        sa.Column("telefone", sa.VARCHAR(11), nullable=False),
        sa.CheckConstraint("LENGTH(telefone) = 11", name="ck_telefone_length"),
    )


def downgrade() -> None:
    op.drop_table("parceiros")
