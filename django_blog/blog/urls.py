# blog/urls.py
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register, profile

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Correct URL for update
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]


from django.urls import path
from .views import PostDetailView, PostListView, add_comment, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

from .views import CommentCreateView

urlpatterns = [
    # Other URL patterns...
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    
]


from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView
)

urlpatterns = [
    # Blog post CRUD URLs
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment CRUD URLs
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),  # For creating a comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),  # For updating a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # For deleting a comment
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
]

from .views import search_posts

urlpatterns = [
    # Other URLs...
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', PostListByTagView.as_view(), name='posts-by-tag'),
]

from .views import search_posts

urlpatterns = [
    # Other URL patterns...
    path('search/', search_posts, name='search-posts'),
]
