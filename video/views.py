from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from video.models import Video


class Home(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'home.html'


class Search(ListView):
    queryset = Video.objects.all()
    context_object_name = 'video_list'
    template_name = 'search.html'


class EditVideo(TemplateView):
    template_name = 'edit_video.html'


class Upload(TemplateView):
    template_name = 'upload.html'


class VideoDetail(TemplateView):
    template_name = 'video_detail.html'


# class DeleteVideo(TemplateView):
#     pass