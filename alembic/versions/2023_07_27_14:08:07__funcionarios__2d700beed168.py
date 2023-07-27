"""funcionarios

Revision ID: 2d700beed168
Revises: 26b013b4f7b5
Create Date: 2023-07-27 14:08:07.269639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2d700beed168"
down_revision = "26b013b4f7b5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "funcionarios",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_Nome", sa.String(100)),
        sa.Column("funcao", sa.String(50), nullable=False),
        sa.Column("telefone", sa.VARCHAR(11), nullable=False),
        sa.CheckConstraint(
            "LENGTH(telefone) = 11", name="ck_funcionarios_telefone_length"
        ),
    )


def downgrade() -> None:
    op.drop_table("funcionarios")
