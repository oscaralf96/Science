
# Django
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime

# models
from django.contrib.auth.models import User
from .models import Science, Course


# Create your views here.

    
@login_required()
def all(request):   

    sciences = Science.objects.all()

    return render(
        request=request, 
        template_name='home/content/courses.html', 
        context={
            'now': now(),
            'sciences': sciences
        }
    )

    
def courses(request, science):   

    courses = Course.objects.filter(science=Science.objects.get(name=science))

    return render(
        request=request, 
        template_name='home/content/courses_category.html', 
        context={
            'now': now(),
            'courses': courses,
            'science': science
        }
    )
    