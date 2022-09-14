from django.urls import path
from . import views


urlpatterns = [
    path(
        route='',
        view=views.main,
        name='main'),
    path(
        route='home/',
        view=views.home,
        name='home'),
    path(
        route='user/',
        view=views.user,
        name='user'),
    path(
        route='settings/',
        view=views.settings,
        name='settings'),
    path(
        route='support/',
        view=views.support,
        name='support'),
    path(
        route='comodin/',
        view=views.comodin,
        name='comodoin'),
    path(
        route='vue/',
        view=views.vue,
        name='vue'),
]
