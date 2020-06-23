from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

BASE_PATH = 'django_youtube_clone.apps.'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(BASE_PATH + 'account.urls')),
    path('', include(BASE_PATH + 'video.urls')),
    path('api/', include(BASE_PATH + 'api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)