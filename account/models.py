from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from core.models import AbstracModel

# Create your models here.

class User(AbstractUser):
    phone = models.CharField('phone', max_length=50, null=True, blank=True)
    email = models.EmailField("email address")
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    ips = ArrayField(models.GenericIPAddressField(), null=True, blank=True)

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return '/static/images/profile.jpg'
        

class BlockedIpAddress(AbstracModel):
    ip_address = models.GenericIPAddressField()