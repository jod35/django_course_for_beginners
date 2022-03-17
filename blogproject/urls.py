from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from blogproject.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('posts.urls')),
    path('auth/',include('users.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
