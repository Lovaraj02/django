from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

from .models import Employee

def get_all(request):
    x = Employee.objects.all()
    print(x)
    return JsonResponse({"all_emp": "working"})


# task-1
def create_api(request):
    name = request.GET.get("name")
    return JsonResponse({
        "message": f"hello {name}"
        })

