from django.contrib import admin

from .models import *

# Register your models here.



@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass