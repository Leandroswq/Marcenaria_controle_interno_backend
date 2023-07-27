"""produtos

Revision ID: d8ddfc52c0fa
Revises: 26a2c5adbc2b
Create Date: 2023-07-26 21:35:19.482249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d8ddfc52c0fa"
down_revision = "a08fa91e79df"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "produtos",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("produto", sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("produtos")
