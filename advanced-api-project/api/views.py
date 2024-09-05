from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
    

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Include OrderingFilter here
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']  # Specify fields that can be ordered
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve a book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# List all books or create a new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Custom validation logic
        if Book.objects.filter(title=serializer.validated_data['title']).exists():
            raise ValidationError('A book with this title already exists.')
        serializer.save()

# Retrieve, update, or delete a book by ID
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

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']

    def perform_create(self, serializer):
        if Book.objects.filter(title=serializer.validated_data['title']).exists():
            raise ValidationError('A book with this title already exists.')
        serializer.save()


