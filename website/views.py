from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return HttpResponse('<h1>"HELLO First Homepage created by Saber"</h1>')


def about_view(request):
    return JsonResponse({'about': 'sABOUT SABER MODIRIAN'})


def contact_view(request):
    return HttpResponse('<h1>"CONTACT TO First page of website"</h1>')


