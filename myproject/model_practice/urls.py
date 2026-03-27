from django.urls import path
from .views import display_all_emp

urlpatterns = [
    path('', display_all_emp)
]