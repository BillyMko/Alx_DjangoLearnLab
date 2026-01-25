from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from .views import   LibraryDetailView
from .views import (
    register,
    admin_view,
    librarian_view,
    member_view,
)


urlpatterns = [
    
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

   
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

  
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]

