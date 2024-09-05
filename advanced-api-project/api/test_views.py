from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a Book instance
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2024-01-01'
        )
        self.url = '/api/books/'  # Adjust URL based on your endpoint

    def test_create_book(self):
        response = self.client.post(self.url, {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2024-02-01'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_read_book(self):
        response = self.client.get(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        response = self.client.put(f'{self.url}{self.book.id}/', {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'published_date': '2024-03-01'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test filtering, searching, and ordering
    def test_filter_books(self):
        response = self.client.get(self.url, {'author': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_permission_denied(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create a Book instance
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2024-01-01'
        )
        self.url = '/api/books/'  # Adjust URL based on your endpoint

    def test_create_book(self):
        response = self.client.post(self.url, {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2024-02-01'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_read_book(self):
        response = self.client.get(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        response = self.client.put(f'{self.url}{self.book.id}/', {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'published_date': '2024-03-01'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(f'{self.url}{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test filtering, searching, and ordering
    def test_filter_books(self):
        response = self.client.get(self.url, {'author': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_permission_denied(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

