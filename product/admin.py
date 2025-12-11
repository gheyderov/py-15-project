from django.contrib import admin
from .models import ProductCategory, Product, ProductTag, ProductImage

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(ProductImage)