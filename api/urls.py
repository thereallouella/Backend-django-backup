
from django.urls import path, include
from rest_framework import routers

from accounts.views import FilesViewSets

urlpatterns = [
    path('accounts/', include('djoser.urls')),
    path('accounts/', include('djoser.urls.authtoken')),
]
