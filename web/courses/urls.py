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
        route='remove_course/',
        view=views.remove_course,
        name='remove_course'
    ),
]
