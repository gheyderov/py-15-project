from django.contrib import admin
from .models import User, BlockedIpAddress

# Register your models here.

admin.site.register(User)
admin.site.register(BlockedIpAddress)