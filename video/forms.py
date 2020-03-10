from django.forms import Form, ModelForm

from video.models import Video


class UploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ['video_file', 'title', 'description']


class EditVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description']
