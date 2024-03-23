from django.shortcuts import render


# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'catalog/templates/home.html')


def contact(request):
    if request.method == 'POST':
        visiter = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)
    return render(request, 'catalog/templates/contact.html')
