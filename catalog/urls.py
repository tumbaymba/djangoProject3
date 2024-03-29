from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contact, products

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('<int:pk>/products/', products, name='products')
]