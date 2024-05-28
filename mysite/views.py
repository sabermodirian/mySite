from django.http import HttpResponse


def http_test(request):
    return HttpResponse('<h1>"HELLO First HTTP_TEST that created by SABER"</h1>')