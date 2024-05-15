from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views_2 import CategoryDetailView, ProductListView, CategoriesListView, ContactsView, ProductDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='products'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
