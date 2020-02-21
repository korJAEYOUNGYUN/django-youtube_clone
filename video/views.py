from django.shortcuts import render
from django.views.generic import ListView

from video.models import Video


class Home(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'home.html'
