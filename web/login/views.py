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

# Forms
from .forms import SignupForm
from django import forms

# Create your views here.
class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'auth/login.html'


@login_required
def logout_view(request):
    logout(request)
    return redirect('auth:login')

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('auth:login')
        print(form.errors.get('__all__')[0])
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='auth/signup.html',
        context={
            'form': form, 
        }
    ) 