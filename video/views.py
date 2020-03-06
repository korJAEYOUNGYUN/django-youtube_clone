from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from video.models import Video


class Home(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'home.html'


class Search(ListView):
    context_object_name = 'video_list'
    template_name = 'search.html'

    def get_queryset(self):
        self.searching_by = self.request.GET['searching_by']
        video_list = Video.objects.filter(title__contains=self.searching_by)
        return video_list

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['searching_by'] = self.searching_by
        return super(Search, self).get_context_data(**kwargs)


# 비디오 creator와 유저가 일치하는지 확인해야함
class EditVideo(LoginRequiredMixin, TemplateView):
    template_name = 'edit_video.html'


class Upload(LoginRequiredMixin, TemplateView):
    template_name = 'upload.html'


class VideoDetail(DetailView):
    context_object_name = 'video'
    template_name = 'video_detail.html'

    def get_queryset(self):
        video_id = self.kwargs['id']
        video = get_object_or_404(Video, id=video_id)
        return video


# class DeleteVideo(LoginRequiredMixin, TemplateView):
#     pass