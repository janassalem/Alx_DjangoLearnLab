# views.py

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView

from .models import Book, Library
from .forms import BookForm  # Assuming you have a form for Book

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Book List View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Book Add View
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

# Book Edit View
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

# Librarian View
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Admin View
def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Admin Dashboard View with Authentication Check
def admin_dashboard_view(request):
    if not request.user.is_authenticated or request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You are not allowed to access this page.")
    return render(request, 'relationship_app/admin_dashboard.html')

# Library Detail View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Assuming Library has a relationship with Book
        return context

# List Books with Detail View
class ListBooksView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'
