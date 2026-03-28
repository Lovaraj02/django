from django.db import models

# Create your models here.
class Employee(models.Model):

    name        = models.CharField(max_length=100)
    age         = models.IntegerField()
    salary      = models.FloatField()
    is_active   = models.BooleanField(default=False)

    def __str__(self):
        return self.name
