from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from catalog.models import Product, Category


# Create your views here.

def index(request):
    category_name = Category.objects.all()
    context = {'object_list': category_name, 'title': 'Перечень продуктов - Главная'}

    return render(request, 'catalog/templates/index.html', context)


class CategoriesListView(ListView):
    model = Category


# def categories(request):
# context = {'object_list': Category.objects.all(), 'title': 'Все продукты'}

# return render(request, 'catalog/templates/categories.html', context)
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({email}, {phone}): {message}')
    return render(request, 'catalog/templates/contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/templates/product_list.html'
