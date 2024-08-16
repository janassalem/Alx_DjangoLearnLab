from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

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
