from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from .forms import ExampleForm  # Ensure this form is defined in forms.py
# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def view_content(request):
    # View logic here
    return render(request, 'bookshelf/view_content.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_content(request):
    # Create logic here
    return render(request, 'bookshelf/create_content.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_content(request):
    # Edit logic here
    return render(request, 'bookshelf/edit_content.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_content(request):
    # Delete logic here
    return render(request, 'bookshelf/delete_content.html')
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def book_list(request):
    # Securely querying all books from the database
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

def book_list(request):
    # Securely querying all books from the database
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list after successful submission
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})
