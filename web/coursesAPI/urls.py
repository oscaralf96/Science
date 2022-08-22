from django.urls import path
from . import views


urlpatterns = [
    path(
        route='list/',
        view=views.api_courses_list,
        name='api_sciences'
    ),
    path(
        route='asign_course/',
        view=views.api_asign_course,
        name='api_asign_course'
    ),
]
