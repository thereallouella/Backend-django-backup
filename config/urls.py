from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from accounts.views import ListingViewSet
from accounts.views import activate
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('djoser.social.urls')),
    re_path(r'^activation/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', activate, name='activate'),
    path('api/v1/listings/', ListingViewSet.as_view({'get': 'list', 'post': 'create'}), name='listings'),
    # listing with user_id
    path('api/v1/listings/<int:user_id>/', ListingViewSet.as_view({'get': 'list'}), name='listings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
