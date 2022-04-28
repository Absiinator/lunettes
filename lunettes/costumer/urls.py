from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', costumersList, name='costumers'),
    path('create', costumersCreate, name='costumersCreate'),
    path('modify/<int:id>', costumersModify, name='costumersModify'),
    path('details/<int:id>', costumersDetails, name='costumersDetails'), 
    path('delete/<int:id>', costumersDelete, name='costumersDelete'),
]