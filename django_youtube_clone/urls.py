from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('join/'),
    path('login/'),
    path('logout/'),
    path('search/'),
    path('user/', include('account.urls')),
    path('video/', include('video.urls'))
]
