from __future__ import absolute_import
import pytest
from django.test.utils import override_settings

from tests.testapp.models import Thing

pytestmark = pytest.mark.django_db


def test_simple_query(client, caplog):
    client.get('/test_orm_create/', HTTP_X_REQUEST_ID='foo')
    assert ' -- request_id=foo' in caplog.records[-1].message


def test_query_with_newlines(client, caplog):
    client.get('/test_raw_query/', HTTP_X_REQUEST_ID='foo')
    assert ' -- request_id=foo' in caplog.records[-1].message


def test_signal_handling(client, caplog):
    with override_settings(
            MIDDLEWARE_CLASSES=[],
            INSTALLED_APPS=['tests.testapp', 'django_db_log_requestid']):
        client.get('/test_orm_create/', HTTP_X_REQUEST_ID='foo')
        assert ' -- request_id=foo' in caplog.records[-1].message