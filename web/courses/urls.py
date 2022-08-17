from django.urls import path
from . import views


urlpatterns = [
    path(
        route='',
        view=views.all,
        name='all'
    ),
    path(
        route='<str:science>/',
        view=views.courses,
        name='science'
    )
]
