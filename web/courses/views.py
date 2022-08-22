# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime
from django.http import HttpResponse, JsonResponse

# models
from django.contrib.auth.models import User
from .models import Science, Course, Asignation

# utils
from science.settings import SERVER_URL
import requests

# Create your views here.
    
@login_required()
def all(request):   
    endpoint = "http://web:8000/coursesAPI/list/"
    sciences = requests.get(endpoint).json()

    return render(
        request=request, 
        template_name='home/content/courses.html', 
        context={
            'now': now(),
            'sciences': sciences
        }
    )
       
@login_required()
def asign_course(request):   
    endpoint = "http://web:8000/coursesAPI/asign_course/"
    data = {
        'course': Course.objects.get(name=request.GET['course']).id,
        'user': User.objects.get(username=request.user.username).id,
    }
    post = requests.post(endpoint,json=data)

    return redirect('home:user')
       
@login_required()
def remove_course(request):   
    endpoint = "http://web:8000/coursesAPI/asign_course/"
    data = {
        'course': Course.objects.get(name=request.GET['course']).id,
        'user': User.objects.get(username=request.user.username).id,
    }
    post = requests.delete(endpoint,json=data)

    return redirect('home:user')
    
def courses(request, science):   
    science_id = Science.objects.get(name=science).id
    #courses = Course.objects.filter(science=Science.objects.get(name=science))
    courses_active_asignation = Course.objects.raw(
        f"""select * from (
            select id, name, logo, difficulty 
            from courses_course
            where science_id={science_id}
            ) as c 
            left join (
                select course_id, active 
                from courses_asignation 
                where user_id = {request.user.pk}
                ) as a 
            on c.id = a.course_id;
        """
    )
    

    return render(
        request=request, 
        template_name='home/content/courses_category.html', 
        context={
            'now': now(),
            'courses': courses,
            'science': science,
            'active_asignation': courses_active_asignation
        }
    )
    
