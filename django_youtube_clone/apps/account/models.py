from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # User has username, email, password fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/avatars/', default='uploads/avatars/no_avatar.png')

    def __str__(self):
        return self.user.username
