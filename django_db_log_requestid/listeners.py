from django_db_log_requestid import utils


def handle_request_started(signal, sender, environ, **kwargs):
    utils.set_request_id(environ.get(utils.get_meta_key_name(), None))


def handle_request_finished(signal, sender, **kwargs):
    utils.clear_request_id()


