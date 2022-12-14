
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime

# models
from django.contrib.auth.models import User
from users.models import Profile
from courses.models import Asignation, Course



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
    user = request.user
    try:
        profile = user.profile
    except:
        profile = None
    asignated_curses = Asignation.objects.filter(user=user.id)
    
    return render(
        request=request, 
        template_name='home/content/user.html', 
        context={
            'asignated_curses': asignated_curses
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

def vue(request):
    return render(
        request=request, 
        template_name='vue/vue.html', 
        context={
        }
    )
    