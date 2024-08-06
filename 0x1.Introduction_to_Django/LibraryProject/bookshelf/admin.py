from django.contrib import admin # type: ignore
from .models import Book

admin.site.register(Book)
