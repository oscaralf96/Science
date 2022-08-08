from django.urls import path
from . import views


urlpatterns = [
    path(
        route='signin/',
        view=views.LoginView.as_view(),
        name='login'),


]
