# blog/views.py
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
# blog/views.py

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirect to the profile page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})


# blog/views.py
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'blog/profile.html')
