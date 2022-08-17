
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime

# models
from django.contrib.auth.models import User
from users.models import Profile



# Create your views here.

@login_required()
def main(request):    
    return render(
        request=request, 
        template_name='home/main.html', 
        context={
        }
    )

    
@login_required()
def home(request):    
    return render(
        request=request, 
        template_name='home/content/home.html', 
        context={
        }
    )    

    
@login_required()
def user(request): 
    try:
        profile = request.user.profile
    except:
        profile = None

    return render(
        request=request, 
        template_name='home/content/user.html', 
        context={
        }
    )
    
@login_required()
def settings(request):    
    return render(
        request=request, 
        template_name='home/content/settings.html', 
        context={
        }
    )

    
@login_required()
def support(request):    
    return render(
        request=request, 
        template_name='home/content/support.html', 
        context={
        }
    )


@login_required()
def comodin(request):    
    return render(
        request=request, 
        template_name='home/content/comodin.html', 
        context={
        }
    )

    