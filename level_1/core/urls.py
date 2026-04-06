# modelviewset reat world
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register('book', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]







# genericks
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('create-add/', views.CreateAddView.as_view()),
#     path('update-delete/<int:pk>/', views.UpdateDeleteView.as_view())
# ]