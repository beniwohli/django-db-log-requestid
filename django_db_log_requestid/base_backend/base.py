import logging

from django.db.backends import utils as backend_utils
from django.conf import settings

from django_db_log_requestid import utils, defaults


logger = logging.getLogger('django_db_log_requestid')


class DBLogRequestIdCursorWrapperMixin(object):
    def execute(self, sql, params=None):
        sql = self._append_request_id_comment(sql)
        result = super(DBLogRequestIdCursorWrapperMixin, self).execute(sql, params=params)
        if getattr(settings, 'REQUEST_ID_ENABLE_LOGGING', defaults.REQUEST_ID_ENABLE_LOGGING):
            logger.info(sql, extra={'params': params})
        return result

    def executemany(self, sql, param_list):
        sql = self._append_request_id_comment(sql)
        result = super(DBLogRequestIdCursorWrapperMixin, self).executemany(sql, param_list)
        if getattr(settings, 'REQUEST_ID_ENABLE_LOGGING', defaults.REQUEST_ID_ENABLE_LOGGING):
            logger.info(sql, extra={'param_list': param_list})
        return result

    def _append_request_id_comment(self, sql):
        template = getattr(settings,
                           'REQUEST_ID_SQL_TEMPLATE',
                           defaults.REQUEST_ID_SQL_TEMPLATE)
        request_id = utils.get_request_id()
        if request_id:
            sql = template.format(sql=sql, request_id=request_id)
        return sql


class CursorWrapper(DBLogRequestIdCursorWrapperMixin, backend_utils.CursorWrapper):
    pass


class CursorDebugWrapper(DBLogRequestIdCursorWrapperMixin, backend_utils.CursorDebugWrapper):
    pass


class DBLogRequestIdDatabaseWrapperMixin(object):
    def make_cursor(self, cursor):
        return CursorWrapper(cursor, self)

    def make_debug_cursor(self, cursor):
        return CursorDebugWrapper(cursor, self)
