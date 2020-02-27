from django.urls import path

from video.views import Upload, Search, VideoDetail, EditVideo, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('videos/upload/', Upload.as_view(), name='upload'),
    path('search/', Search.as_view(), name='search'),
    path('videos/<int:id>/', VideoDetail.as_view(), name='video_detail'),
    path('videos/<int:id>/edit', EditVideo.as_view(), name='edit_video'),
    # path('<int:id>/delete', DeleteVideo.as_view(), name='delete_video'),
]
