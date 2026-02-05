from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAdminUser

class BookList(generics.ListCreateAPIView):
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
