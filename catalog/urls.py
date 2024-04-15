from django.urls import path

import catalog
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, products, categories

app_name = CatalogConfig.name
urlpatterns = [
    path('contacts', contacts),
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    #path('products/', products, name='products'),
    path('products/<int:pk>/', products, name='products'),
    #path('catalog/<int:pk>/', catalog, name='catalog'),
]
