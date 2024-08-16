from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView, add_book, edit_book, delete_book

urlpatterns = [
    path("list_books/", list_books, name="list-books"),
    path("library_detail/", LibraryDetailView.as_view(), name="library-detail"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("add_book/", add_book, name="add-book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit-book"),
    path("delete_book/<int:book_id>/", delete_book, name="delete-book"),
]

from django.urls import path
from . import views

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
