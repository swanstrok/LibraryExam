from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from rest_framework.filters import SearchFilter

from .models import Book, Library
from .serializers import BookSerializer, LibrarySerializer


# Create your views here.

class LibraryAPIViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'address']

    def get_queryset(self):
        queryset = Library.objects.all()
        return queryset


class BookAPIViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ('title', 'genre', 'author')

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
