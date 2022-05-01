from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # products urls
    path('', productList, name='products'),
    path('create', productsCreate, name='productsCreate'),
    path('modify/<int:id>', productsModify, name='productsModify'),
    path('details/<int:id>', productsDetails, name='productsDetails'),
    path('delete/<int:id>', productsDelete, name='productsDelete'),

    # categories urls``
    path('categories/create', categoriesCreate, name='categoriesCreate'),
    path('category/modify/<int:id>', categoriesModify, name='categoriesModify'),
    path('category/details/<int:id>', categoriesDetails, name='categoriesDetails'),
    path('category/delete/<int:id>', categoriesDelete, name='categoriesDelete'),
]