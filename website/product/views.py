from django.shortcuts import render
from .models import ComapanyInformation, Product

def home(request):
    info = ComapanyInformation.objects.all().first()
    products = Product.objects.all()
    data = {
        'info': info,
        'products': products
    }
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')

def product(request):
    info = ComapanyInformation.objects.all().first()
    products = Product.objects.all()
    data = {
        'info': info,
        'products': products
    }
    return render(request, 'product.html', data)
