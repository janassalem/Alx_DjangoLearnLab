# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books, 
    LibraryDetailView, 
    register, 
    librarian_view, 
    admin_view, 
    add_book, 
    edit_book
)

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),

    # Book and Library URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Librarian and Admin URLs
    path('librarian/', librarian_view, name='librarian_view'),
    path('admin/', admin_view, name='admin_view'),
    path('admin-dashboard/', admin_view, name='admin_dashboard'),  # Use the same view if the template differs

    # Book Management URLs
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    
    # Other URLs can be added here
]
