from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from selectel_test import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jokes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)