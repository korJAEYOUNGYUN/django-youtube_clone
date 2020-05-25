from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'yuntube',
        'USER': 'jaeyoung',
        'PASSWORD': '0000'
    }
}