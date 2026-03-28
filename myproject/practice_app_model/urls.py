from django.urls import path
from . import views
urlpatterns = [
    path('get/',views.get_all),
    path('name/',views.create_api),

]