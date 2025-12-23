from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField('phone', max_length=50, null=True, blank=True)
    email = models.EmailField("email address")