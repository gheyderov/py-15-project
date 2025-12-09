from django.db import models

# Create your models here.

class ProductCategory(models.Model):

    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.title
    

class Product(models.Model):

    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, related_name= 'products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.title} / {self.title}'