from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Book
from .seriealizers import BookSerializer

# List all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve a book by ID
class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Update a book by ID
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Additional logic during update
        if not serializer.validated_data.get('title'):
            raise ValidationError('Title cannot be empty.')
        
        # Save the updated book instance
        serializer.save()

# Delete a book by ID
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        # Additional logic before deletion
        if instance.is_important:  # Example condition
            raise ValidationError('Important books cannot be deleted.')
        
        # Perform the deletion
        instance.delete()

# Combined Retrieve, Update, or Delete a book by ID
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Additional logic during update
        if not serializer.validated_data.get('title'):
            raise ValidationError('Title cannot be empty.')

        # Example: Only allow the 'published_date' to be updated if the book is already marked as published
        if 'published_date' in serializer.validated_data:
            book = self.get_object()
            if not book.is_published:
                raise ValidationError('Cannot update published date for an unpublished book.')

        # Save the updated book instance
        serializer.save()

    def perform_destroy(self, instance):
        # Additional logic before deletion
        if instance.is_important:
            raise ValidationError('Important books cannot be deleted.')
        
        # Perform the deletion
        instance.delete()
