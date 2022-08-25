# Django
import re
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
from rest_framework.response import Response

# utils
from science.settings import SERVER_URL
import requests


# Create your views here.

@api_view(["GET"])
def courses_list(request):
    if request.method == 'GET':
        sciences = Science.objects.all()
        serializer = ScienceSerializer(sciences, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

     
@api_view(["GET"]) 
def asignations(request):
    if request.method == 'GET':
        #if request.GET:
        query_set  = dict(**request.GET)
        if 'user' in query_set.keys():
            query_set['user'] = int(query_set['user'][0])
        if 'course' in query_set.keys():
            query_set['course'] = int(query_set['course'][0])
        asignations = Asignation.objects.filter(**query_set)
        serializer = AsignationSerializer(asignations, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)


@api_view(["POST"])
@csrf_exempt
def new_asignation(request, course):
    if request.method == 'POST':
        serializer = AsignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["DELETE", "GET", "PUT"])
@csrf_exempt
def asignation(request, pk):
    if request.method == 'GET':
        asignation = Asignation.objects.get(pk=pk)
        serializer = AsignationSerializer(asignation)
        return Response(serializer.data)

    if request.method == 'PUT':
        asignation = Asignation.objects.get(pk=pk)
        serializer = AsignationSerializer(asignation, data=request.data['ids'])
        if serializer.is_valid():
            serializer.save(**request.data['new_data'])
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        serializer = AsignationSerializer(data=request.data)
        if serializer.is_valid():
            course = Course.objects.get(pk=request.data['course'])
            user = User.objects.get(pk=request.data['user'])
            Asignation.objects.get(course=course, user=user).delete()
            # return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
    
    return Response(serializer.data)
