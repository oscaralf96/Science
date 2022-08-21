
# Django
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime
from django.http import HttpResponse, JsonResponse

# models
from django.contrib.auth.models import User

from .serializers import ScienceSerializer, AsignationSerializer
from .models import Science, Course, Asignation

from science.settings import SERVER_URL
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.

def api_courses_list(request):
    """
    List all sciences available, or create a new snippet.
    """
    if request.method == 'GET':
        sciences = Science.objects.all()
        serializer = ScienceSerializer(sciences, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
@csrf_exempt
def api_asign_course(request):
    if request.method == 'POST':
        serializer = AsignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    
@login_required()
def all(request):   
    endpoint = "http://web:8000/courses/api/list/"
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
    endpoint = "http://web:8000/courses/api/asign_course/"
    # print(course)
    data = {
        'course': request.GET['course'],
        'user': request.user.username
    }
    post = requests.post(endpoint,json=data)
    print(data)
    print(post)

    return redirect('courses:all')
    
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
    
