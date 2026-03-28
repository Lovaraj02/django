from django.db import models

# Create your models here.

'''Task 1

Create Employee model:
    name
    salary
    department
'''

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    salary = models.IntegerField()
    department = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.age} - {self.salary} - {self.department} - {self.is_active}"
    


