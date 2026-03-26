from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# def myres(request):
#     return HttpResponse("<h1>hello django</h1>")

# def home(request):
#     return HttpResponse("this is home")

# def jsnres(request):
#     # data = {'name':'raj'}
#     return JsonResponse({'name': 'raju'})

def render_fun(request):
    return render(request, 'home.html')


# # *****  Task-1 *****

# def home(request):
#     return HttpResponse("<h1>This is home page</h1>")

# def about(request):
#     return HttpResponse("<h1>This is about page</h1>")

# def contact(request):
#     return HttpResponse('<h1>This is contact page</h1>')


# # Task-2
# def user(request, name,id):
#     # return HttpResponse("hii im " + name "with " + id "age")
#     return HttpResponse(f"<h1>Hii im {name} with {id} age</h1>")




# # Task-3
# def calculator(request, n1, n2):
#     x = n1+n2
#     return HttpResponse(f"sum of 2 num are:  {x}")


# # taks-4
# # all students
# students = [{"id": 1, "name": "Raju"},{"id": 2, "name": "Balu"},]
# def get_students(request):
#     return JsonResponse(students, safe=False)

# # single student
# def single_student(request, id):
#     for student in students:
#         if student['id'] == id:
#             return JsonResponse(student)
#     return JsonResponse({"error":"student not found"})
            
# # Add new student
# def new_student(request, name):
#     new_id = len(students)+1
#     new_student = {"id":new_id, "name":name}
#     students.append(new_student)
#     return JsonResponse(new_student)


# # task-5
# def findnadreturn(request, name):
#     result = []

#     for student in students:
#         if name.lower() in student["name"].lower():
#             result.append(student)

#     if result:
#         return JsonResponse(result, safe=False)

#     return JsonResponse({"error": "not found"})

