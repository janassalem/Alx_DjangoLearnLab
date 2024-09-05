

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2021)

    def test_create_book(self):
        response = self.client.post('/books/', {'title': 'New Book', 'author': 'Author C', 'publication_year': 2022})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 3)

    def test_filter_books_by_author(self):
        response = self.client.get('/books/?author=Author A')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get('/books/?search=Book')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_title(self):
        response = self.client.get('/books/?ordering=title')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'Book One')
