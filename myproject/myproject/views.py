from django.http import HttpResponse

def myres(request):
    return HttpResponse("hello django")