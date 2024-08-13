from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import register
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from .models import Library

from django.shortcuts import render
from relationship_app.models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from relationship_app.models import Library

class LibraryDetailView(DetailView):
   class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


   from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.views.generic import ListView, DetailView
from .models import Book, Library

class ListBooksView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render

def register(request):
    return render(request, 'relationship_app/register.html')
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')
from django.http import HttpResponseForbidden
from django.shortcuts import render

def admin_view(request):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return HttpResponseForbidden("You are not allowed to access this page.")
    return render(request, 'relationship_app/admin_dashboard.html')
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    # Code to add a book
    pass

@permission_required('relationship_app.can_change_book')
def change_book_view(request):
    # Code to change a book
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book_view(request):
    # Code to delete a book
    pass

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book  # Assuming you have a Book model
from .forms import BookForm  # Assuming you have a form for Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view')  # Replace 'some_view' with your redirect target
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('some_view')  # Replace 'some_view' with your redirect target
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book  # Assuming you have a Book model
from .forms import BookForm  # Assuming you have a form for Book

@permission_required('relationship_app.add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view')  # Replace 'some_view' with your redirect target
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('some_view')  # Replace 'some_view' with your redirect target
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})
