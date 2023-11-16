"""default users

Revision ID: b7bab10d732e
Revises: 2eaa76eb09a3
Create Date: 2023-11-17 00:03:09.407158

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete
from sqlalchemy.sql import table, column
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b7bab10d732e'
down_revision = '2eaa76eb09a3'
branch_labels = None
depends_on = None


def upgrade():
    users_table = table(
        "user",
        column("id", postgresql.UUID(as_uuid=True)),
        column("name", sa.String),
    )
    
    op.bulk_insert(
        users_table,
        [
            {
                "id": "c449c8d9-32cc-470c-b479-c63add1efb88",
                "name": "Default user",
            }
        ],
    )


def downgrade():
    users_table = table(
        "user",
        column("id", postgresql.UUID(as_uuid=True)),
        column("name", sa.String),
    )

    connection = op.get_bind()

    connection.execute(
        delete(users_table).where(users_table.c.id == "c449c8d9-32cc-470c-b479-c63add1efb88")
    )

