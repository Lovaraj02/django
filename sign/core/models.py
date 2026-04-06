from django.db import models
from django.contrib.auth.models import AbstractUser


# ------------Sgnup/login---------------
class User(AbstractUser):
    pass

# --------------Product model------------
class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
