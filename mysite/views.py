from django.http import HttpResponse , JsonResponse


def http_test(request):
    return HttpResponse('<h1>"HELLO First HTTP_TEST created by SABER"</h1>')

def json_test(request):
    return JsonResponse({'name' : 'Saber SASA'})