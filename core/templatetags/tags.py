from django import template
register = template.Library()
from product.models import ProductCategory, Product


@register.simple_tag
def get_categories(limit):
    return ProductCategory.objects.all()[:limit]


@register.inclusion_tag('includes/recent-products.html')
def show_recent_products(count=3):
    products = Product.objects.order_by('-created_at')[:count]
    return {'recent_products': products} # Returns a context dictionary
