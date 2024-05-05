from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from catalog.models import Product, Category, Contacts


# Create your views here.

def index(request):
    category_name = Category.objects.all()
    context = {'object_list': category_name, 'title': 'Перечень продуктов - Главная'}

    return render(request, 'catalog/category_list.html', context)


class CategoryDetailView(DetailView):
    model = Category


class CategoriesListView(ListView):
    model = Category


# def categories(request):
# context = {'object_list': Category.objects.all(), 'title': 'Все продукты'}

# return render(request, 'catalog/templates/categories.html', context)
'''def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({email}, {phone}): {message}')
    return render(request, 'catalog/templates/contacts_list.html')'''


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
    template_name = 'catalog/templates/product_list.html'


class ProductDetailView(DetailView):
    model = Product
