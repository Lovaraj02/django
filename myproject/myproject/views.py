# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.shortcuts import render


# def myres(request):
#     return HttpResponse("<h1>hello django</h1>")

# def home(request):
#     return HttpResponse("this is home")

# def jsnres(request):
#     # data = {'name':'raj'}
#     return JsonResponse({'name': 'raju'})

# def render_fun(request):
#     return render(request, 'home.html')


# *****  Task-1 *****

'''Task 1 — Basic Routing (Foundation)

    Create 3 pages:

    / → "Home Page"
    /about/ → "About Page"
    /contact/ → "Contact Page"
'''
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is home page</h1>")

def about(request):
    return HttpResponse("<h1>This is about page</h1>")

def contact(request):
    return HttpResponse('<h1>This is contact page</h1>')



''' Task 2 — Dynamic URL (Must Know)

    Build:
        /user/raju/
        /user/john/

    Output:
        Hello, raju
        Hello, john
'''

def user(request, name,id):
    return HttpResponse(f"Hii im {name} with {id} age")