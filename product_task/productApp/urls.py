from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductView

router = DefaultRouter()

router.register('product',ProductView)

urlpatterns = [
    path('',include(router.urls))
]