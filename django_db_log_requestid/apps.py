from django.apps.config import AppConfig
from django.core.signals import request_started, request_finished

from django_db_log_requestid import listeners


class DBLogRequestIDConfig(AppConfig):
    name = 'django_db_log_requestid'

    def ready(self):
        request_started.connect(listeners.handle_request_started,
                                dispatch_uid='db-log-request-id-request-started')
        request_finished.connect(listeners.handle_request_finished,
                                 dispatch_uid='db-log-request-id-request-finished')