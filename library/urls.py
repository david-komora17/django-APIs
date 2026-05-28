from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# Define urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
