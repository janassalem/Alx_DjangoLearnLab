from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

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
    book = Book.objects.get(id=book_id)
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
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list-books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

def list_books(request):
  books = Book.objects.all()
  context = {"books": books}
  return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(ListView):
  model = Library
  context_object_name = "library"
  template_name = "relationship_app/library_detail.html"
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library"] = Library.objects.all()
        return context

def register(request):
  if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
  else:
      form = UserCreationForm()
  return render(request, "relationship_app/register.html", {"form": form})

class LoginView(LoginView):
    template_name = "login.html"

class LogoutView(LogoutView):
    template_name = "logout.html"


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
# relationship_app/views.py
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import UserProfile

# Function-based view example
@login_required
def librarian_view(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'Librarian':
        # Logic for Librarian view
        return render(request, 'relationship_app/librarian_view.html')
    else:
        return HttpResponseForbidden("You are not authorized to view this page.")

# Class-based view example
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class LibrarianRequiredMixin(UserPassesTestMixin, LoginRequiredMixin):
    def test_func(self):
        return hasattr(self.request.user, 'userprofile') and self.request.user.userprofile.role == 'Librarian'

class LibrarianView(LibrarianRequiredMixin, TemplateView):
    template_name = 'relationship_app/librarian_view.html'

 # relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def librarian_required(view_func):
    return user_passes_test(lambda u: u.userprofile.role == 'Librarian')(view_func)

@librarian_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian.html')
def book_list(request):
    form = BookForm()
    return render(request, 'relationship_app/book_list.html', {'form': form})


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
<<<<<<< HEAD


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_template.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_template.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_template.html')
=======
>>>>>>> 011d79bfd636f1e16c9774636f46f60d0e5daa82
