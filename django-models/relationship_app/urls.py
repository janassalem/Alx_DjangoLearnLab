from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView, add_book, edit_book, delete_book

from .views import librarian_view, LibrarianView

from . import views
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path("list_books/", list_books, name="list-books"),
    path("library_detail/", LibraryDetailView.as_view(), name="library-detail"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("add_book/", add_book, name="add-book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit-book"),
    path("delete_book/<int:book_id>/", delete_book, name="delete-book"),
    path('librarian/', librarian_view, name='librarian-view'),  # Function-based view
    path('librarian/', LibrarianView.as_view(), name='librarian-view'),  # Class-based view
     path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    
]




