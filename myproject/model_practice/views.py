from django.shortcuts import render

# Create your views here.
from .models import Employee

def display_all_emp(request):
    employees = Employee.objects.all()
    return render(request, 'emp.html', {'employees':employees})
