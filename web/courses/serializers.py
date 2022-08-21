from rest_framework import serializers

from .models import Science, Asignation, Course
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CoursreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ['name', 'image']


class AsignationSerializer(serializers.ModelSerializer):
    # user = serializers.Int

    class Meta:
        model = Asignation
        fields = ['id','active',  'user', 'course']

        def to_representation(self, instace):
            self.fields['user'] = UserSerializer(read_only=True)