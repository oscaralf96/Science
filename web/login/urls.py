from django.urls import path
from . import views


urlpatterns = [
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=views.signup,
        name='signup'),


]
