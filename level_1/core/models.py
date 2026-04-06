from django.db import models

# Create your models here.

'''LEVEL 1 — Core CRUD + Validation (foundation)
Task 1: Book Management API
Model: title, author price, created_at,

Requirements: Create book, Get all books, Update book, Delete book, Add constraints, price must be > 0, title cannot be empty'''

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
