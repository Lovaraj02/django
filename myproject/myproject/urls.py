"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.myres),
    # path('home/', views.home),
    # path('res/', views.jsnres),
    path('rend/', views.render_fun),


    # *** Task-1 urls ***
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),


    # *** Task-2 urls ***
    path('user/<str:name>/<int:id>', views.user),
    # path('user/<str:name>', views.user)


    # *** Task-3 urls ***
    path('calculator/<int:n1>/<int:n2>', views.calculator),


    # task-4
    path('all-students', views.get_students),
    path('single-student/<int:id>', views.single_student),
    path('new-student/<str:name>', views.new_student),

    # task-5
    path('find/<str:name>', views.findnadreturn),



    # Models urls from model_practice App
    path('emp/', include('model_practice.urls'))

]
