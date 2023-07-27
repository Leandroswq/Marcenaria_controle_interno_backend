"""medidas

Revision ID: 2a1d2b765e11
Revises: 4196cb3cd475
Create Date: 2023-07-27 14:16:05.804039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2a1d2b765e11"
down_revision = "4196cb3cd475"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "medidas",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("medida", sa.String(50), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("medidas")
