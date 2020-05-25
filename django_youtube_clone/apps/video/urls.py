from django.urls import path

from django_youtube_clone.apps.video import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('videos/upload/', views.Upload.as_view(), name='upload'),
    path('search/', views.Search.as_view(), name='search'),
    path('videos/<int:id>/edit', views.EditVideo.as_view(), name='edit_video'),
    path('videos/<int:pk>/', views.VideoDetail.as_view(), name='video_detail'),
    path('videos/<int:pk>/delete', views.DeleteVideo.as_view(), name='delete_video'),
]
