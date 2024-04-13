from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, products, categories

app_name = CatalogConfig.name
urlpatterns = [
    path('contacts', contacts),
    path('', index, name='index'),
    path('categories', index, name='categories'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', products, name='products')
]