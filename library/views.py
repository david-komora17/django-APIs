from django.shortcuts import render
from rest_framework import viewsets  # This line fixes the NameError
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book 
from .serializers import BookSerializer

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):

    """
    ViewSet handles full CRUD operations, built in pagination
    and filtering by author or title.
    """
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    filterset_fields = ['title', 'author']
    filter_backends = [DjangoFilterBackend]

