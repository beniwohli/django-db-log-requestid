from django.conf.urls import url

from tests.testapp import views

urlpatterns = [
    url(r'^test_orm_create/$', views.test_orm_create_view, name='test'),
    url(r'^test_raw_query/$', views.test_raw_query_view, name='test'),
]