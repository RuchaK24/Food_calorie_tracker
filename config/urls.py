from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# This is the main urls.py file for the project. It is telling Django to look for urls in the
# foodtracker app.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodtracker.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)