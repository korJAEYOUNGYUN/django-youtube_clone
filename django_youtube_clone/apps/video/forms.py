from django.forms import Form, ModelForm, CharField

from django_youtube_clone.apps.video.models import Video


class UploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']


class EditVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description']


class AddCommentForm(Form):
    comment = CharField(max_length=128, label='Add a comment')
