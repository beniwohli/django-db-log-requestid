from django.conf import settings
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from django_query_commenter import local, defaults

HEADER_NAME = settings.get('QUERY_COMMENTER_HEADER_NAME', defaults.REQUEST_ID_HEADER_NAME)

class QueryCommenterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        local.request_id = request.META.get(HEADER_NAME, None)

    def process_response(self, request, response):
        if hasattr(local, 'request_id'):
            del local.request_id
        return response
