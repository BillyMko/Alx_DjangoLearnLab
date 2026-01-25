from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    # Question 1 views (THIS IS WHAT THE ERROR IS ABOUT)
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]

