from django.shortcuts import render
from django.views.generic import ListView, DetailView
from catalog.models import Product, Category, Contacts, Version


# Create your views here.

def index(request):
    category_name = Category.objects.all()
    context = {'object_list': category_name, 'title': 'Перечень продуктов - Главная'}

    return render(request, 'catalog/category_list.html', context)


class CategoryDetailView(DetailView):
    model = Category


class CategoriesListView(ListView):
    model = Category


class ContactsView(ListView):
    model = Contacts

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}, Phone: {phone}, Message: {message}')
        return super().get(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/templates/templates/catalog/product_list.html'


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_data = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_data.pk
        context_data['title'] = f'{category_data.name}'
        for product in context_data.get('object_list'):
            product.version = product.version_set.filter(is_active=True).first()
            return context_data
