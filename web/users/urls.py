from django.urls import path
from . import views


urlpatterns = [
    path(
        route='update_profile/',
        view=views.update_profile,
        name='update_profile'),
]
