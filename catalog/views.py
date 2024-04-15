from django.shortcuts import render
from catalog.models import Product, Category


# Create your views here.
def index(request):
    category_name = Category.objects.all()
    context = {'object_list': category_name, 'title': 'Перечень продуктов - Главная'}

    return render(request, 'catalog/templates/index.html', context)


def categories(request):

    context = {'object_list': Category.objects.all(), 'title': 'Все продукты'}

    return render(request, 'catalog/templates/categories.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({email}, {phone}): {message}')
    return render(request, 'catalog/templates/contacts.html')


def products(request, pk):
    product_category = Category.objects.get(pk=pk)
    context = {'object_list': Product.objects.filter(product_category_id=pk), 'title': f'Описание товара {product_category.name}'}
    return render(request, 'catalog/templates/products.html', context)
