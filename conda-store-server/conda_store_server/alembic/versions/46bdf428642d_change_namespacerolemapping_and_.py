"""Change NamespaceRoleMapping and Namespace

Revision ID: 46bdf428642d
Revises: b387747ca9b7
Create Date: 2023-10-08 10:40:06.227854

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "46bdf428642d"
down_revision = "b387747ca9b7"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "namespace_role_mapping_new",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("namespace_id", sa.Integer(), nullable=False),
        sa.Column("other_namespace_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.Unicode(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["namespace_id"],
            ["namespace.id"],
        ),
        sa.ForeignKeyConstraint(
            ["other_namespace_id"],
            ["namespace.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("namespace_id", "other_namespace_id", name="_uc"),
    )
    # Note: data is NOT copied before dropping the old table
    op.drop_table("namespace_role_mapping")
    op.rename_table("namespace_role_mapping_new", "namespace_role_mapping")


def downgrade():
    op.create_table(
        "namespace_role_mapping_new",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("namespace_id", sa.Integer(), nullable=False),
        sa.Column("entity", sa.Unicode(length=255), nullable=False),
        sa.Column("role", sa.Unicode(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["namespace_id"],
            ["namespace.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # Note: data is NOT copied before dropping the old table
    op.drop_table("namespace_role_mapping")
    op.rename_table("namespace_role_mapping_new", "namespace_role_mapping")
