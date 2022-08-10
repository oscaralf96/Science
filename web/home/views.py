
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def main(request):
    
    return render(request, template_name='home/base.html')