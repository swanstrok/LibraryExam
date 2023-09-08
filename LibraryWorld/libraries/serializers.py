from rest_framework import serializers

from .models import Book, Library


class LibrarySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Library"""

    class Meta:
        model = Library
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Book"""

    class Meta:
        model = Book
        fields = '__all__'
