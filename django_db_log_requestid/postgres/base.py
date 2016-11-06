from django.db.backends.postgresql_psycopg2 import base

from django_db_log_requestid.base_backend.base import DBLogRequestIdDatabaseWrapperMixin

class DatabaseWrapper(DBLogRequestIdDatabaseWrapperMixin, base.DatabaseWrapper):
    pass