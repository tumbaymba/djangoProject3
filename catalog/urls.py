from django.urls import path

import catalog
from catalog.apps import CatalogConfig
from catalog.views import index, ProductListView, CategoriesListView, contacts

app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', contacts, contacts),
    path('', index, name='index'),
    path('categories/', CategoriesListView.as_view, name='categories'),
    #path('products/', products, name='products'),
    path('products/<int:pk>/', ProductListView.as_view, name='products'),
    #path('catalog/<int:pk>/', catalog, name='catalog'),
]
