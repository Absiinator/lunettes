from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('imports/', Import_database, name='import_database'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)