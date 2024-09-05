
from django.urls import path
from .views import BookListView
from .views import BookListCreateView, BookRetrieveUpdateDestroyView
from .views import (
    BookListView,
    BookDetailView,
    BookListCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
     # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookListCreateView.as_view(), name='book-create'),

    # Update a book by ID
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book by ID
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

