from django.shortcuts import render
from catalog.models import Product, Category


# Create your views here.
def index(request):
    category_name = Category.objects.all()
    context = {'object_list': category_name, 'title': 'Перечень продуктов - Главная'}

    return render(request, 'catalog/templates/index.html', context)


def categories(request):
    product_name = Product.objects.all()
    context = {'product_list': product_name, 'title': 'Все продукты'}

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
    context = {'object_list': Product.objects.filter(pk=pk), 'title': 'Описание товара'}
    return render(request, 'catalog/templates/products.html', context)
