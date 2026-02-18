from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']


    def validate_publication_year(self, value):
        """
        Function ensures that publication_year is valid
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Invalid publication year")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']