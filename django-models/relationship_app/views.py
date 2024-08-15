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
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books(request):
    books = Book.objects.all()
    list_book = [f"{book.title} by {book.author}" for book in books]
    return render(request, 'relationship_app/list_books.html', {'list_book': list_book})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.userprofile.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have access to this page.")
        return _wrapped_view
    return decorator

@role_required('Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

@role_required('Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@role_required('Member')
def member_view(request):
    return render(request, 'member_view.html')
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def admin_check(user):
    return user.userprofile.role == 'Admin'

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(admin_check)
def admin_view(request):
    return HttpResponse("Welcome Admin! You have special access to this view.")

@user_passes_test(librarian_check)
def librarian_view(request):
    return HttpResponse("Welcome Librarian! You have access to librarian resources.")

@user_passes_test(member_check)
def member_view(request):
    return HttpResponse("Welcome Member! You can view general content.")
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'member_view.html')

