from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

BASE_PATH = 'django_youtube_clone.apps.'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(BASE_PATH + 'account.urls')),
    path('', include(BASE_PATH + 'video.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)