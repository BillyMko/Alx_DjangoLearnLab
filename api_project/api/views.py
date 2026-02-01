from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAdminUser

class BookViewSet(viewsets.ModelViewSet):
    # Handles CRUD operations for Book model.

    # Authentication:
    #     - TokenAuthentication required.
    # Permissions:
    #     - Authenticated users can list, create, update.
    #     - Only admins can delete.

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
