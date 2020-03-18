from django.forms import Form, ModelForm, CharField

from video.models import Video, Comment


class UploadForm(ModelForm):
    class Meta:
        model = Video
        fields = ['video_file', 'title', 'description']


class EditVideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description']


class AddCommentForm(Form):
    comment = CharField(max_length=128, label='Add a comment')
