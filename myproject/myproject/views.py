from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def myres(request):
    return HttpResponse("<h1>hello django</h1>")

def home(request):
    return HttpResponse("this is home")

def jsnres(request):
    return JsonResponse({'name': 'raju'})

def render_fun(request):
    return render(request, 'home.html')