from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from django_youtube_clone.apps.api import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]