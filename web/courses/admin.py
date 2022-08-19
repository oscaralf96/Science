from django.contrib import admin

from .models import *

# Register your models here.



@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

@admin.register(Asignation)
class AsignationAdmin(admin.ModelAdmin):
    """Asignation Admin display"""

    list_display = ('course', 'user', 'created', 'modified', 'active')
    #list_display_links = ('course', 'user')
    list_editable = []
    list_filter = (
        'active',
        'user__is_staff',
        'created',
        'modified',
    )