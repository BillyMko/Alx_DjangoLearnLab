from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser 
from django.contrib.auth import get_user_model

from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    search_fields = ('title', 'author')                     # Search by title or author
    list_filter = ('publication_year',)                     # Filter by publication year

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    ordering = ('email',)

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
