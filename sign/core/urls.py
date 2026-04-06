from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterApiView, ProductModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register('product',ProductModelViewSet)

urlpatterns = [
    path('signup/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('',include(router.urls))
]