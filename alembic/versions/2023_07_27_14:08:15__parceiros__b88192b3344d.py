"""parceiros

Revision ID: b88192b3344d
Revises: 2d700beed168
Create Date: 2023-07-27 14:08:15.212120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b88192b3344d"
down_revision = "2d700beed168"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "parceiros",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_Nome", sa.String(100)),
        sa.Column("empresa", sa.String(50), nullable=True),
        sa.Column("e_empresa", sa.Boolean, nullable=False, default=False),
        sa.Column("telefone", sa.VARCHAR(11), nullable=False),
        sa.CheckConstraint(
            "LENGTH(telefone) = 11", name="ck_parceiros_telefone_length"
        ),
    )


def downgrade() -> None:
    op.drop_table("parceiros")