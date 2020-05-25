from django.db import models


class Video(models.Model):
    video_file = models.FileField(upload_to='uploads/videos/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    views = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('account.Profile', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    author = models.ForeignKey('account.Profile', on_delete=models.CASCADE)