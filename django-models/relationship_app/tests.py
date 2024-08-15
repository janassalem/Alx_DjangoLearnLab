from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AdminViewTests(TestCase):
    def setUp(self):
        # Create users with different roles
        self.admin_user = User.objects.create_user(username='admin_user', password='admin_pass')
        self.librarian_user = User.objects.create_user(username='librarian_user', password='librarian_pass')
        self.member_user = User.objects.create_user(username='member_user', password='member_pass')

        # Assign roles to users
        self.admin_user.userprofile.role = 'Admin'
        self.admin_user.userprofile.save()

        self.librarian_user.userprofile.role = 'Librarian'
        self.librarian_user.userprofile.save()

        self.member_user.userprofile.role = 'Member'
        self.member_user.userprofile.save()

    def test_admin_access(self):
        # Login as Admin and check access
        self.client.login(username='admin_user', password='admin_pass')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 200)  # Success

    def test_librarian_access_denied(self):
        # Login as Librarian and check access
        self.client.login(username='librarian_user', password='librarian_pass')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_member_access_denied(self):
        # Login as Member and check access
        self.client.login(username='member_user', password='member_pass')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 403)  # Forbidden
