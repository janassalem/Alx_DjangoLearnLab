from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(user_is_librarian)
def librarian_view(request):
    # Add logic for librarian content here
    return render(request, 'relationship_app/librarian_view.html')
