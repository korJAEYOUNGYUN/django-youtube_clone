from django.urls import path


urlpatterns = [
    path('upload/'),
    path('<int:id>/'),
    path('<int:id>/edit'),
    path('<int:id>/delete')
]
