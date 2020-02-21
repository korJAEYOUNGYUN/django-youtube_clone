from django.urls import path


urlpatterns = [
    path('<int:id>/'),
    path('edit-profile/'),
    path('change-password/')
]
