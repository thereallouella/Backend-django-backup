"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from accounts.views import FilesViewSets
from accounts.views import activate
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('djoser.social.urls')),
    re_path(r'^activation/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', activate, name='activate'),
    path('api/v1/files/', FilesViewSets.as_view({'get': 'list', 'post': 'create'}), name='files'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
