from django.shortcuts import render

# Create your views here.
from .models import Employee


''' ORM Practice (Important)
Task 3: Filtering

Using Employee model:

Get employees with salary > 30000
Get employees with age < 25
Check if any employee exists with name = "Raju"'''

def display_all_emp(request):

    # employees = Employee.objects.all()
    salary = Employee.objects.filter(salary__gt = 30000)
    age = Employee.objects.filter(age__lt = 20)
    name_exists = Employee.objects.filter(name = "kusaraju").exists()
    return render(request, 'emp.html', {
        'salary':salary, 
        'age':age, 
        'name_exists': name_exists
        })
