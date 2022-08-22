# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now, localtime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# models
from django.contrib.auth.models import User
from courses.models import Science, Course, Asignation

# serializers
from courses.serializers import ScienceSerializer, AsignationSerializer

# Django Rest Framework
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# utils
from science.settings import SERVER_URL
import requests


# Create your views here.

def api_courses_list(request):
    """
    List all sciences available, or create a new snippet.
    """
    if request.method == 'GET':
        sciences = Science.objects.all()
        serializer = ScienceSerializer(sciences, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(["POST", "DELETE"])
@csrf_exempt
def api_asign_course(request):
    if request.method == 'POST':
        serializer = AsignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        print('delete')
        print(request.data)
        serializer = AsignationSerializer(data=request.data)
        if serializer.is_valid():
            course = Course.objects.get(pk=request.data['course'])
            user = User.objects.get(pk=request.data['user'])
            Asignation.objects.get(course=course, user=user).delete()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
