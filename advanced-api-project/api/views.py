from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.exceptions import ValidationError


# List all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a book by ID
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # Custom validation logic
        if Book.objects.filter(title=serializer.validated_data['title']).exists():
            raise ValidationError('A book with this title already exists.')
        serializer.save()
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        # Additional logic during update

        # Example 1: Prevent empty title
        if not serializer.validated_data.get('title'):
            raise ValidationError('Title cannot be empty.')

        # Example 2: Only allow the 'published_date' to be updated if the book is already marked as published
        if 'published_date' in serializer.validated_data:
            book = self.get_object()
            if not book.is_published:
                raise ValidationError('Cannot update published date for an unpublished book.')

        # Save the updated book instance with any modifications applied
        serializer.save()
    def perform_update(self, serializer):
        # Additional logic during update
        if not serializer.validated_data.get('title'):
            raise ValidationError('Title cannot be empty.')
        
        # Save the updated book instance
        serializer.save()

    def perform_delete(self, instance):
        # Additional logic before deletion
        if instance.is_important:  # Example condition
            raise ValidationError('Important books cannot be deleted.')
        
        # Perform the deletion
        instance.delete()


