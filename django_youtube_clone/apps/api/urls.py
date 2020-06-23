from django.urls import path

from django_youtube_clone.apps.api import views


urlpatterns = [
    path('login', views.UserLoginAPI.as_view(), name='login_api')
]