from django.urls import path,include
from .views import RegisterApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]