from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views
from rest_framework import routers

from jokes.views import JokeViewSet
from selectel_test import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jokes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

# # Создаем router и регистрируем наш ViewSet
# router = routers.DefaultRouter()
# router.register(r'jokes', JokeViewSet)
# # URLs настраиваются автоматически роутером
# urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)