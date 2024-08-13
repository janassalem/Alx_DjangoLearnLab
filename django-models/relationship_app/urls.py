from django.contrib.auth import views as auth_views

from .views import list_books
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
urlpatterns = [
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('admin/', views.admin_view, name='admin_view'),
]
from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin-dashboard'),
]

urlpatterns = [
    path('book/add/', views.add_book_view, name='add_book'),
    path('book/change/', views.change_book_view, name='change_book'),
    path('book/delete/', views.delete_book_view, name='delete_book'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    # Other URL patterns
]
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]