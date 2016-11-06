from django.http.response import HttpResponse

from tests.testapp.models import Thing


def test_orm_create_view(request):
    Thing.objects.create(foo='bar')
    return HttpResponse()


def test_raw_query_view(request):
    l = list(Thing.objects.raw('SELECT * from testapp_thing'))
    return HttpResponse(len(l))