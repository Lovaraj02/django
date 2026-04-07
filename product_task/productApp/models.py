from django.db import models

# -------- Product Model ------------
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
