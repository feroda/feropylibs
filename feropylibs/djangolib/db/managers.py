
import copy
from django.db import models

from django.conf import settings

class MultischemaManager(models.Manager):
    """
    Manager with dynamic multischema facility
    if using the db.backends.postgresql_psycopg2_multischema
    """

    def using(self, db_alias, template={'backend': 'psycopg2'}):

        if not settings.DATABASES.get(db_alias):
            if template['backend'] == 'psycopg2':
                settings.DATABASES[db_alias] = copy.copy(settings.DATABASES[template.get('originate_from', 'default')])
                settings.DATABASE_SCHEMAS[db_alias] = db_alias
            elif template['backend'] == 'sqlite3':
                dbconf = copy.copy(settings.DATABASES[template['originate_from']])
                if 'NAME' in template:
                    dbconf['NAME'] = template['NAME']
                settings.DATABASES[db_alias] = dbconf

        return super(MultischemaManager, self).using(db_alias)


