from rest_framework import serializers

from .models import Science, Asignation

class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ['name', 'image']


class AsignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignation
        fields = ['user', 'course']