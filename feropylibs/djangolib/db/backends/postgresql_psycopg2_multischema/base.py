
import django

from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper
from django.conf import settings

class DatabaseWrapper(DatabaseWrapper):
    """PostgreSQL wrapper that honours database schema.

    It uses the database alias to find a correspondance
    of the alias and the schema name in the `DATABASE_SCHEMAS` setting.

    Then uses "SET search_path TO" PostgreSQL facility when it
    gets the cursor

    """

    if (django.VERSION < (1, 8)):

        def _cursor(self):
            cursor = super(DatabaseWrapper, self)._cursor()
            db_schema = settings.DATABASE_SCHEMAS.get(self.alias)
            if db_schema:
                cursor.execute("SET search_path TO \"%s\";" % db_schema)
            return cursor

    else:
        # For Django 1.11
        def create_cursor(self, name=None):
            cursor = super(DatabaseWrapper, self).create_cursor()
            db_schema = settings.DATABASE_SCHEMAS.get(self.alias)
            if db_schema:
                # DEBUG print(db_schema)
                cursor.execute("SET search_path TO \"%s\";" % db_schema)
            return cursor

