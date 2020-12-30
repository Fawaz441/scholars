
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('boss1/', admin.site.urls),
    path('user/',include('users.urls')),
    path('utils/',include('utils.urls')),
    path('',include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)