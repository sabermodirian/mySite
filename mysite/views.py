from django.http import HttpResponse


def http_test(request):
    return HttpResponse("HELLO First HTTP_TEST that created by SABER")