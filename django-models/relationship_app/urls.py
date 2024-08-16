from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView, add_book, edit_book, delete_book

from .views import librarian_view, LibrarianView

from . import views
urlpatterns = [
    path("relationship_app/list_books/", list_books, name="list-books"),
    path("relationship_app/library_detail/", LibraryDetailView.as_view(), name="library-detail"),
    path("relationship_app/register/", register, name="register"),
    path("relationship_app/login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("relationship_app/logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("relationship_app/add_book/", add_book, name="add-book"),
    path("relationship_app/edit_book/<int:book_id>/", edit_book, name="edit-book"),
    path("relationship_app/delete_book/<int:book_id>/", delete_book, name="delete-book"),
    path('relationship_app/librarian/', librarian_view, name='librarian-view'),  # Function-based view
    path('relationship_app/librarian/', LibrarianView.as_view(), name='librarian-view'),  # Class-based view
]



urlpatterns = [
    path("list_books/", views.list_books, name="list-books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library-detail"),
    path("register/", views.register, name="register"),
    path("login/", views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("add_book/", views.add_book, name="add-book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit-book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete-book"),
]

