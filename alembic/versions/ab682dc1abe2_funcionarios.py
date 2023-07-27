"""funcionarios

Revision ID: ab682dc1abe2
Revises: 
Create Date: 2023-07-26 17:06:24.212518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ab682dc1abe2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "funcionarios",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nome", sa.String(50), nullable=False),
        sa.Column("sobre_Nome", sa.String(100)),
        sa.Column("funcao", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("funcionarios")
