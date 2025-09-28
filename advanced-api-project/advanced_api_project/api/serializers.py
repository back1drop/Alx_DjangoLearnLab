from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    Serializes all fields of the Book model.
    Adds custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Ensure publication year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    Serializes author details and dynamically nests related books.
    Demonstrates handling of one-to-many relationship between Author and Book.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested representation

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
