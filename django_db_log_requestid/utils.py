from django.conf import settings

from django_db_log_requestid import defaults, local


def set_request_id(request_id):
    local.request_id = request_id


def get_request_id():
    return getattr(local, 'request_id', None)


def clear_request_id():
    if hasattr(local, 'request_id'):
        del local.request_id


def get_meta_key_name():
    header_name = getattr(settings, 'QUERY_COMMENTER_HEADER_NAME',
                          defaults.REQUEST_ID_HEADER_NAME)

    # turn header name into Django META key
    return 'HTTP_' + header_name.upper().replace('-', '_')
