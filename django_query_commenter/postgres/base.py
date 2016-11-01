
from django.db.backends.postgresql_psycopg2 import base
from django.db.backends import utils

from django_query_commenter import local


class CommenterCursorWrapperMixin(object):
    def execute(self, sql, params=None):
        if getattr(local, 'request_id', None):
            sql = '%s -- %s' % (sql, local.request_id)
        return super(CommenterCursorWrapperMixin, self).execute(sql, params=params)

    def executemany(self, sql, param_list):
        if getattr(local, 'request_id', None):
            sql = '%s -- %s' % (sql, local.request_id)
        return super(CommenterCursorWrapperMixin, self).executemany(sql, param_list)


class CursorWrapper(CommenterCursorWrapperMixin, utils.CursorWrapper):
    pass


class CursorDebugWrapper(CommenterCursorWrapperMixin, utils.CursorDebugWrapper):
    pass


class DatabaseWrapper(base.DatabaseWrapper):
    def make_cursor(self, cursor):
        return CursorWrapper(cursor, self)

    def make_debug_cursor(self, cursor):
        return CursorDebugWrapper(cursor, self)
