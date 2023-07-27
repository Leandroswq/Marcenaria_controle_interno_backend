"""clientes

Revision ID: fe04d9ecc88b
Revises: 26a2c5adbc2b
Create Date: 2023-07-27 09:55:04.916620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fe04d9ecc88b"
down_revision = "26a2c5adbc2b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "clientes",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_Nome", sa.String(100)),
        sa.Column("telefone", sa.VARCHAR(11), nullable=False),
        sa.Column("empresa", sa.String(50), nullable=False),
        sa.Column("e_empresa", sa.Boolean, nullable=False, default=False),
        sa.Column("pais", sa.String(50), nullable=False),
        sa.Column("estado", sa.String(50), nullable=False),
        sa.Column("cidade", sa.String(50), nullable=False),
        sa.Column("bairro", sa.String(50), nullable=False),
        sa.Column("endereco", sa.String(100), nullable=False),
        sa.Column("complemeto", sa.String(150)),
        sa.Column("cep", sa.VARCHAR(8), nullable=False),
        sa.CheckConstraint(
            "LENGTH(telefone) = 11", name="ck_cliente_telefone_length"
        ),
        sa.CheckConstraint("LENGTH(cep) = 8", name="ck_cep_length"),
    )


def downgrade() -> None:
    op.drop_table("clientes")
