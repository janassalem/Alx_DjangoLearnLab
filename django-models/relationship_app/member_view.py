from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def user_is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
