from django.forms import Form, ModelForm

from video.models import Video


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = [video_title]