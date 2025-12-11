from django.shortcuts import render
from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all() # Django ORM






    context = {
        'products' : products
    }
    return render(request, 'shop.html', context)