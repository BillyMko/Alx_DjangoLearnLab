from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from .views import register_view, profile_view, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, CommentCreateView, CommentDeleteView, CommentUpdateView
urlpatterns = [

    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('posts/<int:pk>/comments/new/',CommentCreateView.as_view(),name='comment-create'),
    path('comments/<int:pk>/edit/',CommentUpdateView.as_view(),name='comment-update'),
    path('comments/<int:pk>/delete/',CommentDeleteView.as_view(),name='comment-delete'),




]