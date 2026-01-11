from .models import Book


from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    search_fields = ('title', 'author')                     # Search by title or author
    list_filter = ('publication_year',)                     # Filter by publication year

admin.site.register(Book, BookAdmin)
