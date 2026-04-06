from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class SignupUser(AbstractUser):
    email = models.EmailField(unique=True)

    # add if login with email or if u want to login with username dont add
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['useraname']

    def __str__(self):
        return self.email
    
