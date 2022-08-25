from django.urls import path
from . import views


urlpatterns = [
    path(
        route='science/',
        view=views.areas,
        name='areas'
    ),
    path(
        route='show/<str:area>/',
        view=views.courses,
        name='science'
    ),
    path(
        route='asign_course/',
        view=views.asign_course,
        name='asign_course'
    ),
    path(
        route='remove_course/',
        view=views.update_course,
        name='remove_course'
    ),
]
