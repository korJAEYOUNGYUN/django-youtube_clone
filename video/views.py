from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, FormView

from video import forms
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


class Upload(LoginRequiredMixin, FormView):
    template_name = 'upload.html'
    form_class = forms.UploadForm

    def form_valid(self, form):
        user = self.request.user.profile
        video_file = form.files['video_file']
        title = form.data['title']
        description = form.data['description']

        video = Video(video_file=video_file, title=title, description=description, creator=user)
        video.save()

        return redirect(reverse('video_detail', args=(video.id,)))


class VideoDetail(DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'video_detail.html'



# class DeleteVideo(LoginRequiredMixin, TemplateView):
#     pass