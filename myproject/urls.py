from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'home.html'), name='home'),

    path('users/', include('users.urls')),
    path('diary/', include('diary.urls')),
    path('events/', include('events.urls')),

    path('materials/', include('materials.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
