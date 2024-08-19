from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(user_is_admin)
def admin_view(request):
    # Add logic for admin content here
    return render(request, 'relationship_app/admin_view.html')
