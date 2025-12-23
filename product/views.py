from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all() # Django ORM 

    context = {
        'products' : products,
    }
    return render(request, 'shop.html', context)


def shop_detail(request, pk):
    # product = Product.objects.get(id = pk) # Select * from Product where id = pk
    product = get_object_or_404(Product, id = pk)

    context = {
        'product' : product
    }

    return render(request, 'shop-detail.html', context)