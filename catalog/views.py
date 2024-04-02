from django.shortcuts import render
from catalog.models import Product


# Create your views here.
def home(request):
    product_list = Product.objects.all()
    context = {'object_list': product_list, 'title': 'Перечень товаров'}

    return render(request, 'catalog/templates/home.html', context)


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
