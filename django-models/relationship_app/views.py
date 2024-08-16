from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from .models import Book, Library, UserProfile
from .forms import BookForm

# Book Views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {"books": books})

@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

@permission_required("relationship_app.can_change_book")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list-books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

@permission_required("relationship_app.can_delete_book")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list-books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

# Library Views
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# Authentication Views
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

# Role-Based Access Control
def check_role(user, role):
    return user.is_authenticated and user.userprofile.role == role

@user_passes_test(lambda user: check_role(user, "Admin"))
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(lambda user: check_role(user, "Librarian"))
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(lambda user: check_role(user, "Member"))
def member_view(request):
    return render(request, "relationship_app/member_view.html")
