try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from django_db_log_requestid import utils


class DatabaseLogRequestIDMiddleware(MiddlewareMixin):
    def process_request(self, request):
        utils.set_request_id(request.META.get(utils.get_meta_key_name(), None))

    def process_response(self, request, response):
        utils.clear_request_id()
        return response
