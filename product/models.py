from django.db import models
from core.models import AbstracModel
# from account.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class ProductTag(AbstracModel):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class ProductCategory(AbstracModel):

    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title
    

class Product(AbstracModel):
    category = models.ForeignKey(ProductCategory, related_name= 'products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(ProductTag, related_name='products')

    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='product_images/', null=True, blank=True)


    def __str__(self):
        return f'{self.category.title} / {self.title}'
    

class ProductImage(AbstracModel):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
    

class ProductReview(AbstracModel):

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)

    message = models.TextField()

    def __str__(self):
        return self.product.title
    

