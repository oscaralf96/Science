from django.urls import path
from . import views


urlpatterns = [
    path(
        route='science/',
        view=views.all,
        name='all'
    ),
    path(
        route='show/<str:science>/',
        view=views.courses,
        name='science'
    ),
    path(
        route='asign_course/',
        view=views.asign_course,
        name='asign_course'
    ),
    path(
        route='api/list/',
        view=views.api_courses_list,
        name='api_sciences'
    ),
    path(
        route='api/asign_course/',
        view=views.api_asign_course,
        name='api_asign_course'
    )
]
