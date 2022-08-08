# Django
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.views.decorators.cache import cache_control

#Models
from django.contrib.auth.models import User

# Create your views here.
class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'login/login.html'


@login_required
def logout_view(request):
    logout(request)
    return redirect('login:login')

def sign_up(request):

    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation = request.POST['password_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'authentication/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'authentication/signup.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['username']
        user.save()

        return redirect('auth:login')

    return render(request, 'login/signup.html')