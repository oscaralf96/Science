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
def areas(request):   
    endpoint = "http://web:8000/api/areas/list/"
    areas = requests.get(endpoint).json()

    return render(
        request=request, 
        template_name='home/content/areas.html', 
        context={
            'now': now(),
            'areas': areas
        }
    )
       
@login_required()
def asign_course(request):   
    course = int(request.GET['course'])
    user = User.objects.get(username=request.user.username).id
    asignation = Asignation.objects.filter(course=course, user=user)
    if asignation.exists():
        asignation = asignation[0]
        endpoint = f"http://web:8000/api/{asignation.id}/asignation/"
        
        data = {
            'new_data': {
                'active': True
            },
            'ids':{
                'course': course,
                'user': user,
            }        
        }

        post = requests.put(endpoint,json=data)

    else:
        endpoint = f"http://web:8000/api/course/{course}/asignation/"

        data = {
            'course': int(request.GET['course']),
            'user': user,
        }

        post = requests.post(endpoint,json=data)

    return redirect('home:user')
       
@login_required()
def update_course(request):   
    course: int = int(request.GET['course'])
    user = User.objects.get(username=request.user.username).id
    asignation = Asignation.objects.get(course=course, user=user)

    endpoint = f"http://web:8000/api/{asignation.id}/asignation/"

    data = {
        'new_data': {
            'active': False
        },
        'ids':{
            'course': course,
            'user': user,
        }        
    }
    post = requests.put(endpoint,json=data)

    return redirect('home:user')
    
@login_required()
def remove_course(request):   
    course = int(request.GET['course'])
    endpoint = f"http://web:8000/api/{course}/asignation/"
    data = {
        'course': course,
        'user': User.objects.get(username=request.user.username).id,
    }
    post = requests.delete(endpoint,json=data)

    return redirect('home:user')
    
def courses(request, area):   
    area_id = Science.objects.get(name=area).id
    courses_active_asignation = Course.objects.raw(
        f"""select * from (
            select id, name, logo, difficulty 
            from courses_course
            where science_id={area_id}
            ) as c 
            left join (
                select course_id, active
                from courses_asignation 
                where user_id = {request.user.pk}
                ) as a 
            on c.id = a.course_id;
        """
    )
    # case when active=false then cast(1 as bit) when active=true then cast (0 as bit) end as active 
    

    return render(
        request=request, 
        template_name='home/content/courses.html', 
        context={
            'now': now(),
            'courses': courses,
            'area': area,
            'active_asignation': courses_active_asignation
        }
    )
    
