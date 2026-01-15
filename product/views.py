from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from product.forms import ReviewForm
from django.urls import reverse_lazy

# Create your views here.

class ShopListView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 2
    # queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        if cat_id:
            queryset = queryset.filter(category = cat_id)
        if tag_id:
            queryset = queryset.filter(tags = tag_id)
        if cat_id and tag_id:
            queryset = queryset.filter(category = cat_id, tags = tag_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(parent = None)
        return context


def shop(request):
    products = Product.objects.all() # Django ORM 
    categories = ProductCategory.objects.filter(parent = None)

    context = {
        'products' : products,
        'categories' : categories
    }
    return render(request, 'shop.html', context)


class ShopDetailView(FormMixin, DetailView):
    form_class = ReviewForm
    model = Product # product
    template_name = 'shop-detail.html'
    success_url = reverse_lazy('home')
    # context_object_name = 'productt'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        product = self.get_object()
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.product = product
            form.save()
        return self.get(request, *args, **kwargs)


def shop_detail(request, pk):
    # product = Product.objects.get(id = pk) # Select * from Product where id = pk
    product = get_object_or_404(Product, id = pk)

    context = {
        'product' : product
    }

    return render(request, 'shop-detail.html', context)