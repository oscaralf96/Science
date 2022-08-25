from django.urls import path
from . import views


urlpatterns = [
    path(
        route='areas/list/',
        view=views.courses_list,
        name='api_sciences'
    ),
    path(
        route='course/<int:course>/asignation/',
        view=views.new_asignation,
        name='api_new_asignation'
    ),
    path(
        route='<int:pk>/asignation/',
        view=views.asignation,
        name='apias_asignation'
    ),
    path(
        route='asignations/',
        view=views.asignations,
        name='api_asignations'
    ),
]
